#!/usr/bin/env python3
"""
Build armor_chest_2 frame 0 (80×64 PNG):
  - Start from leather_armor_1 frame 0 (all 135 pixels)
  - Overlay iron plate pixels (pauldrons + chest plate), clipped to shirt mask
  - Report every pixel assigned so the caller can verify
"""
from PIL import Image
import numpy as np

PROJECT = "/Users/matthauth/Projects/TaskQuest"
CHAR    = f"{PROJECT}/sprites/preview_assets/char"
OUT     = "/Users/matthauth/Desktop/armor_chest_2_frame0.png"

# ── Iron palette ──────────────────────────────────────────────────────────
def r(h):
    h = h.lstrip('#')
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), 255)

E = r('#E0E0E0')  # bright highlight (top rim)
B = r('#B8B8B8')  # highlight face
M = r('#8C8C8C')  # mid tone
S = r('#606060')  # shadow
D = r('#3A3A3A')  # dark shadow
O = r('#1A1A1A')  # outline/deepest

# ── Load exact shirt mask ─────────────────────────────────────────────────
shirt_img = Image.open(f"{CHAR}/shirt.png").convert('RGBA')
s0 = np.array(shirt_img.crop((0,0,80,64)))
shirt_mask = {(x,y) for y in range(64) for x in range(80) if s0[y,x,3]>0}
assert len(shirt_mask) == 135, f"Expected 135, got {len(shirt_mask)}"

# ── Load leather_armor_1 frame 0 as base ─────────────────────────────────
la_img = Image.open(f"{CHAR}/leather_armor_1.png").convert('RGBA')
la0 = np.array(la_img.crop((0,0,80,64)))
armor = {}
for (x,y) in shirt_mask:
    c = tuple(la0[y,x])
    armor[(x,y)] = c

# ── Plate overlay (will be clipped to mask) ───────────────────────────────
plate = {}

def pp(x, y, c):
    if (x,y) in shirt_mask:
        plate[(x,y)] = c
    # silently skip pixels outside mask

# Left pauldron (shoulder plate, top-left)
pp(35,34,E); pp(36,34,B)
pp(34,35,O); pp(35,35,E); pp(36,35,B)
pp(34,36,S); pp(35,36,M); pp(36,36,S)
pp(34,37,O); pp(35,37,D); pp(36,37,O)

# Right pauldron (mirror)
pp(44,34,B); pp(45,34,E)
pp(43,35,B); pp(44,35,M); pp(45,35,O)
pp(43,36,S); pp(44,36,M); pp(45,36,S)
pp(44,37,D); pp(45,37,O); pp(46,37,O)

# Chest plate — top rim y=37 (x=37-43)
for x in range(37,44):
    pp(x,37,E)

# Chest plate — y=38: outline+highlight (x=43 in mask here)
pp(36,38,O)
for x in range(37,44): pp(x,38,B)
pp(44,38,O)

# Chest plate — y=39: x=43 NOT in mask, right border naturally ends at x=42
pp(36,39,O)
for x in range(37,43): pp(x,39,M)   # x=37-42; x=43 skipped by mask check

# Chest plate — y=40: same gap
pp(36,40,O)
for x in range(37,43): pp(x,40,M)

# Chest plate — y=41: mask only has x=35-41 (x=42+ absent)
pp(36,41,O)
for x in range(37,42): pp(x,41,S)

# Chest plate — y=42: shadow
pp(36,42,O)
for x in range(37,42): pp(x,42,D)

# Chest plate — y=43: bottom edge, full dark
pp(36,43,O)
for x in range(37,42): pp(x,43,O)

# ── Apply plate over leather ──────────────────────────────────────────────
armor.update(plate)

# ── Build 80×64 canvas and save ──────────────────────────────────────────
out_arr = np.zeros((64,80,4), dtype=np.uint8)
for (x,y), c in armor.items():
    out_arr[y,x] = c

out = Image.fromarray(out_arr)
out.save(OUT)
print(f"Saved → {OUT}")

# ── Report ────────────────────────────────────────────────────────────────
color_names = {E:'E0E0E0(bright rim)', B:'B8B8B8(highlight)', M:'8C8C8C(mid)',
               S:'606060(shadow)', D:'3A3A3A(dark)', O:'1A1A1A(outline)'}

print(f"\nTotal armor pixels: {len(armor)}  (leather base + {len(plate)} plate overrides)")
print("\nPlate pixels painted (within shirt mask):")

by_row = {}
for (x,y), c in sorted(plate.items()):
    by_row.setdefault(y, []).append((x, c))

for y in sorted(by_row):
    row = by_row[y]
    # Group consecutive x runs by color
    parts = []
    for x, c in sorted(row):
        cn = color_names.get(c, f"#{c[0]:02X}{c[1]:02X}{c[2]:02X}")
        parts.append(f"  x={x}→#{c[0]:02X}{c[1]:02X}{c[2]:02X}")
    print(f"y={y}: {len(row)} pixels")
    for x, c in sorted(row):
        cn = color_names.get(c, "?")
        print(f"       ({x},{y}) → {cn}")
