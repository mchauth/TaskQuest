#!/usr/bin/env python3
"""Daily-approval preview grids for the FIFTY-EIGHTH net-new-geometry axis batch
(VORTICE family — COUNTER-HANDED WHORLS: chest cuirass, legs chausses, boots sabatons, helmet helm). For each class and gender: full dressed avatar across idle/walk/run/cheer/slash, plus
one isolated slot-over-skin so the net-new relation — that every whorl is BENT and so has a
HAND, and that no two whorls sharing an edge of the lattice ever turn the same way — is clear.
Emits four _PREVIEW_vortice_*.png plus a chest, a head and a hands zoom at repo root. Nothing here touches
sprites/preview_assets/char or git."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new VORTICE %s (a field of small pinwheels, every arm ending in a hook that TURNS, so "
        "every whorl has a HAND — and two whorls sharing an edge of the lattice never turn the same "
        "way, anywhere on the piece; both hands are the SAME METAL, so the only thing telling them "
        "apart is form — FIRST AXIS WHOSE ELEMENT IS CHIRAL, i.e. the first whose motif cannot be "
        "brought back onto itself by turning the piece in your hands), 58th %s axis (repaint, "
        "QA-safe)")

SETS = {
    "chest": dict(
        prev="_vortice_legendary_preview", out="_PREVIEW_vortice_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary58", "Warlord's Copperwhorl Vortice Cuirass"),
              ("mage", "shirt_mage_legendary58", "Archmage's Jadewhorl Vortice Mantle"),
              ("ranger", "shirt_ranger_legendary58", "Warden's Pewterwhorl Vortice Jerkin")],
    ),
    "legs": dict(
        prev="_vortice_legs_preview", out="_PREVIEW_vortice_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary58", "Warlord's Copperwhorl Vortice Chausses"),
              ("mage", "pants_mage_legendary58", "Archmage's Jadewhorl Vortice Leggings"),
              ("ranger", "pants_ranger_legendary58", "Warden's Pewterwhorl Vortice Chausses")],
    ),
    "boots": dict(
        prev="_vortice_boots_preview", out="_PREVIEW_vortice_boots.png",
        note=NOTE % ("SABATONS", "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_vortice", "Warlord's Copperwhorl Vortice Sabatons"),
              ("mage", "boots_mage_legendary_vortice", "Archmage's Jadewhorl Vortice Striders"),
              ("ranger", "boots_ranger_legendary_vortice", "Warden's Pewterwhorl Vortice Field-Boots")],
    ),
    "helmet": dict(
        prev="_vorticedome_helmet_preview", out="_PREVIEW_vorticedome_helmet.png",
        note=NOTE % ("HELM", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary58", "Warlord's Copperwhorl Vortice Helm"),
              ("mage", "helmet_mage_legendary58", "Archmage's Jadewhorl Vortice Crown"),
              ("ranger", "helmet_ranger_legendary58", "Warden's Pewterwhorl Vortice Hood-Helm")],
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
    """Large single-frame zoom of the three whorled chests, so the one thing the axis rests on is
    unmistakable at pixel scale: TWO whorls side by side on one piece, the same size, the same
    metal, the same light — and turning opposite ways. Follow one arm out from a hub and watch which
    side it kicks to at the end; then do it on the whorl next to it. Hold the image up to a mirror
    and neither whorl becomes the other; the pair becomes the pair again, with the two swapped. That
    exchange, and not the pinwheel, is what makes this axis new."""
    Z = 10
    crop = (28, 20, 56, 48)
    cells = [("_vortice_legendary_preview/shirt_warrior_legendary58.png", "warrior chest idle"),
             ("_vortice_legendary_preview/shirt_mage_legendary58.png", "mage chest idle"),
             ("_vortice_legendary_preview/shirt_ranger_legendary58.png", "ranger chest idle")]
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
    canvas.convert("RGB").save("_ZOOM_vortice_chest.png")
    print("wrote _ZOOM_vortice_chest.png", canvas.size)


def build_head_zoom():
    """Large single-frame zoom of the three whorled helms over the skin head, so the visor eye and
    mouth slits and the whorls set into the dome can both be judged at pixel scale. A dome is the
    hardest slot for this axis for the opposite reason to the 57th's: a helmet is the one piece of
    armour a viewer reads as a FACE, and a face has a left and a right, so a hooked whorl on a brow
    is competing with the strongest handed shape on the sprite. The thing to check is that the visor
    still reads as a visor and the hooks still read as hooks."""
    Z = 12
    crop = (28, 14, 52, 34)
    cells = [("_vorticedome_helmet_preview/helmet_warrior_legendary58.png", "warrior helm"),
             ("_vorticedome_helmet_preview/helmet_mage_legendary58.png", "mage helm"),
             ("_vorticedome_helmet_preview/helmet_ranger_legendary58.png", "ranger helm")]
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
    canvas.convert("RGB").save("_ZOOM_vortice_head.png")
    print("wrote _ZOOM_vortice_head.png", canvas.size)


def build_hands_zoom():
    """CLAUSE 1, DRAWN. The left five cells are the right-handed whorl and its four quarter-turns;
    the last cell is its MIRROR. The whole axis is the claim that the last cell is not one of the
    first four — that no amount of turning the piece brings the mirror back — and this panel is that
    claim at a size where it can be checked by eye in about two seconds. Follow the hook at the end
    of the arm pointing east: in every one of the four rotations it kicks the same way round the
    hub; in the mirror it kicks the other way.

    This is also the panel to look at when judging whether the axis SURVIVES at 13px, because it is
    the only place in the batch where the two objects being distinguished are shown at the same
    scale and the same orientation, side by side, with nothing else on the plate."""
    import sys as _sys
    _sys.path.insert(0, "scripts")
    import numpy as np
    import gen_vortice_axis58 as G

    Z = 26
    box = 7                                     # 5x5 whorl with one cell of enamel all round
    labels = ["right hand", "turned 90", "turned 180", "turned 270", "MIRROR (not any of them)"]
    cells = dict(G.gauge_cells("std"))
    forms = []
    c = dict(cells)
    for _ in range(4):
        forms.append(dict(c))
        c = G._rot(c)
    forms.append(G._mir(cells))

    pad, lab = 12, 20
    cw = box * Z
    canvas = Image.new("RGBA", (pad + len(forms) * (cw + pad),
                                pad + 3 * (cw + lab) + pad), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fsm, fbig = font(13), font(15)
    for ri, cls in enumerate(("warrior", "mage", "ranger")):
        stops = G.VORTICE[cls]
        for ci, form in enumerate(forms):
            a = np.zeros((box, box, 4), dtype=np.uint8)
            a[..., :3] = stops[G.R_FIELD]
            a[..., 3] = 255
            for (dx, dy), r in form.items():
                a[box // 2 + dy, box // 2 + dx, :3] = stops[r]
            im = Image.fromarray(a).resize((cw, cw), Image.NEAREST)
            x = pad + ci * (cw + pad)
            y = pad + ri * (cw + lab)
            canvas.alpha_composite(im, (x, y))
            if ri == 2:
                d.text((x + 2, y + cw + 2), labels[ci], font=fsm,
                       fill=((255, 190, 120, 255) if ci == 4 else (200, 200, 210, 255)))
    d.text((pad, pad + 3 * (cw + lab) - 2),
           "CLAUSE 1: the mirror is none of the four rotations — that is what it means for the "
           "motif to have a HAND, and it is checked in code by exactly these five comparisons.",
           font=fbig, fill=(150, 200, 255, 255))
    canvas.convert("RGB").save("_ZOOM_vortice_hands.png")
    print("wrote _ZOOM_vortice_hands.png", canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_hands_zoom()


if __name__ == "__main__":
    main()
