#!/usr/bin/env python3
"""Composite preview of female mage/ranger hat progression (t1 existing -> t6 new).

Frame-0 composite: skin_f1 + class shirt_f + helmet_f, cropped to head+torso,
scaled up, arranged in a labeled grid. t1 pulls the committed sheet; t2-6 pull
the freshly generated _fem_hat_preview sheets.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
NEW = "_fem_hat_preview"
FW, FH = 80, 64
SCALE = 7
CROP = (26, 8, 58, 44)   # x0,y0,x1,y1 head+torso region
BG = (58, 62, 78, 255)
PANEL = (40, 43, 55, 255)

TIER_NAMES = {
    "mage":   {1: "Apprentice", 2: "Apprentice II", 3: "Journeyman",
               4: "Arcane", 5: "Elder", 6: "Archmage"},
    "ranger": {1: "Scout", 2: "Tracker II", 3: "Pathfinder",
               4: "Stalker", 5: "Warden", 6: "Shadowstalker"},
}
LEVELS = {1: "L1", 2: "L5", 3: "L10", 4: "L20", 5: "L30", 6: "L40"}


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def load_font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def cell(cls, tier):
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    skin = frame0(f"{CH}/skin_f1.png")
    base.alpha_composite(skin)
    shirt = f"{CH}/shirt_{cls}{tier}_f.png"
    if os.path.exists(shirt):
        base.alpha_composite(frame0(shirt))
    hat = f"{CH}/helmet_{cls}{tier}_f.png" if tier == 1 else f"{NEW}/helmet_{cls}{tier}_f.png"
    base.alpha_composite(frame0(hat))
    crop = base.crop(CROP)
    cw, chh = crop.size
    scaled = crop.resize((cw * SCALE, chh * SCALE), Image.NEAREST)
    return scaled


def main():
    cols = [1, 2, 3, 4, 5, 6]
    rows = ["mage", "ranger"]
    sample = cell("mage", 1)
    cw, chh = sample.size
    pad, top, label_h, left = 16, 104, 40, 96
    grid_w = left + len(cols) * (cw + pad) + pad
    grid_h = top + len(rows) * (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    ftitle, fhdr, flbl, fsub = load_font(30), load_font(22), load_font(19), load_font(15)

    d.text((pad, 16), "TaskQuest — Female Class Hat Progression (NEW: t2-t6)",
           font=ftitle, fill=(240, 240, 250, 255))
    d.text((pad, 50), "t1 = existing/approved   |   t2-t6 = generated today, PASS shade+QA   |   preview only, not pushed",
           font=fsub, fill=(180, 184, 200, 255))

    # column headers
    for ci, tier in enumerate(cols):
        cx = left + ci * (cw + pad) + pad
        tag = "EXISTING" if tier == 1 else "NEW"
        col = (150, 200, 150, 255) if tier == 1 else (255, 210, 120, 255)
        d.text((cx, top - 26), f"T{tier}  {LEVELS[tier]}  [{tag}]", font=fsub, fill=col)

    for ri, cls in enumerate(rows):
        ry = top + ri * (chh + label_h + pad)
        d.text((pad, ry + chh // 2 - 12), cls.upper(), font=fhdr, fill=(230, 230, 240, 255))
        for ci, tier in enumerate(cols):
            cx = left + ci * (cw + pad) + pad
            d.rectangle([cx - 4, ry - 4, cx + cw + 4, ry + chh + 4], fill=PANEL)
            img.alpha_composite(cell(cls, tier), (cx, ry))
            name = TIER_NAMES[cls][tier]
            d.text((cx, ry + chh + 6), name, font=flbl, fill=(225, 225, 235, 255))

    out = "_fem_hat_preview/PREVIEW_female_hats.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
