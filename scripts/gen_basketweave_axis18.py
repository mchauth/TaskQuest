#!/usr/bin/env python3
"""EIGHTEENTH net-new-geometry axis for ALL FOUR SLOTS — the BASKETWEAVE / WICKER
family: an interlaced ORTHOGONAL WOVEN field. The body is tiled into a checkerboard of
square cells; every other cell shows the WEFT (a bundle of short HORIZONTAL threads)
and the cells between them show the WARP (a bundle of short VERTICAL threads), so the
surface reads as a plaited basket / wickerwork where perpendicular thread bundles pass
over and under one another. This is the interlaced-orthogonal-weave surface axis that
none of the seventeen existing legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid CONTINUOUS CROSSING DIAGONAL lines -> diamond/lozenge mesh
  * 15th axis laid OVERLAPPING CURVED ARCS -> an imbricated scale field
  * 16th axis laid SHORT alternating-slope DIAGONAL dashes -> herringbone / twill
  * 17th axis laid a STAGGERED grid of closed RECTANGULAR CELLS -> ashlar masonry
  * 18th (this) laid a CHECKER of perpendicular SHORT-THREAD BUNDLES -> basketweave.
Distinct from the 12th (pure continuous horizontal, no vertical, no checker), from the
16th twill (SHORT DIAGONAL dashes, not orthogonal), from the 17th ashlar (continuous
mortar outlining CLOSED cells, not a checker of solid thread bundles), and from the
13th point grid (discrete dots, not short strokes). The over/under CHECKER of H vs V
thread bundles is what separates it from every prior axis.

Per slot it lands as the 18th distinct axis:
  * CHEST  — woven cuirass: plaited basketweave over the whole cuirass.
  * LEGS   — woven chausses: basketweave over the thighs.
  * BOOTS  — woven greaves: basketweave over the boot.
  * HELMET — woven dome: basketweave over the whole crown.

Authoring philosophy is identical to gen_ashlar_axis17.py / gen_twill_axis16.py:
weave pixels are painted ONLY onto pixels that are ALREADY opaque body pixels.
Because it never adds a pixel outside the existing silhouette it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — QA-safe
purely by construction. Sleep frames (fi>=60, lying down) get the recolor only — no
weave. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 17th (ashlar, warm sandstone/brass) and
16th (twill, cool frost-steel), the basketweave family is a deep DARK-LEATHER /
BRONZE-THREAD tint per class (the natural read for woven wicker/leather cord):
  * warrior — dark tanned-leather body + BRIGHT BRONZE threads, black-brown shadow
  * mage    — deep indigo body + PALE-SILVER threads, blue-black shadow
  * ranger  — dark bark-green body + TAN-STRAW threads, deep-forest shadow

Run from repo root:
  python3 scripts/gen_basketweave_axis18.py
Then QA (examples):
  python3 scripts/sprite_qa.py _basketweave_legendary_preview/shirt_warrior_legendary18.png
  python3 scripts/sprite_qa.py _basketdome_helmet_preview/helmet_mage_legendary18.png --y-min 2
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

# Per-class thread palettes: (THREAD bright weave pixel, SHADOW dark under-thread pixel).
THREAD = {
    'warrior': ((198, 150, 86), (34, 24, 16)),      # bronze thread, black-brown
    'mage':    ((198, 206, 224), (24, 20, 52)),      # pale silver, blue-black
    'ranger':  ((196, 172, 108), (24, 34, 20)),      # tan straw, deep forest
}

# Per-class body tones: deep shadow / base / highlight. Dark-leather variants so the
# set reads apart from the warm-sandstone ashlar 17th axis.
BODY = {
    'warrior': ((30, 22, 14), (74, 54, 32), (120, 92, 56)),    # tanned leather
    'mage':    ((20, 16, 44), (48, 40, 96), (96, 84, 168)),    # deep indigo
    'ranger':  ((18, 30, 16), (44, 70, 36), (88, 128, 66)),    # dark bark-green
}

# One config block per slot. `largest` restricts the weave to the biggest connected
# component (torso / dome) so raised arms are not woven; boots/legs weave all opaque
# pixels (both limbs). `tile` = weave cell size in px.
SLOTS = {
    'chest': dict(
        outdir='_basketweave_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary18', tile=4, largest=True,
    ),
    'legs': dict(
        outdir='_basketweave_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary18', tile=3, largest=False,
    ),
    'boots': dict(
        outdir='_basketweave_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_basket', tile=3, largest=False,
    ),
    'helmet': dict(
        outdir='_basketdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary18', tile=3, largest=True,
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


def draw_basketweave(fr, comp, thread, shadow, tile):
    """Paint a basketweave / wicker field onto one component. The component's bounding
    box is divided into a CHECKERBOARD of square TILES of side `tile`. Tiles with even
    (tx+ty) parity carry the WEFT — short HORIZONTAL thread bundles (mortar painted on
    the even rows within the tile). Tiles with odd parity carry the WARP — short
    VERTICAL thread bundles (mortar painted on the even columns within the tile). The
    perpendicular bundles meeting at tile edges give the plaited over/under read. A dark
    under-thread SHADOW pixel is painted just past the far end of each thread bundle
    where opaque, giving woven relief. Only opaque body pixels are ever painted, so it
    cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    opaque = set(zip(ys.tolist(), xs.tolist()))

    t = max(2, tile)
    th = set()      # thread pixels
    for (y, x) in opaque:
        tx = (x - x0) // t
        ty = (y - y0) // t
        rin = (y - y0) % t     # row within tile
        cin = (x - x0) % t     # col within tile
        if (tx + ty) % 2 == 0:
            # WEFT tile: horizontal threads on even rows of the tile
            if rin % 2 == 0:
                th.add((y, x))
        else:
            # WARP tile: vertical threads on even cols of the tile
            if cin % 2 == 0:
                th.add((y, x))

    for (y, x) in th:
        put(fr, y, x, thread)
    # under-thread shadow: one pixel below a weft thread / right of a warp thread,
    # only where opaque and not itself a thread — gives the plaited depth.
    for (y, x) in th:
        tx = (x - x0) // t
        ty = (y - y0) // t
        if (tx + ty) % 2 == 0:
            ny, nx = y + 1, x
        else:
            ny, nx = y, x + 1
        if (ny, nx) in opaque and (ny, nx) not in th:
            put(fr, ny, nx, shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    thread, shadow = THREAD[cls]
    tile, largest = cfg['tile'], cfg['largest']
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
        draw_basketweave(fr, comp, thread, shadow, tile)
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
