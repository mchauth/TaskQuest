#!/usr/bin/env python3
"""Preview the winged-helm legendaries (Valkyr War-Wings / Astral Aether-Wings /
Falcon Wing-Helm) — full-avatar composites (skin+pants+shirt+hair+winged helm)
across idle/walk/run/cheer/slash, male and female, all three classes, so the
WIDE horizontal side-wing silhouette can be checked tracking the head across the
animation. Writes _PREVIEW_winghelm_legendary.png in the repo root + outputs.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
PREV = "_winghelm_legendary_preview"
FW, FH, COLS = 80, 64, 10
OUT_REPO = "_PREVIEW_winghelm_legendary.png"
OUT_SESS = "/sessions/friendly-lucid-feynman/mnt/outputs/PREVIEW_winghelm_legendary.png"
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (50, "slash")]

# class -> (body-set token, helm out name, label)
CLASSES = [
    ("warrior", "rare1", "helmet_warrior_legendary3", "WARRIOR · Valkyr War-Wings"),
    ("mage", "mage4", "helmet_mage_legendary3", "MAGE · Astral Aether-Wings"),
    ("ranger", "ranger4", "helmet_ranger_legendary3", "RANGER · Falcon Wing-Helm"),
]


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def avatar(token, helm_name, gender, fi):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    skin = Image.open(f"{CH}/skin_{g}1.png").convert("RGBA")
    hair = Image.open(f"{CH}/hair_{g}1.png").convert("RGBA")
    shirt = Image.open(f"{CH}/shirt_{token}{suf}.png").convert("RGBA")
    pants = Image.open(f"{CH}/pants_{token}{suf}.png").convert("RGBA")
    helm = Image.open(f"{PREV}/{helm_name}{suf}.png").convert("RGBA")
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(skin, fi))
    base.alpha_composite(frame(pants, fi))
    base.alpha_composite(frame(shirt, fi))
    base.alpha_composite(frame(hair, fi))
    base.alpha_composite(frame(helm, fi))     # winged helm over hair
    return base.crop((0, 2, 80, 62))          # keep full width so wings are visible


def main():
    S = 5
    cw, chh = 80 * S, 60 * S
    pad = 14
    BG = (22, 24, 36, 255)
    ncols = len(FRAMES)
    W = pad + ncols * (cw + pad)
    rows = []
    for token, helm, label in [(c[1], c[2], c[3]) for c in CLASSES]:
        rows.append((token, helm, label, "m", "MALE"))
        rows.append((token, helm, label, "f", "FEMALE"))
    H = 60 + len(rows) * (chh + 44)
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 14),
           "CONCEPT — Winged legendary helmets (all classes, hyper-rare)  ·  "
           "net-new WIDE side-wing geometry  ·  staged, NOT pushed",
           font=font(18), fill=(240, 240, 250))
    y = 52
    last_label = None
    for token, helm, label, g, glabel in rows:
        head = label if label != last_label else ""
        last_label = label
        col = (255, 220, 120) if head else (150, 150, 165)
        if head:
            d.text((pad, y), head, font=font(15), fill=col)
        d.text((pad, y + 18), glabel, font=font(12), fill=(190, 190, 205))
        x = pad
        for fi, flabel in FRAMES:
            av = avatar(token, helm, g, fi)
            av = av.resize((av.width * S, av.height * S), Image.NEAREST)
            img.alpha_composite(av, (x, y + 34))
            d.text((x + 4, y + 20), flabel, font=font(11), fill=(150, 150, 165))
            x += cw + pad
        y += chh + 44
    img.convert("RGB").save(OUT_REPO)
    try:
        img.convert("RGB").save(OUT_SESS)
    except Exception as e:
        print("session save skipped:", e)
    print("wrote", OUT_REPO, "and", OUT_SESS, img.size)


if __name__ == "__main__":
    main()
