#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-THIRD net-new-geometry axis batch
(SURVEY family - the ornament is a set of BEACONS and the law is that they give every pixel of the
garment AN ADDRESS OF ITS OWN).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 67th's was a sentence, so
its evidence became a READING. The 68th's was that nothing repeats, so its evidence became a
HISTOGRAM. The 69th's was that nobody drew the ornament, so its evidence was the poles ringed. The
70th's was about motion, so its evidence was the seed cycle traced. The 71st's could not be seen at
all, so its evidence was the reckoning set out in full. The 72nd's was half a fact and half a
non-event, so it took two panels of two different kinds.
THIS AXIS'S CLAIM IS ABOUT THE PART OF THE PLATE THAT CARRIES NO ORNAMENT, so for the first time in
the project THE EVIDENCE PANEL HAS TO PAINT THE PLAIN FIELD:

  _ZOOM_survey_addresses.png   One real cuirass per class at 10x with every beacon CORE ringed in
                               white, and beside it the four rules tried coarsest-first, the first
                               that resolves, and therefore the class - read off the plate and told
                               to nobody. This is the law stated.

  _ZOOM_survey_ground.png      THE SAME PLATE TWICE: at its own rule, where every pixel of the cloth
                               has an address of its own and there is nothing to mark; and ONE RULE
                               COARSER, where the pixels that have fallen into each other's
                               addresses are painted red. THE SECOND PICTURE IS CLAUSE PRECISION -
                               the first clause in the project that demands the ornament be
                               INSUFFICIENT for something - and it is the only panel in seventy-three
                               axes whose subject is the pixels between the marks.

  _ZOOM_survey_controls.png    The same cuirass four ways: as shipped, ALIGNED (the beacons put on
                               one row, which is a direction the pixel grid respects, so the
                               garment's own left-right likeness supplies collisions and 0 of 379
                               plates get through), CLIPPED (one arm pruned where the cloth would
                               have taken it - the law untouched and caught anyway, 0 of 407) and
                               SPARE (one beacon more than the law needs, which is not wrong about
                               the ground and is wrong about the plate).

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_survey_axis73 as G                                 # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

RNAME = {1: "WHOLE PIXELS ONLY", 2: "TO THE HALF PIXEL", 3: "EXACTLY, OR NOT AT ALL"}

NOTE = ("net-new SURVEY %s (the ornament is a set of BEACONS - a bright CORE with its four "
        "orthogonal ARMS, drawn wherever the cloth has room for them, and every arm that is missing "
        "is missing because there is no cloth to put it on, which the reader checks against the "
        "silhouette. The law is that the beacons give EVERY PIXEL OF THE GARMENT AN ADDRESS OF ITS "
        "OWN: take any pixel's list of distances to the beacon centres and no other pixel of the "
        "piece shares it. FIRST INVARIANT WHOSE SUBJECT IS THE PIXELS THAT CARRY NO ORNAMENT - "
        "seventy-two axes state a law about the marks, and here the marks are only the instrument "
        "while the plain field is the thing the law is about. Exact complement of the 68th SEME, "
        "which forbids the MARKS to repeat a displacement; this forbids the CLOTH to repeat an "
        "address, and the two are indistinguishable by eye. Class identity is A PRECISION - the "
        "coarsest rule under which the survey still stands: warrior whole pixels, ranger half "
        "pixels, mage exact distances and nothing coarser. It is an OUTPUT, because the rules are "
        "nested and the reader tries them crudest-first. THE AMOUNT OF ORNAMENT IS DERIVED AND NOT "
        "CHOSEN: the blunter the instrument the more beacons the plate must carry, so the warrior "
        "settles at four or five, the ranger at three and the mage at two - and the class that is "
        "hardest to draw is the easiest to read, which inverts the whole project. THE WARRIOR PAYS "
        "FOR THE READER'S CARELESSNESS. See _ZOOM_survey_addresses.png, _ZOOM_survey_ground.png "
        "and _ZOOM_survey_controls.png)"
        ", 73rd %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_survey_legendary_preview", out="_PREVIEW_survey_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary73", "Warlord's Benchmark Cuirass"),
              ("mage", "shirt_mage_legendary73", "Archmage's Meridian Mantle"),
              ("ranger", "shirt_ranger_legendary73", "Warden's Half-Measure Jerkin")],
    ),
    "legs": dict(
        prev="_survey_legs_preview", out="_PREVIEW_survey_legs.png",
        note=NOTE % ("CHAUSSES - and note that THE SURVEY IS RUN OVER THE WHOLE GARMENT AND NOT "
                     "OVER EACH PART. A suit of two greaves is one piece of ground with one system "
                     "of coordinates laid across it, and a pixel on the left greave is told apart "
                     "from one on the right by the same rule that tells two pixels of the same "
                     "greave apart. The male warrior's chausses are PLAIN AND REPORTED: two poses "
                     "out of 35 would not take a survey coarse enough for a warrior", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary73", "Warlord's Benchmark Chausses"),
              ("mage", "pants_mage_legendary73", "Archmage's Meridian Leggings"),
              ("ranger", "pants_ranger_legendary73", "Warden's Half-Measure Greaves")],
    ),
    "boots": dict(
        prev="_survey_boots_preview", out="_PREVIEW_survey_boots.png",
        note=NOTE % ("SABATONS - and this is the slot where the class's own precision decides who "
                     "gets an ornament, IN THE ORDER OF THE INSTRUMENT. A blunt rule needs more "
                     "beacons and a sabaton has room for fewer, so the two demands meet here and "
                     "the coarsest class loses. Measured: the mage (exact) is dressed on both "
                     "sheets in all 42 poses; the ranger (half pixel) on the female sheet, and "
                     "reaches 32 of 35 on the male; the warrior (whole pixels) reaches 23 of 35 on "
                     "either. Three sheets are therefore PLAIN AND REPORTED, in exactly the order "
                     "the precisions predict - and an exhaustive search over every lawful "
                     "placement rescues only 3 of the warrior's 12 missing poses, so nine of them "
                     "are a fact about the sabaton and not about the search", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_survey", "Warlord's Benchmark Sabatons"),
              ("mage", "boots_mage_legendary_survey", "Archmage's Meridian Steps"),
              ("ranger", "boots_ranger_legendary_survey", "Warden's Half-Measure Boots")],
    ),
    "helmet": dict(
        prev="_surveydome_helmet_preview", out="_PREVIEW_surveydome_helmet.png",
        note=NOTE % ("HELM - and the ranger's hood is the sheet that taught this axis the "
                     "difference between a hard garment and a bad search. Forty-seven pixels in six "
                     "rows, and the first draft reported it PLAIN in all 35 poses because pure "
                     "greed put its first beacon where it cut the most ties on its own and left "
                     "nowhere legal for a third. An exhaustive search proved a lawful survey "
                     "existed in every one of the 35. Restarting the greed from each well-spread "
                     "candidate in turn recovers them all, and the hood now carries three beacons "
                     "in all 42 poses", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary73", "Warlord's Benchmark Helm"),
              ("mage", "helmet_mage_legendary73", "Archmage's Meridian Crown"),
              ("ranger", "helmet_ranger_legendary73", "Warden's Half-Measure Hood")],
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
        r = G.R[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, rule {G.RULES[r].upper()} - {RNAME[r]})",
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
    lab = 22 + 14 * max(len(n.split('\n')) - 1 for _im, n in cells)
    step = max(cw + pad, max((max(len(ln) for ln in n.split('\n')) * 7 + pad)
                             for _im, n in cells))
    canvas = Image.new("RGBA", (max(pad + len(cells) * step, wide),
                                pad + chh + lab + extra), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in cells:
        canvas.alpha_composite(im if im.size == (cw, chh) else im.resize((cw, chh), Image.NEAREST),
                               (x, pad))
        yy = pad + chh + 2
        for ln in name.split('\n'):
            d.text((x + 2, yy), ln, font=font(12), fill=(210, 210, 220, 255))
            yy += 14
        x += step
    if caption:
        yy = pad + chh + lab
        for line in caption.split('\n'):
            d.text((pad, yy), line, font=font(13), fill=(150, 200, 255, 255))
            yy += 16
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def _plate(cls, mode=None, fi=0, kind="chest", suffix=""):
    """One real plate, built through the generator, BEFORE the finishing pass."""
    cfg = G.SLOTS[kind]
    stem = '%s%s' % (cfg['srcs'][cls], suffix)
    base = G.load_any('%s.png' % stem)
    for f, sl, a in G.frames_of(base):
        if f != fi:
            continue
        fr, got = G.one_plate(base, sl, a, cls, mode, '%s|%d' % (stem, f))
        return fr, a, got, '%s|%d' % (stem, f)
    return None, None, None, None


CROP = (26, 16, 56, 50)
Z = 10
CW, CHH = (CROP[2] - CROP[0]) * Z, (CROP[3] - CROP[1]) * Z


def build_addresses_zoom():
    """THE LAW STATED. White rings every beacon CORE - the pixel every address is measured from -
    and beside each plate the four rules tried coarsest-first."""
    cells = []
    for cls in ("warrior", "ranger", "mage"):
        fr, a, _got, salt = _plate(cls)
        centres, r, _drop = G.compose(a, cls, None, salt)
        pts = np.argwhere(a)
        im = Image.fromarray(fr).crop(CROP).resize((CW, CHH), Image.NEAREST)
        d = ImageDraw.Draw(im)
        for c in centres:
            cx = (c[1] - CROP[0]) * Z + Z // 2
            cy = (c[0] - CROP[1]) * Z + Z // 2
            d.ellipse([cx - Z, cy - Z, cx + Z, cy + Z], outline=(255, 255, 255, 255), width=2)
        lines = ["%s   %d beacons, %d pixels of cloth" % (cls, len(centres), len(pts))]
        for rr in range(len(G.RULES)):
            ok = G.resolves(pts, centres, rr)
            lines.append("  %-7s %s" % (G.RULES[rr].upper(),
                                        "every pixel has its own address"
                                        if ok else "pixels fall into each other"))
        got = G.coarsest_that_resolves(pts, centres)
        lines.append("coarsest that works: %s  ->  %s (the CLASS, read off)"
                     % (G.RULES[got].upper(), cls))
        cells.append((im, "\n".join(lines)))
    _zoom(cells, CW, CHH, "_ZOOM_survey_addresses.png",
          caption="THE LAW. White rings each beacon's CORE. Give any pixel of the cloth its list of\n"
                  "distances to those cores and no other pixel of the piece has the same list - so\n"
                  "the ornament is not a decoration on the field, IT IS A SYSTEM OF COORDINATES FOR\n"
                  "IT, and what the law constrains is the plain cloth between the marks, which no\n"
                  "previous axis has ever said anything about.\n"
                  "The four rules are nested - each is a function of the one finer than it - so the\n"
                  "reader walks up from the crudest and stops at the first that works. That answer\n"
                  "is unique and it is the class: nobody is told it. Note what the counts do: the\n"
                  "BLUNTER THE INSTRUMENT THE MORE BEACONS THE PLATE MUST CARRY, and the amount of\n"
                  "ornament is therefore an output of this axis rather than a choice made by it.")


def build_ground_zoom():
    """THE SUBJECT IS THE UNMARKED FIELD, so for the first time in the project a panel paints it.
    Left: the plate at its own rule, where every pixel has an address of its own and there is
    nothing to mark. Right: the same plate one rule coarser, with every pixel that has fallen into
    somebody else's address painted red. The right-hand picture is clause PRECISION."""
    cells = []
    for cls in ("warrior", "ranger", "mage"):
        fr, a, _got, salt = _plate(cls)
        centres, r, _drop = G.compose(a, cls, None, salt)
        pts = np.argwhere(a)
        for rr, tag in ((r, "own rule"), (r - 1, "one rule coarser")):
            arr = fr.copy()
            M = np.stack([G.address_col(pts, b, rr) for b in centres], 1)
            _u, inv, cnt = np.unique(M, axis=0, return_inverse=True, return_counts=True)
            clash = cnt[inv] > 1
            for (y, x), bad in zip(pts, clash):
                if bad:
                    arr[y, x, :3] = (232, 60, 60)
            im = Image.fromarray(arr).crop(CROP).resize((CW, CHH), Image.NEAREST)
            n = int(clash.sum())
            cells.append((im, "%s, %s\n%s\n%s"
                          % (cls, tag, G.RULES[rr].upper(),
                             "no pixel shares an address" if n == 0
                             else "%d pixels of cloth collide" % n)))
    _zoom(cells, CW, CHH, "_ZOOM_survey_ground.png",
          caption="THE ONLY PANEL IN SEVENTY-THREE AXES WHOSE SUBJECT IS THE PIXELS BETWEEN THE\n"
                  "MARKS. Red is a pixel of plain cloth that shares its address with another pixel\n"
                  "of plain cloth. At the plate's own rule there is no red anywhere - that is the\n"
                  "law. One rule coarser the plate falls apart, and THAT IS ALSO THE LAW: clause\n"
                  "PRECISION demands the survey FAIL for a reader one step blunter, because a plate\n"
                  "that survived would be a different class wearing this one's colours. It is the\n"
                  "first clause in the project that asks the ornament to be INSUFFICIENT for\n"
                  "something, and it is what makes the class an output instead of a label.\n"
                  "Read the three pairs together and the axis's arithmetic is visible: the warrior\n"
                  "buys a careless reader's comfort with extra beacons, and the mage - two beacons,\n"
                  "the cheapest plate in the batch - can be read by nobody but the exact.")


def build_controls_zoom():
    """The same cuirass four ways, and only one of them is a plate this axis would ship."""
    cells = []
    for mode, name in ((None, "SURVEY (shipped)\nthree beacons, half-pixel rule"),
                       ('aligned', "ALIGNED\nbeacons on one row"),
                       ('clipped', "CLIPPED\none arm pruned where cloth allows"),
                       ('spare', "SPARE\none beacon more than needed")):
        fr, a, got, _salt = _plate('ranger', mode)
        if fr is None or got is None:
            continue
        cells.append((Image.fromarray(fr).crop(CROP), name))
    _zoom(cells, CW, CHH, "_ZOOM_survey_controls.png",
          caption="ONE RANGER CUIRASS, FOUR WAYS, ONE PAINTER, ONE PALETTE, ONE KIND OF RELIEF.\n"
                  "ALIGNED puts the beacons on one row. Two pixels share an EXACT address under two\n"
                  "beacons exactly when they are reflections in the line through them, and\n"
                  "reflection carries the pixel grid into itself only when that line is horizontal,\n"
                  "vertical or at 45 degrees. A row is such a line, the garment's own left-right\n"
                  "likeness supplies the collisions, and 0 of 379 plates get through. Counted over\n"
                  "the wardrobe, all 140 two-beacon mage plates lie along a direction the grid does\n"
                  "NOT respect - so THE MAGE IS LEGIBLE BY ARITHMETIC AND NOT BY DESIGN, and this\n"
                  "control is that sentence switched off.\n"
                  "CLIPPED prunes one arm from a beacon where the cloth would have taken it. The\n"
                  "law is untouched - every address is exactly what it was - and all 407 plates are\n"
                  "caught anyway, by the reader holding the figure against the silhouette it stands\n"
                  "on: a beacon clipped by the edge of the cloth is lawful, a beacon clipped by a\n"
                  "careless hand is not, and nobody has to tell the reader which is which.\n"
                  "SPARE adds one beacon beyond what the law needs. It is NOT WRONG ABOUT THE\n"
                  "GROUND - every pixel still has its own address - it is wrong about the PLATE,\n"
                  "and clause TIGHT catches 387 of 407. This axis is the first that TAKES ORNAMENT\n"
                  "BACK: the painter draws what the law needs and then removes every mark it can\n"
                  "do without.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_addresses_zoom()
    build_ground_zoom()
    build_controls_zoom()


if __name__ == "__main__":
    main()
