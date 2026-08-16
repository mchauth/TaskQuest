#!/usr/bin/env python3
"""Approval preview for the 2nd legendary sets: Ember Magus (mage) + Frosthunter
(ranger). Frame-0 full-avatar composites (skin+hair+shirt+pants+boots+helmet),
male and female. For each set/gender: left = t4 SOURCE geometry it was recolored
from, right = the NEW legendary. Also a scaled raw helmet+shirt strip.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH = 80, 64
SCALE = 6
CROP = (18, 8, 62, 64)
BG = (26, 28, 40, 255)
PANEL = (40, 42, 60, 255)
LAYERS = ["shirt", "pants", "boots", "helmet"]

SETS = [
    ("Ember Magus", "mage2", "mage4", (250, 150, 44)),
    ("Frosthunter", "ranger2", "ranger4", (176, 206, 224)),
]
PREV = {"mage2": "_mage_legendary2_preview", "ranger2": "_ranger_legendary2_preview"}


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def font(sz, bold=True):
    p = f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def avatar(gender, tag, srctier, legendary):
    suf = "_f" if gender == "f" else ""
    g = "f" if gender == "f" else "m"
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame0(f"{CH}/skin_{g}1.png"))
    base.alpha_composite(frame0(f"{CH}/hair_{g}1.png"))
    for slot in LAYERS:
        if legendary:
            path = f"{PREV[tag]}/{slot}_rare_{tag}{suf}.png"
        else:
            path = f"{CH}/{slot}_{srctier}{suf}.png"
        if os.path.exists(path):
            base.alpha_composite(frame0(path))
    crop = base.crop(CROP)
    return crop.resize((crop.width * SCALE, crop.height * SCALE), Image.NEAREST)


def main():
    cell_w = (CROP[2] - CROP[0]) * SCALE
    cell_h = (CROP[3] - CROP[1]) * SCALE
    pad = 16
    title_h = 40
    label_h = 22
    # per set: header + 2 genders x (src,new) = 4 avatars in a row
    row_w = pad + 4 * (cell_w + pad)
    row_h = title_h + label_h + cell_h + pad
    W = row_w
    H = pad + len(SETS) * row_h + pad
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    fT = font(26); fL = font(15); fS = font(13, False)

    y = pad
    for name, tag, srctier, accent in SETS:
        d.text((pad, y), f"{name}  —  L25 legendary  (rare_{tag})", font=fT, fill=accent)
        yy = y + title_h
        cols = [("m SOURCE t4", "m", srctier, False),
                ("m NEW", "m", tag, True),
                ("f SOURCE t4", "f", srctier, False),
                ("f NEW", "f", tag, True)]
        x = pad
        for lbl, gender, _t, leg in cols:
            panel = Image.new("RGBA", (cell_w, cell_h), PANEL)
            av = avatar(gender, tag, srctier, leg)
            panel.alpha_composite(av, ((cell_w - av.width)//2, (cell_h - av.height)//2))
            img.alpha_composite(panel, (x, yy + label_h))
            col = accent if leg else (150, 152, 168)
            d.text((x + 4, yy), lbl, font=fL, fill=col)
            x += cell_w + pad
        y += row_h

    img.convert("RGB").save("_PREVIEW_legendary2.png")
    img.convert("RGB").save(os.path.join(os.environ.get("OUTDIR", "."), "PREVIEW_legendary2.png"))
    print("wrote _PREVIEW_legendary2.png", img.size)


if __name__ == "__main__":
    main()
