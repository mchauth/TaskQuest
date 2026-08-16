#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-FOURTH net-new-geometry axis batch
(TALLY family — a mosaic of raised and sunken tesserae whose arrangement is a CODEWORD: the
exclusive-or of the numbers of the raised studs is zero, and if you turn one stud over that
exclusive-or becomes the NUMBER OF THE STUD YOU TURNED).

*** THE DELIVERABLE, AND WHY IT HAS AN EXTRA PANEL AGAIN. ***
The 62nd could not be judged on one sheet and its evidence became a dressed character. The 63rd
could not be judged on one picture and its evidence became a filmstrip and a GIF. This one CAN be
judged on one picture — every stud of the code is right there — but not by an eye, because an eye
cannot take an exclusive-or. So the four slot grids show what the player gets (a hammered,
close-worked metal that reads as expensive at 13px) and the fifth panel shows what the player
does not get and the reader does:

  _ZOOM_tally_decode.png    THE AXIS CAUGHT WORKING — a pristine cuirass beside four copies of
                            itself, each with exactly ONE tessera turned over. Under each copy is
                            the number the plate itself reports, and ringed on each copy is the
                            stud that number points at. The ring is drawn from the SYNDROME, never
                            from the knowledge of which stud was broken, and it lands on the broken
                            stud every time.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_tally_axis64 as G                                  # noqa: E402
from sprite_finish import finish_array                        # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new TALLY %s (a mosaic of RAISED and SUNKEN 2x2 tesserae whose arrangement is a "
        "CODEWORD: the exclusive-or of the numbers of the raised studs is zero, and five or six "
        "studs of the plate are spent making it so. FIRST AXIS THAT CAN BE WRONG AND KNOW IT — "
        "turn one stud over and the plate reports the NUMBER of the stud you turned; see "
        "_ZOOM_tally_decode.png), 64th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_tally_legendary_preview", out="_PREVIEW_tally_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary64", "Warlord's Tallied Cuirass"),
              ("mage", "shirt_mage_legendary64", "Archmage's Reckoning Mantle"),
              ("ranger", "shirt_ranger_legendary64", "Warden's Tallystone Jerkin")],
    ),
    "legs": dict(
        prev="_tally_legs_preview", out="_PREVIEW_tally_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary64", "Warlord's Tallied Chausses"),
              ("mage", "pants_mage_legendary64", "Archmage's Reckoning Leggings"),
              ("ranger", "pants_ranger_legendary64", "Warden's Tallystone Chausses")],
    ),
    "boots": dict(
        prev="_tally_boots_preview", out="_PREVIEW_tally_boots.png",
        note=NOTE % ("SABATONS — the two feet are ONE plate, because a single sabaton holds six "
                     "tesserae and a code on six studs is four parts check to two parts message. "
                     "Turn over a stud on the left boot and some of the studs that name it are on "
                     "the right one: THE REDUNDANCY IS NON-LOCAL", "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_tally", "Warlord's Tallied Sabatons"),
              ("mage", "boots_mage_legendary_tally", "Archmage's Reckoning Striders"),
              ("ranger", "boots_ranger_legendary_tally", "Warden's Tallystone Boots")],
    ),
    "helmet": dict(
        prev="_tallydome_helmet_preview", out="_PREVIEW_tallydome_helmet.png",
        note=NOTE % ("HELM — the dome carries the longest code in the set (up to 64 studs on the "
                     "mage hat, seven of them check)", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary64", "Warlord's Tallied Helm"),
              ("mage", "helmet_mage_legendary64", "Archmage's Reckoning Crown"),
              ("ranger", "helmet_ranger_legendary64", "Warden's Tallystone Hood")],
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
    """The three cuirasses at pixel scale. What to look for is the SURFACE: every tessera has a
    highlight on one corner and a shadow on the opposite one, so the plate reads as close-worked
    hammered metal rather than as a printed pattern — and the arrangement is irregular because it is
    a message, not a repeat."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_tally_legendary_preview/shirt_{c}_legendary64.png"), 0).crop(crop),
              f"{c} chest idle f0") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_tally_chest.png",
          caption="the diagonal is the whole vocabulary: light upper-left = a boss, light "
                  "lower-right = a pit. Half of every tessera is plain mid metal, which is where "
                  "the class colour lives.")


def build_head_zoom():
    """The head zone. The visor's black eye and mouth slits must survive a plate covered in
    tesserae, which is why no stop in the palette goes near black (the 49th's lesson)."""
    crop = (28, 14, 56, 42)
    cells = [(frame(_open(f"_tallydome_helmet_preview/helmet_{c}_legendary64.png"), 0).crop(crop),
              f"{c} helm idle f0") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_tally_head.png",
          caption="darkest stops are channel-sum 200 / 212 / 194 — the visor slits are the only "
                  "near-black on the sheet and read cleanly through the stud field.")


def build_decode_panel(out="_ZOOM_tally_decode.png", zoom=14):
    """*** THE EVIDENCE. ***

    A pristine warrior cuirass, then four copies of it with ONE tessera turned over in each. Under
    each copy is the number the plate reports about itself — the exclusive-or of the numbers of its
    raised studs, which is zero when nothing is wrong — and the ring is drawn AT THAT NUMBER'S
    ADDRESS, computed from the syndrome alone and never from any record of which stud was broken.

    It lands on the broken stud, four times out of four, and it would land on it for any of the
    twenty-six."""
    cls = "warrior"
    cfg = G.SLOTS["chest"]
    base = G.load_any("%s.png" % cfg["srcs"][cls])
    stem = cfg["dst"] % cls
    stops = G.TALPAL[cls]
    src = base[:FH, :FW]
    a = src[..., 3] > 0

    fr0 = np.zeros_like(src)
    G.recolor(src, fr0, a, *G.BODY[cls])
    comps, bits = G.build_frame(fr0, a, True, stops, stem)
    flat = [c for _, cells in comps for c in cells]
    n = len(bits)

    picks = [p for p in (3, 9, 16, 22) if 1 <= p <= n]
    crop = (28, 20, 56, 48)
    x0, y0, x1, y1 = crop
    w, h = x1 - x0, y1 - y0

    panels = [(fr0[y0:y1, x0:x1].copy(), None, 0, "pristine")]
    for i in picks:
        b2 = list(bits)
        b2[i - 1] ^= 1
        fr2 = np.zeros_like(src)
        G.recolor(src, fr2, a, *G.BODY[cls])
        G.paint_cells(fr2, comps, b2, stops)
        rb = G.read_cells(fr2, comps, stops)
        ok, loc, _ = G.decode(rb)
        syn = G.xor_syndrome(rb)
        # THE RING IS PLACED FROM THE SYNDROME. `loc` is what the plate said; nothing here consults
        # `i`, and the label prints both so the reader can see that they agree.
        _, _, _, cy, cx = flat[loc - 1]
        panels.append((fr2[y0:y1, x0:x1].copy(), (cy - y0, cx - x0), syn,
                       "turned stud %d -> plate says %d" % (i, loc)))

    pad, lab = 12, 46
    canvas = Image.new("RGBA", (pad + len(panels) * (w * zoom + pad), pad + h * zoom + lab + 30),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    for k, (arr, ring, syn, label) in enumerate(panels):
        px = pad + k * (w * zoom + pad)
        canvas.alpha_composite(Image.fromarray(arr).resize((w * zoom, h * zoom), Image.NEAREST),
                               (px, pad))
        if ring is not None:
            ry, rx = ring
            d.rectangle([px + rx * zoom - 2, pad + ry * zoom - 2,
                         px + (rx + G.CELL_W) * zoom + 1, pad + (ry + G.CELL_H) * zoom + 1],
                        outline=(255, 90, 90, 255), width=3)
        col = (150, 255, 170, 255) if syn == 0 else (255, 170, 120, 255)
        d.text((px + 2, pad + h * zoom + 4), "syndrome = %d" % syn, font=font(15), fill=col)
        d.text((px + 2, pad + h * zoom + 24), label, font=font(12), fill=(205, 205, 215, 255))
    d.text((pad, pad + h * zoom + lab + 2),
           "THE RING IS DRAWN FROM THE SYNDROME, NOT FROM THE RECORD OF THE DAMAGE: the number "
           "under each plate is the exclusive-or of the numbers of its raised studs, and the ring "
           "is placed at that address. No table, no search.",
           font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_decode_panel()


if __name__ == "__main__":
    main()
