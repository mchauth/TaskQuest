#!/usr/bin/env python3
"""FIFTY-SECOND net-new-geometry axis for ALL FOUR SLOTS — the AJOURE family (openwork: a PIERCED
top plate over a SECOND SURFACE): the armour is a solid sheet that has been fretted through with a
field of small square openings, and behind it, seen only through those openings, lies a LINING of a
different material carrying a texture of its own.

    the ornament is  WEB    (the surviving 2px bars of the pierced top plate, with a lit lip on the
                             edge that overhangs each opening and a dull one on the far side)
                   + VOID   (the opening itself, a hole cut clean through the plate)
                   + LINER  (a SECOND SURFACE at a lower depth, a different metal with its own
                             45-degree grain, CONTINUOUS underneath the whole piece and visible
                             only in the gaps)
                   + CAST SHADOW (the top plate's lip throwing shade onto the liner below it)

*** THIS IS THE FIRST AXIS WITH TWO SURFACES. OCCLUSION IS THE SUBJECT. ***
All fifty-one prior axes model ONE skin. However elaborate they get, every pixel on the piece
belongs to the same continuous surface and its tone is a statement about the SHAPE of that one
surface: the 11th flute is that skin folded, the 37th coffer is that skin sunk, the 46th craquelure
is that skin broken, the 47th mokume is that skin's boundary read inward, the 51st flowgrain is that
skin's grain. Depth in all fifty-one is RELIEF — a few tenths of a pixel of modelled height on a
single sheet. Here there are two sheets at two different depths with air between them, and a pixel's
first question is not "where on the surface am I" but "WHICH SURFACE AM I ON". That is a categorical
difference, not a decorative one, and it buys the one thing relief cannot: a pixel of the lower
surface tells you about a place the upper surface is NOT.

The families it could be confused with, and why each fails:
  * The OUTLINE-NET axes — 14th lattice, 19th honeycomb, 20th trellis, 21st chainmail, 17th ashlar —
    are the obvious near miss, because a fret is also a net with holes in it. Two things separate
    them and both are visible at 1x. First, their member is a 1px LINE: a drawn boundary between
    cells of the same body, with nothing inside it but the body itself. The member here is a 2px
    BAR carrying its own two-stop relief (lit lip / dull back), which is what makes it read as a
    SHEET that has been pierced rather than as a line that has been drawn. Second, and decisively,
    what shows in the holes of a net axis is the body — the same material, the same tone, phase-
    locked to the net because it IS the net's ground. What shows in these holes is a DIFFERENT
    MATERIAL with a DIFFERENT HUE and A PATTERN OF ITS OWN, and that pattern is NOT phase-locked to
    the openings: the liner's grain runs at 45 degrees on a period of 3 while the openings sit
    square on a period of 4, so the liner steps one pixel from each opening to the next and threads
    diagonally across the plate right THROUGH the intervening bars. Two neighbouring holes of a net
    axis are identical; two neighbouring holes here are different, and the difference is exactly the
    amount the hidden surface has moved. That mismatch is the evidence of a continuous thing behind,
    and it is the whole axis.
  * The 37th COFFER and the 45th ARCADE are recesses — a panel or a niche sunk into the plate. Their
    floor is the SAME material one level down: it takes a darker stop off the SAME ramp, it is
    uniform within a cell, and it is necessarily identical in every cell, because a recess has no
    existence apart from the thing it is recessed into. A liner does: it has its own ramp, its own
    hue, and its own pattern which does not know or care where the openings are.
  * The 13th STUDWORK is the exact inverse operation — material ADDED on a grid rather than REMOVED
    — and the inverse of a hole is a boss, not a second surface.
  * The 26th TARTAN and the 33rd OCTAGRAM do superpose two line families, but they superpose them
    IN THE SAME PLANE, so the result is one merged pattern in which both families are visible
    everywhere and their crossings are the interesting part. Here the second family is visible
    NOWHERE except through the first, there are no crossings, and the relation between them is not
    overlay but occlusion.

THE MARGIN. Every piece carries a SOLID FRAME one pixel wide around its whole silhouette: no
opening is ever cut at the boundary. This is how real ajoure work is made — a fretted panel with no
margin has no strength and falls apart at the edge — and it does two other jobs. It keeps the
brightest stop off the silhouette edge, the standing rule since the 47th. And it is the reason this
axis cannot be mistaken for the 47th mokume even though both know about the outline: mokume's whole
figure is a function of distance-to-edge and every band is a copy of the boundary, whereas here the
boundary buys exactly one pixel of frame and the field inside it is a square lattice that owes the
outline nothing.

Geometry. On the component's bounding box, with BAR = 2 and OPEN = 2 so the period is P = 4:

    hole   = (y mod P >= BAR) and (x mod P >= BAR)
    shadow = the hole pixel at (BAR, BAR) of its cell — the corner nearest the light, which the
             overhanging lip shades (the light is upper-left everywhere in this set)
    liner  = liner_hi where (x + y) mod 3 == 0, else liner_lo
    lip    = a web pixel with a hole directly BELOW or RIGHT of it   (the overhanging edge, lit)
    back   = a web pixel with a hole directly ABOVE or LEFT of it    (the far edge, turned away)
    web    = the remaining web pixels: the crossing nodes of the fret
    margin = any pixel on the silhouette boundary, or on a 1px protrusion, forced to `web`

Authoring philosophy identical to gen_flowgrain_axis51.py / gen_runic_axis50.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body, so nothing is ever actually cut out — the
"hole" is painted, not deleted. The generator therefore CANNOT create isolated pixels, background
bleed, extra components or a changed silhouette; it is QA-safe by construction. Sleep frames
(fi >= 60) get a plain body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()` — the canonical chain
(no-smooth shading with protect=False, shirt pauldron/gorget/chest-plate separation, helmet black
eye+mouth visor with NO full-silhouette rim, hat brim/crease folds for open headgear). See
CONTEXT.md "MANDATORY - the finishing pass".

Run from repo root:
  python3 scripts/gen_ajoure_axis52.py
  python3 scripts/gen_ajoure_axis52.py --cells     # ASCII dump of the cell + the liner-phase stats
  python3 scripts/gen_ajoure_axis52.py --swatch    # bare motif on a test plate, no sheets
  python3 scripts/gen_ajoure_axis52.py --sweep     # BAR/OPEN sweep on a real torso AND a real leg
Then QA (examples):
  python3 scripts/sprite_qa.py _ajoure_legendary_preview/shirt_warrior_legendary52.png
  python3 scripts/sprite_qa.py _ajouredome_helmet_preview/helmet_mage_legendary52.png --y-min 2
  python3 scripts/sprite_qa.py _ajoure_boots_preview/boots_warrior_legendary_ajoure.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# --- Ajoure constants -----------------------------------------------------------------------
# BAR is the width of the surviving web, OPEN the side of the square hole; the lattice period is
# their sum. Swept (--sweep) on a real torso AND a real leg. Both ends of the sweep fail, and — as
# with the 49th, 50th and 51st — they fail INTO older axes rather than into mush:
#   BAR 1 / OPEN 2 (P=3)  a 1px web is a LINE, not a pierced sheet. It cannot carry the lit-lip /
#                         dull-back pair that says "this is a plate with thickness", so the relief
#                         collapses and what is left is a drawn grid over a darker ground: the 14th
#                         LATTICE. The second surface is still there but nothing signals that it is
#                         a second surface, and the axis evaporates.
#   BAR 2 / OPEN 2 (P=4)  three hole columns across a 13px torso and four down a thigh, web bars
#                         carrying both their stops, and the liner's period-3 grain stepping one
#                         pixel per opening so the diagonal is legible across three holes — chosen.
#   BAR 2 / OPEN 3 (P=5)  only two hole columns survive on a torso inside the margin, and at that
#                         count a row of large dark squares in a light field stops reading as a
#                         pierced sheet and starts reading as sunken panels: the 37th COFFER.
#   BAR 3 / OPEN 3 (P=6)  one hole column on a torso, none on a boot. Not a field at all.
#   BAR 2 / OPEN 4 (P=6)  the hole is wide enough that the liner shows four grain pixels and the
#                         eye resolves the liner as the SUBJECT with a frame around it, which is
#                         the 45th ARCADE's figure-ground, not this one's.
BAR = 2
OPEN = 2
P = BAR + OPEN

# The liner's grain: broad bright bands on the anti-diagonal, LINER_W wide on a period of LINER_P,
# measured in the SAME component-local frame as the openings.
#
# THE LINER'S GRAIN MUST BE COARSER THAN THE APERTURE. This is the lesson the first cut paid for.
# It ran a 1px grain on a period of 3, which is a perfectly good texture and completely wrong here:
# an opening is 2x2 and shows three pixels of liner, so a fine grain puts one bright pixel somewhere
# different inside each hole and the plate comes out SPARKLING — the eye reads scattered glints, not
# a surface. Continuity across an occluder can only be read at a scale the occluder does not
# destroy, so the grain has to be legible at the scale of the HOLE GRID rather than of the pixel:
# at LINER_P 7 / LINER_W 3 a band covers two to three openings, so a run of holes lights up together
# along a diagonal while their neighbours stay dark, and THAT the eye joins into one surface passing
# behind the bars.
#
# THE TWO PERIODS MUST STAY COPRIME. If the liner's period shared a factor with the opening period
# the grain would be phase-locked to the lattice: every hole would show the identical pixels, the
# liner would become part of the cell, and the piece would collapse into a one-surface axis with a
# slightly fussier cell — precisely the 37th coffer, whose floor is also the same in every panel.
# gcd(7, 4) = 1, so the liner's phase advances by three pixels from each opening to the next and the
# hole appearances cycle with period 7 along the diagonal instead of repeating.
LINER_P = 7
LINER_W = 3

# A component needs at least this many INTERIOR pixels (pixels with all four 4-neighbours inside the
# component) before it is given the solid 1px margin. Measured on the real idle frames: chest 78,
# helmet dome 59, legs 39 — all comfortably framed; boots 2 to 8, because a foot at this scale is
# four or five pixels across and is ALL boundary. Framing a boot leaves it a flat recolor with not
# one opening on it, which is not a slot delivery. So a component with no real interior keeps the
# openings and gives up the frame, and the standing edge rule is honoured the other way instead: on
# an unframed component no boundary pixel may take the bright `lip` stop. This is also what real
# ajoure work does — the pierced field lives on the broad plates and the small fittings are pierced
# right out to their edge, because there is nowhere else for the piercing to go.
MARGIN_MIN = 20

# Per class, six stops: (lip, web, back, shadow, liner_hi, liner_lo).
#   * The plate and the liner are DIFFERENT MATERIALS, not two stops of one ramp. That is the point
#     of the axis and it has to be carried by HUE, because at 13px a luminance step alone reads as
#     shading. Each class pairs a plate metal with a contrasting liner metal.
#   * No stop is near pure black. HELMET constraint, not taste: the finishing pass carves the visor
#     as black eye and mouth pixels, and a near-black stop on the dome swallows the face slit (the
#     49th's lesson). The `shadow` stop is the darkest thing here and it still clears sum 150.
#   * The pale plate stops are kept off the skin ramp — cool greys, lilac and green-birch, never a
#     warm off-white, which on a narrow female chest reads as bare shoulder (the 47th's rose gold).
#   * `shadow` is a DARKENED LINER TONE, not a darkened plate tone. The shadow falls ON the lower
#     surface, so it has to belong to the lower surface's ramp; a plate-coloured shadow inside the
#     hole reads as more plate and closes the hole up. First cut had it plate-grey on all three and
#     the ranger holes in particular went to a single dark blob.
#   * THE LINER IS IN SHADE AND MUST BE PAINTED THAT WAY. First cut ran the liner at mid luminance
#     — brass at 150, teal at 190 — on the reasoning that a second metal should be able to hold its
#     own. It cannot: an opening filled with a tone as bright as the plate stops reading as an
#     OPENING and reads as an INLAY, a stone set into the surface, and the axis silently becomes the
#     13th studwork with coloured bosses. A hole is dark first and coloured second. Every liner stop
#     therefore sits at or below the plate's darkest stop (`back`), which is also physically
#     correct: it is a surface underneath a plate that is shadowing it.
AJOURE = {
    # blued steel fretwork over a brass lining
    'warrior': ((196, 208, 226), (134, 144, 166), (88, 96, 118),
                (64, 52, 30), (140, 110, 54), (98, 76, 38)),
    # moonsilver-lilac tracery over an arcane teal lining
    'mage':    ((208, 204, 228), (150, 144, 180), (100, 96, 132),
                (26, 56, 66), (58, 128, 132), (38, 86, 96)),
    # green-birch fretwork over a slate-blue lining
    'ranger':  ((196, 204, 146), (134, 144, 96), (88, 98, 60),
                (38, 44, 74), (80, 92, 144), (56, 64, 104)),
}

# Per-class body (ground) tones for the recolor, visible on sleep frames only; taken off the plate
# stops so the piece reads as one object when the fretwork is not drawn.
BODY = {
    'warrior': ((62, 68, 86), (146, 156, 176), (206, 216, 232)),
    'mage':    ((54, 50, 84), (168, 162, 196), (228, 224, 244)),
    'ranger':  ((54, 66, 48), (146, 156, 104), (206, 212, 158)),
}

# One config block per slot. `largest` restricts the field to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_ajoure_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary52', largest=True,
    ),
    'legs': dict(
        outdir='_ajoure_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary52', largest=False,
    ),
    'boots': dict(
        outdir='_ajoure_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_ajoure', largest=False,
    ),
    'helmet': dict(
        outdir='_ajouredome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary52', largest=True,
    ),
}

# role codes
R_WEB, R_LIP, R_BACK, R_SHADOW, R_LINER_HI, R_LINER_LO = 0, 1, 2, 3, 4, 5


def role_field(h, w, bar=None, open_=None, liner_p=None, liner_w=None):
    """Classify every pixel of an h x w box into one of the six roles.

    The lattice is square and lives in the component's own frame, so the fretwork is registered to
    the piece rather than to the sprite sheet. `lip` and `back` are derived from ADJACENCY to a
    hole rather than from a residue, so they stay correct for any BAR/OPEN in the sweep."""
    bar = BAR if bar is None else bar
    open_ = OPEN if open_ is None else open_
    lp = LINER_P if liner_p is None else liner_p
    lw = LINER_W if liner_w is None else liner_w
    p = bar + open_
    yy, xx = np.mgrid[0:h, 0:w]
    my, mx = yy % p, xx % p
    hole = (my >= bar) & (mx >= bar)

    role = np.full((h, w), R_WEB, dtype=np.int8)

    # --- the liner, seen through the holes -------------------------------------------------
    # (x + y) is constant along the anti-diagonal, so the grain runs '/' — 45 degrees off the
    # square fret above it, which is the second, purely visual half of the depth cue: two families
    # at two ANGLES as well as two depths cannot be read as one merged in-plane pattern.
    role[hole] = np.where(((xx + yy) % lp < lw)[hole], R_LINER_HI, R_LINER_LO)

    # --- the cast shadow --------------------------------------------------------------------
    # Light is upper-left, so the lip that overhangs the top-left of each opening shades the floor
    # nearest it. For a 2px hole that is the single corner pixel; for a wider hole it is the top
    # row and left column, an L, exactly as a real cut edge shades.
    if open_ >= 3:
        role[hole & ((my == bar) | (mx == bar))] = R_SHADOW
    else:
        role[hole & (my == bar) & (mx == bar)] = R_SHADOW

    # --- the two web stops ------------------------------------------------------------------
    below = np.zeros_like(hole)
    right = np.zeros_like(hole)
    above = np.zeros_like(hole)
    leftm = np.zeros_like(hole)
    below[:-1, :] = hole[1:, :]
    right[:, :-1] = hole[:, 1:]
    above[1:, :] = hole[:-1, :]
    leftm[:, 1:] = hole[:, :-1]
    web = ~hole
    lip = web & (below | right)
    back = web & ~lip & (above | leftm)
    role[lip] = R_LIP
    role[back] = R_BACK
    return role


def paint_ajoure(fr, comp, stops, bar=None, open_=None, liner_p=None, liner_w=None):
    """Paint the openwork onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette — the holes are painted, not cut.

    The MARGIN is applied last and overrides everything: any pixel on the component's boundary, and
    any pixel on a 1px protrusion, takes the solid `web` stop. That is how a real fretted panel is
    made (a pierced sheet with no margin has no edge strength), it keeps the brightest stop off the
    silhouette per the standing rule, and it keeps the darkest stop off it too — so no piece ever
    grows the full-silhouette dark rim that mangles patterned helmet domes."""
    if comp.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp)
    y0, x0 = int(ys.min()), int(xs.min())
    h = int(ys.max()) - y0 + 1
    w = int(xs.max()) - x0 + 1
    role = role_field(h, w, bar, open_, liner_p, liner_w)

    lip, web, back, shadow, lin_hi, lin_lo = stops
    table = (web, lip, back, shadow, lin_hi, lin_lo)

    # boundary of the component (4-neighbourhood) and 1px protrusions
    left = np.zeros_like(comp)
    right = np.zeros_like(comp)
    up = np.zeros_like(comp)
    down = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    up[1:, :] = comp[:-1, :]
    down[:-1, :] = comp[1:, :]
    interior = comp & left & right & up & down
    margin_m = comp & ~interior
    thin_m = comp & ~(left & right)
    framed = int(interior.sum()) >= MARGIN_MIN

    for y, x in zip(ys, xs):
        r = int(role[int(y) - y0, int(x) - x0])
        if thin_m[y, x] or (framed and margin_m[y, x]):
            rgb = web
        elif (not framed) and margin_m[y, x] and r == R_LIP:
            # unframed component: openings run to the edge, but the brightest stop still never
            # lands on the silhouette, or the piece grows a detached bright rim (47th / 49th)
            rgb = web
        else:
            rgb = table[r]
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free).
    Returns (labels int32 array, n). Background (False) is label 0."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    n = 0
    stack = []
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and labels[sy, sx] == 0:
                n += 1
                labels[sy, sx] = n
                stack.append((sy, sx))
                while stack:
                    y, x = stack.pop()
                    if y > 0 and mask[y - 1, x] and labels[y - 1, x] == 0:
                        labels[y - 1, x] = n
                        stack.append((y - 1, x))
                    if y < h - 1 and mask[y + 1, x] and labels[y + 1, x] == 0:
                        labels[y + 1, x] = n
                        stack.append((y + 1, x))
                    if x > 0 and mask[y, x - 1] and labels[y, x - 1] == 0:
                        labels[y, x - 1] = n
                        stack.append((y, x - 1))
                    if x < w - 1 and mask[y, x + 1] and labels[y, x + 1] == 0:
                        labels[y, x + 1] = n
                        stack.append((y, x + 1))
    return labels, n


def load_any(fname):
    """Load a source sheet; if the female (_f) variant is absent (warrior boots are a
    single gender-shared sheet), fall back to the base sheet."""
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    stops = AJOURE[cls]
    largest = cfg['largest']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        if fi >= 60:                            # sleep: body only
            continue
        if largest:
            lbl, n = label4(a)
            if n >= 1:
                counts = np.bincount(lbl.ravel())
                counts[0] = 0
                comp = (lbl == int(counts.argmax()))
            else:
                comp = a
        else:
            comp = a
        paint_ajoure(fr, comp, stops)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ----------------------------------------------------------------------------
def _test_plate(w=44, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the
    fretwork can be judged on a shape that has the features real slots have — including a boundary
    long enough to show what the solid margin does."""
    m = np.zeros((h, w), dtype=bool)
    yy, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False          # neck notch
    return m


def swatch(path='_diag_ajoure_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the web relief, the cast
    shadow and — the thing that actually has to work — the liner's diagonal threading from one
    opening to the next can be judged before any sheet is written."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_ajoure(a, m, AJOURE[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def sweep(path='_diag_ajoure_sweep.png', zoom=11):
    """Render the warrior chest idle frame at a range of bar/opening sizes, plus a leg frame, so
    the lattice can be judged on a real piece: at the fine end on whether the web still reads as a
    plate rather than a line, and at the coarse end on whether enough openings survive inside the
    solid margin for the field to be a field."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    for bar, opn in ((1, 2), (2, 2), (2, 3), (3, 3), (2, 4)):
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comp = (lbl == int(counts.argmax())) if n else a
            fr = np.zeros_like(src)
            paint_ajoure(fr, comp, AJOURE['warrior'], bar=bar, open_=opn)
            col.append(Image.fromarray(fr).crop(crop))
        cells.append(('BAR=%d OPEN=%d' % (bar, opn), col))
    cw, ch = 28 * zoom, 26 * zoom
    pad, lab = 8, 18
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + 2 * (ch + lab)), (24, 24, 28, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
    except Exception:
        f = ImageFont.load_default()
    x = pad
    for name, col in cells:
        y = pad
        for im in col:
            img.alpha_composite(im.resize((cw, ch), Image.NEAREST), (x, y))
            d.text((x + 2, y + ch), name, font=f, fill=(210, 210, 220, 255))
            y += ch + lab
        x += cw + pad
    img.convert('RGB').save(path)
    print('wrote %s (bar/open sweep - no sheets written)' % path)


def dump_cells():
    """ASCII dump of the role field plus the liner-phase statistics.

    The phase table is the actual acceptance test for this axis. If the number of DISTINCT hole
    appearances is 1, the liner is phase-locked to the openings, every hole looks the same, and the
    piece has collapsed into a one-surface axis (the 37th coffer with a fussier floor). It must be
    LINER_P, i.e. 3, and the appearances must cycle along a diagonal so the eye can join them up."""
    legend = {R_WEB: 'o', R_LIP: '#', R_BACK: '=', R_SHADOW: ' ', R_LINER_HI: '*', R_LINER_LO: '.'}
    for label, (hh, ww) in (('torso 13x20', (20, 13)), ('plate 30x44', (30, 44))):
        role = role_field(hh, ww)
        print('== %s   BAR=%d OPEN=%d P=%d LINER_P=%d LINER_W=%d'
              % (label, BAR, OPEN, P, LINER_P, LINER_W))
        for y in range(hh):
            print('   ' + ''.join(legend[int(v)] for v in role[y]))
    print('legend: # lip (lit, overhangs the hole)  = back (far edge)  o node')
    print('        (space) cast shadow  * liner bar  . liner ground')
    # liner phase per opening, over an 8x8 block of cells
    N = 8
    role = role_field(P * N, P * N)
    sigs = {}
    for cy in range(N):
        for cx in range(N):
            blk = role[cy * P + BAR:cy * P + P, cx * P + BAR:cx * P + P]
            sigs.setdefault(tuple(blk.ravel().tolist()), []).append((cy, cx))
    print('distinct hole appearances over an %dx%d block of openings: %d   (gcd(P=%d, LINER_P=%d)=%d)'
          % (N, N, len(sigs), P, LINER_P, np.gcd(P, LINER_P)))
    print('  1 would mean the liner is PHASE-LOCKED to the openings and the axis has collapsed')
    print('  into a one-surface cell (the 37th coffer). Wanted: LINER_P distinct appearances,')
    print('  cycling along the anti-diagonal so consecutive holes share a band.')
    for i, (sig, at) in enumerate(sorted(sigs.items(), key=lambda kv: min(kv[1]))):
        nhi = sum(1 for v in sig if v == R_LINER_HI)
        print('   appearance %d: %d of %d liner px lit, first at cell (cy=%d, cx=%d), %d of %d openings'
              % (i + 1, nhi, len(sig), at[0][0], at[0][1], len(at), N * N))


def main():
    if '--cells' in sys.argv:
        dump_cells()
        return
    if '--swatch' in sys.argv:
        swatch()
        return
    if '--sweep' in sys.argv:
        sweep()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                # save_finished() rather than a bare .save(): it writes the TaskQuestFinish
                # version stamp, without which a later bulk `sprite_finish.py <dir>` backfill
                # would run the whole chain over these sheets a SECOND time.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
