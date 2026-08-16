#!/usr/bin/env python3
"""Generate a net-new-geometry HYPER-RARE legendary helmet for all three
classes with a SECOND, distinct helmet silhouette: a tall VERTICAL CREST /
PLUME rising straight up from the crown of the head.

  helmet_warrior_legendary2  "Legion War-Crest"   (crimson horsehair crest)
  helmet_mage_legendary2     "Astral Spire Circlet" (amethyst crystal spire)
  helmet_ranger_legendary2   "Falcon War-Plume"    (hawk-feather plume)

Why this is a NEW silhouette (not a recolor, not a repeat):
  - Wyrmhorn Warhelm / Starweaver's Crown / Plumed Hood all flare a PAIR of
    accents UP-and-OUTWARD to the sides (wide profile).
  - The crest is a single NARROW, TALL fin on the top-centre of the head — a
    completely different profile (mohawk/plume vs. horns/fans).

Authoring philosophy is identical to gen_horned_legendary_helm.py /
gen_mage_crown_legendary.py: build per-frame from an existing helmet
silhouette (recolour via per-frame luminance-quantile mapping onto a class
3-tone ramp) then draw the net-new accent ONLY in out-of-silhouette space.

Connectivity is guaranteed BY CONSTRUCTION: the crest is centred on the
column of the frame's topmost opaque pixel (`anchor_x`) and starts one row
above it (`anchor_y-1`). Every crest row shares column `anchor_x`, so the whole
fin is one 4-connected blob, and its root pixel sits directly above the opaque
crown pixel, fusing it to the helm. All crest pixels are above the topmost
opaque row, so nothing ever overpaints the helm. Height is clamped per-frame so
the tip never crosses y=2 (QA head zone); the leaf profile always tapers to a
1px tip so a shortened crest (mage cone) still reads as a spire.

Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_crest_legendary.py
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Y_MIN = 2                 # crest tip must stay at y>=2 (QA head zone)
CH_TARGET = 11            # nominal crest height in px (rows above the crown)

# Per-class config: body source sheet, body 3-tone ramp + quantile thresholds,
# crest palette (lit / mid / dark / outer-edge / tip), and max crest width.
CLASSES = {
    'warrior': dict(
        body='helmet_rare1', out_dir='_crest_legendary_preview',
        out='helmet_warrior_legendary2',
        D=(58, 50, 38), M=(120, 104, 74), L=(202, 182, 132),  # brass galea
        Q_LO=0.82, Q_HI=1.20,
        CL=(232, 86, 70), CM=(196, 40, 36), CD=(126, 20, 20),
        CE=(74, 10, 10), CT=(250, 150, 120),                  # crimson crest
        wmax=3),
    'mage': dict(
        body='helmet_mage4', out_dir='_crest_legendary_preview',
        out='helmet_mage_legendary2',
        D=(46, 34, 96), M=(96, 74, 190), L=(196, 186, 250),   # cosmic
        Q_LO=0.85, Q_HI=1.18,
        CL=(236, 214, 255), CM=(176, 116, 232), CD=(112, 62, 172),
        CE=(70, 40, 110), CT=(255, 224, 130),                 # amethyst+gold tip
        wmax=2),
    'ranger': dict(
        body='helmet_ranger4', out_dir='_crest_legendary_preview',
        out='helmet_ranger_legendary2',
        D=(20, 44, 18), M=(44, 86, 34), L=(120, 150, 80),     # forest
        Q_LO=0.85, Q_HI=1.18,
        CL=(238, 228, 200), CM=(150, 96, 54), CD=(92, 58, 34),
        CE=(52, 34, 20), CT=(250, 240, 214),                  # hawk plume
        wmax=3),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def crest_widths(h, wmax):
    """Leaf/plume profile over h rows (i=0 root .. i=h-1 tip): width grows to a
    mid bulge then tapers to a 1px point, so any truncation still ends in a
    tip. Root width 1 keeps the base a single column (clean fuse to the helm)."""
    if h <= 1:
        return [1]
    mid = (h - 1) / 2.0
    ws = []
    for i in range(h):
        w = 1 + (wmax - 1) * (1.0 - abs(i - mid) / mid)
        ws.append(max(1, int(round(w))))
    ws[0] = 1
    ws[-1] = 1
    return ws


def draw_crest(fr, a, cfg):
    """Draw one vertical crest centred on the frame's top-centre crown pixel.
    Returns list of painted (x,y)."""
    ys, xs = np.where(a)
    top = int(ys.min())
    anchor_x = int(round(np.median(xs[ys == top])))
    anchor_y = top
    room = anchor_y - 1 - Y_MIN + 1           # rows available above the crown
    h = max(1, min(CH_TARGET, room))
    ws = crest_widths(h, cfg['wmax'])
    painted = []
    for i, w in enumerate(ws):               # i=0 root (just above crown)
        y = anchor_y - 1 - i
        is_tip = (i == len(ws) - 1)
        half = w // 2
        for dx in range(-half, half + 1 if w % 2 else half):
            x = anchor_x + dx
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                       # never overpaint the helm
                continue
            off = abs(dx)
            if is_tip and dx == 0:
                rgb = cfg['CT']
            elif w >= 3 and off == half:      # outer column -> outline
                rgb = cfg['CE']
            elif dx <= 0:                     # left face shaded / centre lit
                rgb = cfg['CL'] if dx == 0 else cfg['CM']
            else:                             # right face darker
                rgb = cfg['CD']
            # feather / horsehair barb notches every other row on the body
            if (not is_tip) and i % 2 == 1 and rgb == cfg['CM']:
                rgb = cfg['CD']
            put(fr, y, x, rgb)
            painted.append((x, y))
    return painted


def build(base, cfg):
    out = np.zeros_like(base)
    D, M, L = cfg['D'], cfg['M'], cfg['L']
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        # 1. quantized body recolor
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < cfg['Q_LO'] else (L if q > cfg['Q_HI'] else M)
            put(fr, y, x, tone)
        # 2. net-new vertical crest above the crown
        draw_crest(fr, a, cfg)
    return out


def main():
    for name, cfg in CLASSES.items():
        os.makedirs(cfg['out_dir'], exist_ok=True)
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['body'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.16, adj_max=0.24)
            dst = '%s/%s%s.png' % (cfg['out_dir'], cfg['out'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %s  (opaque_px=%d)' % (
                dst, int((arr[..., 3] > 0).sum())))


if __name__ == '__main__':
    main()
