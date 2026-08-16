#!/usr/bin/env python3
"""TWENTY-SIXTH net-new-geometry axis for ALL FOUR SLOTS — the TARTAN / PLAID / SETT family:
an all-over field of CROSSING FULL-LENGTH ORTHOGONAL BANDS — bold vertical bands and bold
horizontal bands laid over the whole body SIMULTANEOUSLY — with a distinct BRIGHTER THIRD
TONE painted at every crossing NODE (the woven "sett"), plus a thin single-pixel over-check
guard line midway between the bold bands. The repeated motif is the THREE-LEVEL WOVEN
CROSSING: body / single-band / brighter overlap-node. This crossing-band-with-overlap-tone
geometry is occupied by none of the twenty-five existing legendary axes per slot:
  * 11th laid CONTINUOUS STRAIGHT VERTICAL parallel lines ONLY (fluting)
  * 12th laid CONTINUOUS STRAIGHT HORIZONTAL parallel lines ONLY (lamellar bands)
  * 13th laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th laid TWO crossing STRAIGHT DIAGONAL families -> lozenge OUTLINE / diamond MESH
  * 15th laid OVERLAPPING SHORT CURVED ARCS -> imbricated scale field
  * 16th laid SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone/twill
  * 17th laid a STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th laid a CHECKER of perpendicular SHORT-THREAD bundles alternating direction
           per tile -> basketweave (over-under weave, NO overlap tone)
  * 19th laid a tessellation of SIX-sided OUTLINE cells -> honeycomb
  * 20th laid THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st laid a staggered grid of closed CIRCLE OUTLINES -> chainmail rings
  * 22nd laid CONTINUOUS UNDULATING SINE lines -> watered-steel ripple
  * 23rd laid a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th laid CONTINUOUS CURVED COILS winding around centres -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th (this) CROSSES BOLD ORTHOGONAL BANDS with a BRIGHTER OVERLAP NODE -> tartan / sett.
Critically distinct from the 11th fluting and 12th lamellar: those are SINGLE-DIRECTION line
families; tartan lays BOTH the vertical and horizontal bold bands over the whole body at once
AND introduces a THIRD brighter tone at every crossing node — a multi-level woven check, not
a one-direction line field. Distinct from the 18th basketweave: basketweave alternates thread
DIRECTION per checker tile (only horizontal OR only vertical threads in any one tile, no
overlap tone); tartan runs continuous full-length bands in BOTH directions everywhere with a
distinct crossing-node tone. Distinct from the 17th ashlar (which draws rectangular cell
OUTLINES, empty interiors) — tartan fills BANDS and NODES, not cell edges. The thin
single-pixel over-check guard line is a minor classic accent, not the motif.

Per slot it lands as the 26th distinct axis:
  * CHEST  — tartan cuirass: woven sett over the whole cuirass.
  * LEGS   — tartan chausses: woven sett over the thighs.
  * BOOTS  — tartan sabatons: woven sett over the boot.
  * HELMET — tartan dome: woven sett over the whole crown.

Authoring philosophy is identical to gen_argyle_axis25.py / gen_spiral_axis24.py: every
tartan pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction. Sleep
frames (fi>=60, lying down) get the recolor only — no bands. Shading applied in this script
via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 25th (argyle, regal jewel body + gold diamond)
and the 24th (spiral, verdigris teal + copper) the tartan family is a WOVEN-CLOTH highland
look: a deep muted body with BOLD CONTRASTING BANDS and a bright sett node — clan-cloth, not
metal. The body tint distinguishes class:
  * warrior — charcoal-black body + crimson bands + bone-white sett (Royal Stewart vibe)
  * mage    — midnight-indigo body + violet-blue bands + silver sett
  * ranger  — bottle-green body + saffron-gold bands + cream sett (hunting tartan)

Run from repo root:
  python3 scripts/gen_tartan_axis26.py
Then QA (examples):
  python3 scripts/sprite_qa.py _tartan_legendary_preview/shirt_warrior_legendary26.png
  python3 scripts/sprite_qa.py _tartandome_helmet_preview/helmet_mage_legendary26.png --y-min 2
  python3 scripts/sprite_qa.py _tartan_boots_preview/boots_warrior_legendary_tartan.png --y-max 63
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

# Tartan geometry. Work in component-local coords (dx, dy) relative to the component bbox
# top-left so the sett is stable frame-to-frame. Tile the plane at PITCH. A BOLD band of
# thickness BW runs where the local coordinate is < BW in either axis; a thin single-pixel
# GUARD over-check line sits at offset GUARD within the tile. Where a vertical bold band
# crosses a horizontal bold band the pixel is the brighter SETT NODE. Priority per pixel:
#   node (both bold)  >  band (either bold)  >  guard (either thin)  >  recolored body.
PITCH = 8               # band pitch (px)
BW = 2                  # bold band thickness (px)
GUARD = 4               # thin over-check line offset within the tile (px)


# Per-class accent palettes: (BAND bold tone, SETT crossing-node tone, GUARD thin tone).
SEAM = {
    'warrior': ((176, 40, 46), (238, 230, 216), (210, 150, 120)),   # crimson band, bone sett, dusty guard
    'mage':    ((96, 92, 196), (222, 224, 238), (150, 150, 210)),   # violet-blue band, silver sett, pale guard
    'ranger':  ((196, 158, 60), (238, 230, 196), (170, 160, 110)),  # saffron band, cream sett, tan guard
}

# Per-class body tones: deep shadow / base / highlight. WOVEN-CLOTH variants so the set reads
# apart from argyle's jewel body: here the body is a deep muted highland ground.
BODY = {
    'warrior': ((14, 14, 20), (34, 34, 44), (60, 60, 74)),     # charcoal-black
    'mage':    ((16, 18, 46), (32, 36, 82), (56, 62, 122)),    # midnight-indigo
    'ranger':  ((12, 34, 24), (26, 62, 42), (48, 92, 66)),     # bottle-green
}

# One config block per slot. `largest` restricts the tartan field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs field all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_tartan_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary26', largest=True,
    ),
    'legs': dict(
        outdir='_tartan_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary26', largest=False,
    ),
    'boots': dict(
        outdir='_tartan_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_tartan', largest=False,
    ),
    'helmet': dict(
        outdir='_tartandome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary26', largest=True,
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


def draw_tartan(fr, comp, band, node, guard):
    """Paint a woven-sett field of crossing orthogonal bands onto one component. For each
    opaque pixel, take local (dx, dy) relative to the component bbox top-left. A pixel is on a
    bold VERTICAL band if (dx % PITCH) < BW, on a bold HORIZONTAL band if (dy % PITCH) < BW.
    Where both hold it is the brighter SETT NODE; where one holds it is the BAND tone. Failing
    those, a thin over-check GUARD pixel sits where dx % PITCH == GUARD or dy % PITCH == GUARD.
    Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())

    for yy, xx in zip(ys.tolist(), xs.tolist()):
        dx = xx - x0
        dy = yy - y0
        fx = dx % PITCH
        fy = dy % PITCH
        v_band = fx < BW
        h_band = fy < BW
        if v_band and h_band:
            put(fr, yy, xx, node)
        elif v_band or h_band:
            put(fr, yy, xx, band)
        elif fx == GUARD or fy == GUARD:
            put(fr, yy, xx, guard)
        # else: leave the recolored body tone


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    band, node, guard = SEAM[cls]
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
        draw_tartan(fr, comp, band, node, guard)
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
                print('wrote %-54s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
