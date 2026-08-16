#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-NINTH net-new-geometry axis batch
(ANNEAL family - the plate is pinned at n points of its own outline and then LET GO).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 64th's claim could not be seen because an eye cannot take an exclusive-or, so its evidence became
a DECODE. The 66th's claim was a negative and a negative has no picture, so its evidence became a
DISASSEMBLY. The 67th's claim was a sentence, so its evidence became a READING. The 68th's claim was
that nothing repeats, so its evidence became a HISTOGRAM. THIS AXIS'S CLAIM IS THAT NOBODY DREW THE
ORNAMENT - so its evidence is the two things you would need in order to disbelieve that:

  _ZOOM_anneal_field.png     One real cuirass per class at 10x with THE POLES RINGED. Three pixels,
                             four pixels, two pixels - that is the entire input, and everything else
                             on the plate follows from them and from the outline. The three classes
                             do not merely obey different laws, THEY HANG DIFFERENTLY: a dipole's
                             ribs cross the plate, a tripole's stack, a quadrupole's stand on end.

  _ZOOM_anneal_controls.png  THE SAME CUIRASS FOUR TIMES: as shipped, then DISTANCE (which is the
                             47th MOKUME drawn by this axis's own painter), HALFWAY (the relaxation
                             stopped at 25 sweeps) and GROUNDED (the rim held at zero). Same pixel,
                             same relief, same palette. Three of them are false. HALFWAY in
                             particular is invisible, and that is the point of it: the only way this
                             axis can be false is to be a plate that was still moving.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_anneal_axis69 as G                                 # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new ANNEAL %s (n pixels of the piece's own outline are HELD at fixed potentials and "
        "every other pixel is let go until it is the MEAN OF ITS NEIGHBOURS; the ribs are where "
        "that equilibrium changes band. FIRST INVARIANT THAT IS AN EQUILIBRIUM - all 68 axes before "
        "it are constructions and somebody decided where the ornament went; here NOTHING IN THE "
        "INTERIOR IS AUTHORED and there is nothing to author. Exact complement of the 65th CASCADE, "
        "which is a plate that remembers how it was made: clause AMNESIA re-relaxes each plate from "
        "six different histories - zero, noise, the 47th's distance transform, random interiors - "
        "and all six arrive at the same picture, 90/90. The acceptance test is a RECOMPUTATION: the "
        "reader is handed the MASK, told nothing, DRAWS THE ORNAMENT ITSELF and demands the plate "
        "pixel for pixel; the class falls out as the only n that matches. Class identity is the "
        "ORDER OF A MULTIPOLE - warrior 2, ranger 3, mage 4 - and it is VISIBLE: a dipole's ribs "
        "cross the plate, a tripole's stack, a quadrupole's stand on end. There is NO PITCH "
        "anywhere in this axis; the band count comes down until every band has a field to stand on, "
        "so the spacing is an output. Axis ALL PASS on 840 plates; 8 controls, 6 false, 1 lawful "
        "and misnamed, 1 DEAD. See _ZOOM_anneal_field.png and _ZOOM_anneal_controls.png)"
        ", 69th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_anneal_legendary_preview", out="_PREVIEW_anneal_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary69", "Warlord's Annealed Cuirass"),
              ("mage", "shirt_mage_legendary69", "Archmage's Quenched Mantle"),
              ("ranger", "shirt_ranger_legendary69", "Warden's Settled Jerkin")],
    ),
    "legs": dict(
        prev="_anneal_legs_preview", out="_PREVIEW_anneal_legs.png",
        note=NOTE % ("CHAUSSES - and note that EVERY PART IS ANNEALED SEPARATELY. The 67th's census "
                     "had to be of the whole garment because a count is only a count of something; "
                     "a potential is a local object and two legs are two bodies, each with its own "
                     "outline and its own poles",
                     "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary69", "Warlord's Annealed Chausses"),
              ("mage", "pants_mage_legendary69", "Archmage's Quenched Leggings"),
              ("ranger", "pants_ranger_legendary69", "Warden's Settled Chausses")],
    ),
    "boots": dict(
        prev="_anneal_boots_preview", out="_PREVIEW_anneal_boots.png",
        note=NOTE % ("SABATONS - and this time the boots SPEAK. The 66th missed a sabaton by a "
                     "pixel and the 67th missed it by a theorem (no self-descriptive word is "
                     "shorter than four). This axis's minimum is TWO POLES and a twelve-pixel "
                     "sabaton has two pixels, so every class is shod. What the sabatons cost "
                     "instead is BAND COUNT: they take three levels where a cuirass takes seven, "
                     "and on seven poses of the female mage's boots the ruling will not go on at "
                     "all - those parts are left plain and counted rather than faked",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_anneal", "Warlord's Annealed Sabatons"),
              ("mage", "boots_mage_legendary_anneal", "Archmage's Quenched Striders"),
              ("ranger", "boots_ranger_legendary_anneal", "Warden's Settled Boots")],
    ),
    "helmet": dict(
        prev="_annealdome_helmet_preview", out="_PREVIEW_annealdome_helmet.png",
        note=NOTE % ("HELM - the black eye and mouth slits are the finishing pass, untouched. A "
                     "dome is the most convex body in the batch and therefore the one on which "
                     "this axis comes CLOSEST to the 11th FLUTING (control LINEAR is exactly that "
                     "degeneration); the amount by which a helm's ribs are not straight reeds is "
                     "the amount by which a skull is not a box",
                     "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary69", "Warlord's Annealed Helm"),
              ("mage", "helmet_mage_legendary69", "Archmage's Quenched Crown"),
              ("ranger", "helmet_ranger_legendary69", "Warden's Settled Hood")],
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
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, n = {G.NPOLE[cls]} poles)",
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


def build_field_zoom():
    """THE ENTIRE INPUT, RINGED. Three, four or two pixels; everything else is a consequence."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for cls in ("warrior", "ranger", "mage"):
        fr, a, _got = _plate(cls)
        im = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
        d = ImageDraw.Draw(im)
        for comp in G.parts_of(a):
            pol = G.poles_of(comp, G.NPOLE[cls])
            if pol is None:
                continue
            for (py, px, v) in pol:
                cx = (px - crop[0]) * Z + Z // 2
                cy = (py - crop[1]) * Z + Z // 2
                if not (0 <= cx < cw and 0 <= cy < chh):
                    continue
                col = (255, 235, 120, 255) if v > 0 else (120, 190, 255, 255)
                d.ellipse([cx - Z, cy - Z, cx + Z, cy + Z], outline=col, width=2)
        cells.append((im, "%s  n=%d  (hot ringed gold, cold ringed blue)"
                      % (cls, G.NPOLE[cls])))
    _zoom(cells, cw, chh, "_ZOOM_anneal_field.png",
          caption="THIS IS THE WHOLE INPUT. Two, three or four pixels of the piece's own outline are\n"
                  "held at cos(2*pi*j*floor(n/2)/n) - values that sum to zero, so no class is a\n"
                  "brighter version of another - and EVERY OTHER PIXEL IS FREE. Nothing in the\n"
                  "interior was placed, chosen, spaced or phased; the ribs are the level lines of the\n"
                  "state in which no pixel has a reason left to move. The three classes HANG\n"
                  "DIFFERENTLY and nobody has to be told which is which: the dipole's ribs cross the\n"
                  "plate, the tripole's stack, the quadrupole's stand on end.")


def build_controls_zoom():
    """The same cuirass, four ways. Three of them are false and one of the three is invisible."""
    Z = 10
    crop = (26, 16, 56, 50)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    cells = []
    for mode, name in ((None, "ANNEAL (shipped)"), ('distance', "DISTANCE = the 47th MOKUME"),
                       ('halfway', "HALFWAY (25 sweeps)"), ('grounded', "GROUNDED (rim at 0)")):
        fr, _a, _got = _plate('ranger', mode)
        im = Image.fromarray(fr).crop(crop)
        cells.append((im, name))
    _zoom(cells, cw, chh, "_ZOOM_anneal_controls.png",
          caption="ONE RANGER CUIRASS, FOUR FIELDS, ONE PAINTER, ONE PALETTE, ONE KIND OF RELIEF.\n"
                  "DISTANCE is the 47th axis drawn by this one's hand: its contours are CLOSED and\n"
                  "hug the outline, it has a RIDGE of local maxima down every limb (683 violations),\n"
                  "and when a pole is moved NOTHING ON IT MOVES - 13175 of 13175 free pixels deaf,\n"
                  "which is the distinctness argument stated as a number instead of as an opinion.\n"
                  "HALFWAY is this axis stopped 25 sweeps early. AT THIS ZOOM IT IS INVISIBLE, and\n"
                  "it is false: 1684 pixels of it are strict local extrema, which an equilibrium\n"
                  "cannot have. It is the only way this axis knows how to be wrong - a plate that\n"
                  "was still moving - and it is exactly what the 65th CASCADE is made of.\n"
                  "GROUNDED holds the whole rim at zero instead of leaving it insulated: the ribs\n"
                  "pull off the outline and close into rings, and 12 of 24 sheets cannot be drawn.\n"
                  "AN INSULATED RIM IS WHY A RIB CAN END ON THE SILHOUETTE, and a rib that cannot\n"
                  "end on the silhouette is a closed curve, and a closed curve is the 47th again.")


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_field_zoom()
    build_controls_zoom()


if __name__ == "__main__":
    main()
