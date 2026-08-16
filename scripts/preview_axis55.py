#!/usr/bin/env python3
"""Daily-approval preview grids for the FIFTY-FIFTH net-new-geometry axis batch
(STRATA family — LAP-JOINTED BANDS in a readable order: chest cuirass, legs chausses, boots
sabatons, helmet helm). For each class and gender: full dressed avatar across idle/walk/run/cheer/slash, plus
one isolated slot-over-skin so the net-new relation — that the bands were laid one after another in
a READABLE ORDER, each new one whole across the ones already there and each older one severed at its
edge — is clear. Emits four _PREVIEW_strata_*.png plus a chest and a head zoom at repo root. Nothing here touches
sprites/preview_assets/char or git."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new STRATA %s (broad bands lap-jointed across the piece at different angles, each new "
        "one passing OVER the ones already laid and casting a hard shadow onto them, so the pile "
        "reads back as the SEQUENCE it was built in — first axis with a TIME ORDER; nothing is "
        "woven), 55th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_strata_legendary_preview", out="_PREVIEW_strata_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary55", "Warlord's Ironlap Banded Cuirass"),
              ("mage", "shirt_mage_legendary55", "Archmage's Amethyst Lapweave Mantle"),
              ("ranger", "shirt_ranger_legendary55", "Warden's Bog-Oak Lapstrap Jerkin")],
    ),
    "legs": dict(
        prev="_strata_legs_preview", out="_PREVIEW_strata_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary55", "Warlord's Ironlap Banded Chausses"),
              ("mage", "pants_mage_legendary55", "Archmage's Amethyst Lapweave Leggings"),
              ("ranger", "pants_ranger_legendary55", "Warden's Bog-Oak Lapstrap Chausses")],
    ),
    "boots": dict(
        prev="_strata_boots_preview", out="_PREVIEW_strata_boots.png",
        note=NOTE % ("SABATONS", "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_strata", "Warlord's Ironlap Banded Sabatons"),
              ("mage", "boots_mage_legendary_strata", "Archmage's Amethyst Lapweave Striders"),
              ("ranger", "boots_ranger_legendary_strata", "Warden's Bog-Oak Lapstrap Field-Boots")],
    ),
    "helmet": dict(
        prev="_stratadome_helmet_preview", out="_PREVIEW_stratadome_helmet.png",
        note=NOTE % ("HELM", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary55", "Warlord's Ironlap Banded Helm"),
              ("mage", "helmet_mage_legendary55", "Archmage's Amethyst Lapweave Crown"),
              ("ranger", "helmet_ranger_legendary55", "Warden's Bog-Oak Lapstrap Hood-Helm")],
    ),
}


def frame(sheet, fi):
    r, c = fi // COLS, fi % COLS
    return sheet.crop((c * FW, r * FH, c * FW + FW, r * FH + FH))


def font(sz):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def _open(path):
    return Image.open(path).convert("RGBA")


def slot_path(prev, stem, suf):
    p = f"{prev}/{stem}{suf}.png"
    if os.path.exists(p):
        return p
    return f"{prev}/{stem}.png"


def avatar(kind, prev, stem, crop, gender, fi, hair=True, dress=True):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(_open(f"{CH}/skin_{g}1.png"), fi))
    if kind == "chest":
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_pants_1{suf}.png"), fi))
        base.alpha_composite(frame(_open(slot_path(prev, stem, suf)), fi))
    elif kind == "legs":
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_boots_1.png"), fi))
        base.alpha_composite(frame(_open(slot_path(prev, stem, suf)), fi))
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_armor_1{suf}.png"), fi))
    elif kind == "boots":
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_pants_1{suf}.png"), fi))
        base.alpha_composite(frame(_open(slot_path(prev, stem, suf)), fi))
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_armor_1{suf}.png"), fi))
    elif kind == "helmet":
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_pants_1{suf}.png"), fi))
            base.alpha_composite(frame(_open(f"{CH}/leather_armor_1{suf}.png"), fi))
    if hair and kind != "helmet":
        base.alpha_composite(frame(_open(f"{CH}/hair_{g}1.png"), fi))
    if kind == "helmet":
        if hair:
            base.alpha_composite(frame(_open(f"{CH}/hair_{g}1.png"), fi))
        base.alpha_composite(frame(_open(slot_path(prev, stem, suf)), fi))
    return base.crop(crop)


def build(kind, cfg):
    prev, out, note = cfg["prev"], cfg["out"], cfg["note"]
    crop, cw, ch = cfg["crop"], cfg["cw"], cfg["ch"]
    rows = cfg["rows"]
    Z = 2
    pad, lab_h, title_h = 8, 18, 30
    ncols = len(FRAMES)
    row_w = (ncols + 1) * cw * Z
    row_h = ch * Z + lab_h
    class_h = title_h + 2 * row_h
    W = pad * 2 + row_w + pad
    H = pad + len(rows) * (class_h + pad)
    canvas = Image.new("RGBA", (W, H), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fbig, fsm = font(15), font(11)
    y = pad
    for cls, stem, disp in rows:
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE — {note})",
               font=fbig, fill=(150, 200, 255, 255))
        yy = y + title_h
        for gender in ("m", "f"):
            x = pad
            for fi, nm in FRAMES:
                cell = avatar(kind, prev, stem, crop, gender, fi).resize((cw * Z, ch * Z), Image.NEAREST)
                canvas.alpha_composite(cell, (x, yy))
                d.text((x + 2, yy + ch * Z), f"{gender} {nm}", font=fsm, fill=(200, 200, 210, 255))
                x += cw * Z
            iso = avatar(kind, prev, stem, crop, gender, 0, hair=False, dress=False).resize((cw * Z, ch * Z), Image.NEAREST)
            canvas.alpha_composite(iso, (x, yy))
            d.text((x + 2, yy + ch * Z), f"{gender} iso (slot only)", font=fsm, fill=(200, 200, 210, 255))
            yy += row_h
        y += class_h + pad
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_chest_zoom():
    """Large single-frame zoom of the three banded chests, so the one thing the axis rests on is
    unmistakable at pixel scale: at every crossing ONE band runs through whole and the OTHER stops
    dead at its edge, with a hard cast shadow in between — never a blended third tone (that would be
    the 26th tartan) and never an alternation (that would be a weave). Follow the severings and the
    order the bands were laid in reads straight off the piece."""
    Z = 10
    crop = (28, 20, 56, 48)
    cells = [("_strata_legendary_preview/shirt_warrior_legendary55.png", "warrior chest idle"),
             ("_strata_legendary_preview/shirt_mage_legendary55.png", "mage chest idle"),
             ("_strata_legendary_preview/shirt_ranger_legendary55.png", "ranger chest idle")]
    cw = (crop[2] - crop[0]) * Z
    chh = (crop[3] - crop[1]) * Z
    pad = 10
    canvas = Image.new("RGBA", (pad + len(cells) * (cw + pad), pad + chh + 20), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fsm = font(12)
    x = pad
    for path, name in cells:
        fr = frame(_open(path), 0).crop(crop).resize((cw, chh), Image.NEAREST)
        canvas.alpha_composite(fr, (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=fsm, fill=(210, 210, 220, 255))
        x += cw + pad
    canvas.convert("RGB").save("_ZOOM_strata_chest.png")
    print("wrote _ZOOM_strata_chest.png", canvas.size)


def build_head_zoom():
    """Large single-frame zoom of the three banded helms over the skin head, so the visor eye/mouth
    slits and the bands lapped across the dome can both be judged at pixel scale."""
    Z = 12
    crop = (28, 14, 52, 34)
    cells = [("_stratadome_helmet_preview/helmet_warrior_legendary55.png", "warrior helm"),
             ("_stratadome_helmet_preview/helmet_mage_legendary55.png", "mage helm"),
             ("_stratadome_helmet_preview/helmet_ranger_legendary55.png", "ranger helm")]
    cw = (crop[2] - crop[0]) * Z
    chh = (crop[3] - crop[1]) * Z
    pad = 10
    canvas = Image.new("RGBA", (pad + len(cells) * (cw + pad), pad + chh + 20), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fsm = font(12)
    x = pad
    for path, name in cells:
        base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), 0))
        base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), 0))
        base.alpha_composite(frame(_open(path), 0))
        canvas.alpha_composite(base.crop(crop).resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=fsm, fill=(210, 210, 220, 255))
        x += cw + pad
    canvas.convert("RGB").save("_ZOOM_strata_head.png")
    print("wrote _ZOOM_strata_head.png", canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()


if __name__ == "__main__":
    main()
