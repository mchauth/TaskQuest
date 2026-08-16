#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-SIXTH net-new-geometry axis batch
(DOVETAIL family — the plate is cut into stones, and the stones are cut so that the plate cannot be
taken apart).

*** THE DELIVERABLE, AND WHY IT HAS AN EXTRA PANEL. ***
The 64th could be judged on one picture but not by an eye, because an eye cannot take an
exclusive-or, so its evidence became a DECODE. The 65th's claim was about what made the pixels, so
its evidence became a DERIVATION and a DIVERGENCE. This axis's claim is a negative — that nothing
can be carried away — and a negative has no picture at all. So the evidence is the ATTEMPT:

  _ZOOM_dovetail_disassembly.png   One real cuirass twice. On the left, the plate as shipped, with
                                   the largest part that could come away picked out — and there is
                                   none, so nothing is picked out. On the right, THE SAME PLATE WITH
                                   ITS KEYS STRUCK OUT (plain courses, the 17th ASHLAR), with the
                                   part that now comes away DRAGGED OUT OF THE PLATE in the
                                   direction it leaves. Same stones, same silhouette, same palette;
                                   one holds and one does not, and the difference is three pixels
                                   per joint.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_dovetail_axis66 as G                               # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new DOVETAIL %s (the plate is cut into STONES and the stones are keyed into each other "
        "so that NO PART OF THE PLATE CAN BE CARRIED AWAY IN ANY DIRECTION. FIRST AXIS WHOSE "
        "INVARIANT IS AN IMPOSSIBILITY - every predecessor says the plate IS something; this one "
        "says a set is EMPTY. The acceptance test is a DISASSEMBLY: it takes hold of every one of "
        "the 2^n-2 ways of parting the plate, in each of four directions, and pulls, and every "
        "attempt fails. Class identity is the SHAPE OF THE KEY TREE - warrior CHAIN, mage RADIAL, "
        "ranger COMB - recovered from the pixels by a reader never told the class. See "
        "_ZOOM_dovetail_disassembly.png), 66th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_dovetail_legendary_preview", out="_PREVIEW_dovetail_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary66", "Warlord's Keystone Cuirass"),
              ("mage", "shirt_mage_legendary66", "Archmage's Seized Mantle"),
              ("ranger", "shirt_ranger_legendary66", "Warden's Locked Jerkin")],
    ),
    "legs": dict(
        prev="_dovetail_legs_preview", out="_PREVIEW_dovetail_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary66", "Warlord's Keystone Chausses"),
              ("mage", "pants_mage_legendary66", "Archmage's Seized Leggings"),
              ("ranger", "pants_ranger_legendary66", "Warden's Locked Chausses")],
    ),
    "boots": dict(
        prev="_dovetail_boots_preview", out="_PREVIEW_dovetail_boots.png",
        note=NOTE % ("SABATONS - AND THE AXIS'S OWN LIMIT, STATED: a sabaton is fourteen pixels of "
                     "ragged diagonal and a dovetail is four pixels across in each direction, so "
                     "THE JOINT DOES NOT FIT. The boots are cut as ONE UNCUT STONE, which is this "
                     "axis's own GLUE control worn as an item - reported, never faked",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_dovetail", "Warlord's Keystone Sabatons"),
              ("mage", "boots_mage_legendary_dovetail", "Archmage's Seized Striders"),
              ("ranger", "boots_ranger_legendary_dovetail", "Warden's Locked Boots")],
    ),
    "helmet": dict(
        prev="_dovetaildome_helmet_preview", out="_PREVIEW_dovetaildome_helmet.png",
        note=NOTE % ("HELM - the dome is the slot with the most stones and the clearest joints",
                     "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary66", "Warlord's Keystone Helm"),
              ("mage", "helmet_mage_legendary66", "Archmage's Seized Crown"),
              ("ranger", "helmet_ranger_legendary66", "Warden's Locked Hood")],
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
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE - {note})",
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
    extra = 44 if caption else 0
    canvas = Image.new("RGBA", (pad + len(cells) * (cw + pad), pad + chh + 22 + extra),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in cells:
        canvas.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += cw + pad
    if caption:
        yy = pad + chh + 20
        for line in caption.split('\n'):
            d.text((pad, yy), line, font=font(13), fill=(150, 200, 255, 255))
            yy += 16
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_chest_zoom():
    crop = (28, 18, 56, 50)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        im = frame(_open(f"_dovetail_legendary_preview/shirt_{c}_legendary66.png"), 0).crop(crop)
        cells.append((im, f"{c} chest idle f0  ({G.TREE[c]} tree)"))
    _zoom(cells, crop, 10, "_ZOOM_dovetail_chest.png",
          caption="each stone is lit on its top and right and shadowed below and left, so the seams\n"
                  "read as hard grooves. Where a seam JOGS by a pixel, that is a key: a tail two\n"
                  "pixels deep and two wide at its far end, which cannot come back out of its throat.")


def build_head_zoom():
    crop = (28, 14, 54, 40)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        im = frame(_open(f"_dovetaildome_helmet_preview/helmet_{c}_legendary66.png"), 0).crop(crop)
        cells.append((im, f"{c} helm idle f0"))
    _zoom(cells, crop, 11, "_ZOOM_dovetail_head.png",
          caption="the dome carries the most stones of any slot. The visor's black eye and mouth\n"
                  "pixels survive: no stop in any of the three stone palettes goes near black.")


def _plate(cls, mode=None):
    """One real cuirass, rebuilt so the panel can show the stones and the keys."""
    base = G.load_any('%s.png' % G.SLOTS['chest']['srcs'][cls])
    a = base[:FH, :FW][..., 3] > 0
    fr = np.zeros((FH, FW, 4), dtype=base.dtype)
    D, M, L = G.BODY[cls]
    G.recolor(base[:FH, :FW], fr, a, D, M, L)
    comp = G.comps_of(a, True)[0]
    got = G.build_component(fr, comp, cls, mode)
    return fr, comp, got


def build_disassembly():
    """THE AXIS'S REAL EVIDENCE: the same plate keyed and unkeyed, and the part that walks off."""
    cls = 'warrior'
    fr, comp, got = _plate(cls)
    if got is None:
        print('no jointed plate on frame 0; skipping disassembly panel')
        return
    g, lab0, lab, keys, _s = got
    crop = (28, 18, 56, 50)
    held = Image.fromarray(fr).crop(crop)

    # the same stones with every key struck out — plain courses, the 17th ASHLAR
    fr2 = np.zeros_like(fr)
    a = comp
    base = G.load_any('%s.png' % G.SLOTS['chest']['srcs'][cls])
    D, M, L = G.BODY[cls]
    G.recolor(base[:FH, :FW], fr2, base[:FH, :FW][..., 3] > 0, D, M, L)
    G.paint(fr2, lab0, G.PAL[cls])
    plain = Image.fromarray(fr2).crop(crop)

    # find a part that now comes away, and drag it out
    freed, direction = None, None
    for name, dy, dx in G.DIRS:
        ids, E = G.blocking(lab0, dy, dx)
        f = G.free_subsets(ids, E, brute=len(ids) <= G.BRUTE_MAX)
        if f:
            freed, direction = min(f, key=len), (name, dy, dx)
            break
    dragged = plain
    if freed:
        fr3 = fr2.copy()
        name, dy, dx = direction
        moving = np.isin(lab0, list(freed))
        keep = fr3.copy()
        for y, x in np.argwhere(moving):
            keep[y, x, :] = 0
        for y, x in np.argwhere(moving):
            ny, nx = y + dy * 4, x + dx * 4
            if 0 <= ny < FH and 0 <= nx < FW:
                keep[ny, nx] = fr3[y, x]
        dragged = Image.fromarray(keep).crop(crop)

    cells = [(held, 'as shipped: keyed  (nothing comes away)'),
             (plain, 'keys struck out: plain courses'),
             (dragged, 'and %d stone(s) walk off %s' % (len(freed or []),
                                                        direction[0] if direction else '-'))]
    _zoom(cells, crop, 10, "_ZOOM_dovetail_disassembly.png",
          caption="THE SAME STONES, THE SAME SILHOUETTE, THE SAME PALETTE. The only difference is\n"
                  "three pixels per joint. Left: the acceptance test pulls on all 2^n-2 partings in\n"
                  "four directions and nothing moves. Right: strike the keys out and a part leaves.")


def build_tree_zoom():
    """The three trees, drawn: every key ringed, on the stones it holds together."""
    crop = (28, 18, 56, 50)
    cells = []
    for cls in ('warrior', 'mage', 'ranger'):
        fr, comp, got = _plate(cls)
        if got is None:
            continue
        g, lab0, lab, keys, _s = got
        im = Image.fromarray(fr).crop(crop).resize(((crop[2] - crop[0]) * 10,
                                                    (crop[3] - crop[1]) * 10), Image.NEAREST)
        d = ImageDraw.Draw(im)
        for (gr, gc, vertical) in keys:
            moved, _w, _n, _t = G.key_pixels(g, gr, gc, vertical)
            ys = [p[0] for p in moved]
            xs = [p[1] for p in moved]
            y0 = (min(ys) - crop[1]) * 10
            x0 = (min(xs) - crop[0]) * 10
            y1 = (max(ys) - crop[1] + 1) * 10
            x1 = (max(xs) - crop[0] + 1) * 10
            d.rectangle([x0 - 2, y0 - 2, x1 + 1, y1 + 1], outline=(255, 90, 90, 255), width=2)
        cells.append((im, '%s: %s tree, %d keys' % (cls, G.TREE[cls], len(keys))))
    if not cells:
        return
    pad = 10
    w = pad + sum(im.size[0] + pad for im, _ in cells)
    h = pad + max(im.size[1] for im, _ in cells) + 82
    canvas = Image.new("RGBA", (w, h), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in cells:
        canvas.alpha_composite(im, (x, pad))
        d.text((x + 2, pad + im.size[1] + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += im.size[0] + pad
    yy = pad + max(im.size[1] for im, _ in cells) + 20
    for line in ("every key ringed. The keys are the edges of a graph on the stones and the plate is",
                 "seized exactly when that graph is connected, so the ornament is a SPANNING TREE and",
                 "costs n-1 keys - the provable minimum. Which tree it is, is which class it is."):
        d.text((pad, yy), line, font=font(13), fill=(150, 200, 255, 255))
        yy += 16
    canvas.convert("RGB").save("_ZOOM_dovetail_tree.png")
    print("wrote _ZOOM_dovetail_tree.png", canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_tree_zoom()
    build_disassembly()


if __name__ == "__main__":
    main()
