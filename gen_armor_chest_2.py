#!/usr/bin/env python3
"""
Propagate studded-leather armor across all active shirt frames.
Stud pixels removed; uses centroid-offset tracking against shirt.png.
"""
import numpy as np
from PIL import Image

PROJECT = "/Users/matthauth/Projects/TaskQuest"
SHIRT_PATH = f"{PROJECT}/sprites/preview_assets/char/shirt.png"
OUT_PATH   = f"{PROJECT}/sprites/preview_assets/char/armor_chest_2.png"
DESK_PATH  = "/Users/matthauth/Desktop/armor_chest_2_preview.png"

FRAME_W, FRAME_H = 80, 64
COLS, ROWS = 10, 7

# ── Helpers ──────────────────────────────────────────────────────────────
def rgba(h):
    h = h.lstrip('#')
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), 255)

DARK  = rgba('#1A0D05')
MID   = rgba('#5F3219')
LITE  = rgba('#8C5A2A')
BASE  = rgba('#C07834')
STRAP = rgba('#C8A870')

# ── Frame-0 armor pixel map (no studs) ───────────────────────────────────
# Studs that were removed: (35,35), (44,35), (37,39), (44,39)
armor = {}  # (local_x, local_y) -> rgba

def p(x, y, c): armor[(x, y)] = c

# y=33
p(36,33,DARK); p(41,33,MID); p(42,33,LITE); p(43,33,LITE); p(44,33,DARK)

# y=34
p(35,34,DARK); p(36,34,MID); p(40,34,MID); p(41,34,LITE)
p(42,34,BASE); p(43,34,LITE); p(44,34,MID); p(45,34,DARK)

# y=35  (35,35) and (44,35) are transparent — omitted
p(34,35,DARK); p(36,35,MID); p(39,35,MID)
p(40,35,LITE); p(41,35,BASE); p(42,35,BASE); p(43,35,LITE); p(45,35,DARK)

# y=36  x=34-45
p(34,36,DARK); p(35,36,MID);  p(36,36,LITE); p(37,36,BASE)
p(38,36,STRAP); p(39,36,BASE); p(40,36,BASE); p(41,36,BASE)
p(42,36,BASE); p(43,36,STRAP); p(44,36,MID); p(45,36,DARK)

# y=37  x=34-46
p(34,37,DARK); p(35,37,MID);  p(36,37,LITE); p(37,37,BASE)
p(38,37,STRAP); p(39,37,BASE); p(40,37,BASE); p(41,37,BASE)
p(42,37,BASE); p(43,37,STRAP); p(44,37,LITE); p(45,37,MID); p(46,37,DARK)

# y=38  x=35-46
p(35,38,DARK); p(36,38,MID); p(37,38,LITE)
p(38,38,STRAP); p(39,38,BASE); p(40,38,BASE); p(41,38,BASE)
p(42,38,BASE); p(43,38,STRAP); p(44,38,LITE); p(45,38,MID); p(46,38,DARK)

# y=39  (37,39) and (44,39) transparent — omitted
p(35,39,DARK); p(36,39,MID)
p(38,39,STRAP); p(39,39,BASE); p(40,39,BASE); p(41,39,BASE)
p(42,39,BASE); p(43,39,STRAP); p(45,39,MID); p(46,39,DARK)

# y=40  x=35-46
p(35,40,DARK); p(36,40,MID); p(37,40,LITE)
p(38,40,STRAP); p(39,40,BASE); p(40,40,BASE); p(41,40,BASE)
p(42,40,BASE); p(43,40,STRAP); p(44,40,LITE); p(45,40,MID); p(46,40,DARK)

# y=41  x=35-46
p(35,41,DARK); p(36,41,MID); p(37,41,LITE)
p(38,41,STRAP); p(39,41,BASE); p(40,41,BASE); p(41,41,BASE)
p(42,41,BASE); p(43,41,STRAP); p(44,41,LITE); p(45,41,MID); p(46,41,DARK)

# y=42  x=36-46
p(36,42,DARK); p(37,42,MID); p(38,42,LITE)
p(39,42,BASE); p(40,42,BASE); p(41,42,BASE); p(42,42,BASE); p(43,42,BASE)
p(44,42,LITE); p(45,42,MID); p(46,42,DARK)

# y=43  x=36-46
p(36,43,DARK); p(37,43,MID); p(38,43,LITE)
p(39,43,BASE); p(40,43,BASE); p(41,43,BASE); p(42,43,BASE); p(43,43,BASE)
p(44,43,LITE); p(45,43,MID); p(46,43,DARK)

# y=44  x=36-46
p(36,44,DARK); p(37,44,MID); p(38,44,LITE)
p(39,44,BASE); p(40,44,BASE); p(41,44,BASE); p(42,44,BASE); p(43,44,BASE)
p(44,44,LITE); p(45,44,MID); p(46,44,DARK)

# y=45  x=36-41
p(36,45,DARK); p(37,45,MID); p(38,45,LITE)
p(39,45,BASE); p(40,45,LITE); p(41,45,DARK)

# y=46  x=35-41
p(35,46,DARK); p(36,46,MID); p(37,46,LITE)
p(38,46,BASE); p(39,46,LITE); p(40,46,MID); p(41,46,DARK)

# y=47  x=35-41
p(35,47,DARK); p(36,47,MID); p(37,47,LITE)
p(38,47,BASE); p(39,47,LITE); p(40,47,MID); p(41,47,DARK)

print(f"Armor pixel count: {len(armor)}")

# ── Frame-0 centroid (exact 135 shirt pixels) ────────────────────────────
f0 = []
sparse_rows = {
    33: [(36,33),(41,33),(42,33),(43,33),(44,33)],
    34: [(35,34),(36,34),(40,34),(41,34),(42,34),(43,34),(44,34),(45,34)],
    35: [(34,35),(35,35),(36,35),(39,35),(40,35),(41,35),(42,35),(43,35),(44,35),(45,35)],
}
full_rows = {
    36: range(34,46), 37: range(34,47), 38: range(35,47),
    39: range(35,47), 40: range(35,47), 41: range(35,47),
    42: range(36,47), 43: range(36,47), 44: range(36,47),
    45: range(36,42), 46: range(35,42), 47: range(35,42),
}
for y, coords in sparse_rows.items():
    f0.extend(coords)
for y, xs in full_rows.items():
    f0.extend((x, y) for x in xs)

cx0 = sum(pt[0] for pt in f0) / len(f0)
cy0 = sum(pt[1] for pt in f0) / len(f0)
print(f"Frame-0 shirt centroid: ({cx0:.3f}, {cy0:.3f})  pixel count: {len(f0)}")

# ── Load shirt sheet ──────────────────────────────────────────────────────
shirt_img = Image.open(SHIRT_PATH).convert('RGBA')
assert shirt_img.size == (800, 448), f"Unexpected size: {shirt_img.size}"
shirt_arr = np.array(shirt_img)

# ── Build output canvas ───────────────────────────────────────────────────
out_arr = np.zeros((448, 800, 4), dtype=np.uint8)

active = 0
skipped = 0

for fi in range(COLS * ROWS):
    col = fi % COLS
    row = fi // COLS
    gx  = col * FRAME_W
    gy  = row * FRAME_H

    frame_slice = shirt_arr[gy:gy+FRAME_H, gx:gx+FRAME_W]
    opaque = np.argwhere(frame_slice[:, :, 3] > 0)   # (row=y, col=x)

    if len(opaque) == 0:
        skipped += 1
        continue

    active += 1
    cx_n = float(np.mean(opaque[:, 1]))  # x
    cy_n = float(np.mean(opaque[:, 0]))  # y
    dx = round(cx_n - cx0)
    dy = round(cy_n - cy0)

    for (lx, ly), color in armor.items():
        nx = lx + dx
        ny = ly + dy
        gnx = nx + gx
        gny = ny + gy
        if 0 <= gnx < 800 and 0 <= gny < 448:
            out_arr[gny, gnx] = color

print(f"Active frames: {active}  |  Skipped (empty): {skipped}")

# ── Save ──────────────────────────────────────────────────────────────────
out = Image.fromarray(out_arr, 'RGBA')
out.save(OUT_PATH)
out.save(DESK_PATH)
print(f"Saved → {OUT_PATH}")
print(f"Saved → {DESK_PATH}")
