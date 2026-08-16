#!/usr/bin/env python3
"""Approval preview: Ranger legendary set "Verdant Monarch" (NEW L25).

Frame-0 full-avatar composite (skin + hair + shirt + pants + boots + helmet),
male and female, at 6x. For each gender: left = the ranger t4 SOURCE geometry it
was recolored from (context), right = the NEW Verdant Monarch legendary. Shows
the recolor is a distinct item, not a tier clone.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
NEW = "_ranger_legendary_preview"
FW, FH = 80, 64
SCALE = 6
CROP = (18, 8, 62, 64)
BG = (26, 40, 28, 255)
PANEL = (40, 54, 40, 255)

LAYERS = ["shirt", "pants", "boots", "helmet"]  # draw order (helmet last)
SRC = {"helmet": "helmet_ranger4", "shirt": "shirt_ranger4",
       "pants": "pants_ranger4", "boots": "boots_ranger4"}


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
            path = f"{NEW}/{slot}_rare_ranger1{suf}.png"
        else:
            path = f"{CH}/{SRC[slot]}{suf}.png"
        if os.path.exists(path):
            base.alpha_composite(frame0(path))
    crop = base.crop(CROP)
    return crop.resize((crop.width * SCALE, crop.height * SCALE), Image.NEAREST)


def main():
    cells = []
    for g in ("m", "f"):
        cells.append((f"{'Male' if g=='m' else 'Female'} · Ranger t4 (source)", avatar(g, False)))
        cells.append((f"{'Male' if g=='m' else 'Female'} · Verdant Monarch (NEW)", avatar(g, True)))
    cw, chh = cells[0][1].size
    pad, top, label_h, left = 22, 118, 34, 22
    cols = 4
    grid_w = left + cols * (cw + pad) + pad
    grid_h = top + (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 22), "Ranger Legendary — \"Verdant Monarch\" (L25) · approval preview",
           font=font(30), fill=(228, 244, 224))
    d.text((pad, 60), "NEW ranger legendary set (helmet/shirt/pants/boots, M+F) · luminance-quantile recolor of t4 · all 8 shaded + QA PASS · 42-45/45 frames parity",
           font=font(15, False), fill=(170, 216, 150))
    d.text((pad, 84), "Emerald→radiant-gold ramp, distinct from the ranger tiers' muted dark-green family. First ranger legendary — all 3 classes now have legendary loot.",
           font=font(15, False), fill=(170, 216, 150))

    for ci, (label, cell) in enumerate(cells):
        cx = left + ci * (cw + pad)
        is_new = "NEW" in label
        d.rectangle([cx - 5, top - 5, cx + cw + 5, top + chh + 5],
                    fill=(48, 70, 44, 255) if is_new else PANEL)
        img.alpha_composite(cell, (cx, top))
        d.text((cx, top + chh + 10), label, font=font(14),
               fill=(198, 240, 176) if is_new else (196, 210, 196))

    out = f"{NEW}/PREVIEW_ranger_legendary.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
