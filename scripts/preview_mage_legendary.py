#!/usr/bin/env python3
"""Approval preview: Mage legendary set "Astral Magus" (NEW L25).

Frame-0 full-avatar composite (skin + shirt + pants + boots + helmet), male and
female, at 6x. For each gender: left = the mage t4 SOURCE geometry it was
recolored from (context), right = the NEW Astral Magus legendary. Shows the
recolor is a distinct item, not a tier clone.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
NEW = "_mage_legendary_preview"
FW, FH = 80, 64
SCALE = 6
CROP = (18, 8, 62, 64)
BG = (30, 34, 52, 255)
PANEL = (44, 40, 66, 255)

LAYERS = ["shirt", "pants", "boots", "helmet"]  # draw order (helmet last)
SRC = {"helmet": "helmet_mage4", "shirt": "shirt_mage4",
       "pants": "pants_mage4", "boots": "boots_mage4"}


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def font(sz, bold=True):
    for p in (f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def avatar(gender, legendary):
    suf = "_f" if gender == "f" else ""
    g = "f" if gender == "f" else "m"
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame0(f"{CH}/skin_{g}1.png"))
    base.alpha_composite(frame0(f"{CH}/hair_{g}1.png"))
    for slot in LAYERS:
        if legendary:
            path = f"{NEW}/{slot}_rare_mage1{suf}.png"
        else:
            path = f"{CH}/{SRC[slot]}{suf}.png"
        if os.path.exists(path):
            base.alpha_composite(frame0(path))
    crop = base.crop(CROP)
    return crop.resize((crop.width * SCALE, crop.height * SCALE), Image.NEAREST)


def main():
    cells = []
    for g in ("m", "f"):
        cells.append((f"{'Male' if g=='m' else 'Female'} · Mage t4 (source)", avatar(g, False)))
        cells.append((f"{'Male' if g=='m' else 'Female'} · Astral Magus (NEW)", avatar(g, True)))
    cw, chh = cells[0][1].size
    pad, top, label_h, left = 22, 118, 34, 22
    cols = 4
    grid_w = left + cols * (cw + pad) + pad
    grid_h = top + (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 22), "Mage Legendary — \"Astral Magus\" (L25) · approval preview",
           font=font(30), fill=(232, 240, 250))
    d.text((pad, 60), "NEW mage legendary set (helmet/shirt/pants/boots, M+F) · luminance-quantile recolor of t4 · all 8 shaded + QA PASS · 42-45/45 frames parity",
           font=font(15, False), fill=(150, 210, 225))
    d.text((pad, 84), "Cyan→starlight ramp, distinct from the mage tiers' purple family.",
           font=font(15, False), fill=(150, 210, 225))

    for ci, (label, cell) in enumerate(cells):
        cx = left + ci * (cw + pad)
        is_new = "NEW" in label
        d.rectangle([cx - 5, top - 5, cx + cw + 5, top + chh + 5],
                    fill=(50, 66, 78, 255) if is_new else PANEL)
        img.alpha_composite(cell, (cx, top))
        d.text((cx, top + chh + 10), label, font=font(14),
               fill=(180, 235, 245) if is_new else (200, 196, 214))

    out = f"{NEW}/PREVIEW_mage_legendary.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
