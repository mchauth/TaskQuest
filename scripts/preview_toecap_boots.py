#!/usr/bin/env python3
"""Preview the horizontal buckle-strap boots (8th boots axis) for daily approval.
For each class and gender: full avatar (skin + base pants + base shirt + strap
boots + hair) across idle/walk/run/cheer/slash, plus one isolated boots-over-skin
so the net-new horizontal buckle-strap geometry is clear. Writes to $OUTP (default
_PREVIEW_toecap_boots.png)."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_toecap_boots_preview"
FW, FH, COLS = 80, 64, 10
OUT = os.environ.get("OUTP", "_PREVIEW_toecap_boots.png")
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]
CLASSES = [
    ("warrior", "boots_warrior_legendary_toecap", "Ironshod Warboots"),
    ("mage", "boots_mage_legendary_toecap", "Astral Toecap Striders"),
    ("ranger", "boots_ranger_legendary_toecap", "Wildshod Striders"),
]


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def _open(path):
    return Image.open(path).convert("RGBA")


def avatar(stem, gender, fi, hair=True, dress=True):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(_open(f"{CH}/skin_{g}1.png"), fi))
    if dress:
        base.alpha_composite(frame(_open(f"{CH}/leather_pants_1{suf}.png"), fi))
    base.alpha_composite(frame(_open(f"{PREV}/{stem}{suf}.png"), fi))  # boots over pants
    if dress:
        base.alpha_composite(frame(_open(f"{CH}/leather_armor_1{suf}.png"), fi))
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
    H = pad + len(CLASSES) * (class_h + pad)
    canvas = Image.new("RGBA", (W, H), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fbig, fsm = font(16), font(11)
    y = pad
    for cls, stem, disp in CLASSES:
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE boots — net-new steel TOE-CAP, 9th boots axis (repaint, QA-safe))",
               font=fbig, fill=(255, 224, 130, 255))
        yy = y + title_h
        for gender in ("m", "f"):
            x = pad
            for fi, nm in FRAMES:
                cell = avatar(stem, gender, fi).resize((cw * Z, ch * Z), Image.NEAREST)
                canvas.alpha_composite(cell, (x, yy))
                d.text((x + 2, yy + ch * Z), f"{gender} {nm}", font=fsm, fill=(200, 200, 210, 255))
                x += cw * Z
            iso = avatar(stem, gender, 0, hair=False, dress=False).resize((cw * Z, ch * Z), Image.NEAREST)
            canvas.alpha_composite(iso, (x, yy))
            d.text((x + 2, yy + ch * Z), f"{gender} iso (boots+skin)", font=fsm, fill=(200, 200, 210, 255))
            yy += row_h
        y += class_h + pad
    canvas.convert("RGB").save(OUT)
    print("wrote", OUT, canvas.size)


if __name__ == "__main__":
    main()
