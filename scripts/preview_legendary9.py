#!/usr/bin/env python3
"""Approval preview for the 9th legendary sets (2026-07-25 batch):
  Tidewarden Sovereign (warrior, teal/turquoise),
  Celestial Magus (mage, opal/pearl-white),
  Sunspear Warden (ranger, yellow-gold).

Frame-0 full-avatar composites (skin+hair+shirt+pants+boots+helmet), male and
female. For each set/gender: left = SOURCE geometry it was recolored from,
right = the NEW legendary. Writes _PREVIEW_legendary9.png and a copy to the
outputs dir for daily approval.
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
OUTDIR = "/sessions/awesome-pensive-allen/mnt/outputs"

# (title, source-tier token, preview-dir, legendary-suffix, swatch)
SETS = [
    ("Tidewarden Sovereign (Warrior)", "rare1", "_warrior_legendary9_preview", "_rare9", (24, 152, 160)),
    ("Celestial Magus (Mage)", "mage4", "_mage_legendary9_preview", "_rare_mage9", (222, 218, 224)),
    ("Sunspear Warden (Ranger)", "ranger4", "_ranger_legendary9_preview", "_rare_ranger9", (234, 190, 44)),
]


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def font(sz, bold=True):
    p = f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def avatar(gender, srctier, prevdir, suffix, legendary):
    suf = "_f" if gender == "f" else ""
    g = "f" if gender == "f" else "m"
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame0(f"{CH}/skin_{g}1.png"))
    base.alpha_composite(frame0(f"{CH}/hair_{g}1.png"))
    for slot in LAYERS:
        if legendary:
            path = f"{prevdir}/{slot}{suffix}{suf}.png"
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
    title_h = 34
    label_h = 20
    row_w = pad + 4 * (cell_w + pad)
    row_h = title_h + label_h + cell_h + pad
    W = row_w
    H = 46 + len(SETS) * row_h + pad
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    fT = font(20); fL = font(13); fH = font(22)
    d.text((pad, 12), "TaskQuest — 9th Legendary Sets  (2026-07-25, awaiting approval)", font=fH, fill=(240, 240, 250))

    labels = ["M source", "M NEW", "F source", "F NEW"]
    y = 46
    for title, srctier, prevdir, suffix, sw in SETS:
        d.rectangle([pad // 2, y, W - pad // 2, y + row_h - pad // 2], fill=PANEL)
        d.rectangle([pad, y + 8, pad + 18, y + 26], fill=sw + (255,))
        d.text((pad + 26, y + 8), title, font=fT, fill=(235, 235, 245))
        cx = pad
        cy = y + title_h
        avs = [
            avatar("m", srctier, prevdir, suffix, False),
            avatar("m", srctier, prevdir, suffix, True),
            avatar("f", srctier, prevdir, suffix, False),
            avatar("f", srctier, prevdir, suffix, True),
        ]
        for i, av in enumerate(avs):
            img.alpha_composite(av, (cx, cy + label_h))
            col = (255, 220, 120) if "NEW" in labels[i] else (150, 150, 165)
            d.text((cx + 4, cy), labels[i], font=fL, fill=col)
            cx += cell_w + pad
        y += row_h

    img.convert("RGB").save("_PREVIEW_legendary9.png")
    os.makedirs(OUTDIR, exist_ok=True)
    img.convert("RGB").save(os.path.join(OUTDIR, "PREVIEW_legendary9.png"))
    print("wrote _PREVIEW_legendary9.png and outputs/PREVIEW_legendary9.png", img.size)


if __name__ == "__main__":
    main()
