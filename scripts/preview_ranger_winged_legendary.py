#!/usr/bin/env python3
"""Preview the ranger winged legendary ("Skyhunter's Wings") — full-avatar
composites (skin + hair + winged chest) across idle/walk/run/cheer/slash frames,
male and female, to show the hawk wing pose + flutter. Writes to outputs for
daily approval."""
import os
import numpy as np  # noqa: F401
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_ranger_winged_legendary_preview"
FW, FH, COLS = 80, 64, 10
OUT = os.environ.get(
    "PREVIEW_OUT",
    "/sessions/charming-eloquent-planck/mnt/outputs/PREVIEW_ranger_winged_legendary.png")
FRAMES = [(0, "idle 0"), (12, "walk 12"), (22, "run 22"),
          (41, "cheer 41"), (51, "slash 51")]


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
    shirt = Image.open(f"{PREV}/shirt_ranger_legendary1{suf}.png").convert("RGBA")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(shirt, fi))   # wings behind body (read via transparency)
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(hair, fi))
    base.alpha_composite(frame(shirt, fi))   # body/wing over torso
    return base.crop((2, 2, 78, 62))


def main():
    S = 6
    cw, chh = 76 * S, 60 * S
    pad = 16
    BG = (16, 24, 18, 255)
    ncols = len(FRAMES)
    W = pad + ncols * (cw + pad)
    rows = [("m", "MALE"), ("f", "FEMALE")]
    H = 62 + len(rows) * (chh + 30)
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 16),
           "CONCEPT - Skyhunter's Wings (ranger hyper-rare)  ·  net-new hawk wings"
           "  ·  staged, NOT pushed",
           font=font(19), fill=(224, 236, 200))
    y = 56
    for g, glabel in rows:
        d.text((pad, y), glabel, font=font(15), fill=(176, 206, 128))
        x = pad
        for fi, flabel in FRAMES:
            av = avatar(g, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 20))
            d.text((x + 4, y + 4), flabel, font=font(12), fill=(150, 160, 140))
            x += cw + pad
        y += chh + 30
    img.convert("RGB").save(OUT)
    # also drop a copy in the repo root for the daily-approval convention
    img.convert("RGB").save("_PREVIEW_ranger_winged_legendary.png")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
