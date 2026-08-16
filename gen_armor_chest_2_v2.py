#!/usr/bin/env python3
"""
armor_chest_2: leather_armor_1 base + propagated iron plate overlay.
Plate pixels are defined in frame-0 local coords and offset-tracked via
shirt.png centroids (same technique as hair/leather propagation).
"""
import numpy as np
from PIL import Image

PROJECT    = "/Users/matthauth/Projects/TaskQuest"
LEATHER    = f"{PROJECT}/sprites/preview_assets/char/leather_armor_1.png"
SHIRT      = f"{PROJECT}/sprites/preview_assets/char/shirt.png"
OUT_PATH   = f"{PROJECT}/sprites/preview_assets/char/armor_chest_2.png"
DESK_PATH  = "/Users/matthauth/Desktop/armor_chest_2_preview.png"

FRAME_W, FRAME_H = 80, 64
COLS, ROWS = 10, 7

# ── Colour helpers ────────────────────────────────────────────────────────
def rgba(h):
    h = h.lstrip('#')
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), 255)

IRON_HI     = rgba('#9A9A9A')
IRON_MID    = rgba('#8C8C8C')
IRON_BODY   = rgba('#7A7A7A')
IRON_SHADOW = rgba('#707070')
IRON_DARK   = rgba('#5A5A5A')
OUTLINE     = rgba('#2A2A2A')

# ── Plate overlay pixels (frame-0 local coords) ───────────────────────────
plate = {}   # (local_x, local_y) -> rgba

def px(x, y, c): plate[(x, y)] = c

# Left pauldron
px(34,35, OUTLINE)   # left outline overrides mid
px(35,35, IRON_MID)
px(36,35, IRON_MID)
px(34,36, IRON_SHADOW)
px(35,36, IRON_SHADOW)

# Right pauldron
px(44,35, IRON_MID)
px(45,35, OUTLINE)   # right outline overrides mid
px(45,36, IRON_SHADOW)
px(46,36, IRON_SHADOW)

# Chest plate — top highlight row
for x in range(37, 43):
    px(x, 37, IRON_HI)

# Chest plate — body rows
for y in (38, 39):
    for x in range(37, 43):
        px(x, y, IRON_BODY)

# Chest plate — bottom shadow row
for x in range(37, 43):
    px(x, 40, IRON_DARK)

# Chest plate — left and right outlines
for y in range(37, 41):
    px(36, y, OUTLINE)
    px(43, y, OUTLINE)

print(f"Plate pixel count: {len(plate)}")

# ── Frame-0 shirt centroid (exact 149 tunic pixels) ───────────────────────
f0 = []
sparse = {
    33: [(36,33),(41,33),(42,33),(43,33),(44,33)],
    34: [(35,34),(36,34),(40,34),(41,34),(42,34),(43,34),(44,34),(45,34)],
    35: [(34,35),(35,35),(36,35),(39,35),(40,35),(41,35),(42,35),(43,35),(44,35),(45,35)],
}
full = {
    36: range(34,46), 37: range(34,47), 38: range(35,47),
    39: range(35,47), 40: range(35,47), 41: range(35,47),
    42: range(36,47), 43: range(36,47), 44: range(36,47),
    45: range(36,42), 46: range(35,42), 47: range(35,42),
}
for coords in sparse.values():
    f0.extend(coords)
for y, xs in full.items():
    f0.extend((x, y) for x in xs)

cx0 = sum(pt[0] for pt in f0) / len(f0)
cy0 = sum(pt[1] for pt in f0) / len(f0)
print(f"Frame-0 centroid: ({cx0:.3f}, {cy0:.3f})  [{len(f0)} pixels]")

# ── Load sources ──────────────────────────────────────────────────────────
leather_arr = np.array(Image.open(LEATHER).convert('RGBA'))
shirt_arr   = np.array(Image.open(SHIRT).convert('RGBA'))

assert leather_arr.shape == (448, 800, 4), f"Bad leather size: {leather_arr.shape}"
assert shirt_arr.shape   == (448, 800, 4), f"Bad shirt size:   {shirt_arr.shape}"

# ── Start from a full copy of leather_armor_1 ────────────────────────────
out_arr = leather_arr.copy()

# ── Overlay plate pixels per active frame ────────────────────────────────
active = 0
skipped = 0

for fi in range(COLS * ROWS):
    col = fi % COLS
    row = fi // COLS
    gx  = col * FRAME_W
    gy  = row * FRAME_H

    shirt_frame = shirt_arr[gy:gy+FRAME_H, gx:gx+FRAME_W]
    opaque = np.argwhere(shirt_frame[:, :, 3] > 0)   # (y, x)

    if len(opaque) == 0:
        skipped += 1
        continue

    active += 1
    dx = round(float(np.mean(opaque[:, 1])) - cx0)
    dy = round(float(np.mean(opaque[:, 0])) - cy0)

    for (lx, ly), color in plate.items():
        nx  = lx + dx
        ny  = ly + dy
        gnx = nx + gx
        gny = ny + gy
        if 0 <= gnx < 800 and 0 <= gny < 448:
            out_arr[gny, gnx] = color

print(f"Active frames: {active}  |  Skipped (empty): {skipped}")

# ── Save ──────────────────────────────────────────────────────────────────
out = Image.fromarray(out_arr)
out.save(OUT_PATH)
out.save(DESK_PATH)
print(f"Saved → {OUT_PATH}")
print(f"Saved → {DESK_PATH}")
