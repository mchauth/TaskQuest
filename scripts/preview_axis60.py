#!/usr/bin/env python3
"""Daily-approval preview grids for the SIXTIETH net-new-geometry axis batch
(CADENCE family — reeds of exactly TWO widths whose ORDER is the ornament: chest cuirass, legs
chausses, boots sabatons, helmet helm). For each class and gender: full dressed avatar across
idle/walk/run/cheer/slash, plus one isolated slot-over-skin so the sequence is readable.

Emits four _PREVIEW_cadence_*.png plus a chest zoom, a head zoom, and TWO panels that draw the
acceptance test itself:

  _ZOOM_cadence_word.png     the same chest painted from the axis's word and from each of the four
                             controls, with the subword count under each — the RATIONAL cell is the
                             one to look at, because it is the one that looks right and is not.
  _ZOOM_cadence_censor.png   the sampling bias that made the first acceptance run FAIL on a batch
                             whose ornament was correct, drawn on one leg.

Nothing here touches sprites/preview_assets/char or git."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new CADENCE %s (the piece is ruled edge to edge with raised reeds of exactly TWO "
        "widths, in one metal, one relief, one light — and the ORDER the two widths come in is the "
        "entire ornament; FIRST AXIS WHOSE PITCH IS IRRATIONAL, so the reeding cannot repeat, not "
        "on a torso and not on a wall), 60th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_cadence_legendary_preview", out="_PREVIEW_cadence_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary60", "Warlord's Brass Cadence Cuirass"),
              ("mage", "shirt_mage_legendary60", "Archmage's Moonstone Cadence Mantle"),
              ("ranger", "shirt_ranger_legendary60", "Warden's Verdigris Cadence Jerkin")],
    ),
    "legs": dict(
        prev="_cadence_legs_preview", out="_PREVIEW_cadence_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary60", "Warlord's Brass Cadence Chausses"),
              ("mage", "pants_mage_legendary60", "Archmage's Moonstone Cadence Leggings"),
              ("ranger", "pants_ranger_legendary60", "Warden's Verdigris Cadence Chausses")],
    ),
    "boots": dict(
        prev="_cadence_boots_preview", out="_PREVIEW_cadence_boots.png",
        note=NOTE % ("SABATONS — a boot is only a few reeds long, so no boot can show that the "
                     "word never repeats; what it CAN show is that its few reeds are a quotation "
                     "from the same text every other piece is quoting", "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_cadence", "Warlord's Brass Cadence Sabatons"),
              ("mage", "boots_mage_legendary_cadence", "Archmage's Moonstone Cadence Striders"),
              ("ranger", "boots_ranger_legendary_cadence", "Warden's Verdigris Cadence Field-Boots")],
    ),
    "helmet": dict(
        prev="_cadencedome_helmet_preview", out="_PREVIEW_cadencedome_helmet.png",
        note=NOTE % ("HELM", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary60", "Warlord's Brass Cadence Helm"),
              ("mage", "helmet_mage_legendary60", "Archmage's Moonstone Cadence Crown"),
              ("ranger", "helmet_ranger_legendary60", "Warden's Verdigris Cadence Hood-Helm")],
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
    pad, lab_h, title_h = 8, 18, 30
    row_w = (len(FRAMES) + 1) * cw * Z
    row_h = ch * Z + lab_h
    class_h = title_h + 2 * row_h
    canvas = Image.new("RGBA", (pad * 2 + row_w + pad, pad + len(rows) * (class_h + pad)),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    fbig, fsm = font(15), font(11)
    y = pad
    for cls, stem, disp in rows:
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE — {note})",
               font=fbig, fill=(150, 200, 255, 255))
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


def _zoom(paths, crop, Z, out, caption=None):
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad = 10
    extra = 26 if caption else 0
    canvas = Image.new("RGBA", (pad + len(paths) * (cw + pad), pad + chh + 20 + extra),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in paths:
        canvas.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += cw + pad
    if caption:
        d.text((pad, pad + chh + 20), caption, font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_chest_zoom():
    """The three cadence cuirasses at pixel scale. What to look for: a reed opens on a bright CREST
    row and closes on a SHADE row, and a WIDE reed — and only a wide reed — has one flat FIELD row
    between them. Read down the plate and you are reading the word. Two wide reeds never touch and
    three narrow ones never run together; that is balance, and it is meant to be visible without
    counting anything."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_cadence_legendary_preview/shirt_{c}_legendary60.png"), 0).crop(crop),
              f"{c} chest idle") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_cadence_chest.png")


def build_head_zoom():
    """The three cadence helms over the skin head. The dome is where a reeded axis is most at risk
    of eating its own visor, because the reeds run across the face at the same scale as the eye
    slit. Check that the slit still reads as a slit: no stop in this palette is near black (darkest
    channel-sums 218 / 312 / 206), which is what leaves the finishing pass somewhere dark to put
    it."""
    crop = (28, 14, 52, 34)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), 0))
        base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), 0))
        base.alpha_composite(frame(_open(f"_cadencedome_helmet_preview/helmet_{c}_legendary60.png"), 0))
        cells.append((base.crop(crop), f"{c} helm"))
    _zoom(cells, crop, 12, "_ZOOM_cadence_head.png")


# --------------------------------------------------------------------------------------------
def _chest_plate():
    """The warrior chest as a bare component, cropped to its bounding box — the plate both panels
    below are painted on."""
    import sys
    sys.path.insert(0, "scripts")
    import numpy as np
    import gen_cadence_axis60 as G
    base = G.load_any("armor_chest_4.png")
    src = base[0:FH, 0:FW]
    a = src[..., 3] > 0
    comp = next(iter(G.comps_of(a, True)))
    ys, xs = np.nonzero(comp)
    y0, x0, y1, x1 = int(ys.min()), int(xs.min()), int(ys.max()), int(xs.max())
    return G, np, comp[y0:y1 + 1, x0:x1 + 1]


def build_word_zoom():
    """THE ACCEPTANCE TEST, DRAWN — the panel to judge this batch by.

    The same warrior chest, painted five times through the same code path: once from the axis's own
    word and once from each of the four controls. Under each cell is the number of distinct subwords
    of length 1..5 that the sequence has in the limit. The axis is the cell reading 2,3,4,5,6.

    The cell to actually look at is RATIONAL. It is slope 3/5 — a Fibonacci convergent, the closest
    a whole-number pitch can come to this axis without being it. It is balanced, no two wide reeds
    touch, no three narrow ones run together, and on a plate this size it is very nearly
    indistinguishable by eye. It saturates at length 5: five subwords where the axis has six,
    because a periodic word can only ever have as many subwords as its period. That is the whole
    reason the acceptance test counts a LANGUAGE and not a picture.
    """
    G, np, sub = _chest_plate()
    stops = G.CADENCE["warrior"]
    names = [("cadence", "CADENCE  (this axis)"),
             ("uniform", "UNIFORM  = axis 11 fluting"),
             ("alternating", "ALTERNATING = axis 38"),
             ("rational", "RATIONAL  slope 3/5"),
             ("random", "RANDOM  = axis 46 craquelure")]
    cells, subs = [], []
    for mode, label in names:
        wd = G.Word(mode)
        fr = np.zeros((sub.shape[0], sub.shape[1], 4), dtype=np.uint8)
        G.paint_cadence(fr, sub, stops, word=wd)
        seq = [wd.run(0, 4000)]
        f = [len(G.factors(seq, n)) for n in range(1, 6)]
        nn = sum(1 for c in seq[0] if c == G.NARROW)
        ratio = nn / float(max(4000 - nn, 1))
        cells.append(fr)
        subs.append((label, f, ratio, mode == "cadence"))
        print("   word panel: %-12s complexity %s  ratio %.4f" % (mode, f, ratio))

    Z = 11
    h, w = sub.shape
    cw, chh = w * Z, h * Z
    pad = 14
    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    cell_w = max([cw + pad] + [probe.textbbox((0, 0), lb, font=font(12))[2] + pad + 6
                               for lb, _, _, _ in subs])
    lines = [("THE ACCEPTANCE TEST: exactly n+1 distinct subwords of length n. Only the first cell "
              "manages it — that is what 'aperiodic, and minimally so' means.",
              (150, 200, 255, 255), 15),
             ("Look at RATIONAL. Slope 3/5, a convergent of the golden ratio: balanced, no WW, no "
              "NNN, and by eye it is this axis. It saturates at length 5 (five, not six).",
              (255, 190, 120, 255), 13),
             ("Every control also misses the golden frequency by more than 0.05 — so each is "
              "excluded twice over, on the sequence AND on how often the two reeds turn up.",
              (170, 170, 185, 255), 12)]
    text_w = max(probe.textbbox((0, 0), t, font=font(sz))[2] for t, _, sz in lines)
    text_h = sum(sz + 5 for _, _, sz in lines) + pad
    canvas = Image.new("RGBA", (max(pad + len(cells) * cell_w, text_w + 2 * pad),
                                pad + chh + 60 + text_h), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for fr, (label, f, ratio, is_axis) in zip(cells, subs):
        canvas.alpha_composite(Image.fromarray(fr).resize((cw, chh), Image.NEAREST), (x, pad))
        col = (255, 190, 120, 255) if is_axis else (200, 200, 210, 255)
        d.text((x + 2, pad + chh + 5), label, font=font(12), fill=col)
        d.text((x + 2, pad + chh + 22), "|F(n)| = " + ",".join(str(v) for v in f),
               font=font(12), fill=(140, 200, 150, 255) if is_axis else (190, 130, 130, 255))
        d.text((x + 2, pad + chh + 38), "N:W = %.3f" % ratio, font=font(12),
               fill=(140, 200, 150, 255) if is_axis else (190, 130, 130, 255))
        x += cell_w
    ty = pad + chh + 60
    for line, col, sz in lines:
        d.text((pad, ty), line, font=font(sz), fill=col)
        ty += sz + 5
    canvas.convert("RGB").save("_ZOOM_cadence_word.png")
    print("wrote _ZOOM_cadence_word.png", canvas.size)


def build_censor_zoom():
    """THE ESTIMATOR BUG, DRAWN — why clause 4 is measured on run interiors.

    The first acceptance run over this batch FAILED clause 4: narrow to wide came back 1.752 against
    phi = 1.618. Nothing was wrong with the armour. A reed is only readable if the silhouette leaves
    all of its rows on the plate, and a WIDE reed is three rows where a NARROW reed is two — so a
    wide reed is systematically likelier to be clipped and thrown away. The sample was censored by
    an event whose probability depends on the very quantity being measured.

    Three cells of the same chest: every reed the word places; the subset that survives to be read;
    and the run interiors, which are the reeds admitted because their NEIGHBOURS were readable and
    not because of their own width. The numbers under them are the batch figures, not this plate's.
    """
    G, np, sub = _chest_plate()
    stops = G.CADENCE["warrior"]
    fr = np.zeros((sub.shape[0], sub.shape[1], 4), dtype=np.uint8)
    info = G.paint_cadence(fr, sub, stops)
    read, _ = G.read_word(fr, sub, stops, info)
    runs = G.runs_of(read)
    inter = G.interiors_of(runs)

    # Which BAND each pixel belongs to, so a reed can be greyed out cell by cell.
    ys, xs = np.nonzero(sub)
    tr = G.t_real(xs, ys, G.DIRV)
    T = np.floor(tr - float(tr.min())).astype(np.int64)
    cuts = info["cuts"]
    reed_of = {}
    for j in range(len(info["letters"])):
        for t in range(cuts[j], cuts[j + 1]):
            reed_of[t] = j
    readable = set(j for j, v in enumerate(read) if v is not None)
    # a reed is "interior" iff it and both neighbours are readable
    interior = set(j for j in readable if (j - 1) in readable and (j + 1) in readable)

    def masked(keep):
        out = fr.copy()
        for k, (yy, xx) in enumerate(zip(ys, xs)):
            j = reed_of.get(int(T[k]))
            if j is None or j not in keep:
                out[yy, xx, :3] = (56, 56, 64)
        return out

    allj = set(range(len(info["letters"])))
    cells = [(masked(allj), "1  every reed the word places", "batch 3182:1947 = 1.634"),
             (masked(readable), "2  the reeds that are READABLE", "batch 2062:1177 = 1.752  FAIL"),
             (masked(interior), "3  RUN INTERIORS", "batch  813: 504 = 1.613  PASS")]
    print("   censor panel: %d reeds placed / %d readable / %d interior on this plate"
          % (len(allj), len(readable), len(interior)))

    Z = 11
    h, w = sub.shape
    cw, chh = w * Z, h * Z
    pad = 14
    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    cell_w = max([cw + pad] + [probe.textbbox((0, 0), lb, font=font(12))[2] + pad + 6
                               for _, lb, _ in cells])
    lines = [("A STATISTIC READ OFF A CENSORED SAMPLE IS THE STATISTIC OF THE CENSORING.",
              (150, 200, 255, 255), 15),
             ("A wide reed is 3 rows where a narrow reed is 2, so the silhouette clips wide reeds "
              "more often and the readable sample leans narrow — by construction, not by design.",
              (170, 170, 185, 255), 13),
             ("The fix is not a wider tolerance. Clause 4 is asked of reeds whose NEIGHBOURS were "
              "readable, which the clipping cannot bias; it then agrees with ground truth to 0.005,",
              (170, 170, 185, 255), 12),
             ("so the tolerance was TIGHTENED 0.12 -> 0.05, and the rational control now fails on "
              "frequency as well as on complexity.", (140, 200, 150, 255), 12)]
    text_w = max(probe.textbbox((0, 0), t, font=font(sz))[2] for t, _, sz in lines)
    text_h = sum(sz + 5 for _, _, sz in lines) + pad
    canvas = Image.new("RGBA", (max(pad + len(cells) * cell_w, text_w + 2 * pad),
                                pad + chh + 44 + text_h), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for a, label, fig in cells:
        canvas.alpha_composite(Image.fromarray(a).resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 5), label, font=font(12),
               fill=(255, 190, 120, 255) if label.startswith("3") else (200, 200, 210, 255))
        d.text((x + 2, pad + chh + 22), fig, font=font(12),
               fill=(140, 200, 150, 255) if "PASS" in fig or label.startswith("1")
               else (190, 130, 130, 255))
        x += cell_w
    ty = pad + chh + 44
    for line, col, sz in lines:
        d.text((pad, ty), line, font=font(sz), fill=col)
        ty += sz + 5
    canvas.convert("RGB").save("_ZOOM_cadence_censor.png")
    print("wrote _ZOOM_cadence_censor.png", canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_word_zoom()
    build_censor_zoom()


if __name__ == "__main__":
    main()
