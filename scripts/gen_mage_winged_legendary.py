#!/usr/bin/env python3
"""Generate a net-new-geometry HYPER-RARE mage legendary chest —
"Starweaver's Wings" (shirt_mage_legendary1 + _f).

The mage-class counterpart to the warrior "Divine Seraph Plate"
(gen_winged_legendary.py): the FIRST mage sprite that goes BEYOND a palette
recolor. Same authoring philosophy — build per-frame from an existing garment
silhouette (shirt_mage4[_f], the mage t4 robe that ships full m+f coverage ->
45 active frames, tracks every pose) recolored via per-frame luminance-QUANTILE
mapping onto a cosmic arcane 3-tone ramp, then draw NET-NEW accent geometry
(arcane feathered WINGS + an orbiting STAR-halo) anchored per frame to the
skull-dome / shoulder metrics from the skin sheet.

Distinct from the warrior Seraph on purpose: warrior wings are white/gold
angelic; these are cool arcane starlight wings (nebula-blue vane, cyan-white
leading edge, violet trailing edge) so the piece reads unmistakably as arcane
mage magic and is NOT a recolor of the warrior wing. The body ramp is a mage
cosmic indigo->violet->starlight (mage's tiers are purple/void, so this stays
in-family while glowing far brighter than any normal robe).

QA-safe construction (identical guarantees to gen_winged_legendary.py):
 - wings are drawn ONLY in transparent out-of-silhouette space to the L/R of
   the torso; the body is never overpainted (source silhouette preserved, so
   dropped source px = 0 by construction).
 - a 1px "wing root" bridges each wing to the shoulder edge so each wing is a
   single connected component (no floating islands).
 - subtle per-frame flutter sweeps the outer feathers +/-1px and lifts the wing
   top +/-1px across an animation row; run/slash rows tuck the wings in 1px.
 - sleep frames (fi>=60, lying down) get body recolor only -- no wings/halo,
   mirroring the warrior Seraph + hat sleep-frame convention.
Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_mage_winged_legendary.py
Then QA (wings intentionally extend outside the normal body silhouette, so a
background-bleed flag on the wing columns is expected -- that IS the legendary
silhouette, not strays):
  python3 scripts/sprite_qa.py _mage_winged_legendary_preview/shirt_mage_legendary1.png
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR  # noqa: F401
from rebuild_class_hats import make_head_dome_fn

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Cosmic mage body ramp (shadow / base / highlight) -- arcane indigo->starlight
D = (46, 34, 96)       # deep indigo shadow
M = (96, 74, 190)      # arcane violet base
L = (196, 186, 250)    # pale starlight highlight

# Arcane feather palette (leading light -> vane -> trailing) + outer edge.
# All chosen cool/violet so the wing reads as magical energy, NOT the warrior's
# warm white/gold. Bright values keep the shader from crushing the glow.
FE_L = (224, 246, 255)   # cyan-white leading edge
FE_M = (150, 176, 244)   # nebula-blue vane
FE_D = (110, 120, 214)   # violet trailing / feather-separator
FE_ED = (72, 70, 150)    # outer/feather-separator outline
ROOT = (198, 214, 252)   # wing root bridge

# Orbiting star-halo (warm-cool starlight)
HALO_O = (150, 176, 250)   # outer arc / faint orbit
HALO_I = (236, 244, 255)   # bright star points

# Wing silhouette: dy (rows from wing top) -> (inner_off, outer_off) magnitude
# from cx. Fans up-and-outward then tapers to a lower tip. Same profile as the
# proven warrior Seraph wing so pose-tracking + QA behavior are identical.
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
    transparent (outside the body). Returns list of painted (x,y).

    A solid per-frame ROOT bridge closes the ACTUAL gap between the body's
    shoulder edge and the wing inner column (the mage robe is narrower than the
    warrior plate, so a fixed offset would leave the wing floating — this walks
    to the body's real per-row edge, same idea as the horned-helm root bridge),
    guaranteeing wing+body is a single connected component on every frame.
    """
    wing_top = shoulder_y - 4 + flutter_top
    painted = []
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


def bridge_to_body(fr, a, painted):
    """Guarantee the wing (list of painted (x,y)) is 4-connected to the body by
    filling a straight ROOT line from the wing pixel nearest the body to the
    nearest body pixel. Pose-independent — closes whatever gap this frame has.
    Only fills currently-transparent cells (never overpaints body or wing)."""
    if not painted:
        return
    bys, bxs = np.where(a)
    if len(bxs) == 0:
        return
    best = None
    for (wx, wy) in painted:
        d2 = (bxs - wx) ** 2 + (bys - wy) ** 2
        i = int(d2.argmin())
        dd = int(d2[i])
        if best is None or dd < best[0]:
            best = (dd, wx, wy, int(bxs[i]), int(bys[i]))
    _, wx, wy, bx, by = best
    if best[0] <= 2:            # already touching (4- or 8-neighbour)
        return
    n = max(abs(bx - wx), abs(by - wy))
    for k in range(1, n):       # exclusive of both endpoints
        x = round(wx + (bx - wx) * k / n)
        y = round(wy + (by - wy) * k / n)
        if 0 <= x < FW and 0 <= y < FH and not a[y, x] and fr[y, x, 3] == 0:
            put(fr, y, x, ROOT)


def draw_halo(fr, a, cx, head_top, flutter_top):
    """Orbiting star-ring: 4 bright star points on a faint elliptical orbit."""
    cy = head_top - 4 + flutter_top
    for dx in range(-7, 8):
        x = cx + dx
        # thin faint orbit ring: top & bottom arcs
        if abs(dx) >= 6:
            put(fr, cy, x, HALO_O)
        if abs(dx) <= 6:
            put(fr, cy - 1, x, HALO_O if abs(dx) >= 5 else HALO_I)
            put(fr, cy, x, HALO_I if abs(dx) <= 5 else HALO_O)
    # bright star points at the cardinal orbit positions
    for sx in (-6, -2, 2, 6):
        put(fr, cy - 1, cx + sx, HALO_I)


def build(base, dome):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]

        # ── 1. quantized cosmic recolor of the robe silhouette ───────────────
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

        # ── 3. wings (both sides), each bridged to the body per pose ─────────
        pl = draw_wing(fr, a, cx, shoulder_y, -1, flutter_out, flutter_top)
        pr = draw_wing(fr, a, cx, shoulder_y, +1, flutter_out, flutter_top)
        bridge_to_body(fr, a, pl)
        bridge_to_body(fr, a, pr)
        # arcane shoulder caps OVER the robe at the wing roots (drawn on body,
        # so no floating components) — read the wings as shoulder-mounted.
        for sgn in (1, -1):
            for dx, dy, col in ((3, 0, L), (4, 0, FE_L), (3, 1, M), (4, 1, L)):
                x, y = cx + sgn * dx, shoulder_y + dy
                if 0 <= x < FW and 0 <= y < FH and a[y, x]:
                    put(fr, y, x, col)
    return out


def main():
    os.makedirs('_mage_winged_legendary_preview', exist_ok=True)
    for suffix, skin in (('', 'skin_m1.png'), ('_f', 'skin_f1.png')):
        base = load('shirt_mage4%s.png' % suffix)
        dome = make_head_dome_fn(load(skin))
        arr = build(base, dome)
        arr = shade(arr, adj_min=-0.18, adj_max=0.26)
        dst = '_mage_winged_legendary_preview/shirt_mage_legendary1%s.png' % suffix
        Image.fromarray(arr).save(dst)
        n = sum(1 for fi in range(NFR)
                if (arr[(fi // COLS) * FH:(fi // COLS + 1) * FH,
                        (fi % COLS) * FW:(fi % COLS + 1) * FW, 3] > 0).any())
        print('wrote %s  (opaque_px=%d, active_frames=%d)'
              % (dst, (arr[..., 3] > 0).sum(), n))


if __name__ == '__main__':
    main()
