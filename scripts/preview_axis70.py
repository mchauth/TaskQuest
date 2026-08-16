#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTIETH net-new-geometry axis batch
(TRUSS family - the ornament is a BAR FRAMEWORK and the law is how many ways it could move).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 67th's was a sentence, so
its evidence became a READING. The 68th's was that nothing repeats, so its evidence became a
HISTOGRAM. The 69th's was that nobody drew the ornament, so its evidence was the poles ringed.
THIS AXIS'S CLAIM IS ABOUT MOTION, AND NOTHING ON THE PLATE MOVES - so its evidence is the two
things you would need in order to disbelieve it:

  _ZOOM_truss_seed.png      One real cuirass per class at 10x with the JOINTS RINGED and the SEED
                            CYCLE traced. A triangle, a quadrilateral, a pentagon: the class is the
                            number of sides of the one closed circuit the framework was started
                            from, and every later bar in the piece changes nothing about how free
                            it is. You can count the class without being told it.

  _ZOOM_truss_controls.png  THE SAME CUIRASS FOUR TIMES: as shipped, then TREE (which is the 66th
                            DOVETAIL's own structure), GRID (the 14th LATTICE) and TRELLIS (the
                            20th). Same painter, same palette, same relief, same pixel budget.
                            Three of them are false, and the two nearest visual neighbours in the
                            whole project fail for OPPOSITE reasons: the 14th is a mechanism in
                            every cell it has, and the 20th is rigid several times over.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_truss_axis70 as G                                  # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

SEEDNAME = {0: "TRIANGLE", 1: "QUADRILATERAL", 2: "PENTAGON"}

NOTE = ("net-new TRUSS %s (the ornament is a BAR FRAMEWORK - joints on the piece's own mask, "
        "straight struts between them, each strut with its own dark witness - and the law is not "
        "about where the bars are but about WHAT THE FIGURE WOULD DO IF YOU PUSHED IT: the "
        "rigidity matrix has a kernel of exactly 3 + k, three of which are the plane's own "
        "translations and rotation. FIRST INVARIANT THAT IS A BEHAVIOUR RATHER THAN A FACT - every "
        "one of the 69 axes before it states something true of the pixels as they lie, and this "
        "one states something about velocities that are never given to it. Exact complement of the "
        "66th DOVETAIL, whose law is that no part can be REMOVED; here no part can MOVE, and the "
        "66th's own spanning tree is control TREE, which scores n-2 motions instead of k because "
        "CONNECTED IS NOT RIGID. The acceptance test is a FLEX: the reader recovers the joints and "
        "bars off the pixels, writes down the rigidity matrix and takes its RANK - the first "
        "acceptance test in the project that is linear algebra on the plate's own coordinates, and "
        "the first whose verdict changes if the ornament is drawn the same but PLACED differently "
        "(control COLLINEAR). Class identity is THE FREEDOM OF THE SEED: warrior a triangle that "
        "cannot move, ranger a quadrilateral that can lozenge one way, mage a pentagon that can "
        "lozenge two - and every later joint is a Henneberg type-I extension, so THE ORNAMENT "
        "GROWS WITHOUT EVER CHANGING HOW FREE IT IS. No pitch, no lattice, no phase: one irregular "
        "figure per part, sized to the part. See _ZOOM_truss_seed.png and "
        "_ZOOM_truss_controls.png)"
        ", 70th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_truss_legendary_preview", out="_PREVIEW_truss_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary70", "Warlord's Unmoving Cuirass"),
              ("mage", "shirt_mage_legendary70", "Archmage's Twofold-Hinge Mantle"),
              ("ranger", "shirt_ranger_legendary70", "Warden's Single-Hinge Jerkin")],
    ),
    "legs": dict(
        prev="_truss_legs_preview", out="_PREVIEW_truss_legs.png",
        note=NOTE % ("CHAUSSES - and note that EVERY PART IS TRUSSED SEPARATELY. A framework is a "
                     "local object: two legs are two structures, and a pauldron that is not "
                     "touching the torso is not braced by it. The 67th's census had to be of the "
                     "whole garment; this, like the 69th, is a fact about one piece at a time",
                     "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary70", "Warlord's Unmoving Chausses"),
              ("mage", "pants_mage_legendary70", "Archmage's Twofold-Hinge Leggings"),
              ("ranger", "pants_ranger_legendary70", "Warden's Single-Hinge Chausses")],
    ),
    "boots": dict(
        prev="_truss_boots_preview", out="_PREVIEW_truss_boots.png",
        note=NOTE % ("SABATONS - and this slot is MOSTLY SILENT, on a second theorem beside the "
                     "class minimum. A framework needs a CYCLE and a cycle needs the part to "
                     "ENCLOSE something; a sabaton in most poses is a ribbon two pixels wide, and "
                     "a two-pixel ribbon has no interior to put a polygon in. It is not a matter "
                     "of size - a fourteen-pixel square would take a triangle - it is a matter of "
                     "WIDTH, and the axis has no way to pretend otherwise. Five of the six boots "
                     "sheets are therefore a plain recolor and are reported as such; the female "
                     "ranger's boot is the one that is wide enough in all forty-two poses, and it "
                     "is trussed",
                     "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_truss", "Warlord's Unmoving Sabatons"),
              ("mage", "boots_mage_legendary_truss", "Archmage's Twofold-Hinge Steps"),
              ("ranger", "boots_ranger_legendary_truss", "Warden's Single-Hinge Boots")],
    ),
    "helmet": dict(
        prev="_trussdome_helmet_preview", out="_PREVIEW_trussdome_helmet.png",
        note=NOTE % ("HELM - and the dome is where this axis is at its most legible, because a "
                     "skull is the most convex part in the batch and a convex part is the one on "
                     "which every bar the framework wants is actually inside the mask. It is also "
                     "the slot where the class can be read at a glance: three struts, four, five",
                     "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary70", "Warlord's Unmoving Helm"),
              ("mage", "helmet_mage_legendary70", "Archmage's Twofold-Hinge Crown"),
              ("ranger", "helmet_ranger_legendary70", "Warden's Single-Hinge Hood")],
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
        k = G.KDOF[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, k = {k} motions, seed = a {SEEDNAME[k]})",
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
        fr, got = G.one_plate(base, sl, a, cls, mode)
        return fr, a, got
    return None, None, None


def build_seed_zoom():
    """THE CLASS, TRACED. A triangle, a quadrilateral, a pentagon - and everything else on the
    plate is a Henneberg extension that changes nothing about how free the figure is."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for cls in ("warrior", "ranger", "mage"):
        k = G.KDOF[cls]
        fr, a, _got = _plate(cls)
        im = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
        d = ImageDraw.Draw(im)
        nbars = 0
        for comp in G.parts_of(a):
            got = G.truss_of(comp, k)
            if got is None:
                continue
            J, E, _PX = got
            nbars += len(E)
            m = 3 + k

            def pt(i):
                return ((J[i][1] - crop[1 - 1]) * Z + Z // 2, (J[i][0] - crop[1]) * Z + Z // 2)
            # the seed cycle is the first m joints, in the order they were laid
            for i in range(m):
                a1 = pt(i)
                b1 = pt((i + 1) % m)
                d.line([a1, b1], fill=(255, 220, 90, 255), width=2)
            for i in range(len(J)):
                cx, cy = pt(i)
                col = (255, 220, 90, 255) if i < m else (140, 200, 255, 255)
                d.ellipse([cx - Z, cy - Z, cx + Z, cy + Z], outline=col, width=2)
        cells.append((im, "%s  k=%d  seed = a %s  (%d bars)"
                      % (cls, k, SEEDNAME[k], nbars)))
    _zoom(cells, cw, chh, "_ZOOM_truss_seed.png",
          caption="THE CLASS IS THE SEED, AND THE SEED IS THE ONLY THING WITH ANY FREEDOM IN IT.\n"
                  "Gold is the seed cycle - a triangle for the warrior, a quadrilateral for the\n"
                  "ranger, a pentagon for the mage - and a triangle cannot move, a quadrilateral\n"
                  "lozenges one way and a pentagon two. Blue joints were added afterwards, each\n"
                  "with EXACTLY TWO BARS to joints already placed: a Henneberg type-I extension,\n"
                  "which is a theorem that changes neither the independence of the framework nor\n"
                  "its number of motions. So the ornament GROWS WITHOUT EVER CHANGING HOW FREE IT\n"
                  "IS, and a torso with ten bars in it is the same object as a pauldron with three.\n"
                  "Nothing here is at a pitch, on a lattice or in a phase; it is one irregular\n"
                  "figure per part, and the part decides how big it is.")


def build_controls_zoom():
    """The same cuirass, four ways. Three are false, and the two nearest neighbours in the whole
    project are false for opposite reasons."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for mode, name in ((None, "TRUSS (shipped)"), ('tree', "TREE = the 66th DOVETAIL"),
                       ('grid', "GRID = the 14th LATTICE"), ('trellis', "TRELLIS = the 20th")):
        fr, _a, _got = _plate('ranger', mode)
        im = Image.fromarray(fr).crop(crop)
        cells.append((im, name))
    _zoom(cells, cw, chh, "_ZOOM_truss_controls.png",
          caption="ONE RANGER CUIRASS, FOUR FRAMEWORKS, ONE PAINTER, ONE PALETTE, ONE KIND OF\n"
                  "RELIEF. TREE is the 66th DOVETAIL's own structure - a spanning tree, connected,\n"
                  "tidy, and with n-2 motions instead of one, because CONNECTED IS NOT RIGID; it\n"
                  "also has leaves, and a leaf is a whisker that carries no load. GRID is the 14th\n"
                  "LATTICE: the most obviously structural picture in the project and a MECHANISM in\n"
                  "every cell it has - it looks the stiffest and it is the floppiest thing in the\n"
                  "file: FLEX 39, and the DOFs it reads are 2, 3, 5, 7, 8 and 9. TRELLIS is the\n"
                  "20th, the same net with a diagonal in every cell: it IS rigid, and it fails\n"
                  "anyway - FLEX 26, TIGHT 3, CLOSED 36, CLEAR 13 - because it is rigid several\n"
                  "times over and most of its bars are carrying nothing. THE TWO NEAREST VISUAL\n"
                  "NEIGHBOURS IN THE PROJECT FAIL THIS AXIS FOR OPPOSITE REASONS, and that is the\n"
                  "distinctness argument stated as an experiment rather than as an opinion.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_seed_zoom()
    build_controls_zoom()


if __name__ == "__main__":
    main()
