"""
Redesign of armor_chest_4 (Iron Plate), armor_chest_5 (Diamond) and
armor_chest_6 (Emerald): instead of a flat recolor of the tunic, paint an
actual segmented plate structure (pauldrons, chest plate, ab guard strips)
with a 4-tone ramp (highlight edge / face / shadow edge / separator gap) to
give the plates a raised, dimensional look.

Step 1: fresh 3-tone remap of shirt.png -> darkest source -> shadow,
        middle two sources -> face, lightest source -> highlight edge.
Step 2: paint plate segments on top, using each frame's bbox to scale the
        pauldron / chest / ab-guard zones proportionally.
"""

from PIL import Image
import numpy as np

ROOT = '/Users/matthauth/Projects/TaskQuest'
SHIRT_PATH = f'{ROOT}/sprites/preview_assets/char/shirt.png'
OUT_DIR = f'{ROOT}/sprites/preview_assets/char'

FW, FH = 80, 64
COLS, ROWS = 10, 7

DARK = (97, 75, 68)
MIDDARK = (163, 137, 130)
MIDLIGHT = (191, 176, 168)
LIGHT = (229, 218, 209)


def load_rgba(path):
    return np.array(Image.open(path).convert('RGBA'))


def get_frames(shirt):
    frames = []
    for r in range(ROWS):
        for c in range(COLS):
            sub_alpha = shirt[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW, 3]
            if sub_alpha.max() == 0:
                continue
            ys, xs = np.where(sub_alpha > 0)
            y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
            frames.append((r, c, int(y0), int(y1), int(x0), int(x1)))
    return frames


def base_remap3(shirt, highlight, face, shadow):
    out = shirt.copy()
    rgb = shirt[:, :, :3]

    def m(color):
        return (rgb[:, :, 0] == color[0]) & (rgb[:, :, 1] == color[1]) & (rgb[:, :, 2] == color[2])

    out[m(DARK), :3] = shadow
    out[m(MIDDARK), :3] = face
    out[m(MIDLIGHT), :3] = face
    out[m(LIGHT), :3] = highlight
    return out


def paint_plate_armor(armor, frame, face, hi, sh, sep):
    r, c, y0, y1, x0, x1 = frame
    h, w = y1 - y0 + 1, x1 - x0 + 1
    base_y, base_x = r * FH + y0, c * FW + x0

    def is_opaque(ly, lx):
        return armor[base_y + ly, base_x + lx, 3] > 0

    def set_if_opaque(ly, lx, color):
        if 0 <= ly < h and 0 <= lx < w and is_opaque(ly, lx):
            armor[base_y + ly, base_x + lx, :3] = color

    # ---- Zone heights ----
    shoulder_h = min(max(2, round(h * 0.2)), h)
    chest_h = min(max(3, round(h * 0.33)), h - shoulder_h)
    ab_h = h - shoulder_h - chest_h

    # ---- Pauldrons (left 40% / right 40% of width) ----
    pw = max(1, round(w * 0.4))
    right_start = max(pw, w - pw)
    sides = [list(range(0, pw)), list(range(right_start, w))]

    for side_idx, cols in enumerate(sides):
        if not cols:
            continue
        if shoulder_h >= 1:
            for lx in cols:
                set_if_opaque(0, lx, hi)
        if shoulder_h >= 2:
            for lx in cols:
                set_if_opaque(shoulder_h - 1, lx, sh)
        outer = cols[:2] if side_idx == 0 else cols[-2:]
        for ly in range(1, shoulder_h - 1):
            for lx in cols:
                set_if_opaque(ly, lx, hi if lx in outer else face)

    # ---- Chest plate (full width) ----
    for i in range(chest_h):
        ly = shoulder_h + i
        if i == 0:
            for lx in range(w):
                set_if_opaque(ly, lx, hi)
        elif i == chest_h - 1:
            for lx in range(w):
                set_if_opaque(ly, lx, sh)
        else:
            for lx in range(w):
                set_if_opaque(ly, lx, face)
            opq = [lx for lx in range(w) if is_opaque(ly, lx)]
            if opq:
                set_if_opaque(ly, opq[0], hi)
                set_if_opaque(ly, opq[-1], hi)

    # ---- Ab guard (2 strips, 1px separator if room) ----
    ab_start = shoulder_h + chest_h
    if ab_h >= 3:
        strip1_h = (ab_h - 1) // 2
        strip2_h = ab_h - 1 - strip1_h
        sep_row = ab_start + strip1_h
        strips = [(ab_start, strip1_h), (sep_row + 1, strip2_h)]
        for lx in range(w):
            set_if_opaque(sep_row, lx, sep)
    elif ab_h == 2:
        strips = [(ab_start, 1), (ab_start + 1, 1)]
    elif ab_h == 1:
        strips = [(ab_start, 1)]
    else:
        strips = []

    for start_row, sh_h in strips:
        for i in range(sh_h):
            ly = start_row + i
            if sh_h == 1:
                color = sh
            elif i == 0:
                color = hi
            elif i == sh_h - 1:
                color = sh
            else:
                color = face
            for lx in range(w):
                set_if_opaque(ly, lx, color)


TIERS = {
    4: dict(name='iron_plate',
            hi=(210, 215, 225), face=(120, 125, 135), sh=(55, 58, 65), sep=(35, 37, 42)),
    5: dict(name='diamond',
            hi=(230, 248, 255), face=(110, 190, 230), sh=(45, 90, 130), sep=(25, 50, 80)),
    6: dict(name='emerald',
            hi=(195, 255, 195), face=(60, 175, 75), sh=(20, 75, 30), sep=(12, 45, 18)),
}


def main():
    shirt = load_rgba(SHIRT_PATH)
    frames = get_frames(shirt)
    shirt_mask = shirt[:, :, 3] > 0

    for tier_n, spec in TIERS.items():
        armor = base_remap3(shirt, spec['hi'], spec['face'], spec['sh'])
        for frame in frames:
            paint_plate_armor(armor, frame, spec['face'], spec['hi'], spec['sh'], spec['sep'])

        out_path = f'{OUT_DIR}/armor_chest_{tier_n}.png'
        Image.fromarray(armor).save(out_path)

        mask = armor[:, :, 3] > 0
        from collections import Counter
        counts = Counter(map(tuple, armor[mask][:, :3]))
        print(f'\n=== Tier {tier_n} ({spec["name"]}) -> {out_path} ===')
        print(f'  mask preserved: {np.array_equal(mask, shirt_mask)}  total opaque: {mask.sum()}')
        for color, n in counts.most_common():
            print(f'    {color}: {n}')


if __name__ == '__main__':
    main()
