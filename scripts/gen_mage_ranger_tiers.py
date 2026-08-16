#!/usr/bin/env python3
"""Generate mage & ranger armor tiers 2-6 (male + female) from the tier 1 sheets.

Method: hue-preserving palette remap of the tier 1 sprites. Silhouettes stay
pixel-identical (female tier 1 items already share the warrior female
templates exactly: shirt 91px / leggings 252px / boots 59px in frame 0), so
recoloring in place is silhouette-safe -- female pants remain leggings.

Per slot:
  shirts : palette remap; tiers 4-6 get 1px collar + cuff trim in the tier
           accent; mage t3 shoulder rune dots, t4 azure chest stripe,
           t6 center rune line; shaded with ADJ_MIN=-0.20 ADJ_MAX=0.25.
  pants  : palette remap; seam lines at thigh/knee and knee/shin (V*0.60),
           edge darkening (V*0.75); default shading.
  boots  : palette remap + 1px cuff trim in the tier accent; default shading.
  helmets: palette remap (male only); default shading.

Run from repo root:  python3 scripts/gen_mage_ranger_tiers.py
Then QA:  sprite_qa.py (shirts/helmets), --y-max 62 (pants), --y-max 63 (boots)
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sprite_shade

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAR = os.path.join(ROOT, 'sprites', 'preview_assets', 'char') + os.sep
FW, FH, COLS, NFR = 80, 64, 10, 70

OUTLINE_V = 0.125   # pixels at/below this V are outline -- never recolored

# ── Tier palettes ────────────────────────────────────────────────────────────

MAGE = {
    2: dict(base='#5A189A', trim='#C0C0C0', accent='#C0C0C0'),
    3: dict(base='#2D1B69', trim='#C0C0C0', accent='#C0C0C0'),
    4: dict(base='#1A1A5E', trim='#FFD700', accent='#FFD700', azure='#40C4FF'),
    5: dict(base='#0D0D2B', trim='#FFD700', accent='#FFD700', shimmer=True),
    6: dict(base='#0A0A1A', trim='#F0E68C', accent='#F0E68C', purple='#9B59B6'),
}

# leather sub-classes: brown (matte leather), strap (bright saturated orange
# straps/buckles), tan (low-sat khaki patches). Modes: ('scale', k) keeps hue
# and multiplies V; ('target', '#hex') remaps to the target color V-scaled.
RANGER = {
    2: dict(green='#3A6B35', brown=('scale', 0.78), strap=('scale', 0.80),
            tan=('scale', 0.85), accent='#3B2A1A'),
    3: dict(green='#1F4718', brown=('scale', 0.85), strap=('scale', 0.90),
            tan=('target', '#C3B091'), accent='#C3B091'),
    4: dict(green='#1A3A15', brown=('scale', 0.62), strap=('target', '#C0C0C0'),
            tan=('scale', 0.62), accent='#C0C0C0'),
    5: dict(green='#0F2E0A', brown=('scale', 0.55), strap=('target', '#B87333'),
            tan=('scale', 0.55), accent='#B87333'),
    6: dict(green='#050D04', brown=('target', '#2D5A27'), strap=('target', '#8B6914'),
            tan=('target', '#8B6914'), accent='#8B6914'),
}

# ── Color helpers ────────────────────────────────────────────────────────────

def hx(hexs):
    return tuple(int(hexs[i:i + 2], 16) for i in (1, 3, 5))

def hsv1(hexs):
    r, g, b = [c / 255.0 for c in hx(hexs)]
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    if d < 1e-9:
        h = 0.0
    elif mx == r:
        h = (60.0 * ((g - b) / d)) % 360.0
    elif mx == g:
        h = 60.0 * ((b - r) / d) + 120.0
    else:
        h = 60.0 * ((r - g) / d) + 240.0
    s = 0.0 if mx == 0 else d / mx
    return h, s, mx

def to_hsv(rgb):
    rf = rgb.astype(np.float32) / 255.0
    r, g, b = rf[:, 0], rf[:, 1], rf[:, 2]
    mx = rf.max(1)
    mn = rf.min(1)
    d = mx - mn
    h = np.zeros_like(mx)
    m = d > 1e-9
    i = m & (mx == r)
    h[i] = (60.0 * ((g - b)[i] / d[i])) % 360.0
    i = m & (mx == g) & (mx != r)
    h[i] = 60.0 * ((b - r)[i] / d[i]) + 120.0
    i = m & (mx == b) & (mx != r) & (mx != g)
    h[i] = 60.0 * ((r - g)[i] / d[i]) + 240.0
    s = np.where(mx > 0, d / np.maximum(mx, 1e-9), 0.0)
    return h, s, mx

def from_hsv(h, s, v):
    h6 = (h % 360.0) / 60.0
    i = np.floor(h6).astype(np.int64) % 6
    f = h6 - np.floor(h6)
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    sel = [i == k for k in range(6)]
    r = np.select(sel, [v, q, p, p, t, v])
    g = np.select(sel, [t, v, v, q, p, p])
    b = np.select(sel, [p, p, t, v, v, q])
    return np.clip(np.stack([r, g, b], 1) * 255.0 + 0.5, 0, 255).astype(np.uint8)

def frames():
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        yield slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW)

def load(name):
    return np.array(Image.open(CHAR + name).convert('RGBA'))

# ── Palette remap ────────────────────────────────────────────────────────────

def recolor_mage(arr, tier):
    P = MAGE[tier]
    out = arr.copy()
    op = out[..., 3] > 10
    rgb = out[..., :3][op]
    h, s, v = to_hsv(rgb)
    touch = v > OUTLINE_V
    base = touch & (h >= 215) & (h <= 315)
    trim = touch & (h >= 35) & (h <= 70) & (s >= 0.40)

    nh, ns, nv = h.copy(), s.copy(), v.copy()
    if base.any():
        vref = float(np.median(v[base]))
        th, ts, tv = hsv1(P['base'])
        ratio = np.clip(v / max(vref, 1e-3), 0.45, 1.8) ** 0.9
        nh[base] = th
        ns[base] = np.clip(0.75 * ts + 0.25 * s[base], 0.0, 1.0)
        nv[base] = np.clip(tv * ratio[base], 0.045, 1.0)
        if P.get('shimmer'):                       # t5: subtle purple shimmer
            hi = base & (ratio > 1.30)
            nh[hi] = 268.0
            ns[hi] = ns[hi] * 0.85
            nv[hi] = np.clip(nv[hi] * 1.5, 0.0, 0.40)
        if 'purple' in P:                          # t6: bright purple accents
            hi = base & (ratio > 1.32)
            ph, ps, pv = hsv1(P['purple'])
            nh[hi] = ph
            ns[hi] = ps
            nv[hi] = np.clip(pv * np.clip(ratio[hi] / 1.6, 0.75, 1.05), 0.0, 0.62)
    if trim.any():
        vref = float(np.median(v[trim]))
        th, ts, tv = hsv1(P['trim'])
        ratio = np.clip(v / max(vref, 1e-3), 0.5, 1.4)
        nh[trim] = th
        ns[trim] = ts
        nv[trim] = np.clip(tv * ratio[trim], 0.10, 1.0)

    out[..., :3][op] = from_hsv(nh, ns, nv)
    return out

def recolor_ranger(arr, tier):
    P = RANGER[tier]
    out = arr.copy()
    op = out[..., 3] > 10
    rgb = out[..., :3][op]
    h, s, v = to_hsv(rgb)
    touch = v > OUTLINE_V
    green = touch & (h >= 70) & (h <= 165)
    leather = touch & (h >= 4) & (h < 48)
    strap = leather & (s > 0.72) & (v > 0.45)
    tan = leather & (s < 0.45) & ~strap
    brown = leather & ~strap & ~tan

    nh, ns, nv = h.copy(), s.copy(), v.copy()
    if green.any():
        vref = float(np.median(v[green]))
        th, ts, tv = hsv1(P['green'])
        ratio = np.clip(v / max(vref, 1e-3), 0.45, 1.8) ** 0.9
        nh[green] = th
        ns[green] = np.clip(0.75 * ts + 0.25 * s[green], 0.0, 1.0)
        nv[green] = np.clip(tv * ratio[green], 0.05, 1.0)
    for mask, mode in ((brown, P['brown']), (strap, P['strap']), (tan, P['tan'])):
        if not mask.any():
            continue
        kind, val = mode
        if kind == 'scale':
            nv[mask] = np.clip(v[mask] * val, 0.05, 1.0)
        else:
            vref = float(np.median(v[mask]))
            th, ts, tv = hsv1(val)
            ratio = np.clip(v[mask] / max(vref, 1e-3), 0.5, 1.6) ** 0.9
            nh[mask] = th
            ns[mask] = ts
            nv[mask] = np.clip(tv * ratio, 0.05, 1.0)

    out[..., :3][op] = from_hsv(nh, ns, nv)
    return out

# ── Slot detail passes ───────────────────────────────────────────────────────

def _setpx(fr, y, x, hexs, k=1.0):
    r, g, b = hx(hexs)
    fr[y, x, 0] = min(255, int(r * k))
    fr[y, x, 1] = min(255, int(g * k))
    fr[y, x, 2] = min(255, int(b * k))
    fr[y, x, 3] = 255

def shirt_details(arr, cls, tier, P):
    acc = P['accent']
    for sy, sx in frames():
        fr = arr[sy, sx]
        a = fr[..., 3] > 10
        if not a.any():
            continue
        vmax = fr[..., :3].astype(np.float32).max(-1) / 255.0
        ys, xs = np.where(a)
        x0, x1 = int(xs.min()), int(xs.max())
        y0, y1 = int(ys.min()), int(ys.max())
        w = max(1, x1 - x0)
        hh = max(1, y1 - y0)
        cols = np.unique(xs)
        top = {int(x): int(ys[xs == x].min()) for x in cols}
        bot = {int(x): int(ys[xs == x].max()) for x in cols}

        if tier >= 4:   # 1px collar + cuff trim in the tier accent
            for x in top:
                rel = (x - x0) / w
                if 0.30 <= rel <= 0.70 and top[x] <= y0 + 1:
                    _setpx(fr, top[x], x, acc)
                if rel <= 0.18 or rel >= 0.82:
                    _setpx(fr, bot[x], x, acc, 0.9)
        if cls == 'mage':
            if tier == 3:   # silver shoulder rune dots
                for relx in (0.16, 0.84):
                    x = min(top, key=lambda c: abs(c - (x0 + relx * w)))
                    _setpx(fr, top[x], x, '#C0C0C0')
            if tier == 4:   # bright azure chest stripe
                yr = int(round(y0 + 0.45 * hh))
                for x in top:
                    rel = (x - x0) / w
                    if (0.30 <= rel <= 0.70 and top[x] <= yr <= bot[x]
                            and fr[yr, x, 3] > 10 and vmax[yr, x] > OUTLINE_V):
                        _setpx(fr, yr, x, P['azure'])
            if tier == 6:   # pale gold center rune line
                xc = int(round(x0 + 0.5 * w))
                for y in range(int(y0 + 0.30 * hh), int(y0 + 0.62 * hh) + 1):
                    if fr[y, xc, 3] > 10 and vmax[y, xc] > OUTLINE_V:
                        _setpx(fr, y, xc, P['trim'], 0.95)

def boots_details(arr, acc):
    for sy, sx in frames():
        fr = arr[sy, sx]
        a = fr[..., 3] > 10
        if not a.any():
            continue
        vmax = fr[..., :3].astype(np.float32).max(-1) / 255.0
        ys, xs = np.where(a)
        for x in np.unique(xs):
            yy = ys[xs == x]
            y = int(yy.min())
            if vmax[y, x] <= OUTLINE_V and (yy == y + 1).any():
                y += 1                       # skip outline row, trim below it
            if vmax[y, x] > OUTLINE_V:
                _setpx(fr, y, x, acc, 0.95)

def pants_details(arr):
    """Seam lines at thigh/knee and knee/shin (V*0.60) + edge darkening (V*0.75)."""
    for sy, sx in frames():
        fr = arr[sy, sx]
        a = fr[..., 3] > 10
        if not a.any():
            continue
        rgb = fr[..., :3].astype(np.float32)
        vmax = rgb.max(-1) / 255.0
        paintable = a & (vmax > OUTLINE_V)
        ys = np.where(a)[0]
        y0, y1 = int(ys.min()), int(ys.max())
        hh = max(1, y1 - y0)
        pad = np.pad(a, 1)
        interior = (pad[:-2, 1:-1] & pad[2:, 1:-1] &
                    pad[1:-1, :-2] & pad[1:-1, 2:])
        mult = np.ones(a.shape, np.float32)
        mult[~interior] = 0.75                                # edge darkening
        for r in (int(round(y0 + 0.38 * hh)), int(round(y0 + 0.70 * hh))):
            mult[r, :] = 0.60                                 # seam lines
        mult = np.where(paintable, mult, 1.0)
        fr[..., :3] = np.clip(rgb * mult[..., None], 0, 255).astype(np.uint8)

# ── Shading wrapper ──────────────────────────────────────────────────────────

def shade(arr, adj_min=-0.12, adj_max=0.30):
    sprite_shade.ADJ_MIN = adj_min
    sprite_shade.ADJ_MAX = adj_max
    sprite_shade.BELL_WIDTH = 0.7
    sprite_shade.X_ADJ = sprite_shade._build_x_adj_lut()
    out, _ = sprite_shade.shade_sheet(arr)
    return out

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    made = []
    for cls, rec, pal in (('mage', recolor_mage, MAGE),
                          ('ranger', recolor_ranger, RANGER)):
        for tier in range(2, 7):
            P = pal[tier]
            jobs = [
                ('shirt',  'shirt_%s1.png' % cls,    'shirt_%s%d.png' % (cls, tier)),
                ('shirt',  'shirt_%s1_f.png' % cls,  'shirt_%s%d_f.png' % (cls, tier)),
                ('pants',  'pants_%s1.png' % cls,    'pants_%s%d.png' % (cls, tier)),
                ('pants',  'pants_%s1_f.png' % cls,  'pants_%s%d_f.png' % (cls, tier)),
                ('boots',  'boots_%s1.png' % cls,    'boots_%s%d.png' % (cls, tier)),
                ('boots',  'boots_%s1_f.png' % cls,  'boots_%s%d_f.png' % (cls, tier)),
                ('helmet', 'helmet_%s1.png' % cls,   'helmet_%s%d.png' % (cls, tier)),
            ]
            for slot, src, dst in jobs:
                arr = rec(load(src), tier)
                if slot == 'shirt':
                    shirt_details(arr, cls, tier, P)
                elif slot == 'boots':
                    boots_details(arr, P['accent'])
                elif slot == 'pants':
                    pants_details(arr)
                if slot == 'shirt':
                    arr = shade(arr, adj_min=-0.20, adj_max=0.25)
                else:
                    arr = shade(arr)
                Image.fromarray(arr).save(CHAR + dst)
                made.append(dst)
                print('wrote %s' % dst)
    print('%d sheets generated' % len(made))

if __name__ == '__main__':
    main()
