#!/usr/bin/env python3
"""FIFTY-SEVENTH net-new-geometry axis for ALL FOUR SLOTS — the FESTOON family (HANGING SWAGS):
a few chains are hung across the piece between studded anchors, and every one of them SAGS. The
sag is not a style. It is a consequence: a chain hung between two points that are further apart
hangs deeper, and hangs RELATIVELY deeper, because the weight it has to carry grows with its own
length while the anchors do not move. Nothing on this armour is laid out. Everything on it is
HUNG, and it has therefore been hung the only way it can be.

    the ornament is  LINK   (the chain itself, one pixel of it per column, sagging)
                   + LIP    (its lit upper edge — a chain is round and the light is above)
                   + BOSS   (the studded anchor the chain is hung FROM, at each end of a swag)
                   + SHADE  (the core shadow the chain casts on the plate, one pixel under it)
                   + CAST   (that shadow WIDENED at the belly, where the chain hangs slackest and
                             therefore stands furthest off the plate — so the shadow's own WIDTH
                             is a second, independent reading of the sag)
                   + FIELD  (the plate or velvet the chain is hung against)

*** THIS IS THE FIRST AXIS THAT HAS AN UP. ***
Take any one of the fifty-six and turn the sheet a half-turn. A honeycomb is the same honeycomb. A
granulated field is the same field. The 54th's wire has the same route, the 55th's bands the same
order, the 56th's straps go through the same holes. What changes is the LIGHTING, and only the
lighting: every prior axis is a GEOMETRY that is invariant under a half-turn, dressed in a lit
flank that is not. Every one of them could be worn upside down and the ornament would be intact.
This one cannot. Turn a festoon a half-turn and the chains ARCH, springing upward off their studs
and holding themselves there — and there is nothing in the picture holding them, so the picture is
simply wrong. The subject is not the elements, nor how they relate, nor the order they were laid
in, nor which side of the surface they are on. The subject is that the ornament is subject to a
FORCE THAT COMES FROM OUTSIDE IT, and the whole field records the direction of that force.

Two consequences follow, and both of them are checkable against the pixels:
  1. PENDENCY. Every swag's lowest point is strictly below both of its own anchors. This is the
     bare statement that the ornament has an up, and it is exactly what the FLIP control breaks.
  2. THE SPAN LAW. Sag is a function of span, and a non-decreasing one: of two chains hung on the
     same piece, the one hung wider hangs deeper. And the family is NOT SIMILAR — sag grows faster
     than span, so a long swag is relatively deeper as well as absolutely deeper, and no swag on
     the piece is a scaled copy of any other. This is what the UNIFORM control breaks, and it is
     the difference between a hanging chain and a repeated arc.

Every near miss fails on something COUNTED.
  * The 34th SEIGAIHA — the reflex answer, since it is a field of arcs. Its arcs are CONGRUENT and
    laid on a half-drop LATTICE: one arc is authored, then stamped. Here no two swags of different
    span are congruent and none of them is on a lattice — an anchor sits where the BODY's own edge
    at that row puts it, so the piece's own width chooses the span and the span chooses the sag.
    The UNIFORM control in --sweep IS the 34th seigaiha: hold the sag constant, change nothing
    else, and the axis is gone while every arc is still there.
  * The 22nd WAVE — a continuous curve running across the piece, and the sharpest formal near
    miss, because a sine is exactly the thing a festoon is not: it is symmetric about its own
    midline, so it is its OWN half-turn, and its crests and troughs are interchangeable. A festoon
    is asymmetric by construction — round bellies pointing down, sharp cusps pointing UP at the
    studs — and a viewer can tell which way is up from the ornament alone.
  * The 15th SCALE and 31st OGEE — curved cells with a z-order or a pinch, but congruent, on a
    lattice, and orientation-free in the same way the seigaiha is.
  * The 41st BEAD-AND-REEL and 30th CABLE — genuinely threaded strings, and both STRAIGHT and
    PERIODIC: the string's route is stated by two numbers and it does not know where it is on the
    body. Here two chains on the same piece have different shapes because they are hung in
    different places.
  * The 53rd GRANULATION — the closest thing in the set to "the element's size is an output", and
    it fails on two counts. Its output is a SCALAR (a radius) read off the local distance
    transform, and its beads are SIMILAR — a big bead is a small bead scaled up. Here the output
    is a CURVE, the quantity that determines it is the SPAN BETWEEN TWO ANCHORS rather than the
    room at a point, and the family is not similar (sag/span itself grows with span).
  * The 47th MOKUME — shape-conformal, so the silhouette determines the ornament there too. Tone
    is a function of DISTANCE TO THE EDGE, which is a scalar field with no direction in it at all;
    turn the piece any way you like and the mokume is unchanged.
  * The 8th SIDE-STRIPE, 10th CROSS, 12th BANDED-LAMELLAR — straight members between two points.
    The TAUT control in --sweep pulls every chain tight and lands precisely here: same anchors,
    same count, same palette, zero sag, and the piece is a set of straps again.
  * The 7th LACE-BOOTS and 6th BALDRIC — a named accessory in a fixed place, not a field.

Geometry, per connected component, in the component's own frame:
    tiers      rows every TIER_P down the component, the first at an OFFSET chosen per component
               from a ladder (below)
    anchors    on a tier row, the component's own opaque run at that row, INSET 1px so the studs
               sit on plate rather than on the silhouette; the run is divided into
               round(L / SPAN_TARGET) swags, so a wide row carries more chains and a narrow row
               fewer, and every anchor position is read off the body
    swag       between two anchors, a shallow catenary: y = y0 + SAG * (1 - u^2), u in [-1, 1]
    sag        SAG = clamp(round(span^2 / SAG_DEN), 1, SAG_MAX) — the span SQUARED, which is the
               shallow-catenary law and the reason the family is not similar
    relief     LIP above the chain, SHADE one pixel below it along its whole length, and CAST — a
               second shadow row below the belly only, present where |u| <= BELLY

Authoring philosophy identical to gen_slotwork_axis56.py / gen_strata_axis55.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing is added, nothing removed,
the silhouette is untouched, so the generator CANNOT create isolated pixels, background bleed,
extra components or a changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain
recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Thirteenth generator to call it in-line, after axes 45-56.

Run from repo root:
  python3 scripts/gen_festoon_axis57.py
  python3 scripts/gen_festoon_axis57.py --cells    # ASCII dump + the EQUILIBRIUM acceptance test
  python3 scripts/gen_festoon_axis57.py --accept   # that test over every component of every frame
  python3 scripts/gen_festoon_axis57.py --swatch   # bare motif on a test plate, no sheets
  python3 scripts/gen_festoon_axis57.py --sweep    # tier/span sweep + FLIP/TAUT/UNIFORM controls
Then QA (examples):
  python3 scripts/sprite_qa.py _festoon_legendary_preview/shirt_warrior_legendary57.png
  python3 scripts/sprite_qa.py _festoondome_helmet_preview/helmet_mage_legendary57.png --y-min 2
  python3 scripts/sprite_qa.py _festoon_boots_preview/boots_warrior_legendary_festoon.png --y-max 63
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

# --- Festoon constants ------------------------------------------------------------------------
# Vertical spacing of the tiers a chain is hung from. It has to clear the DEEPEST swag plus its
# two shadow rows, or one tier's belly lands in the next tier's studs and the two chains read as
# one broken zigzag — which is the 44th ZIGZAG, and this axis's entire claim is that its members
# are CURVED and hang.  TIER_P >= SAG_MAX + 3 is therefore a hard constraint, not a taste.
TIER_P = 7
SAG_MAX = 4

# The shallow-catenary law: sag grows with the SQUARE of the span. This is the single most
# important constant in the file and the one the whole axis rests on, so it is worth being exact
# about why it is a square and not a proportion.
#   * sag = k * span  would make every swag a SCALED COPY of every other. The family would be
#     similar, "which chain is longer" would be unanswerable from a cropped view, and the ornament
#     would be a set of arcs whose size happens to vary — the 53rd GRANULATION's relation, moved
#     onto a curve. Similar elements are what forty-odd axes in this set already have.
#   * sag = k * span^2 is what a hanging chain actually does (w*L^2 / 8H for a shallow catenary),
#     and it is the reason a viewer can tell a festoon from a scalloped border at a glance: the
#     long chains are not just bigger, they are DROOPIER.
# SAG_DEN 32 was the first cut and it was tuned on the synthetic test plate, which is 30px tall and
# affords spans of 7 to 12. THE REAL BODIES DO NOT: a 13px torso's opaque run at a tier row, inset,
# is 4 to 9px, so at SAG_DEN 32 every chain on every real slot came out at sag 1 and the span law
# had nothing to say — the fourth time in this series a constant tuned on the test plate did not
# survive contact with the armour. SAG_DEN 20 puts the interesting part of the curve inside the
# range the bodies actually offer: span 4 -> 1, 5 -> 1, 6 -> 2, 7 -> 2, 8 -> 3, 9 -> 4, and the
# clamp only binds at span 10 and up, which happens on a cheer pose and a synthetic plate.
SAG_DEN = 20

# How wide a chain wants to be. A row of length L carries round(L / SPAN_TARGET) chains.
#   SPAN_TARGET 5   three or four little chains across a 13px torso: at 13px each one is 4px wide
#                   with a 1px sag, which is not a hanging chain, it is a row of dots with a dip in
#                   it — the 13th STUDWORK. Also every span comes out equal, which kills the span
#                   law dead: the piece can carry the axis only if its chains DIFFER.
#   SPAN_TARGET 9   CHOSEN. One chain per tier on a torso, a leg and a dome; two on the widest
#                   rows of a cheer pose. Spans then vary from tier to tier because the BODY varies
#                   — a shoulder row is 11px and a waist row is 8 — so the span law is legible on
#                   ONE PIECE, which is what it has to be.
#   SPAN_TARGET 13  one chain per component and no second tier worth having; the piece becomes the
#                   6th BALDRIC, a single named strap.
SPAN_TARGET = 9
# *** MIN_SPAN 4 LEFT EVERY PIECE 80% BARE, AND THAT IS THE 6th BALDRIC. ***
# Rendered on the real slots, MIN_SPAN 4 hung exactly ONE chain on a torso, a leg, a boot and a
# dome: a single deep swag across the shoulders and nothing below it. It is a handsome necklace and
# it is not a field — it is a NAMED ACCESSORY IN A FIXED PLACE, which this set already has four
# times over (6th baldric, 7th sword-belt, 8th side-stripe, 10th cross). The cause is that a torso
# is 13px across the shoulders and 6px at the waist: with the 1px anchor inset, the lower tiers
# offer a 4px run, one short of what a 4px minimum needs, so every tier below the first was
# silently dropped and the offset ladder — correctly, given what it was offered — spent its whole
# budget making the one surviving chain as deep as possible. At MIN_SPAN 3 the waist rows carry a
# short shallow chain, the shoulders carry a long deep one, and THAT PAIR IS THE AXIS: two chains
# on one piece, visibly different, different because the body under them is different.
MIN_SPAN = 3

# The belly: |u| <= BELLY gets the second shadow row. Half the chain's length, so the widened part
# is unmistakably a middle rather than an accident of rounding.
BELLY = 0.5

# A component with fewer than this many INTERIOR pixels is all boundary — a foot at this scale is
# four or five pixels across — and gets the THIN rhythm. Same constant and the same measured reason
# as the 52nd's, 53rd's, 54th's, 55th's and 56th's MARGIN_MIN.
MARGIN_MIN = 20
THIN = dict(tier_p=5, sag_max=2, sag_den=12, span_target=6, min_span=3)
# Last resort for the narrowest components. A single boot at this scale is a 3-to-4px-wide, 6px-tall
# blob of 16 opaque pixels; measured, it takes NO chain at all under either rhythm above, and a slot
# that falls back to a flat recolor is not a weaker version of this axis, it is the absence of it
# (the 54th's "one leg filled, the other a flat recolor" failure). So: anchors at the very edge of
# the run and a 2px minimum span. A 2px chain is O#O with the middle pixel one row down — three
# pixels, and all three of the axis's clauses are still readable off them.
TINY = dict(tier_p=5, sag_max=2, sag_den=6, span_target=4, min_span=2, inset=0)

# *** THE ONE HARD INVARIANT IN THIS FILE, AND IT IS ASSERTED BECAUSE BREAKING IT IS SILENT. ***
# A tier must clear the deepest swag the tier above it can hang, plus that swag's two shadow rows.
# TINY was first written with tier_p 4 against sag_max 2, which leaves a belly and the studs below
# it only TWO rows apart: rendered, the two chains fuse into one continuous zigzag (the 44th
# ZIGZAG, which is precisely the axis this one must not collapse into), and the acceptance test
# then traced one chain onto the other and reported the second as taut — 65 failures, all of them
# on 30px boots, all of them from this one arithmetic slip. It is not a taste, it is a clearance.
for _n, _p in (('TIER_P', dict(tier_p=TIER_P, sag_max=SAG_MAX)), ('THIN', THIN), ('TINY', TINY)):
    assert _p['tier_p'] >= _p['sag_max'] + 3, (
        '%s: tier pitch %d does not clear a sag of %d plus its two shadow rows'
        % (_n, _p['tier_p'], _p['sag_max']))

# The tier OFFSET is chosen per component from this ladder: the offset that hangs the most chains
# on this particular silhouette, ties broken by total sag and then toward the lowest offset, so a
# sheet regenerates identically and male and female agree wherever their masks do. Sixth appearance
# of the adaptive-boundary lesson (52nd MARGIN_MIN, 53rd shot pass, 54th adaptive pitch, 55th
# spread ladder, 56th phase ladder) and it does more work here than anywhere except the 56th:
# MEASURED, at a fixed offset 0 a third of all components hang no chain at all, because whether a
# tier row lands on the wide part of a torso or in the notch under an arm is decided entirely by
# where the first row happens to fall.
OFFSETS = tuple(range(TIER_P))

# Per class, SIX stops: (boss, lip, link, shade, cast, field).
#   * TWO SHADOW STOPS, and this is the first palette in the series to have them. SHADE is the core
#     shadow directly under the chain; CAST is the widened outer row present only at the belly. The
#     55th's lesson said a shadow landing on two different MATERIALS needs two stops; this is the
#     same lesson for a different reason — the shadow here lands on one material and changes its
#     WIDTH, because a slack chain stands further off the plate than a taut one. Giving the two
#     rows one tone makes the widening read as a fat blurry line; giving the outer row one step
#     back from the core makes it read as the chain lifting away. That widening is the third
#     independent statement of the sag on the piece, after the curve itself and the stud spacing.
#   * NO SEVENTH "DEEP" FIELD STOP. Like the 56th, and for a related reason: the field is not a
#     passive background here, it is the thing the chain hangs AGAINST and casts onto, and the two
#     shadow stops are already the field's own ramp. A third field tone in the untouched corners
#     would read as staining.
#   * THE HUE PLAN, chosen against the four tiers this one will sit beside in the grid. 52nd blued
#     steel on slate, 53rd gold on graphite, 54th platinum on oxblood, 55th blackened iron on pale
#     steel, 56th cool steel on hide. All five are METAL ON METAL OR HIDE. This one is metal on
#     TEXTILE — chains hung against velvet — and the fields are accordingly saturated and chromatic
#     rather than neutral: warrior CRIMSON, mage MIDNIGHT SEA-BLUE, ranger MULBERRY-PLUM. No prior
#     tier in the series has a saturated textile field, and at 1x in the inventory grid, where no
#     pattern resolves at all, that is what will read.
#   * THE CHAIN METALS ARE DELIBERATELY THREE DIFFERENT METALS and none of them is the metal that
#     class wore in 54-56: warrior GOLD (54 platinum, 55 blackened iron, 56 cool steel), mage MOON
#     SILVER (54 amber-gold, 55 amethyst, 56 ice-blue), ranger VERDIGRIS BRONZE (54 copper, 55
#     bog-oak, 56 bone). Verdigris green on plum is the one complementary pair in the whole series.
#   * The pale stops stay off the skin ramp — the 47th's lesson. Warrior gold is the risk and it is
#     pushed cool and light (246,226,166) rather than toward the tan the skin ramp sits on, and it
#     appears only on the BOSS, which is a handful of pixels per piece.
#   * NO STOP NEAR PURE BLACK. The finishing pass carves the visor as black eye and mouth pixels,
#     and a near-black darkest stop swallows them (the 49th's lesson). Every class's darkest stop —
#     SHADE — clears channel-sum 150: warrior 154, mage 170, ranger 158.
FESTOON = {
    # gold chains hung against crimson velvet
    'warrior': ((246, 226, 166), (228, 198, 126), (188, 152, 84),
                (78, 36, 40), (92, 44, 46), (118, 54, 56)),
    # moon-silver chains hung against midnight sea-blue
    'mage':    ((238, 244, 255), (206, 216, 238), (162, 176, 204),
                (40, 50, 80), (52, 66, 104), (68, 86, 130)),
    # verdigris-bronze chains hung against mulberry-plum
    'ranger':  ((198, 228, 200), (160, 200, 168), (110, 150, 124),
                (62, 40, 56), (84, 52, 72), (108, 66, 92)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only: the field ramp plus the
# chain's lit tone as the highlight, so the piece still reads as one object when no chain is drawn.
BODY = {
    'warrior': ((84, 38, 42), (118, 54, 56), (214, 186, 120)),
    'mage':    ((46, 58, 92), (68, 86, 130), (198, 208, 230)),
    'ranger':  ((70, 44, 62), (108, 66, 92), (156, 194, 164)),
}

SLOTS = {
    'chest': dict(
        outdir='_festoon_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary57', largest=True,
    ),
    'legs': dict(
        outdir='_festoon_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary57', largest=False,
    ),
    'boots': dict(
        outdir='_festoon_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_festoon', largest=False,
    ),
    'helmet': dict(
        outdir='_festoondome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary57', largest=True,
    ),
}

R_BOSS, R_LIP, R_LINK, R_SHADE, R_CAST, R_FIELD = 0, 1, 2, 3, 4, 5

# The standing edge rule — brightest stop never on the silhouette, darkest stop never on the
# silhouette — applied by DEMOTION on boundary pixels. SHADE demotes to CAST and not to FIELD: a
# shadow that runs off the edge of the piece is still a shadow there, and flattening it would erase
# the relief the sag is read from.
DEMOTE = {R_BOSS: R_LIP, R_LIP: R_LINK, R_LINK: R_LINK,
          R_SHADE: R_CAST, R_CAST: R_CAST, R_FIELD: R_FIELD}

_ROLE_CACHE = {}


def _neighbours(comp):
    left = np.zeros_like(comp)
    right = np.zeros_like(comp)
    up = np.zeros_like(comp)
    down = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    up[1:, :] = comp[:-1, :]
    down[:-1, :] = comp[1:, :]
    return left, right, up, down


def _interior(comp):
    left, right, up, down = _neighbours(comp)
    return comp & left & right & up & down


def _has_interior(comp):
    return int(_interior(comp).sum()) >= MARGIN_MIN


def _runs(row):
    """Contiguous opaque runs of one row, as (x0, x1) inclusive."""
    xs = np.nonzero(row)[0]
    if not len(xs):
        return []
    out = []
    s = p = int(xs[0])
    for x in xs[1:]:
        x = int(x)
        if x == p + 1:
            p = x
        else:
            out.append((s, p))
            s = p = x
    out.append((s, p))
    return out


def sag_for(span, sag_den, sag_max):
    """THE SPAN LAW. Sag grows with the square of the span, clamped so a swag can never reach the
    tier below it. The clamp produces TIES at the long end (two long spans can share a sag) — which
    is why the acceptance test asks for NO INVERSION rather than for strict increase."""
    return int(min(sag_max, max(1, int(round(span * span / float(sag_den))))))


def _layout_once(comp, off, tier_p, sag_max, sag_den, span_target, min_span, inset,
                 flip=False, taut=False, uniform=0, linear=False):
    """Hang the chains on one component at one tier offset.

    A swag is only hung if EVERY pixel of its curve lands on the piece — a chain needs something to
    hang against along its whole length, and a chain that disappears into the background halfway
    along is not a shorter chain, it is a broken one. That completeness rule is also what makes the
    acceptance test below non-trivial: every swag that reaches the sheet has a curve that can be
    read end to end.
    """
    h, w = comp.shape
    rows = np.nonzero(comp.any(axis=1))[0]
    if not len(rows):
        return []
    top, bot = int(rows.min()), int(rows.max())
    swags = []
    y = top + off
    while y <= bot:
        for (rx0, rx1) in _runs(comp[y]):
            # *** THE INSET IS A PREFERENCE, NOT A RULE, AND THAT IS THE DIFFERENCE BETWEEN
            # CHAUSSES AND A BELT. *** The studs sit one pixel inside the edge so they land on
            # plate rather than on the silhouette (which is also what keeps the brightest stop off
            # the outline). But a single chausse leg is FOUR pixels across: inset it and there is
            # nothing left to hang anything between, so at inset 1 the legs slot came out as one
            # chain at the waist and two bare legs below it — a sword-belt, i.e. the 7th axis. Where
            # the inset leaves no room, the studs go on the edge instead. A stud at the edge of a
            # 4px plate is what a real chain mount looks like at that size anyway.
            got = False
            for ins in ((inset, 0) if inset else (0,)):
                ax0, ax1 = rx0 + ins, rx1 - ins
                L = ax1 - ax0 + 1
                if L >= min_span + 1:
                    got = True
                    break
            if not got:
                continue
            nsw = max(1, int(round(L / float(span_target))))
            anchors = [ax0 + int(round(j * (L - 1) / float(nsw))) for j in range(nsw + 1)]
            for j in range(nsw):
                a, b = anchors[j], anchors[j + 1]
                span = b - a
                if span < min_span:
                    continue
                if taut:
                    sag = 0
                elif uniform:
                    sag = int(min(sag_max, uniform))
                elif linear:                     # CONTROL: sag = span/3, a SIMILAR family
                    sag = int(min(sag_max, max(1, int(round(span / 3.0)))))
                else:
                    sag = sag_for(span, sag_den, sag_max)
                curve = {}
                xm = (a + b) / 2.0
                ok = True
                for x in range(a, b + 1):
                    u = 2.0 * (x - xm) / span
                    dy = int(round(sag * (1.0 - u * u)))
                    yc = y - dy if flip else y + dy
                    if not (0 <= yc < h) or not comp[yc, x]:
                        ok = False
                        break
                    curve[x] = yc
                if ok:
                    swags.append(dict(y0=y, a=a, b=b, span=span, sag=sag, curve=curve))
        y += tier_p
    return swags


# A chain hung from two studs that COINCIDE is a chain hung from one stud, and it hangs straight
# down. That is not a second kind of ornament bolted on to rescue the small pieces — it is this
# axis's own element at span 0, and it is the purest statement the axis has: a plumb line is
# gravity and nothing else.
#
# *** WHY IT EXISTS AT ALL. *** Measured over the batch, 42 of 985 components — always ONE BOOT OF
# A PAIR, a 12-to-17px L-shaped blob four pixels across — can hang no swag at any offset under any
# of the three rhythms, because a swag needs its belly to land on the piece and these shapes have
# no two-row-deep column under any run they own. Leaving them as a flat recolor is exactly the
# 54th's measured failure (one leg wired, the other blank) and it is worse here, because the two
# boots of a pair sit side by side in every frame. A pendant costs four pixels and states the axis.
PENDANT_LEN = 3


def _pendants(comp):
    """Hang one plumb line on a component too small for any swag: the stud goes at the top of the
    longest unbroken vertical run the piece has, nearest its centre, and the chain drops from it."""
    h, w = comp.shape
    best = None
    for x in range(w):
        y = 0
        while y < h:
            if not comp[y, x]:
                y += 1
                continue
            y1 = y
            while y1 + 1 < h and comp[y1 + 1, x]:
                y1 += 1
            n = y1 - y + 1
            if n >= 3:
                key = (-n, abs(x - (w - 1) / 2.0), y, x)
                if best is None or key < best[0]:
                    best = (key, y, x, min(n - 1, PENDANT_LEN))
            y = y1 + 1
    if best is None:
        return []
    _, y0, x, ln = best
    return [dict(y0=y0, a=x, b=x, span=0, sag=ln, kind='pendant',
                 curve={y0 + i: x for i in range(ln + 1)})]


def _paint_pendants(comp, role, pends):
    h, w = comp.shape
    for pd in pends:
        x, y0, ln = pd['a'], pd['y0'], pd['sag']
        for i in range(1, ln + 1):
            role[y0 + i, x] = R_LINK
            if x - 1 >= 0 and comp[y0 + i, x - 1] and role[y0 + i, x - 1] == R_FIELD:
                role[y0 + i, x - 1] = R_LIP
            if x + 1 < w and comp[y0 + i, x + 1] and role[y0 + i, x + 1] == R_FIELD:
                role[y0 + i, x + 1] = R_SHADE
        role[y0, x] = R_BOSS
    return role


def _paint_roles(comp, swags):
    """Turn a set of hung chains into a role field. Shadows first, then the lit edge, then the
    chain, then the studs, so a later chain always wins over an earlier one's relief."""
    h, w = comp.shape
    role = np.where(comp, R_FIELD, -1).astype(np.int8)
    for sw in swags:
        xm = (sw['a'] + sw['b']) / 2.0
        for x, yc in sw['curve'].items():
            u = 2.0 * (x - xm) / sw['span']
            y1 = yc + 1
            if 0 <= y1 < h and comp[y1, x] and role[y1, x] == R_FIELD:
                role[y1, x] = R_SHADE
            if abs(u) <= BELLY:
                y2 = yc + 2
                if 0 <= y2 < h and comp[y2, x] and role[y2, x] == R_FIELD:
                    role[y2, x] = R_CAST
    for sw in swags:
        for x, yc in sw['curve'].items():
            yl = yc - 1
            if 0 <= yl < h and comp[yl, x] and role[yl, x] in (R_FIELD, R_SHADE, R_CAST):
                role[yl, x] = R_LIP
    for sw in swags:
        for x, yc in sw['curve'].items():
            role[yc, x] = R_LINK
    for sw in swags:
        role[sw['y0'], sw['a']] = R_BOSS
        role[sw['y0'], sw['b']] = R_BOSS
    return role


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — an EQUILIBRIUM read off the painted pixels.
#
# Every previous axis is accepted on a STATISTIC of its field (46th cell count, 48th size ratio,
# 50th glyph survival, 52nd distinct-hole appearances, 53rd radius histogram), on its TOPOLOGY
# (54th), on the ALGEBRA of a relation (55th) or on a CONSERVATION LAW along a traversal (56th).
# All of those are facts about the ornament ALONE. This axis's content is a relation between the
# ornament and something OUTSIDE it, so it is accepted on a PHYSICAL LAW: does this thing hang?
# ---------------------------------------------------------------------------------------------
def read_curve(role, y0, a, b, reach=SAG_MAX):
    """Read one swag's curve back OFF THE PAINTED PIXELS by TRACING it: put a finger on the left
    stud and follow the chain, column by column, taking at each step the nearest chain pixel to the
    one before it.

    *** THIS WAS A REAL BUG AND IT IS WORTH THE PARAGRAPH. *** The first version scanned a fixed
    BAND of rows around the tier line and took the chain pixel furthest from it. On the synthetic
    plate that silently picked up THE TIER ABOVE's chain — a deep swag hangs SAG_MAX below its own
    studs and the tier above is only TIER_P away, so the two come within TIER_P - SAG_MAX = 3 rows
    of each other, well inside any band wide enough to contain a deep swag. The reader then saw one
    chain climb into another and reported a second belly, i.e. it failed a correct sheet. A band
    narrow enough to be safe is too narrow to contain the deepest legal swag, so there is no band
    that works: the fix is not a better constant, it is that a CHAIN IS A CONNECTED THING AND MUST
    BE READ AS ONE. Tracing is also the honest reading — it is exactly what a viewer's eye does.
    """
    h, w = role.shape
    if not (0 <= a < w and 0 <= b < w and 0 <= y0 < h):
        return {}
    if role[y0, a] not in (R_LINK, R_BOSS):
        return {}
    out = {a: y0}
    y = y0
    for x in range(a + 1, b + 1):
        lo = max(0, max(y - 2, y0 - reach))
        hi = min(h, min(y + 3, y0 + reach + 1))
        cands = [yy for yy in range(lo, hi) if role[yy, x] in (R_LINK, R_BOSS)]
        if not cands:
            break
        # Nearest to where the chain already is, ties broken toward this swag's OWN tier line.
        # *** THE TIE-BREAK IS NOT COSMETIC. *** It first read "ties downward, because a chain
        # hangs", which is true of a chain and false of a READER: on the CLIMBING half of a swag
        # the correct next pixel is one row UP, so whenever the tier below happened to have a chain
        # pixel one row DOWN in that column the trace stepped onto the wrong chain and then
        # reported that chain as taut. Measured, that alone accounted for every one of the 16
        # ranger-boot pendency failures. `reach` closes the same hole from the other side: a trace
        # may never wander further from its own studs than its own rhythm's deepest legal sag.
        y = min(cands, key=lambda yy: (abs(yy - y), abs(yy - y0)))
        out[x] = y
    return out


def swag_verdict(curve, a, b, y0):
    """Clauses 1 and 2, on one swag.

    (1) PENDENCY  — the lowest point of the chain is strictly below BOTH of its studs. This is the
        bare statement that the ornament has an up. The FLIP control breaks exactly this, and so
        does TAUT (a straight chord's lowest point IS its studs).
    (2) SINGLE BELLY — walking the chain from stud to stud, it descends and then it climbs, and it
        never does those in the other order. One minimum, no inflection. A chain with two bellies
        is hanging off something in the middle that is not drawn; a chain that climbs and then
        descends has a bulge in it that nothing is holding up.
    """
    if a not in curve or b not in curve:
        return False, 'chain does not reach both of its studs'
    xs = sorted(curve)
    if len(xs) != (b - a + 1):
        return False, 'chain is broken between its studs'
    ys = [curve[x] for x in xs]
    low = max(ys)
    if not (low > curve[a] and low > curve[b]):
        return False, 'chain does not hang below its studs (it is taut, or it arches)'
    # descend (y increasing) then climb (y decreasing), never the reverse
    climbing = False
    for i in range(len(ys) - 1):
        d = ys[i + 1] - ys[i]
        if d < 0:
            climbing = True
        elif d > 0 and climbing:
            return False, 'chain climbs and then falls again — two bellies, nothing holding it'
    return True, 'hangs'


def span_law(pairs, population=False):
    """Clause 3, on a set of swags given as (span, sag) pairs read off the pixels.

    NO INVERSION   — of two chains, the one hung wider never hangs shallower. This is the law
                     itself, it holds on every component, and it is what makes the field a set of
                     HANGING chains rather than a set of arcs whose size happens to vary.

    The other two clauses are POPULATION clauses and are asked only of a whole sheet or a whole
    batch, never of one component, and that distinction is itself a tuning lesson: a 13px boot
    carries ONE chain, so "the chains on this piece differ" is not a question a boot can be asked.
    NOT CONGRUENT  — at least two distinct sags occur across the population, so the law is doing
                     visible work on real armour rather than being vacuously true on a field of
                     identical arcs. This is the clause the UNIFORM control fails.
    *** WHAT IS DELIBERATELY *NOT* A CLAUSE, AND WHY — A RENDER-PAID LESSON ABOUT WHAT A 13px
    RASTER CAN AND CANNOT BE ASKED. *** The design intended a third clause, NOT SIMILAR: sag/span
    should itself rise with span, since the square law makes long chains relatively droopier and a
    similar family (sag = k*span) would hold that ratio flat. Measured, that clause is not
    expressible here and asking for it FAILS CORRECT SHEETS. Sag is an integer between 1 and 4, so
    the ratio is quantised into a handful of values: spans 4 and 5 both round to sag 1, giving
    ratios 0.25 and 0.20 — a ratio inversion produced entirely by rounding. Stating it at the
    extremes instead of pairwise survives rounding but then fails to SEPARATE, because over the
    span range a 13px body actually affords (4 to 9, with the clamp binding above that) the square
    law and a linear one round to almost the same integers: the LINEAR control passes it. So the
    ratio is reported as a MEASUREMENT and not asserted as a law — the same treatment the 56th gave
    its LOCK control — and the honest statement of what this raster confirms is that the sags on a
    piece are ORDERED by span and are not all the same. The square is still the right law to
    generate with, for the reason given at SAG_DEN: it is what puts the interesting part of the
    curve inside the span range the armour offers. It is simply not what the pixels can prove.
    """
    # *** THE LAW IS STATED WITHIN ONE RHYTHM, AND THIS TOO WAS PAID FOR ON A MEASUREMENT. ***
    # Run naively over the whole batch, the no-inversion clause reported 44,969 inversions on a set
    # of sheets in which every single component was individually correct. The cause is not the
    # ornament, it is the question: a 3px boot runs the TINY rhythm, whose SAG_DEN is 6 because a
    # denominator of 20 cannot bend a 2px chain at all, so a TINY span-3 chain sags 2 while a
    # STANDARD span-4 chain sags 1. That is not a wider chain hanging shallower — it is a different
    # GAUGE of chain, the way a watch chain and an anchor chain are both obeying the same physics
    # while neither tells you anything about the other's sag. Chains are comparable when they are
    # the same chain, so the population is partitioned by rhythm before the law is applied.
    groups = {}
    for p in pairs:
        groups.setdefault(p[2] if len(p) > 2 else 'std', []).append(p)
    inv = 0
    for g in groups.values():
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][0] < g[j][0] and g[i][1] > g[j][1]:
                    inv += 1
    spans = sorted({p[0] for p in pairs})
    sags = sorted({p[1] for p in pairs})
    info = dict(inversions=inv, rhythms=len(groups),
                distinct_spans=len(spans), distinct_sags=len(sags))
    ok = inv == 0
    if population:
        # the ratio is only comparable within ONE rhythm and away from the SAG_MAX clamp: the THIN
        # and TINY rhythms run their own SAG_DEN (a 3px boot cannot express a denominator of 20),
        # and a clamped sag is by definition not on the curve.
        free = [p for p in pairs if len(p) > 2 and p[2] == 'std' and p[1] < SAG_MAX]
        if free:
            fs = sorted({p[0] for p in free})
            rmin = max(g for s, g, _ in free if s == fs[0]) / float(fs[0])
            rmax = max(g for s, g, _ in free if s == fs[-1]) / float(fs[-1])
            info['ratio_narrowest'] = round(rmin, 3)
            info['ratio_widest'] = round(rmax, 3)
            info['superlinear'] = rmax > rmin          # measured, NOT asserted — see above
        info['congruent'] = len(sags) < 2
        ok = ok and len(sags) >= 2
    return ok, info


def _params(comp, mode):
    if mode == 'thin':
        d = dict(THIN)
        d['inset'] = 1
        return d
    if mode == 'tiny':
        return dict(TINY)
    return dict(tier_p=TIER_P, sag_max=SAG_MAX, sag_den=SAG_DEN,
                span_target=SPAN_TARGET, min_span=MIN_SPAN, inset=1)


def _linear_hang(comp):
    """CONTROL: a SIMILAR family. Sag proportional to the span rather than to its square, so every
    chain on the piece is a scaled copy of every other one, the ratio sag/span is flat, and the
    population clause NOT SIMILAR fails while pendency and the single belly both still hold. This
    is the control that isolates the SQUARE in the span law from the law itself."""
    return hang(comp, linear=True)


def hang(comp, flip=False, taut=False, uniform=0, linear=False, **override):
    """Hang the chains on a component: walk the OFFSETS ladder and keep the offset that hangs the
    most chains, ties broken by total sag and then toward the lowest offset. Falls back through the
    THIN and TINY rhythms for components too narrow for the standard one — a single chausse leg is
    four pixels across and still has to carry the axis.

    Returns (role, swags, mode).
    """
    key = (comp.shape, comp.tobytes(), flip, taut, uniform, linear,
           tuple(sorted(override.items())))
    hit = _ROLE_CACHE.get(key)
    if hit is not None:
        return hit
    modes = ['std', 'thin', 'tiny'] if _has_interior(comp) else ['thin', 'tiny']
    best = None
    for mode in modes:
        p = _params(comp, mode)
        p.update(override)
        for off in range(p['tier_p']):
            sw = _layout_once(comp, off, p['tier_p'], p['sag_max'], p['sag_den'],
                              p['span_target'], p['min_span'], p['inset'],
                              flip=flip, taut=taut, uniform=uniform, linear=linear)
            # *** SCORED ON TOTAL SAG FIRST, NOT ON CHAIN COUNT, AND THAT ORDER IS A RENDER-PAID
            # LESSON. *** Scoring on count picks the offset whose tier rows land where the body is
            # NARROWEST, because a narrow run splits into the same one chain while a wide run may
            # lose its chain entirely to the completeness rule — so the ladder systematically chose
            # the shallowest possible reading of the piece and every chain on every real slot came
            # out at sag 1. Total sag asks the opposite question: where on this body can a chain
            # actually be seen to HANG? Count survives as the tie-break, so a piece that can carry
            # two equally deep chains still gets two.
            score = (sum(s['sag'] for s in sw), len(sw))
            if best is None or score > best[0]:
                best = (score, mode, sw, p)
        if best is not None and best[0][0] > 0:
            break
    score, mode, swags, p = best
    role = _paint_roles(comp, swags)
    if not swags and not (taut or flip):
        swags = _pendants(comp)
        role = _paint_pendants(comp, role, swags)
        if swags:
            mode = 'pendant'
    out = (role, swags, mode)
    _ROLE_CACHE[key] = out
    return out


def verdicts(role, swags, mode='std'):
    """Clauses 1 and 2 for every swag of a component, read off the pixels.
    Returns (ok, why, span, sag, rhythm) per chain, with span and sag both READ, never assumed."""
    reach = {'std': SAG_MAX, 'thin': THIN['sag_max'], 'tiny': TINY['sag_max']}.get(mode, SAG_MAX)
    out = []
    for sw in swags:
        if sw.get('kind') == 'pendant':
            # a plumb line: read it by walking straight down from its stud and requiring that it
            # goes DOWN and keeps going, which is clause 1 with the chord collapsed to a point
            x, y0 = sw['a'], sw['y0']
            n = 0
            while y0 + n + 1 < role.shape[0] and role[y0 + n + 1, x] == R_LINK:
                n += 1
            out.append((n >= 2, 'plumb line hangs' if n >= 2 else
                        'the pendant does not descend from its stud', 0, n, mode))
            continue
        curve = read_curve(role, sw['y0'], sw['a'], sw['b'], reach)
        ok, why = swag_verdict(curve, sw['a'], sw['b'], sw['y0'])
        read_sag = (max(curve.values()) - sw['y0']) if curve else 0
        out.append((ok, why, sw['b'] - sw['a'], abs(read_sag), mode))
    return out


def accepts(role, swags, mode='std'):
    """The acceptance test for ONE COMPONENT: clauses 1 and 2 on every chain, plus the no-inversion
    half of clause 3. The NOT CONGRUENT half is a population statement and is asked of the whole
    batch instead — a 13px boot carries one chain, so "the chains on this piece differ" is not a
    question a boot can be asked. See span_law()."""
    if not swags:
        return False, 'no chain hangs on this component at any offset'
    vs = verdicts(role, swags, mode)
    for ok, why, _, _, _ in vs:
        if not ok:
            return False, why
    # a pendant has no chord, so it has no span and the span law has nothing to say about it
    ok, info = span_law([(s, g, m) for _, _, s, g, m in vs if s > 0])
    if not ok:
        return False, ('a wider chain hangs shallower than a narrower one on this piece: %s' % info)
    return True, 'every chain hangs; no chain on the piece inverts the span law'


def paint_festoon(fr, comp_full, stops, flip=False, taut=False, uniform=0, linear=False, **kw):
    """Paint the festoon onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette."""
    if comp_full.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    role = hang(comp, flip=flip, taut=taut, uniform=uniform, linear=linear, **kw)[0]
    interior = _interior(comp)
    boundary = comp & ~interior

    for y, x in zip(ys, xs):
        ly, lx = int(y) - y0, int(x) - x0
        r = int(role[ly, lx])
        if r < 0:
            continue
        rgb = stops[DEMOTE[r]] if boundary[ly, lx] else stops[r]
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free)."""
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


def comps_of(a, largest):
    lbl, n = label4(a)
    if n < 1:
        return []
    if largest:
        counts = np.bincount(lbl.ravel())
        counts[0] = 0
        return [(lbl == int(counts.argmax()))]
    return [(lbl == i) for i in range(1, n + 1)]


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    stops = FESTOON[cls]
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
        # ONE SET OF CHAINS PER CONNECTED COMPONENT — a chain is bolted to a physical plate and
        # cannot span the gap between the two legs of a pair of chausses or between the left boot
        # and the right. Each component is its own piece of armour with its own studs. (The 54th's
        # lesson, and it bites harder here: an anchor's position is read off the component's own
        # opaque run at that row, so a bounding-box layout would hang chains across empty air.)
        for comp in comps_of(a, largest):
            paint_festoon(fr, comp, stops)
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
    festoon can be judged on a shape with the features the real slots have — in particular, rows of
    genuinely different widths, which is what the span law needs to become visible."""
    m = np.zeros((h, w), dtype=bool)
    _, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False
    return m


def swatch(path='_diag_festoon_swatch.png', zoom=12):
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_festoon(a, m, FESTOON[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def _big_comp(arr, fi=0):
    r, c = fi // COLS, fi % COLS
    src = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def sweep(path='_diag_festoon_sweep.png', zoom=11):
    """Warrior chest and leg idle frames across the tier pitch and span target, plus the three
    CONTROLS. FLIP is the one to look at: it is this generator's own output with the sag negated,
    so the geometry, the count, the studs and the palette are all identical and the only thing that
    has changed is which way the chains hang."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    variants = [('TIER 5', dict(tier_p=5)), ('TIER 7', dict(tier_p=7)), ('TIER 9', dict(tier_p=9)),
                ('SPAN 5', dict(span_target=5)), ('SPAN 13', dict(span_target=13)),
                ('LINEAR', dict(_linear=True)),
                ('FLIP', dict(_flip=True)), ('TAUT', dict(_taut=True)),
                ('UNIFORM', dict(_uniform=2))]
    cells = []
    for name, kw in variants:
        kw = dict(kw)
        ctrl = dict(flip=kw.pop('_flip', False), taut=kw.pop('_taut', False),
                    uniform=kw.pop('_uniform', 0), linear=kw.pop('_linear', False))
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            comp = _big_comp(arr)
            fr = np.zeros_like(arr[0:FH, 0:FW])
            paint_festoon(fr, comp, FESTOON['warrior'], **dict(ctrl, **kw))
            col.append(Image.fromarray(fr).crop(crop))
        cells.append((name, col))
    cw, ch = 28 * zoom, 26 * zoom
    pad, lab = 8, 18
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + 2 * (ch + lab)),
                    (24, 24, 28, 255))
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
    print('wrote %s (tier/span sweep + FLIP/TAUT/UNIFORM controls - no sheets written)' % path)


def slots_diag(path='_diag_festoon_slots.png', zoom=10):
    """All three classes x all four slots, bare motif, no finishing pass."""
    srcs = [('chest', 'armor_chest_4.png', 'shirt_mage4.png', 'shirt_ranger4.png', True),
            ('legs', 'armor_pants_4.png', 'pants_mage4.png', 'pants_ranger4.png', False),
            ('boots', 'armor_boots_4.png', 'boots_mage4.png', 'boots_ranger4.png', False),
            ('helmet', 'helmet_rare1.png', 'helmet_mage4.png', 'helmet_ranger4.png', True)]
    crop = (26, 12, 58, 60)
    cw, chh = (crop[2] - crop[0]) * zoom, (crop[3] - crop[1]) * zoom
    pad, lab = 8, 16
    img = Image.new('RGBA', (pad + 4 * (cw + pad), pad + 3 * (chh + lab)), (24, 24, 28, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)
    except Exception:
        f = ImageFont.load_default()
    for ci, (kind, wf, mf, rf, largest) in enumerate(srcs):
        for ri, (cls, fn) in enumerate((('warrior', wf), ('mage', mf), ('ranger', rf))):
            arr = load_any(fn)
            a = arr[0:FH, 0:FW][..., 3] > 0
            fr = np.zeros_like(arr[0:FH, 0:FW])
            for comp in comps_of(a, largest):
                paint_festoon(fr, comp, FESTOON[cls])
            cell = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
            x = pad + ci * (cw + pad)
            y = pad + ri * (chh + lab)
            img.alpha_composite(cell, (x, y))
            d.text((x + 2, y + chh), '%s %s' % (cls, kind), font=f, fill=(210, 210, 220, 255))
    img.convert('RGB').save(path)
    print('wrote %s (all classes x all slots, bare motif)' % path)


def dump_cells():
    legend = {R_BOSS: 'O', R_LIP: '+', R_LINK: '#', R_SHADE: ':', R_CAST: '.', R_FIELD: '-'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    allpass = True
    allpairs = []
    for label, comp in cases:
        role, swags, mode = hang(comp)
        vs = verdicts(role, swags, mode)
        allpairs.extend([(s, g, m) for _, _, s, g, m in vs])
        print('== %s   area=%d chains=%d rhythm=%s'
              % (label, int(comp.sum()), len(swags), mode))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        ok, why = accepts(role, swags, mode)
        allpass = allpass and ok
        print('   (span -> sag, read off the pixels): %s'
              % ', '.join('%d->%d' % (s, g) for _, _, s, g, _ in vs))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL'))

    ok, info = span_law(allpairs, population=True)
    print('== THE SPAN LAW over the population of all the cases above: %s   -> %s'
          % (info, 'PASS' if ok else 'FAIL'))
    allpass = allpass and ok

    # the four CONTROLS, over the same population, so the failures are measured and not asserted
    for cname, kw, why in (
            ('FLIP    (this axis\'s own output with the sag negated - the first control in the '
             'series that IS the axis, transformed)', dict(flip=True),
             'the chains arch off their studs with nothing holding them up'),
            ('TAUT    (every chain pulled tight - 8th side-stripe / 10th cross)', dict(taut=True),
             'a straight chord between two studs is a strap, and straps this set already has'),
            ('UNIFORM (every chain given the same sag - 34th seigaiha)', dict(uniform=2),
             'congruent arcs on a body: the sag stops being a consequence of anything'),
            ('LINEAR  (sag proportional to span, not to its square - a SIMILAR family). MEASURED, '
             'NOT ASSERTED: this is the one control the axis CANNOT separate at 13px, and the '
             'number below is the evidence for that. Compare its ratio spread with the real one '
             'above - integer sag over the span range a body affords rounds the two laws onto '
             'nearly the same values. Reported for the same reason the 56th reports LOCK.',
             dict(sag_den=None, linear=True),
             'a similar family still hangs and still orders its sags; what it loses is only that '
             'the long chains are RELATIVELY droopier, and that is below the raster\'s resolution')):
        kw = dict(kw)
        linear = kw.pop('linear', False)
        if kw.get('sag_den') is None:
            kw.pop('sag_den', None)
        cpairs = []
        nfail = nch = 0
        for _, comp in cases:
            if linear:
                role, swags, cmode = _linear_hang(comp)
            else:
                role, swags, cmode = hang(comp, **kw)
            vs = verdicts(role, swags, cmode)
            nch += len(vs)
            nfail += sum(1 for v in vs if not v[0])
            cpairs.extend([(s, g, m) for _, _, s, g, m in vs])
        lok, linfo = span_law(cpairs, population=True)
        print('== CONTROL: %s' % cname)
        print('   chains=%d  failing pendency/belly=%d  span law=%s %s  -> %s'
              % (nch, nfail, 'PASS' if lok else 'FAIL', linfo,
                 'PASS' if (nfail == 0 and lok) else 'FAIL'))
        print('   %s' % why)

    print('legend: # chain  + its lit upper edge  O the stud it hangs from  : the core shadow  '
          '. the shadow widened at the belly  - field')
    print('ACCEPTANCE (a PHYSICAL LAW, not a statistic, a topology, an algebra or a conservation):')
    print('(1) PENDENCY     every chain hangs strictly below both of its own studs;')
    print('(2) SINGLE BELLY it descends then climbs, one minimum, no inflection;')
    print('(3) THE SPAN LAW no chain on a piece hangs shallower than a narrower one, and across')
    print('    the batch at least two distinct sags occur, so the sags are ORDERED BY SPAN and are')
    print('    not all the same. Every quantity above is read off the painted pixels by TRACING')
    print('    each chain from its stud, never taken from the formula it was drawn with.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def accept_all():
    """The acceptance test run over EVERY component of EVERY active frame of all 24 sheets — the
    same reading the --cells dump prints, but on the real bodies in every pose, because a constant
    tuned on the idle frame is not a constant that survives every pose (the 52nd through 56th all
    paid for that lesson)."""
    ncomp = nchain = nfail = nbare = npend = 0
    sagsum = 0
    pairs = []
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                for fi in range(60):
                    r, c = fi // COLS, fi % COLS
                    src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
                    a = src[..., 3] > 0
                    if not a.any():
                        continue
                    for comp_full in comps_of(a, largest):
                        if comp_full.sum() < MIN_PX:
                            continue
                        ys, xs = np.nonzero(comp_full)
                        comp = comp_full[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
                        role, swags, mode = hang(comp)
                        ncomp += 1
                        if not swags:
                            nbare += 1
                            nfail += 1
                            print('   VIOLATION %s %s%s frame %d: no chain hangs at any offset'
                                  % (kind, cls, suffix, fi))
                            continue
                        vs = verdicts(role, swags, mode)
                        nchain += len(vs)
                        sagsum += sum(v[3] for v in vs)
                        pairs.extend([(v[2], v[3], v[4]) for v in vs if v[2] > 0])
                        npend += sum(1 for v in vs if v[2] == 0)
                        cok, cwhy = accepts(role, swags, mode)
                        if not cok:
                            nfail += 1
                            print('   VIOLATION %s %s%s frame %d: %s'
                                  % (kind, cls, suffix, fi, cwhy))
    ok, info = span_law(pairs, population=True)
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components               %d' % ncomp)
    print('  chains hung              %d  (of which %d are plumb-line pendants on components too'
          ' small for a swag)' % (nchain, npend))
    print('  mean sag (read)          %.2f px' % (sagsum / max(1, nchain)))
    print('  components with nothing  %d' % nbare)
    print('  pendency/belly failures  %d' % nfail)
    print('  THE SPAN LAW             %s  %s' % ('PASS' if ok else 'FAIL', info))
    print('OVERALL: %s' % ('ALL PASS' if (nfail == 0 and ok) else 'FAIL'))
    return nfail == 0 and ok


def main():
    if '--accept' in sys.argv:
        accept_all()
        return
    if '--cells' in sys.argv:
        dump_cells()
        return
    if '--swatch' in sys.argv:
        swatch()
        return
    if '--sweep' in sys.argv:
        sweep()
        slots_diag()
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
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
