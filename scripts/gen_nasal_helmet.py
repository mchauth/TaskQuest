#!/usr/bin/env python3
"""ELEVENTH net-new-geometry HELMET showcase per class — a NASAL BAR: a vertical
nose-guard ridge running down the centre of the face from the brow, the defining
feature of a nasal helm. This brings the helmet slot to ELEVEN distinct axes. It is
the central-vertical-faceguard axis none of the ten existing legendary helmets
occupy:

  * legendary1 (base)      — plain dome.
  * legendary2 (crest)     — a tall vertical crest (silhouette, on TOP).
  * legendary3 (winghelm)  — wide side wings (silhouette).
  * legendary4 (aventail)  — a mail drape hanging below.
  * legendary5 (visor)     — a forward FULL faceplate + eye-slit.
  * legendary6 (antler)    — a branching antler rack (silhouette).
  * legendary7 (diadem)    — a jewelled brow-band (across the brow).
  * legendary8 (comb)      — a vertical median comb down the crown (above the face).
  * legendary9 (cheek)     — paired lateral cheek-plates framing the face.
  * legendary10 (rivet-rim)— a horizontal riveted band low on the rim.
  * this NASAL BAR runs a single VERTICAL ridge down the FACE centre (brow to
    chin) — the central-nose-guard axis, distinct from the crown comb (top, not
    face), the full visor plate, and the lateral cheek-plates. A flat repaint that
    adds no silhouette pixels; where the eye slit is open it simply forms a ridge
    around the opening.

Authoring philosophy is identical to gen_rivet_helmet.py: nasal pixels are painted
ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — QA-safe by construction. Painted on
the LARGEST helm component per frame only.

Sleep frames (fi>=60) get the recolor only — no nasal. Shading applied in-script via
shade(); do NOT run sprite_shade.py again.

Per class the ridge hue is the class accent family:
  * warrior "Warlord's Nasal Helm"   — dark-iron body + steel ridge, gold brow-boss
  * mage    "Astral Nasal Circlet"    — cosmic-indigo body + silver ridge, cyan brow-boss
  * ranger  "Warden's Nose-Guard"     — forest body + bronze ridge, copper brow-boss

Run from repo root:
  python3 scripts/gen_nasal_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _nasal_helmet_preview/helmet_warrior_legendary11.png --y-min 2
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

# Nasal bar spans the vertical face band [NASAL_TOP, NASAL_BOT] of the helm bbox
# height, one lit ridge column at the helm centre-x with a dark shadow column beside.
NASAL_TOP = 0.42
NASAL_BOT = 0.84
MIN_PX = 12

# body : deep shadow / base / highlight
# nasal: RIDGE (lit ridge col) / SHADOW (dark side col) / BOSS (bright brow boss)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary11',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),      # dark iron -> steel
        nasal=((178, 184, 200), (58, 62, 74), (232, 190, 70)),    # steel ridge, dark side, gold boss
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary11',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),       # cosmic indigo -> violet
        nasal=((196, 202, 224), (34, 30, 92), (72, 200, 244)),    # silver ridge, dark side, cyan boss
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary11',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),         # forest green
        nasal=((160, 118, 60), (30, 52, 26), (206, 132, 66)),     # bronze ridge, dark side, copper boss
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


def draw_nasal(fr, comp, pal):
    """Paint a vertical nasal ridge down the face centre of one helm component."""
    RIDGE, SHADOW, BOSS = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cx = 0.5 * (x0 + x1)
    ytop = y0 + NASAL_TOP * h
    ybot = y0 + NASAL_BOT * h
    ridge_top = None
    for y, x in zip(ys, xs):
        if not (ytop <= y <= ybot):
            continue
        if abs(x - cx) < 0.5:
            put(fr, y, x, RIDGE)
            if ridge_top is None or y < ridge_top:
                ridge_top = y
        elif abs(x - (cx + 1.0)) < 0.5:
            put(fr, y, x, SHADOW)
    # bright brow boss at the very top of the ridge
    if ridge_top is not None:
        put(fr, ridge_top, int(round(cx)), BOSS)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['nasal']
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
            helm = (lbl == (int(np.argmax(sizes)) + 1))
            draw_nasal(fr, helm, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_nasal_helmet_preview'
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
