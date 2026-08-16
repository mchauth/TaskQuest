#!/usr/bin/env python3
"""TWENTY-NINTH net-new-geometry axis for ALL FOUR SLOTS — the HOUNDSTOOTH / DOGTOOTH /
BROKEN-CHECK family: an all-over two-tone field of interlocking JAGGED four-pointed "broken
check" cells produced by the classic color-and-weave effect of a 2/2 twill woven from bands of
4 dark + 4 light warp and weft. Each cell is a solid pointed hook that notches into its
neighbours — the unmistakable dogtooth silhouette of high-fashion cloth. The repeated motif is
the INTERLOCKING JAGGED BROKEN-CHECK produced by a color-and-weave twill; none of the
twenty-eight existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> lozenge OUTLINE / diamond MESH (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS -> imbricated scale field
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone / twill
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th CHECKER of perpendicular SHORT-THREAD bundles alternating dir -> basketweave
  * 19th tessellation of SIX-sided OUTLINE cells -> honeycomb
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE OUTLINES -> chainmail rings
  * 22nd CONTINUOUS UNDULATING SINE lines -> watered-steel ripple
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th CONTINUOUS CURVED COILS winding around centres -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID (smooth lozenges) -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE point -> sunburst / compass
  * 28th STACKS NESTED CLOSED RINGS at growing radius around a shared CENTRE -> target
  * 29th (this) INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill -> houndstooth.
Critically distinct from the 25th argyle (the only other SOLID-FILL axis): argyle fills SMOOTH
straight-edged DIAMOND lozenges on a clean diagonal checker; houndstooth cells are JAGGED —
each solid shape throws pointed teeth that HOOK into the adjacent cell, an interlocking notched
tessellation, not smooth lozenges. Distinct from the 16th twill / herringbone (short parallel
diagonal DASHES that never close into shapes) — houndstooth is a closed AREA fill of broken
checks. Distinct from the 18th basketweave (perpendicular thread bundles in a plain checker
with straight edges) — houndstooth breaks every check with diagonal hooks. Distinct from the
26th tartan (crossing continuous bands over a ground) — houndstooth has no continuous bands,
only tessellating hooked cells. Second and last SOLID-FILL axis, deliberately paired against
argyle as its jagged foil.

Per slot it lands as the 29th distinct axis:
  * CHEST  — houndstooth cuirass: broken-check field over the whole cuirass.
  * LEGS   — houndstooth chausses: broken-check field over the thighs.
  * BOOTS  — houndstooth sabatons: broken-check field over the boot.
  * HELMET — houndstooth dome: broken-check field over the whole crown.

Construction is the genuine textile one: color-and-weave over a 2/2 twill.  For each opaque body
pixel, in component-local coords (lx, ly) anchored at the component bbox top-left:
    warp_on_top = ((lx - ly) mod 4) < 2         # 2/2 twill interlacement
    warp_is_dark = (lx mod 8) < 4               # warp banded 4 dark / 4 light
    weft_is_dark = (ly mod 8) < 4               # weft banded 4 dark / 4 light
    pixel_is_dark = warp_is_dark if warp_on_top else weft_is_dark
This is exactly how houndstooth is woven, so the emergent broken-check is authentic rather than
faked. Anchoring to the component bbox keeps the weave stable frame-to-frame.

Authoring philosophy is identical to gen_concentric_axis28.py / gen_sunburst_axis27.py: every
textile pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never
adds a pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed,
or accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60, lying
down) get a plain body recolor only — no weave. Shading applied in this script via shade(); do
NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 25th argyle (jewel body + gold diamond) and the
28th concentric (burnished metal target-work) the houndstooth family is a fine TWO-TONE woven
cloth — classic couture dogtooth — with a dark ground and a light tooth. The tone pair
distinguishes class:
  * warrior — jet-black ground + bone-white tooth (iconic monochrome dogtooth)
  * mage    — deep-violet ground + pale-lilac tooth (arcane houndstooth)
  * ranger  — deep-forest ground + oat-cream tooth (woodland houndstooth)

Run from repo root:
  python3 scripts/gen_houndstooth_axis29.py
Then QA (examples):
  python3 scripts/sprite_qa.py _houndstooth_legendary_preview/shirt_warrior_legendary29.png
  python3 scripts/sprite_qa.py _houndsdome_helmet_preview/helmet_mage_legendary29.png --y-min 2
  python3 scripts/sprite_qa.py _houndstooth_boots_preview/boots_warrior_legendary_houndstooth.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Houndstooth color-and-weave constants.
BAND = 4        # warp/weft colour-band width (4 dark + 4 light => 8px repeat)
REPEAT = 2 * BAND
TWILL = 4       # 2/2 twill period ( (lx-ly) mod 4 < 2 -> warp on top )

# Per-class tone pair: (DARK ground, LIGHT tooth).
SEAM = {
    'warrior': ((26, 24, 30), (226, 220, 208)),    # jet ground, bone tooth
    'mage':    ((52, 38, 84), (214, 204, 236)),     # deep-violet ground, pale-lilac tooth
    'ranger':  ((28, 48, 34), (206, 204, 166)),     # deep-forest ground, oat tooth
}

# Per-class body tones for pixels OUTSIDE the woven component (e.g. raised arms) — a plain
# mid recolor so those pixels still read as the same garment. (deep shadow / base / highlight)
BODY = {
    'warrior': ((70, 66, 74), (120, 114, 122), (176, 170, 178)),
    'mage':    ((78, 66, 108), (120, 106, 152), (170, 158, 196)),
    'ranger':  ((60, 78, 62), (104, 122, 100), (156, 172, 148)),
}

# One config block per slot. `largest` restricts the woven field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs weave all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_houndstooth_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary29', largest=True,
    ),
    'legs': dict(
        outdir='_houndstooth_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary29', largest=False,
    ),
    'boots': dict(
        outdir='_houndstooth_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_houndstooth', largest=False,
    ),
    'helmet': dict(
        outdir='_houndsdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary29', largest=True,
    ),
}


def load_any(fname):
    """Load a source sheet; if the female (_f) variant is absent (warrior boots are a
    single gender-shared sheet), fall back to the base sheet."""
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_houndstooth(fr, comp, dark, light):
    """Paint the genuine houndstooth color-and-weave onto one component. For each opaque body
    pixel, in component-local coords (lx, ly) anchored at the component bbox top-left:
        warp_on_top  = ((lx - ly) mod 4) < 2      2/2 twill interlacement
        warp_is_dark = (lx mod 8) < 4             warp banded 4 dark / 4 light
        weft_is_dark = (ly mod 8) < 4             weft banded 4 dark / 4 light
        is_dark      = warp_is_dark if warp_on_top else weft_is_dark
    Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        warp_on_top = ((lx - ly) % TWILL) < 2
        if warp_on_top:
            is_dark = (lx % REPEAT) < BAND
        else:
            is_dark = (ly % REPEAT) < BAND
        put(fr, yy, xx, dark if is_dark else light)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    dark, light = SEAM[cls]
    largest = cfg['largest']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        if fi >= 60:                            # sleep: body only
            continue
        if largest:
            lbl, n = ndimage.label(a)
            if n >= 1:
                sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
                comp = (lbl == (int(np.argmax(sizes)) + 1))
            else:
                comp = a
        else:
            comp = a
        draw_houndstooth(fr, comp, dark, light)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                arr = shade(arr, adj_min=-0.20, adj_max=0.25)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                Image.fromarray(arr).save(dst)
                print('wrote %-56s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
