#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-EIGHTH net-new-geometry axis batch
(SEME family - the plate is POWDERED with studs and the law is about the ARROWS BETWEEN THEM).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 64th's claim could not be seen because an eye cannot take an exclusive-or, so its evidence became
a DECODE. The 66th's claim was a negative and a negative has no picture, so its evidence became a
DISASSEMBLY. The 67th's claim was a sentence, so its evidence became a READING. This axis's claim is
that NOTHING ON THE PLATE REPEATS - a claim about a set of relations none of which is drawn - so its
evidence is the arrows themselves and the histogram they make:

  _ZOOM_seme_arrows.png   One real plate per class at 14x, every stud ringed and the relation that
                          ATTAINS the class's ceiling drawn in. The warrior has no such relation to
                          draw - every one of its 28 arrows occurs exactly once, which is the whole
                          of its law - so its panel shows the plate with nothing joined, and that
                          absence is the ornament.

  _ZOOM_seme_grid.png     THE SAME CUIRASS FOUR TIMES: as shipped, then GRID (which is the 13th
                          STUDWORK drawn by this axis's own painter), RANDOM and LOOSE. Same pixel,
                          same relief, same palette, the same number of studs. Three of them are
                          false. If they cannot be told apart by eye, that is the finding.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
from collections import Counter

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_seme_axis68 as G                                   # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new SEME %s (the plate is POWDERED with one-pixel STUDS and the law is not about the "
        "studs, it is about the DISPLACEMENTS BETWEEN THEM: no relation between two studs occurs "
        "more than LAMBDA times, and some relation occurs exactly LAMBDA times. FIRST AXIS WHOSE "
        "LAW IS A REFUSAL TO REPEAT - an ornament is a thing that repeats and this one repeats "
        "nothing. It is the EXACT NEGATION of the 13th STUDWORK, where every displacement is the "
        "same; control GRID is the 13th drawn by this painter to prove the two cannot be told "
        "apart by looking. The acceptance test is the first reader in 68 axes whose input is NOT A "
        "PICTURE: it forms the multiset of arrows, throws the positions away, and rebuilds the "
        "plate from the arrows alone. Class identity is a CEILING ON REPETITION - warrior 1, "
        "ranger 2, mage 3 - and the assignment is upside down because LAMBDA=1 needs two studs "
        "while LAMBDA=3 needs a four-stud chain. See _ZOOM_seme_arrows.png and _ZOOM_seme_grid.png)"
        ", 68th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_seme_legendary_preview", out="_PREVIEW_seme_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary68", "Warlord's Unrepeating Cuirass"),
              ("mage", "shirt_mage_legendary68", "Archmage's Strewn Mantle"),
              ("ranger", "shirt_ranger_legendary68", "Warden's Powdered Jerkin")],
    ),
    "legs": dict(
        prev="_seme_legs_preview", out="_PREVIEW_seme_legs.png",
        note=NOTE % ("CHAUSSES - and note that the PIECE IS THE GARMENT: a stud on the left leg and "
                     "a stud on the right stand in a relation, and that relation is on the plate",
                     "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary68", "Warlord's Unrepeating Chausses"),
              ("mage", "pants_mage_legendary68", "Archmage's Strewn Leggings"),
              ("ranger", "pants_ranger_legendary68", "Warden's Powdered Chausses")],
    ),
    "boots": dict(
        prev="_seme_boots_preview", out="_PREVIEW_seme_boots.png",
        note=NOTE % ("SABATONS - AND THE SLOT THAT DECIDED THE CLASS ASSIGNMENT. A warrior sabaton "
                     "in mid-jump is TWELVE PIXELS in a 5x4 box; it will hold two studs and nothing "
                     "else, and two studs are exactly what LAMBDA=1 needs. The 67th's boots went "
                     "silent because its law had a minimum; this axis's strictest law has a "
                     "minimum of TWO and the boots of all three classes speak",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary68", "Warlord's Unrepeating Sabatons"),
              ("mage", "boots_mage_legendary68", "Archmage's Strewn Striders"),
              ("ranger", "boots_ranger_legendary68", "Warden's Powdered Boots")],
    ),
    "helmet": dict(
        prev="_semedome_helmet_preview", out="_PREVIEW_semedome_helmet.png",
        note=NOTE % ("HELM - the black eye and mouth slits are the finishing pass, untouched; where "
                     "a slit lands on a stud the stud is simply gone, and the survival diagnostic "
                     "reports it (87% on the female warrior helm, 98-100% everywhere else)",
                     "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary68", "Warlord's Unrepeating Helm"),
              ("mage", "helmet_mage_legendary68", "Archmage's Strewn Crown"),
              ("ranger", "helmet_ranger_legendary68", "Warden's Powdered Hood")],
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
    pad, lab_h, title_h = 8, 18, 46
    row_w = (len(FRAMES) + 1) * cw * Z
    row_h = ch * Z + lab_h
    class_h = title_h + 2 * row_h
    canvas = Image.new("RGBA", (pad * 2 + row_w + pad, pad + len(rows) * (class_h + pad)),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fbig, fsm = font(15), font(11)
    y = pad
    for cls, stem, disp in rows:
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, LAMBDA = {G.LAM[cls]})",
               font=fbig, fill=(150, 200, 255, 255))
        wrap, line, lines = max(40, (canvas.size[0] - 2 * pad) // 6), "", []
        for w in note.split():
            if len(line) + len(w) + 1 > wrap:
                lines.append(line)
                line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        for i, ln in enumerate(lines[:2]):
            d.text((pad, y + 18 + i * 13), ln, font=fsm, fill=(150, 160, 175, 255))
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


def _zoom(cells, cw, chh, out, caption=None):
    pad = 10
    nlines = len(caption.split('\n')) if caption else 0
    extra = 16 * nlines + 8 if caption else 0
    wide = max(len(ln) for ln in caption.split('\n')) * 8 + 2 * pad if caption else 0
    canvas = Image.new("RGBA", (max(pad + len(cells) * (cw + pad), wide),
                                pad + chh + 22 + extra), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in cells:
        canvas.alpha_composite(im if im.size == (cw, chh) else im.resize((cw, chh), Image.NEAREST),
                               (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += cw + pad
    if caption:
        yy = pad + chh + 20
        for line in caption.split('\n'):
            d.text((pad, yy), line, font=font(13), fill=(150, 200, 255, 255))
            yy += 16
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def _plate(cls, mode=None, fi=0, kind="chest", suffix=""):
    """One real plate, built through the generator, BEFORE the finishing pass."""
    cfg = G.SLOTS[kind]
    base = G.load_any('%s%s.png' % (cfg['srcs'][cls], suffix))
    for f, sl, a in G.frames_of(base):
        if f != fi:
            continue
        fr, pts, box = G.one_plate(base, sl, a, cfg, cls, f, (), mode)
        return fr, pts, box
    return None, None, None


def build_chest_zoom():
    cells = []
    crop = (28, 18, 56, 50)
    Z = 10
    for c in ("warrior", "mage", "ranger"):
        im = frame(_open(f"_seme_legendary_preview/shirt_{c}_legendary68.png"), 0).crop(crop)
        cells.append((im, f"{c} chest idle f0  (LAMBDA = {G.LAM[c]})"))
    _zoom(cells, (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z, "_ZOOM_seme_chest.png",
          caption="A STUD IS ONE PIXEL OF CREST AND ITS WITNESS IS ONE DARK 4-NEIGHBOUR. Not a\n"
                  "domino (the 67th's boss is a domino) because the whole of this axis is POSITIONS\n"
                  "and a domino has two of them - which pixel would the arrow start at? Same two\n"
                  "pixels of relief, and the arrow has an endpoint. No two studs come within\n"
                  "Chebyshev 2: through the finishing pass a diagonal pair reads as one short bar.")


def build_head_zoom():
    cells = []
    crop = (30, 14, 52, 36)
    Z = 12
    for c in ("warrior", "mage", "ranger"):
        im = frame(_open(f"_semedome_helmet_preview/helmet_{c}_legendary68.png"), 0).crop(crop)
        cells.append((im, f"{c} helm f0 (LAMBDA = {G.LAM[c]})"))
    _zoom(cells, (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z, "_ZOOM_seme_head.png",
          caption="THE ORNAMENT HAS NO UP AND NO ORIGIN. There is no pitch, no phase, no register,\n"
                  "no direction anywhere in this law - slide the whole powdering across the dome or\n"
                  "turn it through a half-turn and the arrows are the same arrows (controls SLIDE\n"
                  "and TURN, 840 of 840 plates lawful). The 67th was blind to where a boss sat\n"
                  "inside its register; this one is blind to WHERE, full stop.")


def build_arrows_zoom():
    """THE AXIS'S REAL EVIDENCE: the studs ringed and the relation that attains the ceiling drawn."""
    Z = 14
    cells, lines = [], []
    for cls in ("warrior", "ranger", "mage"):
        fr, pts, box = _plate(cls)
        crop = (box.x0 - 1, box.y0 - 1, box.x0 + box.w + 1, box.y0 + box.h + 1)
        cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
        im = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST).convert("RGBA")
        d = ImageDraw.Draw(im)

        def px(p):
            y, x = box.to_frame(p[0], p[1])
            return ((x - crop[0]) * Z + Z // 2, (y - crop[1]) * Z + Z // 2)

        for p in pts:
            cx, cy = px(p)
            d.ellipse([cx - Z // 2 - 2, cy - Z // 2 - 2, cx + Z // 2 + 2, cy + Z // 2 + 2],
                      outline=(255, 210, 90, 255), width=2)
        bag = G.arrows(pts)
        top, mult = max(bag.items(), key=lambda kv: kv[1])
        if mult > 1:
            for i, p in enumerate(pts):
                for q in pts[i + 1:]:
                    if G.canon((q[0] - p[0], q[1] - p[1])) == top:
                        d.line([px(p), px(q)], fill=(120, 255, 160, 255), width=3)
        hist = Counter(bag.values())
        cells.append((im, "%s  LAMBDA=%d  %d studs  %d arrows"
                      % (cls, G.LAM[cls], len(pts), sum(bag.values()))))
        lines.append("   %-8s %2d studs -> %2d relations;  occurring once: %2d   twice: %2d   "
                     "three times: %2d   -> LAMBDA = %d"
                     % (cls, len(pts), sum(bag.values()), hist.get(1, 0), hist.get(2, 0),
                        hist.get(3, 0), mult))
    cw, chh = max(c[0].size[0] for c in cells), max(c[0].size[1] for c in cells)
    cells = [(im.resize((cw, chh), Image.NEAREST) if im.size != (cw, chh) else im, n)
             for im, n in cells]
    cap = ["EVERY STUD RINGED; THE RELATION THAT ATTAINS THE CEILING DRAWN IN GREEN.", ""] + lines
    cap += ["",
            "   The warrior has NOTHING TO DRAW and that is its law: every one of its relations",
            "   occurs exactly once, so no two studs anywhere on the plate stand alike. The ranger",
            "   carries one echoed relation and the mage one relation running three times - a CHAIN",
            "   of four studs in step, six pixels of span before an ornamental stud is placed, which",
            "   is why the LOOSE class is the expensive one and the STRICT class fits a sabaton.",
            "",
            "   Measured over the batch: 840 plates, 22573 arrows, spectrum histogram 1:280 2:280",
            "   3:280, and clauses RECOVERY / SPECTRUM / TIGHT / REBUILD / BLIND / LEGIBLE all 0."]
    _zoom(cells, cw, chh, "_ZOOM_seme_arrows.png", caption="\n".join(cap))


def build_grid_zoom():
    """The same cuirass, once true and three times false, at the same magnification."""
    Z = 12
    cls = "warrior"
    cells, crop = [], None
    for mode, label in ((None, "AS SHIPPED"), ("grid", "GRID (=13th STUDWORK)"),
                        ("random", "RANDOM"), ("loose", "LOOSE")):
        fr, pts, box = _plate(cls, mode)
        if not pts:
            continue
        if crop is None:
            crop = (box.x0 - 1, box.y0 - 1, box.x0 + box.w + 1, box.y0 + box.h + 1)
        L = G.lam(pts)
        ok = "LAWFUL" if L == G.LAM[cls] else "FALSE"
        cells.append((Image.fromarray(fr).crop(crop),
                      "%s  %d studs  LAMBDA=%d  %s" % (label, len(pts), L, ok)))
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    _zoom(cells, cw, chh, "_ZOOM_seme_grid.png",
          caption="Same pixel, same witness, same relief, same palette, the same eight studs.\n"
                  "GRID is the 13th STUDWORK rendered by THIS axis's painter - it is not a straw\n"
                  "man, it is a shipped axis - and its arrows are a wall: 726 of 840 plates false.\n"
                  "RANDOM is what everyone assumes this axis is, and the measured surprise is that\n"
                  "chance satisfies the STRICT class 35.7% of the time and the LOOSE class 10.0%.\n"
                  "SO THE EVIDENCE IS NOT A PLATE, IT IS THE WARDROBE: 280 warrior plates every one\n"
                  "of them lawful, where chance gives 0.357^280, about 10^-125.\n"
                  "IF YOU CANNOT TELL THESE FOUR APART BY EYE, THAT IS THE FINDING.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_arrows_zoom()
    build_grid_zoom()


if __name__ == "__main__":
    main()
