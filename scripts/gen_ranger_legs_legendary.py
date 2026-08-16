#!/usr/bin/env python3
"""Generate the matching net-new-geometry legs for the ranger "Skyhunter"
legendary set — Skyhunter's Pelt-Tassets (pants) + Skyhunter's Talon Striders
(boots). Ranger counterpart to the warrior Divine Seraph Greaves + Sabatons and
the mage Starweaver's Robe-Tassets + Comet Striders.

Same authoring philosophy as gen_mage_legs_legendary.py: build per-frame from an
existing ranger garment silhouette (pants_ranger4[_f] / boots_ranger4[_f]) so
every pose / animation is tracked, then draw NET-NEW hawk-plumage geometry
anchored to per-frame garment edges. Completes the ranger 4-slot showcase with
the winged chest + plumed hood.

  * Tassets: ranger recolor + a pair of trailing hunter's pelt-tassets that
    sweep down-and-outward from each hip (mirrored L/R) — a feathered streamer.
  * Striders: ranger recolor + a pair of small TALON ankle-fins that fan
    up-and-outward from the outer-top edge of each foot.

Accents are drawn ONLY in transparent (out-of-silhouette) space and share an
edge with the garment, so each accent is one connected component with the body
(QA-safe: no isolated pixels, no multi-component frames). Sleep frames (fi>=60,
lying down) get the recolor only — no accents — matching the winged shirt and
the hat convention.

Body recolor + accent palette match the ranger wings/hood so all four slots read
as one Skyhunter set. Shading applied in-script via shade(); do NOT run
sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_ranger_legs_legendary.py
Then QA (accents intentionally sit at/inside the silhouette; standard flags):
  python3 scripts/sprite_qa.py _ranger_legs_legendary_preview/pants_ranger_legendary1.png --y-max 62
  python3 scripts/sprite_qa.py _ranger_legs_legendary_preview/boots_ranger_legendary1.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Ranger legendary body ramp (shadow / base / highlight) -- matches the wings.
D = (22, 46, 28)       # deep forest shadow
M = (58, 120, 66)      # living emerald base
L = (206, 196, 128)    # pale bronze-gold highlight

# Hawk-plumage accent palette (leading light -> vane -> trailing) + outer edge,
# matches the ranger wings/hood so all four slots read as one Skyhunter set.
FE_L = (238, 224, 190)   # cream leading edge
FE_M = (166, 116, 70)    # russet-brown vane
FE_D = (104, 68, 42)     # dark-brown trailing / separator
FE_ED = (58, 38, 26)     # outer outline


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a):
    """Quantized ranger-family recolor of the legendary silhouette (matches chest)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def accent_tone(dy, off, outer):
    """Pick an accent tone for a pixel at outward offset `off`, edge at `outer`."""
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


# ── Tassets: trailing pelt-streamer (down-and-out) ────────────────────────────
TASSET = {0: 1, 1: 2, 2: 3, 3: 3, 4: 2, 5: 1}


def draw_tasset(fr, a, edge_x, anchor_y, sign):
    for dy, outer in TASSET.items():
        y = anchor_y + dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                 # never overpaint the body
                continue
            put(fr, y, x, accent_tone(dy, off, outer))


# ── Striders: talon ankle-fin (up-and-out) ────────────────────────────────────
AWING = {0: 2, 1: 3, 2: 4, 3: 4, 4: 3, 5: 2}


def draw_ankle_wing(fr, a, edge_x, ankle_y, sign):
    for dy, outer in AWING.items():
        y = ankle_y - dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                 # never overpaint the body
                continue
            put(fr, y, x, accent_tone(dy, off, outer))


def side_anchor(a, sign, band=4):
    """Return (edge_x, anchor_y) at the TOP band of the silhouette for the given
    side, so accents root at the hip/ankle corner and share an edge with body."""
    ys, xs = np.where(a)
    top_y = int(ys.min())
    band_mask = a[top_y:top_y + band, :]
    bxs = np.where(band_mask.any(axis=0))[0]
    edge_x = int(bxs.min()) if sign < 0 else int(bxs.max())
    col = np.flatnonzero(a[top_y:top_y + band, edge_x])
    anchor_y = top_y + int(col.min()) if col.size else top_y
    return edge_x, anchor_y


def _build(base, draw_fn):
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
            draw_fn(fr, a, edge_x, anchor_y, sign)
    return out


def main():
    os.makedirs('_ranger_legs_legendary_preview', exist_ok=True)
    jobs = [
        ('pants_ranger4', 'pants_ranger_legendary1', draw_tasset),
        ('boots_ranger4', 'boots_ranger_legendary1', draw_ankle_wing),
    ]
    for src_stem, dst_stem, draw_fn in jobs:
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (src_stem, suffix))
            arr = _build(base, draw_fn)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '_ranger_legs_legendary_preview/%s%s.png' % (dst_stem, suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %s  (opaque_px=%d)' % (dst, int((arr[..., 3] > 0).sum())))


if __name__ == '__main__':
    main()
