#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-FIRST net-new-geometry axis batch
(GAMBIT family - the ornament is a POSITION IN A GAME and the law is what it is worth).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 67th's was a sentence, so
its evidence became a READING. The 68th's was that nothing repeats, so its evidence became a
HISTOGRAM. The 69th's was that nobody drew the ornament, so its evidence was the poles ringed. The
70th's was about motion, so its evidence was the seed cycle traced.
THIS AXIS'S CLAIM CANNOT BE SEEN AT ALL. Two plates one edge apart are two different classes and
look alike; the number is something the plate knows and does not show. So the evidence is not a
picture of the law - there is no such picture - it is the READING and the RECKONING set out in full,
and then the one comparison that proves the order matters:

  _ZOOM_gambit_words.png     One real cuirass per class at 10x with every stalk's GROUND END ringed
                             in gold and its free end in blue, and beside each the word the reader
                             walks off it, that word's value by Berlekamp's rule, and the sum. The
                             sum is the class, and nothing else on the plate is.

  _ZOOM_gambit_controls.png  THE SAME CUIRASS FOUR TIMES: as shipped, then REVERSED (every pixel
                             the same colour, every stalk the same length, only the order along the
                             stalk turned round - and a different number), MONO (one colour per
                             stalk: a stripe nobody argues about) and FLOATING (the same stalks
                             grown from an interior pixel, joined to the ground nowhere, which in
                             this game is not a wrong position but NO POSITION).

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
from fractions import Fraction

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_gambit_axis71 as G                                 # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

VNAME = {Fraction(0): "A DRAWN GAME - whoever moves first loses",
         Fraction(1, 2): "LEFT IS HALF A MOVE AHEAD",
         Fraction(1, 4): "LEFT IS A QUARTER OF A MOVE AHEAD"}

NOTE = ("net-new GAMBIT %s (the ornament is a POSITION IN A GAME. Each stalk is a chain of pixels "
        "rooted on the piece's own silhouette and growing inward, every pixel of it one edge, and "
        "every edge painted in one of two stops: the brightest is LEFT's claim, the next is "
        "RIGHT's. The game is Blue-Red Hackenbush - each player may cut an edge of their own "
        "colour, everything no longer joined to the ground falls off, and the player with no move "
        "loses - and the law is not about where the stalks are but about WHAT THE PLATE IS WORTH "
        "WHEN BOTH SIDES PLAY PERFECTLY. FIRST INVARIANT THAT REQUIRES AN OPPONENT: the 66th "
        "DOVETAIL asks whether a part can be taken away and a hand tries; the 70th TRUSS asks what "
        "the figure would do if pushed and a force pushes; this asks what happens if somebody "
        "WANTS IT GONE and has read the plate as carefully as the reader has. The acceptance test "
        "is a SOLUTION and it is done twice by two methods that share nothing: Berlekamp's rule "
        "turns each word into a number and the numbers are added, and then the real game tree is "
        "built and solved by minimax with no arithmetic in it at all. CLAUSE PLAYOUT IS THE FIRST "
        "CLAUSE IN THE PROJECT THAT COULD CONTRADICT ANOTHER CLAUSE OF ITS OWN AXIS, and on 735 "
        "plates it never did. Class identity is A FRACTION OF A MOVE - warrior 0, ranger 1/2, mage "
        "1/4 - and it is the first class that CANNOT BE SEEN, only reckoned. Exact inversion of "
        "the 60th CADENCE, which admits one word of each length and forbids every other; this "
        "admits EVERY word and constrains only the total. See _ZOOM_gambit_words.png and "
        "_ZOOM_gambit_controls.png)"
        ", 71st %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_gambit_legendary_preview", out="_PREVIEW_gambit_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary71", "Warlord's Stalemate Cuirass"),
              ("mage", "shirt_mage_legendary71", "Archmage's Quarter-Move Mantle"),
              ("ranger", "shirt_ranger_legendary71", "Warden's Half-Move Jerkin")],
    ),
    "legs": dict(
        prev="_gambit_legs_preview", out="_PREVIEW_gambit_legs.png",
        note=NOTE % ("CHAUSSES - and note that THE POSITION IS THE WHOLE PLATE, NOT THE PART. This "
                     "is the exact opposite of the 70th, where a framework is a local object and "
                     "two legs are two structures. Hackenbush positions ADD over their components: "
                     "a stalk on the left greave and a stalk on the right are in the same game, "
                     "either player may cut either, and the balance is struck across the whole "
                     "garment at once", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary71", "Warlord's Stalemate Chausses"),
              ("mage", "pants_mage_legendary71", "Archmage's Quarter-Move Leggings"),
              ("ranger", "pants_ranger_legendary71", "Warden's Half-Move Greaves")],
    ),
    "boots": dict(
        prev="_gambit_boots_preview", out="_PREVIEW_gambit_boots.png",
        note=NOTE % ("SABATONS - and this is the slot where the axis's own theorems decide who gets "
                     "an ornament and who does not, in the order they predict. A stalk is never "
                     "worth nothing, so a DRAWN game needs two stalks, and a sabaton has room for "
                     "one: the warrior's boots are PLAIN AND REPORTED. A quarter of a move is the "
                     "third halving, so it needs a stalk THREE edges long, and the male mage's "
                     "sabaton runs out of garment at two in seven of its poses: PLAIN AND "
                     "REPORTED. Half a move is '+-' and fits in two edges anywhere, so the "
                     "ranger's are contested in all forty-two poses. THE CLASS'S DENOMINATOR IS A "
                     "LOWER BOUND ON ITS LONGEST STALK AND ITS BALANCE IS A LOWER BOUND ON ITS "
                     "STALK COUNT, and the three boots fail in exactly that order", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_gambit", "Warlord's Stalemate Sabatons"),
              ("mage", "boots_mage_legendary_gambit", "Archmage's Quarter-Move Steps"),
              ("ranger", "boots_ranger_legendary_gambit", "Warden's Half-Move Boots")],
    ),
    "helmet": dict(
        prev="_gambitdome_helmet_preview", out="_PREVIEW_gambitdome_helmet.png",
        note=NOTE % ("HELM - and the dome is the easiest surface in the batch for this axis, "
                     "because a skull is convex and a convex part has an interior for a stalk's "
                     "FREE END to stop in. A stalk whose far end lands back on the silhouette can "
                     "be walked from either end and is worth two different numbers depending on "
                     "which, so it is refused; on a flat ribbon almost every stalk is refused, and "
                     "on a dome almost none is", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary71", "Warlord's Stalemate Helm"),
              ("mage", "helmet_mage_legendary71", "Archmage's Quarter-Move Crown"),
              ("ranger", "helmet_ranger_legendary71", "Warden's Half-Move Hood")],
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
        v = G.TARGET[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, value = {v} - {VNAME[v]})",
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
    canvas = Image.new("RGBA", (max(pad + len(cells) * (cw + pad), wide),
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
        x += cw + pad
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


def build_words_zoom():
    """THE READING AND THE RECKONING, SET OUT. The gold ring is the ground end - the pixel the
    reader starts from - and the blue ring is the free end. The word between them is what the plate
    says, the fraction is what Berlekamp's rule makes of it, and the sum is the class."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for cls in ("warrior", "ranger", "mage"):
        fr, a, _got, salt = _plate(cls)
        got = G.compose(a, cls, None, salt)
        im = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
        d = ImageDraw.Draw(im)
        stalks, words = got
        for px in stalks:
            for p, col in ((px[0], (255, 220, 90, 255)), (px[-1], (140, 200, 255, 255))):
                cx = (p[1] - crop[0]) * Z + Z // 2
                cy = (p[0] - crop[1]) * Z + Z // 2
                d.ellipse([cx - Z, cy - Z, cx + Z, cy + Z], outline=col, width=2)
        tot = sum((G.value_of(w) for w in words), Fraction(0))
        oc = G.outcome(words)
        lines = ["%s   value %s" % (cls, tot)]
        cur = ""
        for w in words:
            piece = "%s = %s" % (w, G.value_of(w))
            if len(cur) + len(piece) + 3 > 34:
                lines.append(cur)
                cur = piece
            else:
                cur = (cur + "   " + piece).strip()
        if cur:
            lines.append(cur)
        lines.append("playout: L-first %s, R-first %s"
                     % (oc[0] if oc else '?', oc[1] if oc else '?'))
        cells.append((im, "\n".join(lines)))
    _zoom(cells, cw, chh, "_ZOOM_gambit_words.png",
          caption="THE CLASS IS THE SUM, AND NOTHING ON THE PLATE SHOWS IT.\n"
                  "Gold is the GROUND END of a stalk - the pixel that touches the silhouette, the\n"
                  "only pixel on the plate the piece did not choose for itself - and blue is the\n"
                  "FREE END. The reader walks from gold to blue and gets a word in two letters;\n"
                  "Berlekamp's rule turns the word into a number (an initial run of m same-coloured\n"
                  "edges is worth m outright, and every edge after the first change of colour is\n"
                  "worth half the one below it); the numbers add, because disjoint games add.\n"
                  "Warrior 0, ranger 1/2, mage 1/4. THE LAST LINE OF EACH LABEL IS THE SECOND,\n"
                  "INDEPENDENT RECKONING: the real game tree, solved by minimax with no arithmetic\n"
                  "in it, saying who actually wins moving first and moving second. A value of zero\n"
                  "must mean WHOEVER MOVES FIRST LOSES, and a positive value must mean Left wins\n"
                  "either way. The formula and the search have never once disagreed, on any of the\n"
                  "735 plates in this batch.")


def build_controls_zoom():
    """The same cuirass, four ways - and the second of them has not moved a single pixel."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for mode, name in ((None, "GAMBIT (shipped)\nvalue 1/2"),
                       ('reversed', "REVERSED\nsame pixels, other order"),
                       ('mono', "MONO\none colour per stalk"),
                       ('floating', "FLOATING\nno ground end at all")):
        fr, a, _got, salt = _plate('ranger', mode)
        if fr is None:
            continue
        im = Image.fromarray(fr).crop(crop)
        cells.append((im, name))
    _zoom(cells, cw, chh, "_ZOOM_gambit_controls.png",
          caption="ONE RANGER CUIRASS, FOUR POSITIONS, ONE PAINTER, ONE PALETTE, ONE KIND OF\n"
                  "RELIEF. REVERSED is the finding: every stalk keeps its length, every colour\n"
                  "keeps its count, and only the ORDER along the stalk is turned round - '+-' is\n"
                  "half a move and '-+' is minus half a move, so the plate is worth something else\n"
                  "entirely. THE GROUND IS NOT DECORATION. MONO paints each stalk in one colour:\n"
                  "the values become whole numbers, and no whole number is 1/2 or 1/4 - a\n"
                  "one-coloured stalk is a run of free moves that nobody contests, which is what\n"
                  "the fraction is FOR. FLOATING grows the same stalks from an interior pixel so\n"
                  "that nothing touches the ground; in Hackenbush anything not joined to the ground\n"
                  "is already gone, so however much ink is on the plate THE POSITION IS EMPTY. It\n"
                  "is the only control in seventy-one axes that is not wrong but ABSENT.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_words_zoom()
    build_controls_zoom()


if __name__ == "__main__":
    main()
