#!/usr/bin/env python3
"""Daily-approval preview grids for the SIXTY-FIRST net-new-geometry axis batch
(CANON family — every piece divided into exactly THREE hoops in the proportions 3 : 2 : 1, each
hoop divided 1 : 1 : 2 : 1 : 1 in its own turn: chest cuirass, legs chausses, boots sabatons,
helmet helm). For each class and gender: full dressed avatar across idle/walk/run/cheer/slash, plus
one isolated slot-over-skin so the proportion is readable.

Emits four _PREVIEW_canon_*.png plus a chest zoom, a head zoom, and TWO panels that draw the
acceptance test itself:

  _ZOOM_canon_scale.png     THE AXIS DRAWN — the same ornament on plates of six, ten, fifteen,
                            twenty-two and thirty rows. There is no pitch anywhere in it; every
                            one of them is the same drawing at a different size, and the boot at
                            six rows is the canon at its irreducible minimum, one pixel to the
                            part.
  _ZOOM_canon_controls.png  THE CLAUSES DRAWN — the same warrior chest painted from the axis and
                            from each of the five controls, with the clause each one fails under
                            it. EQUAL is the cell to stare at: three equal hoops is the 12th
                            axis's banded lamellar, it is what anyone would draw first, and on a
                            six-row sabaton it differs from this axis by a single pixel.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new CANON %s (the piece is divided top to bottom into exactly THREE raised hoops in "
        "the proportions 3 : 2 : 1, and each hoop into 1 : 1 : 2 : 1 : 1 in its own turn; FIRST "
        "AXIS WHOSE INVARIANT IS A RATIO AND NOT A LENGTH — there is not one measurement in "
        "pixels anywhere in it, so the boot is the cuirass printed small), 61st %s axis "
        "(repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_canon_legendary_preview", out="_PREVIEW_canon_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary61", "Warlord's Crimson Canon Cuirass"),
              ("mage", "shirt_mage_legendary61", "Archmage's Amethyst Canon Mantle"),
              ("ranger", "shirt_ranger_legendary61", "Warden's Tidewrought Canon Jerkin")],
    ),
    "legs": dict(
        prev="_canon_legs_preview", out="_PREVIEW_canon_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary61", "Warlord's Crimson Canon Chausses"),
              ("mage", "pants_mage_legendary61", "Archmage's Amethyst Canon Leggings"),
              ("ranger", "pants_ranger_legendary61", "Warden's Tidewrought Canon Chausses")],
    ),
    "boots": dict(
        prev="_canon_boots_preview", out="_PREVIEW_canon_boots.png",
        note=NOTE % ("SABATONS — a sabaton is six rows tall and 3 : 2 : 1 is exactly six parts, so "
                     "the smallest piece in the game is this ornament at its irreducible minimum: "
                     "one pixel to the part, and not a pixel to spare", "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_canon", "Warlord's Crimson Canon Sabatons"),
              ("mage", "boots_mage_legendary_canon", "Archmage's Amethyst Canon Striders"),
              ("ranger", "boots_ranger_legendary_canon", "Warden's Tidewrought Canon Field-Boots")],
    ),
    "helmet": dict(
        prev="_canondome_helmet_preview", out="_PREVIEW_canondome_helmet.png",
        note=NOTE % ("HELM", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary61", "Warlord's Crimson Canon Helm"),
              ("mage", "helmet_mage_legendary61", "Archmage's Amethyst Canon Crown"),
              ("ranger", "helmet_ranger_legendary61", "Warden's Tidewrought Canon Hood-Helm")],
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


def _zoom(paths, crop, Z, out, caption=None):
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad = 10
    extra = 26 if caption else 0
    canvas = Image.new("RGBA", (pad + len(paths) * (cw + pad), pad + chh + 20 + extra),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in paths:
        canvas.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += cw + pad
    if caption:
        d.text((pad, pad + chh + 20), caption, font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_chest_zoom():
    """The three canon cuirasses at pixel scale. What to look for: three hoops and only three, the
    top one half the plate, the next a third, the last a sixth — and the bright crest of each hoop a
    QUARTER of that hoop, so the big hoop has a wide crest and the small one a thin one. That last
    part is the clause FIXED-CREST fails, and it is what stops the plate reading as flat panels with
    wires down them."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_canon_legendary_preview/shirt_{c}_legendary61.png"), 0).crop(crop),
              f"{c} chest idle") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_canon_chest.png")


def build_head_zoom():
    """The three canon helms over the skin head. A hooped dome is where the visor is most at risk,
    because a hoop seam and an eye slit are the same width. Check the slit still reads: no stop in
    this palette is near black (darkest channel-sums 224 / 330 / 280), which is what leaves the
    finishing pass somewhere dark to put it."""
    crop = (28, 14, 52, 34)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), 0))
        base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), 0))
        base.alpha_composite(frame(_open(f"_canondome_helmet_preview/helmet_{c}_legendary61.png"), 0))
        cells.append((base.crop(crop), f"{c} helm"))
    _zoom(cells, crop, 12, "_ZOOM_canon_head.png")


# --------------------------------------------------------------------------------------------
def _G():
    sys.path.insert(0, "scripts")
    import numpy as np
    import gen_canon_axis61 as G
    return G, np


def _chest_plate():
    """The warrior chest as a bare component, cropped to its bounding box."""
    G, np = _G()
    base = G.load_any("armor_chest_4.png")
    src = base[0:FH, 0:FW]
    a = src[..., 3] > 0
    comp = next(iter(G.comps_of(a, True)))
    ys, xs = np.nonzero(comp)
    return G, np, comp[int(ys.min()):int(ys.max()) + 1, int(xs.min()):int(xs.max()) + 1]


def build_scale_zoom():
    """THE AXIS DRAWN — the same ornament at five sizes.

    Five plates, six to thirty rows tall, all painted through the same code path with the same
    three tones and no size constant anywhere. Under each is the extent and the hoop widths the
    canon works out for it. Read left to right: nothing repeats at a fixed interval, nothing is
    ever thinner than it has to be, and the six-row plate — a sabaton — is the whole ornament at one
    pixel to the part.

    This is also the panel that shows the property no fixed-pitch axis in the set can have: the
    ornament CANNOT go too fine to see, because it has no gauge to be too fine at. On a fixed-pitch
    axis a small piece gets fewer elements and eventually one; here it gets the same three, larger
    relative to itself.
    """
    G, np = _G()
    Z = 12
    heights = (6, 10, 15, 22, 30)
    pad = 10
    plates = [G._scaled_plate(h) for h in heights]
    cw = max(p.shape[1] for p in plates) * Z
    chh = max(p.shape[0] for p in plates) * Z
    canvas = Image.new("RGBA", (pad + len(plates) * (cw + pad), pad + chh + 46), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for m in plates:
        arr = np.zeros(m.shape + (4,), dtype=np.uint8)
        info = G.paint_canon(arr, m, G.CANONPAL["warrior"])
        im = Image.fromarray(arr).resize((m.shape[1] * Z, m.shape[0] * Z), Image.NEAREST)
        canvas.alpha_composite(im, (x, pad + chh - im.height))
        d.text((x + 2, pad + chh + 2), "%d rows" % info["E"], font=font(13),
               fill=(210, 210, 220, 255))
        d.text((x + 2, pad + chh + 18), "hoops %s" % ",".join(str(w) for w in info["widths"]),
               font=font(12), fill=(150, 200, 255, 255))
        x += cw + pad
    d.text((pad, pad + chh + 32),
           "the same drawing five times — no pitch, no gauge, no pixel constant anywhere; "
           "3 : 2 : 1 is six parts and the sabaton is six rows",
           font=font(13), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save("_ZOOM_canon_scale.png")
    print("wrote _ZOOM_canon_scale.png", canvas.size)


def build_controls_zoom():
    """THE CLAUSES DRAWN — the panel to judge this batch by.

    The same warrior chest painted six times through the same code path: once from the canon and
    once from each of the five controls, with the clause each one fails written under it.

    The cell to actually look at is EQUAL. Three equal hoops is the 12th axis's BANDED LAMELLAR; it
    is what anyone would draw first; and it is a real ornament, not a straw man. What separates it
    from this axis is a proportion and nothing else — its crest centres land two and a half rows off
    on this chest, and on a six-row sabaton the difference between the two is one pixel. The second
    cell to look at is FIXED-CREST, which gets the proportion exactly right and pins the crest at
    one pixel the way every other axis in the set does: the hoops are in the right places and the
    plate has gone flat, because a hoop whose highlight does not grow with it stops being a roll.
    """
    G, np, sub = _chest_plate()
    stops = G.CANONPAL["warrior"]
    names = [(None, "CANON (this axis)", "-"),
             ("fixed-3", "FIXED-3 (axis 11)", "PARTITION"),
             ("equal", "EQUAL (axis 12)", "PLACED"),
             ("golden", "GOLDEN 1:phi:phi^2", "PLACED"),
             ("remainder", "REMAINDER", "SELF-SIMILAR"),
             ("fixed-crest", "FIXED-CREST 1px", "SELF-SIMILAR")]
    Z = 16
    pad = 10
    cw, chh = sub.shape[1] * Z, sub.shape[0] * Z
    cw = max(cw, 190)
    canvas = Image.new("RGBA", (pad + len(names) * (cw + pad), pad + chh + 62), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for mode, label, clause in names:
        arr = np.zeros(sub.shape + (4,), dtype=np.uint8)
        G.paint_canon(arr, sub, stops, mode=mode)
        runs, rows, E = G.read_hoops(arr, sub, stops)
        ok, failed, why, _ = G.accepts_component(runs, rows, E)
        im = Image.fromarray(arr).resize((cw, chh), Image.NEAREST)
        canvas.alpha_composite(im, (x, pad))
        d.text((x + 2, pad + chh + 2), label, font=font(12), fill=(210, 210, 220, 255))
        d.text((x + 2, pad + chh + 18),
               "PASS" if ok else "fails " + ", ".join(failed),
               font=font(11), fill=(140, 230, 150, 255) if ok else (255, 150, 150, 255))
        d.text((x + 2, pad + chh + 32), "%d crest runs %s" % (len(runs), [n for _, n in runs]),
               font=font(11), fill=(170, 170, 185, 255))
        x += cw + pad
    d.text((pad, pad + chh + 48),
           "EQUAL is the one to stare at: it is the 12th axis, it is what anyone draws first, and "
           "on a six-row sabaton it differs from this axis by one pixel",
           font=font(13), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save("_ZOOM_canon_controls.png")
    print("wrote _ZOOM_canon_controls.png", canvas.size)


if __name__ == "__main__":
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_scale_zoom()
    build_controls_zoom()
