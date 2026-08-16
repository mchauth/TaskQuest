#!/usr/bin/env python3
"""ELEVENTH net-new-geometry CHEST showcase per class — a FLUTED CUIRASS: a set of
parallel vertical grooves (Maximilian-style fluting) incised down the breastplate.
This brings the chest slot to ELEVEN distinct axes. It is the repeated-parallel-
vertical (fluting) surface axis none of the ten existing legendary chests occupy:

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
  * this FLUTED CUIRASS lays THREE evenly-spaced vertical grooves across the whole
    cuirass — the repeated-parallel-vertical axis, distinct from the single-banner
    tabard, the single-spine cross, and every band/boss/V. A flat repaint that adds
    no silhouette pixels.

Authoring philosophy is identical to gen_cross_legendary.py: groove pixels are
painted ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated
pixels, background bleed, or accent-caused multi-component frames — QA-safe purely
by construction. To keep the fluting on the chest (not on raised arms, which split
into their own components on some poses) it is painted onto the LARGEST connected
component per frame only.

Sleep frames (fi>=60, lying down) get the recolor only — no flutes. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class the groove hue is the class accent family:
  * warrior "Warlord's Fluted Cuirass" — obsidian/steel body + bright-steel ridge, gold pip
  * mage    "Astral Fluted Robe"       — arcane-violet body + silver ridge, cyan pip
  * ranger  "Warden's Ribbed Jerkin"   — forest body + pale-bone ridge, copper pip

Run from repo root:
  python3 scripts/gen_flute_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _flute_legendary_preview/shirt_warrior_legendary11.png
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

# Three groove centre-cols as fractions of the torso bbox width. Each groove is a
# dark incision (FIELD) with a lit ridge (EDGE) on its viewer-left side.
GROOVE_FRACS = (0.30, 0.50, 0.70)
MIN_PX = 12

# body : deep shadow / base / highlight
# flute: FIELD (dark groove incision) / EDGE (lit ridge) / PIP (bright top pip)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary11',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian -> steel
        flute=((44, 46, 56), (196, 202, 218), (232, 190, 70)),       # dark groove, bright steel ridge, gold pip
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary11',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        flute=((34, 28, 88), (198, 204, 224), (96, 210, 244)),       # dark groove, silver ridge, cyan pip
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary11',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        flute=((28, 54, 26), (206, 200, 168), (206, 132, 66)),       # dark groove, pale bone ridge, copper pip
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


def draw_flutes(fr, comp, pal):
    """Paint parallel vertical grooves onto one torso component."""
    FIELD, EDGE, PIP = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    x0, x1 = int(xs.min()), int(xs.max())
    w = max(x1 - x0, 1)
    grooves = [x0 + f * w for f in GROOVE_FRACS]
    mid_col = []                             # painted pixels of the centre groove
    for y, x in zip(ys, xs):
        for gi, gc in enumerate(grooves):
            if abs(x - gc) < 0.5:            # the incised groove
                put(fr, y, x, FIELD)
                if gi == 1:
                    mid_col.append((y, x))
                break
            if abs(x - (gc - 1.0)) < 0.5:    # lit ridge on its viewer-left
                put(fr, y, x, EDGE)
                break
    # a single bright pip at the top of the centre groove (always an opaque pixel)
    if mid_col:
        y, x = min(mid_col)
        put(fr, y, x, PIP)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['flute']
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
            draw_flutes(fr, torso, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_flute_legendary_preview'
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
