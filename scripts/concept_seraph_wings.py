#!/usr/bin/env python3
"""CONCEPT MOCKUP ONLY (not a shippable sheet, not pushed).

Demonstrates the sanctioned in-repo path for a hyper-rare "winged" legendary:
net-new wing + halo geometry drawn as pixels behind/around the existing gold
warrior body, composited over skin+hair. Frame-0 (south idle). Purpose: give
Matt a concrete concept to approve or redirect before committing to a full
42-frame build. Uses only Pillow + existing repo assets — no external API.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH = 80, 64
OUT = "/sessions/ecstatic-eager-cray/mnt/outputs/CONCEPT_seraph_wings.png"


def f0(name):
    return Image.open(f"{CH}/{name}.png").convert("RGBA").crop((0, 0, FW, FH))


def gold_body(src):
    """Recolor an existing warrior chest to a gold/white Divine ramp."""
    a = np.array(src)
    P = a[..., 3] > 10
    rgb = a[..., :3].astype(np.float64)
    L = (3 * rgb[..., 0] + 6 * rgb[..., 1] + rgb[..., 2]) / 10.0
    ramp = np.array([
        (60, 40, 12), (110, 78, 24), (168, 124, 40), (214, 170, 66),
        (240, 208, 110), (250, 232, 170), (255, 246, 214), (255, 255, 245),
    ], np.uint8)
    Lp = L[P]
    if Lp.size:
        q = (Lp - Lp.min()) / max(1e-6, (Lp.max() - Lp.min()))
        idx = np.clip((q * (len(ramp) - 1)).round().astype(int), 0, len(ramp) - 1)
        out = a.copy()
        out[P, :3] = ramp[idx]
        # keep dark outline pixels dark
        edge = P & (L < 40)
        out[edge, :3] = (40, 28, 10)
        return Image.fromarray(out, "RGBA")
    return src


def draw_wings(size=(FW, FH)):
    """Angelic wings spreading symmetrically behind the shoulders (south view)."""
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # feather palette light->shadow
    FE = (250, 250, 255, 255)
    F2 = (220, 224, 245, 255)
    F3 = (188, 196, 230, 255)
    OL = (150, 158, 200, 255)
    cx = 40
    shoulder_y = 30
    # each wing: 3 stacked feather rows sweeping up-and-out from the shoulder
    for sgn in (-1, 1):
        base_x = cx + sgn * 8
        # upper long feathers
        for i, (dx, dy, ln, col) in enumerate([
            (10, -10, 9, FE), (13, -6, 10, F2), (15, -1, 10, F3),
            (15, 4, 8, F3), (13, 8, 6, F2),
        ]):
            x0 = base_x + sgn * (dx - ln)
            x1 = base_x + sgn * dx
            y = shoulder_y + dy
            lo, hi = sorted((x0, x1))
            d.line([(lo, y), (hi, y)], fill=col, width=1)
            d.point((base_x + sgn * dx, y), fill=OL)  # outer tip outline
        # wing shoulder joint (bright)
        d.ellipse([base_x + sgn * 2 - 2, shoulder_y - 3, base_x + sgn * 2 + 2, shoulder_y + 3], fill=FE)
    return img


def draw_halo(size=(FW, FH)):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = 40, 15
    d.ellipse([cx - 9, cy - 3, cx + 9, cy + 3], outline=(255, 236, 150, 255), width=1)
    d.ellipse([cx - 7, cy - 2, cx + 7, cy + 2], outline=(255, 250, 210, 255), width=1)
    return img


def compose():
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(draw_wings())       # wings behind body
    base.alpha_composite(f0("skin_m1"))
    base.alpha_composite(f0("hair_m1"))
    base.alpha_composite(gold_body(f0("armor_chest_5")))
    base.alpha_composite(draw_halo())        # halo in front (above head)
    return base


def scale(im, s):
    return im.resize((im.width * s, im.height * s), Image.NEAREST)


def main():
    S = 9
    concept = compose().crop((6, 2, 74, 62))
    plain = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    plain.alpha_composite(f0("skin_m1"))
    plain.alpha_composite(f0("hair_m1"))
    plain.alpha_composite(gold_body(f0("armor_chest_5")))
    plain = plain.crop((6, 2, 74, 62))

    cw, chh = concept.width * S, concept.height * S
    pad = 20
    BG = (24, 26, 38, 255)
    W = pad * 3 + cw * 2
    H = 70 + chh + pad
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    try:
        fH = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        fL = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except Exception:
        fH = fL = ImageFont.load_default()
    d.text((pad, 16), "CONCEPT — Divine Seraph Plate (warrior hyper-rare)  ·  frame 0 south idle  ·  NOT pushed", font=fH, fill=(240, 240, 250))
    d.text((pad, 46), "gold body only", font=fL, fill=(150, 150, 165))
    d.text((pad * 2 + cw, 46), "+ wings + halo (net-new geometry)", font=fL, fill=(255, 220, 120))
    img.alpha_composite(scale(plain, S), (pad, 68))
    img.alpha_composite(scale(concept, S), (pad * 2 + cw, 68))
    img.convert("RGB").save(OUT)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
