#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-SIXTH net-new-geometry axis batch
(GAUGE family - the ornament is a set of TICKS standing on a RULE, and the law is that no length the
rule spans is missing from it).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 66th's claim was a negative, so its evidence became a DISASSEMBLY. The 69th's was that nobody
drew the ornament. The 73rd's was about the pixels between the marks. The 74th's was that the picture
does not matter, so it showed one plate as four pictures. The 75th's was about a picture that is not
on the plate.

THIS AXIS'S CLAIM IS ABOUT MARKS THAT ARE NOT THERE - a gauge is lawful only if there is no length
it fails to measure - so its evidence has to point twice at absences:

  _ZOOM_gauge_reading.png   One cuirass per class at 10x with every tick ringed and every rule's
                            reading worked out beside it: the span the silhouette handed over, the
                            ticks standing on it, the fewest ticks that span could ever have been
                            measured with, and therefore the excess. THE CLASS IS THE TOTAL, and no
                            single comb on the plate carries it.

  _ZOOM_gauge_hole.png      THE LAW, AND WHAT BREAKING IT LOOKS LIKE. One real rule as shipped, then
                            the same rule with a single tick taken off - a picture almost identical
                            to the first, and unlawful, because one length in the middle of its
                            range is now unmeasurable. The panel names that length. On a mage plate
                            EVERY tick does this and no experiment is needed; on a warrior one tick
                            in five can go.

  _ZOOM_gauge_minima.png    THE EXHAUSTION - the only panel in the project whose subject is pictures
                            THAT DO NOT EXIST. Every mark set smaller than the minimum for one real
                            span, drawn in full, each with the length it cannot measure written
                            under it. That the plate carries the fewest ticks it could is not a
                            claim about the plate; it is a claim about all of these.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_gauge_axis76 as G                                  # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

ENAME = {0: "PERFECT - NOTHING SPARE", 1: "ONE TICK SPARE", 2: "TWO TICKS SPARE"}

NOTE = ("net-new GAUGE %s (the ground is a RULE - an unbroken run of cloth two rows deep - and the "
        "ornament is a TICK, a post two pixels tall with a hard shadow one down and one left, so a "
        "rule reads as a comb with irregular teeth. Any two ticks measure the pixels between them. "
        "THE LAW IS THAT NO LENGTH FROM ONE TO THE SPAN IS MISSING: the gauge measures everything "
        "it is long enough to measure. FIRST LAW THAT IS A COMPLETENESS - seventy-five axes are "
        "satisfied by the marks that are there, and this one is about the marks that are not, so "
        "the reader's job is to go looking for a hole. EXACT COMPLEMENT OF THE 68th SEME AND THERE "
        "IS NO THIRD THING TO SAY: a set of marks on a line can be forbidden to REPEAT a "
        "displacement (a Sidon set, the 68th) or forbidden to MISS one (a complete ruler, this), "
        "and that exhausts the sentence. The span is the SILHOUETTE'S and not the painter's, "
        "because the ticks must reach both ends of the run they stand on. Class identity is an "
        "EXCESS - how many more ticks the WHOLE PLATE carries than the fewest that could have done "
        "its job: mage 0, ranger 1, warrior 2. FIRST CLASS IDENTITY THAT NO SINGLE ORNAMENT ON THE "
        "PLATE CARRIES - every comb on a warrior cuirass is usually exactly the comb a mage would "
        "have worn, and the whole difference is two ticks somewhere on the garment, so THE READER "
        "HAS TO TOTAL THE PLATE. It is also the first class that is a comparison with something "
        "nobody drew, and the acceptance test is a new kind - an EXHAUSTION over every smaller mark "
        "set there is. See _ZOOM_gauge_reading.png, _ZOOM_gauge_hole.png and "
        "_ZOOM_gauge_minima.png), 76th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_gauge_legendary_preview", out="_PREVIEW_gauge_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary76", "Warlord's Measured Cuirass"),
              ("mage", "shirt_mage_legendary76", "Archmage's Exact Mantle"),
              ("ranger", "shirt_ranger_legendary76", "Warden's Reckoning Jerkin")],
    ),
    "legs": dict(
        prev="_gauge_legs_preview", out="_PREVIEW_gauge_legs.png",
        note=NOTE % ("CHAUSSES - and the chausses are where the reach argument earns its keep. A "
                     "rule can absorb only so many ticks before it has four in a row and stops "
                     "being a comb, so every pose has a CEILING on the excess it could ever wear, "
                     "and both plain sheets here are UNDER it rather than unfound: the male "
                     "warrior on 5 poses of 35 and the male ranger on 2. The class that asks for "
                     "most is dressed least often, which is the first time in the project that the "
                     "expensive class is expensive in COVERAGE", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary76", "Warlord's Measured Chausses"),
              ("mage", "pants_mage_legendary76", "Archmage's Exact Leggings"),
              ("ranger", "pants_ranger_legendary76", "Warden's Reckoning Greaves")],
    ),
    "boots": dict(
        prev="_gauge_boots_preview", out="_PREVIEW_gauge_boots.png",
        note=NOTE % ("SABATONS - the slot where the axis meets garments it cannot have, and can "
                     "prove it. A gauge needs a straight run of four pixels two rows deep, and on "
                     "35 poses of 35 the warrior sabaton has none at all: its ceiling is not low, "
                     "it is EMPTY. Four sheets are PLAIN AND REPORTED and the two female mage and "
                     "ranger boots, whose shafts are the widest in the slot, carry the axis - the "
                     "mage in all 42 poses. THE SABATON HAS NOWHERE TO PUT A RULE, and that is a "
                     "fact about the sabaton", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_gauge", "Warlord's Measured Sabatons"),
              ("mage", "boots_mage_legendary_gauge", "Archmage's Exact Steps"),
              ("ranger", "boots_ranger_legendary_gauge", "Warden's Reckoning Boots")],
    ),
    "helmet": dict(
        prev="_gaugedome_helmet_preview", out="_PREVIEW_gaugedome_helmet.png",
        note=NOTE % ("HELM - and the helm is the slot that carries this axis best. A dome is a "
                     "stack of long unbroken runs, which is exactly what a rule is, so all six "
                     "sheets are ruled in all 42 poses and the warrior's ceiling is three times "
                     "the excess its class asks for. The visor is the finishing pass's, not the "
                     "axis's: the ticks stop where the eye slits start", "helmet"),
        crop=(20, 14, 62, 46), cw=42, ch=32,
        rows=[("warrior", "helmet_warrior_legendary76", "Warlord's Measured Greathelm"),
              ("mage", "helmet_mage_legendary76", "Archmage's Exact Crown"),
              ("ranger", "helmet_ranger_legendary76", "Warden's Reckoning Hood")],
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
        e = G.EXCESS[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, excess {e} - {ENAME[e]})",
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


def repaint(fr, a, cls, keep):
    """The SAME plate wearing a DIFFERENT set of ticks. The evidence has to draw gauges the batch
    does not ship - a rule with a tick taken out of it - and this is what draws them."""
    arr = fr.copy()
    shadow_c, field_c, tick_c = G.PAL[cls]
    for y, x in np.argwhere(a):
        G.put(arr, y, x, field_c)
    core, dark = G.paint(a, keep)
    for y, x in np.argwhere(dark):
        G.put(arr, y, x, shadow_c)
    for y, x in np.argwhere(core):
        G.put(arr, y, x, tick_c)
    return arr


def _im(arr):
    return Image.fromarray(arr[CROP[1]:CROP[3], CROP[0]:CROP[2]]).resize((CW, CHH), Image.NEAREST)


def build_reading_zoom():
    """THE READING, DONE ON THE PAGE. Every tick ringed, every rule totalled, the class read off the
    plate and told to nobody."""
    cells = []
    for cls in ('warrior', 'ranger', 'mage'):
        fr, a, _got, salt = _plate(cls)
        keep = G.compose(a, cls, None, salt)
        im = _im(fr).convert('RGBA')
        d = ImageDraw.Draw(im)
        tot = exc = 0
        for y, x0, x1, marks in keep:
            span = x1 - x0
            tot += len(marks)
            exc += len(marks) - G.min_marks(span)
            for x in marks:
                if not (CROP[1] <= y - 1 < CROP[3] and CROP[0] <= x < CROP[2]):
                    continue
                px, py = (x - CROP[0]) * Z, (y - 1 - CROP[1]) * Z
                d.rectangle([px - 1, py - 1, px + Z, py + 2 * Z],
                            outline=(255, 80, 200, 255), width=2)
        cells.append((im, '%s - %d rules, %d ticks\nminimum %d, EXCESS %d = %s'
                      % (cls.upper(), len(keep), tot, tot - exc, exc, cls)))
    cap = ('THREE CUIRASSES AT TEN TIMES, EVERY TICK RINGED. The rings are the PANEL\'S and not the '
           'plate\'s.\n'
           'Read a rule: the run of cloth under it fixes the SPAN, and the ticks must reach both '
           'ends of it, so the painter cannot measure less than the garment offers.\n'
           'Every rule here measures every length from one to its span - that is the law - and '
           'every rule here is also, on its own, EXACTLY WHAT A MAGE WOULD HAVE WORN.\n'
           'The class is the TOTAL: the ticks on the whole plate less the fewest each of its rules '
           'could have been drawn with. Nothing on the plate carries it but the plate.')
    _zoom(cells, CW, CHH, '_ZOOM_gauge_reading.png', cap)


def build_hole_zoom():
    """THE LAW, AND WHAT BREAKING IT LOOKS LIKE. The panel has to point at something that is not
    there, so it names the length."""
    cls = 'warrior'
    fr, a, _got, salt = _plate(cls)
    keep = G.compose(a, cls, None, salt)
    # the longest rule on the plate, and a tick that is load bearing on it
    idx = max(range(len(keep)), key=lambda i: keep[i][2] - keep[i][1])
    y, x0, x1, marks = keep[idx]
    span = x1 - x0
    rel = sorted(x - x0 for x in marks)
    lost = kept = None
    for m in rel[1:-1]:                    # an END tick is load bearing for a second reason - the
                                           # ticks must REACH both ends - so the panel drops an
                                           # interior one and lets the law speak on its own
        left = [r for r in rel if r != m]
        miss = [k for k in range(1, span + 1) if k not in G.measures(left)]
        if miss and lost is None:
            lost = (m, miss)
        if not miss and kept is None:
            kept = m
    broken = list(keep)
    broken[idx] = (y, x0, x1, tuple(x for x in marks if x - x0 != lost[0]))
    cells = [(_im(fr), 'AS SHIPPED\nrule of span %d, %d ticks' % (span, len(marks))),
             (_im(repaint(fr, a, cls, broken)),
              'ONE TICK GONE\nCANNOT MEASURE %s' % ', '.join(str(k) for k in lost[1]))]
    if kept is not None:
        spare = list(keep)
        spare[idx] = (y, x0, x1, tuple(x for x in marks if x - x0 != kept))
        cells.append((_im(repaint(fr, a, cls, spare)),
                      'A DIFFERENT TICK GONE\nstill measures 1..%d - THE EXCESS' % span))
    cap = ('THE LAW IS ABOUT WHAT IS MISSING, SO THE EVIDENCE HAS TO NAME IT. Ticks at %s on a span '
           'of %d.\n'
           'Take out the tick at %d and no pair on the rule is %s apart any more: the gauge has a '
           'hole in it and the plate is unlawful, and the picture barely changed.\n'
           'A MAGE PLATE CANNOT SURVIVE ANY OF THESE, AND THAT IS PROVED RATHER THAN CHECKED - its '
           'rules carry the proved minimum, so one tick fewer is fewer than the span can be\n'
           'measured with. The ranger and the warrior have slack, and the file measures exactly how '
           'much: over the whole batch a dropped tick leaves the gauge standing 0%% of the time for\n'
           'the mage, 8%% for the ranger and 20%% for the warrior. THE EXCESS IS A LICENCE TO LOSE '
           'ORNAMENT, and that is the licence being spent.'
           % (str(rel), span, lost[0], ' or '.join(str(k) for k in lost[1])))
    _zoom(cells, CW, CHH, '_ZOOM_gauge_hole.png', cap)


def build_minima_zoom():
    """THE EXHAUSTION. The only panel in the project whose subject is pictures that do not exist."""
    span = 9
    m = G.min_marks(span)
    from itertools import combinations
    smaller = [(0,) + c + (span,) for c in combinations(range(1, span), m - 3)]
    cellw, cellh = 26, 26
    pad = 10
    cols = 7
    rows_n = (len(smaller) + cols - 1) // cols + 2
    W = pad * 2 + cols * (cellw * (span + 1) // 2 + 40)
    W = max(W, 1500)
    canvas = Image.new('RGBA', (W, pad + rows_n * (cellh + 30) + 150), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    d.text((pad, pad), 'EVERY MARK SET SMALLER THAN THE MINIMUM, ON A SPAN OF %d - AND THE LENGTH '
           'EACH ONE CANNOT MEASURE' % span, font=font(15), fill=(150, 200, 255, 255))
    step_x = (W - 2 * pad) // cols
    yy = pad + 28
    for i, r in enumerate(smaller):
        cx = pad + (i % cols) * step_x
        cy = yy + (i // cols) * (cellh + 30)
        for k in range(span + 1):
            on = k in r
            d.rectangle([cx + k * 14, cy, cx + k * 14 + 12, cy + cellh],
                        fill=(214, 226, 240, 255) if on else (52, 54, 64, 255))
        miss = [k for k in range(1, span + 1) if k not in G.measures(r)]
        d.text((cx, cy + cellh + 4), 'no %s' % ', '.join(str(k) for k in miss),
               font=font(12), fill=(240, 130, 130, 255))
    yy2 = yy + ((len(smaller) + cols - 1) // cols) * (cellh + 30) + 16
    d.text((pad, yy2), 'AND THE FEWEST THAT DO MEASURE EVERYTHING (%d ticks, %d of them exist):'
           % (m, len(G.rulers(span, m))), font=font(15), fill=(150, 200, 255, 255))
    for i, r in enumerate(G.rulers(span, m)[:cols]):
        cx = pad + i * step_x
        cy = yy2 + 26
        for k in range(span + 1):
            on = k in r
            d.rectangle([cx + k * 14, cy, cx + k * 14 + 12, cy + cellh],
                        fill=(150, 240, 170, 255) if on else (52, 54, 64, 255))
        d.text((cx, cy + cellh + 4), 'measures 1..%d' % span, font=font(12),
               fill=(150, 240, 170, 255))
    cap = ['THAT A PLATE CARRIES THE FEWEST TICKS IT COULD IS NOT A CLAIM ABOUT THE PLATE. It is a '
           'claim about all %d of the pictures above, none of which is in the batch.' % len(smaller),
           'Clause EXCESS is settled by drawing every one of them and finding the hole - the first '
           'clause in the project whose subject is pictures that do not exist,',
           'and the reason the class is an OUTPUT: the reader proves the minimum for itself and '
           'subtracts. Across the wardrobe the exhaustion refuses 51,964 mark sets.',
           'The law bites where there is room for it to: on a span of 3 every set of the right size '
           'measures everything, on a span of 12 one in 28 does, on 21 one in 692.']
    for i, line in enumerate(cap):
        d.text((pad, yy2 + 26 + cellh + 34 + i * 18), line, font=font(13), fill=(150, 200, 255, 255))
    canvas.convert('RGB').save('_ZOOM_gauge_minima.png')
    print('wrote _ZOOM_gauge_minima.png', canvas.size)


def main():
    which = [a for a in sys.argv[1:] if not a.startswith('-')]
    if '--zoom' in sys.argv:
        build_reading_zoom()
        build_hole_zoom()
        build_minima_zoom()
        return
    for kind, cfg in SETS.items():
        if which and kind not in which:
            continue
        build(kind, cfg)
    if not which:
        build_reading_zoom()
        build_hole_zoom()
        build_minima_zoom()


if __name__ == '__main__':
    main()
