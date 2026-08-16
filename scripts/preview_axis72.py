#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-SECOND net-new-geometry axis batch
(QUORUM family - the ornament is a set of SHARES OF A SECRET and the law is that k of them say it
and k-1 of them say nothing).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 67th's was a sentence, so
its evidence became a READING. The 68th's was that nothing repeats, so its evidence became a
HISTOGRAM. The 69th's was that nobody drew the ornament, so its evidence was the poles ringed. The
70th's was about motion, so its evidence was the seed cycle traced. The 71st's could not be seen at
all, so its evidence was the reckoning set out in full.
THIS AXIS'S CLAIM IS HALF A FACT AND HALF A NON-EVENT, so it takes two panels and they are not the
same kind of panel:

  _ZOOM_quorum_shares.png      One real cuirass per class at 10x with every rod's TOP-LEFT END
                               ringed in gold and its BEAD ringed in white, and beside each the
                               shares the reader lifts off the pixels, the class it reads out of
                               their degree, and the secret every quorum of them agrees on. This is
                               the half that can be shown.

  _ZOOM_quorum_ignorance.png   The same mage cuirass and, beside it, THE WHOLE INTERROGATION: every
                               below-quorum subset of its shares, and against each one the list of
                               secrets that are still standing afterwards. Four out of five, every
                               time, one plate apiece. This is the half that cannot be shown, so
                               what is shown instead is the COUNT OF WHAT SURVIVES - the only way an
                               absence of knowledge has ever been put on a panel in this project.

  _ZOOM_quorum_controls.png    The same cuirass four ways: as shipped, FLAT (every bead level - the
                               secret is still 3 and any ONE rod now tells you so), SHORT (one rod
                               short of a quorum: not wrong, unanswerable) and CROWDED (the rods
                               allowed to touch, so two of them become one figure of ten pixels and
                               the reader refuses the plate rather than misreading it).

Nothing here touches sprites/preview_assets/char or git."""
import itertools
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_quorum_axis72 as G                                 # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

KNAME = {4: "FOUR RODS MUST AGREE", 3: "THREE RODS MUST AGREE", 2: "TWO RODS MUST AGREE"}

NOTE = ("net-new QUORUM %s (the ornament is a SET OF SHARES OF A SECRET. Each rod is a straight run "
        "of exactly five pixels and exactly one of them is a bead; the bead's POSITION along the "
        "rod, counted from its top-left end, is the number that rod holds, and the rods are ranked "
        "top to bottom so the highest is share 1. The law is that the shares lie on a polynomial "
        "over GF(5) of degree exactly k-1 whose value at zero is THE SECRET, which is 3 on every "
        "plate of every class in the wardrobe - and the secret's own place, x = 0, is the one place "
        "the ornament deliberately leaves empty. FIRST INVARIANT THAT TREATS TWO READERS "
        "DIFFERENTLY: seventy-one axes say the same thing to everybody who looks, and this one's "
        "answer depends on HOW MUCH OF THE PLATE THE READER HOLDS. Hold k rods and the secret is "
        "yours; hold k-1 and four of the five secrets are still standing, one plate apiece, so the "
        "best you can do is one guess in four. The acceptance test is an INTERROGATION and half of "
        "it looks for a non-result: clause IGNORANCE is the first clause in the project that passes "
        "by FINDING something - four surviving explanations - rather than by finding nothing wrong. "
        "Class identity is THE SIZE OF A COALITION: warrior 4, ranger 3, mage 2, and it is the "
        "first class that is a property of the plate's READERS rather than of the plate. Exact "
        "complement of the 67th COLOPHON, which was the first plate that could lie; this is the "
        "first plate that can refuse to answer. See _ZOOM_quorum_shares.png, "
        "_ZOOM_quorum_ignorance.png and _ZOOM_quorum_controls.png)"
        ", 72nd %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_quorum_legendary_preview", out="_PREVIEW_quorum_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary72", "Warlord's Fourfold Seal Cuirass"),
              ("mage", "shirt_mage_legendary72", "Archmage's Two-Witness Mantle"),
              ("ranger", "shirt_ranger_legendary72", "Warden's Threefold Seal Jerkin")],
    ),
    "legs": dict(
        prev="_quorum_legs_preview", out="_PREVIEW_quorum_legs.png",
        note=NOTE % ("CHAUSSES - and note that THE SECRET IS SPLIT ACROSS THE WHOLE GARMENT, NOT "
                     "ACROSS EACH PART. A suit of two greaves holds one secret between them, so "
                     "either greave on its own is below quorum and knows nothing. That is the axis "
                     "stating its own law about its own halves, and it is the reason the rods are "
                     "laid out over the whole plate at once", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary72", "Warlord's Fourfold Seal Chausses"),
              ("mage", "pants_mage_legendary72", "Archmage's Two-Witness Leggings"),
              ("ranger", "pants_ranger_legendary72", "Warden's Threefold Seal Greaves")],
    ),
    "boots": dict(
        prev="_quorum_boots_preview", out="_PREVIEW_quorum_boots.png",
        note=NOTE % ("SABATONS - and this is the slot where the class's own definition decides who "
                     "gets an ornament, IN THE ORDER OF THE QUORUM. Everywhere else in this project "
                     "a class needs a minimum because of what its number is worth; here the minimum "
                     "IS the class, since a warrior means four rods and four five-pixel rods a "
                     "pixel apart will not go on a sabaton at any attempt. Measured: the mage "
                     "(k=2) is dressed on the female sheet in all 42 poses and on the male in 30 "
                     "of 35; the ranger (k=3) is dressed on the female and reaches 10 of 35 on the "
                     "male; the warrior (k=4) reaches none. Three sheets are therefore PLAIN AND "
                     "REPORTED and they are plain in exactly the order the class numbers predict",
                     "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_quorum", "Warlord's Fourfold Seal Sabatons"),
              ("mage", "boots_mage_legendary_quorum", "Archmage's Two-Witness Steps"),
              ("ranger", "boots_ranger_legendary_quorum", "Warden's Threefold Seal Boots")],
    ),
    "helmet": dict(
        prev="_quorumdome_helmet_preview", out="_PREVIEW_quorumdome_helmet.png",
        note=NOTE % ("HELM - and the dome is the kindest surface in the batch, because a rod needs "
                     "five pixels in a straight line and a skull offers them in four directions at "
                     "once. The warrior's helm carries all four rods in all 42 poses; the ranger's "
                     "hood settles at three, which is its quorum exactly, so on that sheet EVERY "
                     "ROD IS LOAD-BEARING and losing any one of them would leave the plate "
                     "unreadable rather than merely poorer", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary72", "Warlord's Fourfold Seal Helm"),
              ("mage", "helmet_mage_legendary72", "Archmage's Two-Witness Crown"),
              ("ranger", "helmet_ranger_legendary72", "Warden's Threefold Seal Hood")],
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
        k = G.K[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, quorum k = {k} - {KNAME[k]})",
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
    # A cell is as wide as its picture OR as its label, whichever is wider. The first draft sized
    # the columns off the picture alone and the warrior's interrogation ran off the right edge of
    # the panel, which is the one place in this batch a reader would look for it.
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


def build_shares_zoom():
    """THE READING. Gold is the rod's top-left end - the pixel the reader counts from, fixed by the
    picture and not by the painter - and white is the bead, whose distance from the gold ring IS the
    number that rod holds."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for cls in ("warrior", "ranger", "mage"):
        fr, a, _got, salt = _plate(cls)
        rods, vals = G.compose(a, cls, None, salt)
        rod, bead, _dark = G.paint(a, rods, vals)
        shares = G.recover(a, rod, bead)
        im = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
        d = ImageDraw.Draw(im)
        for px, v in zip(rods, vals):
            for p, col in ((px[0], (255, 220, 90, 255)), (px[v % G.ROD], (255, 255, 255, 255))):
                cx = (p[1] - crop[0]) * Z + Z // 2
                cy = (p[0] - crop[1]) * Z + Z // 2
                d.ellipse([cx - Z, cy - Z, cx + Z, cy + Z], outline=col, width=2)
        k = G.K[cls]
        deg = G.degree_of(G.interp_coefs(shares))
        secrets = sorted({G.lagrange0(list(s)) for s in itertools.combinations(shares, k)})
        lines = ["%s   %d rods" % (cls, len(shares)),
                 "shares " + " ".join("f(%d)=%d" % s for s in shares),
                 "degree %d  ->  k = %d (the CLASS, read off)" % (deg, deg + 1),
                 "all %d quorums agree: secret = %s"
                 % (len(list(itertools.combinations(shares, k))),
                    secrets[0] if len(secrets) == 1 else secrets)]
        cells.append((im, "\n".join(lines)))
    _zoom(cells, cw, chh, "_ZOOM_quorum_shares.png",
          caption="THE HALF OF THE LAW THAT CAN BE SHOWN. Gold rings the rod's TOP-LEFT END and\n"
                  "white rings its BEAD; the number of pixels between them is the number that rod\n"
                  "holds, and the rods are ranked top to bottom so the highest is share 1. Nothing\n"
                  "tells the reader which rod was drawn first, only which lies higher - the rank is\n"
                  "a fact about the picture. Interpolate the shares over GF(5) and the DEGREE names\n"
                  "the class (3 -> warrior, 2 -> ranger, 1 -> mage): the class is an OUTPUT, nobody\n"
                  "is told it. Evaluate at zero and every quorum of k rods agrees on 3, the secret\n"
                  "every plate in this wardrobe keeps - and x = 0 is the one abscissa with no rod\n"
                  "on it, so THE ONE THING THE PLATE IS ABOUT IS THE ONE PLACE IT LEAVES EMPTY.\n"
                  "The other half of the law is on _ZOOM_quorum_ignorance.png, because it is a\n"
                  "non-event and there is no picture of it.")


def build_ignorance_zoom():
    """THE INTERROGATION. There is no picture of an absence, so what is drawn is the COUNT OF WHAT
    SURVIVES: every below-quorum subset of a real plate and, against each, the secrets it is still
    consistent with."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for cls in ("mage", "ranger", "warrior"):
        fr, a, _got, salt = _plate(cls)
        rods, vals = G.compose(a, cls, None, salt)
        rod, bead, _dark = G.paint(a, rods, vals)
        shares = G.recover(a, rod, bead)
        k = G.K[cls]
        im = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
        lines = ["%s, quorum %d - a reader holding %d rod%s:"
                 % (cls, k, k - 1, "" if k == 2 else "s")]
        for sub in list(itertools.combinations(shares, k - 1))[:4]:
            surv = G.surviving_secrets(list(sub), k)
            denied = [t for t in range(G.P) if t not in surv]
            lines.append("  %s -> still %s, ruled out %s"
                         % (" ".join("f(%d)=%d" % s for s in sub),
                            sorted(surv), denied))
        lines.append("  every survivor by exactly ONE plate: %s"
                     % ("yes" if all(set(G.surviving_secrets(list(s), k).values()) == {1}
                                     for s in itertools.combinations(shares, k - 1)) else "no"))
        cells.append((im, "\n".join(lines)))
    _zoom(cells, cw, chh, "_ZOOM_quorum_ignorance.png",
          caption="THE HALF OF THE LAW THAT CANNOT BE SHOWN, SO IT IS COUNTED INSTEAD. Each list is\n"
                  "every secret still standing after a reader has taken all the plate would give a\n"
                  "coalition one short of the quorum. FOUR OUT OF FIVE SURVIVE, EACH BY EXACTLY ONE\n"
                  "PLATE THIS AXIS WOULD HAVE DRAWN, so below quorum the best any reader can do is\n"
                  "one guess in four. This is the first clause in seventy-two axes that passes by\n"
                  "FINDING something rather than by finding nothing wrong - it fails if it counts\n"
                  "three survivors, not if it counts a violation.\n"
                  "THE FIFTH SECRET IS DENIED, AND THE FILE WILL NOT ROUND THAT AWAY. Shamir's\n"
                  "scheme is perfectly secret when the polynomial may have any leading coefficient;\n"
                  "this axis insists the degree be exactly k-1, because a degenerate plate would be\n"
                  "readable by fewer rods than its class admits. That insistence costs one\n"
                  "candidate - the one that would flatten the polynomial - and so the axis buys\n"
                  "clause DEGREE for log2(5/4) of a bit and says so out loud.")


def build_controls_zoom():
    """The same cuirass four ways, and only one of them is a plate this axis would ship."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for mode, name in ((None, "QUORUM (shipped)\nk=3, secret 3"),
                       ('flat', "FLAT\nevery bead level: quorum of ONE"),
                       ('short', "SHORT\none rod below quorum"),
                       ('crowded', "CROWDED\nrods allowed to touch")):
        fr, a, got, _salt = _plate('ranger', mode)
        if fr is None or got is None:
            continue
        cells.append((Image.fromarray(fr).crop(crop), name))
    _zoom(cells, cw, chh, "_ZOOM_quorum_controls.png",
          caption="ONE RANGER CUIRASS, FOUR WAYS, ONE PAINTER, ONE PALETTE, ONE KIND OF RELIEF.\n"
                  "FLAT lays every bead at the same index. It is NOT WRONG ABOUT THE SECRET - the\n"
                  "constant polynomial still reads 3 - it is wrong about WHO MAY HAVE IT, because a\n"
                  "constant is degree 0 and one rod now tells a reader everything. That is what\n"
                  "clause DEGREE is for, and it is the only clause in the axis that guards a\n"
                  "threshold rather than a value: 0 of 40 flat plates get through.\n"
                  "SHORT draws k-1 rods and stops. Nothing on it is false; it simply cannot be\n"
                  "asked, and clause DISTINCT refuses it before the secret comes up at all - the\n"
                  "plate keeps its secret from everybody, its own maker included.\n"
                  "CROWDED switches off the one-pixel gap. Where two rods meet, the reader finds a\n"
                  "single crest figure ten pixels long, and a rod is five: it does not misread the\n"
                  "shares, IT FINDS NONE. Twenty-four of forty-three are caught, and the nineteen\n"
                  "that are not are simply plates whose rods happened not to collide.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_shares_zoom()
    build_ignorance_zoom()
    build_controls_zoom()


if __name__ == "__main__":
    main()
