#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-FIFTH net-new-geometry axis batch
(CONFLUENCE family - the ornament is a set of LOADED PILES, and the law is that the picture they
become is the same picture whoever runs them, and that picture is nowhere on the plate).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 69th's was that nobody
drew the ornament, so its evidence was the poles ringed. The 71st's could not be seen at all, so its
evidence was the reckoning set out in full. The 73rd's was about the pixels between the marks, so it
had to paint the plain field. The 74th's was that the picture does not matter, so it showed one
plate as four different pictures.

THIS AXIS'S CLAIM IS ABOUT A PICTURE THAT IS NOT ON THE PLATE - the one the piles settle into - so
for the first time the evidence panel has to draw something the batch does not ship:

  _ZOOM_confluence_race.png     One real cuirass, then the SAME cuirass half way through two
                                deliberately opposite schedules, then the end of each. The two
                                middles are different pictures. THE TWO ENDS ARE THE SAME PICTURE,
                                pixel for pixel, and that picture is in no file in this batch. The
                                reader is what produces it, and every reader produces this one.

  _ZOOM_confluence_piles.png    One cuirass per class at 10x with every LOADED socket ringed cyan
                                and every settled one ringed grey - and the rings are the PANEL'S,
                                not the plate's, because a settled socket is just a stud.
                                Beside it the avalanche worked out: how many topples, which socket
                                is the busiest, how many times it goes off, and therefore the class,
                                read off the plate and told to nobody.

  _ZOOM_confluence_weak.png     THE ONE STUD THAT IS CARRYING THE CLASS. The same cuirass as
                                shipped, then advanced by an ORDINARY legal move (a different
                                picture, the same destination, the same class), then advanced by the
                                ONE move that spends the class. Two hundred and twenty-one plates in
                                the batch have such a move and none of them has two.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_confluence_axis75 as G                             # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

DNAME = {1: "ONE TOPPLE DEEP", 2: "TWO TOPPLES DEEP", 3: "THREE TOPPLES DEEP"}

NOTE = ("net-new CONFLUENCE %s (the ground is a BOARD - every cloth pixel of one lattice is a "
        "socket, and THE PAINTER NEVER SAYS WHICH OF THE NINE IT USED, because exactly one of them "
        "makes the picture parse at all and the reader finds it by trying all nine. A socket holds "
        "one, two or three chips, drawn as a cluster that grows in a fixed order - centre, then "
        "right, then down - so a stud is one, a dash is two and an L is three, each with a hard "
        "shadow one down and one left. A pile of one is settled and a pile of two or three is "
        "LOADED, so you can see which sockets are about to go off. The move is a TOPPLE: a loaded "
        "socket gives one chip to the socket on its right and one to the socket below, and chips "
        "aimed off the cloth are gone. THE LAW IS THAT EVERY ORDER OF PLAY HALTS AND EVERY ORDER "
        "ENDS AT THE SAME PICTURE AND THE SAME TALLY OF TOPPLES. FIRST INVARIANT THAT IS A "
        "UNIQUENESS OF OUTCOME RATHER THAN A CONSTANCY - seventy-four axes name something that does "
        "not move; this names something that does, and says the reader has no say in where it moves "
        "to. Exact complement of the 74th ATTRITION: that one said do what you like and this number "
        "will not change, this one says do what you like and you will end up in the same place. "
        "FIRST LAW WHOSE SUBJECT IS A PICTURE THAT WAS NEVER PAINTED - the arrangement the law is "
        "about is not on the plate, not in the file, and was drawn by nobody. Class identity is a "
        "DEPTH, the greatest number of times any one socket has to topple: mage 1, ranger 2, "
        "warrior 3. Every previous class counts a number of THINGS; this is the first that is a "
        "number of TIMES. The halt is PROVED and not budgeted - weight each chip by how far it has "
        "left to travel and a topple costs exactly two - so there is no iteration limit anywhere in "
        "the axis. See _ZOOM_confluence_race.png, _ZOOM_confluence_piles.png and "
        "_ZOOM_confluence_weak.png), 75th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_confluence_legendary_preview", out="_PREVIEW_confluence_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary75", "Warlord's Confluent Cuirass"),
              ("mage", "shirt_mage_legendary75", "Archmage's Settling Mantle"),
              ("ranger", "shirt_ranger_legendary75", "Warden's Landslip Jerkin")],
    ),
    "legs": dict(
        prev="_confluence_legs_preview", out="_PREVIEW_confluence_legs.png",
        note=NOTE % ("CHAUSSES - and the chausses are where the ceiling argument earns its keep. "
                     "The male warrior sheet is PLAIN AND REPORTED, and it is not the painter's "
                     "fault: the tally of topples is MONOTONE in the load, so filling every socket "
                     "to the most its cloth can show and settling that once gives the deepest "
                     "avalanche the garment could EVER carry. On one pose of the male chausses that "
                     "ceiling is two and the warrior needs three, so the sheet is impossible rather "
                     "than unfound - a theorem for the price of one settling, where the 74th needed "
                     "an enumeration over every subset of every parity. The other five sheets carry "
                     "the axis in all 42 poses", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary75", "Warlord's Confluent Chausses"),
              ("mage", "pants_mage_legendary75", "Archmage's Settling Leggings"),
              ("ranger", "pants_ranger_legendary75", "Warden's Landslip Greaves")],
    ),
    "boots": dict(
        prev="_confluence_boots_preview", out="_PREVIEW_confluence_boots.png",
        note=NOTE % ("SABATONS - the slot where the axis meets garments it cannot have, and can "
                     "prove it. A sabaton is thirty pixels, which is four sockets, and a chip that "
                     "topples has nowhere to land: the ceiling on both warrior sheets is ZERO on "
                     "every one of the 35 poses, so no painter could have loaded them. Four sheets "
                     "are PLAIN AND REPORTED - both warriors and the male mage and male ranger - "
                     "and the female mage and female ranger, whose boards are the widest in the "
                     "slot, carry the axis in all 42 poses. THE SABATON HAS NO ROOM FOR AN "
                     "AVALANCHE, and that is a fact about the sabaton", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_confluence", "Warlord's Confluent Sabatons"),
              ("mage", "boots_mage_legendary_confluence", "Archmage's Settling Steps"),
              ("ranger", "boots_ranger_legendary_confluence", "Warden's Landslip Boots")],
    ),
    "helmet": dict(
        prev="_confluencedome_helmet_preview", out="_PREVIEW_confluencedome_helmet.png",
        note=NOTE % ("HELM - and the helm is where the undeclared lattice earns its keep. The "
                     "painter chooses one of the nine and tells nobody; the constraint it accepts "
                     "in exchange is that EXACTLY ONE lattice may parse the finished picture, which "
                     "is checked at the easel with the reader's own parser and refused otherwise. "
                     "On a hood of forty-seven pixels that is a real constraint and it is met on "
                     "every pose: all six helms and hoods carry the axis in all 42", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary75", "Warlord's Confluent Helm"),
              ("mage", "helmet_mage_legendary75", "Archmage's Settling Crown"),
              ("ranger", "helmet_ranger_legendary75", "Warden's Landslip Hood")],
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
        dep = G.DEPTH[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, depth {dep} - {DNAME[dep]})",
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


# --- evidence ----------------------------------------------------------------------------------
CROP = (28, 20, 55, 50)
Z = 10
CW, CHH = (CROP[2] - CROP[0]) * Z, (CROP[3] - CROP[1]) * Z


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


def repaint(fr, a, cls, bc_inv, chips):
    """The SAME plate wearing a DIFFERENT arrangement of piles. This axis's evidence needs to draw
    configurations the batch does not ship - the half way points, and the destination - and this is
    what draws them."""
    arr = fr.copy()
    shadow_c, field_c, chip_c = G.PAL[cls]
    for y, x in np.argwhere(a):
        G.put(arr, y, x, field_c)
    core, dark = G.paint(a, bc_inv, chips)
    for y, x in np.argwhere(dark):
        G.put(arr, y, x, shadow_c)
    for y, x in np.argwhere(core):
        G.put(arr, y, x, chip_c)
    return arr


def _im(arr):
    return Image.fromarray(arr[CROP[1]:CROP[3], CROP[0]:CROP[2]]).resize((CW, CHH), Image.NEAREST)


def _run(chips, B, sched, salt, stop=None):
    """Play a schedule, optionally stopping part way. Returns (chips, topples taken)."""
    ch = {c: k for c, k in chips.items() if k}
    n = 0
    while stop is None or n < stop:
        loaded = [c for c, k in ch.items() if k >= G.THRESH]
        if not loaded:
            break
        if sched == 'first':
            c = min(loaded)
        elif sched == 'last':
            c = max(loaded)
        else:
            c = max(loaded, key=lambda z: (ch[z], z))
        ch[c] -= G.THRESH
        if not ch[c]:
            del ch[c]
        for du, dv in G.FIRE:
            t = (c[0] + du, c[1] + dv)
            if t in B:
                ch[t] = ch.get(t, 0) + 1
        n += 1
    return ch, n


def build_race_zoom():
    """THE LAW, IN PICTURES. The middles disagree and the ends do not."""
    cls = 'warrior'
    fr, a, _got, salt = _plate(cls)
    _py, _px, _cells, _bc, bc_inv, B, chips = G.compose(a, cls, None, salt)
    full, total = _run(chips, B, 'first', salt)
    half = max(1, total // 2)
    mid_a, _ = _run(chips, B, 'first', salt, stop=half)
    mid_b, _ = _run(chips, B, 'last', salt, stop=half)
    end_a, _ = _run(chips, B, 'first', salt)
    end_b, _ = _run(chips, B, 'last', salt)
    end_c, _ = _run(chips, B, 'loaded', salt)
    same_ab = sorted(end_a.items()) == sorted(end_b.items())
    same_ac = sorted(end_a.items()) == sorted(end_c.items())
    mid_diff = sorted(mid_a.items()) != sorted(mid_b.items())
    cells = [
        (_im(repaint(fr, a, cls, bc_inv, chips)),
         'AS SHIPPED\n%d chips, %d loaded sockets' % (sum(chips.values()),
                                                      sum(1 for v in chips.values()
                                                          if v >= G.THRESH))),
        (_im(repaint(fr, a, cls, bc_inv, mid_a)),
         'HALF WAY, lowest-first\n%d topples in' % half),
        (_im(repaint(fr, a, cls, bc_inv, mid_b)),
         'HALF WAY, highest-first\n%d topples in - A DIFFERENT PICTURE' % half),
        (_im(repaint(fr, a, cls, bc_inv, end_a)),
         'SETTLED, lowest-first\n%d topples, %d chips left' % (total, sum(end_a.values()))),
        (_im(repaint(fr, a, cls, bc_inv, end_b)),
         'SETTLED, highest-first\nTHE SAME PICTURE' if same_ab else 'SETTLED, highest-first\nDIFFERS'),
    ]
    cap = ('ONE WARRIOR CUIRASS, PLAYED TWO OPPOSITE WAYS. The two middles are different pictures '
           '(%s). The two ends are the same picture,\n'
           'pixel for pixel (%s), and so is the third schedule (%s) - and THAT PICTURE IS IN NO '
           'FILE IN THIS BATCH.\n'
           'The plate ships the loaded arrangement; the arrangement the law is about is the one it '
           'settles into, and nobody drew it.\n'
           'This is the first law in the project whose subject was never painted, and the first '
           'that is a uniqueness of outcome rather than a constancy.'
           % ('confirmed' if mid_diff else 'IDENTICAL - retune',
              'confirmed' if same_ab else 'FAILED',
              'confirmed' if same_ac else 'FAILED'))
    _zoom(cells, CW, CHH, '_ZOOM_confluence_race.png', cap)


def build_piles_zoom():
    """THE READING, DONE ON THE PAGE. Loaded sockets ringed white, settled ones ringed grey, the
    avalanche worked out, the class read off the plate."""
    cells = []
    for cls in ('warrior', 'ranger', 'mage'):
        fr, a, _got, salt = _plate(cls)
        _py, _px, _cells, _bc, bc_inv, B, chips = G.compose(a, cls, None, salt)
        im = _im(fr).convert('RGBA')
        d = ImageDraw.Draw(im)
        for c, k in chips.items():
            y0, x0 = bc_inv[c]
            if not (CROP[1] <= y0 < CROP[3] and CROP[0] <= x0 < CROP[2]):
                continue
            px, py = (x0 - CROP[0]) * Z, (y0 - CROP[1]) * Z
            hot = k >= G.THRESH
            d.rectangle([px - 2, py - 2, px + Z + 1, py + Z + 1],
                        outline=(90, 240, 255, 255) if hot else (128, 132, 150, 255),
                        width=2 if hot else 1)
        _fin, od, n = G.stabilise(chips, B, 'first', salt)
        busiest = max(od, key=lambda z: (od[z], z)) if od else None
        dep = max(od.values()) if od else 0
        cells.append((im, '%s\n%d sockets, %d chips, %d loaded\n%d topples, busiest socket goes off '
                          '%d time(s)\nDEPTH %d  ->  %s'
                      % (cls.upper(), len(B), sum(chips.values()),
                         sum(1 for v in chips.values() if v >= G.THRESH), n,
                         od.get(busiest, 0), dep, cls.upper())))
    cap = ('CYAN RINGS ARE LOADED SOCKETS (two or three chips, about to go off), GREY RINGS ARE '
           'SETTLED ONES - AND THE RINGS ARE THE PANEL\'S, NOT THE PLATE\'S.\n'
           'A settled socket is a single stud and needs no other ink; the reader finds the lattice '
           'by trying all nine and keeping the one that parses.\n'
           'The class is a DEPTH - the greatest number of times any ONE socket has to topple - and '
           'it is the first class identity in the project\n'
           'that is a number of TIMES rather than a number of things. It is an output: run the '
           'plate and look at the busiest socket.')
    _zoom(cells, CW, CHH, '_ZOOM_confluence_piles.png', cap)


def build_weak_zoom():
    """THE ONE STUD CARRYING THE CLASS. An ordinary move changes the picture and nothing else; the
    move at the busiest socket changes the class and nothing else."""
    cls = 'warrior'
    fr, a, _got, salt = _plate(cls)
    _py, _px, _cells, _bc, bc_inv, B, chips = G.compose(a, cls, None, salt)
    end0, od0, n0 = G.stabilise(chips, B, 'first', salt)
    d0 = max(od0.values()) if od0 else 0
    ordinary = spent = None
    for c in sorted([c for c, v in chips.items() if v >= G.THRESH]):
        t = dict(chips)
        t[c] -= G.THRESH
        if not t[c]:
            del t[c]
        for du, dv in G.FIRE:
            q = (c[0] + du, c[1] + dv)
            if q in B:
                t[q] = t.get(q, 0) + 1
        if not G.drawable(a, bc_inv, t) or any(v > G.MAXCHIPS for v in t.values()):
            continue
        e, od, _n = G.stabilise(t, B, 'first', salt)
        dd = max(od.values()) if od else 0
        same = sorted(e.items()) == sorted(end0.items())
        if dd == d0 and ordinary is None:
            ordinary = (t, dd, same, c)
        if dd != d0 and spent is None:
            spent = (t, dd, same, c)
    cells = [(_im(repaint(fr, a, cls, bc_inv, chips)),
              'AS SHIPPED\ndepth %d  ->  WARRIOR' % d0)]
    if ordinary:
        cells.append((_im(repaint(fr, a, cls, bc_inv, ordinary[0])),
                      'AFTER AN ORDINARY MOVE\ndepth %d, destination %s\nstill a WARRIOR'
                      % (ordinary[1], 'unchanged' if ordinary[2] else 'CHANGED')))
    if spent:
        cells.append((_im(repaint(fr, a, cls, bc_inv, spent[0])),
                      'AFTER THE ONE MOVE THAT SPENDS IT\ndepth %d, destination %s\nnow reads as a '
                      '%s' % (spent[1], 'unchanged' if spent[2] else 'CHANGED',
                              {1: 'MAGE', 2: 'RANGER', 3: 'WARRIOR'}.get(spent[1], 'nothing'))))
    cap = ('EVERY LEGAL MOVE OF EVERY PLATE IN THE BATCH WAS ENUMERATED: 1299 moves, and 1299 of '
           'them leave the destination exactly where it was.\n'
           '221 of them spend the class, spread over 221 different plates - so WHERE A PLATE HAS A '
           'WEAK POINT IT HAS EXACTLY ONE, and 156 have none at all.\n'
           'A topple only shortens the journey of the socket it happens at, so the only move that '
           'can change the class is a topple at the socket carrying it.\n'
           'Nothing in the 74th ATTRITION had a weak point of any kind: that is what an invariance '
           'buys, and what a confluence does not.')
    _zoom(cells, CW, CHH, '_ZOOM_confluence_weak.png', cap)


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else None
    if which == 'zoom':
        build_race_zoom()
        build_piles_zoom()
        build_weak_zoom()
        return
    for kind, cfg in SETS.items():
        if which and kind != which:
            continue
        build(kind, cfg)
    if not which:
        build_race_zoom()
        build_piles_zoom()
        build_weak_zoom()


if __name__ == '__main__':
    main()
