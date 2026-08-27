"""
add_staff_orb.py — add glowing energy orb at staff tip in slash frames 51-53.
Finds the topmost visible pixels in those frames (the staff tip) and draws
a glowing orb around them. Does NOT touch other frames or the bow shape.
"""
import numpy as np
from PIL import Image
import os

FW, FH, COLS = 80, 64, 10

STAFF_TRAILS = {
    't1': ((180,120,255,255), (220,180,255,180)),
    't2': ((100,160,255,255), (160,200,255,180)),
    't3': ((80,220,120,255),  (160,255,180,180)),
    't4': ((255,200,60,255),  (255,230,120,180)),
    't5': ((255,80,80,255),   (255,160,120,180)),
    't6': ((200,160,255,255), (160,200,255,180)),
}

def add_orb(fname, tier):
    core_c, glow_c = STAFF_TRAILS[tier]
    img = Image.open(fname).convert('RGBA')
    arr = np.array(img)

    for fi in [51, 52, 53]:
        r2, c2 = fi // COLS, fi % COLS
        gx, gy = c2 * FW, r2 * FH
        frame = arr[gy:gy+FH, gx:gx+FW]

        # Find topmost visible pixels (staff tip)
        op = np.argwhere(frame[..., 3] > 0)
        if len(op) == 0:
            continue
        top_y = int(op[:, 0].min())
        top_pts = op[op[:, 0] <= top_y + 3]
        orb_y = max(3, min(FH-4, top_y + 1))
        orb_x = max(3, min(FW-4, int(np.mean(top_pts[:, 1]))))

        # Draw glow halo then bright core on top
        for dy in range(-3, 4):
            for dx in range(-3, 4):
                ry, rx = orb_y + dy, orb_x + dx
                if 0 <= ry < FH and 0 <= rx < FW:
                    dist = abs(dy) + abs(dx)
                    if dist <= 1:
                        arr[gy + ry, gx + rx] = core_c
                    elif dist <= 4:
                        # Blend glow with existing pixel
                        arr[gy + ry, gx + rx] = glow_c

    Image.fromarray(arr).save(fname)
    print(f"  Orb added: {os.path.basename(fname)}")

OUT_DIR = '/tmp/tq_bow2/sprites/preview_assets/char/'
for tier in ['t1','t2','t3','t4','t5','t6']:
    for g in ['m','f']:
        fname = f'{OUT_DIR}staff_mage_{tier}_{g}.png'
        if os.path.exists(fname):
            add_orb(fname, tier)

print("Done.")
