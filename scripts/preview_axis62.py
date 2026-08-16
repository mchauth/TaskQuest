#!/usr/bin/env python3
"""Daily-approval preview grids for the SIXTY-SECOND net-new-geometry axis batch
(DATUM family — ONE oblique rib lattice laid across the whole suit from an origin that is not on
the armour but on the WEARER: the crown of the skull, taken per frame from the skin sheet).

Emits four _PREVIEW_datum_*.png plus a chest zoom, a head zoom, and TWO panels that are this
axis's real evidence — because this is the first axis in the set that CANNOT be judged from a
single sheet:

  _ZOOM_datum_suit.png      THE AXIS DRAWN — a DRESSED character, all four slots at once, beside
                            the same character under the SELF-ANCHORED control (which is what all
                            sixty-one prior axes do). Follow one rib down from the shoulder: under
                            the axis it crosses the chest/hip seam and the hip/boot seam without
                            stepping; under the control it breaks at every seam. On any ONE sheet
                            the two are indistinguishable, which is the whole point.
  _ZOOM_datum_controls.png  THE CLAUSES DRAWN — the same dressed warrior under the axis and each
                            of the five controls, with the clauses each one fails.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new DATUM %s (ONE oblique rib lattice laid across the WHOLE SUIT from the crown of "
        "the wearer's skull; FIRST AXIS WHOSE ORIGIN IS OUTSIDE THE PIECE — the boot cannot say "
        "where its ribs go without asking where the head is, and the ribs cross the seams "
        "unbroken), 62nd %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_datum_legendary_preview", out="_PREVIEW_datum_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary62", "Warlord's Pewter Meridian Cuirass"),
              ("mage", "shirt_mage_legendary62", "Archmage's Cobalt Meridian Mantle"),
              ("ranger", "shirt_ranger_legendary62", "Warden's Mosswrought Meridian Jerkin")],
    ),
    "legs": dict(
        prev="_datum_legs_preview", out="_PREVIEW_datum_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary62", "Warlord's Pewter Meridian Chausses"),
              ("mage", "pants_mage_legendary62", "Archmage's Cobalt Meridian Leggings"),
              ("ranger", "pants_ranger_legendary62", "Warden's Mosswrought Meridian Chausses")],
    ),
    "boots": dict(
        prev="_datum_boots_preview", out="_PREVIEW_datum_boots.png",
        note=NOTE % ("SABATONS — a sabaton is six rows tall and gets whatever part of the lattice "
                     "happens to fall on it: a crest, or only shade, and nothing is done about it, "
                     "because doing something about it is exactly the SELF-ANCHORED control",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_datum", "Warlord's Pewter Meridian Sabatons"),
              ("mage", "boots_mage_legendary_datum", "Archmage's Cobalt Meridian Striders"),
              ("ranger", "boots_ranger_legendary_datum", "Warden's Mosswrought Meridian Boots")],
    ),
    "helmet": dict(
        prev="_datumdome_helmet_preview", out="_PREVIEW_datumdome_helmet.png",
        note=NOTE % ("HELM — the helm sits closest to the datum, so its ribs are the ones to check "
                     "against the shoulders", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary62", "Warlord's Pewter Meridian Helm"),
              ("mage", "helmet_mage_legendary62", "Archmage's Cobalt Meridian Crown"),
              ("ranger", "helmet_ranger_legendary62", "Warden's Mosswrought Meridian Hood")],
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
    return p if os.path.exists(p) else f"{prev}/{stem}.png"


def avatar(kind, prev, stem, crop, gender, fi, hair=True, dress=True):
    g = "f" if gender == "f" else "m"
    suf = "_f" if gender == "f" else ""
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(_open(f"{CH}/skin_{g}1.png"), fi))
    if kind == "chest":
        if dress:
            base.alpha_composite(frame(_open(f"{CH}/leather_pants_1{suf}.png"), fi))
        base.alpha_composite(frame(_open(slot_path(prev, stem, suf)), fi))
    elif kind in ("legs", "boots"):
        if dress and kind == "legs":
            base.alpha_composite(frame(_open(f"{CH}/leather_boots_1.png"), fi))
        if dress and kind == "boots":
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
    row_w = (len(FRAMES) + 1) * cw * Z
    row_h = ch * Z + lab_h
    class_h = title_h + 2 * row_h
    canvas = Image.new("RGBA", (pad * 2 + row_w + pad, pad + len(rows) * (class_h + pad)),
                       (24, 24, 30, 255))
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
                cell = avatar(kind, prev, stem, crop, gender, fi).resize((cw * Z, ch * Z),
                                                                        Image.NEAREST)
                canvas.alpha_composite(cell, (x, yy))
                d.text((x + 2, yy + ch * Z), f"{gender} {nm}", font=fsm, fill=(200, 200, 210, 255))
                x += cw * Z
            iso = avatar(kind, prev, stem, crop, gender, 0, hair=False,
                         dress=False).resize((cw * Z, ch * Z), Image.NEAREST)
            canvas.alpha_composite(iso, (x, yy))
            d.text((x + 2, yy + ch * Z), f"{gender} iso (slot only)", font=fsm,
                   fill=(200, 200, 210, 255))
            yy += row_h
        y += class_h + pad
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def _zoom(cells, crop, Z, out, caption=None):
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad = 10
    extra = 26 if caption else 0
    canvas = Image.new("RGBA", (pad + len(cells) * (cw + pad), pad + chh + 20 + extra),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in cells:
        canvas.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += cw + pad
    if caption:
        d.text((pad, pad + chh + 20), caption, font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_chest_zoom():
    """The three meridian cuirasses at pixel scale. What to look for: one family of straight
    oblique ribs, each a bright crest sitting directly on its own cast shadow, dropping one pixel
    every two columns toward the LEFT (the character faces left). The ribs are the plainest
    ornament in the set on purpose — a registration can only be seen if the thing registered is
    simple enough to follow across a seam."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_datum_legendary_preview/shirt_{c}_legendary62.png"), 0).crop(crop),
              f"{c} chest idle") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_datum_chest.png")


def build_head_zoom():
    """The three meridian helms over the skin head. The helm is the piece nearest the datum, so a
    rib on the dome and a rib on the shoulder are the strictest test of the registration by eye.
    Check the visor still reads: no stop in this palette is near black (darkest channel-sums
    270 / 244 / 210), which is what leaves the finishing pass somewhere dark to put the slits."""
    crop = (28, 14, 52, 34)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), 0))
        base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), 0))
        base.alpha_composite(frame(_open(f"_datumdome_helmet_preview/helmet_{c}_legendary62.png"),
                                   0))
        cells.append((base.crop(crop), f"{c} helm"))
    _zoom(cells, crop, 12, "_ZOOM_datum_head.png")


# --------------------------------------------------------------------------------------------
def _G():
    sys.path.insert(0, "scripts")
    import numpy as np
    import gen_datum_axis62 as G
    return G, np


def _dressed(cls, gender, fi, mode=None):
    G, np = _G()
    arr = G.dress(cls, gender, (fi,), mode=mode)[0]
    return Image.fromarray(arr)


def build_suit_zoom():
    """THE AXIS DRAWN, and the panel this batch should be judged on.

    Left of each pair: the character wearing all four slots of this axis. Right: the same four
    slots regenerated under the SELF-ANCHORED control — every piece its own origin, which is what
    all sixty-one prior axes do and what any single sheet of this axis is indistinguishable from.

    Follow ONE rib down from the shoulder. Under the axis it leaves the bottom of the cuirass and
    arrives at the top of the thigh on the same line, and leaves the thigh and arrives at the boot
    on the same line, because all four sheets asked the same body the same question. Under the
    control every seam is a step. Neither picture can be told from the other one piece at a time.
    """
    crop = (24, 12, 60, 63)
    Z = 11
    pad = 10
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    classes = ("warrior", "mage", "ranger")
    canvas = Image.new("RGBA", (pad + 6 * (cw + pad), pad + chh + 60), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for cls in classes:
        for mode, lab in ((None, "DATUM"), ("self-anchored", "SELF-ANCHORED")):
            im = _dressed(cls, "m", 0, mode).crop(crop).resize((cw, chh), Image.NEAREST)
            canvas.alpha_composite(im, (x, pad))
            d.text((x + 2, pad + chh + 2), f"{cls} {lab}", font=font(12),
                   fill=(150, 230, 170, 255) if mode is None else (255, 175, 160, 255))
            x += cw + pad
    d.text((pad, pad + chh + 22),
           "follow one rib from the shoulder down: under DATUM it crosses the chest/hip and "
           "hip/boot seams unbroken; under SELF-ANCHORED it steps at every seam.",
           font=font(13), fill=(150, 200, 255, 255))
    d.text((pad, pad + chh + 40),
           "the two are indistinguishable on any single sheet — which is exactly what this axis "
           "is for, and why its preview is a dressed character and not a garment.",
           font=font(13), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save("_ZOOM_datum_suit.png")
    print("wrote _ZOOM_datum_suit.png", canvas.size)


def build_controls_zoom():
    """THE CLAUSES DRAWN — the dressed warrior under the axis and each of the five controls, with
    the clauses each fails underneath, measured by the same reader on its own lattice.

    SELF-ANCHORED is the cell to stare at: it is what every prior axis does. FRAME-ANCHORED is the
    honest near miss in the other direction — it registers perfectly across the seams and its ribs
    stand still while the character walks through them, which is the reason the datum is a body
    landmark and not the canvas corner.
    """
    G, np = _G()
    modes = [(None, "DATUM (axis)")] + [(m, m.upper()) for m in G.CONTROLS]
    crop = (24, 12, 60, 63)
    Z = 9
    pad = 10
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cw = max(cw, 230)
    canvas = Image.new("RGBA", (pad + len(modes) * (cw + pad), pad + chh + 80), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for mode, label in modes:
        im = _dressed("warrior", "m", 0, mode).crop(crop).resize((cw, chh), Image.NEAREST)
        canvas.alpha_composite(im, (x, pad))
        r = G._clauses_for(mode)
        fails = []
        if r["disagree"]:
            fails.append("SEAMLESS %d/%d" % (r["disagree"], r["nframes"]))
        if r["ext"] >= G.EXT_MAX:
            fails.append("EXTERNAL %.2f" % r["ext"])
        if len(r["body"]) != 1:
            fails.append("BODY-TRACKING")
        if len(r["lattices"]) != 1:
            fails.append("ONE LATTICE")
        elif not all(a != 0 and b != 0 for a, b, _ in r["lattices"]):
            fails.append("not OBLIQUE")
        d.text((x + 2, pad + chh + 2), label, font=font(12), fill=(210, 210, 220, 255))
        d.text((x + 2, pad + chh + 18), "PASS" if not fails else "fails " + ", ".join(fails),
               font=font(11), fill=(140, 230, 150, 255) if not fails else (255, 150, 150, 255))
        x += cw + pad
    d.text((pad, pad + chh + 44),
           "SELF-ANCHORED is what all sixty-one prior axes do. FRAME-ANCHORED registers across the "
           "seams and crawls under the walk cycle instead.",
           font=font(13), fill=(150, 200, 255, 255))
    d.text((pad, pad + chh + 62),
           "HORIZONTAL is registered too — and a level line crossing a seam would have lined up by "
           "accident, which is why the ribs are oblique.",
           font=font(13), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save("_ZOOM_datum_controls.png")
    print("wrote _ZOOM_datum_controls.png", canvas.size)


if __name__ == "__main__":
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_suit_zoom()
    build_controls_zoom()
