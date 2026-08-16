#!/usr/bin/env python3
"""Generate the matching net-new-geometry legs for the "Divine Seraph" warrior
legendary set — Seraph Greaves (pants) + Seraph Sabatons (winged boots).

Same authoring philosophy as gen_winged_legendary.py: build per-frame from an
existing garment silhouette (pants_rare1[_f] / boots_rare1[_f]) so every pose /
animation is tracked, then draw NET-NEW feather geometry anchored to per-frame
garment edges. This goes beyond a palette recolor and pairs with the already
staged Divine Seraph Plate chest (gold plate + angel wings + halo).

  * Greaves: gold-plate recolor + a pair of hanging feathered hip-tassets that
    sweep down-and-outward from each hip (mirrored L/R).
  * Sabatons: gold-plate recolor + a pair of small ANGEL ANKLE-WINGS (Hermes
    motif) fanning up-and-outward from the outer-top edge of each foot.

Accents are drawn ONLY in transparent (out-of-silhouette) space and share an
edge with the garment, so each accent is one connected component with the body
(QA-safe: no isolated pixels, no multi-component frames). Sleep frames (fi>=60,
lying down) get the gold recolor only — no accents — mirroring the winged shirt
and how hats are suppressed on sleep frames.

Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_seraph_legs.py
Then QA (note: accents intentionally extend outside the normal silhouette):
  python3 scripts/sprite_qa.py _seraph_legs_preview/pants_warrior_legendary1.png --y-max 62
  python3 scripts/sprite_qa.py _seraph_legs_preview/boots_warrior_legendary1.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Divine gold/white body ramp (shadow / base / highlight) — matches the chest
D = (150, 104, 32)     # deep gold shadow
M = (222, 176, 70)     # gold base
L = (250, 232, 168)    # pale gold highlight

# Feather palette (light -> shadow) + outer edge — matches the chest wings
FE_L = (250, 250, 255)
FE_M = (216, 222, 244)
FE_D = (176, 186, 220)
FE_ED = (110, 120, 164)   # outer / feather-separator outline
ROOT = (232, 236, 250)


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a):
    """Quantized gold/white recolor of the legendary silhouette (matches chest)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def feather_tone(dy, off, outer):
    """Pick a feather tone for a pixel at outward offset `off`, edge at `outer`."""
    if off >= outer:
        rgb = FE_ED
    elif off >= outer - 1:
        rgb = FE_D
    elif off <= 1:
        rgb = FE_L
    else:
        rgb = FE_M
    if dy % 2 == 1 and off >= outer - 2 and rgb == FE_M:
        rgb = FE_D
    return rgb


# ── Greaves: hanging hip-tasset (down-and-out) ────────────────────────────────
# dy (rows below the hip anchor) -> outward reach from the edge column.
TASSET = {0: 1, 1: 2, 2: 3, 3: 3, 4: 2, 5: 1}


def draw_tasset(fr, a, edge_x, anchor_y, sign):
    """One feathered hip-tasset hanging from (anchor_y, edge_x), fanning out."""
    for dy, outer in TASSET.items():
        y = anchor_y + dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                 # never overpaint the body
                continue
            put(fr, y, x, feather_tone(dy, off, outer))


# ── Sabatons: ankle-wing (up-and-out) ─────────────────────────────────────────
# dy (rows ABOVE / at the ankle) -> outward reach from the edge column.
AWING = {0: 2, 1: 3, 2: 4, 3: 4, 4: 3, 5: 2}


def draw_ankle_wing(fr, a, edge_x, ankle_y, sign):
    """One ankle-wing fanning up-and-outward from (ankle_y, edge_x)."""
    for dy, outer in AWING.items():
        y = ankle_y - dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                 # never overpaint the body
                continue
            put(fr, y, x, feather_tone(dy, off, outer))


def side_anchor(a, sign, band=4):
    """Return (edge_x, anchor_y) for the given side from silhouette mask `a`.

    Anchor at the TOP band of the silhouette (hip for pants, ankle for boots):
    anchor_y = silhouette top row; edge_x = outermost opaque column found within
    the top `band` rows on that side. This roots the accent at the hip/ankle
    corner, never mid-leg, and always shares an edge with the body."""
    ys, xs = np.where(a)
    top_y = int(ys.min())
    band_mask = a[top_y:top_y + band, :]
    bxs = np.where(band_mask.any(axis=0))[0]
    edge_x = int(bxs.min()) if sign < 0 else int(bxs.max())
    # anchor_y = the top row that actually has a pixel at edge_x (guarantees the
    # off=1 accent pixel is edge-adjacent to the body for connectivity)
    col = np.flatnonzero(a[top_y:top_y + band, edge_x])
    anchor_y = top_y + int(col.min()) if col.size else top_y
    return edge_x, anchor_y


def build_greaves(base):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a)
        if fi >= 60:                    # sleep: body only
            continue
        # hip anchors: outer-top corner of each side, root shares an edge w/ body
        for sign in (-1, +1):
            edge_x, anchor_y = side_anchor(a, sign)
            draw_tasset(fr, a, edge_x, anchor_y, sign)
    return out


def build_sabatons(base):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a)
        if fi >= 60:                    # sleep: body only
            continue
        for sign in (-1, +1):
            edge_x, anchor_y = side_anchor(a, sign)
            draw_ankle_wing(fr, a, edge_x, anchor_y, sign)
    return out


def main():
    os.makedirs('_seraph_legs_preview', exist_ok=True)
    jobs = [
        ('pants_rare1', 'pants_warrior_legendary1', build_greaves),
        ('boots_rare1', 'boots_warrior_legendary1', build_sabatons),
    ]
    for src_stem, dst_stem, builder in jobs:
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (src_stem, suffix))
            arr = builder(base)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '_seraph_legs_preview/%s%s.png' % (dst_stem, suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %s  (opaque_px=%d)' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
