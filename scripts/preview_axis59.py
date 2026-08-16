#!/usr/bin/env python3
"""Daily-approval preview grids for the FIFTY-NINTH net-new-geometry axis batch
(COUNTERCHANGE family — a two-tincture vair that TRADES PLACES across an undrawn division: chest
surcoat, legs chausses, boots sabatons, helmet helm). For each class and gender: full dressed avatar
across idle/walk/run/cheer/slash, plus one isolated slot-over-skin so the net-new relation — that
the metal on one side of the line is doing exactly what the colour is doing on the other — is clear.
Emits four _PREVIEW_counterchange_*.png plus a chest zoom, a head zoom, and the FOLD panel, which
draws the acceptance clause itself. Nothing here touches sprites/preview_assets/char or git."""
import os
from PIL import Image, ImageDraw, ImageFont

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new COUNTERCHANGE %s (a two-tincture heraldic vair covering the piece edge to edge, "
        "and somewhere across it the metal and the colour TRADE PLACES — no line is drawn, the "
        "division is visible only because the fur on one side is doing the opposite of the fur on "
        "the other; FIRST AXIS WHOSE SYMMETRY IS AN ANTISYMMETRY, i.e. the first whose invariance "
        "belongs to neither the shapes nor the palette but only to both together), 59th %s axis "
        "(repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_counterchange_legendary_preview", out="_PREVIEW_counterchange_legendary.png",
        note=NOTE % ("SURCOAT", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary59", "Warlord's Or-and-Azure Counterchanged Surcoat"),
              ("mage", "shirt_mage_legendary59", "Archmage's Argent-and-Purpure Counterchanged Mantle"),
              ("ranger", "shirt_ranger_legendary59", "Warden's Or-and-Vert Counterchanged Jerkin")],
    ),
    "legs": dict(
        prev="_counterchange_legs_preview", out="_PREVIEW_counterchange_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary59", "Warlord's Or-and-Azure Counterchanged Chausses"),
              ("mage", "pants_mage_legendary59", "Archmage's Argent-and-Purpure Counterchanged Leggings"),
              ("ranger", "pants_ranger_legendary59", "Warden's Or-and-Vert Counterchanged Chausses")],
    ),
    "boots": dict(
        prev="_counterchange_boots_preview", out="_PREVIEW_counterchange_boots.png",
        note=NOTE % ("SABATONS — and note that on a boot the division is not on the piece at all: "
                     "the pair is too small to be folded, so the LEFT boot carries the fur and the "
                     "RIGHT boot carries its negative, and the line runs between them, in the air",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_cchange", "Warlord's Or-and-Azure Counterchanged Sabatons"),
              ("mage", "boots_mage_legendary_cchange", "Archmage's Argent-and-Purpure Counterchanged Striders"),
              ("ranger", "boots_ranger_legendary_cchange", "Warden's Or-and-Vert Counterchanged Field-Boots")],
    ),
    "helmet": dict(
        prev="_cchangedome_helmet_preview", out="_PREVIEW_cchangedome_helmet.png",
        note=NOTE % ("HELM", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary59", "Warlord's Or-and-Azure Counterchanged Helm"),
              ("mage", "helmet_mage_legendary59", "Archmage's Argent-and-Purpure Counterchanged Crown"),
              ("ranger", "helmet_ranger_legendary59", "Warden's Or-and-Vert Counterchanged Hood-Helm")],
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
    """The three counterchanged surcoats at pixel scale. What to look for: find the column (or row)
    where the fur stops phasing the way it was phasing and starts doing the opposite. That is the
    division. Nothing is drawn on it — no line, no seam, no rivet — and it is still the most
    conspicuous thing on the piece once you have seen it."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_counterchange_legendary_preview/shirt_{c}_legendary59.png"), 0).crop(crop),
              f"{c} chest idle") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_counterchange_chest.png")


def build_head_zoom():
    """The three counterchanged helms over the skin head. A dome is the hardest slot for this axis
    for a reason no previous one had: half the head is now a saturated dark COLOUR, and the finishing
    pass carves the visor as near-black pixels. The thing to check is that the eye slit reads as a
    slit on BOTH halves — over the metal, where it is easy, and over the colour, where the three
    colour edges clearing channel-sum 150 is the only thing keeping it visible."""
    crop = (28, 14, 52, 34)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), 0))
        base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), 0))
        base.alpha_composite(frame(_open(f"_cchangedome_helmet_preview/helmet_{c}_legendary59.png"), 0))
        cells.append((base.crop(crop), f"{c} helm"))
    _zoom(cells, crop, 12, "_ZOOM_counterchange_head.png")


def build_fold_zoom():
    """THE ACCEPTANCE CLAUSE, DRAWN, and the panel to judge this batch by.

    Four cells of the same warrior chest.
      1  THE PIECE.
      2  THE PIECE FOLDED — reflected about its own division. Every shape lands on a shape, and
         every one of them is the wrong tincture. So the fold is NOT a symmetry.
      3  THE PALETTE SWAPPED — the gold made blue and the blue gold, nothing moved. Nothing lines
         up with anything. So the swap is NOT a symmetry either.
      4  BOTH AT ONCE — and it is cell 1 again, pixel for pixel.

    That is the whole axis in four pictures: an invariance that belongs to neither the geometry nor
    the colouring, only to their product. Hold cell 4 against cell 1; they are the same image, and
    neither 2 nor 3 is.
    """
    import sys
    sys.path.insert(0, "scripts")
    import numpy as np
    import gen_counterchange_axis59 as G

    stops = G.CCHANGE["warrior"]
    base = G.load_any("armor_chest_4.png")
    comp = G._big_comp(base)
    ys, xs = np.nonzero(comp)
    y0, x0, y1, x1 = int(ys.min()), int(xs.min()), int(ys.max()), int(xs.max())
    sub = comp[y0:y1 + 1, x0:x1 + 1]
    fr = np.zeros((sub.shape[0], sub.shape[1], 4), dtype=np.uint8)
    info = G.paint_cchange(fr, sub, stops)

    # *** THIS PANEL IS DRAWN ON TINCTURE ALONE, FLAT, WITH NO RELIEF AND NO EDGE DEMOTION, AND
    # THAT IS NOT A SIMPLIFICATION FOR THE VIEWER — IT IS THE CLAIM BEING MADE. *** The first
    # version of this panel used the finished pixels and cell 4 came back NOT equal to cell 1, on
    # 37 of 135 pixels. Nothing was wrong with the sheet. The tone is not part of the ornament: the
    # shade is cast by a light from above, which a per-fess fold turns upside down, and the edge
    # tone is set by the silhouette, which no reflection of an asymmetric body preserves. The
    # acceptance test reads TINCTURE off the pixels and is blind to tone by construction (the 58th
    # reads a hand and is blind to colour, for the mirror-image reason), so the panel that certifies
    # it must be blind to tone too, or it is certifying something else.
    tflat = np.zeros_like(fr)
    pal = np.array(stops, dtype=np.int32)
    py, px = np.nonzero(fr[..., 3] > 0)
    idx = ((fr[py, px, :3].astype(np.int32)[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
    for k, (yy0, xx0) in enumerate(zip(py, px)):
        tflat[yy0, xx0, :3] = stops[G.R_A if G.FAMILY[int(idx[k])] == 0 else G.R_B]
        tflat[yy0, xx0, 3] = 255

    def swap(a):
        out = a.copy()
        m = np.all(a[..., :3] == stops[G.R_A], axis=-1) & (a[..., 3] > 0)
        n = np.all(a[..., :3] == stops[G.R_B], axis=-1) & (a[..., 3] > 0)
        out[m, :3] = stops[G.R_B]
        out[n, :3] = stops[G.R_A]
        return out

    def fold(a):
        h, w = a.shape[:2]
        out = np.zeros_like(a)
        yy, xx = np.mgrid[0:h, 0:w]
        oy, ox = G.op_apply(info["op"], yy, xx)
        ok = (oy >= 0) & (oy < h) & (ox >= 0) & (ox < w)
        out[yy[ok], xx[ok]] = a[oy[ok], ox[ok]]
        return out

    c2, c3, c4 = fold(tflat), swap(tflat), swap(fold(tflat))
    sup = (tflat[..., 3] > 0) & (c2[..., 3] > 0)
    same4 = bool(np.array_equal(c4[sup], tflat[sup]))
    same2 = bool(np.array_equal(c2[sup], tflat[sup]))
    same3 = bool(np.array_equal(c3[sup], tflat[sup]))
    print("   fold panel: cell4==cell1 %s   cell2==cell1 %s   cell3==cell1 %s   (%d px witnessed)"
          % (same4, same2, same3, int(sup.sum())))

    panels = [(tflat, "1  the piece"),
              (c2, "2  folded — NOT a symmetry"),
              (c3, "3  swapped — NOT one either"),
              (c4, "4  BOTH  =  cell 1 exactly")]
    lines = [("THE ANTISYMMETRY: the fold alone is not a symmetry, the exchange alone is not a "
              "symmetry, and the two composed ARE one.", (150, 200, 255, 255), 15),
             ("Division: %s. Nothing is drawn on it. It is simply the only place the piece can be "
              "laid on its own negative." % G.op_name(info["op"]), (170, 170, 185, 255), 13),
             ("Drawn on TINCTURE only — flat, no relief, no edge tone. The light comes from outside "
              "the ornament and is no part of it; the test is blind to tone for the same reason.",
              (150, 150, 165, 255), 12),
             ("checked in code on this very panel: cell4==cell1 %s / cell2==cell1 %s / "
              "cell3==cell1 %s, over %d witnessed pixels"
              % (same4, same2, same3, int(sup.sum())), (140, 200, 150, 255), 12)]
    Z = 13
    h, w = sub.shape
    cw, chh = w * Z, h * Z
    pad = 14
    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    text_w = max(probe.textbbox((0, 0), t, font=font(sz))[2] for t, _, sz in lines)
    cell_w = max([cw + pad] + [probe.textbbox((0, 0), nm, font=font(12))[2] + pad + 6
                               for _, nm in panels])
    canvas = Image.new("RGBA", (max(pad + len(panels) * cell_w, text_w + 2 * pad),
                                pad + chh + 26 + 68), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for a, name in panels:
        canvas.alpha_composite(Image.fromarray(a).resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 5), name, font=font(12),
               fill=(255, 190, 120, 255) if name.startswith("4") else (200, 200, 210, 255))
        x += cell_w
    ty = pad + chh + 26
    for line, col, sz in lines:
        d.text((pad, ty), line, font=font(sz), fill=col)
        ty += sz + 5
    canvas.convert("RGB").save("_ZOOM_counterchange_fold.png")
    print("wrote _ZOOM_counterchange_fold.png", canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_fold_zoom()


if __name__ == "__main__":
    main()
