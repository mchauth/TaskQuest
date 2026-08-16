#!/usr/bin/env python3
"""
Propagate armor_chest_2 frame 0 across all active frames.

Method:
  - Output starts as full copy of leather_armor_1.png (800x448)
  - Plate overlay pixels = positions in armor_chest_2_frame0.png that differ
    from leather_armor_1.png frame 0
  - For each active frame: compute shirt centroid offset vs frame 0,
    shift each plate pixel, paint ONLY if shifted pos is opaque in that
    frame's shirt mask
"""
import numpy as np
from PIL import Image

PROJECT = "/Users/matthauth/Projects/TaskQuest"
CHAR    = f"{PROJECT}/sprites/preview_assets/char"
OUT     = f"{CHAR}/armor_chest_2.png"
DESK    = "/Users/matthauth/Desktop/armor_chest_2_preview.png"

FRAME_W, FRAME_H = 80, 64
COLS, ROWS = 10, 7

# ── Load sources ──────────────────────────────────────────────────────────
armor_f0   = np.array(Image.open("/Users/matthauth/Desktop/armor_chest_2_frame0.png").convert('RGBA'))
leather    = np.array(Image.open(f"{CHAR}/leather_armor_1.png").convert('RGBA'))
shirt_full = np.array(Image.open(f"{CHAR}/shirt.png").convert('RGBA'))

assert leather.shape    == (448, 800, 4)
assert shirt_full.shape == (448, 800, 4)

# ── Compute plate overlay: pixels that differ from leather_armor_1 frame 0 ──
leather_f0 = leather[:FRAME_H, :FRAME_W]
plate_overlay = {}   # (local_x, local_y) -> rgba tuple
for y in range(FRAME_H):
    for x in range(FRAME_W):
        if armor_f0[y, x, 3] > 0:
            a = tuple(armor_f0[y, x])
            l = tuple(leather_f0[y, x])
            if a != l:
                plate_overlay[(x, y)] = a

print(f"Plate overlay pixels: {len(plate_overlay)}")

# ── Frame 0 shirt centroid ────────────────────────────────────────────────
f0_shirt = shirt_full[:FRAME_H, :FRAME_W]
f0_opaque = np.argwhere(f0_shirt[:, :, 3] > 0)   # (row=y, col=x)
cx0 = float(np.mean(f0_opaque[:, 1]))
cy0 = float(np.mean(f0_opaque[:, 0]))
print(f"Frame 0 centroid: ({cx0:.3f}, {cy0:.3f})")

# ── Start output from leather_armor_1 copy ───────────────────────────────
out = leather.copy()

active = 0
skipped = 0
total_painted = 0
mask_rejected = 0

for fi in range(COLS * ROWS):
    col = fi % COLS
    row = fi // COLS
    gx  = col * FRAME_W
    gy  = row * FRAME_H

    frame_shirt = shirt_full[gy:gy+FRAME_H, gx:gx+FRAME_W]
    opaque      = np.argwhere(frame_shirt[:, :, 3] > 0)

    if len(opaque) == 0:
        skipped += 1
        continue

    active += 1

    # Centroid offset (rounded to nearest pixel)
    dx = round(float(np.mean(opaque[:, 1])) - cx0)
    dy = round(float(np.mean(opaque[:, 0])) - cy0)

    # Build shirt mask set for this frame (local coords)
    shirt_mask = set(zip(opaque[:, 1].tolist(), opaque[:, 0].tolist()))  # (x,y)

    # Paint plate overlay, shifted, masked
    for (lx, ly), color in plate_overlay.items():
        nx = lx + dx
        ny = ly + dy
        if (nx, ny) in shirt_mask:          # only paint within shirt mask
            gnx = nx + gx
            gny = ny + gy
            if 0 <= gnx < 800 and 0 <= gny < 448:
                out[gny, gnx] = color
                total_painted += 1
        else:
            mask_rejected += 1

print(f"Active frames: {active}  |  Skipped (empty): {skipped}")
print(f"Total plate pixels painted: {total_painted}")
print(f"Mask-rejected (shifted outside shirt): {mask_rejected}")

# ── Save ──────────────────────────────────────────────────────────────────
result = Image.fromarray(out)
result.save(OUT)
result.save(DESK)
print(f"Saved → {OUT}")
print(f"Saved → {DESK}")
