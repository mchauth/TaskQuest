#!/usr/bin/env python3
"""Generate a net-new-geometry HYPER-RARE legendary warrior helmet —
"Wyrmhorn Warhelm" (helmet_warrior_legendary1 + _f).

Same authoring philosophy as gen_winged_legendary.py: build per-frame from an
existing helmet silhouette (helmet_rare1[.png/_f]) so every pose/animation is
tracked, then draw NET-NEW accent geometry (a pair of curved dragon HORNS)
anchored to per-frame skull-dome metrics (head_top, cx). This goes beyond a
palette recolor — the horns give a dramatic bigger-than-normal silhouette, the
first net-new geometry in the *helmet* slot (the winged Seraph is a chest).

Horns are drawn ONLY in out-of-silhouette space to the left/right above the
helm (real horns sweep up-and-out from the temples). Each horn base sits at the
helm's top-side edge so it is one connected component with the helm (QA-safe);
the recoloured helm is drawn first so the horns never overpaint it. Horns are
rigid bone, so — unlike the fluttering wings — they simply track the head
position per frame (no flutter), which is both cleaner and more physically
correct. Helmets have no sleep frames (42 active); empty frames are skipped.

Body recolor: helmet V quantized into a dark-iron 3-tone ramp so the pale bone
horns pop. Shading applied in-script via shade(); do NOT run sprite_shade.py
again on the output.

Run from repo root:
  python3 scripts/gen_horned_legendary_helm.py
Then QA (note: horns intentionally extend outside the normal helm silhouette):
  python3 scripts/sprite_qa.py \
    _horned_legendary_preview/helmet_warrior_legendary1.png --y-min 2
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402
from rebuild_class_hats import make_head_dome_fn        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.82, 1.20

# Dark-iron body ramp (shadow / base / highlight)
D = (38, 40, 48)      # deep iron shadow
M = (78, 82, 94)      # iron base
L = (150, 156, 172)   # steel highlight

# Bone / ivory horn palette (highlight -> shadow) + outer outline
HN_L = (240, 234, 210)
HN_M = (208, 198, 166)
HN_D = (150, 140, 110)
HN_ED = (92, 84, 62)     # horn outline / feather-separator
ROOT = (170, 160, 128)   # dim bone at the horn root

# Horn silhouette: dy (rows ABOVE head_top) -> (inner_off, outer_off) from cx.
# Sweeps up and outward, then tapers to a 1px hooked tip.
HORN = {
    0: (3, 5), 1: (4, 6), 2: (5, 7), 3: (6, 8), 4: (7, 9),
    5: (8, 10), 6: (9, 11), 7: (10, 11), 8: (11, 11),
}
HH = max(HORN) + 1


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def draw_horn(fr, a, cx, head_top, sign):
    """Draw one horn on the given side. Only paints where the base helm is
    transparent (outside the silhouette). Returns painted (x,y) list."""
    painted = []
    # root bridge: tie the horn base to the helm's ACTUAL edge on this side.
    # The helm edge varies row-to-row (narrow at head_top, wider just below),
    # so a fixed offset can miss it; instead close the gap between the horn's
    # base-inner column and the real helm edge at the base rows.
    horn_inner_x = cx + sign * HORN[0][0]
    for ry in (head_top, head_top + 1):
        if not (0 <= ry < FH):
            continue
        row = np.where(a[ry])[0]
        if row.size == 0:
            continue
        edge = int(row.max()) if sign > 0 else int(row.min())
        lo, hi = sorted((edge, horn_inner_x))
        for rx in range(lo, hi + 1):
            if 0 <= rx < FW and not a[ry, rx]:
                put(fr, ry, rx, ROOT)
                painted.append((rx, ry))
    for dy, (inner, outer) in HORN.items():
        y = head_top - dy
        xin = cx + sign * inner
        xout = cx + sign * outer
        lo, hi = (xin, xout) if sign > 0 else (xout, xin)
        for x in range(lo, hi + 1):
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                     # never overpaint the helm
                continue
            off = abs(x - cx)
            if off >= outer:                # outer edge -> outline
                rgb = HN_ED
            elif off <= inner + 1:          # inner face catches light
                rgb = HN_L
            elif off >= outer - 1:          # just inside the edge -> shadow
                rgb = HN_D
            else:
                rgb = HN_M
            # ridge notches: darken a step every 3rd row for horn segmentation
            if dy % 3 == 2 and rgb == HN_M:
                rgb = HN_D
            put(fr, y, x, rgb)
            painted.append((x, y))
    return painted


def build(base, dome):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue                        # empty / sleep frame -> skip
        fr = out[sl]

        # ── 1. quantized dark-iron recolor of the helm silhouette ────────────
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            put(fr, y, x, tone)

        # ── 2. per-frame head metrics ───────────────────────────────────────
        ys, xs = np.where(a)
        hp = dome(fi)
        cx = hp[1] if hp else int(round(xs.mean()))
        head_top = hp[0] if hp else int(ys.min())

        # ── 3. horns (both sides), helm already drawn underneath ─────────────
        draw_horn(fr, a, cx, head_top, -1)
        draw_horn(fr, a, cx, head_top, +1)
    return out


def main():
    for suffix, skin in (('', 'skin_m1.png'), ('_f', 'skin_f1.png')):
        base = load('helmet_rare1%s.png' % suffix)
        skin_sheet = load(skin)
        dome = make_head_dome_fn(skin_sheet)
        arr = build(base, dome)
        arr = shade(arr, adj_min=-0.16, adj_max=0.24)
        os.makedirs('_horned_legendary_preview', exist_ok=True)
        dst = '_horned_legendary_preview/helmet_warrior_legendary1%s.png' % suffix
        Image.fromarray(arr).save(dst)
        print('wrote %s  (opaque_px=%d)' % (dst, int((arr[..., 3] > 0).sum())))


if __name__ == '__main__':
    main()
