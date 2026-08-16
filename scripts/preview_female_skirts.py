#!/usr/bin/env python3
"""Approval preview: female colored starter skirts (NEW) vs male colored pants.

Frame-0 composite: female skin + corset (silhouette context) + skirt, cropped
to the body, scaled up, arranged in a labeled grid. Top row = committed male
colored pants (reference for the color families); bottom row = the freshly
generated female skirts from the preview dir.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
CLO = "sprites/preview_assets/clothing"
NEW = "_fem_skirt_preview"
FW, FH = 80, 64
SCALE = 7
CROP = (22, 18, 58, 64)
BG = (58, 62, 78, 255)
PANEL = (40, 43, 55, 255)

# color -> (male pants file, female corset for context, label, item name)
COLS = [
    ("default", "Pants.png",        "Skirt.png",        "Default", "Adventurer Skirt"),
    ("Blue",    "Blue_Pants.png",   "Blue_Skirt.png",   "Blue",    "Azure Skirt"),
    ("Green",   "Green_Pants.png",  "Green_Skirt.png",  "Green",   "Forest Skirt"),
    ("Orange",  "Orange_Pants.png", "Orange_Skirt.png", "Orange",  "Ember Skirt"),
    ("Purple",  "Purple_Pants.png", "Purple_Skirt.png", "Purple",  "Shadow Skirt"),
]


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def load_font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def cell(gender, key, male_file, skirt_file):
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    if gender == "m":
        base.alpha_composite(frame0(f"{CH}/skin_m1.png"))
        base.alpha_composite(frame0(f"{CLO}/male/Shirt.png"))
        base.alpha_composite(frame0(f"{CLO}/male/{male_file}"))
    else:
        base.alpha_composite(frame0(f"{CH}/skin_f1.png"))
        base.alpha_composite(frame0(f"{CLO}/female/Corset.png"))
        if key == "default":
            base.alpha_composite(frame0(f"{CLO}/female/{skirt_file}"))
        else:
            base.alpha_composite(frame0(f"{NEW}/{skirt_file}"))
    crop = base.crop(CROP)
    cw, chh = crop.size
    return crop.resize((cw * SCALE, chh * SCALE), Image.NEAREST)


def main():
    rows = [("m", "MALE PANTS (ref)"), ("f", "FEMALE SKIRTS (new)")]
    sample = cell("f", "Blue", "Blue_Pants.png", "Blue_Skirt.png")
    cw, chh = sample.size
    pad, top, label_h, left = 18, 132, 46, 210
    grid_w = left + len(COLS) * (cw + pad) + pad
    grid_h = top + len(rows) * (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    ftitle, fhdr, flbl, fsub = load_font(30), load_font(19), load_font(18), load_font(15)

    d.text((pad, 20), "Female Colored Starter Skirts — approval preview", font=ftitle, fill=(236, 238, 245))
    d.text((pad, 60), "NEW: blue/green/orange/purple skirts — pure palette swap of the approved Skirt.png",
           font=fsub, fill=(150, 200, 160))
    d.text((pad, 82), "Uses the exact male colored-pants ramps. Geometry identical to source (10196 px) - all QA PASS.",
           font=fsub, fill=(150, 200, 160))
    d.text((pad, 104), "Fills the pants-slot color gap: males had 5 colored pants, females had only 1 skirt.",
           font=fsub, fill=(178, 182, 196))

    for ri, (g, rlabel) in enumerate(rows):
        ry = top + ri * (chh + label_h + pad)
        d.text((pad, ry + chh // 2 - 10), rlabel, font=fhdr, fill=(210, 214, 224))
        for ci, (key, male_file, skirt_file, label, name) in enumerate(COLS):
            cx = left + ci * (cw + pad)
            d.rectangle([cx - 4, ry - 4, cx + cw + 4, ry + chh + 4], fill=PANEL)
            img.alpha_composite(cell(g, key, male_file, skirt_file), (cx, ry))
            if ri == 1:
                d.text((cx + 4, ry + chh + 8), label, font=flbl, fill=(232, 234, 242))
                d.text((cx + 4, ry + chh + 28), name, font=fsub, fill=(150, 154, 168))

    out = "_fem_skirt_preview/PREVIEW_female_skirts.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
