#!/usr/bin/env python3
"""Generate FEMALE warrior tier boots from the male warrior boot tiers.

The documented gap: female warrior had full chest / pants / helmet tier
progressions but NO tiered boots (only the 3 rare-set sabatons). Boots are
ground-aligned foot coverings, so they warp onto the female foot silhouette
with the exact same proven run-mapping technique used for the female leggings
(scripts/gen_female_leggings.py): per frame, intersect the male boot's row
band (ground-aligned) with the female skin silhouette, then transfer colors by
relative run mapping so run endpoints map to run endpoints and outlines survive.

We reuse gen_female_leggings.gen_frame verbatim. We do NOT run its downward
cuff-extension pass (pass 3 of fix_passes) — boots already sit at the foot, so
there is nothing below to extend into, and running it risks bleeding boot color
up the shin. We keep only the horizontal gap-fill and vertical hole-fill passes,
which repair 1px seams introduced by the remap.

Writes to an --out dir so the repo working tree is untouched until the daily
preview is approved. Run from repo root:

  python3 scripts/gen_female_warrior_boots.py --out _fem_warrior_boots_preview
  python3 scripts/sprite_shade.py _fem_warrior_boots_preview/armor_boots_2_f.png
  python3 scripts/sprite_qa.py    _fem_warrior_boots_preview/armor_boots_2_f.png --y-max 63
"""
import argparse
import os
import numpy as np
from PIL import Image

import gen_female_leggings as L   # reuse gen_frame + run-mapping machinery

CHAR = L.CHAR
FW, FH = L.FW, L.FH

PAIRS = [
    ('leather_boots_1', 'leather_boots_1_f'),
    ('armor_boots_2',   'armor_boots_2_f'),
    ('armor_boots_3',   'armor_boots_3_f'),
    ('armor_boots_4',   'armor_boots_4_f'),
    ('armor_boots_5',   'armor_boots_5_f'),
    ('armor_boots_6',   'armor_boots_6_f'),
]


def boot_fix(mp, fs, out):
    """Boot-safe repair: horizontal gap-fill + vertical hole-fill only.

    Same as gen_female_leggings.fix_passes passes 1 & 2; omits the downward
    cuff-extension pass, which is meaningless (and risky) for footwear.
    """
    pm = mp[..., 3] > 0
    if not pm.any():
        return
    ys, xs = np.where(pm)
    cols = mp[ys, xs, :3].astype(int)
    lum = cols @ [3, 6, 1]
    seam = mp[ys[lum.argmin()], xs[lum.argmin()]]

    def covered(y, x):
        return out[y, x, 3] > 0

    # 1. horizontal interior gap fill within one skin run
    for y in range(FH):
        if not fs[y].any():
            continue
        for x in range(FW):
            if not fs[y, x] or covered(y, x):
                continue
            ok_l = ok_r = False
            for d in (1, 2):
                if x - d >= 0 and fs[y, x - d] and covered(y, x - d):
                    ok_l = True; break
                if x - d < 0 or not fs[y, x - d]:
                    break
            for d in (1, 2):
                if x + d < FW and fs[y, x + d] and covered(y, x + d):
                    ok_r = True; break
                if x + d >= FW or not fs[y, x + d]:
                    break
            if ok_l and ok_r:
                out[y, x] = seam

    # 2. vertical hole fill: skin pixel covered above and below
    for y in range(1, FH - 1):
        for x in range(FW):
            if fs[y, x] and not covered(y, x) and covered(y - 1, x) and covered(y + 1, x):
                out[y, x] = out[y - 1, x]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_fem_warrior_boots_preview")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    skin_m = L.load('skin_m1.png')
    skin_f = L.load('skin_f1.png')
    am = skin_m[..., 3] > 0
    af = skin_f[..., 3] > 0

    for src, dst in PAIRS:
        mp = L.load(src + '.png')
        out = np.zeros_like(mp)
        for r in range(7):
            for c in range(10):
                sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
                L.gen_frame(mp[sl], am[sl], af[sl], out[sl])
                boot_fix(mp[sl], af[sl], out[sl])
        Image.fromarray(out).save(f"{args.out}/{dst}.png")
        print(f"{dst} written, {int((out[..., 3] > 0).sum())} px")


if __name__ == '__main__':
    main()
