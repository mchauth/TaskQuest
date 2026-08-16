#!/usr/bin/env python3
"""TWENTY-EIGHTH net-new-geometry axis for ALL FOUR SLOTS — the CONCENTRIC / TARGET /
RIPPLE-RING family: an all-over field of tiled CENTRES, each ringed by a set of NESTED CLOSED
RINGS at growing radius (radius 1, 2, 3, 4 ...) sharing ONE origin — a bullseye / target /
tree-ring / water-ripple look — with a bright CORE dot at the shared centre and the nested
rings alternating a bright/dark tone by radius parity so the concentric banding reads. The
repeated motif is the NESTED CONCENTRIC RING SET: several separate closed loops of increasing
radius stacked around a common point. This nested-rings-around-a-point geometry is occupied by
none of the twenty-seven existing legendary axes per slot:
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
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE point -> sunburst / compass
  * 28th (this) STACKS NESTED CLOSED RINGS at growing radius around a shared CENTRE -> target.
Critically distinct from the 21st chainmail (a tiled field of SINGLE same-radius interlinked
rings, one ring per centre) — concentric stacks MULTIPLE nested rings of increasing radius
around ONE centre (a bullseye), not a mesh of equal single rings. Distinct from the 24th spiral
(ONE CONTINUOUS coil whose radius grows as it winds) — concentric rings are SEPARATE closed
loops, never joined into a coil. Distinct from the 27th sunburst (STRAIGHT rays shooting OUT
from the centre) — concentric are CLOSED CURVED rings encircling the centre, no radial rays.
Distinct from the 15th scale (short OPEN arcs, no shared centre) and the 3rd studwork (isolated
POINTS, no rings). The bright core dot is the origin accent; the motif is the nested ring set.

Per slot it lands as the 28th distinct axis:
  * CHEST  — target cuirass: nested ring bullseyes over the whole cuirass.
  * LEGS   — target chausses: nested ring bullseyes over the thighs.
  * BOOTS  — rippleward sabatons: nested ring bullseyes over the boot.
  * HELMET — oracle dome: nested ring bullseyes over the whole crown.

Authoring philosophy is identical to gen_sunburst_axis27.py / gen_tartan_axis26.py: every ring
pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60, lying
down) get the recolor only — no rings. Shading applied in this script via shade(); do NOT run
sprite_shade.py again.

To read as a clearly DIFFERENT set from the 27th (sunburst — near-void body with bright rays
bursting out) the concentric family INVERTS the contrast: a LIGHTER burnished-metal body with
the rings ENGRAVED into it as recessed dark grooves plus a bright raised ring-crest — light
metal target-work, not light bursting from darkness. Reads apart from tartan (woven cloth) and
argyle (jewel body + gold diamond) too. The body tint distinguishes class:
  * warrior — burnished-bronze body + dark-umber ring groove + bright-gold ring crest (aegis-ring)
  * mage    — pale-silver-violet body + deep-violet groove + white ring crest (oracle ripple)
  * ranger  — pale-sage-bronze body + deep-forest groove + warm-gold ring crest (tideward)

Run from repo root:
  python3 scripts/gen_concentric_axis28.py
Then QA (examples):
  python3 scripts/sprite_qa.py _concentric_legendary_preview/shirt_warrior_legendary28.png
  python3 scripts/sprite_qa.py _oracledome_helmet_preview/helmet_mage_legendary28.png --y-min 2
  python3 scripts/sprite_qa.py _concentric_boots_preview/boots_warrior_legendary_concentric.png --y-max 63
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

# Concentric-ring geometry. Work in component-local coords relative to the component bbox
# top-left so the ring grid is stable frame-to-frame. Tile the plane at PITCH; a ring CENTRE
# sits at every grid node. For each opaque pixel take its offset (rx, ry) to the NEAREST
# centre and its Chebyshev radius r = max(|rx|, |ry|) (square rings — crisp at pixel scale and
# clearly nested). If r == 0 the pixel is the CORE. If 1 <= r <= RMAX the pixel is on ring r:
# odd r -> bright ring crest, even r -> dark ring groove, giving the alternating target banding.
# Beyond RMAX the pixel keeps the recolored body, so with PITCH > 2*RMAX the bullseyes stay
# discrete, separated by body ground. Priority per pixel: core > ring > recolored body.
PITCH = 10              # bullseye spacing (px) — centre-to-centre
RMAX = 4                # outermost ring radius (px); < PITCH/2 keeps bullseyes discrete
CORE = 0                # core is the single centre pixel (r == 0)


# Per-class accent palettes: (RING-CREST bright tone, RING-GROOVE dark tone, CORE tone).
SEAM = {
    'warrior': ((224, 176, 78), (60, 40, 18), (255, 240, 200)),   # gold crest, umber groove, bright core
    'mage':    ((198, 176, 236), (58, 40, 92), (244, 238, 255)),  # violet crest, deep-violet groove, white core
    'ranger':  ((208, 178, 96), (28, 52, 34), (240, 230, 176)),   # gold crest, forest groove, pale-gold core
}

# Per-class body tones: deep shadow / base / highlight. LIGHTER burnished-metal variants (vs
# sunburst's near-void body) so the recessed rings read as engraved into a bright metal ground.
BODY = {
    'warrior': ((104, 74, 34), (150, 110, 54), (198, 154, 84)),    # burnished bronze
    'mage':    ((96, 88, 120), (142, 132, 170), (188, 180, 214)),  # pale silver-violet
    'ranger':  ((84, 96, 62), (126, 140, 90), (172, 186, 128)),    # pale sage-bronze
}

# One config block per slot. `largest` restricts the ring field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs field all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_concentric_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary28', largest=True,
    ),
    'legs': dict(
        outdir='_concentric_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary28', largest=False,
    ),
    'boots': dict(
        outdir='_concentric_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_concentric', largest=False,
    ),
    'helmet': dict(
        outdir='_oracledome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary28', largest=True,
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


def draw_concentric(fr, comp, crest, groove, core):
    """Paint a field of nested concentric ring bullseyes onto one component. For each opaque
    pixel take its offset (rx, ry) to the NEAREST centre on a PITCH grid anchored at the
    component bbox top-left, and its Chebyshev radius r = max(|rx|, |ry|). r==0 -> CORE; odd r
    in [1, RMAX] -> bright ring CREST; even r in [1, RMAX] -> dark ring GROOVE; else keep the
    recolored body. Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    half = PITCH // 2

    for yy, xx in zip(ys.tolist(), xs.tolist()):
        dx = xx - x0
        dy = yy - y0
        # offset to nearest centre, in range [-half, half)
        rx = ((dx + half) % PITCH) - half
        ry = ((dy + half) % PITCH) - half
        r = max(abs(rx), abs(ry))
        if r == CORE:
            put(fr, yy, xx, core)
        elif r <= RMAX:
            put(fr, yy, xx, crest if (r % 2 == 1) else groove)
        # else: leave the recolored body tone


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    crest, groove, core = SEAM[cls]
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
        draw_concentric(fr, comp, crest, groove, core)
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
