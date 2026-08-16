#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-FOURTH net-new-geometry axis batch
(ATTRITION family - the ornament is a BOARD OF SOCKETS, some of them filled, and the law is a number
that no amount of destroying the ornament can change).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 67th's was a sentence, so
its evidence became a READING. The 69th's was that nobody drew the ornament, so its evidence was the
poles ringed. The 71st's could not be seen at all, so its evidence was the reckoning set out in
full. The 72nd's was half a fact and half a non-event, so it took two panels of two different kinds.
The 73rd's was about the pixels between the marks, so its evidence had to paint the plain field.
THIS AXIS'S CLAIM IS THAT THE PICTURE DOES NOT MATTER, so for the first time in the project THE
EVIDENCE PANEL SHOWS THE SAME PLATE AS SEVERAL DIFFERENT PICTURES:

  _ZOOM_attrition_orbit.png     One real cuirass at four moments of its own demolition - as shipped,
                                after one jump, half way down, and played out until no move is left.
                                Two thirds of the ornament is gone by the last frame and the number
                                under every frame is the same number. THE LAW IS NOT A PROPERTY OF
                                THE PLATE, IT IS A PROPERTY OF EVERY PLATE THE PLATE CAN BECOME, and
                                this panel is the only way to say that with pictures.

  _ZOOM_attrition_board.png     One cuirass per class at 10x with every FILLED socket ringed white
                                and every EMPTY socket ringed grey - AND THE GREY RINGS ARE
                                THE PANEL'S, NOT THE PLATE'S: the empty sockets carry no ink,
                                because any one peg fixes the parity and the silhouette supplies
                                the rest. Beside it the two diagonal sums worked out in GF(4), which coordinates have closed, and
                                therefore the class - read off the plate and told to nobody. Under
                                the mage, the ninth of the board its last peg must stand on.

  _ZOOM_attrition_controls.png  The same cuirass four ways: as shipped, JUMPED (advanced by one
                                legal move - A DIFFERENT PICTURE AND THE SAME PLATE, and the only
                                control in seventy-four axes that is MEANT to pass), SLID (a peg
                                walked one socket instead of jumping) and OFFGRID (one peg beside
                                the lattice instead of on it - the value untouched and the plate
                                refused anyway, because the reader can no longer say what the board
                                IS).

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_attrition_axis74 as G                              # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

ONAME = {0: "NOTHING IN ITS WAY", 1: "ONE DIAGONAL CLOSED", 2: "BOTH DIAGONALS CLOSED"}
GF = {0: "0", 1: "1", 2: "w", 3: "w2"}

NOTE = ("net-new ATTRITION %s (the ground is a BOARD - every cloth pixel of one parity is a socket, "
        "so the board belongs to the silhouette and not to the painter. A filled socket is a bright PEG with a hard shadow one down and one left of it. "
        "THE EMPTY SOCKETS ARE NOT DRAWN AND DO NOT NEED TO BE: any one peg fixes the parity "
        "and the silhouette supplies the rest, so the reader rebuilds the whole board out of the "
        "pegs and the outline. The move is a JUMP: a peg hops its neighbour "
        "into the socket beyond AND THE PEG IT JUMPED IS TAKEN OFF THE PLATE.  The law is the "
        "plate's value - two sums in GF(4), one along each diagonal - AND NO JUMP CAN MOVE IT. "
        "FIRST INVARIANT THAT SURVIVES THE DESTRUCTION OF THE ORNAMENT THAT CARRIES IT: seventy-"
        "three axes state a law about a picture, and here the reader is invited to take the "
        "ornament apart until two thirds of it is gone and the number is where it was. Exact "
        "complement of the 66th DOVETAIL, whose acceptance test was satisfied by FAILING to take "
        "the artefact apart; this one's is satisfied by SUCCEEDING and finding the law standing in "
        "the rubble. Class identity is A NUMBER OF OBSTRUCTIONS - how many of the two coordinates "
        "have vanished, and therefore how many ways the plate can no longer end: mage 0 and it can "
        "name the ninth of the board its last peg must stand on, ranger 1, warrior 2. Every "
        "previous class counts something the plate HAS; this counts what it has LOST. "
        "See _ZOOM_attrition_orbit.png, _ZOOM_attrition_board.png and _ZOOM_attrition_controls.png)"
        ", 74th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_attrition_legendary_preview", out="_PREVIEW_attrition_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary74", "Warlord's Attrition Cuirass"),
              ("mage", "shirt_mage_legendary74", "Archmage's Remnant Mantle"),
              ("ranger", "shirt_ranger_legendary74", "Warden's Wasting Jerkin")],
    ),
    "legs": dict(
        prev="_attrition_legs_preview", out="_PREVIEW_attrition_legs.png",
        note=NOTE % ("CHAUSSES - and note that THE BOARD IS ONE BOARD AND NOT TWO. A suit of two "
                     "greaves is a single board with a gap down the middle of it; a peg on the left "
                     "greave counts into the same two sums as a peg on the right, and a jump can no "
                     "more cross the gap than it can cross the edge of the cloth, because the "
                     "socket it would land in is not there. All four chausses sheets carry the axis "
                     "in all 42 poses", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary74", "Warlord's Attrition Chausses"),
              ("mage", "pants_mage_legendary74", "Archmage's Remnant Leggings"),
              ("ranger", "pants_ranger_legendary74", "Warden's Wasting Greaves")],
    ),
    "boots": dict(
        prev="_attrition_boots_preview", out="_PREVIEW_attrition_boots.png",
        note=NOTE % ("SABATONS - and this is the slot where the axis meets a garment it cannot have. "
                     "A jump needs three sockets in a straight line, the sockets stand three pixels "
                     "apart, so a jump is seven pixels end to end and a sabaton is not seven pixels "
                     "of anything. The 73rd taught this project to find out whether a plain sheet is "
                     "a fact about the garment or a failure of the painter's search before saying "
                     "anything about it, so EVERY SUBSET OF EVERY ONE OF THE NINE PARITIES WAS "
                     "ENUMERATED, pose by pose: warrior 30 of 34 poses PROVED IMPOSSIBLE, ranger "
                     "male 11 of 11, mage male 10 of 10, and the four the search could still be "
                     "argued about are on a sheet that is plain either way. THE SABATON IS THE ONE "
                     "GARMENT IN THE WARDROBE WITH NOTHING LEFT TO LOSE. Four sheets are PLAIN AND "
                     "REPORTED - both warriors and both males - and the female mage and female "
                     "ranger, whose boards are the widest in the slot, carry the axis in all 42 "
                     "poses", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_attrition", "Warlord's Attrition Sabatons"),
              ("mage", "boots_mage_legendary_attrition", "Archmage's Remnant Steps"),
              ("ranger", "boots_ranger_legendary_attrition", "Warden's Wasting Boots")],
    ),
    "helmet": dict(
        prev="_attritiondome_helmet_preview", out="_PREVIEW_attritiondome_helmet.png",
        note=NOTE % ("HELM - and the helm is where the parity choice earns its keep. The painter "
                     "picks which of the nine parities the board sits on and nothing else; the "
                     "reader is never told which, because it reads the parity off the marks and "
                     "then checks against the outline that nothing of that parity was left out. On "
                     "a hood of forty-seven pixels the roomiest parity is often the one with no "
                     "straight run of three sockets anywhere in it, so A PARITY WITH FEWER SOCKETS "
                     "AND A GAME IN IT IS THE BETTER BOARD - and with all nine offered, every helm "
                     "and hood in the batch carries the axis in all 42 poses", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary74", "Warlord's Attrition Helm"),
              ("mage", "helmet_mage_legendary74", "Archmage's Remnant Crown"),
              ("ranger", "helmet_ranger_legendary74", "Warden's Wasting Hood")],
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
        o = G.OBSTRUCT[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, {o} obstruction(s) - {ONAME[o]})",
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


def repaint(fr, a, cls, cells, bc, pegs):
    """The SAME plate with a DIFFERENT set of pegs on it - which is the only thing this axis's
    evidence panel needs and which no previous axis has had a reason to want."""
    arr = fr.copy()
    wit_c, field_c, peg_c = G.PAL[cls]
    for y, x in np.argwhere(a):
        G.put(arr, y, x, field_c)
    core, dark = G.paint(a, cells, bc, pegs)
    for y, x in np.argwhere(dark):
        G.put(arr, y, x, wit_c)
    for y, x in np.argwhere(core):
        G.put(arr, y, x, peg_c)
    return arr


CROP = (26, 16, 56, 50)
Z = 10
CW, CHH = (CROP[2] - CROP[0]) * Z, (CROP[3] - CROP[1]) * Z


def build_orbit_zoom():
    """THE CLAIM IS THAT THE PICTURE DOES NOT MATTER, SO THE PANEL IS FOUR PICTURES. One warrior
    cuirass at four moments of its own demolition, with the value printed under each. It is the same
    number four times and it is under four different plates."""
    cls = 'warrior'
    fr, a, _got, salt = _plate(cls)
    _py, _px, cells, bc, pegs = G.compose(a, cls, None, salt)
    allc = set(bc.values())

    # replay the reader's own demolition, keeping the positions it passed through
    st = set(pegs)
    rng = G.Rng(salt + '|demo')
    states = [set(st)]
    while True:
        js = sorted(G.legal_jumps(st, allc))
        if not js:
            break
        A, B, C = js[rng.below(len(js))]
        st.discard(A)
        st.discard(B)
        st.add(C)
        states.append(set(st))
    n = len(states) - 1
    picks = [(0, "AS SHIPPED"), (1, "AFTER ONE JUMP"), (n // 2, "HALF WAY DOWN"),
             (n, "PLAYED OUT - NO MOVE LEFT")]
    start = len(states[0])
    cells_out = []
    for i, tag in picks:
        p = states[i]
        val = G.value(p)
        arr = repaint(fr, a, cls, cells, bc, p)
        im = Image.fromarray(arr).crop(CROP).resize((CW, CHH), Image.NEAREST)
        cells_out.append((im, "%s\n%d jumps played, %d pegs left\n%d%% of the ornament destroyed\n"
                              "VALUE  (%s, %s)   obstructions %d"
                          % (tag, i, len(p), 100 * (start - len(p)) // start,
                             GF[val[0]], GF[val[1]], G.obstructions(val))))
    _zoom(cells_out, CW, CHH, "_ZOOM_attrition_orbit.png",
          caption="ONE WARRIOR CUIRASS, FOUR TIMES, AND THE NUMBER UNDER IT NEVER MOVES.\n"
                  "Each frame is the frame before it after some legal jumps. A jump takes a peg\n"
                  "over its neighbour into the empty socket beyond and REMOVES THE PEG IT JUMPED,\n"
                  "so the plate loses one peg a move and by the last frame two thirds of the\n"
                  "ornament is gone. The two sums are unchanged because the three sockets a jump\n"
                  "touches lie one after another along a diagonal, and w^2 + w + 1 = 0 in GF(4):\n"
                  "the jump adds their three labels to the total, and those three add to nothing.\n"
                  "THE LAW IS NOT A PROPERTY OF THIS PICTURE. It is a property of every picture\n"
                  "reachable from it, and the plate the batch ships is only the one the painter\n"
                  "happened to stop at. That is why control JUMPED is the only control in\n"
                  "seventy-four axes that this project WANTS to pass - and it passes 335 of 335,\n"
                  "while TOGGLED (84 of 363), SLID (95 of 365) and RANDOM (76 of 365, a board\n"
                  "filled with no thought at all) all land within five points of each other at a\n"
                  "quarter. EVERY ILLEGAL ALTERATION IS EXACTLY AS GOOD AS STARTING OVER, AND THE\n"
                  "LEGAL ONE IS FREE.")


def build_board_zoom():
    """THE LAW STATED. White rings a filled socket, grey rings an empty one, and beside each plate
    the two diagonal sums worked out and the class read off them."""
    cells_out = []
    for cls in ("warrior", "ranger", "mage"):
        fr, a, _got, salt = _plate(cls)
        _py, _px, cells, bc, pegs = G.compose(a, cls, None, salt)
        allc = set(bc.values())
        im = Image.fromarray(fr).crop(CROP).resize((CW, CHH), Image.NEAREST)
        d = ImageDraw.Draw(im)
        for (y, x), (u, v) in bc.items():
            cx, cy = (x - CROP[0]) * Z + Z // 2, (y - CROP[1]) * Z + Z // 2
            if not (0 <= cx < CW and 0 <= cy < CHH):
                continue
            filled = (u, v) in pegs
            d.ellipse([cx - Z // 2 - 2, cy - Z // 2 - 2, cx + Z // 2 + 2, cy + Z // 2 + 2],
                      outline=(255, 255, 255, 255) if filled else (128, 132, 140, 255),
                      width=2 if filled else 1)
        val = G.value(pegs)
        nin = G.ninth_of(val)
        n, seen, left = G.demolish(pegs, allc, salt)
        lines = ["%s   %d sockets, %d filled" % (cls, len(allc), len(pegs)),
                 "  S = XOR of w^(u+v) = %s" % GF[val[0]],
                 "  T = XOR of w^(u-v) = %s" % GF[val[1]],
                 "obstructions %d  ->  %s (the CLASS, read off)" % (G.obstructions(val), cls),
                 "demolition: %d jumps, %d pegs left," % (n, len(left)),
                 "  %d distinct values seen" % len(set(seen))]
        lines.append("last peg: %s" % ("sockets (u,v) = (%d,%d) mod 3" % nin if nin
                                       else "NO socket on this board can be it"))
        cells_out.append((im, "\n".join(lines)))
    _zoom(cells_out, CW, CHH, "_ZOOM_attrition_board.png",
          caption="THE LAW. White rings a FILLED socket, grey an EMPTY one. The board is every\n"
                  "cloth pixel of one parity, so it is the silhouette's and not the painter's, and\n"
                  "the reader checks against the outline that no socket was hidden. Give each\n"
                  "socket the label w^(u+v) on one diagonal and w^(u-v) on the other, add up the\n"
                  "filled ones in GF(4), and the plate has a value. THE GREY RINGS ARE THIS PANEL'S\n"
                  "AND NOT THE PLATE'S: an empty socket carries no ink, because any one peg fixes\n"
                  "the parity and the outline supplies every other socket for nothing.\n"
                  "A LONE PEG HAS BOTH COORDINATES NON-ZERO, ALWAYS. So a coordinate that vanishes\n"
                  "is a door that has closed: the plate can never be played down to a single peg,\n"
                  "and nothing you do to it will ever reveal that - only the sum will. The class is\n"
                  "how many doors have closed. The mage has none, and can therefore name the ninth\n"
                  "of the board its last peg must stand on before a single move is played; the\n"
                  "warrior has both, and its plate is the most ornamented in the batch and the one\n"
                  "with the least future. EVERY PREVIOUS CLASS IDENTITY COUNTS SOMETHING THE PLATE\n"
                  "HAS. THIS ONE COUNTS WHAT IT HAS LOST.\n"
                  "Counted over the wardrobe: 130 mage plates name their last socket and 0 cannot;\n"
                  "0 ranger and 0 warrior plates can name one, and 235 of them confirm it the hard\n"
                  "way, by the reader trying all 2903 sockets those boards have.")


def build_controls_zoom():
    """The same cuirass four ways - and for the first time in the project, one of the three
    alterations is one the axis is pleased to see pass."""
    cells_out = []
    for mode, name in ((None, "ATTRITION (shipped)\nranger, one diagonal closed"),
                       ('jumped', "JUMPED - MEANT TO PASS\none legal move, two fewer pegs"),
                       ('slid', "SLID\na peg walked one socket"),
                       ('offgrid', "OFFGRID\none peg off the lattice")):
        fr, a, got, _salt = _plate('ranger', mode)
        if fr is None or got is None:
            continue
        cells_out.append((Image.fromarray(fr).crop(CROP), name))
    _zoom(cells_out, CW, CHH, "_ZOOM_attrition_controls.png",
          caption="ONE RANGER CUIRASS, FOUR WAYS, ONE PAINTER, ONE PALETTE, ONE KIND OF RELIEF.\n"
                  "JUMPED advances the plate by a single legal move. It is a different picture with\n"
                  "two fewer pegs on it and IT PASSES EVERY CLAUSE, 335 of 335 - the only control in\n"
                  "seventy-four axes that this project is pleased to see get through. It is the\n"
                  "orbit, run as a control: the axis's whole claim is that these two pictures are\n"
                  "one plate, and the only honest way to test that claim is to build the other\n"
                  "picture and hand it to the reader without saying which is which.\n"
                  "SLID moves one peg to a neighbouring socket instead of jumping it. That is the\n"
                  "nearest thing to a legal move that is not one - nothing is destroyed, nothing is\n"
                  "added - and it takes the value with it: 95 of 365 clean, which is where CHANCE\n"
                  "puts it. TOGGLED (84 of 363) and RANDOM (76 of 365) land in the same place.\n"
                  "The value has only sixteen states, so a plate drawn at random wears its class's\n"
                  "shape about a quarter of the time, and this file would rather print that than\n"
                  "hide it - BECAUSE IT IS THE FINDING. Every illegal alteration is worth exactly\n"
                  "what starting over is worth, and the legal one costs nothing at all.\n"
                  "OFFGRID puts one peg beside the lattice instead of on it. The value does not\n"
                  "move a hair - a stray is not on the board at all, so it is in neither sum - and\n"
                  "the reader refuses all 365 anyway, because the pegs no longer agree on a parity\n"
                  "and it can no longer say what the BOARD is. That is the price of not painting\n"
                  "the empty sockets, and clause BOARD collects it in full - all 365. Not shown,\n"
                  "and worth the same sentence: DEAD fills alternate sockets so no peg has a\n"
                  "neighbour and no jump exists anywhere. Its value is safe from every move for the\n"
                  "wrong reason - nothing can happen to it - and clause LIVE catches all 372. It is\n"
                  "the first clause in the project that DEMANDS THE ARTEFACT BE DESTRUCTIBLE.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_orbit_zoom()
    build_board_zoom()
    build_controls_zoom()


if __name__ == "__main__":
    main()
