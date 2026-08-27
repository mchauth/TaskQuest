"""
add_projectiles.py
Adds animated projectiles to bow and staff slash frames 51-53.
Arrow/orb moves right across the 3 frames toward the enemy.
Erases any existing projectile pixels first. Does NOT touch frame 0.
"""
import numpy as np
from PIL import Image
import os

FW, FH, COLS = 80, 64, 10

# Arrow colors
SHAFT = np.array([120, 80, 35, 255], dtype=np.uint8)
TIP   = np.array([180, 180, 190, 255], dtype=np.uint8)
FEATH = np.array([200, 60, 60, 255], dtype=np.uint8)
CLEAR = np.array([0, 0, 0, 0], dtype=np.uint8)

STAFF_TRAILS = {
    't1': (np.array([180,120,255,255],dtype=np.uint8), np.array([220,180,255,220],dtype=np.uint8)),
    't2': (np.array([100,160,255,255],dtype=np.uint8), np.array([160,200,255,220],dtype=np.uint8)),
    't3': (np.array([80,220,120,255],dtype=np.uint8),  np.array([160,255,180,220],dtype=np.uint8)),
    't4': (np.array([255,200,60,255],dtype=np.uint8),  np.array([255,230,120,220],dtype=np.uint8)),
    't5': (np.array([255,80,80,255],dtype=np.uint8),   np.array([255,160,120,220],dtype=np.uint8)),
    't6': (np.array([200,160,255,255],dtype=np.uint8), np.array([160,200,255,220],dtype=np.uint8)),
}

def erase_colors(frame, *colors):
    for color in colors:
        mask = np.all(frame == color, axis=-1)
        frame[mask] = CLEAR

def draw_arrow_right(frame, ax_start, arrow_y):
    """Draw 10px right-pointing arrow at given position."""
    ax_start = max(0, min(FW-14, ax_start))
    arrow_y  = max(2, min(FH-3, arrow_y))
    ax_end   = min(FW-2, ax_start + 10)
    for ax in range(ax_start, ax_end):
        frame[arrow_y, ax] = SHAFT
    # Tip at right
    for ay in [-1, 0, 1]:
        ry = arrow_y + ay
        if 0 <= ry < FH and ax_end + 1 < FW:
            frame[ry, ax_end + 1] = TIP
    # Feathers at left
    for ay in [-1, 1]:
        ry = arrow_y + ay
        if 0 <= ry < FH:
            frame[ry, ax_start] = FEATH

def draw_orb(frame, ox, oy, core, glow, size=2):
    """Draw glowing energy orb at (ox, oy) with given size."""
    ox = max(size+1, min(FW-size-2, ox))
    oy = max(size+1, min(FH-size-2, oy))
    for dy in range(-size-1, size+2):
        for dx in range(-size-1, size+2):
            ry, rx = oy+dy, ox+dx
            if 0 <= ry < FH and 0 <= rx < FW:
                dist = abs(dy) + abs(dx)
                if dist <= size - 1:
                    frame[ry, rx] = core
                elif dist <= size + 1:
                    frame[ry, rx] = glow

OUT_DIR = '/tmp/tq_proj/sprites/preview_assets/char/'

# ── Bow: animated arrow ───────────────────────────────────────────────────────
for tier in ['t1','t2','t3','t4','t5','t6']:
    for g in ['m','f']:
        fname = f'{OUT_DIR}bow_ranger_{tier}_{g}.png'
        if not os.path.exists(fname): continue
        img = Image.open(fname).convert('RGBA')
        arr = np.array(img)

        for i, fi in enumerate([51, 52, 53]):
            r2, c2 = fi // COLS, fi % COLS
            gx, gy = c2 * FW, r2 * FH
            frame = arr[gy:gy+FH, gx:gx+FW]

            # Erase existing arrow pixels
            erase_colors(frame, SHAFT, TIP, FEATH)

            # Find bow centroid
            op = np.argwhere(frame[..., 3] > 0)
            if len(op) == 0: continue
            cx = float(np.mean(op[:, 1]))
            cy = float(np.mean(op[:, 0]))

            # Arrow position: starts just right of bow, moves across frames
            # i=0 (fr51): near bow  i=1 (fr52): middle  i=2 (fr53): near enemy
            ax_start = round(cx) + 4 + i * 18
            arrow_y  = round(cy)  # same row as bow centroid
            draw_arrow_right(frame, ax_start, arrow_y)
            arr[gy:gy+FH, gx:gx+FW] = frame

        Image.fromarray(arr).save(fname)
        print(f"  Arrow added: {os.path.basename(fname)}")

# ── Staff: animated orb ───────────────────────────────────────────────────────
for tier in ['t1','t2','t3','t4','t5','t6']:
    core, glow = STAFF_TRAILS[tier]
    for g in ['m','f']:
        fname = f'{OUT_DIR}staff_mage_{tier}_{g}.png'
        if not os.path.exists(fname): continue
        img = Image.open(fname).convert('RGBA')
        arr = np.array(img)

        # Find staff position in fr51 to anchor orb start
        fi51_r, fi51_c = 51 // COLS, 51 % COLS
        gx51, gy51 = fi51_c * FW, fi51_r * FH
        f51 = arr[gy51:gy51+FH, gx51:gx51+FW]
        op51 = np.argwhere(f51[..., 3] > 0)
        if len(op51) == 0:
            print(f"  SKIP (empty fr51): {os.path.basename(fname)}"); continue
        # Staff tip = topmost pixels
        top_y = int(op51[:, 0].min())
        top_xs = op51[op51[:,0] <= top_y + 3][:, 1]
        tip_x = int(np.mean(top_xs))
        tip_y = top_y + 2  # just below the very tip

        for i, fi in enumerate([51, 52, 53]):
            r2, c2 = fi // COLS, fi % COLS
            gx, gy = c2 * FW, r2 * FH
            frame = arr[gy:gy+FH, gx:gx+FW]

            # Orb moves right from staff tip across the 3 frames
            orb_x = tip_x + i * 20
            orb_y = tip_y - i * 3   # slight upward arc toward enemy
            orb_size = 2 + i        # grows as it approaches enemy (1→2→3)

            draw_orb(frame, orb_x, orb_y, core, glow, size=orb_size)
            arr[gy:gy+FH, gx:gx+FW] = frame

        Image.fromarray(arr).save(fname)
        print(f"  Orb added: {os.path.basename(fname)}")

print("Done.")
