#!/usr/bin/env python3
"""Daily-approval preview panels for the SEVENTY-SEVENTH net-new-geometry axis batch
(CLASP family - the ornament is a set of CLASPS on the garment's own lattice, and the law is that
the plate is a KNIFE EDGE: nothing can be added to it and nothing can be taken away).

*** WHY THE EVIDENCE PANELS LOOK LIKE THIS. ***
The 74th's claim was that the picture does not matter, so it showed one plate as four pictures. The
75th's was about a picture that is not on the plate. The 76th's was about marks that are not there.

THIS AXIS'S CLAIM IS THAT THE PLATE IS PINNED - the first law in the project that is broken by
ADDING and by TAKING AWAY - so its evidence has to be shown TWICE, once in each direction:

  _ZOOM_clasp_pinned.png   THE SQUEEZE. One real cuirass as shipped, then the same plate with one
                           clasp put on, then the same plate with one clasp taken off. Both
                           neighbours are unlawful and for OPPOSITE reasons, and the two reasons do
                           not even look alike: an addition makes two clasps meet, which is drawn as
                           one long bent bright thing, so the plate stops being made of clasps at
                           all and the EYE refuses it; a removal leaves two bare sockets side by
                           side, which looks perfectly ordinary, and only the ARITHMETIC refuses it.

  _ZOOM_clasp_price.png    THE CLASS, WHICH IS A PLAN THE LAW FORBIDS. One plate per class at 10x
                           with every socket ringed - filled where a clasp holds it, hollow where it
                           is bare - and the cheapest improvement drawn over the top: the chain that
                           runs from one bare socket to another, whose clasps would have to be broken
                           and re-made to end up one clasp better. The warrior's chain costs one, the
                           mage's costs two, and the RANGER HAS NO CHAIN AT ALL - not one that was
                           not found, one that does not exist, which is Berge's theorem and is why
                           the ranger's identity can be stated rather than merely searched for.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_clasp_axis77 as G                                  # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

PNAME = {1: "PRICE ONE", 2: "PRICE TWO", None: "NO PRICE - ALREADY THE MOST IT CAN HOLD"}

NOTE = ("net-new CLASP %s (the ground is a LATTICE - every cloth pixel on one phase of a "
        "three-pixel grid is a SOCKET, and the sockets are the SILHOUETTE'S, not the painter's. "
        "The ornament is a CLASP: a straight bright bar four pixels long joining two neighbouring "
        "sockets, lying down or standing up, with a hard shadow one down and one left. A socket "
        "with no clasp on it carries no ink. THE LAW IS THAT THE PLATE IS A KNIFE EDGE - no two "
        "clasps meet and no two bare sockets meet - so you cannot draw another clasp anywhere "
        "without two of them sharing a socket, and you cannot rub one out without leaving two bare "
        "sockets side by side. FIRST LAW IN THE PROJECT THAT IS NOT MONOTONE: the 68th SEME "
        "survives every deletion, the 76th GAUGE survives every addition, and this one survives "
        "neither. THE PICTURE IS PINNED. Class identity is a PRICE - what it would cost to carry "
        "one more clasp: warrior 1, mage 2, and the ranger NOTHING WILL DO IT, because a ranger "
        "plate already carries the most clasps its garment can ever hold. First class identity "
        "whose third value is not a number, and first that is a plan the law forbids the reader to "
        "carry out. The acceptance test is a new kind - a SQUEEZE, every clasp that could go on and "
        "every clasp that could come off, 5866 and 2916 of them, none of which leaves a lawful "
        "plate. See _ZOOM_clasp_pinned.png and _ZOOM_clasp_price.png), 77th %s axis (repaint, "
        "QA-safe)")

SETS = {
    "chest": dict(
        prev="_clasp_legendary_preview", out="_PREVIEW_clasp_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary77", "Warlord's Pinned Cuirass"),
              ("mage", "shirt_mage_legendary77", "Archmage's Fastened Mantle"),
              ("ranger", "shirt_ranger_legendary77", "Warden's Full Harness")],
    ),
    "legs": dict(
        prev="_clasp_legs_preview", out="_PREVIEW_clasp_legs.png",
        note=NOTE % ("CHAUSSES - and the male mage leggings are PLAIN AND PROVED. On one pose of "
                     "35 the best phase offers ten sockets and six pairs, and every pinned pairing "
                     "on every one of the nine phases was listed out: not one of them costs two. "
                     "That is not a search that gave up, it is a statement about every picture "
                     "that could have been painted there", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary77", "Warlord's Pinned Chausses"),
              ("mage", "pants_mage_legendary77", "Archmage's Fastened Leggings"),
              ("ranger", "pants_ranger_legendary77", "Warden's Full Greaves")],
    ),
    "boots": dict(
        prev="_clasp_boots_preview", out="_PREVIEW_clasp_boots.png",
        note=NOTE % ("SABATONS - the slot where the axis meets garments it cannot have and can "
                     "prove it. A boot at three pixels of pitch is four or five sockets, and a "
                     "price of two needs a chain of six; the enumeration lists every pinned "
                     "pairing there and finds none. Five sheets are PLAIN AND PROVED and only the "
                     "female ranger boot, whose shaft is the widest in the slot, carries the axis - "
                     "and it carries the identity that asks for least, which is the one that asks "
                     "for nothing", "boots"),
        crop=(10, 20, 70, 64), cw=60, ch=44,
        rows=[("warrior", "boots_warrior_legendary_clasp", "Warlord's Pinned Sabatons"),
              ("mage", "boots_mage_legendary_clasp", "Archmage's Fastened Steps"),
              ("ranger", "boots_ranger_legendary_clasp", "Warden's Full Boots")],
    ),
    "helmet": dict(
        prev="_claspdome_helmet_preview", out="_PREVIEW_claspdome_helmet.png",
        note=NOTE % ("HELM - the slot that carries this axis best. A dome is a broad unbroken "
                     "sheet of cloth, which is what a lattice wants, so all six sheets are clasped "
                     "in all 42 poses and every one of the three identities was available to every "
                     "one of them. The visor is the finishing pass's, not the axis's: the clasps "
                     "stop where the eye slits start", "helmet"),
        crop=(20, 14, 62, 46), cw=42, ch=32,
        rows=[("warrior", "helmet_warrior_legendary77", "Warlord's Pinned Greathelm"),
              ("mage", "helmet_mage_legendary77", "Archmage's Fastened Crown"),
              ("ranger", "helmet_ranger_legendary77", "Warden's Full Hood")],
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
        p = G.PRICE[cls]
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE, {PNAME[p]})",
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
COLW = 430          # each pane gets a column wide enough for its own caption
HEADW = 150         # characters of header before it is wrapped


def plate_of(cls, kind='chest'):
    """A real pose, its outline, and the pairing that ships on it."""
    stem = G.SLOTS[kind]['srcs'][cls]
    base = G.load_any('%s.png' % stem)
    for fi, sl, a in G.frames_of(base):
        salt = '%s|%d' % (stem, fi)
        keep = G.compose(a, cls, None, salt)
        if keep is None:
            continue
        return base, sl, a, cls, keep, fi
    return None


def render(a, cls, M, phase, extra_core=None, drop=None):
    """Paint one pose the way the generator does, with a clasp added or taken off if asked."""
    fr = np.zeros((FH, FW, 4), np.uint8)
    shadow_c, field_c, bar_c = G.PAL[cls]
    for y, x in np.argwhere(a):
        G.put(fr, y, x, field_c)
    N = list(M)
    if drop is not None:
        N = [e for i, e in enumerate(N) if i != drop]
    if extra_core is not None:
        N = N + [extra_core]
    core, dark = G.paint(a, (phase, N))
    for y, x in np.argwhere(dark):
        G.put(fr, y, x, shadow_c)
    for y, x in np.argwhere(core):
        G.put(fr, y, x, bar_c)
    return fr, N


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


def zoom(fr):
    im = Image.fromarray(fr).crop(CROP)
    return im.resize((im.size[0] * Z, im.size[1] * Z), Image.NEAREST)


def at(pt):
    """Pixel (y, x) of the frame -> centre of its cell in the zoomed crop."""
    y, x = pt
    return ((x - CROP[0]) * Z + Z // 2, (y - CROP[1]) * Z + Z // 2)


def ring(d, pt, col, r=6, w=2):
    cx, cy = at(pt)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=w)


def evidence_pinned():
    """THE SQUEEZE, on one real cuirass: as shipped, plus one, minus one."""
    got = plate_of('warrior')
    base, sl, a, cls, (phase, M), fi = got
    S, E, g = G.lattice(a, phase)
    ms = {tuple(sorted(e)) for e in M}
    add = next(e for e in E if tuple(sorted(e)) not in ms)
    drop = 0

    fsm, fbig = font(13), font(17)
    panes = []
    # as shipped
    fr, _ = render(a, cls, M, phase)
    panes.append((zoom(fr), "AS SHIPPED - LAWFUL",
                  ["no two clasps meet", "no two bare sockets meet",
                   "%d clasps, %d sockets, %d bare" % (len(M), len(S), len(S) - 2 * len(M))],
                  (140, 230, 150, 255), []))
    # plus one
    fr2, N2 = render(a, cls, M, phase, extra_core=add)
    hit = [e for e in M if add[0] in e or add[1] in e]
    marks = [p for e in hit for p in e if p in add]
    panes.append((zoom(fr2), "ONE CLASP ADDED - UNLAWFUL",
                  ["there was nowhere for it to go", "two clasps now share a socket",
                   "drawn as ONE BENT BAR: the EYE refuses it"],
                  (255, 120, 120, 255), [(marks[0] if marks else add[0], (255, 90, 90, 255))]))
    # minus one
    fr3, N3 = render(a, cls, M, phase, drop=drop)
    u, v = M[drop]
    panes.append((zoom(fr3), "ONE CLASP TAKEN OFF - UNLAWFUL",
                  ["it left two bare sockets side by side", "the picture still looks like clasps",
                   "only the ARITHMETIC refuses it"],
                  (255, 120, 120, 255), [(u, (255, 90, 90, 255)), (v, (255, 90, 90, 255))]))

    pw, ph = panes[0][0].size
    pad, foot = 16, 90
    W = pad + len(panes) * COLW
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    head = 34 + 3 * 15 + 12
    H = head + ph + foot
    canvas = Image.new("RGBA", (W, H), (22, 22, 28, 255))
    d = ImageDraw.Draw(canvas)
    d.text((pad, 10), "THE SQUEEZE - one warrior cuirass, and both of its neighbours",
           font=fbig, fill=(150, 200, 255, 255))
    wrap_text(d, "77th CLASP axis. The first law in the project that is broken by ADDING and by "
                 "TAKING AWAY - the 68th SEME survives every deletion, the 76th GAUGE survives "
                 "every addition, and this survives neither. Across the whole batch 5866 additions "
                 "and 2916 removals were tried and not one of them left a lawful plate.",
              pad, 34, W - 2 * pad, fsm, (150, 160, 175, 255))
    x = pad
    for im, title, lines, col, rings in panes:
        ix = x + (COLW - pad - pw) // 2
        canvas.alpha_composite(im, (ix, head))
        dd = ImageDraw.Draw(canvas)
        for pt, rc in rings:
            cx, cy = at(pt)
            dd.ellipse([ix + cx - 7, head + cy - 7, ix + cx + 7, head + cy + 7],
                       outline=rc, width=2)
        d.text((x, head + ph + 8), title, font=fsm, fill=col)
        for i, ln in enumerate(lines):
            d.text((x, head + ph + 26 + i * 15), ln, font=fsm, fill=(200, 200, 210, 255))
        x += COLW
    canvas.convert("RGB").save("_ZOOM_clasp_pinned.png")
    print("wrote _ZOOM_clasp_pinned.png", canvas.size)


def evidence_price():
    """THE CLASS - the cheapest improvement, drawn over the plate that may not make it."""
    fsm, fbig = font(13), font(17)
    panes = []
    for cls in ('warrior', 'mage', 'ranger'):
        base, sl, a, _c, (phase, M), fi = plate_of(cls)
        S, E, g = G.lattice(a, phase)
        fr, _ = render(a, cls, M, phase)
        path = G.augment_path(S, g, M)
        married = {u for e in M for u in e}
        bare = [s for s in S if s not in married]
        want = G.PRICE[cls]
        if want is None:
            lines = ["%d clasps, %d bare sockets" % (len(M), len(bare)),
                     "NO CHAIN RUNS FROM ONE BARE SOCKET TO ANOTHER",
                     "so there is no improvement at any price:",
                     "this plate carries the most the garment can hold"]
        else:
            lines = ["%d clasps, %d bare sockets" % (len(M), len(bare)),
                     "the cheapest chain runs bare -> %d clasp(s) -> bare" % want,
                     "break those %d and re-marry along it: %d clasps" % (want, len(M) + 1),
                     "THE LAW FORBIDS IT. The price is what it WOULD cost"]
        panes.append((zoom(fr), "%s - %s" % (cls.upper(), PNAME[want]), lines, S, bare, path))

    pw, ph = panes[0][0].size
    pad, foot = 16, 100
    W = pad + len(panes) * COLW
    head = 34 + 3 * 15 + 12
    H = head + ph + foot
    canvas = Image.new("RGBA", (W, H), (22, 22, 28, 255))
    d = ImageDraw.Draw(canvas)
    d.text((pad, 10), "THE PRICE - a plan the law will not let anybody carry out",
           font=fbig, fill=(150, 200, 255, 255))
    wrap_text(d, "Every socket the lattice offers is ringed: FILLED where a clasp holds it, HOLLOW "
                 "where it is bare. The yellow chain is the cheapest improvement there is, and its "
                 "length in clasps IS the class - warrior 1, mage 2. The ranger has no chain: not "
                 "one that was not found, one that does not exist, which is Berge's theorem.",
              pad, 34, W - 2 * pad, fsm, (150, 160, 175, 255))
    x = pad
    for im, title, lines, S, bare, path in panes:
        ix = x + (COLW - pad - pw) // 2
        canvas.alpha_composite(im, (ix, head))
        dd = ImageDraw.Draw(canvas)
        for s in S:
            cx, cy = at(s)
            if not (0 <= cx < pw and 0 <= cy < ph):
                continue
            r = 5
            if s in bare:
                dd.ellipse([ix + cx - r, head + cy - r, ix + cx + r, head + cy + r],
                           outline=(120, 220, 255, 255), width=2)
            else:
                dd.ellipse([ix + cx - 3, head + cy - 3, ix + cx + 3, head + cy + 3],
                           fill=(120, 220, 255, 255))
        if path:
            pts = [(ix + at(p)[0], head + at(p)[1]) for p in path]
            dd.line(pts, fill=(255, 214, 96, 255), width=3)
            for cx, cy in (pts[0], pts[-1]):
                dd.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], outline=(255, 214, 96, 255), width=3)
        d.text((x, head + ph + 8), title, font=fsm, fill=(150, 230, 160, 255))
        for i, ln in enumerate(lines):
            d.text((x, head + ph + 26 + i * 15), ln, font=fsm, fill=(200, 200, 210, 255))
        x += COLW
    canvas.convert("RGB").save("_ZOOM_clasp_price.png")
    print("wrote _ZOOM_clasp_price.png", canvas.size)


def main():
    if '--evidence' in sys.argv:
        evidence_pinned()
        evidence_price()
        return
    for kind, cfg in SETS.items():
        build(kind, cfg)
    evidence_pinned()
    evidence_price()


if __name__ == '__main__':
    main()
