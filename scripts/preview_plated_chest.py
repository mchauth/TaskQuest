#!/usr/bin/env python3
"""Preview the plated-chest prototype (leather base + sculptural iron plate) for
approval. Warrior, both genders, across idle/walk/run/cheer/slash + an isolated
chest-over-skin, for each of the 3 plate variants. Writes _PREVIEW_plated_chest.png."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_plated_chest_preview"
FW, FH, COLS = 80, 64, 10
OUT = os.environ.get("OUTP", "_PREVIEW_plated_chest.png")
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]
VARIANTS = [
    ("shirt_warrior_plated1", "Ironheart Cuirass  (domed boss)"),
    ("shirt_warrior_plated2", "Warden's Muscled Cuirass  (anatomical)"),
    ("shirt_warrior_plated3", "Lamellar Warplate  (stacked lames)"),
]


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def _open(path):
    return Image.open(path).convert("RGBA")


def avatar(stem, gender, fi, hair=True):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(_open(f"{CH}/skin_{g}1.png"), fi))
    base.alpha_composite(frame(_open(f"{PREV}/{stem}{suf}.png"), fi))
    if hair:
        base.alpha_composite(frame(_open(f"{CH}/hair_{g}1.png"), fi))
    return base.crop((10, 8, 70, 60))


def main():
    cw, ch = 60, 52
    Z = 2
    pad, lab_h, title_h = 8, 18, 30
    ncols = len(FRAMES)
    row_w = (ncols + 1) * cw * Z
    row_h = ch * Z + lab_h
    class_h = title_h + 2 * row_h
    W = pad * 2 + row_w + pad
    H = pad + len(VARIANTS) * (class_h + pad)
    canvas = Image.new("RGBA", (W, H), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fbig, fsm = font(16), font(11)
    y = pad
    for stem, disp in VARIANTS:
        d.text((pad, y), f"{disp}  —  steel body + outlined breastplate + pauldron discs, gold trim (3/4-biased)",
               font=fbig, fill=(255, 224, 130, 255))
        yy = y + title_h
        for gender in ("m", "f"):
            x = pad
            for fi, nm in FRAMES:
                cell = avatar(stem, gender, fi).resize((cw * Z, ch * Z), Image.NEAREST)
                canvas.alpha_composite(cell, (x, yy))
                d.text((x + 2, yy + ch * Z), f"{gender} {nm}", font=fsm, fill=(200, 200, 210, 255))
                x += cw * Z
            iso = avatar(stem, gender, 0, hair=False).resize((cw * Z, ch * Z), Image.NEAREST)
            canvas.alpha_composite(iso, (x, yy))
            d.text((x + 2, yy + ch * Z), f"{gender} iso (no hair)", font=fsm, fill=(200, 200, 210, 255))
            yy += row_h
        y += class_h + pad
    canvas.convert("RGB").save(OUT)
    print("wrote", OUT, canvas.size)


if __name__ == "__main__":
    main()
