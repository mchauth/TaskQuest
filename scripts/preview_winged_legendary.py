#!/usr/bin/env python3
"""Preview the winged legendary (Divine Seraph Plate) — full-avatar composites
(skin+hair+winged shirt) across idle/walk/run frames, male and female, to show
the wing pose + flutter across the animation. Writes to outputs for approval."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_winged_legendary_preview"
FW, FH, COLS = 80, 64, 10
OUT = "/sessions/ecstatic-eager-cray/mnt/outputs/PREVIEW_winged_legendary.png"
FRAMES = [(0, "idle 0"), (12, "walk 12"), (22, "run 22"), (41, "cheer 41")]


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def avatar(gender, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = Image.open(f"{CH}/skin_{g}1.png").convert("RGBA")
    hair = Image.open(f"{CH}/hair_{g}1.png").convert("RGBA")
    shirt = Image.open(f"{PREV}/shirt_warrior_legendary1{suf}.png").convert("RGBA")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(shirt, fi))   # wings behind body read via transparency
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(hair, fi))
    base.alpha_composite(frame(shirt, fi))   # body/wing over torso
    return base.crop((2, 2, 78, 62))


def main():
    S = 6
    cw, chh = (76) * S, (60) * S
    pad = 16
    BG = (22, 24, 36, 255)
    ncols = len(FRAMES)
    W = pad + ncols * (cw + pad)
    rows = [("m", "MALE"), ("f", "FEMALE")]
    H = 60 + len(rows) * (chh + 30)
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 16), "CONCEPT — Divine Seraph Plate (warrior hyper-rare)  ·  wings + halo  ·  staged, NOT pushed",
           font=font(19), fill=(240, 240, 250))
    y = 56
    for g, glabel in rows:
        d.text((pad, y), glabel, font=font(15), fill=(255, 220, 120))
        x = pad
        for fi, flabel in FRAMES:
            av = avatar(g, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 20))
            d.text((x + 4, y + 4), flabel, font=font(12), fill=(150, 150, 165))
            x += cw + pad
        y += chh + 30
    img.convert("RGB").save(OUT)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
