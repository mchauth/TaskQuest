#!/usr/bin/env python3
"""NINETEENTH net-new-geometry axis for ALL FOUR SLOTS — the HONEYCOMB / HEXAGONAL
family: an all-over field of tessellating SIX-SIDED CELLS. Hex cell centres are laid on
a flat-top hexagonal lattice (column spacing 1.5*s, row spacing sqrt(3)*s, alternate
columns offset by half a row). Each opaque body pixel is assigned to its NEAREST centre;
the Euclidean-nearest partition of a hexagonal centre lattice is a field of regular
HEXAGONS, so the seam pixels (where a pixel borders a pixel in a different cell) trace a
clean honeycomb net. This is the hexagonal-tessellation surface axis that none of the
eighteen existing legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid CONTINUOUS CROSSING DIAGONAL lines -> diamond/lozenge mesh
  * 15th axis laid OVERLAPPING CURVED ARCS -> an imbricated scale field
  * 16th axis laid SHORT alternating-slope DIAGONAL dashes -> herringbone / twill
  * 17th axis laid a STAGGERED grid of closed RECTANGULAR (4-sided) CELLS -> ashlar
  * 18th axis laid a CHECKER of perpendicular SHORT-THREAD BUNDLES -> basketweave
  * 19th (this) laid a tessellation of SIX-SIDED CELLS -> honeycomb.
Distinct from the 17th ashlar (closed FOUR-sided rectangular cells in an offset brick
bond) and the 14th lattice (FOUR-sided lozenges from crossing straight diagonals): the
honeycomb cell is a HEXAGON, a genuinely new tessellation. Distinct from basketweave
(solid woven thread bundles, no outlined cell) and from studwork (discrete dots, no
cell boundary). The SIX-SIDED closed cell is what separates it from every prior axis.

Per slot it lands as the 19th distinct axis:
  * CHEST  — honeycomb cuirass: gilded hex net over the whole cuirass.
  * LEGS   — honeycomb chausses: hex net over the thighs.
  * BOOTS  — honeycomb greaves: hex net over the boot.
  * HELMET — honeycomb dome: hex net over the whole crown.

Authoring philosophy is identical to gen_basketweave_axis18.py / gen_ashlar_axis17.py:
seam pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction.
Sleep frames (fi>=60, lying down) get the recolor only — no net. Shading applied in
this script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 17th (ashlar, whole-body warm sandstone) and
18th (basketweave, bronze weave over dark leather), the honeycomb family is a GILDED
comb: a deep JEWEL-TONED body per class with a bright common GOLD seam net (the natural
read for a golden honeycomb) — the shared gold net reads instantly as "honeycomb" while
the jewel body distinguishes the class:
  * warrior — deep garnet-red body + bright GOLD seams, black-red shadow
  * mage    — deep violet body + GOLD seams, blue-black shadow
  * ranger  — deep teal-green body + GOLD seams, deep-forest shadow

Run from repo root:
  python3 scripts/gen_honeycomb_axis19.py
Then QA (examples):
  python3 scripts/sprite_qa.py _honeycomb_legendary_preview/shirt_warrior_legendary19.png
  python3 scripts/sprite_qa.py _honeydome_helmet_preview/helmet_mage_legendary19.png --y-min 2
  python3 scripts/sprite_qa.py _honeycomb_boots_preview/boots_warrior_legendary_honey.png --y-max 63
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

# Per-class seam palettes: (SEAM bright gold pixel, SHADOW dark under-seam pixel).
SEAM = {
    'warrior': ((214, 176, 86), (40, 14, 16)),      # gold seam, black-red shadow
    'mage':    ((214, 182, 96), (26, 18, 48)),      # gold seam, blue-black shadow
    'ranger':  ((214, 184, 96), (14, 34, 28)),      # gold seam, deep-forest shadow
}

# Per-class body tones: deep shadow / base / highlight. Jewel-toned variants so the set
# reads apart from ashlar's warm sandstone (17th) and basketweave's dark leather (18th).
BODY = {
    'warrior': ((36, 14, 16), (92, 30, 34), (150, 58, 60)),    # deep garnet
    'mage':    ((26, 16, 44), (64, 40, 104), (120, 84, 180)),  # deep violet
    'ranger':  ((14, 34, 30), (34, 74, 66), (72, 128, 112)),   # deep teal-green
}

# One config block per slot. `largest` restricts the net to the biggest connected
# component (torso / dome) so raised arms are not netted; boots/legs net all opaque
# pixels (both limbs). `hs` = hex size in px (radius-ish; larger cells on the chest).
SLOTS = {
    'chest': dict(
        outdir='_honeycomb_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary19', hs=3.2, largest=True,
    ),
    'legs': dict(
        outdir='_honeycomb_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary19', hs=2.6, largest=False,
    ),
    'boots': dict(
        outdir='_honeycomb_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_honey', hs=2.6, largest=False,
    ),
    'helmet': dict(
        outdir='_honeydome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary19', hs=2.6, largest=True,
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


def hex_centers(y0, y1, x0, x1, s):
    """Flat-top hexagonal lattice of cell centres covering the bbox (with one cell of
    padding on every side so edge cells are complete). Column spacing 1.5*s, row spacing
    sqrt(3)*s, alternate columns offset vertically by half a row."""
    dx = 1.5 * s
    dy = math.sqrt(3.0) * s
    centers = []
    col = 0
    x = x0 - dx
    while x <= x1 + dx:
        yoff = (dy / 2.0) if (col % 2) else 0.0
        y = y0 - dy + yoff
        while y <= y1 + dy:
            centers.append((y, x))
            y += dy
        x += dx
        col += 1
    return np.array(centers, dtype=np.float32)


def draw_honeycomb(fr, comp, seam, shadow, s):
    """Paint a honeycomb hex net onto one component. Assign every opaque pixel to its
    nearest hex centre (Euclidean-nearest of a hex lattice => regular hexagon cells).
    Seam pixels are opaque pixels that border an opaque pixel in a DIFFERENT cell — this
    traces the closed six-sided cell boundaries. A dark under-seam SHADOW pixel below the
    seam (where opaque and not itself a seam) gives the comb its raised relief. Only
    opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())

    C = hex_centers(y0, y1, x0, x1, s)
    if C.shape[0] == 0:
        return
    P = np.stack([ys, xs], axis=1).astype(np.float32)          # (N,2)
    d2 = ((P[:, None, 0] - C[None, :, 0]) ** 2 +
          (P[:, None, 1] - C[None, :, 1]) ** 2)                 # (N,K)
    lab = d2.argmin(axis=1)

    labmap = {}
    for (yy, xx), lv in zip(zip(ys.tolist(), xs.tolist()), lab.tolist()):
        labmap[(yy, xx)] = lv
    opaque = set(labmap)

    seam_px = set()
    for (yy, xx), lv in labmap.items():
        for dyn, dxn in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = (yy + dyn, xx + dxn)
            l2 = labmap.get(nb)
            if l2 is not None and l2 != lv:
                seam_px.add((yy, xx))
                break

    for (yy, xx) in seam_px:
        put(fr, yy, xx, seam)
    # under-seam relief: one pixel below each seam pixel, if opaque and not a seam
    for (yy, xx) in seam_px:
        nb = (yy + 1, xx)
        if nb in opaque and nb not in seam_px:
            put(fr, nb[0], nb[1], shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    seam, shadow = SEAM[cls]
    hs, largest = cfg['hs'], cfg['largest']
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
        draw_honeycomb(fr, comp, seam, shadow, hs)
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
