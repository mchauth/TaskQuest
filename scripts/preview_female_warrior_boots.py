#!/usr/bin/env python3
"""Approval preview: female warrior tier boots t1-6 (NEW) vs male reference.

Frame-0 composite: skin + warrior tier pants + boots, cropped to the lower
body / feet, scaled up, arranged in a labeled grid. Top row = committed male
boots (visual reference); bottom row = freshly generated female boots from the
preview dir. Boots are the review target, so pants are included only for
silhouette context.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
NEW = "_fem_warrior_boots_preview"
FW, FH = 80, 64
SCALE = 8
CROP = (24, 34, 58, 64)   # x0,y0,x1,y1 lower-body + feet region
BG = (58, 62, 78, 255)
PANEL = (40, 43, 55, 255)

# tier -> (male boot file stem, female pants stem for context, name, level)
TIERS = [
    (1, "leather_boots_1", "leather_pants_1", "Leather Boots",   "L1"),
    (2, "armor_boots_2",   "armor_pants_2",   "Studded Leather", "L5"),
    (3, "armor_boots_3",   "armor_pants_3",   "Chainmail",       "L10"),
    (4, "armor_boots_4",   "armor_pants_4",   "Silver Sabatons", "L20"),
    (5, "armor_boots_5",   "armor_pants_5",   "Gold Sabatons",   "L30"),
    (6, "armor_boots_6",   "armor_pants_6",   "Diamond Sabatons","L40"),
]


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def load_font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def cell(gender, boot_stem, pants_stem):
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    suf = "_f" if gender == "f" else ""
    base.alpha_composite(frame0(f"{CH}/skin_{'f' if gender=='f' else 'm'}1.png"))
    pants = f"{CH}/{pants_stem}{suf}.png"
    if os.path.exists(pants):
        base.alpha_composite(frame0(pants))
    boot = f"{CH}/{boot_stem}.png" if gender == "m" else f"{NEW}/{boot_stem}_f.png"
    base.alpha_composite(frame0(boot))
    crop = base.crop(CROP)
    cw, chh = crop.size
    return crop.resize((cw * SCALE, chh * SCALE), Image.NEAREST)


def main():
    rows = [("m", "MALE (ref)"), ("f", "FEMALE (new)")]
    sample = cell("m", "armor_boots_2", "armor_pants_2")
    cw, chh = sample.size
    pad, top, label_h, left = 18, 150, 42, 176
    grid_w = left + len(TIERS) * (cw + pad) + pad
    grid_h = top + len(rows) * (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    ftitle, fhdr, flbl, fsub = load_font(30), load_font(20), load_font(18), load_font(15)

    d.text((pad, 22), "Female Warrior Tier Boots — approval preview", font=ftitle, fill=(236, 238, 245))
    d.text((pad, 62), "NEW female boots warped from male tiers (run-mapping) · all 6 shaded + QA PASS · 45/45 frames",
           font=fsub, fill=(150, 200, 160))

    for ri, (g, rlabel) in enumerate(rows):
        ry = top + ri * (chh + label_h + pad)
        d.text((pad, ry + chh // 2 - 10), rlabel, font=fhdr, fill=(210, 214, 224))
        for ci, (tier, boot_stem, pants_stem, name, lvl) in enumerate(TIERS):
            cx = left + ci * (cw + pad)
            d.rectangle([cx - 4, ry - 4, cx + cw + 4, ry + chh + 4], fill=PANEL)
            img.alpha_composite(cell(g, boot_stem, pants_stem), (cx, ry))
            if ri == 0:
                d.text((cx, top - 58), name, font=flbl, fill=(232, 210, 140))
                d.text((cx, top - 34), lvl, font=fsub, fill=(150, 154, 168))

    out = f"{NEW}/PREVIEW_female_warrior_boots.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
