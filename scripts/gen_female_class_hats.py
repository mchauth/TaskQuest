#!/usr/bin/env python3
"""Generate FEMALE mage/ranger helmets tiers 2-6 (the documented gap).

Reuses the approved builders in rebuild_class_hats.py (mage_hat / ranger_hat,
head_dome_f, HW, get_active_frames, build_sheet) so geometry, palettes and the
skull-dome tracker are identical to the committed male sheets — only the skin
base (skin_f1) and active-frame set (from helmet_{cls}1_f) change.

Writes to an --out dir so nothing in the repo working tree is touched until the
previews are approved. Run from repo root:

  python3 scripts/gen_female_class_hats.py --out _fem_hat_preview
  python3 scripts/sprite_shade.py _fem_hat_preview/helmet_mage2_f.png
  python3 scripts/sprite_qa.py    _fem_hat_preview/helmet_mage2_f.png --y-min 2
"""
import argparse
import os
import numpy as np
from PIL import Image

import rebuild_class_hats as R   # module-level guard prevents its main() running


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_fem_hat_preview")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    builders = {"mage": R.mage_hat, "ranger": R.ranger_hat}
    for cls, builder in builders.items():
        t1f = f"{R.CH}/helmet_{cls}1_f.png"
        frames_f = R.get_active_frames(t1f)   # female active-frame set
        for tier in range(2, 7):
            sheet = R.build_sheet(builder, tier, frames_f, R.head_dome_f)
            name = f"helmet_{cls}{tier}_f.png"
            Image.fromarray(sheet).save(f"{args.out}/{name}")
            print(f"wrote {name} ({len(frames_f)} frames)")


if __name__ == "__main__":
    main()
