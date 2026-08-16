#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-FIFTH net-new-geometry axis batch
(CASCADE family — the engraving is not laid out, it is GROWN: every row of the field is the image
of the row above it under one fixed nearest-neighbour rule, and each class is a different rule).

*** THE DELIVERABLE, AND WHY IT HAS TWO EXTRA PANELS. ***
The 62nd could not be judged on one sheet and its evidence became a dressed character. The 63rd
could not be judged on one picture and its evidence became a filmstrip and a GIF. The 64th could be
judged on one picture but not by an eye, because an eye cannot take an exclusive-or, so its evidence
became a decode. This one is the same shape of problem and the opposite answer: everything is in one
picture and no eye can see it, because the claim is not about what the pixels ARE but about what
made them. So:

  _ZOOM_cascade_growth.png       THE LAW CAUGHT WORKING — one real cuirass with its seed row marked
                                 and, printed beside it, the row-by-row derivation: each row of the
                                 plate re-derived from the row above it by the rule recovered from
                                 the pixels, with every cell it got right left plain.
  _ZOOM_cascade_divergence.png   THE EXACT COMPLEMENT OF THE 64th's DECODE PANEL. A pristine
                                 cuirass beside three copies of itself with ONE cell of the seed
                                 row turned over in each. The 64th's panel rings the one stud that
                                 changed and prints its number. This one rings EVERY cell that
                                 changed, and the ring is a widening cone that swallows the plate.
                                 Same question, opposite answer, side by side.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_cascade_axis65 as G                                # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new CASCADE %s (the engraving is GROWN, not laid out: every row of the rib field is "
        "the image of the row above it under one fixed nearest-neighbour rule, so the vertical "
        "direction of the plate is a HISTORY. FIRST AXIS WHOSE INVARIANT IS A CAUSE. Class "
        "identity is the LAW, not the palette - warrior rule 30, mage rule 90, ranger rule 150, "
        "all three recovered from the pixels by a reader that is never told them. The exact "
        "complement of the 64th: there one wrong pixel changes one stud and the plate names it; "
        "here one wrong pixel in the seed rewrites everything beneath it, see "
        "_ZOOM_cascade_divergence.png), 65th %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_cascade_legendary_preview", out="_PREVIEW_cascade_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary65", "Warlord's Cascade Cuirass"),
              ("mage", "shirt_mage_legendary65", "Archmage's Unfolding Mantle"),
              ("ranger", "shirt_ranger_legendary65", "Warden's Downrush Jerkin")],
    ),
    "legs": dict(
        prev="_cascade_legs_preview", out="_PREVIEW_cascade_legs.png",
        note=NOTE % ("CHAUSSES - and the legs are the slot where the axis is easiest to read, "
                     "because they are the tallest plate in the set and the cascade needs ROWS",
                     "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary65", "Warlord's Cascade Chausses"),
              ("mage", "pants_mage_legendary65", "Archmage's Unfolding Leggings"),
              ("ranger", "pants_ranger_legendary65", "Warden's Downrush Chausses")],
    ),
    "boots": dict(
        prev="_cascade_boots_preview", out="_PREVIEW_cascade_boots.png",
        note=NOTE % ("SABATONS - the shortest plate in the set and the one where the law mostly "
                     "cannot be seen: a boot six cells tall shows five rows of consequence and "
                     "the reader reports it as such rather than passing it",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_cascade", "Warlord's Cascade Sabatons"),
              ("mage", "boots_mage_legendary_cascade", "Archmage's Unfolding Striders"),
              ("ranger", "boots_ranger_legendary_cascade", "Warden's Downrush Boots")],
    ),
    "helmet": dict(
        prev="_cascadedome_helmet_preview", out="_PREVIEW_cascadedome_helmet.png",
        note=NOTE % ("HELM - the dome is where the seed row itself is on show, along the very top "
                     "of the skull", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary65", "Warlord's Cascade Helm"),
              ("mage", "helmet_mage_legendary65", "Archmage's Unfolding Crown"),
              ("ranger", "helmet_ranger_legendary65", "Warden's Downrush Hood")],
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
        d.text((pad, y), f"{disp}  ({cls}, HYPER-RARE - {note})",
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


def _zoom(cells, crop, Z, out, caption=None):
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad = 10
    extra = 26 if caption else 0
    canvas = Image.new("RGBA", (pad + len(cells) * (cw + pad), pad + chh + 20 + extra),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    x = pad
    for im, name in cells:
        canvas.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=font(12), fill=(210, 210, 220, 255))
        x += cw + pad
    if caption:
        d.text((pad, pad + chh + 20), caption, font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_chest_zoom():
    """The three cuirasses at pixel scale, one per class — which here is one per LAW."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_cascade_legendary_preview/shirt_{c}_legendary65.png"), 0).crop(crop),
              f"{c} chest idle f0  (rule {G.RULE[c]})") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_cascade_chest.png",
          caption="a rib two pixels wide, lit on the left face or on the right. Runs of like cells "
                  "make ribbing; the dislocations between runs are where the automaton is doing "
                  "something, and they are the ornament.")


def build_head_zoom():
    """The head zone. The visor's black eye and mouth slits must survive the rib field, which is
    why no stop in the palette goes near black (the 49th's lesson)."""
    crop = (28, 14, 56, 42)
    cells = [(frame(_open(f"_cascadedome_helmet_preview/helmet_{c}_legendary65.png"), 0).crop(crop),
              f"{c} helm idle f0") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_cascade_head.png",
          caption="darkest stops are channel-sum 190 / 224 / 200 - the visor slits are the only "
                  "near-black on the sheet and read cleanly through the rib field.")


# --- the two evidence panels ------------------------------------------------------------------
def _plate_setup(cls="warrior", kind="chest", fi=0, pick=0):
    cfg = G.SLOTS[kind]
    base = G.load_any("%s.png" % cfg["srcs"][cls])
    stem = cfg["dst"] % cls
    r, c = fi // COLS, fi % COLS
    src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    comps = [k for k in G.comps_of(a, cfg["largest"]) if k.sum() >= G.MIN_PX]
    comp = sorted(comps, key=lambda m: -int(m.sum()))[pick]
    g = G.grid_of(comp)
    return cfg, src, a, comp, g, stem


def _pooled_table(cls):
    """The rule as the acceptance test recovers it: from every plate of every sheet of the class,
    never from the one picture in the panel. A single 7-row cuirass does not show all eight
    neighbourhoods, and pretending otherwise would be the panel lying about the reader."""
    _tot, per = G.gather(None)
    obs = per[cls]["top"] + per[cls]["bot"]
    tab, bad = G.fit(obs)
    return tab, G.wolfram(tab), len(obs), bad


def _paint(src, a, cls, g, win):
    fr = np.zeros_like(src)
    G.recolor(src, fr, a, *G.BODY[cls])
    crest, shade, _d = G.CASPAL[cls]
    G.paint_cells_pal(fr, g, win, crest, shade)
    return fr


def build_growth_panel(out="_ZOOM_cascade_growth.png", zoom=14, cls="ranger"):
    """*** THE FIRST PIECE OF EVIDENCE. ***

    The plate, with its seed row marked, beside the derivation. Every row under the seed is
    re-computed from the row above it using the rule RECOVERED FROM THE PIXELS — the number is an
    output of the reader, printed here, and never handed to it — and every cell the derivation gets
    right is left plain. Nothing is ringed because nothing is wrong: the point of the panel is that
    the whole plate follows from its top row and eight bits."""
    # The panel has to be shown on the plate that shows the most of the law. That is not a cosmetic
    # choice: on a narrow component almost nothing is verifiable, and a panel built on one of those
    # would be advertising the axis on its worst evidence.
    best = None
    for kind in ("helmet", "chest", "legs"):
        for fi in (0, 12, 41):
            try:
                s = _plate_setup(cls, kind, fi)
            except (IndexError, FileNotFoundError, ValueError):
                continue
            if s[4] is None:
                continue
            n = int(G.verifiable_mask(s[4][2]).sum())
            if best is None or n > best[0]:
                best = (n, kind, fi, s)
    cfg, src, a, comp, g, stem = best[3]
    kind = best[1]
    _y0, _x0, live = g
    orb = G.orbit(stem, cls)
    nr, nc = live.shape
    win = orb[:nr, :nc]
    fr = _paint(src, a, cls, g, win)

    st = G.read_cells(fr, g)
    ver = G.verifiable_mask(live) & (st >= 0)
    tab, num, nobs, bad = _pooled_table(cls)

    crop = (24, 12, 60, 52) if kind == "helmet" else (24, 18, 60, 58)
    x0, y0, x1, y1 = crop
    w, h = x1 - x0, y1 - y0
    pad = 12
    txt_w = 800
    canvas = Image.new("RGBA", (pad + w * zoom + pad + txt_w + pad,
                                pad + max(h * zoom, 44 + 17 * nr) + 46), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    canvas.alpha_composite(Image.fromarray(fr[y0:y1, x0:x1]).resize((w * zoom, h * zoom),
                                                                    Image.NEAREST), (pad, pad))
    gy, gx = g[0] - y0, g[1] - x0
    d.rectangle([pad + gx * zoom - 2, pad + gy * zoom - 2,
                 pad + (gx + nc * G.CELL_W) * zoom + 1, pad + (gy + G.CELL_H) * zoom + 1],
                outline=(120, 255, 170, 255), width=3)
    d.text((pad, pad + h * zoom + 6),
           "the SEED ROW is ringed. everything below it is consequence.",
           font=font(14), fill=(120, 255, 170, 255))

    tx = pad + w * zoom + pad
    d.text((tx, pad), "law recovered from the pixels of the whole %s batch: RULE %s"
           % (cls, num), font=font(15), fill=(150, 200, 255, 255))
    d.text((tx, pad + 21), "%d observations, %d contradictions.   #=RISE  .=FALL   right column: "
           "this row re-derived from the one above, correct/checked"
           % (nobs, bad), font=font(12), fill=(205, 205, 215, 255))
    yy = pad + 44
    for gr in range(nr):
        line = "".join(" " if not live[gr, gc] else ("#" if st[gr, gc] == G.RISE else ".")
                       for gc in range(nc))
        if gr == 0:
            mark, col = "SEED", (120, 255, 170, 255)
        else:
            row = np.array([max(int(v), 0) for v in st[gr - 1]], dtype=np.uint8)
            pred = G.run_recovered(row, tab)
            ncheck = int(ver[gr].sum())
            okc = sum(1 for gc in range(nc) if ver[gr, gc] and int(pred[gc]) == int(st[gr, gc]))
            mark = ("%d/%d" % (okc, ncheck)) if ncheck else "(no verifiable cell)"
            col = (150, 255, 170, 255) if (ncheck and okc == ncheck) else (205, 205, 215, 255)
        d.text((tx, yy), "|%s|" % line, font=font(13), fill=(225, 225, 235, 255))
        d.text((tx + 9 * (nc + 3), yy), mark, font=font(13), fill=col)
        yy += 17
    d.text((pad, canvas.size[1] - 34),
           "eight bits of law and one row of seed produce the whole plate. the rule number is an "
           "OUTPUT of the reader - it is written nowhere the reader can see.",
           font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_divergence_panel(out="_ZOOM_cascade_divergence.png", zoom=14, cls="warrior"):
    """*** THE SECOND PIECE OF EVIDENCE, AND THE ONE THAT EXISTS TO BE PUT NEXT TO THE 64th's. ***

    A pristine cuirass, then three copies with exactly ONE cell of the seed row turned over. The
    64th's decode panel rings the single stud that changed and prints its number, because its
    invariant is redundancy and damage there is local and nameable. This panel rings every cell
    that changed, and what it draws is a cone."""
    cfg, src, a, comp, g, stem = _plate_setup(cls, "legs")
    _y0, _x0, live = g
    nr, nc = live.shape
    orb = G.orbit(stem, cls)
    win = orb[:nr, :nc]
    fr0 = _paint(src, a, cls, g, win)

    seed = G.seed_row(stem)
    rule = G.RULE[cls]
    picks = sorted({max(1, nc // 5), max(2, nc // 2), max(3, (4 * nc) // 5)})

    crop = (24, 18, 60, 58)
    x0, y0, x1, y1 = crop
    w, h = x1 - x0, y1 - y0

    LW, LH, LZ = 32, 26, 6      # the bare lattice strip under each plate: the cone, unclipped
    full0 = orb[:LH, :LW]

    panels = [(fr0[y0:y1, x0:x1].copy(), [], full0, [], "pristine", 0, 0)]
    for i in picks:
        s2 = seed.copy()
        s2[i] ^= 1
        rows = [s2]
        for _ in range(G.LAT_H - 1):
            rows.append(G.step(rows[-1], rule))
        allr = np.array(rows, dtype=np.uint8)
        w2 = allr[:nr, :nc]
        fr2 = _paint(src, a, cls, g, w2)
        diff = [(gr, gc) for gr in range(nr) for gc in range(nc)
                if live[gr, gc] and w2[gr, gc] != win[gr, gc]]
        f2 = allr[:LH, :LW]
        fdiff = np.nonzero(f2 ^ full0)
        panels.append((fr2[y0:y1, x0:x1].copy(), diff, f2, fdiff,
                       "one seed cell turned over (column %d)" % i, len(diff),
                       int((f2 ^ full0).sum())))

    pad, lab = 12, 54
    strip_h = LH * LZ + 22
    canvas = Image.new("RGBA", (pad + len(panels) * (w * zoom + pad),
                                pad + h * zoom + lab + strip_h + 40), (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    gy, gx = g[0] - y0, g[1] - x0
    crest, shade, _dk = G.CASPAL[cls]
    for k, (arr, diff, lat, fdiff, label, ndiff, nfull) in enumerate(panels):
        px = pad + k * (w * zoom + pad)
        canvas.alpha_composite(Image.fromarray(arr).resize((w * zoom, h * zoom), Image.NEAREST),
                               (px, pad))
        for (gr, gc) in diff:
            ry, rx = gy + gr * G.CELL_H, gx + gc * G.CELL_W
            d.rectangle([px + rx * zoom - 1, pad + ry * zoom - 1,
                         px + (rx + G.CELL_W) * zoom, pad + (ry + G.CELL_H) * zoom],
                        outline=(255, 90, 90, 255), width=2)
        col = (150, 255, 170, 255) if ndiff == 0 else (255, 170, 120, 255)
        d.text((px + 2, pad + h * zoom + 4), "%d cells changed on the plate" % ndiff,
               font=font(14), fill=col)
        d.text((px + 2, pad + h * zoom + 24), label, font=font(12), fill=(205, 205, 215, 255))

        # the bare lattice: the same orbit with nothing cropping it, so the cone is visible whole
        sy = pad + h * zoom + lab
        img = np.zeros((LH, LW, 3), dtype=np.uint8)
        img[lat == G.RISE] = crest
        img[lat == G.FALL] = shade
        for (ry, rx) in zip(*fdiff):
            img[ry, rx] = (255, 90, 90)
        canvas.alpha_composite(
            Image.fromarray(img).convert("RGBA").resize((LW * LZ, LH * LZ), Image.NEAREST),
            (px, sy))
        d.text((px + 2, sy + LH * LZ + 3),
               ("the orbit itself, uncropped" if nfull == 0
                else "%d of %d lattice cells changed" % (nfull, LW * LH)),
               font=font(12), fill=(205, 205, 215, 255) if nfull == 0 else (255, 140, 140, 255))
    d.text((pad, canvas.size[1] - 32),
           "the 64th TALLY answers this question with the number 1 and prints the address of the "
           "stud it names. this axis answers it with a CONE. redundancy buys the location of an "
           "error; determinism buys the whole plate for eight bits and a seed row. neither is free.",
           font=font(14), fill=(150, 200, 255, 255))
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def main():
    for kind, cfg in SETS.items():
        build(kind, cfg)
    build_chest_zoom()
    build_head_zoom()
    build_growth_panel()
    build_divergence_panel()


if __name__ == "__main__":
    main()
