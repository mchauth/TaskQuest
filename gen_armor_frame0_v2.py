#!/usr/bin/env python3
"""
armor_chest_2 frame 0 — perspective-corrected plate repaint.
Character faces 3/4 left: character-right shoulder (our LEFT, x=34-37) recedes;
character-left shoulder (our RIGHT, x=43-46) faces viewer.
Chest plate shades dark-left → bright-right.
"""
from PIL import Image
import numpy as np

PROJECT = "/Users/matthauth/Projects/TaskQuest"
CHAR    = f"{PROJECT}/sprites/preview_assets/char"
OUT     = "/Users/matthauth/Desktop/armor_chest_2_frame0.png"
OUT_C   = "/Users/matthauth/Desktop/armor_chest_2_frame0_composite.png"

# ── Exact shirt mask (verified from PNG) ──────────────────────────────────
SHIRT_MASK = {
    **{(x,33): 1 for x in [36,41,42,43,44]},
    **{(x,34): 1 for x in [35,36,40,41,42,43,44,45]},
    **{(x,35): 1 for x in [34,35,36,39,40,41,42,43,44,45]},
    **{(x,36): 1 for x in range(34,46)},
    **{(x,37): 1 for x in range(34,47)},
    **{(x,38): 1 for x in range(35,47)},
    **{(x,39): 1 for x in [35,36,37,38,39,40,41,42,44,45,46]},
    **{(x,40): 1 for x in [35,36,37,38,39,40,41,42,44,45,46]},
    **{(x,41): 1 for x in [35,36,37,38,39,40,41,45,46]},
    **{(x,42): 1 for x in [36,37,38,39,40,41,45,46]},
    **{(x,43): 1 for x in [36,37,38,39,40,41,45,46]},
    **{(x,44): 1 for x in [36,37,38,39,40,41,45,46]},
    **{(x,45): 1 for x in range(36,42)},
    **{(x,46): 1 for x in range(35,42)},
    **{(x,47): 1 for x in range(35,42)},
}
assert len(SHIRT_MASK) == 135

# ── Iron palette ──────────────────────────────────────────────────────────
def c(h):
    h = h.lstrip('#')
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), 255)

E = c('#E0E0E0')  # bright highlight
B = c('#B8B8B8')  # highlight face
M = c('#8C8C8C')  # mid tone
S = c('#606060')  # shadow
D = c('#3A3A3A')  # dark shadow
O = c('#1A1A1A')  # outline / deepest

# ── Load leather base ─────────────────────────────────────────────────────
la0 = np.array(Image.open(f"{CHAR}/leather_armor_1.png").convert('RGBA').crop((0,0,80,64)))
armor = {(x,y): tuple(la0[y,x]) for (x,y) in SHIRT_MASK}

# ── Apply plate pixel (guard: must be in shirt mask) ─────────────────────
plate = {}

def pp(x, y, col):
    if (x,y) in SHIRT_MASK:
        plate[(x,y)] = col

# ────────────────────────────────────────────────────────────────────────
# RIGHT PAULDRON  (character's right = our LEFT, x≈34-36, recedes away)
# Small, mostly dark — barely visible curving away from viewer
# ────────────────────────────────────────────────────────────────────────
pp(35,34, D)      # tiny top hint
pp(34,35, O)      # hard outline left edge
pp(35,35, D)      # dark face
pp(36,35, S)      # slight mid, transitions toward chest
pp(34,36, O)      # outline continues
pp(35,36, D)      # shadow
pp(36,36, S)      # soft transition
# y=37 is owned by chest plate rim — no separate pauldron pixel there

# ────────────────────────────────────────────────────────────────────────
# LEFT PAULDRON  (character's left = our RIGHT, x=43-46, faces viewer)
# Prominent highlight — most visible shoulder plate
# ────────────────────────────────────────────────────────────────────────
pp(43,34, D)      # inner shadow/edge (left side of pauldron)
pp(44,34, E)      # bright top rim
pp(45,34, E)      # bright top rim
pp(43,35, M)      # mid face
pp(44,35, B)      # highlight face
pp(45,35, E)      # brightest face (top of curve)
pp(43,36, S)      # underside shadow
pp(44,36, M)      # mid
pp(45,36, B)      # face, still catching light
# y=37: pauldron tail — picks up from chest rim gradient
pp(45,37, S)      # pauldron underside
pp(46,37, O)      # outline/edge

# ────────────────────────────────────────────────────────────────────────
# CHEST PLATE — TOP RIM  y=37  (gradient left-dark → right-bright)
# ────────────────────────────────────────────────────────────────────────
pp(34,37, O)   # hard outline, far receding edge
pp(35,37, D)   # dark band
pp(36,37, S)   # gradient start
pp(37,37, S)   # mid-shadow zone
pp(38,37, B)   # turning toward viewer
pp(39,37, B)
pp(40,37, B)
pp(41,37, E)   # viewer-facing bright rim
pp(42,37, E)
pp(43,37, E)
pp(44,37, E)   # brightest corner (closest to viewer + top)
# x=45,46 handled by pauldron above

# ────────────────────────────────────────────────────────────────────────
# CHEST PLATE — BODY  y=38-41
# Columns: x34-36=dark band | x37-39=mid shadow | x40-42=face | x43-44=highlight
# Mask gaps: x34 absent y≥38; x43 absent y≥39; x42,43,44 absent y≥41
# ────────────────────────────────────────────────────────────────────────

for y in range(38, 42):
    # Dark band (x=35-36; x=34 only available at y=37)
    pp(35,y, D)
    pp(36,y, D)
    # Mid shadow
    pp(37,y, S)
    pp(38,y, S)
    pp(39,y, S)
    # Face
    pp(40,y, M)
    pp(41,y, M)
    pp(42,y, B)    # rightmost face column (absent at y=41 → guard handles it)

# Highlight corner: x=43 available y=38 only (absent y≥39); x=44 available y=38-40
pp(43,38, E)
pp(44,38, E)
pp(44,39, E)   # x=43 gone at y=39, x=44 still visible — isolated but spec says so

# ────────────────────────────────────────────────────────────────────────
# CHEST PLATE — BOTTOM  y=42-43  (full dark, plate base in shadow)
# ────────────────────────────────────────────────────────────────────────
# y=42: available x=36-41 (central block)
pp(36,42, O)
pp(37,42, D)
pp(38,42, D)
pp(39,42, D)
pp(40,42, D)
pp(41,42, O)

# y=43: full black bottom edge
for x in range(36, 42):
    pp(x,43, O)

# ── Merge plate onto leather base ────────────────────────────────────────
armor.update(plate)

# ── Build and save PNG ───────────────────────────────────────────────────
out_arr = np.zeros((64,80,4), dtype=np.uint8)
for (x,y), col in armor.items():
    out_arr[y,x] = col

img = Image.fromarray(out_arr)
img.save(OUT)
print(f"Saved armor-only → {OUT}")

# ── Print report ─────────────────────────────────────────────────────────
color_labels = {
    E:'E0E0E0(bright)', B:'B8B8B8(hi-face)', M:'8C8C8C(mid)',
    S:'606060(shadow)', D:'3A3A3A(dark)', O:'1A1A1A(outline)',
}
print(f"\nPlate pixels applied: {len(plate)}")
print("\nPer-row breakdown:")
by_y = {}
for (x,y), col in sorted(plate.items()):
    by_y.setdefault(y,[]).append((x,col))
for y in sorted(by_y):
    row = sorted(by_y[y])
    parts = [f"x={x}→{color_labels.get(col, '#{:02X}{:02X}{:02X}'.format(col[0],col[1],col[2]))}" for x,col in row]
    print(f"  y={y}: {parts}")
