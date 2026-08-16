#!/usr/bin/env python3
"""Preview the Divine Seraph legs — Seraph Greaves (pants) + Seraph Sabatons
(winged boots). Two panels per gender: (1) the FULL Seraph avatar
(skin+greaves+sabatons+winged chest+hair) so the pieces read as a set, and
(2) greaves-over-skin and sabatons-over-skin isolated at high zoom so the
net-new feather geometry is obvious. Writes to outputs for daily approval."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_seraph_legs_preview"
FW, FH, COLS = 80, 64, 10
OUT = "/sessions/beautiful-compassionate-bardeen/mnt/outputs/PREVIEW_seraph_legs.png"
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def _open(path):
    return Image.open(path).convert("RGBA")


def full_avatar(gender, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = _open(f"{CH}/skin_{g}1.png")
    hair = _open(f"{CH}/hair_{g}1.png")
    pants = _open(f"{PREV}/pants_warrior_legendary1{suf}.png")
    boots = _open(f"{PREV}/boots_warrior_legendary1{suf}.png")
    # winged chest already staged in its own preview dir
    shirt = _open(f"_winged_legendary_preview/shirt_warrior_legendary1{suf}.png")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(shirt, fi))    # wings behind body
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(pants, fi))    # z2
    base.alpha_composite(frame(boots, fi))    # z3
    base.alpha_composite(frame(shirt, fi))    # z4 (body/wings over torso)
    base.alpha_composite(frame(hair, fi))     # z6
    return base.crop((2, 2, 78, 62))


def piece_only(gender, stem, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = _open(f"{CH}/skin_{g}1.png")
    piece = _open(f"{PREV}/{stem}{suf}.png")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(piece, fi))
    return base.crop((2, 2, 78, 62))


def main():
    S = 6
    cw = 76 * S
    pad = 16
    BG = (22, 24, 36, 255)
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    rows = [("m", "MALE"), ("f", "FEMALE")]

    ncols = len(FRAMES)
    # width driven by the full-avatar row (5 frames)
    W = pad + ncols * (cw + pad)
    chh = 60 * S
    # layout: title, then per gender: full-avatar row + isolated (greaves/sabatons) row
    row_h = chh + 30
    H = 70 + len(rows) * (2 * row_h + 24)
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 14),
           "Divine Seraph legs — Greaves (pants) + Sabatons (winged boots)  ·  warrior hyper-rare  ·  net-new geometry  ·  STAGED, not pushed",
           font=font(18), fill=(240, 240, 250))
    d.text((pad, 40),
           "Row A: full Seraph avatar (chest+greaves+sabatons).   Row B: greaves-only & sabatons-only over skin (zoom on the new feathers).",
           font=font(13), fill=(150, 152, 170))
    y = 70
    for g, glabel in rows:
        d.text((pad, y), glabel + " — Row A: full set", font=font(14), fill=(255, 220, 120))
        x = pad
        for fi, flabel in FRAMES:
            av = full_avatar(g, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 20))
            d.text((x + 4, y + 4), flabel, font=font(12), fill=(150, 150, 165))
            x += cw + pad
        y += row_h + 6
        d.text((pad, y), glabel + " — Row B: greaves-only / sabatons-only", font=font(14), fill=(255, 220, 120))
        x = pad
        combos = [("pants_warrior_legendary1", 0, "greaves idle"),
                  ("pants_warrior_legendary1", 22, "greaves run"),
                  ("boots_warrior_legendary1", 0, "sabatons idle"),
                  ("boots_warrior_legendary1", 22, "sabatons run"),
                  ("boots_warrior_legendary1", 41, "sabatons cheer")]
        for stem, fi, flabel in combos:
            av = piece_only(g, stem, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 20))
            d.text((x + 4, y + 4), flabel, font=font(12), fill=(150, 150, 165))
            x += cw + pad
        y += row_h + 24
    img.convert("RGB").save(OUT)
    # also drop a copy into the repo working tree alongside the other _PREVIEW_*
    img.convert("RGB").save("_PREVIEW_seraph_legs.png")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
