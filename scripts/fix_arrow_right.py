"""Fix bow arrow to shoot RIGHT in the sprite sheet."""
import numpy as np
from PIL import Image
import os

FW, FH, COLS = 80, 64, 10
SRC_DIR = '/sessions/optimistic-confident-einstein/mnt/TaskQuest/sprites/preview_assets/char/'

SHAFT = (120, 80,  35, 255)
TIP   = (180, 180, 190, 255)
FEATH = (200, 60,  60, 255)
CLEAR = (0, 0, 0, 0)

def fix_arrow(fname):
    img = Image.open(fname).convert('RGBA')
    arr = np.array(img)

    for fi in [51, 52, 53]:
        r2, c2 = fi // COLS, fi % COLS
        gx, gy = c2 * FW, r2 * FH
        frame = arr[gy:gy+FH, gx:gx+FW]

        # Erase any existing arrow pixels
        for color in [SHAFT, TIP, FEATH]:
            mask = np.all(frame == np.array(color, dtype=np.uint8), axis=-1)
            frame[mask] = CLEAR

        # Find bow centroid
        op = np.argwhere(frame[..., 3] > 0)
        if len(op) == 0: continue
        cx = float(np.mean(op[:, 1]))
        cy = float(np.mean(op[:, 0]))

        # Arrow shoots RIGHT, offset slightly below centroid to stay clear of bow
        arrow_y = max(4, min(FH-5, round(cy) + 4))
        ax_l = min(FW-14, round(cx) + 2)   # feather end (left, near bow)
        ax_r = min(FW-2,  ax_l + 12)        # tip end (right, toward enemy)

        for ax in range(ax_l, ax_r):
            frame[arrow_y, ax] = SHAFT
        # Tip at right
        for ay in [-1, 0, 1]:
            ry = arrow_y + ay
            if 0 <= ry < FH and ax_r + 1 < FW:
                frame[ry, ax_r + 1] = TIP
        # Feathers at left
        for ay in [-1, 1]:
            ry = arrow_y + ay
            if 0 <= ry < FH:
                frame[ry, ax_l] = FEATH

        arr[gy:gy+FH, gx:gx+FW] = frame

    Image.fromarray(arr).save(fname)
    print(f"  Fixed: {os.path.basename(fname)}")

for tier in ['t1','t2','t3','t4','t5','t6']:
    for g in ['m','f']:
        fname = f'{SRC_DIR}bow_ranger_{tier}_{g}.png'
        if os.path.exists(fname):
            fix_arrow(fname)
print("Done.")
