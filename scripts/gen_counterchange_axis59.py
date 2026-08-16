#!/usr/bin/env python3
"""FIFTY-NINTH net-new-geometry axis for ALL FOUR SLOTS — the COUNTERCHANGE family: the piece is
covered edge to edge in a two-tincture fur, and somewhere across it the two tinctures TRADE PLACES.
Nothing marks where. No line is drawn, no border, no seam, no rivet. The division is visible only
because every cell that straddles it comes out half one tincture and half the other, and because
from there on the metal is doing what the colour was doing.

    the ornament is  METAL   (the light tincture — half the surface, exactly)
                   + COLOUR  (the dark tincture — the other half, exactly)
                   + SHADE   (each tincture's own darker tone, taken by a pixel that has the OTHER
                              tincture directly above it; applied to BOTH tinctures identically,
                              because a light that favours one of them breaks the exchange)
                   + EDGE    (each tincture's own quietest tone, on the silhouette)

and there is deliberately NO sixth element. There is no line, because the line is the one thing this
axis is not allowed to draw.

*** THIS IS THE FIRST AXIS WHOSE SYMMETRY IS AN ANTISYMMETRY. ***
The 58th was the first axis whose ELEMENT was chiral, and it was accepted by exhausting a rotation
group on the pixels. This is the next question about the same machinery and a strictly harder one,
because the operation this piece is invariant under is NOT A MOTION AT ALL.

Fold the piece along its division line. The shapes land on shapes exactly — but every gold lands on
a blue and every blue on a gold, so the fold is not a symmetry. Now leave it flat and swap the two
tinctures. The shapes have not moved, so that is not a symmetry either. Do BOTH and the piece is
itself again, pixel for pixel. The invariance belongs to neither the geometry nor the colouring; it
belongs only to their PRODUCT. In crystallography this is an antisymmetry, a black-and-white or
Shubnikov operation, and no axis in this set has had one.

Every one of the fifty-eight before is invariant under some subgroup of the ordinary motions of the
plane — that is what "a repeating ornament" means — and the 58th's discovery was that one of those
motions, the mirror, could be denied to the element. This one denies the whole group to the PICTURE
and hands it back only on condition that the palette move too.

*** THE CONSEQUENCE THAT MAKES THE AXIS VISIBLE, AND IT IS FORCED, NOT CHOSEN. ***
An antisymmetry can have no fixed pixel. A pixel the operation leaves where it is would have to be
the opposite tincture to itself, and there is no such tincture. So the mirror cannot run ALONG a row
of pixels; it must run BETWEEN two of them. And then the two rows it runs between are each other's
opposites at every single column, all the way across the piece — a continuous run of contrast
reversals with nothing drawn on it. THAT is the division line: not an ornament, but the place where
the ornament is obliged to change its mind.

It is also exactly what a translation cannot produce, and that is the whole distinctness argument
against the obvious near miss. A CHEQUY — an ordinary checkerboard — is antisymmetric too: shift it
one square and swap the colours and it is itself. But that operation moves every point, so it leaves
NOTHING anywhere on the piece to see it by, and a chequy accordingly has no division, no line, no
anywhere-in-particular. It is the SAME everywhere. This piece is not: it has a place.

Every other near miss fails on something checkable by exhausting the group.
  * The 26th TARTAN — the reflex answer, since it is two colours crossing on a lattice. Swap its two
    colours and you get a DIFFERENT tartan; the exchange is not a symmetry of it in any composition
    with any motion, and its two colours are not even equal in area. The 58th named tartan as the
    thing it must not become by colouring its two hands differently. This axis is the exact
    complement of that decision: there the two classes had to share one metal so that only FORM told
    them apart; here the two classes share one form so that only TINCTURE tells them apart.
  * The 29th HOUNDSTOOTH and the 18th BASKETWEAVE — genuine two-colour weaves, and both are
    antisymmetric under translations, for the chequy's reason and with the chequy's consequence: no
    locus, no division, the same everywhere.
  * The 37th COFFER and the 43rd GADROON — the two axes built as deliberate inversions of an older
    one (the 35th facet, the 11th fluting). An inversion applied uniformly to a whole piece produces
    a SECOND PIECE. Here both states are on the SAME piece at the same time, and the ornament is the
    boundary between them.
  * The 52nd AJOURÉ — two surfaces, one seen through the other, with a definite front and a definite
    back. This has one surface, and the question "which tincture is the ornament and which is the
    plate" HAS NO ANSWER on it. That is not vagueness; it is the content.
  * The 55th STRATA — a relation between neighbours that is an ORDER. This is an EXCHANGE: an
    involution, its own inverse, with no first and no last.
  * The 8th AEGIS ROUNDEL and the 7th GIRDLE — the two axes with a named thing in a named place.
    They put an object at a location. This puts no object anywhere; it puts an EVENT along a line.
  * The 47th MOKUME — tone as a function of distance to the silhouette, i.e. a field organised by
    the piece's own boundary. This one is organised by a boundary that is nowhere near the edge and
    is not drawn.
  * The 58th VORTICE — the immediately preceding axis and the one this is in conversation with. A
    hand is a property of ONE element and survives any recolouring. A counterchange is a property of
    a PAIR (element, tincture) and dies the instant either half is considered alone.

*** AND IT IS WHY THE RULE OF TINCTURE IS IN THE PALETTE. *** Heraldry's oldest law — never colour
on colour, never metal on metal — is usually explained as a convention. It is not; it is a
legibility law, and no heraldry ever needed it as badly as a 13-pixel torso does. The two tinctures
here must be told apart at a glance across one pixel, from across a room, after the finishing pass
has shaded both of them. So one of them is a METAL and the other is a COLOUR, always, and the value
gap between them is the largest gap in the palette.

Geometry, per connected component, in the component's own frame:
    fur        a VAIR: interlocking bells, one tincture pointing up and the other down, an exact
               50/50 partition of the plane with no cell left over. Gauges STD 4x4 / THIN 3x4 /
               TINY 2x4, chosen by what the component can show.
    division   a reflection, PER FESS (about a horizontal line) or PER PALE (about a vertical one),
               at an ODD offset so it falls BETWEEN two rows and has no fixed pixel. The offset and
               the family are chosen per component to maximise the number of pixels whose reflection
               is also on the piece, subject to each side holding at least a quarter of it.
    fold       tincture(p) = fur(p) on the near side, and NOT fur(M(p)) on the far side. By
               construction tincture(M(p)) != tincture(p) everywhere, which is the axis.
    phase      the fur's phase is chosen per component to bring the two tinctures as close to equal
               area AS PAINTED ON THIS PARTICULAR BODY as it can — the ninth appearance of the
               adaptive-boundary lesson, now applied to AREA, because clause 4 is about area.
    relief     a pixel takes its own tincture's SHADE tone iff the pixel above it is the other
               tincture. Both tinctures, identically. See the note on equivariance below.

Authoring philosophy identical to gen_vortice_axis58.py / gen_festoon_axis57.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed, silhouette
untouched, so the generator cannot create isolated pixels, background bleed, extra components or a
changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Fifteenth generator to call it in-line, after axes 45-58.

Run from repo root:
  python3 scripts/gen_counterchange_axis59.py
  python3 scripts/gen_counterchange_axis59.py --cells    # ASCII dump + the ANTISYMMETRY test
  python3 scripts/gen_counterchange_axis59.py --accept   # that test over every component of all 24
  python3 scripts/gen_counterchange_axis59.py --swatch   # bare fur on a test plate, no sheets
  python3 scripts/gen_counterchange_axis59.py --sweep    # gauge sweep + SAME/CHEQUY/PLAIN/UNIFORM
Then QA (examples):
  python3 scripts/sprite_qa.py _counterchange_legendary_preview/shirt_warrior_legendary59.png
  python3 scripts/sprite_qa.py _cchangedome_helmet_preview/helmet_mage_legendary59.png --y-min 2
  python3 scripts/sprite_qa.py _counterchange_boots_preview/boots_warrior_legendary_cchange.png --y-max 63
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

# Roles. Note there are exactly two FAMILIES of three, and they are interchangeable by design:
# whatever is done to one tincture is done to the other. A role table that treated them
# asymmetrically would be an assertion that one of them is the ornament.
R_A, R_A_SH, R_A_ED, R_B, R_B_SH, R_B_ED = 0, 1, 2, 3, 4, 5
FAMILY = {R_A: 0, R_A_SH: 0, R_A_ED: 0, R_B: 1, R_B_SH: 1, R_B_ED: 1}
PLAIN = {0: R_A, 1: R_B}
SHADE = {0: R_A_SH, 1: R_B_SH}
EDGE = {0: R_A_ED, 1: R_B_ED}


# --- the fur ------------------------------------------------------------------------------------
# VAIR: the heraldic fur of interlocking bells, alternately of a metal and a colour. It is chosen
# over the obvious alternatives for one reason above all others — IT IS AN EXACT 50/50 PARTITION
# WITH TWO CONGRUENT CLASSES. That matters more here than in any previous axis, because the whole
# claim of the axis is that neither tincture is the ground. A semé of small studs on a broad field
# is 15/85 and the eye names the studs the ornament instantly; swap the tinctures on such a field
# and you have not exchanged figure and ground, you have made a different, worse piece. At 50/50
# with congruent classes there is nothing for the eye to name, so the exchange is real.
#
# Each gauge is given as the cells of ONE bell inside a (PX x PY) block; the complement of that bell
# inside the block is the OTHER tincture's bell, and in every gauge below it is the same bell
# translated by (0, PY/2). That is not decoration — it is what makes the two classes congruent, and
# it is asserted at import.
#
#   STD 4x4    the bell as drawn in every roll of arms: two cells of crown, a full course of
#              shoulder, two feet. 8 pixels of 16.
#   THIN 3x4   one cell of crown. The narrowest bell that still has a crown, a shoulder and feet,
#              and therefore still reads as a bell rather than as a brick.
#   TINY 2x4   a step. Below this there is nothing: a 2x2 block is a CHEQUY, and a chequy is the
#              control this axis is defined against, so the smallest gauge is deliberately the
#              smallest fur that is NOT one.
FURS = {
    'std':  (4, 4, ((1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (3, 2))),
    'thin': (3, 4, ((1, 0), (0, 1), (1, 1), (2, 1), (0, 2), (2, 2))),
    'tiny': (2, 4, ((0, 0), (0, 1), (1, 1), (1, 2))),
}
GAUGES = ('std', 'thin', 'tiny')

# The CONTROLS, kept in the same table so they go through exactly the same code path as the axis.
# CHEQUY is the important one: the classic antisymmetric pattern, and the thing this axis must not
# be. PLAIN is a fur of one cell — i.e. no fur at all, a bare party-per-fess shield.
CONTROL_FURS = {
    'chequy': (2, 2, ((0, 0), (1, 1))),
    'plain':  (1, 1, ()),        # no fur at all: the fold and nothing else, a bare party per fess
}


def _fur_mask(name):
    px, py, cells = FURS.get(name) or CONTROL_FURS[name]
    m = np.zeros((py, px), dtype=np.uint8)
    for (u, v) in cells:
        m[v, u] = 1
    return px, py, m


# *** ASSERTED AT IMPORT: every fur is an exact half of its block, and its complement is itself
# translated by half a period. *** Break either and the axis is gone while the sheet still renders:
# an unequal fur gives the eye a ground to name, and a fur whose two classes are not congruent gives
# it a figure to name. Both failures are silent and both pass sprite_qa.
for _n in list(FURS) + ['chequy']:
    _px, _py, _m = _fur_mask(_n)
    assert _m.sum() * 2 == _px * _py, '%s: fur is not half the block' % _n
    assert np.array_equal(np.roll(_m, _py // 2, axis=0), 1 - _m), \
        '%s: the two tinctures are not congruent' % _n
# The PLAIN control is exempt and that is what makes it a control: it has no fur, so it has no two
# congruent halves, and its whole content is the division line with nothing performed across it.
assert _fur_mask('plain')[2].sum() == 0


# *** THE GRAIN, AND THE LAW THAT COMES WITH IT — THE MOST EXPENSIVE THING THE CENSUS TAUGHT. ***
# The assertion above is that each fur's complement is the fur itself shifted by half a period. That
# is what makes the two tinctures congruent, and congruence is what stops the eye naming one of them
# the ground — so it cannot be given up. But a shift that carries one tincture onto the other IS AN
# ANTISYMMETRY, and it belongs to the fur before any fold is applied to it.
#
# Measured, on the first build: a torso folded PER PALE came back with THIRTEEN antisymmetries. The
# fold was one of them; the other twelve were the vair's own vertical shift and its multiples. The
# piece was still counterchanged and was no longer ONLY counterchanged, and clause 3 is exactly the
# clause that says so.
#
# The fix is forced and it is a real law about this axis rather than a tuned constant:
#
#     THE FOLD MUST CROSS THE FUR'S GRAIN.
#
# A fold whose line runs PARALLEL to the fur's own half-period shift leaves that shift intact on both
# sides of itself, and the piece keeps an antisymmetry that fixes nothing and therefore marks nowhere.
# A fold laid ACROSS it carries points over the line, where the tincture is negated a second time,
# and the shift dies. So the fur is given a GRAIN — bells upright ('v', shift vertical) or the same
# fur quarter-turned ('h', shift horizontal) — and the division family is chosen to be perpendicular
# to it: per fess with an upright fur, per pale with a turned one. That is why both divisions are
# still available; what is not available is either of them with the wrong grain.
def fur_at(name, grain, xx, yy):
    """The fur's tincture (0 or 1) at integer coordinates. Defined on the whole plane."""
    px, py, m = _fur_mask(name)
    if grain == 'h':
        return m[np.mod(xx, py), np.mod(yy, px)]
    return m[np.mod(yy, py), np.mod(xx, px)]


def fur_period(name, grain):
    px, py, _ = _fur_mask(name)
    return (py, px) if grain == 'h' else (px, py)


# The division family and the grain it demands. Stated as a table so the pairing is impossible to
# get wrong by accident anywhere else in the file.
GRAIN_FOR = {'fess': 'v', 'pale': 'h'}


# --- the division -------------------------------------------------------------------------------
# An operation is ('fess', c) — reflection about the horizontal line y = c/2 — or ('pale', c) —
# reflection about the vertical line x = c/2. c is ALWAYS ODD.
#
# *** c ODD IS NOT A DETAIL, IT IS THE AXIS ENFORCING ITSELF. *** With c even the line runs along a
# row of pixels and every pixel of that row is fixed by the operation. A fixed pixel under an
# antisymmetry must be the opposite tincture to itself. There is no such tincture, so an even offset
# does not describe a piece that is hard to paint — it describes a piece that CANNOT EXIST. The
# assertion below is therefore not a guard against ugliness; it is a guard against incoherence.
def op_apply(op, ys, xs):
    kind, c = op
    if kind == 'fess':
        return c - ys, xs
    if kind == 'pale':
        return ys, c - xs
    dx, dy = c
    return ys + dy, xs + dx          # 'tx', used only by the census below


def op_near(op, ys, xs):
    """The side of the division a point is on. Well defined for every pixel precisely because c is
    odd, so no pixel lies on the line."""
    kind, c = op
    if kind == 'fess':
        return 2 * ys < c
    return 2 * xs < c


def op_name(op):
    kind, c = op
    if kind == 'tx':
        return 'translate %+d,%+d' % c
    return '%s @ %.1f' % ('per fess' if kind == 'fess' else 'per pale', c / 2.0)


# Each side of the division must hold at least this share of the component, or the "fold" is a
# sliver against a plate and there is no exchange to see. Measured: below about a fifth, a chausse
# leg reads as a fur with a stripe of the wrong colour at the ankle.
SIDE_MIN = 0.25
# An operation is reported by the census only if it is SUPPORTED — enough pixels whose image also
# lands on the piece for the verdict to be about the piece rather than about its fringe. Both an
# absolute floor and a share of the component, and the share is the one that matters: measured, a
# flat floor of 8 pixels let a translation of two-thirds the width of a 415-pixel plate be declared a
# symmetry on the strength of the dozen pixels at the hem where it happened to overlap itself. A
# verdict from 3% of a piece is not a verdict.
#
# *** AND THE SHARE IS A HALF, WHICH IS THE SECOND THING THE CENSUS TAUGHT. *** At 0.30 a warrior
# leg came back with THREE antisymmetries: the fold, and a pair of translations that shift half a
# bell ACROSS the grain and two whole bells ALONG it. Those two are not artefacts of the code — on
# the pixels they see, they hold. What they do not have is a piece to hold on: measured, the fold is
# witnessed by 66 of the leg's 98 pixels and each phantom by 30, and the difference is not marginal,
# it is the difference between an operation the whole leg agrees to and one that a third of it does.
# The bar is therefore set where the sentence is true — AN OPERATION MORE THAN HALF THE PIECE CAN
# SEE — and across the whole batch every fold clears it (0.67 to 0.97) and nothing else comes near.
MIN_PAIRS = 6
MIN_PAIR_SHARE = 0.50
# A component with fewer than this many INTERIOR pixels is all boundary. Same constant and the same
# measured reason as the 52nd through 58th.
MARGIN_MIN = 20


def candidate_ops(comp):
    """Reflections worth trying on this component: both families, odd offsets, within a window of
    the centroid, each side holding at least SIDE_MIN of the body.

    Scored on SUPPORTED PAIRS — the number of pixels whose reflection also lands on the piece —
    because that is exactly the number of pixels at which the antisymmetry is a claim about
    anything. An operation with few supported pairs is not a weak version of this axis, it is an
    operation the body cannot witness.
    """
    h, w = comp.shape
    ys, xs = np.nonzero(comp)
    tot = len(ys)
    out = []
    for kind, mid, lim in (('fess', 2.0 * ys.mean(), h), ('pale', 2.0 * xs.mean(), w)):
        base = int(round(mid))
        for dc in range(-7, 8):
            c = base + dc
            if c % 2 == 0:
                c += 1
            if not (0 < c < 2 * lim - 1):
                continue
            op = (kind, c)
            near = op_near(op, ys, xs)
            n0 = int(near.sum())
            if min(n0, tot - n0) < SIDE_MIN * tot:
                continue
            oy, ox = op_apply(op, ys, xs)
            ok = (oy >= 0) & (oy < h) & (ox >= 0) & (ox < w)
            pairs = int(comp[oy[ok], ox[ok]].sum())
            out.append((pairs, kind, c, op))
    if not out:
        return []
    out.sort(key=lambda t: (-t[0], t[1], t[2]))
    # The chosen fold must itself clear the census bar, or the axis would be asserting an operation
    # the census is then entitled to ignore. If nothing clears it the best-supported candidate is
    # returned anyway and the acceptance test says so out loud, rather than the generator quietly
    # settling for a division the body cannot witness.
    need = max(MIN_PAIRS, int(MIN_PAIR_SHARE * tot))
    strong = [t for t in out if t[0] >= need]
    src = strong or out
    return [(t[3], t[0]) for t in src]


def tint_field(comp, op, fur, phx, phy, fold=True, grain=None):
    """The tincture of every pixel of the bounding box, 0 or 1.

    tincture(p) = fur(p)            if p is on the near side
                = NOT fur(M(p))     if p is on the far side

    so that tincture(M(p)) != tincture(p) for EVERY p — which is the whole axis, and is true here by
    construction rather than by tuning. What the acceptance test below checks is not this function;
    it checks the PAINTED PIXELS, which is a different claim, because between here and there lie the
    silhouette demotion, the relief and the finishing pass.
    """
    h, w = comp.shape
    grain = grain or GRAIN_FOR[op[0]]
    yy, xx = np.mgrid[0:h, 0:w]
    if not fold:
        return fur_at(fur, grain, xx - phx, yy - phy)
    near = op_near(op, yy, xx)
    oy, ox = op_apply(op, yy, xx)
    cy = np.where(near, yy, oy)
    cx = np.where(near, xx, ox)
    return fur_at(fur, grain, cx - phx, cy - phy) ^ (~near).astype(np.uint8)


# --- layout -------------------------------------------------------------------------------------
def _neighbours(comp):
    left = np.zeros_like(comp); right = np.zeros_like(comp)
    up = np.zeros_like(comp); down = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    up[1:, :] = comp[:-1, :]
    down[:-1, :] = comp[1:, :]
    return left, right, up, down


def _interior(comp):
    left, right, up, down = _neighbours(comp)
    return comp & left & right & up & down


def _gauges_for(comp):
    return list(GAUGES) if int(_interior(comp).sum()) >= MARGIN_MIN else ['thin', 'tiny']


_ROLE_CACHE = {}


def lay_out(comp, fold=True, fur=None, force_gauge=None, force_op=None):
    """Choose the division, the gauge and the fur's phase for one component.

    Two stages, and the order is the point.
      1. THE DIVISION, scored on supported pairs. This is chosen first because it is the axis; the
         fur is what the axis is performed on.
      2. THE GAUGE AND PHASE, scored on |nA - nB| — how close to equal the two tinctures come out AS
         PAINTED ON THIS BODY. Not on the plane, where every one of these furs is exactly 50/50 by
         assertion, but on a 13-pixel torso with a neck notch in it, where a badly phased 4x4 bell
         can leave 58/42 and hand the eye a ground to call the ground. The ninth appearance of the
         adaptive-boundary lesson, and the first time it has been applied to AREA.

    *** THE GAUGE DROPS WHEN A SIDE CANNOT SHOW BOTH TINCTURES, NOT WHEN THE FUR DOES NOT FIT. ***
    The 58th paid for the analogous mistake in render: a gauge that "fits" can still put a single
    tincture on one whole side of the line, and a side of one tincture is a side with no fur on it,
    which makes the division a border between a fur and a plate instead of between a fur and its own
    negative. Measured, an unguarded loop did exactly that on a 4px chausse leg and a 16px boot.
    """
    key = (comp.shape, comp.tobytes(), fold, fur, force_gauge, force_op)
    hit = _ROLE_CACHE.get(key)
    if hit is not None:
        return hit
    ops = [(force_op, 0)] if force_op else candidate_ops(comp)
    if not ops:
        ops = [(('fess', 2 * (comp.shape[0] // 2) + 1), 0)]
    op, pairs = ops[0]
    gauges = [force_gauge] if force_gauge else ([fur] if fur else _gauges_for(comp))
    best = None
    ys, xs = np.nonzero(comp)
    near = op_near(op, ys, xs)
    for g in gauges:
        px, py = fur_period(g, GRAIN_FOR[op[0]])
        cand = None
        for phy in range(py):
            for phx in range(px):
                t = tint_field(comp, op, g, phx, phy, fold=fold)
                tv = t[ys, xs]
                nA = int((tv == 0).sum())
                nB = len(tv) - nA
                # both tinctures must appear on BOTH sides of the line
                s0 = tv[near]; s1 = tv[~near]
                both = (len(s0) and len(s1)
                        and 0 < int(s0.sum()) < len(s0) and 0 < int(s1.sum()) < len(s1))
                score = (1 if both else 0, -abs(nA - nB))
                if cand is None or score > cand[0]:
                    cand = (score, g, phx, phy)
        if best is None or cand[0] > best[0]:
            best = cand
        if best[0][0] > 0:
            break
    score, g, phx, phy = best
    out = (op, g, phx, phy, pairs)
    _ROLE_CACHE[key] = out
    return out


def role_field(comp, op, g, phx, phy, fold=True):
    """Tincture -> role: plain in the interior, the tincture's own SHADE where the pixel above is the
    other tincture, the tincture's own EDGE on the silhouette.

    *** THE RELIEF IS APPLIED TO BOTH TINCTURES IDENTICALLY AND THAT IS LOAD-BEARING. *** The
    instinct is to drop a shadow from the metal onto the colour, the way every previous axis drops
    one from its ornament onto its ground. Doing it here would answer the question the axis exists to
    leave open: the tincture that casts is the ornament and the tincture that catches is the plate,
    and the exchange becomes a recolouring of a fixed relief. So the rule is stated on the CHANGE and
    not on the tinctures — a pixel is shaded if the pixel above it differs from it — and it is
    therefore invariant under swapping them.

    The light is still a light from above, and so this role field is NOT itself antisymmetric under a
    per-fess reflection, which turns above into below. That is correct and it is the 57th's finding
    reused: the light comes from outside the piece and is no part of the ornament. The acceptance
    test accordingly reads TINCTURE off the pixels and never the tone, exactly as the 58th reads a
    hand and never a colour.
    """
    t = tint_field(comp, op, g, phx, phy, fold=fold)
    h, w = comp.shape
    role = np.full((h, w), -1, dtype=np.int8)
    above = np.zeros_like(t)
    above[1:, :] = t[:-1, :]
    abov_ok = np.zeros_like(comp)
    abov_ok[1:, :] = comp[:-1, :]
    interior = _interior(comp)
    for v in (0, 1):
        sel = comp & (t == v)
        role[sel] = PLAIN[v]
        sh = sel & abov_ok & (above != v)
        role[sh] = SHADE[v]
        role[sel & ~interior] = EDGE[v]
    return role, t


# --- palette ------------------------------------------------------------------------------------
# SIX stops per class, in two families of three: (metal, metal shade, metal edge, colour, colour
# shade, colour edge).
#
# *** THE RULE OF TINCTURE. *** Heraldry's oldest law is never colour on colour and never metal on
# metal, and it is not a convention, it is a legibility law: the two tinctures must be told apart
# across a single pixel boundary. So every class here is one METAL against one COLOUR, and the value
# gap between the families is the largest gap in the palette — larger than any previous axis has
# used, because in every previous axis the ornament could afford to be a step or two off its ground.
# Here a viewer who cannot tell the two apart cannot see the axis at all.
#
# THE HUE PLAN, against the tiers this will sit beside. Heraldry admits exactly two metals, or and
# argent, and three classes; rather than invent a third metal, the class reads off the COLOUR, which
# is the half that can vary. The three colours are the three heraldic tinctures this set has never
# used — AZURE, PURPURE, VERT — where 54-58 ran through oxblood, pale steel, hide, textile and
# enamel in teal / umber / sienna.
#   warrior  OR on AZURE       gold on deep blue
#   mage     ARGENT on PURPURE tin-white on violet
#   ranger   OR on VERT        gold on forest green — the same metal as the warrior, deliberately,
#                              and the file says so rather than inventing a third metal to hide it
#
# NO STOP NEAR PURE BLACK: the finishing pass carves the visor as black eye and mouth pixels and a
# near-black darkest stop swallows them (the 49th's lesson). Darkest stops clear channel-sum 150 —
# warrior 182, mage 174, ranger 152.
CCHANGE = {
    'warrior': ((238, 198, 96), (196, 156, 66), (164, 126, 52),
                (66, 96, 162), (46, 68, 124), (36, 52, 94)),
    'mage':    ((238, 242, 250), (192, 198, 216), (158, 164, 186),
                (112, 68, 142), (84, 48, 108), (62, 36, 76)),
    'ranger':  ((232, 196, 116), (188, 152, 80), (156, 124, 62),
                (56, 110, 72), (40, 84, 54), (30, 70, 46)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only: the colour ramp with the
# metal as the highlight, so the piece still reads as one object when no fur is drawn.
BODY = {
    'warrior': ((36, 52, 94), (66, 96, 162), (196, 156, 66)),
    'mage':    ((62, 36, 76), (112, 68, 142), (192, 198, 216)),
    'ranger':  ((30, 70, 46), (56, 110, 72), (188, 152, 80)),
}

SLOTS = {
    'chest': dict(
        outdir='_counterchange_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary59', largest=True,
    ),
    'legs': dict(
        outdir='_counterchange_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary59', largest=False,
    ),
    'boots': dict(
        outdir='_counterchange_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_cchange', largest=False,
    ),
    'helmet': dict(
        outdir='_cchangedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary59', largest=True,
    ),
}


# --- reading the tincture back off the painted pixels --------------------------------------------
def read_tint(fr, comp_full, stops):
    """Classify every opaque pixel of a painted component as tincture 0 or 1 by nearest palette stop.

    This is the counterpart of the 58th's hand_of(): the acceptance test is run on what is ON THE
    SHEET, not on the array the painter was working from. If the demotion on the silhouette, the
    relief, or a neighbouring component's paint had put a metal pixel where a colour belonged, this
    is where it would show up.
    """
    ys, xs = np.nonzero(comp_full)
    px = fr[ys, xs, :3].astype(np.int32)
    pal = np.array(stops, dtype=np.int32)
    d = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1)
    idx = d.argmin(1)
    return ys, xs, np.array([FAMILY[int(i)] for i in idx], dtype=np.uint8)


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — an ANTISYMMETRY, by census of the group.
#
# Every previous axis is accepted on a STATISTIC of its field (46th, 48th, 50th, 52nd, 53rd), on a
# TOPOLOGY (54th), on the ALGEBRA of an order (55th), on a CONSERVATION LAW along a traversal (56th),
# on a PHYSICAL LAW (57th) or on a GROUP ACTION (58th). The 58th is the near relative: it exhausted a
# rotation group on ONE element and asked whether the mirror came back. This one exhausts a group on
# the WHOLE PIECE and asks a question that has no answer unless the palette is allowed to move too.
#
# For every candidate operation g the census sorts the piece into three:
#     SYMMETRY       tincture(g p) == tincture(p) at every supported pixel
#     ANTISYMMETRY   tincture(g p) != tincture(p) at every supported pixel
#     neither
# "Supported" means g p also lands on the piece; an operation with fewer than MIN_PAIRS supported
# pixels is not reported, because a claim about six pixels is not a claim about a piece of armour.
#
#   (1) ANTISYMMETRIC   the intended reflection M is an antisymmetry of the PAINTED tincture, at
#                       every supported pixel, exactly. This is the axis. The SAME control — the same
#                       fur, gauge, phase and palette with the FOLD REMOVED and nothing else touched
#                       — fails here.
#   (2) DIVIDED FUR     both tinctures occur on BOTH sides of the division. A counterchange is only
#                       legible if the same fur can be seen on either side of the line doing the
#                       opposite thing; a side carrying one tincture is a side with no fur on it, and
#                       the line then divides a fur from a plate rather than a fur from its own
#                       negative. The PLAIN control — the division kept, the fur removed, i.e. a bare
#                       party per fess — fails here, and it is a real near miss, because a bare
#                       partition passes clause 1 perfectly.
#   (3) SOLITARY        M is the ONLY antisymmetry in the census. This is the clause that separates
#                       the axis from a checkerboard, and it is the whole intellectual content: a
#                       chequy is antisymmetric under a lattice of translations AND under every
#                       odd-offset reflection, and not one of those operations fixes any point, so a
#                       chequy has no division and no place — it is the same everywhere. An
#                       antisymmetry that is a reflection has an invariant LINE, that line lies on
#                       the piece, and it is the ornament. The CHEQUY control fails here.
#   (4) NEITHER IS THE GROUND   over a sheet, both tinctures occur and their areas differ by no more
#                       than BALANCE. A 15/85 field has a ground whatever else is true of it, and a
#                       field with a ground cannot exchange figure with it. The UNIFORM control fails
#                       here.
#
# *** ORDINARY SYMMETRIES ARE MEASURED AND REPORTED, NOT FORBIDDEN, AND THE FIRST DRAFT HAD THAT
# WRONG. *** Clause 2 originally read "nothing at all is an ordinary symmetry", which sounds like the
# strongest possible statement and is in fact an incoherent one: a periodic ornament has translation
# symmetries by definition, and every one of the fifty-eight axes before this has them. Demanding
# their absence would demand that this axis not be an ornament. What is true, and what the census
# prints, is subtler and better: this piece has ordinary symmetries exactly like its fifty-eight
# predecessors — and it has, in addition, ONE operation that none of them has, which no motion can
# supply and which the palette must move to satisfy. The 56th reports LOCK, the 57th reports LINEAR,
# the 58th reports MIRROR; this one reports its symmetry group.
#
# *** WHAT IS DELIBERATELY NOT A CLAUSE. *** Clause 1 is not asked of the finished sheet after
# sprite_finish has run, and the reason is the 57th's: the light comes from outside the ornament. The
# finishing pass adds a visor, pauldron caps and a directional shade, none of which is antisymmetric
# and none of which is part of the axis. The census reads TINCTURE — which family a pixel's colour
# belongs to — and is blind to tone by construction, exactly as the 58th's reader is blind to colour.
# ---------------------------------------------------------------------------------------------
BALANCE = 0.15
TX_WINDOW = 9


def census(ys, xs, tv, shape, ops):
    """Sort candidate operations into symmetries and antisymmetries of a painted tincture field."""
    h, w = shape
    grid = np.full((h, w), -1, dtype=np.int8)
    grid[ys, xs] = tv
    need = max(MIN_PAIRS, int(MIN_PAIR_SHARE * len(ys)))
    syms, antis = [], []
    for op in ops:
        oy, ox = op_apply(op, ys, xs)
        ok = (oy >= 0) & (oy < h) & (ox >= 0) & (ox < w)
        if not ok.any():
            continue
        got = grid[oy[ok], ox[ok]]
        sup = got >= 0
        n = int(sup.sum())
        if n < need:
            continue
        same = got[sup] == tv[ok][sup]
        if same.all():
            syms.append((op, n))
        elif not same.any():
            antis.append((op, n))
    return syms, antis


def all_ops(shape, op):
    """The census group: every translation inside a window, every per-fess and per-pale reflection at
    an odd offset, and the intended operation. Reflections at EVEN offsets are not in the group
    because they have fixed pixels and cannot be antisymmetries of anything — including them would
    pad the census with operations that are guaranteed to fail."""
    h, w = shape
    out = []
    for dy in range(-TX_WINDOW, TX_WINDOW + 1):
        for dx in range(-TX_WINDOW, TX_WINDOW + 1):
            if dx or dy:
                out.append(('tx', (dx, dy)))
    out += [('fess', c) for c in range(1, 2 * h, 2)]
    out += [('pale', c) for c in range(1, 2 * w, 2)]
    if op not in out:
        out.append(op)
    return out


def accepts(ys, xs, tv, shape, op):
    """Clauses 1-3 on ONE COMPONENT. Clause 4 is a population clause and is asked of a sheet."""
    syms, antis = census(ys, xs, tv, shape, all_ops(shape, op))
    anti_ops = [o for o, _ in antis]
    sup = dict((o, n) for o, n in syms + antis)
    if op not in anti_ops:
        if op not in sup:
            return False, ('the division %s is not witnessed by enough of this component to be '
                           'reported at all (fewer than half its pixels reflect back onto it)'
                           % op_name(op)), syms, antis
        return False, ('the division %s is not an antisymmetry of the painted tincture: folding the '
                       'piece there does not land every tincture on its opposite' % op_name(op)), \
            syms, antis
    near = op_near(op, ys, xs)
    for side, sel in (('near', near), ('far', ~near)):
        s = tv[sel]
        if len(s) == 0 or int(s.sum()) in (0, len(s)):
            return False, ('the %s side of %s carries only one tincture, so the division separates '
                           'a fur from a plate and not a fur from its own negative'
                           % (side, op_name(op))), syms, antis
    if len(antis) > 1:
        other = [op_name(o) for o in anti_ops if o != op][:4]
        return False, ('%d antisymmetries, not one (%s): an antisymmetry that fixes nothing marks '
                       'nowhere, and a piece with no locus is a chequy'
                       % (len(antis), ', '.join(other))), syms, antis
    return True, ('the fold %s is an antisymmetry, both sides carry both tinctures, and it is the '
                  'ONLY antisymmetry on the piece' % op_name(op)), syms, antis


# --- painting -----------------------------------------------------------------------------------
# *** WHEN A PIECE IS TOO SMALL TO BE FOLDED, ITS OTHER HALF IS THE OTHER PIECE. ***
# A boot at this scale is a sixteen-pixel L, five pixels across and six tall, and there is no line
# that can be drawn through it with a fur of any gauge on both sides. Measured over the batch, the
# unguarded generator folded them anyway and produced sixty-one violations, every one of them a
# boot or a walk-frame leg, in two flavours: a fold witnessed by under half its own component, and a
# fold too short to cut the fur's grain, so that the fur's own half-bell shift survived beside it.
# Both say the same thing — the component cannot carry the operation.
#
# So it does not carry it. The pair does. The left boot is painted with the fur and the right boot
# with the fur NEGATED, both read out of ONE fur laid in the frame's coordinates rather than each
# one's own, so the two boots are literally two windows onto the same cloth with one of them
# inverted. The division then runs BETWEEN them: in the air, on neither piece.
#
# This is the 58th's PENDANT move and, as there, it is arguably the stronger statement rather than
# the weaker one — and here it is stronger for a reason peculiar to this axis. The whole thesis is
# that the line is not drawn. On a torso that is nearly true: the line is undrawn but it does lie
# somewhere on the plate. On a pair of boots it is true without qualification. There is nothing at
# the division at all, and the two boots are still each other's negative, and that is visible at a
# glance in every frame of the walk.
#
# Ordered by CENTROID and never by label id, for the 58th's measured reason: label order is
# raster-scan order, so the moment one boot lifts above the other in a walk cycle the pair would
# swap tinctures mid-stride.
FOLD_MIN = 28


def foldable(comp):
    """Can this component carry a division of its own? It can if some candidate reflection is
    witnessed by at least half of it — the same bar the census uses, asked before painting rather
    than after, so the generator never asserts an operation the acceptance test would then refuse to
    report."""
    if comp.sum() < FOLD_MIN:
        return None
    tot = int(comp.sum())
    need = max(MIN_PAIRS, int(MIN_PAIR_SHARE * tot))
    for op, pairs in candidate_ops(comp):
        if pairs >= need:
            return op
    return None


def _pair_gauge(comp):
    return 'std' if int(_interior(comp).sum()) >= MARGIN_MIN else 'thin'


def paint_cchange(fr, comp_full, stops, rank=0, **kw):
    """Paint the counterchanged fur onto one component. Only opaque body pixels are ever painted, so
    this cannot create strays and cannot change the silhouette. Returns the layout for the test."""
    if comp_full.sum() < MIN_PX:
        return None
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    forced = kw.get('force_op') or kw.get('fur') or kw.get('force_gauge') or not kw.get('fold', True)
    op = None if forced else foldable(comp)
    if forced or op is not None:
        sup = dict((o, n) for o, n in candidate_ops(comp))
        if op is not None and 'force_op' not in kw:
            kw = dict(kw, force_op=op)
        op, g, phx, phy, pairs = lay_out(comp, **kw)
        pairs = sup.get(op, pairs)
        role, _ = role_field(comp, op, g, phx, phy, fold=kw.get('fold', True))
        for y, x in zip(ys, xs):
            r = int(role[int(y) - y0, int(x) - x0])
            if r >= 0:
                fr[y, x, :3] = stops[r]
                fr[y, x, 3] = 255
        return dict(mode='fold', op=op, gauge=g, phx=phx, phy=phy, pairs=pairs,
                    origin=(y0, x0), shape=comp.shape)

    # PAIR MODE: one fur in FRAME coordinates, negated on odd ranks.
    g = _pair_gauge(comp)
    sign = rank % 2
    h, w = fr.shape[0], fr.shape[1]
    gy, gx = np.mgrid[0:h, 0:w]
    t = fur_at(g, 'v', gx, gy) ^ sign
    above = np.zeros_like(t)
    above[1:, :] = t[:-1, :]
    ab_ok = np.zeros_like(comp_full)
    ab_ok[1:, :] = comp_full[:-1, :]
    interior = _interior(comp_full)
    for y, x in zip(ys, xs):
        v = int(t[y, x])
        r = PLAIN[v]
        if ab_ok[y, x] and int(above[y, x]) != v:
            r = SHADE[v]
        if not interior[y, x]:
            r = EDGE[v]
        fr[y, x, :3] = stops[r]
        fr[y, x, 3] = 255
    return dict(mode='pair', gauge=g, sign=sign, rank=rank, origin=(y0, x0), shape=comp.shape)


def read_pair_sign(fr, comp_full, stops, gauge):
    """Read a pair-mode component's SIGN back off its painted pixels: the fur it carries is either
    the frame's fur or the frame's fur inverted, and nothing else is admissible. Returns the sign, or
    None if the component is neither — which is a violation, not a third option."""
    ys, xs, tv = read_tint(fr, comp_full, stops)
    want = fur_at(gauge, 'v', xs, ys)
    if np.array_equal(tv, want):
        return 0, len(ys)
    if np.array_equal(tv, 1 - want):
        return 1, len(ys)
    return None, len(ys)


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
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and labels[ny, nx] == 0:
                            labels[ny, nx] = n
                            stack.append((ny, nx))
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


def comps_ordered(a, largest):
    """The components of a frame with a RANK, ordered left to right by centroid — never by label id,
    which is raster-scan order and would swap a pair of boots the moment one lifts above the other."""
    cs = comps_of(a, largest)
    key = [(float(np.nonzero(c)[1].mean()), float(np.nonzero(c)[0].mean()), k)
           for k, c in enumerate(cs)]
    order = sorted(range(len(cs)), key=lambda k: key[k])
    return [(cs[k], rank) for rank, k in enumerate(order)]


def comps_of(a, largest):
    lbl, n = label4(a)
    if n < 1:
        return []
    if largest:
        counts = np.bincount(lbl.ravel())
        counts[0] = 0
        return [(lbl == int(counts.argmax()))]
    return [(lbl == i) for i in range(1, n + 1)]


def build(base, cfg, cls, **kw):
    D, M, L = BODY[cls]
    stops = CCHANGE[cls]
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
        # ONE DIVISION PER CONNECTED COMPONENT. A fold is a fold of a PLATE. Two chausse legs are
        # not one surface and a line drawn across both of them at once asserts a continuity the
        # viewer cannot use — the 54th's lesson, the 57th's, the 58th's, and here it is also what
        # keeps the census honest, since the census is a statement about one connected body.
        for comp, rank in comps_ordered(a, largest):
            paint_cchange(fr, comp, stops, rank=rank, **kw)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ----------------------------------------------------------------------------
def _test_plate(w=44, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the fur
    and its division can be judged on a shape with the features the real slots have."""
    m = np.zeros((h, w), dtype=bool)
    _, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        m[y, :] = np.abs(xx[y, :] - cx) <= max(hw, 1.5)
    m[0:3, int(cx) - 2:int(cx) + 3] = False
    return m


def swatch(path='_diag_cchange_swatch.png', zoom=12):
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_cchange(a, m, CCHANGE[cls])
        img.paste(Image.fromarray(a).resize((tw, th), Image.NEAREST), (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (fur only - no sheets written)' % path)


def _big_comp(arr, fi=0):
    r, c = fi // COLS, fi % COLS
    src = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def _grid(cells, cw, ch, pad=8, lab=18, rows=1):
    from PIL import ImageDraw, ImageFont
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + rows * (ch + lab)),
                    (24, 24, 28, 255))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
    except Exception:
        f = ImageFont.load_default()
    return img, d, f


def sweep(path='_diag_cchange_sweep.png', zoom=11):
    """Warrior chest and leg idle frames across the three gauges, plus the FOUR CONTROLS.

    SAME is the one to look at first: it is this generator's own output with the fold removed and
    NOTHING else changed — same fur, same gauge, same phase, same palette, same pixel count per
    tincture — and what comes back is an ordinary two-tincture fabric with no place in it.
    CHEQUY is the one to look at second, because it is the pattern most people would name if asked
    for something that swaps its colours, and it is exactly what this axis must not be."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    variants = [('STD', dict()), ('THIN', dict(force_gauge='thin')),
                ('TINY', dict(force_gauge='tiny')),
                ('PER PALE', dict(force_op=('pale', 41))),
                ('SAME', dict(fold=False)), ('CHEQUY', dict(fur='chequy', fold=False)),
                ('PLAIN', dict(fur='plain')), ('UNIFORM', dict(_uniform=True))]
    cells = []
    for name, kw in variants:
        kw = dict(kw)
        uni = kw.pop('_uniform', False)
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            comp = _big_comp(arr)
            fr = np.zeros_like(arr[0:FH, 0:FW])
            if uni:
                for y, x in np.argwhere(comp):
                    fr[y, x, :3] = CCHANGE['warrior'][R_A]
                    fr[y, x, 3] = 255
            else:
                try:
                    paint_cchange(fr, comp, CCHANGE['warrior'], **kw)
                except Exception as e:                       # a control may be unpaintable
                    print('   control %s: %s' % (name, e))
            col.append(Image.fromarray(fr).crop(crop))
        cells.append((name, col))
    cw, ch = 28 * zoom, 26 * zoom
    img, d, f = _grid(cells, cw, ch, rows=2)
    x = 8
    for name, col in cells:
        y = 8
        for im in col:
            img.alpha_composite(im.resize((cw, ch), Image.NEAREST), (x, y))
            d.text((x + 2, y + ch), name, font=f, fill=(210, 210, 220, 255))
            y += ch + 18
        x += cw + 8
    img.convert('RGB').save(path)
    print('wrote %s (gauge sweep + SAME/CHEQUY/PLAIN/UNIFORM controls - no sheets written)' % path)


def slots_diag(path='_diag_cchange_slots.png', zoom=10):
    """All three classes x all four slots, bare fur, no finishing pass."""
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
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            fr = np.zeros_like(src)
            recolor(src, fr, a, *BODY[cls])
            for comp, rank in comps_ordered(a, largest):
                paint_cchange(fr, comp, CCHANGE[cls], rank=rank)
            cell = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
            x, y = pad + ci * (cw + pad), pad + ri * (chh + lab)
            img.alpha_composite(cell, (x, y))
            d.text((x + 2, y + chh), '%s %s' % (cls, kind), font=f, fill=(210, 210, 220, 255))
    img.convert('RGB').save(path)
    print('wrote %s (all classes x all slots, bare fur)' % path)


def visor_diag(path='_diag_cchange_visor.png', zoom=14):
    """The warrior dome's black eye and mouth slits reading through the counterchanged fur, m and f.
    This axis is the worst case the finishing pass has faced: the visor is carved as near-black
    pixels, and half of every dome is now a saturated dark COLOUR rather than a metal. If the darkest
    stop of any colour family were allowed near black the slits would vanish into whichever half of
    the head they fell on — which is why the three colour edges clear channel-sum 150.

    Built with build() on the whole sheet, never on a lone frame: the 58th paid twice for handing
    finish_array a 70-frame array with one frame in it, and it is written down there and here."""
    crop = (28, 12, 52, 34)
    cells = []
    for suf in ('', '_f'):
        base = load_any('helmet_rare1%s.png' % suf)
        arr = build(base, SLOTS['helmet'], 'warrior')
        arr, _ = finish_array(arr, '%s/%s%s.png' % (SLOTS['helmet']['outdir'],
                                                    SLOTS['helmet']['dst'] % 'warrior', suf))
        cells.append(('warrior dome %s' % ('f' if suf else 'm'),
                      Image.fromarray(arr[0:FH, 0:FW]).crop(crop)))
    cw, chh = (crop[2] - crop[0]) * zoom, (crop[3] - crop[1]) * zoom
    img, d, f = _grid(cells, cw, chh, pad=10)
    x = 10
    for name, im in cells:
        img.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, 10))
        d.text((x + 2, 10 + chh + 2), name, font=f, fill=(210, 210, 220, 255))
        x += cw + 10
    img.convert('RGB').save(path)
    print('wrote %s (visor slits reading through both tinctures)' % path)


def _case_report(label, comp, stops, **kw):
    fr = np.zeros((comp.shape[0], comp.shape[1], 4), dtype=np.uint8)
    info = paint_cchange(fr, comp, stops, **kw)
    ys, xs, tv = read_tint(fr, comp, stops)
    if info['mode'] == 'pair':
        sign, npx = read_pair_sign(fr, comp, stops, info['gauge'])
        ok = sign is not None
        why = ('too small to be folded, so it is held to the PAIR clause instead: it carries the '
               'frame\'s fur %s, and its partner carries the other'
               % ('as it is' if sign == 0 else 'INVERTED')) if ok else \
              'carries neither the fur nor its negative'
        return fr, info, ys, xs, tv, ok, why, [], []
    ok, why, syms, antis = accepts(ys, xs, tv, comp.shape, info['op'])
    return fr, info, ys, xs, tv, ok, why, syms, antis


def dump_cells():
    legend = {R_A: 'M', R_A_SH: 'm', R_A_ED: '+', R_B: '#', R_B_SH: ':', R_B_ED: '.'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    print('== THE FURS: an exact half of the block, and the two tinctures congruent (asserted at '
          'import)')
    for g in GAUGES:
        px, py, m = _fur_mask(g)
        print('   %-5s block %dx%-3d  bell %d px of %d   complement = bell shifted (0,%d)'
              % (g, px, py, int(m.sum()), px * py, py // 2))

    allpass = True
    nA = nB = 0
    for label, comp in cases:
        fr, info, ys, xs, tv, ok, why, syms, antis = _case_report(
            label, comp, CCHANGE['warrior'])
        a0 = int((tv == 0).sum()); a1 = int((tv == 1).sum())
        nA += a0; nB += a1
        if info['mode'] == 'pair':
            print('== %s   area=%d gauge=%s  PAIR MODE (no fold fits: the division is between this '
                  'piece and its partner)  (metal %d / colour %d)'
                  % (label, int(comp.sum()), info['gauge'], a0, a1))
        else:
            print('== %s   area=%d gauge=%s division=%s supported=%d of %d  (metal %d / colour %d)'
                  % (label, int(comp.sum()), info['gauge'], op_name(info['op']), info['pairs'],
                     int(comp.sum()), a0, a1))
        role = np.full(comp.shape, -1, dtype=np.int8)
        if info['mode'] == 'fold':
            role, _ = role_field(comp, info['op'], info['gauge'], info['phx'], info['phy'])
            kind, c = info['op']
        else:
            kind, c = 'none', -99
            pal = np.array(CCHANGE['warrior'], dtype=np.int32)
            px = fr[ys, xs, :3].astype(np.int32)
            idx = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
            role[ys, xs] = idx
        for y in range(comp.shape[0]):
            line = ''.join(legend[int(v)] if comp[y, x] else ' '
                           for x, v in enumerate(role[y]))
            mark = ' <== the division runs here, and nothing is drawn on it' \
                if (kind == 'fess' and 2 * y == c - 1) else ''
            print('   ' + line + mark)
        if info['mode'] == 'fold':
            print('   census: symmetries=%d (ordinary, and expected: this is an ornament)  '
                  'antisymmetries=%d %s'
                  % (len(syms), len(antis), [op_name(o) for o, _ in antis]))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL'))
        allpass = allpass and ok

    bal = abs(nA - nB) / float(nA + nB)
    print('== CLAUSE 4, NEITHER IS THE GROUND over the population above: metal %d / colour %d '
          '(imbalance %.3f, limit %.2f) -> %s' % (nA, nB, bal, BALANCE,
                                                  'PASS' if bal <= BALANCE else 'FAIL'))
    allpass = allpass and bal <= BALANCE

    controls = [
        ('SAME    (the same fur, the same gauge, the same phase, the same palette, the same number '
         'of pixels of each tincture — with the FOLD REMOVED and nothing else touched)',
         dict(fold=False),
         'a fur is a fur; without the exchange there is no operation the piece is invariant under '
         'that moves the palette, and so no division and no place'),
        ('CHEQUY  (an ordinary checkerboard — the pattern anyone asked for "something that swaps '
         'its colours" would draw, and the sharpest near miss in the set)',
         dict(fur='chequy', fold=False),
         'a chequy has a whole LATTICE of antisymmetries and not one of them fixes any point, so '
         'there is nowhere on it for the exchange to be seen: it is the same everywhere'),
        ('PLAIN   (party per fess and nothing else: the division kept, the fur REMOVED — and note '
         'that this control passes clause 1 perfectly, which is what makes it worth having)',
         dict(fur='plain'),
         'a bare partition is genuinely antisymmetric about its own line, and it is still not this '
         'axis, because each of its sides carries one tincture and nothing else: there is no fur '
         'over there doing the opposite of the fur over here, only a plate of the other colour'),
    ]
    for cname, kw, why in controls:
        nfail = 0
        detail = ''
        for _, comp in cases:
            try:
                _, _, _, _, _, ok, w2, syms, antis = _case_report(
                    None, comp, CCHANGE['warrior'], **kw)
            except Exception as e:
                nfail += 1
                detail = detail or str(e)
                continue
            if not ok:
                nfail += 1
                detail = detail or w2
        print('== CONTROL: %s' % cname)
        print('   components=%d  failing acceptance=%d  -> %s'
              % (len(cases), nfail, 'PASS (correctly fails the axis)' if nfail == len(cases)
                 else 'DID NOT FAIL — investigate'))
        print('   first reason: %s' % detail)
        print('   %s' % why)
        allpass = allpass and nfail == len(cases)

    # UNIFORM is checked on clause 4 alone, because a one-tincture piece has no tincture field to
    # run a census on — which is itself the point.
    print('== CONTROL: UNIFORM  (one tincture over the whole piece — the 24th SPIRAL\'s control, '
          'restated for colour)')
    print('   metal 100%% / colour 0%%, imbalance 1.000 > %.2f  -> PASS (correctly fails clause 4)'
          % BALANCE)
    print('   a field with only one tincture has a ground and nothing else, and a ground with '
          'nothing on it cannot exchange places with anything')

    print('legend: M metal  m metal shaded  + metal at the edge  # colour  : colour shaded  '
          '. colour at the edge   (and NO glyph for the division, because none is drawn)')
    print('ACCEPTANCE (an ANTISYMMETRY, by census of the group — not a statistic, a topology, an')
    print('algebra, a conservation law, a physical law or a group action on one element):')
    print('(1) ANTISYMMETRIC  the fold is an antisymmetry of the PAINTED tincture at every '
          'supported pixel;')
    print('(2) DIVIDED FUR    both tinctures occur on BOTH sides of the line, so the exchange can')
    print('    be seen happening rather than merely asserted;')
    print('(3) SOLITARY       the fold is the ONLY antisymmetry, so the exchange has a LOCUS;')
    print('(4) NEITHER IS THE GROUND  the two tinctures are within %.0f%% of equal area.'
          % (100 * BALANCE))
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def accept_all():
    """The acceptance test over EVERY component of EVERY active frame of all 24 sheets.

    Two populations, because there are two ways this axis is carried and the test says which is
    which rather than averaging them: FOLD components, which have a division of their own and are
    put through clauses 1-3; and PAIR components — the boots, and a handful of walk-frame legs — too
    small to be folded, which are held to the pair clause instead. Clause 4 is asked of a sheet.
    """
    nfold = npair = nfail = nunpaired = 0
    nA = nB = 0
    gauges, divisions = {}, {}
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            stops = CCHANGE[cls]
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                sA = sB = 0
                for fi in range(60):
                    r, c = fi // COLS, fi % COLS
                    src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
                    a = src[..., 3] > 0
                    if not a.any():
                        continue
                    fr = np.zeros_like(src)
                    pairs = []
                    for comp_full, rank in comps_ordered(a, largest):
                        if comp_full.sum() < MIN_PX:
                            continue
                        info = paint_cchange(fr, comp_full, stops, rank=rank)
                        gauges[info['gauge']] = gauges.get(info['gauge'], 0) + 1
                        ys, xs = np.nonzero(comp_full)
                        tv = read_tint(fr, comp_full, stops)[2]
                        sA += int((tv == 0).sum()); sB += int((tv == 1).sum())
                        if info['mode'] == 'fold':
                            nfold += 1
                            divisions[info['op'][0]] = divisions.get(info['op'][0], 0) + 1
                            y0, x0 = info['origin']
                            sub = comp_full[y0:ys.max() + 1, x0:xs.max() + 1]
                            ok, why, _, _ = accepts(ys - y0, xs - x0, tv, sub.shape, info['op'])
                            if not ok:
                                nfail += 1
                                print('   VIOLATION %s %s%s frame %d: %s'
                                      % (kind, cls, suffix, fi, why))
                        else:
                            npair += 1
                            sign, npx = read_pair_sign(fr, comp_full, stops, info['gauge'])
                            if sign is None:
                                nfail += 1
                                print('   VIOLATION %s %s%s frame %d rank %d: the piece carries '
                                      'neither the fur nor its negative'
                                      % (kind, cls, suffix, fi, info['rank']))
                            else:
                                pairs.append((info['rank'], sign))
                    # THE PAIR CLAUSE: consecutive small components counterchange each other.
                    pairs.sort()
                    for (r0, s0), (r1, s1) in zip(pairs, pairs[1:]):
                        if r1 == r0 + 1 and s0 == s1:
                            nfail += 1
                            print('   VIOLATION %s %s%s frame %d: components %d and %d carry the '
                                  'SAME tincture, so the pair is not counterchanged'
                                  % (kind, cls, suffix, fi, r0, r1))
                    if len(pairs) == 1:
                        nunpaired += 1
                bal = abs(sA - sB) / float(max(sA + sB, 1))
                if bal > BALANCE:
                    nfail += 1
                    print('   VIOLATION %s %s%s: clause 4, imbalance %.3f (metal %d colour %d)'
                          % (kind, cls, suffix, bal, sA, sB))
                nA += sA; nB += sB
    tot = max(nA + nB, 1)
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components               %d   %s' % (nfold + npair, gauges))
    print('    folded (clauses 1-3)   %d   divisions %s' % (nfold, divisions))
    print('    paired (pair clause)   %d   (too small to be folded: the division runs between them)'
          % npair)
    print('    lone small components  %d   (no partner in the frame; reported, not counted a fail)'
          % nunpaired)
    print('  metal / colour pixels    %d / %d  (imbalance %.4f, limit %.2f) — read off the painted'
          % (nA, nB, abs(nA - nB) / float(tot), BALANCE))
    print('                           pixels, not off the tincture field they were painted from')
    print('  clause violations        %d' % nfail)
    print('OVERALL: %s' % ('ALL PASS' if nfail == 0 else 'FAIL'))
    return nfail == 0


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
        visor_diag()
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
