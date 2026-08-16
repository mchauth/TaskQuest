"""
Generate warrior chest armor progression (tiers 2-6) using a palette-remap +
detail-painting method, starting from the base tunic silhouette in shirt.png.

Base remap rule (derived from leather_armor_1.png, tier 1, which matches this
exactly): shirt.png has 4 source colors. Sorted by luminance:
  (97,75,68)    darkest      -> tier outline
  (163,137,130) mid-dark   \
  (191,176,168) mid-light  / -> tier mid   (both middle colors collapse to "mid")
  (229,218,209) lightest      -> tier highlight

Then tier-specific detail pixels are painted on top, using each frame's
bounding box (bbox) to place details proportionally (shoulder rims, studs,
chain texture, plate lines, chest pad clusters, facet lines, center seam).
"""

from PIL import Image
import numpy as np
import os

ROOT = '/Users/matthauth/Projects/TaskQuest'
SHIRT_PATH = f'{ROOT}/sprites/preview_assets/char/shirt.png'
SKIN_PATH = f'{ROOT}/sprites/preview_assets/char/skin_m1.png'
OUT_DIR = f'{ROOT}/sprites/preview_assets/char'
SCRATCH = f'{ROOT}/sprites/scratch/armor_progression'

FW, FH = 80, 64
COLS, ROWS = 10, 7

DARK = (97, 75, 68)
MIDDARK = (163, 137, 130)
MIDLIGHT = (191, 176, 168)
LIGHT = (229, 218, 209)


def load_rgba(path):
    return np.array(Image.open(path).convert('RGBA'))


def base_remap(shirt, outline, mid, highlight):
    out = shirt.copy()
    rgb = shirt[:, :, :3]

    def m(color):
        return (rgb[:, :, 0] == color[0]) & (rgb[:, :, 1] == color[1]) & (rgb[:, :, 2] == color[2])

    out[m(DARK), :3] = outline
    out[m(MIDDARK), :3] = mid
    out[m(MIDLIGHT), :3] = mid
    out[m(LIGHT), :3] = highlight
    return out


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


def opaque(armor, gy, gx):
    return armor[gy, gx, 3] > 0


def cur_color(armor, gy, gx):
    return tuple(int(v) for v in armor[gy, gx, :3])


def set_color(armor, gy, gx, color):
    if opaque(armor, gy, gx):
        armor[gy, gx, :3] = color


def shoulder_rows(h, frac=0.22):
    return max(1, round(h * frac))


def chest_pad_positions(h, w):
    cluster_top = round(h * 0.32)
    c1_left = round(w * 0.22)
    c2_left = round(w * 0.56)
    return cluster_top, c1_left, c2_left


# ----------------------------------------------------------------------
# Tier-specific detail painters. Each receives the full armor sheet array
# (already base-remapped) plus one frame's (r, c, y0, y1, x0, x1) bbox and
# the tier's mid/outline/highlight colors, and paints details in place.
# ----------------------------------------------------------------------

def details_studded_leather(armor, frame, mid, outline, highlight):
    r, c, y0, y1, x0, x1 = frame
    h, w = y1 - y0 + 1, x1 - x0 + 1
    base_y, base_x = r * FH + y0, c * FW + x0
    STUD = (160, 160, 155)
    RIM = (65, 38, 15)

    # scattered metal studs every ~3px on the leather "mid" field
    for ly in range(h):
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if ly % 3 == 1 and lx % 3 == 1 and cur_color(armor, gy, gx) == mid:
                set_color(armor, gy, gx, STUD)

    # darker shoulder rims along the top of the bbox
    sh = shoulder_rows(h)
    for ly in range(sh):
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if cur_color(armor, gy, gx) == mid:
                set_color(armor, gy, gx, RIM)


def details_chainmail(armor, frame, mid, outline, highlight):
    r, c, y0, y1, x0, x1 = frame
    h, w = y1 - y0 + 1, x1 - x0 + 1
    base_y, base_x = r * FH + y0, c * FW + x0
    CHAIN_DARK = (90, 92, 98)
    SHOULDER_BRIGHT = (200, 202, 208)

    # alternating-column chain texture in the lower 60% of the bbox
    lower_start = h - round(h * 0.6)
    for ly in range(lower_start, h):
        for lx in range(w):
            if lx % 2 != 0:
                continue
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if cur_color(armor, gy, gx) == mid:
                set_color(armor, gy, gx, CHAIN_DARK)

    # brighter shoulder band
    sh = shoulder_rows(h)
    for ly in range(sh):
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if cur_color(armor, gy, gx) in (mid, highlight):
                set_color(armor, gy, gx, SHOULDER_BRIGHT)


def details_iron_plate(armor, frame, mid, outline, highlight):
    r, c, y0, y1, x0, x1 = frame
    h, w = y1 - y0 + 1, x1 - x0 + 1
    base_y, base_x = r * FH + y0, c * FW + x0
    PLATE_LINE = (60, 62, 68)
    PAD = (175, 178, 185)
    RIM = (50, 52, 58)

    # horizontal plate-line separators every 3 rows in the lower half
    half = h // 2
    for ly in range(half, h):
        if (ly - half) % 3 != 0:
            continue
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if cur_color(armor, gy, gx) in (mid, highlight):
                set_color(armor, gy, gx, PLATE_LINE)

    # shoulder rims
    sh = shoulder_rows(h)
    for ly in range(sh):
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if cur_color(armor, gy, gx) == mid:
                set_color(armor, gy, gx, RIM)

    # two 2x2 chest pad clusters, brighter silver
    cluster_top, c1_left, c2_left = chest_pad_positions(h, w)
    for ly in (cluster_top, cluster_top + 1):
        for lx in (c1_left, c1_left + 1, c2_left, c2_left + 1):
            gy, gx = base_y + ly, base_x + lx
            if 0 <= ly < h and 0 <= lx < w:
                set_color(armor, gy, gx, PAD)


def details_crystal(armor, frame, mid, outline, highlight, facet, rim, seam, pad):
    """Shared facet/rim/seam/pad detail painter for diamond + emerald tiers."""
    r, c, y0, y1, x0, x1 = frame
    h, w = y1 - y0 + 1, x1 - x0 + 1
    base_y, base_x = r * FH + y0, c * FW + x0

    # diagonal facet highlight lines across the chest
    for ly in range(h):
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if (lx - ly) % 4 == 0 and cur_color(armor, gy, gx) == mid:
                set_color(armor, gy, gx, facet)

    # bright rim around the shoulder area
    sh = shoulder_rows(h, frac=0.20)
    for ly in range(sh):
        for lx in range(w):
            gy, gx = base_y + ly, base_x + lx
            if not opaque(armor, gy, gx):
                continue
            if cur_color(armor, gy, gx) in (mid, highlight):
                set_color(armor, gy, gx, rim)

    # two 2x2 chest pad clusters
    cluster_top, c1_left, c2_left = chest_pad_positions(h, w)
    for ly in (cluster_top, cluster_top + 1):
        for lx in (c1_left, c1_left + 1, c2_left, c2_left + 1):
            gy, gx = base_y + ly, base_x + lx
            if 0 <= ly < h and 0 <= lx < w:
                set_color(armor, gy, gx, pad)

    # 2px-tall center seam between the two pad clusters
    seam_cols = range(c1_left + 2, c2_left)
    for ly in (cluster_top, cluster_top + 1):
        for lx in seam_cols:
            gy, gx = base_y + ly, base_x + lx
            if 0 <= ly < h and 0 <= lx < w:
                set_color(armor, gy, gx, seam)


TIERS = {
    2: dict(
        name='studded_leather',
        outline=(25, 15, 5), mid=(95, 58, 25), highlight=(140, 90, 42),
        details=details_studded_leather,
    ),
    3: dict(
        name='chainmail',
        outline=(35, 35, 38), mid=(110, 112, 118), highlight=(185, 188, 195),
        details=details_chainmail,
    ),
    4: dict(
        name='iron_plate',
        outline=(28, 28, 32), mid=(85, 88, 95), highlight=(160, 165, 175),
        details=details_iron_plate,
    ),
    5: dict(
        name='diamond',
        outline=(30, 55, 80), mid=(95, 175, 220), highlight=(200, 235, 255),
        details=lambda armor, frame, mid, outline, highlight: details_crystal(
            armor, frame, mid, outline, highlight,
            facet=(220, 245, 255), rim=(80, 160, 210),
            seam=(40, 70, 100), pad=(80, 155, 200),
        ),
    ),
    6: dict(
        name='emerald',
        outline=(15, 45, 20), mid=(55, 140, 65), highlight=(110, 210, 120),
        details=lambda armor, frame, mid, outline, highlight: details_crystal(
            armor, frame, mid, outline, highlight,
            facet=(130, 230, 145), rim=(35, 100, 45),
            seam=(20, 60, 28), pad=(50, 120, 58),
        ),
    ),
}


def main():
    shirt = load_rgba(SHIRT_PATH)
    frames = get_frames(shirt)
    print(f'Found {len(frames)} populated frames')

    for tier_n, spec in TIERS.items():
        armor = base_remap(shirt, spec['outline'], spec['mid'], spec['highlight'])
        for frame in frames:
            spec['details'](armor, frame, spec['mid'], spec['outline'], spec['highlight'])

        out_path = f'{OUT_DIR}/armor_chest_{tier_n}.png'
        Image.fromarray(armor, 'RGBA').save(out_path)

        # pixel count report
        mask = armor[:, :, 3] > 0
        total = mask.sum()
        from collections import Counter
        counts = Counter(map(tuple, armor[mask][:, :3]))
        print(f'\n=== Tier {tier_n} ({spec["name"]}) -> {out_path} ===')
        print(f'  total opaque pixels: {total}')
        for color, n in counts.most_common():
            print(f'    {color}: {n}')


if __name__ == '__main__':
    main()
