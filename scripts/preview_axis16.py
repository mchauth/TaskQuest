#!/usr/bin/env python3
"""Daily-approval preview grids for the SIXTEENTH net-new-geometry axis batch
(HERRINGBONE / TWILL family: chest twill cuirass, legs twill chausses, boots twill
sabatons, helmet twill dome). For each class and gender: full dressed avatar across
idle/walk/run/cheer/slash, plus one isolated slot-over-skin so the net-new geometry is
clear. Emits four _PREVIEW_*.png at repo root. Nothing here touches
sprites/preview_assets/char or git."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

SETS = {
    "chest": dict(
        prev="_twill_legendary_preview", out="_PREVIEW_twill_legendary.png",
        note="net-new TWILL CUIRASS (herringbone weave over cuirass), 16th chest axis (repaint, QA-safe)",
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary16", "Warlord's Twillforged Cuirass"),
              ("mage", "shirt_mage_legendary16", "Astral Herringweave Robe"),
              ("ranger", "shirt_ranger_legendary16", "Warden's Twill Jerkin")],
    ),
    "legs": dict(
        prev="_twill_legs_preview", out="_PREVIEW_twill_legs.png",
        note="net-new TWILL CHAUSSES (herringbone on thighs), 16th legs axis (repaint, QA-safe)",
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary16", "Warlord's Twill Chausses"),
              ("mage", "pants_mage_legendary16", "Astral Herringweave Leggings"),
              ("ranger", "pants_ranger_legendary16", "Warden's Twill Greaves")],
    ),
    "boots": dict(
        prev="_twill_boots_preview", out="_PREVIEW_twill_boots.png",
        note="net-new TWILL SABATONS (herringbone over boot), 16th boots axis (repaint, QA-safe)",
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_twill", "Warlord's Twill Sabatons"),
              ("mage", "boots_mage_legendary_twill", "Astral Herringweave Striders"),
              ("ranger", "boots_ranger_legendary_twill", "Warden's Twill Field-Boots")],
    ),
    "helmet": dict(
        prev="_twilldome_helmet_preview", out="_PREVIEW_twilldome_helmet.png",
        note="net-new TWILL DOME (herringbone over whole crown), 16th helmet axis (repaint, QA-safe)",
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary16", "Warlord's Twillforged Sallet"),
              ("mage", "helmet_mage_legendary16", "Astral Herringweave Circlet"),
              ("ranger", "helmet_ranger_legendary16", "Warden's Twill Hood-Helm")],
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
               font=fbig, fill=(255, 224, 130, 255))
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


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)


if __name__ == "__main__":
    main()
