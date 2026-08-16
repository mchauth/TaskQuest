#!/usr/bin/env python3
"""Preview the pauldron-chest legendaries for daily approval. For each class and
gender: full avatar (skin+chest+hair) across idle/walk/run/cheer/slash, plus one
isolated chest-over-skin at high zoom so the net-new shoulder geometry is clear.
Writes to outputs."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_pauldron_legendary_preview"
FW, FH, COLS = 80, 64, 10
OUT = os.environ.get("OUTP", "PREVIEW_pauldron_legendary.png")
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]
CLASSES = [
    ("warrior", "shirt_warrior_legendary2", "Colossus Pauldrons"),
    ("mage", "shirt_mage_legendary2", "Archon's Mantle"),
    ("ranger", "shirt_ranger_legendary2", "Wildwarden's Spaulders"),
]


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def _open(path):
    return Image.open(path).convert("RGBA")


def avatar(stem, gender, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = _open(f"{CH}/skin_{g}1.png")
    hair = _open(f"{CH}/hair_{g}1.png")
    shirt = _open(f"{PREV}/{stem}{suf}.png")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(shirt, fi))
    base.alpha_composite(frame(hair, fi))
    return base.crop((10, 8, 70, 60))


def piece(stem, gender, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = _open(f"{CH}/skin_{g}1.png")
    shirt = _open(f"{PREV}/{stem}{suf}.png")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(shirt, fi))
    return base.crop((10, 8, 70, 60))


def main():
    cw, ch = 60, 52
    Z = 2                      # zoom for avatar cells
    pad = 8
    lab_h = 18
    title_h = 30
    ncols = len(FRAMES)
    row_w = (ncols + 1) * cw * Z         # frames + one isolated column
    # per class: 2 gender rows
    rows_per_class = 2
    row_h = ch * Z + lab_h
    class_h = title_h + rows_per_class * row_h
    W = pad * 2 + row_w + pad
    H = pad + len(CLASSES) * (class_h + pad)
    canvas = Image.new("RGBA", (W, H), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fbig, fsm = font(16), font(11)
    y = pad
    for cls, stem, disp in CLASSES:
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE chest — net-new shoulder geometry)",
               font=fbig, fill=(255, 224, 130, 255))
        yy = y + title_h
        for gender in ("m", "f"):
            x = pad
            for fi, name in FRAMES:
                cell = avatar(stem, gender, fi).resize((cw * Z, ch * Z), Image.NEAREST)
                canvas.alpha_composite(cell, (x, yy))
                d.text((x + 2, yy + ch * Z), f"{gender} {name}", font=fsm, fill=(200, 200, 210, 255))
                x += cw * Z
            # isolated chest-over-skin (no hair), same zoom, full figure
            iso = piece(stem, gender, 0).resize((cw * Z, ch * Z), Image.NEAREST)
            canvas.alpha_composite(iso, (x, yy))
            d.text((x + 2, yy + ch * Z), f"{gender} iso (no hair)", font=fsm, fill=(200, 200, 210, 255))
            yy += row_h
        y += class_h + pad
    canvas.convert("RGB").save(OUT)
    print("wrote", OUT, canvas.size)


if __name__ == "__main__":
    main()
