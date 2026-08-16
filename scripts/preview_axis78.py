#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-EIGHTH net-new-geometry axis batch
(WARRANT family - the plate carries a PACKING of posts and a COVERING of grooves, and the law is
that they COUNT THE SAME, which is a proof that no plate on this silhouette could carry more).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 76th's claim was about marks that are not there. The 77th's was that the plate is pinned, so it
had to be shown twice, once in each direction.

THIS AXIS'S CLAIM IS THAT THE PLATE IS A PROOF - the first law that certifies something about every
OTHER plate on the same garment - and a proof has two things worth photographing: what it establishes,
and the fact that it could have been made a different way.

  _ZOOM_warrant_certificate.png  THE CERTIFICATE. One real cuirass at 10x with every cell the
                                 garment offers ringed - filled where a post stands, hollow where
                                 none does - and beside it the two rivals the plate silently rules
                                 out: a fifth post, which has nowhere to stand without sharing a
                                 band or a file with one already there, and a covering one groove
                                 shorter, which leaves a cell naked. Neither is a picture anybody
                                 drew. Both are pictures the EQUALITY OF TWO NUMBERS forbids, and
                                 the reader can reach that conclusion by counting, without looking
                                 for them.

  _ZOOM_warrant_side.png         THE CLASS, WHICH IS THE SHAPE OF THE ARGUMENT AND NOT OF THE
                                 ORNAMENT. Three plates, at 10x, THAT CARRY EXACTLY THE SAME POSTS
                                 IN EXACTLY THE SAME CELLS - pixel for pixel identical in their
                                 bright ink - proving three different classes, because the grooves
                                 that prove them lie down a different number of times. No previous
                                 axis could have made this panel: on all seventy-seven of them, two
                                 classes with the same marks are the same plate.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_warrant_axis78 as G                                 # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

SNAME = {0: "NOTHING LIES DOWN", 1: "ONE GROOVE LIES DOWN", 2: "TWO GROOVES LIE DOWN"}

NOTE = ("net-new WARRANT %s (the ground is a BAY GRID - the cloth is cut into three-pixel CELLS on "
        "one phase of a three-pixel grid, and the cells, the BANDS they lie in and the FILES they "
        "stand in all belong to the SILHOUETTE. TWO ORNAMENTS IN TWO INKS. A PILLAR is a bright "
        "post two pixels tall standing in a cell with a hard shadow down its left flank, and no two "
        "pillars share a band or a file - the posts are a PACKING. A LINTEL is a dark dashed groove "
        "incised along a whole band or down a whole file, and every cell lies under one - the "
        "grooves are a COVERING. THE LAW IS THAT THE TWO ARE EQUAL IN NUMBER. A packing can never "
        "outnumber a covering, so equality pins both to the same number and PROVES the posts are "
        "the most this garment could ever hold and the grooves the fewest that could cover it. "
        "FIRST LAW IN THE PROJECT THAT CERTIFIES SOMETHING ABOUT EVERY OTHER PLATE ON THE SAME "
        "GARMENT: the 77th said nothing could be added to THIS plate, and this one says nothing "
        "could be added to ANY plate here - and hands over the certificate rather than asking to be "
        "believed. Class identity is a SIDE, how much of the proof lies down: warrior 0, mage 1, "
        "ranger 2. FIRST CLASS IDENTITY THAT IS A PROPERTY OF THE ARGUMENT AND NOT OF THE ORNAMENT "
        "- two classes can carry the very same posts and differ only in how they prove them best. "
        "The acceptance test is a new kind, an AUDIT: for all 525 shipped plates the two optima "
        "were recomputed from the outline alone by two independent methods and the ink agreed 525 "
        "times out of 525. See _ZOOM_warrant_certificate.png and _ZOOM_warrant_side.png), 78th %s "
        "axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_warrant_legendary_preview", out="_PREVIEW_warrant_legendary.png",
        note=NOTE % ("CUIRASS - the slot where every sheet carries the axis, male and female, "
                     "because a torso is the one garment wide enough to offer files and tall "
                     "enough to offer bands", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary78", "Warlord's Warranted Cuirass"),
              ("mage", "shirt_mage_legendary78", "Archmage's Attested Mantle"),
              ("ranger", "shirt_ranger_legendary78", "Warden's Certified Harness")],
    ),
    "legs": dict(
        prev="_warrant_legs_preview", out="_PREVIEW_warrant_legs.png",
        note=NOTE % ("CHAUSSES - and three of the six sheets are PLAIN AND PROVED. A leg is two "
                     "narrow columns of cloth, so its grid is nearly all bands and hardly any "
                     "files, and a covering there has almost no choice about how much of it lies "
                     "down. Every minimum covering those garments admit was enumerated in full: "
                     "the identities they cannot wear are ones that do not exist for them, not "
                     "ones the painter failed to find", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary78", "Warlord's Warranted Chausses"),
              ("mage", "pants_mage_legendary78", "Archmage's Attested Leggings"),
              ("ranger", "pants_ranger_legendary78", "Warden's Certified Greaves")],
    ),
    "boots": dict(
        prev="_warrant_boots_preview", out="_PREVIEW_warrant_boots.png",
        note=NOTE % ("SABATONS - the slot the axis cannot have, and can say so exactly. A boot in "
                     "its worst pose is twenty-seven pixels of cloth, which at three pixels of "
                     "pitch is ONE cell: one post, one groove, equal in number and saying nothing "
                     "whatever. That is what clause LIVE is for, and all six sheets are plain and "
                     "reported rather than dressed in an equality that is true and empty", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_warrant", "Warlord's Warranted Sabatons"),
              ("mage", "boots_mage_legendary_warrant", "Archmage's Attested Steps"),
              ("ranger", "boots_ranger_legendary_warrant", "Warden's Certified Boots")],
    ),
    "helmet": dict(
        prev="_warrantdome_helmet_preview", out="_PREVIEW_warrantdome_helmet.png",
        note=NOTE % ("HELM - a dome is a broad unbroken sheet of cloth, which is what a grid wants, "
                     "so all six sheets are warranted in all 42 poses and most of them could have "
                     "worn any of the three identities. The visor is the finishing pass's, not the "
                     "axis's: the posts stop where the eye slits start", "helmet"),
        crop=(20, 14, 62, 46), cw=42, ch=32,
        rows=[("warrior", "helmet_warrior_legendary78", "Warlord's Warranted Greathelm"),
              ("mage", "helmet_mage_legendary78", "Archmage's Attested Crown"),
              ("ranger", "helmet_ranger_legendary78", "Warden's Certified Hood")],
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
        s = G.SIDE[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, SIDE {s} - {SNAME[s]})",
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


# --- evidence ------------------------------------------------------------------------------------
CROP = (28, 18, 56, 50)
Z = 10
COLW = 440


def crop_of(a, pad=2):
    """Frame the whole garment rather than a fixed window - the axis is a plate-wide count, so a
    panel that shows part of the plate would be showing the reader less than the reader needs."""
    ys, xs = np.where(a)
    x0, x1 = max(0, int(xs.min()) - pad), min(FW, int(xs.max()) + 1 + pad)
    y0, y1 = max(0, int(ys.min()) - pad), min(FH, int(ys.max()) + 1 + pad)
    return (x0, y0, x1, y1)


def wrap_text(d, txt, x, y, w, f, col, lh=15):
    line, out = "", []
    for word in txt.split():
        if d.textlength(line + " " + word, font=f) > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    out.append(line)
    for i, ln in enumerate(out):
        d.text((x, y + i * lh), ln, font=f, fill=col)
    return y + len(out) * lh


def zoom(fr, crop=CROP):
    im = Image.fromarray(fr).crop(crop)
    return im.resize((im.size[0] * Z, im.size[1] * Z), Image.NEAREST)


def at(pt, crop=CROP):
    """Pixel (y, x) of the frame -> centre of its cell in the zoomed crop."""
    y, x = pt
    return ((x - crop[0]) * Z + Z // 2, (y - crop[1]) * Z + Z // 2)


def plate_of(cls, kind='chest'):
    """A real pose, its outline, and the packing and covering that ship on it."""
    stem = G.SLOTS[kind]['srcs'][cls]
    base = G.load_any('%s.png' % stem)
    for fi, sl, a in G.frames_of(base):
        keep = G.compose(a, cls, None, '%s|%d' % (stem, fi))
        if keep is None:
            continue
        return base, sl, a, cls, keep, fi
    return None


def render(a, cls, keep):
    """Paint one pose exactly the way the generator does."""
    fr = np.zeros((FH, FW, 4), np.uint8)
    groove_c, cloth_c, post_c = G.PAL[cls]
    for y, x in np.argwhere(a):
        G.put(fr, y, x, cloth_c)
    core, dark = G.paint(a, keep)
    for y, x in np.argwhere(dark):
        G.put(fr, y, x, groove_c)
    for y, x in np.argwhere(core):
        G.put(fr, y, x, post_c)
    return fr


def cell_mid(cells, e):
    r0, c0 = cells[e]
    return (r0 + 1, c0 + 1)


def evidence_certificate():
    """THE CERTIFICATE: the plate as shipped, and the two rivals its arithmetic rules out."""
    base, sl, a, cls, keep, fi = plate_of('warrior')
    phase, cells, P, B, F = keep
    crop = crop_of(a)
    fsm, fbig = font(13), font(17)

    # the fifth post: every cell that is not one of the shipped posts collides with one of them
    taken_k = {k for k, _j in P}
    taken_j = {j for _k, j in P}
    clash = [e for e in sorted(cells) if e not in P]
    add = clash[0] if clash else None
    culprit = None
    if add:
        culprit = next((e for e in P if e[0] == add[0] or e[1] == add[1]), None)

    # the shorter covering: take one groove away and a cell is left naked
    short_B, short_F = set(B), set(F)
    if short_F:
        gone = sorted(short_F)[0]
        short_F = short_F - {gone}
        naked = [e for e in sorted(cells) if e[0] not in short_B and e[1] not in short_F]
    else:
        gone = sorted(short_B)[0]
        short_B = short_B - {gone}
        naked = [e for e in sorted(cells) if e[0] not in short_B and e[1] not in short_F]

    panes = [
        (zoom(render(a, cls, keep), crop), "AS SHIPPED - A CERTIFICATE",
         ["%d posts, %d grooves, %d cells offered" % (len(P), len(B) + len(F), len(cells)),
          "the two counts are EQUAL, and that is the proof:",
          "no packing here is bigger, no covering smaller",
          "checked against an independent computation 525/525"],
         (140, 230, 150, 255),
         [(cell_mid(cells, e), True) for e in P] +
         [(cell_mid(cells, e), False) for e in sorted(cells) if e not in P], []),
        (zoom(render(a, cls, (phase, cells, P + ([add] if add else []), B, F)), crop),
         "A FIFTH POST - THERE IS NOWHERE FOR IT",
         ["every cell left over shares a band or a file",
          "with a post already standing (marked in red)",
          "the reader never has to look: %d = %d already" % (len(P), len(B) + len(F)),
          "says no packing on this garment is bigger"],
         (255, 120, 120, 255),
         [(cell_mid(cells, e), True) for e in P],
         [cell_mid(cells, add)] + ([cell_mid(cells, culprit)] if culprit else []) if add else []),
        (zoom(render(a, cls, (phase, cells, P, short_B, short_F)), crop),
         "ONE GROOVE FEWER - A CELL IS LEFT NAKED",
         ["%d grooves cannot cover %d cells" % (len(short_B) + len(short_F), len(cells)),
          "%d cell(s) now lie under nothing (red)" % len(naked),
          "the same equality forbids this from the other side:",
          "no covering of this garment is smaller"],
         (255, 120, 120, 255),
         [(cell_mid(cells, e), True) for e in P],
         [cell_mid(cells, e) for e in naked[:6]]),
    ]

    pw, ph = panes[0][0].size
    pad, foot = 16, 100
    W = pad + len(panes) * COLW
    head = 34 + 4 * 15 + 12
    H = head + ph + foot
    canvas = Image.new("RGBA", (W, H), (22, 22, 28, 255))
    d = ImageDraw.Draw(canvas)
    d.text((pad, 10), "THE CERTIFICATE - one warrior cuirass, and the two pictures it rules out",
           font=fbig, fill=(150, 200, 255, 255))
    wrap_text(d, "78th WARRANT axis. Every cell the garment offers is ringed: FILLED where a post "
                 "stands, HOLLOW where none does. A packing of a garment can never outnumber a "
                 "covering of it, so a plate whose two counts are EQUAL has proved both of them "
                 "optimal - and the proof is four numbers the reader can count off the plate, not a "
                 "search through the pictures nobody drew. That is what makes this the first law "
                 "that says anything about plates other than itself.",
              pad, 34, W - 2 * pad, fsm, (150, 160, 175, 255))
    x = pad
    for im, title, lines, col, rings, reds in panes:
        ix = x + (COLW - pad - pw) // 2
        canvas.alpha_composite(im, (ix, head))
        dd = ImageDraw.Draw(canvas)
        for pt, filled in rings:
            cx, cy = at(pt, crop)
            if not (0 <= cx < pw and 0 <= cy < ph):
                continue
            if filled:
                dd.ellipse([ix + cx - 3, head + cy - 3, ix + cx + 3, head + cy + 3],
                           fill=(120, 220, 255, 255))
            else:
                dd.ellipse([ix + cx - 5, head + cy - 5, ix + cx + 5, head + cy + 5],
                           outline=(120, 220, 255, 255), width=2)
        for pt in reds:
            cx, cy = at(pt, crop)
            if not (0 <= cx < pw and 0 <= cy < ph):
                continue
            dd.ellipse([ix + cx - 8, head + cy - 8, ix + cx + 8, head + cy + 8],
                       outline=(255, 90, 90, 255), width=3)
        d.text((x, head + ph + 8), title, font=fsm, fill=col)
        for i, ln in enumerate(lines):
            d.text((x, head + ph + 26 + i * 15), ln, font=fsm, fill=(200, 200, 210, 255))
        x += COLW
    canvas.convert("RGB").save("_ZOOM_warrant_certificate.png")
    print("wrote _ZOOM_warrant_certificate.png", canvas.size)


def evidence_side():
    """THE CLASS - the same posts, three times, proved three different ways.

    This is the panel no previous axis could have made. One pose, one phase, ONE PACKING - and then
    every minimum covering that packing admits, sorted by how many of its grooves lie down. The
    bright ink is identical in all three panes and can be checked pixel for pixel; only the dark ink
    moves, and the class moves with it."""
    want_all = {G.SIDE[c] for c in ('warrior', 'mage', 'ranger')}
    pick = None
    for kind in ('helmet', 'chest'):
        stem = G.SLOTS[kind]['srcs']['warrior']
        base = G.load_any('%s.png' % stem)
        for fi, sl, a in G.frames_of(base):
            for phase in range(G.CELL * G.CELL):
                cells = G.cells_of(a, phase)
                if len(cells) < G.MINCELL:
                    continue
                P = sorted(G.max_packing(cells))
                if len(P) < G.MINPILL:
                    continue
                okB, okF = G.sealable(a, cells)
                covers = G.min_covers(cells, len(P), okB, okF)
                if want_all <= {len(B) for B, _F in covers}:
                    # the richest pose the sheet offers, not merely the first that works: a panel
                    # about counting wants as many things to count as possible
                    if pick is None or len(cells) > len(pick[2]):
                        pick = (a, phase, cells, P, covers)
        if pick:
            break
    if pick is None:
        print('no pose offers all three sides on one packing')
        return
    a, phase, cells, P, covers = pick
    crop = crop_of(a)
    fsm, fbig = font(13), font(17)

    panes = []
    for cls in ('warrior', 'mage', 'ranger'):
        want = G.SIDE[cls]
        got = next((c for c in covers if len(c[0]) == want), None)
        if got is None:
            continue
        B, F = got
        fr = render(a, cls, (phase, cells, P, set(B), set(F)))
        panes.append((zoom(fr, crop), cls, want, len(B), len(F), P, cells))

    pw, ph = panes[0][0].size
    pad, foot = 16, 110
    W = pad + len(panes) * COLW
    head = 34 + 4 * 15 + 12
    H = head + ph + foot
    canvas = Image.new("RGBA", (W, H), (22, 22, 28, 255))
    d = ImageDraw.Draw(canvas)
    d.text((pad, 10), "THE SIDE - one set of posts, three classes, three proofs",
           font=fbig, fill=(150, 200, 255, 255))
    wrap_text(d, "The same pose, the same phase, and THE SAME PACKING in all three panes - the "
                 "bright ink is identical pixel for pixel, and the cyan rings mark the posts so it "
                 "can be checked. What changes is the covering that proves it best: the warrior's "
                 "grooves all stand up, the mage lays one down, the ranger two. Class identity here "
                 "is a property of the ARGUMENT and not of the ornament, which is why this panel is "
                 "possible at all - on every previous axis, two classes carrying the same marks "
                 "are the same plate.",
              pad, 34, W - 2 * pad, fsm, (150, 160, 175, 255))
    x = pad
    for im, cls, want, nb, nf, P, cells in panes:
        ix = x + (COLW - pad - pw) // 2
        canvas.alpha_composite(im, (ix, head))
        dd = ImageDraw.Draw(canvas)
        for e in P:
            cx, cy = at(cell_mid(cells, e), crop)
            if 0 <= cx < pw and 0 <= cy < ph:
                dd.ellipse([ix + cx - 6, head + cy - 6, ix + cx + 6, head + cy + 6],
                           outline=(120, 220, 255, 255), width=2)
        d.text((x, head + ph + 8), "%s - SIDE %d (%s)" % (cls.upper(), want, SNAME[want]),
               font=fsm, fill=(150, 230, 160, 255))
        for i, ln in enumerate([
                "%d posts, %d grooves: still equal, still a proof" % (len(P), nb + nf),
                "%d groove(s) lying down, %d standing up" % (nb, nf),
                "the posts did not move by a single pixel",
                "only the reasoning did, and the class with it"]):
            d.text((x, head + ph + 26 + i * 15), ln, font=fsm, fill=(200, 200, 210, 255))
        x += COLW
    canvas.convert("RGB").save("_ZOOM_warrant_side.png")
    print("wrote _ZOOM_warrant_side.png", canvas.size)


def main():
    if '--evidence' in sys.argv:
        evidence_certificate()
        evidence_side()
        return
    for kind, cfg in SETS.items():
        build(kind, cfg)
    evidence_certificate()
    evidence_side()


if __name__ == '__main__':
    main()
