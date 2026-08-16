#!/usr/bin/env python3
"""Approval preview: female warrior helmets t2-6 (NEW) vs male reference.

Frame-0 composite: skin + warrior tier chest + helmet, cropped to head+torso,
scaled up, arranged in a labeled grid. Top row = committed male helmet (visual
reference); bottom row = freshly generated female helmet from the preview dir.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
NEW = "_fem_warrior_hat_preview"
FW, FH = 80, 64
SCALE = 7
CROP = (26, 8, 58, 44)   # x0,y0,x1,y1 head+torso region
BG = (58, 62, 78, 255)
PANEL = (40, 43, 55, 255)

TIER_NAMES = {2: "Studded Leather", 3: "Chainmail", 4: "Silver Plate",
              5: "Gold Plate", 6: "Diamond Plate"}
LEVELS = {2: "L5", 3: "L10", 4: "L20", 5: "L30", 6: "L40"}


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def load_font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def cell(gender, tier):
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    suf = "_f" if gender == "f" else ""
    base.alpha_composite(frame0(f"{CH}/skin_{'f' if gender=='f' else 'm'}1.png"))
    chest = f"{CH}/armor_chest_{tier}{suf}.png"
    if os.path.exists(chest):
        base.alpha_composite(frame0(chest))
    hat = f"{CH}/helmet_{tier}.png" if gender == "m" else f"{NEW}/helmet_{tier}_f.png"
    base.alpha_composite(frame0(hat))
    crop = base.crop(CROP)
    cw, chh = crop.size
    return crop.resize((cw * SCALE, chh * SCALE), Image.NEAREST)


def main():
    cols = [2, 3, 4, 5, 6]
    rows = [("m", "MALE (ref)"), ("f", "FEMALE (new)")]
    sample = cell("m", 2)
    cw, chh = sample.size
    pad, top, label_h, left = 16, 104, 40, 130
    grid_w = left + len(cols) * (cw + pad) + pad
    grid_h = top + len(rows) * (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    ftitle, fhdr, flbl, fsub = load_font(30), load_font(20), load_font(18), load_font(15)

    d.text((pad, 16), "TaskQuest — Female Warrior Helmets t2-t6 (NEW)",
           font=ftitle, fill=(240, 240, 250, 255))
    d.text((pad, 52),
           "Male frame-0 design propagated onto female head geometry  |  all PASS shade+QA  |  preview only, not pushed",
           font=fsub, fill=(180, 184, 200, 255))

    for ci, tier in enumerate(cols):
        cx = left + ci * (cw + pad) + pad
        d.text((cx, top - 26), f"T{tier}  {LEVELS[tier]}", font=fsub, fill=(255, 210, 120, 255))

    for ri, (g, glabel) in enumerate(rows):
        ry = top + ri * (chh + label_h + pad)
        d.text((pad, ry + chh // 2 - 12), glabel, font=fhdr, fill=(230, 230, 240, 255))
        for ci, tier in enumerate(cols):
            cx = left + ci * (cw + pad) + pad
            d.rectangle([cx - 4, ry - 4, cx + cw + 4, ry + chh + 4], fill=PANEL)
            img.alpha_composite(cell(g, tier), (cx, ry))
            if ri == 1:
                d.text((cx, ry + chh + 6), TIER_NAMES[tier], font=flbl, fill=(225, 225, 235, 255))

    out = f"{NEW}/PREVIEW_female_warrior_helmets.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
