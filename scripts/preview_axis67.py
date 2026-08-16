#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-SEVENTH net-new-geometry axis batch
(COLOPHON family — the plate is ruled into registers and the registers COUNT THEMSELVES).

*** THE DELIVERABLE, AND WHY IT HAS TWO EXTRA PANELS. ***
The 64th could not be judged by an eye because an eye cannot take an exclusive-or, so its evidence
became a DECODE. The 66th's claim was a negative — that nothing can be carried away — and a negative
has no picture, so its evidence became a DISASSEMBLY. This axis's claim is a SENTENCE THE PLATE SAYS
ABOUT ITSELF, and a sentence has no picture either. So the evidence is the READING and the LIE:

  _ZOOM_colophon_census.png    One real cuirass, magnified, with every register bracketed and its
                               bosses counted — and beside it the plate's own sentence checked
                               against the plate, register by register. This is the whole axis on one
                               sheet of paper: "two registers hold none, none holds one, two hold
                               two", and the plate has exactly two empty registers, no register with
                               one boss, and two registers of two.

  _ZOOM_colophon_lies.png      THE SAME CUIRASS FOUR TIMES: as shipped, and then as UNIFORM,
                               PERMUTED and OFFBYONE — three plates with the same ruling, the same
                               relief, the same palette and very nearly the same pixel count, every
                               one of which says something FALSE about itself. If you cannot tell
                               them apart, that is the finding: the difference between this axis and
                               a row of studs is not a look, it is an ARITHMETIC, and it took 630
                               plates and 3219 struck bosses to be sure of it.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_colophon_axis67 as G                               # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new COLOPHON %s (the plate is RULED INTO REGISTERS and the number of raised BOSSES in "
        "register i is the number of registers holding exactly i bosses - THE PLATE IS A CENSUS OF "
        "ITSELF. FIRST AXIS WHOSE INVARIANT THE PLATE ITSELF ASSERTS: every predecessor is a "
        "sentence WE say about the pixels, this one is a sentence the PIXELS say, and it is the "
        "first plate in 67 axes that could be FALSE. The acceptance test is a SELF-AUDIT - it reads "
        "the claim off the plate and checks the plate against it, consulting nothing outside. Class "
        "identity is A NUMBER THAT DESCRIBES ITSELF: warrior 2020, mage 21200, ranger 1210 - and "
        "clause EXHAUSTION proves those are ALL THERE ARE. See _ZOOM_colophon_census.png and "
        "_ZOOM_colophon_lies.png), 67th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_colophon_legendary_preview", out="_PREVIEW_colophon_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary67", "Warlord's Colophon Cuirass"),
              ("mage", "shirt_mage_legendary67", "Archmage's Self-Told Mantle"),
              ("ranger", "shirt_ranger_legendary67", "Warden's Tallied Jerkin")],
    ),
    "legs": dict(
        prev="_colophon_legs_preview", out="_PREVIEW_colophon_legs.png",
        note=NOTE % ("CHAUSSES - and note that ONE REGISTER RUNS ACROSS BOTH LEGS: the census is of "
                     "the GARMENT, so a boss on the left leg and a boss on the right are two bosses "
                     "in ONE register", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary67", "Warlord's Colophon Chausses"),
              ("mage", "pants_mage_legendary67", "Archmage's Self-Told Leggings"),
              ("ranger", "pants_ranger_legendary67", "Warden's Tallied Chausses")],
    ),
    "boots": dict(
        prev="_colophon_boots_preview", out="_PREVIEW_colophon_boots.png",
        note=NOTE % ("SABATONS - AND THE AXIS'S OWN LIMIT, WHICH IS A THEOREM AND NOT A PIXEL "
                     "COUNT: THERE IS NO SELF-DESCRIPTIVE WORD OF LENGTH THREE (all 27 candidates "
                     "enumerated, none works), and a pair of sabatons holds three registers. So the "
                     "boots of all three classes are RULED AND LEFT EMPTY - this axis's own BLANK "
                     "control worn as an item, reported and never faked. The 66th's joint missed a "
                     "sabaton by a pixel; this one misses by a THEOREM",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_colophon", "Warlord's Colophon Sabatons"),
              ("mage", "boots_mage_legendary_colophon", "Archmage's Self-Told Striders"),
              ("ranger", "boots_ranger_legendary_colophon", "Warden's Tallied Boots")],
    ),
    "helmet": dict(
        prev="_colophondome_helmet_preview", out="_PREVIEW_colophondome_helmet.png",
        note=NOTE % ("HELM - and the slot that decided which class got which word: the ranger's "
                     "hood is six rows tall and holds four registers read across the brow, and "
                     "2020 (two registers of two bosses) will not fit in it, so the ranger's word "
                     "is 1210",
                     "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary67", "Warlord's Colophon Helm"),
              ("mage", "helmet_mage_legendary67", "Archmage's Self-Told Crown"),
              ("ranger", "helmet_ranger_legendary67", "Warden's Tallied Hood")],
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
        word = ''.join(map(str, G.WORDS[cls]))
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, word {word})",
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


def _zoom(cells, crop, Z, out, caption=None):
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad = 10
    nlines = len(caption.split('\n')) if caption else 0
    extra = 16 * nlines + 8 if caption else 0
    wide = max(len(ln) for ln in caption.split('\n')) * 8 + 2 * pad if caption else 0
    canvas = Image.new("RGBA", (max(pad + len(cells) * (cw + pad), wide),
                                pad + chh + 22 + extra),
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
        im = frame(_open(f"_colophon_legendary_preview/shirt_{c}_legendary67.png"), 0).crop(crop)
        cells.append((im, f"{c} chest idle f0  (word {''.join(map(str, G.WORDS[c]))})"))
    _zoom(cells, crop, 10, "_ZOOM_colophon_chest.png",
          caption="a GROOVE opens each register and crosses the whole piece; a BOSS is two pixels of\n"
                  "crest on the register's mid field. Where a boss sits inside its register means\n"
                  "NOTHING (clause INDIFFERENCE re-drives 2622 of 2730 of them and the plate says the\n"
                  "same word); which register it is in means EVERYTHING.")


def build_head_zoom():
    crop = (30, 14, 52, 36)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        im = frame(_open(f"_colophondome_helmet_preview/helmet_{c}_legendary67.png"), 0).crop(crop)
        cells.append((im, f"{c} helm f0 (word {''.join(map(str, G.WORDS[c]))})"))
    _zoom(cells, crop, 12, "_ZOOM_colophon_head.png",
          caption="the domes are ruled ACROSS THE BROW where the skull is too short to take four\n"
                  "registers the other way - and the reader is not told which way any piece runs. It\n"
                  "tries both readings and takes the one that IS a ruling; 0 of 630 plates admitted\n"
                  "two. The visor's black eye and mouth slits come from the finishing pass, untouched.")


def _plate(cls, mode=None, fi=0, kind="chest"):
    """One real plate, built through the generator, before the finishing pass."""
    cfg = G.SLOTS[kind]
    base = G.load_any('%s.png' % cfg['srcs'][cls])
    for f, sl, a in G.frames_of(base, cfg):
        if f != fi:
            continue
        fr, painted = G.one_plate(base, sl, a, cfg, cls, mode)
        return fr, painted, a
    return None, None, None


def build_census_zoom():
    """THE AXIS'S REAL EVIDENCE: the plate's own sentence, checked against the plate."""
    cls, Z = "warrior", 14
    fr, painted, a = _plate(cls)
    p, bands, counts, bosses = painted[0]
    crop = (p.x0 - 1, p.y0 - 1, p.x1 + 2, p.y1 + 2)
    im = Image.fromarray(fr).crop(crop)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    marked = im.resize((cw, chh), Image.NEAREST).convert("RGBA")
    d = ImageDraw.Draw(marked)
    # bracket every register and count its bosses, in the plate's own coordinates
    for bi, (r0, r1) in enumerate(bands):
        ys = [p.to_frame(r, 0)[0] for r in (r0, r1)]
        y0 = (min(ys) - crop[1]) * Z
        y1 = (max(ys) + 1 - crop[1]) * Z
        d.rectangle([1, y0 + 1, cw - 2, y1 - 2], outline=(255, 210, 90, 255), width=2)
        d.text((5, y0 + 3), "reg %d : %d" % (bi, counts[bi]), font=font(15),
               fill=(255, 210, 90, 255))
    word = tuple(counts)
    got = G.read_piece(fr, a, G.SLOTS['chest']['largest'])
    lines = ["THE PLATE'S OWN SENTENCE, read off the pixels by a reader told nothing: %s"
             % ''.join(map(str, got[0])),
             ""]
    for i in range(len(word)):
        n = sum(1 for c in word if c == i)
        lines.append("   register %d holds %d boss%-3s and %d register%s hold%s exactly %d   -> %s"
                     % (i, word[i], 'es' if word[i] != 1 else '', n,
                        's' if n != 1 else '', '' if n != 1 else 's', i,
                        'TRUE' if word[i] == n else 'FALSE'))
    lines += ["",
              "   the digits sum to %d and the word is %d long - a THEOREM of self-description, not"
              % (sum(word), len(word)),
              "   an input, and verified for every solution clause EXHAUSTION finds.",
              "   Strike any one of these bosses out and the sentence becomes false: 0 of 3219",
              "   struck plates in the batch survived. NOTHING IN THIS ORNAMENT IS ORNAMENT."]
    _zoom([(marked, "%s cuirass idle f0, word %s" % (cls, ''.join(map(str, word))))],
          (0, 0, (crop[2] - crop[0]), (crop[3] - crop[1])), Z,
          "_ZOOM_colophon_census.png", caption="\n".join(lines))


def build_lies_zoom():
    """The same cuirass, once true and three times false, at the same magnification."""
    cls, Z = "warrior", 12
    cells = []
    order = [(None, "AS SHIPPED"), ("uniform", "UNIFORM"), ("permuted", "PERMUTED"),
             ("offbyone", "OFFBYONE")]
    crop = None
    for mode, label in order:
        fr, painted, a = _plate(cls, mode)
        if painted is None:
            continue
        p = painted[0][0]
        if crop is None:
            crop = (p.x0 - 1, p.y0 - 1, p.x1 + 2, p.y1 + 2)
        got = G.read_piece(fr, a, True)
        w = ''.join(map(str, got[0])) if got else '??'
        ok = "TRUE" if got and G.is_descriptive(got[0]) else "FALSE"
        cells.append((Image.fromarray(fr).crop(crop), "%s  %s  %s" % (label, w, ok)))
    _zoom(cells, (0, 0, crop[2] - crop[0], crop[3] - crop[1]), Z, "_ZOOM_colophon_lies.png",
          caption="Same ruling, same relief, same palette, within one boss of the same pixel count.\n"
                  "One of these four plates is telling the truth about itself. UNIFORM (one boss per\n"
                  "register) is the 13th STUDWORK and the 40th DENTIL and would have to read 0400;\n"
                  "PERMUTED has the axis's exact multiset of counts in the wrong registers; OFFBYONE\n"
                  "is one boss short. Measured over the batch: 630, 595 and 630 false plates.\n"
                  "IF YOU CANNOT TELL THEM APART BY EYE, THAT IS THE FINDING.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_census_zoom()
    build_lies_zoom()


if __name__ == "__main__":
    main()
