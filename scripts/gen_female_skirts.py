#!/usr/bin/env python3
"""Generate female colored starter skirts (blue/green/orange/purple).

Parity fill: male warriors have 5 colored starter pants
(clothing/male/{,Blue_,Green_,Orange_,Purple_}Pants.png) but female warriors
had only a single skirt (clothing/female/Skirt.png) in the 'pants' slot. This
recolors that approved skirt into the same four color families used by the male
colored pants.

Technique — pure palette swap (identical to how the male colored pants relate
to the default): map each fabric tone of the source skirt onto a target color
ramp by luminance order, keep the (19,19,28) outline black, leave every
transparent pixel untouched. Geometry is unchanged, so all frames and animation
are preserved by construction and QA is a formality.
"""
import os
from PIL import Image

CLO = "sprites/preview_assets/clothing/female"
SRC = f"{CLO}/Skirt.png"
OUT_DIR = "_fem_skirt_preview"

OUTLINE = (19, 19, 28)  # kept as-is

# Source skirt fabric tones, darkest -> lightest (deep-shadow first).
SRC_RAMP = [
    (50, 23, 23),     # deep shadow
    (97, 75, 68),     # dark
    (163, 137, 130),  # mid
    (191, 176, 168),  # light
    (229, 218, 209),  # highlight
]

# Target color ramps taken directly from the committed male colored pants
# (clothing/male/*_Pants.png), ordered ascending luminance: dark->highlight.
PANTS_RAMP = {
    "Blue":   [(13, 34, 87), (25, 72, 147), (42, 112, 176), (37, 143, 174)],
    "Green":  [(18, 77, 23), (31, 112, 33), (59, 143, 46), (96, 166, 63)],
    "Orange": [(156, 54, 0), (207, 90, 0), (237, 121, 12), (255, 163, 26)],
    "Purple": [(19, 10, 51), (37, 19, 84), (67, 32, 122), (90, 45, 138)],
}


def darken(c, f):
    return (int(c[0] * f), int(c[1] * f), int(c[2] * f))


def build_map(color):
    ramp = PANTS_RAMP[color]
    # 5 source tones -> deepshadow(= darkest*0.6) + the 4 pants shades
    targets = [darken(ramp[0], 0.6)] + ramp
    return {src: tgt for src, tgt in zip(SRC_RAMP, targets)}


def recolor(src_img, cmap):
    im = src_img.copy()
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            key = (r, g, b)
            if key == OUTLINE:
                continue
            if key in cmap:
                nr, ng, nb = cmap[key]
                px[x, y] = (nr, ng, nb, a)
    return im


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = Image.open(SRC).convert("RGBA")
    for color in PANTS_RAMP:
        cmap = build_map(color)
        out = recolor(src, cmap)
        out_path = f"{OUT_DIR}/{color}_Skirt.png"
        out.save(out_path)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
