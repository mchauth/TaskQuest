#!/usr/bin/env python3
"""Generate a net-new-geometry HYPER-RARE ranger legendary chest —
"Skyhunter's Wings" (shirt_ranger_legendary1 + _f).

The ranger-class counterpart to the warrior "Divine Seraph Plate"
(gen_winged_legendary.py) and the mage "Starweaver's Wings"
(gen_mage_winged_legendary.py): the FIRST ranger sprite that goes BEYOND a
palette recolor. Completes the "each class has a winged hyper-rare" showcase
trio. Same authoring philosophy — build per-frame from an existing garment
silhouette (shirt_ranger4[_f], the ranger t4 chest that ships full m+f coverage
-> 45 active frames, tracks every pose) recolored via per-frame luminance-
QUANTILE mapping onto a glowing verdant->bronze ramp, then draw NET-NEW accent
geometry (broad HAWK wings) anchored per frame to the skull-dome / shoulder
metrics from the skin sheet.

Distinct from the warrior Seraph AND the mage Starweaver on purpose:
 - warrior wings = white/gold angelic + orbiting star-halo.
 - mage wings    = cool nebula-blue/violet arcane + orbiting star-halo.
 - ranger wings  = natural HAWK plumage (dark-brown trailing, russet vane,
   cream leading edge, dark outline) and NO halo — a grounded hunter's raptor
   wing, not a celestial one. The profile is broader/flatter ("soaring hawk")
   vs. the mages'/warriors' upswept angelic fan, so the silhouette reads as a
   bird of prey, not an angel.
The body ramp is a ranger-family forest-green->bronze->pale-gold (the ranger
tiers are a muted darkening green family, so this stays in-family while glowing
far brighter than any normal chest, and leans bronze rather than the Verdant
Monarch's emerald so it reads as its own item).

QA-safe construction (identical guarantees to the warrior/mage winged gens):
 - wings are drawn ONLY in transparent out-of-silhouette space to the L/R of
   the torso; the body is never overpainted (source silhouette preserved, so
   dropped source px = 0 by construction).
 - a per-pose ROOT bridge (bridge_to_body) connects each wing to the body's
   real per-row shoulder edge, so each wing is a single connected component
   (no floating islands) on every frame.
 - subtle per-frame flutter sweeps the outer feathers +/-1px and lifts the wing
   top +/-1px across an animation row; run/slash rows tuck the wings in 1px.
 - sleep frames (fi>=60, lying down) get body recolor only -- no wings.
Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_ranger_winged_legendary.py
Then QA (wings intentionally extend outside the normal body silhouette, so a
background-bleed flag on the wing columns is expected -- that IS the legendary
silhouette, not strays):
  python3 scripts/sprite_qa.py _ranger_winged_legendary_preview/shirt_ranger_legendary1.png
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

# Ranger legendary body ramp (shadow / base / highlight) -- glowing verdant with
# a warm bronze-gold crown so it stays in the ranger green family but reads as a
# distinct luminous item (leans bronze vs. the Verdant Monarch emerald).
D = (22, 46, 28)       # deep forest shadow
M = (58, 120, 66)      # living emerald base
L = (206, 196, 128)    # pale bronze-gold highlight

# Hawk-plumage feather palette (leading light -> vane -> trailing) + outer edge.
# Natural raptor browns/russets/cream so the wing reads as a bird of prey, NOT
# an angelic or arcane wing. Kept reasonably bright so the shader keeps texture.
FE_L = (238, 224, 190)   # cream leading edge (primary tips catch light)
FE_M = (166, 116, 70)    # russet-brown vane
FE_D = (104, 68, 42)     # dark-brown trailing / feather separator
FE_ED = (58, 38, 26)     # outer / feather-separator outline
ROOT = (150, 108, 66)    # wing root bridge (matches vane so it reads as plume)

# Broad "soaring hawk" wing silhouette: dy (rows from wing top) ->
# (inner_off, outer_off) magnitude from cx. Wider + flatter than the angelic
# fan: the outer span opens fast and holds, tapering to a swept primary tip.
WING = {
    0: (7, 12), 1: (7, 16), 2: (7, 19), 3: (8, 21), 4: (8, 22),
    5: (9, 22), 6: (9, 21), 7: (10, 19), 8: (11, 17), 9: (12, 15),
    10: (13, 13),
}
WH = max(WING) + 1


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def row_of(fi):
    return fi // COLS


def draw_wing(fr, a, cx, shoulder_y, sign, flutter_out, flutter_top):
    """Draw one hawk wing on the given side. Only paints where the base garment
    is transparent (outside the body). Returns list of painted (x,y).

    A per-pose ROOT bridge (see bridge_to_body) closes the ACTUAL gap between
    the body's shoulder edge and the wing inner column, guaranteeing wing+body
    is a single connected component on every frame.
    """
    wing_top = shoulder_y - 3 + flutter_top   # hawk wing sits a touch lower/flatter
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
            off = abs(x - cx)
            if off >= outer - 0:
                rgb = FE_ED
            elif off >= outer - 2:
                rgb = FE_D
            elif off <= inner + 1:
                rgb = FE_L
            else:
                rgb = FE_M
            # feather separations: every 3rd row darken a notch near the tip so
            # individual primaries read on the trailing edge.
            if dy % 3 == 2 and off >= outer - 5 and rgb == FE_M:
                rgb = FE_D
            put(fr, y, x, rgb)
            painted.append((x, y))
    return painted


def bridge_to_body(fr, a, painted):
    """Guarantee the wing is 4-connected to the body by filling a straight ROOT
    line from the wing pixel nearest the body to the nearest body pixel. Pose-
    independent — closes whatever gap this frame has. Only fills currently-
    transparent cells (never overpaints body or wing)."""
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

        # -- 1. quantized verdant recolor of the chest silhouette --------------
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            put(fr, y, x, tone)

        sleeping = fi >= 60
        if sleeping:
            continue  # body-only on sleep frames (no wings)

        # -- 2. per-frame metrics ---------------------------------------------
        ys, xs = np.where(a)
        y0 = int(ys.min())
        hp = dome(fi)
        cx = hp[1] if hp else int(round(xs.mean()))
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

        # -- 3. hawk wings (both sides), each bridged to the body per pose -----
        pl = draw_wing(fr, a, cx, shoulder_y, -1, flutter_out, flutter_top)
        pr = draw_wing(fr, a, cx, shoulder_y, +1, flutter_out, flutter_top)
        bridge_to_body(fr, a, pl)
        bridge_to_body(fr, a, pr)
        # bronze pauldron caps OVER the chest at the wing roots (drawn on body,
        # so no floating components) — read the wings as shoulder-mounted.
        for sgn in (1, -1):
            for dx, dy, col in ((3, 0, L), (4, 0, FE_L), (3, 1, M), (4, 1, FE_M)):
                x, y = cx + sgn * dx, shoulder_y + dy
                if 0 <= x < FW and 0 <= y < FH and a[y, x]:
                    put(fr, y, x, col)
    return out


def main():
    os.makedirs('_ranger_winged_legendary_preview', exist_ok=True)
    for suffix, skin in (('', 'skin_m1.png'), ('_f', 'skin_f1.png')):
        base = load('shirt_ranger4%s.png' % suffix)
        dome = make_head_dome_fn(load(skin))
        arr = build(base, dome)
        arr = shade(arr, adj_min=-0.18, adj_max=0.26)
        dst = '_ranger_winged_legendary_preview/shirt_ranger_legendary1%s.png' % suffix
        Image.fromarray(arr).save(dst)
        n = sum(1 for fi in range(NFR)
                if (arr[(fi // COLS) * FH:(fi // COLS + 1) * FH,
                        (fi % COLS) * FW:(fi % COLS + 1) * FW, 3] > 0).any())
        print('wrote %s  (opaque_px=%d, active_frames=%d)'
              % (dst, (arr[..., 3] > 0).sum(), n))


if __name__ == '__main__':
    main()
