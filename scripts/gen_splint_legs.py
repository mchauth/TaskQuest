#!/usr/bin/env python3
"""TWELFTH net-new-geometry LEGS showcase per class — SPLINTED LAMES: a stack of
THREE parallel HORIZONTAL articulation lames banding each leg (laminated splint
armour). This brings the legs slot to TWELVE distinct axes. It is the repeated-
parallel-HORIZONTAL-multiple axis none of the eleven existing legendary legs occupy:

  * legendary1 (base)         — plain field.
  * legendary2 (warkilt)      — a draped hem KILT.
  * legendary3 (faulds)       — a stiff tiered plate SKIRT.
  * legendary4 (poleyn)       — lateral knee-cop DISCS.
  * legendary5 (cuisse)       — lateral hip-wing FLARE.
  * legendary6 (loinguard)    — a SINGLE down-centre vertical strip.
  * legendary7 (swordbelt)    — one DIAGONAL hip->knee belt.
  * legendary8 (sidestripe)   — paired outer VERTICAL stripes.
  * legendary9 (kneeband)     — a SINGLE horizontal knee band.
  * legendary10 (crossgarter) — a '+' cross garter.
  * legendary11 (thighpanel)  — a rectangular cuisse PANEL.
  * these SPLINTED LAMES stack THREE evenly-spaced HORIZONTAL bands per leg — the
    repeated-horizontal-MULTIPLE axis, distinct from the single knee band, the
    vertical side-stripes and centre strip, and the solid rectangular panel. A flat
    repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_kneeband_legs.py: lame pixels are painted
ONLY onto pixels that are ALREADY opaque body pixels. Painted per leg COMPONENT so
both legs band correctly. QA-safe purely by construction — it can never add a pixel
outside the existing silhouette.

Sleep frames (fi>=60) get the recolor only. Shading applied in-script via shade();
do NOT run sprite_shade.py again.

Per class the lame hue is the class accent family:
  * warrior "Warlord's Splinted Chausses" — obsidian/steel body + steel lames, gold rivet
  * mage    "Astral Laminate Leggings"    — arcane-violet body + silver lames, sapphire rivet
  * ranger  "Warden's Banded Greaves"     — forest body + tan lames, copper rivet

Run from repo root:
  python3 scripts/gen_splint_legs.py
Then QA:
  python3 scripts/sprite_qa.py _splint_legs_preview/pants_warrior_legendary12.png --y-max 62
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

# Three lame centre-rows as fractions of each leg-component bbox height. Each lame
# is a lit band (EDGE on its upper edge, BAND metal below); a single rivet PIP sits
# at the centre column of the MIDDLE lame.
LAME_FRACS = (0.34, 0.56, 0.78)
BAND_HALF = 1.0
MIN_PX = 8

# body : deep shadow / base / highlight
# lame : BAND (metal band body) / EDGE (lit upper edge) / PIP (bright centre rivet)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary12',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),      # obsidian -> steel
        lame=((110, 116, 132), (196, 202, 218), (232, 190, 70)), # steel band, lit edge, gold rivet
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary12',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),      # arcane violet
        lame=((120, 126, 150), (198, 204, 224), (72, 132, 244)), # silver band, lit edge, sapphire rivet
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary12',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),        # forest green
        lame=((110, 84, 48), (166, 128, 76), (206, 132, 66)),    # tan band, lit edge, copper rivet
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


def lame_component(fr, comp, pal):
    """Repaint three horizontal lames onto one leg component (body pixels only)."""
    BAND, EDGE, PIP = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cx = 0.5 * (x0 + x1)
    lame_rows = [y0 + f * h for f in LAME_FRACS]
    mid_band = []
    for y, x in zip(ys, xs):
        for li, lc in enumerate(lame_rows):
            if abs(y - lc) <= BAND_HALF:
                put(fr, y, x, EDGE if (y - lc) <= -0.2 else BAND)
                if li == 1:
                    mid_band.append((y, x))
                break
    # single rivet pip at the centre of the middle lame
    if mid_band:
        y, x = min(mid_band, key=lambda p: abs(p[1] - cx))
        put(fr, y, x, PIP)


def draw_lames(fr, a, pal):
    lbl, n = ndimage.label(a)
    for i in range(1, n + 1):
        lame_component(fr, lbl == i, pal)


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
        draw_lames(fr, a, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_splint_legs_preview'
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
