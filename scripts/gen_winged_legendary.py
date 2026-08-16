#!/usr/bin/env python3
"""Generate winged HYPER-RARE legendary — warrior "Divine Seraph Plate"
(shirt_warrior_legendary1 + _f).

Programmatic, in-repo, same authoring philosophy as
redesign_mage_chest_t2_sweater.py: build per-frame from an existing garment
silhouette (shirt_rare1[.png/_f]) so every pose/animation is tracked, then draw
net-new accent geometry (angel WINGS + HALO) anchored to per-frame skull/shoulder
metrics. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Wings are drawn ONLY in out-of-silhouette space to the left/right of the torso
(real wings emerge from behind the back — on the south view only the outer
feathers clear the body). A 1px "wing root" links each wing to the shoulder so
each wing is one connected component (QA-friendly). Subtle per-frame flutter
sweeps the outer feathers ±1px and lifts the wing top ±1px across an animation
row. Sleep frames (fi>=60, lying down) get body recolor only — no wings/halo,
mirroring how hats are suppressed on sleep frames.

Body recolor: T1 legendary V quantized into a gold/white Divine 3-tone ramp.

Run from repo root:
  python3 scripts/gen_winged_legendary.py
Then QA (note: wings intentionally extend outside the normal body silhouette):
  python3 scripts/sprite_qa.py sprites/preview_assets/char/shirt_warrior_legendary1.png
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR
from rebuild_class_hats import make_head_dome_fn

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Divine gold/white body ramp (shadow / base / highlight)
D = (150, 104, 32)     # deep gold shadow
M = (222, 176, 70)     # gold base
L = (250, 232, 168)    # pale gold highlight
OUTLINE = (60, 42, 12)

# Feather palette (light -> shadow) + outer edge
FE_L = (250, 250, 255)
FE_M = (216, 222, 244)
FE_D = (176, 186, 220)
FE_ED = (110, 120, 164)   # outer/feather-separator outline
ROOT = (232, 236, 250)

# Halo
HALO_O = (255, 232, 140)
HALO_I = (255, 250, 214)

# Wing silhouette: dy (rows from wing top) -> (inner_off, outer_off) magnitude
# from cx. Fans up-and-outward then tapers to a lower tip.
WING = {
    0: (8, 11), 1: (8, 14), 2: (8, 16), 3: (9, 17), 4: (9, 18),
    5: (10, 18), 6: (10, 17), 7: (11, 16), 8: (11, 15), 9: (12, 14),
    10: (12, 13),
}
WH = max(WING) + 1


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def row_of(fi):
    return fi // COLS


def draw_wing(fr, a, cx, shoulder_y, sign, flutter_out, flutter_top):
    """Draw one wing on the given side. Only paints where the base garment is
    transparent (outside the body). Returns list of painted (x,y)."""
    wing_top = shoulder_y - 4 + flutter_top
    painted = []
    # root bridge: connect shoulder (body edge) to wing inner at wing_top+2
    root_x = cx + sign * 7
    for ry in (shoulder_y, shoulder_y - 1):
        put(fr, ry, root_x, ROOT)
        painted.append((root_x, ry))
    for dy, (inner, outer) in WING.items():
        outer = outer + flutter_out
        y = wing_top + dy
        xin = cx + sign * inner
        xout = cx + sign * outer
        lo, hi = (xin, xout) if sign > 0 else (xout, xin)
        for x in range(lo, hi + 1):
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:            # never overpaint the body
                continue
            # tone: inner rows light, mid body base, outer edge shaded/outlined
            off = abs(x - cx)
            if off >= outer - 0:
                rgb = FE_ED
            elif off >= outer - 2:
                rgb = FE_D
            elif off <= inner + 1:
                rgb = FE_L
            else:
                rgb = FE_M
            # feather separations: every 3rd row darken a notch near the edge
            if dy % 3 == 2 and off >= outer - 4 and rgb == FE_M:
                rgb = FE_D
            put(fr, y, x, rgb)
            painted.append((x, y))
    return painted


def draw_halo(fr, a, cx, head_top, flutter_top):
    cy = head_top - 4 + flutter_top
    for dx in range(-7, 8):
        x = cx + dx
        # thin ring: top & bottom arcs
        if abs(dx) >= 6:
            put(fr, cy, x, HALO_O)
        if abs(dx) <= 6:
            put(fr, cy - 1, x, HALO_O if abs(dx) >= 5 else HALO_I)
            put(fr, cy, x, HALO_I if abs(dx) <= 5 else HALO_O)


def build(base, skin_sheet, dome):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]

        # ── 1. quantized gold/white recolor of the legendary silhouette ──────
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            put(fr, y, x, tone)

        sleeping = fi >= 60
        if sleeping:
            continue  # body-only on sleep frames (no wings/halo)

        # ── 2. per-frame metrics ─────────────────────────────────────────────
        ys, xs = np.where(a)
        y0 = int(ys.min())
        hp = dome(fi)
        cx = hp[1] if hp else int(round(xs.mean()))
        head_top = hp[0] if hp else y0 - 8
        # shoulder row: top garment row a few px out from center
        sh_cols = [x for x in range(cx - 8, cx + 9) if a[:, x].any()]
        shoulder_y = min(int(np.flatnonzero(a[:, x]).min()) for x in sh_cols) \
            if sh_cols else y0

        # subtle flutter across the animation row
        phase = fi % 4
        flutter_out = (0, 1, 1, 0)[phase]
        flutter_top = (0, -1, -1, 0)[phase]
        # run/slash: wings sweep in a touch (tighter) for motion
        if row_of(fi) in (2, 5):
            flutter_out -= 1

        # ── 3. wings (both sides), then halo on top ──────────────────────────
        draw_wing(fr, a, cx, shoulder_y, -1, flutter_out, flutter_top)
        draw_wing(fr, a, cx, shoulder_y, +1, flutter_out, flutter_top)
        draw_halo(fr, a, cx, head_top, flutter_top)
    return out


def main():
    for suffix, skin in (('', 'skin_m1.png'), ('_f', 'skin_f1.png')):
        base = load('shirt_rare1%s.png' % suffix)
        skin_sheet = load(skin)
        dome = make_head_dome_fn(skin_sheet)
        arr = build(base, skin_sheet, dome)
        arr = shade(arr, adj_min=-0.18, adj_max=0.26)
        os.makedirs('_winged_legendary_preview', exist_ok=True)
        dst = '_winged_legendary_preview/shirt_warrior_legendary1%s.png' % suffix
        Image.fromarray(arr).save(dst)
        print('wrote %s  (opaque_px=%d)' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
