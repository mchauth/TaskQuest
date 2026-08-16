#!/usr/bin/env python3
"""Approval preview: female legendary HELMETS (helmet_rare1/2/3_f) — the last
unregistered piece of the female legendary sets. Shirt/pants/boots _f already
ship in LOOT_TABLE; the female helm sprites exist + pass QA but aren't wired in.

Frame-0 full-body composite: skin + rare shirt + rare pants + rare boots + rare
helm, per set. Top row = committed male legendary set (visual reference); bottom
row = female set with the freshly-verified female helm.
"""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH = 80, 64
SCALE = 7
CROP = (24, 6, 56, 62)   # full body head->feet
BG = (58, 62, 78, 255)
PANEL = (40, 43, 55, 255)

SETS = {1: ("Crimson Sentinel", "#FF1818 / gold"),
        2: ("Shadow Warden", "near-black / teal"),
        3: ("Solar Paladin", "gold / ivory")}


def frame0(path):
    return Image.open(path).convert("RGBA").crop((0, 0, FW, FH))


def load_font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def cell(gender, setn):
    suf = "_f" if gender == "f" else ""
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame0(f"{CH}/skin_{'f' if gender=='f' else 'm'}1.png"))
    for layer in (f"shirt_rare{setn}{suf}", f"pants_rare{setn}{suf}",
                  f"boots_rare{setn}{suf}", f"helmet_rare{setn}{suf}"):
        p = f"{CH}/{layer}.png"
        if os.path.exists(p):
            base.alpha_composite(frame0(p))
    crop = base.crop(CROP)
    cw, chh = crop.size
    return crop.resize((cw * SCALE, chh * SCALE), Image.NEAREST)


def main():
    cols = [1, 2, 3]
    rows = [("m", "MALE (ref)"), ("f", "FEMALE (new helm)")]
    sample = cell("m", 1)
    cw, chh = sample.size
    pad, top, label_h, left = 18, 116, 44, 150
    grid_w = left + len(cols) * (cw + pad) + pad
    grid_h = top + len(rows) * (chh + label_h + pad) + pad
    img = Image.new("RGBA", (grid_w, grid_h), BG)
    d = ImageDraw.Draw(img)
    ftitle, fhdr, flbl, fsub = load_font(32), load_font(20), load_font(19), load_font(15)

    d.text((pad, 16), "TaskQuest — Female Legendary Helmets (L25 sets)",
           font=ftitle, fill=(240, 240, 250, 255))
    d.text((pad, 56),
           "Completes the female legendary sets: shirt/pants/boots already ship; helm sprites pass QA",
           font=fsub, fill=(180, 184, 200, 255))
    d.text((pad, 78),
           "42/42 active frames match male  |  presence-mismatch 0  |  preview only — needs LOOT_TABLE registration, not pushed",
           font=fsub, fill=(180, 184, 200, 255))

    for ci, setn in enumerate(cols):
        cx = left + ci * (cw + pad) + pad
        d.text((cx, top - 30), f"{SETS[setn][0]}", font=fsub, fill=(255, 210, 120, 255))
        d.text((cx, top - 12), f"L25  {SETS[setn][1]}", font=fsub, fill=(150, 154, 172, 255))

    for ri, (g, glabel) in enumerate(rows):
        ry = top + ri * (chh + label_h + pad)
        d.text((pad, ry + chh // 2 - 12), glabel, font=fhdr, fill=(230, 230, 240, 255))
        for ci, setn in enumerate(cols):
            cx = left + ci * (cw + pad) + pad
            d.rectangle([cx - 4, ry - 4, cx + cw + 4, ry + chh + 4], fill=PANEL)
            img.alpha_composite(cell(g, setn), (cx, ry))
            if ri == 1:
                d.text((cx, ry + chh + 8), f"{SETS[setn][0]} Helm", font=flbl,
                       fill=(225, 225, 235, 255))

    os.makedirs("_fem_rare_helmet_preview", exist_ok=True)
    out = "_fem_rare_helmet_preview/PREVIEW_female_rare_helmets.png"
    img.convert("RGB").save(out)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
