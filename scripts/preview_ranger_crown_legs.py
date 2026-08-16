#!/usr/bin/env python3
"""Preview the ranger net-new-geometry set: Skyhunter's Plumed Hood (helmet) +
Pelt-Tassets (pants) + Talon Striders (boots), which complete the ranger 4-slot
showcase alongside the staged Skyhunter's Wings chest. Row A: full Skyhunter
avatar (hood+wings+tassets+striders+hair). Row B: hood-only / tassets-only /
striders-only over skin at high zoom so the net-new hawk geometry is obvious.
Writes to outputs for daily approval (NOT pushed)."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
CROWN = "_ranger_crown_legendary_preview"
LEGS = "_ranger_legs_legendary_preview"
CHEST = "_ranger_winged_legendary_preview"
FW, FH, COLS = 80, 64, 10
OUT = os.environ.get("OUT", "_PREVIEW_ranger_crown_legs.png")
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
    helm = _open(f"{CROWN}/helmet_ranger_legendary1{suf}.png")
    pants = _open(f"{LEGS}/pants_ranger_legendary1{suf}.png")
    boots = _open(f"{LEGS}/boots_ranger_legendary1{suf}.png")
    shirt = _open(f"{CHEST}/shirt_ranger_legendary1{suf}.png")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(shirt, fi))    # wings behind body
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(pants, fi))
    base.alpha_composite(frame(boots, fi))
    base.alpha_composite(frame(shirt, fi))    # body/wings over torso
    base.alpha_composite(frame(hair, fi))
    base.alpha_composite(frame(helm, fi))     # hood over hair
    return base.crop((2, 2, 78, 62))


def piece_only(gender, folder, stem, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = _open(f"{CH}/skin_{g}1.png")
    piece = _open(f"{folder}/{stem}{suf}.png")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(piece, fi))
    return base.crop((2, 2, 78, 62))


def main():
    S = 6
    cw = 76 * S
    pad = 16
    BG = (18, 30, 20, 255)
    rows = [("m", "MALE"), ("f", "FEMALE")]
    ncols = len(FRAMES)
    W = pad + ncols * (cw + pad)
    chh = 60 * S
    row_h = chh + 30
    H = 70 + len(rows) * (2 * row_h + 24)
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 14),
           "Skyhunter ranger set — Plumed Hood (helmet) + Pelt-Tassets (pants) + Talon Striders (boots)  ·  ranger hyper-rare  ·  net-new geometry  ·  STAGED, not pushed",
           font=font(18), fill=(224, 238, 210))
    d.text((pad, 40),
           "Row A: full Skyhunter avatar (hood+wings+tassets+striders).   Row B: hood-only / tassets-only / striders-only over skin (zoom on the new hawk-plume geometry).",
           font=font(13), fill=(150, 176, 150))
    y = 70
    for g, glabel in rows:
        d.text((pad, y), glabel + " — Row A: full set", font=font(14), fill=(190, 224, 150))
        x = pad
        for fi, flabel in FRAMES:
            av = full_avatar(g, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 20))
            d.text((x + 4, y + 4), flabel, font=font(12), fill=(150, 160, 140))
            x += cw + pad
        y += row_h + 6
        d.text((pad, y), glabel + " — Row B: hood / tassets / striders isolated", font=font(14), fill=(190, 224, 150))
        x = pad
        combos = [(CROWN, "helmet_ranger_legendary1", 0, "hood idle"),
                  (CROWN, "helmet_ranger_legendary1", 41, "hood cheer"),
                  (LEGS, "pants_ranger_legendary1", 22, "tassets run"),
                  (LEGS, "boots_ranger_legendary1", 0, "striders idle"),
                  (LEGS, "boots_ranger_legendary1", 22, "striders run")]
        for folder, stem, fi, flabel in combos:
            av = piece_only(g, folder, stem, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 20))
            d.text((x + 4, y + 4), flabel, font=font(12), fill=(150, 160, 140))
            x += cw + pad
        y += row_h + 24
    img.convert("RGB").save(OUT)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
