#!/usr/bin/env python3
"""TENTH net-new-geometry CHEST showcase per class — a HERALDIC COUPED CROSS:
a bold vertical stripe down the torso centreline crossed by a horizontal bar at
mid-chest, forming a '+' emblazoned across the cuirass. This brings the chest
slot to TEN distinct axes. It is the cruciform surface axis none of the nine
existing legendary chests occupy:

  * legendary1 (base)        — plain field.
  * legendary2 (pauldrons)   — outward SHOULDER caps (silhouette).
  * legendary3 (cape)        — a side DRAPE.
  * legendary4 (tabard)      — a single VERTICAL hanging banner (no cross-bar).
  * legendary5 (gorget)      — a high NECK collar.
  * legendary6 (baldric)     — one DIAGONAL sash.
  * legendary7 (girdle)      — one HORIZONTAL war-belt band (no vertical).
  * legendary8 (roundel)     — a central CIRCULAR boss.
  * legendary9 (chevron)     — a down-pointing V.
  * this CROSS combines a vertical spine AND a horizontal bar into a '+':
    orthogonal to the single-axis tabard (vertical only) and girdle (horizontal
    only), and distinct from the V chevron and the round roundel. It is a flat
    repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_chevron_legendary.py / gen_kneeband_legs.py:
the cross is painted ONLY onto pixels that are ALREADY opaque body pixels (`a`).
Because it never adds a pixel outside the existing silhouette it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — the
cross is QA-safe purely by construction. To keep the emblem on the chest (not on
raised arms, which split into their own components on some poses) it is painted
onto the LARGEST connected component per frame only.

  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = the cross. For the torso component we take its bbox, lay a vertical
    band VBAND_HALF cols either side of the component centre-x over the full
    height, and a horizontal band HBAND_HALF rows either side of a bar-row placed
    CROSS_FRAC down. Band pixels get the lit selvage on their leading edge and the
    field colour otherwise; a single bright pip marks the intersection. Everything
    clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no cross — matching the
tabard / baldric / chevron convention. Shading applied in-script via shade(); do
NOT run sprite_shade.py again.

Per class the cross hue is distinct from EVERY prior legendary chest accent:
  * warrior "Crusader's Cross"  — obsidian/steel body + IVORY cross, crimson selvage
  * mage    "Astral Rood"       — arcane-violet body + GOLD cross, cyan pip
  * ranger  "Warden's Cross"    — forest body + PALE-BONE cross, emerald pip

Run from repo root:
  python3 scripts/gen_cross_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _cross_legendary_preview/shirt_warrior_legendary10.png
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

# Cross geometry. Vertical band = VBAND_HALF cols either side of the torso centre.
# Horizontal bar centred CROSS_FRAC of the way down the torso bbox, HBAND_HALF rows
# thick. MIN_PX ignores tiny specks when choosing the torso component.
VBAND_HALF = 1.1
HBAND_HALF = 1.1
CROSS_FRAC = 0.42
MIN_PX = 12

# body : deep shadow / base / highlight
# cross: FIELD (cross body) / EDGE (lit leading selvage) / PIP (bright centre pip)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary10',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian -> steel
        cross=((206, 210, 222), (150, 22, 26), (255, 250, 240)),     # ivory field, crimson selvage, white pip
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary10',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        cross=((214, 168, 52), (140, 100, 20), (96, 210, 244)),      # gold field, bronze selvage, cyan pip
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary10',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        cross=((228, 216, 176), (150, 120, 60), (70, 210, 120)),     # pale bone field, tan selvage, emerald pip
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


def draw_cross(fr, comp, pal):
    """Paint a '+' cross onto one torso component (boolean, frame-sized)."""
    FIELD, EDGE, PIP = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cx = 0.5 * (x0 + x1)              # torso centre-col
    bar_y = y0 + CROSS_FRAC * h       # horizontal bar centre-row
    for y, x in zip(ys, xs):
        on_v = abs(x - cx) <= VBAND_HALF
        on_h = abs(y - bar_y) <= HBAND_HALF
        if not (on_v or on_h):
            continue
        # lit selvage on the leading (upper / left) edge of each arm of the cross
        lead = (on_v and (x - cx) <= -0.2) or (on_h and (y - bar_y) <= -0.2)
        put(fr, y, x, EDGE if lead else FIELD)
    # bright pip at the intersection
    put(fr, int(round(bar_y)), int(round(cx)), PIP)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['cross']
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
        # paint the cross on the LARGEST component (the torso) only
        lbl, n = ndimage.label(a)
        if n >= 1:
            sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
            torso = (lbl == (int(np.argmax(sizes)) + 1))
            draw_cross(fr, torso, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_cross_legendary_preview'
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
