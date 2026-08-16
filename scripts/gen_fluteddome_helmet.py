#!/usr/bin/env python3
"""TWELFTH net-new-geometry HELMET showcase per class — a FLUTED DOME: a fan of
repeated VERTICAL grooves radiating over the CROWN of the helm (a ribbed/fluted
skullcap). This brings the helmet slot to TWELVE distinct axes. It is the repeated-
parallel-vertical-crown axis none of the eleven existing legendary helmets occupy:

  * legendary1 (base)       — plain dome.
  * legendary2 (crest)      — a tall vertical crest (silhouette, on TOP).
  * legendary3 (winghelm)   — wide side wings (silhouette).
  * legendary4 (aventail)   — a mail drape hanging below.
  * legendary5 (visor)      — a forward FULL faceplate + eye-slit.
  * legendary6 (antler)     — a branching antler rack (silhouette).
  * legendary7 (diadem)     — a jewelled brow-band (across the brow).
  * legendary8 (comb)       — a SINGLE vertical median comb down the crown.
  * legendary9 (cheek)      — paired lateral cheek-plates framing the face.
  * legendary10 (rivet-rim) — a horizontal riveted band low on the rim.
  * legendary11 (nasal)     — a SINGLE vertical nose-guard ridge down the face.
  * this FLUTED DOME lays THREE evenly-spaced VERTICAL grooves fanning across the
    CROWN — the repeated-parallel-vertical-crown axis, distinct from the single
    median comb, the single face-centred nasal ridge, and every band/plate/wing. A
    flat repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_nasal_helmet.py: groove pixels are painted
ONLY onto pixels that are ALREADY opaque body pixels. Painted on the LARGEST helm
component per frame only, and confined to the crown band (above the face). QA-safe
purely by construction — it can never add a pixel outside the existing silhouette.

Sleep frames (fi>=60) get the recolor only. Shading applied in-script via shade();
do NOT run sprite_shade.py again.

Per class the ridge hue is the class accent family:
  * warrior "Warlord's Fluted Sallet"   — dark-iron body + steel ridge, gold apex boss
  * mage    "Astral Ribbed Circlet"      — cosmic-indigo body + silver ridge, cyan apex boss
  * ranger  "Warden's Fluted Hood-Helm"  — forest body + bronze ridge, copper apex boss

Run from repo root:
  python3 scripts/gen_fluteddome_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _fluteddome_helmet_preview/helmet_warrior_legendary12.png --y-min 2
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

# Three crown grooves at fractions of the helm bbox width, confined to the crown
# band [CROWN_TOP, CROWN_BOT] of helm height (above the face). Each groove is a dark
# incision (FIELD) with a lit ridge (EDGE) on its viewer-left. A bright apex BOSS
# tops the centre groove.
GROOVE_FRACS = (0.28, 0.50, 0.72)
CROWN_TOP = 0.04
CROWN_BOT = 0.52
MIN_PX = 12

# body  : deep shadow / base / highlight
# groove: FIELD (dark incision) / EDGE (lit ridge) / BOSS (bright apex boss)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary12',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),      # dark iron -> steel
        groove=((52, 54, 66), (196, 202, 218), (232, 190, 70)),   # dark incision, steel ridge, gold boss
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary12',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),       # cosmic indigo -> violet
        groove=((30, 26, 84), (198, 204, 224), (72, 200, 244)),   # dark incision, silver ridge, cyan boss
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary12',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),         # forest green
        groove=((26, 48, 24), (160, 118, 60), (206, 132, 66)),    # dark incision, bronze ridge, copper boss
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
    """Paint repeated vertical grooves over the crown of one helm component."""
    FIELD, EDGE, BOSS = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    w = max(x1 - x0, 1)
    ytop = y0 + CROWN_TOP * h
    ybot = y0 + CROWN_BOT * h
    grooves = [x0 + f * w for f in GROOVE_FRACS]
    mid_col = []
    for y, x in zip(ys, xs):
        if not (ytop <= y <= ybot):
            continue
        for gi, gc in enumerate(grooves):
            if abs(x - gc) < 0.5:            # the incised groove
                put(fr, y, x, FIELD)
                if gi == 1:
                    mid_col.append((y, x))
                break
            if abs(x - (gc - 1.0)) < 0.5:    # lit ridge on its viewer-left
                put(fr, y, x, EDGE)
                break
    # bright apex boss at the top of the centre groove
    if mid_col:
        y, x = min(mid_col)
        put(fr, y, x, BOSS)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['groove']
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
            draw_flutes(fr, helm, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_fluteddome_helmet_preview'
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
