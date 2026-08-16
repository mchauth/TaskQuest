#!/usr/bin/env python3
"""TWENTIETH net-new-geometry axis for ALL FOUR SLOTS — the TRELLIS / TRIANGULATED
family: an all-over field of tessellating THREE-SIDED CELLS. The net is the union of
THREE families of parallel straight lines separated by 60 degrees (one horizontal at 0
deg, plus two obliques at +60 and -60 deg). Where three such line families overlay at
equal spacing they subdivide the plane into a field of alternating up- and down-pointing
EQUILATERAL TRIANGLES — a genuine triangular tessellation whose closed cell is a
THREE-sided polygon. This is the triangular-tessellation surface axis that none of the
nineteen existing legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid TWO crossing diagonal families -> FOUR-sided lozenge/diamond mesh
  * 15th axis laid OVERLAPPING CURVED ARCS -> an imbricated scale field
  * 16th axis laid SHORT alternating-slope DIAGONAL dashes -> herringbone / twill
  * 17th axis laid a STAGGERED grid of closed RECTANGULAR (4-sided) CELLS -> ashlar
  * 18th axis laid a CHECKER of perpendicular SHORT-THREAD BUNDLES -> basketweave
  * 19th axis laid a tessellation of SIX-sided CELLS -> honeycomb
  * 20th (this) laid THREE line families -> tessellation of THREE-sided CELLS -> trellis.
Distinct from the 14th lattice, whose TWO crossing diagonals close only FOUR-sided
lozenges: the trellis adds the THIRD (horizontal) family, which bisects every lozenge
into a pair of TRIANGLES, so the closed cell drops from 4 sides to 3. Distinct from the
19th honeycomb (6-sided cells) and 17th ashlar (4-sided rectangles). The THREE-sided
closed cell is what separates it from every prior axis.

Per slot it lands as the 20th distinct axis:
  * CHEST  — trellis cuirass: argent triangle net over the whole cuirass.
  * LEGS   — trellis chausses: triangle net over the thighs.
  * BOOTS  — trellis sabatons: triangle net over the boot.
  * HELMET — trellis dome: triangle net over the whole crown.

Authoring philosophy is identical to gen_honeycomb_axis19.py / gen_basketweave_axis18.py:
seam pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction.
Sleep frames (fi>=60, lying down) get the recolor only — no net. Shading applied in
this script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 19th (honeycomb, GOLD net over jewel body)
the trellis family is an ARGENT trellis: a metallic body per class with a bright common
SILVER seam net (the natural read for a wrought-iron / steel trellis) — the shared silver
net reads instantly as "trellis" while the metallic body distinguishes the class:
  * warrior — warm bronze body + bright SILVER seams, black-bronze shadow
  * mage    — deep indigo body + SILVER seams, blue-black shadow
  * ranger  — bronze-olive body + SILVER seams, deep-forest shadow

Run from repo root:
  python3 scripts/gen_trellis_axis20.py
Then QA (examples):
  python3 scripts/sprite_qa.py _trellis_legendary_preview/shirt_warrior_legendary20.png
  python3 scripts/sprite_qa.py _trellisdome_helmet_preview/helmet_mage_legendary20.png --y-min 2
  python3 scripts/sprite_qa.py _trellis_boots_preview/boots_warrior_legendary_trellis.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Per-class seam palettes: (SEAM bright argent pixel, SHADOW dark under-seam pixel).
SEAM = {
    'warrior': ((198, 204, 216), (34, 20, 12)),     # silver seam, black-bronze shadow
    'mage':    ((200, 206, 222), (22, 20, 46)),      # silver seam, blue-black shadow
    'ranger':  ((198, 208, 208), (16, 32, 26)),      # silver seam, deep-forest shadow
}

# Per-class body tones: deep shadow / base / highlight. Metallic variants so the set
# reads apart from honeycomb's jewel body + gold seam (19th).
BODY = {
    'warrior': ((44, 30, 18), (104, 74, 40), (168, 128, 74)),   # warm bronze
    'mage':    ((22, 22, 52), (52, 52, 116), (104, 104, 190)),  # deep indigo
    'ranger':  ((22, 32, 18), (56, 74, 40), (104, 132, 74)),    # bronze-olive
}

# One config block per slot. `largest` restricts the net to the biggest connected
# component (torso / dome) so raised arms are not netted; boots/legs net all opaque
# pixels (both limbs). `sp` = triangle line spacing in px (larger cells on the chest).
SLOTS = {
    'chest': dict(
        outdir='_trellis_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary20', sp=5.0, largest=True,
    ),
    'legs': dict(
        outdir='_trellis_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary20', sp=4.0, largest=False,
    ),
    'boots': dict(
        outdir='_trellis_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_trellis', sp=4.0, largest=False,
    ),
    'helmet': dict(
        outdir='_trellisdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary20', sp=4.0, largest=True,
    ),
}

# Three line-family normals (in x,y). Family runs perpendicular to its normal, so
# normals at 90 / 30 / 150 deg give LINES at 0 (horizontal), 120, 60 deg -> triangles.
_NORMALS = [
    (0.0, 1.0),                                  # horizontal lines
    (math.cos(math.radians(30)), math.sin(math.radians(30))),   # +60 deg lines
    (math.cos(math.radians(150)), math.sin(math.radians(150))),  # -60 deg lines
]


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


def draw_trellis(fr, comp, seam, shadow, sp):
    """Paint a triangular trellis net onto one component. A pixel is a SEAM pixel when it
    lies within half a pixel of any of the three line families (equal spacing `sp`,
    normals at 90/30/150 deg). The union of the three families closes a field of
    alternating up/down TRIANGLES. A dark under-seam SHADOW pixel below each seam (where
    opaque and not itself a seam) gives the trellis its raised relief. Only opaque body
    pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    # Anchor phase to the component's top-left so the net is stable across frames.
    y0, x0 = float(ys.min()), float(xs.min())
    px = xs.astype(np.float32) - x0
    py = ys.astype(np.float32) - y0

    on_seam = np.zeros(ys.shape, dtype=bool)
    for nx, ny in _NORMALS:
        proj = px * nx + py * ny
        # distance (in px) to the nearest line of this family
        d = np.abs(proj - np.round(proj / sp) * sp)
        on_seam |= (d < 0.5)

    opaque = set(zip(ys.tolist(), xs.tolist()))
    seam_px = set()
    for yy, xx, s in zip(ys.tolist(), xs.tolist(), on_seam.tolist()):
        if s:
            seam_px.add((yy, xx))
            put(fr, yy, xx, seam)
    # under-seam relief: one pixel below each seam pixel, if opaque and not a seam
    for (yy, xx) in seam_px:
        nb = (yy + 1, xx)
        if nb in opaque and nb not in seam_px:
            put(fr, nb[0], nb[1], shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    seam, shadow = SEAM[cls]
    sp, largest = cfg['sp'], cfg['largest']
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
        draw_trellis(fr, comp, seam, shadow, sp)
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
                print('wrote %-52s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
