#!/usr/bin/env python3
"""TWELFTH net-new-geometry CHEST showcase per class — a BANDED LAMELLAR CUIRASS: a
set of parallel HORIZONTAL lames (laminated bands) stacked down the breastplate.
This brings the chest slot to TWELVE distinct axes. It is the repeated-parallel-
HORIZONTAL surface axis none of the eleven existing legendary chests occupy:

  * legendary1 (base)        — plain field.
  * legendary2 (pauldrons)   — outward SHOULDER caps (silhouette).
  * legendary3 (cape)        — a side DRAPE.
  * legendary4 (tabard)      — a SINGLE vertical hanging banner.
  * legendary5 (gorget)      — a high NECK collar.
  * legendary6 (baldric)     — one DIAGONAL sash.
  * legendary7 (girdle)      — one HORIZONTAL war-belt band.
  * legendary8 (roundel)     — a central CIRCULAR boss.
  * legendary9 (chevron)     — a down-pointing V.
  * legendary10 (cross)      — a '+' cross (one vertical + one horizontal).
  * legendary11 (fluted)     — THREE vertical grooves (repeated-parallel-VERTICAL).
  * this BANDED LAMELLAR lays THREE evenly-spaced HORIZONTAL lames across the whole
    cuirass — the repeated-parallel-HORIZONTAL axis, distinct from the single girdle
    band, the single '+' cross bar, and the repeated VERTICAL fluting. A flat
    repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_flute_legendary.py: lame pixels are painted
ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — QA-safe purely by construction.
Painted onto the LARGEST connected component per frame only (torso, not raised arms).

Sleep frames (fi>=60, lying down) get the recolor only — no lames. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class the lame hue is the class accent family:
  * warrior "Warlord's Lamellar Cuirass" — obsidian/steel body + bright-steel lame, gold rivet
  * mage    "Astral Laminate Robe"       — arcane-violet body + silver lame, cyan rivet
  * ranger  "Warden's Banded Jerkin"     — forest body + pale-bone lame, copper rivet

Run from repo root:
  python3 scripts/gen_lamellar_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _lamellar_legendary_preview/shirt_warrior_legendary12.png
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Three lame centre-rows as fractions of the torso bbox height. Each lame is a lit
# band (EDGE) with a dark seam (FIELD) on its lower edge; a rivet PIP at band centre.
LAME_FRACS = (0.32, 0.54, 0.76)
MIN_PX = 12

# body : deep shadow / base / highlight
# lame : EDGE (lit band) / FIELD (dark seam under it) / PIP (bright centre rivet)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary12',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian -> steel
        lame=((196, 202, 218), (44, 46, 56), (232, 190, 70)),        # bright steel band, dark seam, gold rivet
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary12',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        lame=((198, 204, 224), (34, 28, 88), (96, 210, 244)),        # silver band, dark seam, cyan rivet
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary12',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        lame=((206, 200, 168), (28, 54, 26), (206, 132, 66)),        # pale bone band, dark seam, copper rivet
    ),
}


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


def draw_lames(fr, comp, pal):
    """Paint parallel horizontal lames onto one torso component."""
    EDGE, FIELD, PIP = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    h = max(y1 - y0, 1)
    lames = [y0 + f * h for f in LAME_FRACS]
    mid_row = []                             # painted pixels of the centre lame band
    for y, x in zip(ys, xs):
        for li, lc in enumerate(lames):
            if abs(y - lc) < 0.5:            # the lit lame band
                put(fr, y, x, EDGE)
                if li == 1:
                    mid_row.append((y, x))
                break
            if abs(y - (lc + 1.0)) < 0.5:    # dark seam under the band
                put(fr, y, x, FIELD)
                break
    # a single bright rivet pip at the centre of the middle lame
    if mid_row:
        ys2 = [p[0] for p in mid_row]
        xs2 = [p[1] for p in mid_row]
        cx = int(round(sum(xs2) / len(xs2)))
        # nearest painted pixel on that band to the centre column
        y, x = min(mid_row, key=lambda p: abs(p[1] - cx))
        put(fr, y, x, PIP)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['lame']
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
        if fi >= 60:                       # sleep: body only
            continue
        lbl, n = ndimage.label(a)
        if n >= 1:
            sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
            torso = (lbl == (int(np.argmax(sizes)) + 1))
            draw_lames(fr, torso, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_lamellar_legendary_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.20, adj_max=0.25)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-48s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
