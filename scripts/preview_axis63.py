#!/usr/bin/env python3
"""Daily-approval preview panels for the SIXTY-THIRD net-new-geometry axis batch
(CURRENT family — level bands whose PHASE advances with the animation frame, by P/L, so that the
pattern closes on exactly one period at the end of every loop).

*** THE DELIVERABLE IS DIFFERENT AGAIN, AND FOR A DIFFERENT REASON THAN THE 62nd's. ***
The 62nd could not be judged on one SHEET, so its evidence became a dressed character. This one
cannot be judged on one PICTURE at all — clause INVISIBLE says so as a requirement — so the still
grids below are, correctly, indistinguishable from the 11th FLUTING, and they are not the evidence.
The evidence is:

  _ZOOM_current_strip.png   THE AXIS DRAWN — one whole loop in a row, dressed, with the topmost
                            crest ringed in every frame so the eye can follow it up the plate, and
                            the loop's FIRST FRAME REPEATED at the end, because in the game it is
                            the next frame. Underneath, the same loop under CONSTANT-SPEED. The
                            two rows are identical in kind and differ only in where the band is.
                            IT PLAYS THE IDLE (L = 5) AND NOT THE WALK, and that is not
                            flattering: L = 8 is the one loop CONSTANT-SPEED gets right, so on the
                            walk the two rows are the same picture and there is nothing to see.
                            Naming the loop the control survives is worth more than picking the
                            loop it fails worst.
  _ANIM_current_walk.gif    THE AXIS MOVING — the only artefact in sixty-three axes that has to be
                            played rather than looked at. Two characters side by side, the axis on
                            the left and CONSTANT-SPEED on the right, both looping the idle: the
                            left one runs smoothly forever, the right one hitches once every five
                            frames, and no still of either shows it.

Nothing here touches sprites/preview_assets/char or git."""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_current_axis63 as G                                # noqa: E402
from sprite_finish import finish_array                        # noqa: E402

CH = "sprites/preview_assets/char"
FW, FH, COLS = 80, 64, 10
FRAMES = [(0, "idle"), (12, "walk"), (22, "run"), (41, "cheer"), (52, "slash")]

NOTE = ("net-new CURRENT %s (level bands whose PHASE TRAVELS with the animation: step P/L, so the "
        "pattern closes on exactly ONE period at the end of every loop — 5, 8, 4 and 6 frames long, "
        "four different speeds, none of them written down. FIRST AXIS WHOSE INVARIANT IS NOT A "
        "PROPERTY OF ANY PICTURE: these stills are SUPPOSED to look like plain fluting — see "
        "_ZOOM_current_strip.png and _ANIM_current_walk.gif), 63rd %s axis (repaint, QA-safe)")

SETS = {
    "chest": dict(
        prev="_current_legendary_preview", out="_PREVIEW_current_legendary.png",
        note=NOTE % ("CUIRASS", "chest"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "shirt_warrior_legendary63", "Warlord's Emberflow Cuirass"),
              ("mage", "shirt_mage_legendary63", "Archmage's Arclight Mantle"),
              ("ranger", "shirt_ranger_legendary63", "Warden's Wispfire Jerkin")],
    ),
    "legs": dict(
        prev="_current_legs_preview", out="_PREVIEW_current_legs.png",
        note=NOTE % ("CHAUSSES", "legs"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "pants_warrior_legendary63", "Warlord's Emberflow Chausses"),
              ("mage", "pants_mage_legendary63", "Archmage's Arclight Leggings"),
              ("ranger", "pants_ranger_legendary63", "Warden's Wispfire Chausses")],
    ),
    "boots": dict(
        prev="_current_boots_preview", out="_PREVIEW_current_boots.png",
        note=NOTE % ("SABATONS — six rows tall, which is one and a third periods: the smallest "
                     "piece in the game shows barely one band, and it still has to close",
                     "boots"),
        crop=(10, 8, 70, 60), cw=60, ch=52,
        rows=[("warrior", "boots_warrior_legendary_current", "Warlord's Emberflow Sabatons"),
              ("mage", "boots_mage_legendary_current", "Archmage's Arclight Striders"),
              ("ranger", "boots_ranger_legendary_current", "Warden's Wispfire Boots")],
    ),
    "helmet": dict(
        prev="_currentdome_helmet_preview", out="_PREVIEW_currentdome_helmet.png",
        note=NOTE % ("HELM — the dome is the shortest travel in the suit and the easiest place to "
                     "watch a band leave the top", "helmet"),
        crop=(6, 2, 74, 60), cw=68, ch=58,
        rows=[("warrior", "helmet_warrior_legendary63", "Warlord's Emberflow Helm"),
              ("mage", "helmet_mage_legendary63", "Archmage's Arclight Crown"),
              ("ranger", "helmet_ranger_legendary63", "Warden's Wispfire Hood")],
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
    """The three cuirasses at pixel scale, one frame each. What to look for is NOT the pattern —
    it is a plain band, on purpose — but the relief: a bright crest with its own one-row shade
    directly under it, every 4.5 rows, and a field dark enough that a crest moving one pixel is a
    visible event."""
    crop = (28, 20, 56, 48)
    cells = [(frame(_open(f"_current_legendary_preview/shirt_{c}_legendary63.png"), 0).crop(crop),
              f"{c} chest idle f0") for c in ("warrior", "mage", "ranger")]
    _zoom(cells, crop, 10, "_ZOOM_current_chest.png",
          caption="a still of this axis is a still of the 11th FLUTING — that is clause INVISIBLE, "
                  "and it is a requirement, not a defect")


def build_head_zoom():
    """The three helms over the skin head. Check the visor still reads: no stop in this palette is
    near black (darkest channel-sums 214 / 226 / 208), which is what leaves the finishing pass
    somewhere dark to put the slits."""
    crop = (28, 14, 52, 34)
    cells = []
    for c in ("warrior", "mage", "ranger"):
        base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), 0))
        base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), 0))
        base.alpha_composite(frame(_open(f"_currentdome_helmet_preview/helmet_{c}_legendary63.png"),
                                   0))
        cells.append((base.crop(crop), f"{c} helm"))
    _zoom(cells, crop, 12, "_ZOOM_current_head.png")


# --- the evidence -----------------------------------------------------------------------------
SUIT = (("chest", "armor_chest_4", "shirt_warrior_legendary63"),
        ("legs", "armor_pants_4", "pants_warrior_legendary63"),
        ("boots", "armor_boots_4", "boots_warrior_legendary_current"),
        ("helmet", "helmet_rare1", "helmet_warrior_legendary63"))


def _sheets(mode):
    """Build the whole warrior suit in memory under `mode` (None = the axis), finished."""
    out = {}
    for kind, src, dst in SUIT:
        base = G.load_any(f"{src}.png")
        arr = G.build(base, G.SLOTS[kind], "warrior", mode=mode)
        arr, _ = finish_array(arr, f"{dst}.png")
        out[kind] = Image.fromarray(arr)
    return out


def _dressed(sheets, fi):
    base = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    base.alpha_composite(frame(_open(f"{CH}/skin_m1.png"), fi))
    base.alpha_composite(frame(sheets["legs"], fi))
    base.alpha_composite(frame(sheets["boots"], fi))
    base.alpha_composite(frame(sheets["chest"], fi))
    base.alpha_composite(frame(_open(f"{CH}/hair_m1.png"), fi))
    base.alpha_composite(frame(sheets["helmet"], fi))
    return base


TORSO = (22, 46)          # the rows the cuirass occupies; the comb is read here and nowhere else


def _crest_rows(sheets, fi, kind="chest"):
    """EVERY crest row of the cuirass on frame fi, in frame coordinates — the comb.

    Found by looking for the palette's crest stop rather than by asking the generator where it put
    it: the marker on the strip has to be measured off the picture like everything else, or it is
    a caption drawing itself.

    The first version of this marker ringed only the TOPMOST crest, and it jumped about, because
    the topmost crest is not a thing that persists — when the comb travels up, the top tooth
    leaves the plate and the one below it becomes "topmost". Marking the WHOLE comb fixes it and
    is more honest anyway: what travels is the pattern, not a band, and there is no band to
    follow. (This is the same mistake, in a new place, as the 61st reader segmenting hoops at
    their seams: measuring a feature the ornament does not actually have.)"""
    arr = np.array(sheets[kind])
    r, c = fi // COLS, fi % COLS
    sub = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    crest = np.array(G.CURPAL["warrior"][0], dtype=np.int32)
    pal = np.array(G.CURPAL["warrior"], dtype=np.int32)
    out = []
    for y in range(TORSO[0], TORSO[1]):
        px = sub[y][sub[y, :, 3] > 0][:, :3].astype(np.int32)
        if not len(px):
            out.append(None)
            continue
        r = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
        out.append(int(np.bincount(r, minlength=3).argmax()))
    return out


def build_strip(out="_ZOOM_current_strip.png", cycle="idle", Z=6):
    """THE AXIS DRAWN. The frames of one loop in a row, dressed, under the axis and under the
    CONSTANT-SPEED control, with the topmost chest crest ringed in each frame.

    Read it left to right and watch the ring climb; then read the LAST cell and the FIRST cell as
    if they were adjacent, because in the game they are. Under the axis the step from the last back
    to the first is the same step as all the others. Under the control it is not, and that is the
    hitch."""
    name, f0, L = [c for c in G.CYCLES if c[0] == cycle][0]
    axis, ctrl = _sheets(None), _sheets("const-speed")
    crop = (26, 6, 58, 62)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad, head, lab = 10, 54, 20
    seq = list(range(L)) + [0]
    canvas = Image.new("RGBA", (pad + 18 + len(seq) * (cw + pad) + pad, head + 2 * (chh + lab + pad) + pad),
                       (24, 24, 30, 255))
    d = ImageDraw.Draw(canvas)
    d.text((pad, 8), "THE %s LOOP, %d FRAMES + THE WRAP.  Above: CURRENT (step P/%d, one whole "
                     "period per loop).  Below: CONSTANT-SPEED (step P/8, always)."
           % (name.upper(), L, L), font=font(15), fill=(150, 200, 255, 255))
    d.text((pad, 28), "The strip beside each figure is the cuirass's own crest/shade/field profile, "
                      "MEASURED off that picture. The last cell is frame %d again — the next frame "
                      "the game shows. Above, the comb steps into it evenly; below, it jumps."
           % f0, font=font(13), fill=(200, 200, 210, 255))
    for row, (sheets, tag, col) in enumerate(((axis, "CURRENT", (150, 255, 180, 255)),
                                              (ctrl, "CONSTANT-SPEED", (255, 160, 150, 255)))):
        yy = head + row * (chh + lab + pad)
        for j, k in enumerate(seq):
            fi = f0 + k
            x = pad + 18 + j * (cw + pad)
            cell = _dressed(sheets, fi).crop(crop).resize((cw, chh), Image.NEAREST)
            canvas.alpha_composite(cell, (x, yy))
            # THE COMB, drawn as the thing it is: the cuirass's own role profile, one block per
            # row, read off this very picture. Left to right it walks up by one even step, and
            # the last cell — the wrap — takes one more.
            for i, r in enumerate(_crest_rows(sheets, fi)):
                if r is None:
                    continue
                ry = yy + (TORSO[0] + i - crop[1]) * Z
                d.rectangle([x - 16, ry, x - 5, ry + Z - 1],
                            fill=(col if r == G.R_CREST else
                                  ((90, 60, 60, 255) if r == G.R_SHADE else (48, 48, 56, 255))))
            lb = "%s f%d" % (tag if j == 0 else "", fi)
            if j == len(seq) - 1:
                lb = "-> f%d (the wrap)" % fi
            d.text((x + 2, yy + chh + 2), lb, font=font(12), fill=col)
    canvas.convert("RGB").save(out)
    print("wrote", out, canvas.size)


def build_gif(out="_ANIM_current_walk.gif", cycle="idle", Z=6, ms=140):
    """THE AXIS MOVING. Two characters looping side by side: the axis and CONSTANT-SPEED.

    The IDLE loop is used and not the walk, deliberately. L = 8 is the one loop CONSTANT-SPEED gets
    right, so on the walk the two are identical and there is nothing to show; on the idle (L = 5)
    the control closes 5/8 of a period and hitches once every five frames. Naming the loop the
    control survives is more useful than choosing the one where it looks worst."""
    name, f0, L = [c for c in G.CYCLES if c[0] == cycle][0]
    axis, ctrl = _sheets(None), _sheets("const-speed")
    crop = (26, 6, 58, 62)
    cw, chh = (crop[2] - crop[0]) * Z, (crop[3] - crop[1]) * Z
    pad, lab = 12, 26
    frames = []
    for k in range(L):
        fi = f0 + k
        im = Image.new("RGBA", (pad * 3 + 2 * cw, pad + chh + lab), (24, 24, 30, 255))
        im.alpha_composite(_dressed(axis, fi).crop(crop).resize((cw, chh), Image.NEAREST),
                           (pad, pad))
        im.alpha_composite(_dressed(ctrl, fi).crop(crop).resize((cw, chh), Image.NEAREST),
                           (pad * 2 + cw, pad))
        d = ImageDraw.Draw(im)
        d.text((pad, pad + chh + 4), "CURRENT", font=font(13), fill=(150, 255, 180, 255))
        d.text((pad * 2 + cw, pad + chh + 4), "CONSTANT-SPEED", font=font(13),
               fill=(255, 160, 150, 255))
        frames.append(im.convert("P", palette=Image.ADAPTIVE))
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=ms, loop=0)
    print("wrote %s  (%s loop, %d frames, %dms)" % (out, name, L, ms))


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for kind, cfg in SETS.items():
        if only in (None, kind):
            build(kind, cfg)
    if only is None:
        build_chest_zoom()
        build_head_zoom()
        build_strip()
        build_gif()


if __name__ == "__main__":
    main()
