#!/usr/bin/env python3
"""Generate FEMALE warrior helmets tiers 2-6 (the documented gap).

Warrior helmets (helmet_2..helmet_6) are bitmap designs, not parametric like
the mage/ranger cone hats, so they can't be rebuilt from a builder. Instead we
PROPAGATE the approved male frame-0 helmet bitmap onto the female head geometry:

  1. Read the male helmet sheet's frame-0 design and express every opaque pixel
     as an offset (dx, dy) from the male frame-0 skull-dome anchor (head_top, cx).
  2. For each active frame, look up the FEMALE per-frame skull-dome anchor
     (head_dome_f from rebuild_class_hats — identical tracker to the committed
     male sheets and propagate_rare_helmets.py) and stamp the design there.

This keeps the helmet's exact appearance while re-seating it on the female head
(female head_top=22 vs male 21, so the helmet naturally drops 1px). Skull-dome
tracking — not full-head centroid — avoids the raised-arm drift on slash frames
(row 5) and the double-arm inflation on cheer frames (row 4). See
[[Known Issues Log]] "Cheer row inflated head width".

Writes to an --out dir so nothing in the repo working tree is touched until the
previews are approved. Run from repo root:

  python3 scripts/gen_female_warrior_helmets.py --out _fem_warrior_hat_preview
  python3 scripts/sprite_shade.py _fem_warrior_hat_preview/helmet_2_f.png
  python3 scripts/sprite_qa.py    _fem_warrior_hat_preview/helmet_2_f.png --y-min 2
"""
import argparse
import os
import numpy as np
from PIL import Image

import rebuild_class_hats as R   # reuse head_dome_m/f, get_active_frames, W/H/COLS

CH = R.CH
W, H, COLS = R.W, R.H, R.COLS


def frame_pixels(sheet, fi):
    """Yield ((x, y), (r,g,b,a)) for every opaque pixel in frame fi of a sheet."""
    c, r = fi % COLS, fi // COLS
    gx, gy = c * W, r * H
    cell = sheet[gy:gy + H, gx:gx + W]
    for y in range(H):
        for x in range(W):
            px = cell[y, x]
            if px[3] > 0:
                yield (x, y), tuple(int(v) for v in px)


def extract_design(male_sheet):
    """Design = frame-0 opaque pixels as (dx, dy) offsets from the male anchor."""
    anchor = R.head_dome_m(0)          # (head_top, cx) for male frame 0
    if anchor is None:
        raise RuntimeError("no male frame-0 head dome")
    ht, cx = anchor
    return [((x - cx, y - ht), rgba) for (x, y), rgba in frame_pixels(male_sheet, 0)]


def build_female_sheet(design, frames):
    sheet = np.zeros((H * 7, W * COLS, 4), np.uint8)
    for fi in frames:
        d = R.head_dome_f(fi)
        if d is None:
            continue
        ht, cx = d
        c, r = fi % COLS, fi // COLS
        gx, gy = c * W, r * H
        for (dx, dy), rgba in design:
            x, y = cx + dx, ht + dy
            if 0 <= x < W and 0 <= y < H:
                sheet[gy + y, gx + x] = rgba
    return sheet


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_fem_warrior_hat_preview")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    # Female active-frame set: identical 42 frames across all classes; borrow it
    # from a committed female helmet sheet.
    frames_f = R.get_active_frames(f"{CH}/helmet_mage1_f.png")

    for tier in range(2, 7):
        male_path = f"{CH}/helmet_{tier}.png"
        male_sheet = np.array(Image.open(male_path).convert("RGBA"))
        design = extract_design(male_sheet)
        sheet = build_female_sheet(design, frames_f)
        name = f"helmet_{tier}_f.png"
        Image.fromarray(sheet).save(f"{args.out}/{name}")
        print(f"wrote {name} ({len(frames_f)} frames, {len(design)} design px)")


if __name__ == "__main__":
    main()
