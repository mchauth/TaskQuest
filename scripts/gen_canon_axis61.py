#!/usr/bin/env python3
"""SIXTY-FIRST net-new-geometry axis for ALL FOUR SLOTS — the CANON family: whatever the piece is,
it is divided top to bottom into exactly THREE raised hoops in the proportions 3 : 2 : 1, and each
hoop is itself divided into the proportions 1 : 1 : 2 : 1 : 1 — shade, field, crest, field, shade.
There is no pitch. There is no gauge. There is not one length anywhere in this file measured in
pixels. The armour is told a proportion and it works out its own sizes.

    the ornament is  CREST  (the lit ridge along the middle of a hoop — a QUARTER of the hoop,
                             never one pixel, never two: a quarter)
                   + FIELD  (the flank of the hoop turning away from the crest)
                   + SHADE  (the hoop's outer rows, where it meets the next hoop; two SHADE rows
                             meeting is the seam, and the seam is the only line in the piece)

*** THIS IS THE FIRST AXIS WHOSE INVARIANT IS A RATIO AND NOT A LENGTH. ***
Every one of the sixty before it fixes a distance. The 11th flutes every 3 pixels, the 40th hangs a
tooth every 4, the 46th takes 4.5 and the 51st takes 3.6, the 52nd keeps its two periods coprime and
the 60th makes its pitch irrational — but a pitch it has, and it is a number of pixels, and it is
the same number of pixels on a cuirass as on a sabaton. That is why every one of them looks like a
MATERIAL: a constant gauge is what says "these pieces are cut from one bolt of the same stuff".

This axis has no gauge. Ask it how wide a hoop is and it has no answer until it is shown the piece.
On a warrior chest fifteen rows tall the hoops come out 8, 4 and 3; on the sabaton of the same suit,
six rows tall, they come out 3, 2 and 1 — and 3 : 2 : 1 is exactly six parts, so the smallest piece
in the game is the ornament at its irreducible minimum, one pixel to the part. The boot is not a
detail of the cuirass. It is the same drawing, printed small.

*** THE ACCEPTANCE TEST IS A NEW KIND: A CLAIM OF SIMILARITY. ***
The 54th is accepted on a topology, the 55th on the algebra of an order, the 56th on a conservation
law read off a traversal, the 57th on a physical law, the 58th on a group action, the 59th on a
census of a group, the 60th on the complexity of a formal language. Every one of those is a
statement about ONE picture. This one cannot be made about one picture at all: a single hoop pattern
is in 3 : 2 : 1 or it is not, and that is arithmetic, not an axis. What is being claimed is that
several HUNDRED pictures at a factor of three in size are all the SAME picture — that they are
similar in the geometer's sense, related by a scale factor and nothing else. So the test measures
the ornament on every component the batch contains, re-derives what the canon says that component's
widths must be FROM ITS OWN EXTENT ALONE, and asks whether the two agree everywhere; and then, so
that the agreement cannot be an accident of everything being the same size, it asks how far apart
the largest and smallest gauges in the batch actually are.

    (1) PARTITION      exactly one crest run per hoop — three, no more and no fewer — and every
                       row of the extent carrying a readable role. Nothing left over.
    (2) PLACED         the crest CENTRES are where the canon of 3 : 2 : 1 puts them, re-derived
                       from the component's own extent and nothing else. A crest sits in the
                       middle of its hoop whatever length the crest is, so where the crests are
                       IS a measurement of where the hoops are — and this clause is therefore a
                       statement about the proportion and about nothing else. This is the axis.
    (3) SELF-SIMILAR   the crest RUN LENGTHS are the quarter each hoop's own canon gives it, so
                       the crest scales with the hoop and there is no pixel constant anywhere, at
                       either level. A statement about the inside of a hoop and about nothing
                       else.
    (4) CANONICAL      the umbrella: row for row, every painted role is the role the canon puts
                       there. It implies 1-3, and is stated separately because a test that only
                       reports its umbrella cannot say WHAT went wrong.
    (5) SCALE-FREE     over the batch, the largest gauge is at least twice the smallest. Reported
                       as a histogram. Without this clause the other four are satisfiable by an
                       axis that never has to scale anything, and the claim would be empty.

*** THE FIVE CONTROLS. THEY DO NOT EACH FAIL A DIFFERENT CLAUSE — THEY FAIL IN TWO GROUPS, AND
    THE SPLIT BETWEEN THE GROUPS IS EXACTLY THE SPLIT BETWEEN THE AXIS'S TWO LEVELS. ***
    FIXED-3       a 3-pixel hoop everywhere. Fails PARTITION: a chest gets five crest runs and a
                  boot gets two. It is not a straw man — it is the 11th FLUTING, and it is this
                  axis's lower collapse boundary. Fix the gauge and the count falls out; that is
                  axis 11.
    EQUAL         1 : 1 : 1. Passes PARTITION, fails PLACED — its crest centres land 2.5 rows off
                  on a warrior chest. THIS IS THE CONTROL THE AXIS EXISTS AGAINST: three equal
                  hoops is the 12th axis's BANDED LAMELLAR, it is the first thing anyone would
                  draw, and on a six-row sabaton it is 2:2:2 against this axis's 3:2:1 — one pixel
                  of difference, and the whole content of the axis.
    GOLDEN        1 : phi : phi-squared. Fails PLACED by 4.5 rows. It exists to show that the test
                  discriminates WHICH ratio and not merely "unequal", which is what a looser test
                  would have settled for.
    REMAINDER     each width rounded independently, round(E*r/6), instead of by cumulative
                  boundaries. Leaves a row over on 32 of the 194 extents from 6 to 199 and fails
                  there; on the rest it fails SELF-SIMILAR, because a hoop one row out gets a
                  crest of the wrong quarter. This is the bug the axis would have shipped with.
    FIXED-CREST   hoops proportional, but the crest pinned at 1 pixel the way every other axis in
                  the set pins it. IT IS THE ONLY CONTROL THAT REACHES SELF-SIMILAR WITH THE
                  PROPORTION ALREADY RIGHT — it passes PARTITION and PLACED and fails on the
                  insides — and that is what makes it the sharpest near miss of the five: it is
                  this axis applied to only half of itself, so a large hoop reads as a flat panel
                  with a wire down it instead of as the same roll seen larger.

    So the controls sort into "wrong proportion" (EQUAL, GOLDEN, and REMAINDER where it rounds
    badly) and "right proportion, wrong insides" (FIXED-CREST, and REMAINDER elsewhere), with
    FIXED-3 outside both because it does not have three hoops at all. Reporting that honestly is
    better than picking four controls that happen to line up one per clause.

*** THE PRICE, AND IT IS THE EXACT REVERSE OF THE AXIS IMMEDIATELY BEFORE IT. ***
The 60th CADENCE forbids per-component adaptation outright — a word re-phased to suit each plate is
a different word on each plate, so there is no one word for the pieces to be windows of. This axis
is nothing BUT per-component adaptation, and it is compulsory: a hoop that took its size from
anywhere except the component it is on would break the similarity, which is the whole claim. The
two axes are the same question answered at opposite ends. The 60th is one text quoted everywhere at
constant type size; this is one figure printed at whatever size the paper happens to be.

A consequence worth naming rather than hiding: the ornament BREATHES. A leg that lengthens by a row
through the run cycle gets a proportionally taller hoop on that frame. On a fixed-gauge axis that
would be a defect — the pattern would appear to slide under the animation. Here it is the axis
working: the armour is fitted to the piece, and the piece moves.

*** DISTINCTNESS. ***
  * 11th FLUTING / 43rd GADROON / 12th BANDED-LAMELLAR — parallel hoops at a fixed pitch. They are
    the FIXED-3 and EQUAL controls, and naming them is how this axis states its own boundaries.
  * 60th CADENCE — see above; the exact complement, and deliberately so.
  * 47th MOKUME — shape-conformal, tone = f(distance to the silhouette) rather than f(y). Real
    adaptation, but its band pitch is still a fixed number of pixels: a mokume ring is the same
    thickness on a boot as on a chest, and this axis's hoop is not.
  * 48th COSMATI — three ranks at 8 : 5 : 2, which IS a ratio. But it is a ratio between the ranks
    at a fixed bay size; a cosmati bay is the same size everywhere it appears. Here nothing has a
    size at all until it is placed.
  * 53rd GRANULATION — "the first axis whose element size is an OUTPUT", and the nearest prior
    claim in the whole set. The distinction is exact and it is about LOCALITY: a granulation bead's
    radius is an output of the room the silhouette leaves AT THAT POINT and varies within one
    piece, so the 53rd's evidence is a histogram of radii per slot. This axis is global — the piece
    is divided all at once, and its evidence is ONE gauge per component. The 53rd adapts inside a
    piece; this adapts between pieces and is rigid inside one.
  * 55th STRATA — broad bands, but the subject is which was laid over which. These hoops never
    overlap and there is no order of laying; they are a PARTITION, and a partition is exactly what
    an order is not.

Geometry, per connected component, in the component's own frame:
    extent    E = the component's own bounding-box height. Nothing else is consulted.
    hoops     three, at cumulative boundaries round(E/2) and round(5E/6) — cumulative, not
              independent, which is what makes the widths sum to E for every E (see REMAINDER).
    parts     each hoop split by the same cumulative rule on 1 : 1 : 2 : 1 : 1, with the three
              degenerate widths written out (w=1 is a crest, w=2 is crest over shade, w=3 is
              shade-crest-shade) because a proportion cannot be honoured below six parts and
              pretending otherwise is how a test gets tuned until it passes.
    minimum   a component shorter than SIX rows cannot carry six parts and is left as a plain
              recolor. Reported, never failed. Six is not a tolerance, it is the sum of the canon.

Authoring philosophy identical to gen_cadence_axis60.py / gen_counterchange_axis59.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed,
silhouette untouched, so the generator cannot create isolated pixels, background bleed, extra
components or a changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Seventeenth generator to call it in-line, after axes 45-60.

Run from repo root:
  python3 scripts/gen_canon_axis61.py
  python3 scripts/gen_canon_axis61.py --canon     # the canon at every extent 6..40, and the controls
  python3 scripts/gen_canon_axis61.py --cells     # ASCII dump of five real components + the clauses
  python3 scripts/gen_canon_axis61.py --accept    # the clauses over every component of all 24 sheets
  python3 scripts/gen_canon_axis61.py --swatch    # bare hooping on test plates at five sizes
  python3 scripts/gen_canon_axis61.py --sweep     # slots + visor + the five controls
Then QA (examples):
  python3 scripts/sprite_qa.py _canon_legendary_preview/shirt_warrior_legendary61.png
  python3 scripts/sprite_qa.py _canondome_helmet_preview/helmet_mage_legendary61.png --y-min 2
  python3 scripts/sprite_qa.py _canon_boots_preview/boots_warrior_legendary_canon.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# THREE roles and there is deliberately no fourth. No silhouette rim, no edge tone. Every axis from
# the 52nd on demotes the boundary to a quiet fourth stop when the component has interior enough to
# spare it; this one must not, for two reasons that are the same reason. A rim is a ONE-PIXEL
# feature, and one pixel is a length; and a rimmed row is a row the reader cannot measure, which on
# an axis whose entire evidence is a measured width would mean throwing away exactly the rows the
# silhouette makes narrow. Three tones, every pixel readable, no censored sample. (Compare the 60th,
# where the censoring of wide reeds by the silhouette was the one thing that axis got wrong first
# time and had to be fixed by changing the estimator.)
R_CREST, R_FIELD, R_SHADE = 0, 1, 2
ROLENAME = {R_CREST: 'CREST', R_FIELD: 'FIELD', R_SHADE: 'SHADE'}

# THE CANON. Three hoops, top to bottom, widest first: the piece is broad at the shoulder and
# narrows to the waist, at the hip and narrows to the ankle, at the crown and narrows to the nape.
# 3 : 2 : 1 sums to SIX, and six is the smallest sum for which every part is at least one pixel on
# the smallest component the game contains — a sabaton six rows tall. 4 : 3 : 2 : 1 sums to ten and
# would leave the boots unhoopable; 2 : 1 sums to three and is not a taper, it is two bands.
CANON = (3.0, 2.0, 1.0)
# THE HOOP'S OWN CANON. shade : field : crest : field : shade. The crest is a QUARTER of the hoop at
# every size — that is the clause FIXED-CREST fails, and the reason a large hoop reads as the same
# roll seen larger rather than as a panel with a wire down it.
INNER = (1.0, 1.0, 2.0, 1.0, 1.0)
INNER_ROLES = (R_SHADE, R_FIELD, R_CREST, R_FIELD, R_SHADE)
# Sum of the canon: the shortest component that can carry it. Not a tolerance — an identity.
MIN_EXTENT = int(sum(CANON))
assert MIN_EXTENT == 6


# --- the canon ------------------------------------------------------------------------------
def parts(E, ratio):
    """Divide E into len(ratio) parts in the given proportion, by CUMULATIVE boundaries.

    This is the whole of the axis and it is three lines long. It is written this way, and not as
    [round(E*r/tot) for r in ratio], because the second form rounds each part against its own ideal
    and the results do not have to sum to E — on a fifteen-row chest 3:2:1 rounds independently to
    8, 5, 3 = 16, one row more than the chest has. Rounding the BOUNDARIES instead makes the parts
    the differences of integers, so they sum to E by construction, for every E, with no remainder
    rule and nothing to tune. That is the REMAINDER control, and it is the bug this axis would have
    shipped with.
    """
    tot = float(sum(ratio))
    cum, bounds = 0.0, [0]
    for r in ratio[:-1]:
        cum += r
        bounds.append(int(round(E * cum / tot)))
    bounds.append(E)
    return [bounds[i + 1] - bounds[i] for i in range(len(ratio))]


def hoop_profile(w):
    """The role of each row of a hoop w rows tall, from its own canon.

    The three short cases are written out rather than derived. A proportion in five parts cannot be
    honoured in fewer than five rows, and the honest thing is to say what the ornament degenerates
    to rather than let the rounding pick for us: one row is a crest, two rows are a crest over a
    shade, three rows are a shade, a crest and a shade. Four rows and up take the canon.
    """
    if w <= 0:
        return []
    if w == 1:
        return [R_CREST]
    if w == 2:
        return [R_CREST, R_SHADE]
    if w == 3:
        return [R_SHADE, R_CREST, R_SHADE]
    out = []
    for n, role in zip(parts(w, INNER), INNER_ROLES):
        out += [role] * n
    assert len(out) == w
    if R_CREST not in out:                    # cannot happen for w >= 4; asserted, not repaired
        raise AssertionError('hoop of %d rows came out with no crest' % w)
    return out


def canon_profile(E, ratio=CANON, inner=True):
    """The role of every row of a component E rows tall. Returns (roles, hoop_widths)."""
    ws = parts(E, ratio)
    roles = []
    for w in ws:
        if inner:
            roles += hoop_profile(w)
        else:                                  # FIXED-CREST control: crest pinned at one pixel
            roles += _fixed_crest_profile(w)
    return roles, ws


def _fixed_crest_profile(w):
    """The FIXED-CREST control — hoops proportional, crest one pixel, the way every other axis in
    the set pins its highlight. Not used by the generator; it exists to be failed."""
    if w <= 0:
        return []
    if w == 1:
        return [R_CREST]
    if w == 2:
        return [R_CREST, R_SHADE]
    out = [R_FIELD] * w
    out[0] = R_SHADE
    out[-1] = R_SHADE
    out[w // 2] = R_CREST
    return out


CONTROLS = ('fixed-3', 'equal', 'golden', 'remainder', 'fixed-crest')
PHI = (1.0 + math.sqrt(5.0)) / 2.0


def control_profile(mode, E):
    """Role sequence for one of the five controls, over an extent of E rows."""
    if mode == 'fixed-3':                      # axis 11 FLUTING: a fixed 3px hoop, count falls out
        n = max(1, int(round(E / 3.0)))
        ws = parts(E, tuple([1.0] * n))
        roles = []
        for w in ws:
            roles += hoop_profile(w)
        return roles, ws
    if mode == 'equal':                        # axis 12 BANDED LAMELLAR
        return canon_profile(E, (1.0, 1.0, 1.0))
    if mode == 'golden':
        return canon_profile(E, (1.0, PHI, PHI * PHI))
    if mode == 'remainder':                    # each width rounded against its own ideal
        tot = float(sum(CANON))
        ws = [int(round(E * r / tot)) for r in CANON]
        roles = []
        for w in ws:
            roles += hoop_profile(w)
        return roles[:E] if len(roles) >= E else roles + [R_SHADE] * (E - len(roles)), ws
    if mode == 'fixed-crest':
        return canon_profile(E, CANON, inner=False)
    raise ValueError(mode)


# --- palette --------------------------------------------------------------------------------
# THREE stops per class: crest, field, shade. One ramp, no second colour family — the ornament is a
# relief, and a second family would let the eye read the hoops off the palette instead of off their
# widths, which is the only thing this axis has to say.
#
# THE HUE PLAN, against the tiers this will sit beside. The 59th took azure / purpure / vert on or
# and argent; the 60th took brass / moonstone / verdigris. This one is lacquer over metal and keeps
# clear of both:
#   warrior  OXIDISED CRIMSON STEEL   red-grey, cool for a red
#   mage     AMETHYST                 violet, well clear of the 60th's moonstone
#   ranger   DEEP TEAL                blue-green, well clear of the 60th's verdigris (which is warm)
#
# NO STOP NEAR PURE BLACK: the finishing pass carves the visor as black eye and mouth pixels and a
# near-black darkest stop swallows them (the 49th's lesson). Darkest channel-sums 224 / 330 / 280.
#
# The warrior crest was (236,198,190) on the first render and came back SALMON. The finishing pass
# lifts a sheet before anything else happens to it, so a stop chosen to look right in the swatch is
# already too light by the time it reaches the preview; a crest is chosen for what it becomes, not
# for what it is. Dropped to (232,176,164) with the field pushed toward the red it is supposed to be
# oxidised to.
CANONPAL = {
    'warrior': ((232, 176, 164), (168, 84, 80), (104, 48, 52)),
    'mage':    ((226, 208, 244), (156, 122, 200), (96, 72, 140)),
    'ranger':  ((202, 234, 226), (100, 166, 158), (54, 104, 106)),
}

# Per-class body tones for the plain recolor, visible on sleep frames and on components too short
# to carry the canon.
BODY = {
    'warrior': ((104, 48, 52), (168, 84, 80), (232, 176, 164)),
    'mage':    ((96, 72, 140), (156, 122, 200), (226, 208, 244)),
    'ranger':  ((54, 104, 106), (100, 166, 158), (202, 234, 226)),
}

SLOTS = {
    'chest': dict(
        outdir='_canon_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary61', largest=True,
    ),
    'legs': dict(
        outdir='_canon_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary61', largest=False,
    ),
    'boots': dict(
        outdir='_canon_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_canon', largest=False,
    ),
    'helmet': dict(
        outdir='_canondome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary61', largest=True,
    ),
}


# --- painting -------------------------------------------------------------------------------
def paint_canon(fr, comp_full, stops, ratio=CANON, inner=True, mode=None):
    """Paint the hooping onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette.

    Everything this function knows about sizes it learns from `comp_full` in its first two lines.
    There is no constant in it."""
    if comp_full.sum() < MIN_PX:
        return None
    ys, xs = np.nonzero(comp_full)
    y0, y1 = int(ys.min()), int(ys.max())
    E = y1 - y0 + 1
    if E < MIN_EXTENT:
        return None                            # cannot carry six parts; reported, never failed
    if mode is not None:
        roles, ws = control_profile(mode, E)
    else:
        roles, ws = canon_profile(E, ratio, inner=inner)
    if len(roles) != E:                        # only the REMAINDER control can land here
        roles = (roles + [R_SHADE] * E)[:E]
    for i in range(len(ys)):
        y, x = int(ys[i]), int(xs[i])
        fr[y, x, :3] = stops[roles[y - y0]]
        fr[y, x, 3] = 255
    return dict(E=E, widths=list(ws), roles=roles, y0=y0,
                area=int(comp_full.sum()), shape=comp_full.shape)


# --- reading the hooping back off the painted pixels ------------------------------------------
def read_hoops(fr, comp_full, stops):
    """Read the hooping off the PAINTED PIXELS and return (crest_runs, row_roles, E).

    The counterpart of the 60th's read_word() and the 59th's read_tint(): the acceptance test is run
    on what is ON THE SHEET, not on what the painter intended. Because this axis has no fourth stop
    every row of every component is readable, so unlike the 60th there is no censored sample here
    and no estimator to correct — what comes back below is a measurement, not an estimate of one.

    WHAT IS MEASURED, AND WHY IT IS THE CREST AND NOT THE SEAM. The first draft of this reader
    segmented hoops at their seams, by walking the rows and starting a new hoop wherever the
    brightness stopped falling. That is wrong twice over and both are instructive. It splits a hoop
    down the middle whenever its crest is more than one row — which on this axis is MOST hoops,
    because the crest is a quarter of the hoop and hoops are large; and even repaired, a seam is the
    one feature of this ornament that cannot be located from the pixels alone, because two adjacent
    hoops each contribute shade rows to it and nothing in the picture says where one lot ends. The
    CREST RUNS have neither problem: they are unambiguous, there is exactly one per hoop, and on
    this canon (3 : 2 : 1, widest first) no two of them are ever adjacent, so counting them counts
    the hoops. Everything the test needs is a function of them and of the row roles.
    """
    ys, xs = np.nonzero(comp_full)
    y0, y1 = int(ys.min()), int(ys.max())
    E = y1 - y0 + 1
    px = fr[ys, xs, :3].astype(np.int32)
    pal = np.array(stops, dtype=np.int32)
    role = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)

    rows = [None] * E
    ty = ys - y0
    for t in range(E):
        sel = ty == t
        if sel.any():
            rows[t] = int(np.bincount(role[sel], minlength=3).argmax())

    runs, start = [], None
    for t in range(E):
        if rows[t] == R_CREST and start is None:
            start = t
        elif rows[t] != R_CREST and start is not None:
            runs.append((start, t - start))
            start = None
    if start is not None:
        runs.append((start, E - start))
    return runs, rows, E


def crest_part(w):
    """How many rows of a hoop w tall the hoop's own canon gives to its crest."""
    if w <= 3:
        return 1
    return parts(w, INNER)[2]


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — a SIMILARITY, by measurement.
#
#   (1) PARTITION     exactly len(CANON) crest runs on the component — one hoop per crest, no
#                     more and no fewer — and the roles cover the extent with nothing left over.
#                     FIXED-3 and REMAINDER fail here.
#   (2) CANONICAL     the row roles read off the pixels are, row for row, the canon re-derived
#                     from the component's own extent and nothing else. EQUAL and GOLDEN fail
#                     here.
#   (3) SELF-SIMILAR  each measured crest RUN LENGTH is the quarter its own hoop's canon gives
#                     it — measured directly off the pixels as a run, not inferred. FIXED-CREST
#                     fails here, and only here.
#   (4) SCALE-FREE    over the batch, max gauge / min gauge >= 2, where the gauge is the distance
#                     between the first two crest centres. Without it the other three are
#                     satisfiable without ever scaling anything and the claim would be empty.
#
# Clause 2 is the strong one and it implies 1 and 3. They are stated and computed separately
# because each control fails a DIFFERENT one first, and which clause a thing fails is the whole
# diagnostic value of having four.
#
# *** WHAT IS DELIBERATELY NOT A CLAUSE. *** None of this is asked of the finished sheet after
# sprite_finish has run, for the 57th's and 60th's reason: the light comes from outside the
# ornament. The finishing pass adds a visor, pauldron caps and a directional shade, none of which is
# part of the canon.
#
# *** AND CLAUSE 4 IS ASKED OF THE BATCH, WHICH IS THE ONLY PLACE IT CAN BE ASKED. *** A single
# component has one gauge and one gauge has no spread. The claim of this axis is a relation BETWEEN
# pieces, so the evidence for it is necessarily a collection of pieces — which is also the honest
# reason the 24 sheets are generated before the test is run rather than after.
# ---------------------------------------------------------------------------------------------
SCALE_MIN = 2.0


def canon_centres(E, ratio=CANON):
    """Where the canon puts the middle of each hoop, in rows from the component's top."""
    ws = parts(E, ratio)
    out, at = [], 0
    for w in ws:
        out.append(at + w / 2.0)
        at += w
    return out


def accepts_component(runs, rows, E):
    """The clauses on ONE COMPONENT. Returns (ok, failed_clauses, why, gauge).

    ALL failing clauses are reported, not just the first. An earlier draft returned the first and
    the controls table then said things that were true but misleading — EQUAL was recorded as
    failing SELF-SIMILAR because that check happened to run first, when what is actually wrong with
    EQUAL is that its hoops are in the wrong PROPORTION and its crests are only wrong as a
    consequence. A test that reports the first thing it trips over is reporting the order of its own
    source code.
    """
    failed, why = [], []
    want_w = parts(E, CANON)
    want_r, _ = canon_profile(E)
    want_c = [crest_part(w) for w in want_w]
    want_mid = canon_centres(E)

    # (1) PARTITION — one crest per hoop, and the roles cover the extent
    if len(runs) != len(CANON):
        failed.append('PARTITION')
        why.append('%d crest run%s, the canon has %d hoops'
                   % (len(runs), '' if len(runs) == 1 else 's', len(CANON)))
    if len(rows) != E or any(r is None for r in rows):
        failed.append('PARTITION')
        why.append('a row of the extent carries no readable role')

    got_mid = [s + n / 2.0 for s, n in runs]
    got_c = [n for _, n in runs]

    # (2) PLACED — the crest centres are where the canon of 3:2:1 puts them. This clause is a
    # statement about the PROPORTION and nothing else: a crest sits in the middle of its hoop
    # whatever length the crest is, so where the crests are is a measurement of where the hoops
    # are. It is what separates the ratio controls from the axis.
    if len(runs) == len(CANON):
        off = max(abs(a - b) for a, b in zip(got_mid, want_mid))
        if off > 0.5:
            failed.append('PLACED')
            why.append('crest centres %s, the canon of %s puts them at %s (off by %.1f rows)'
                       % (['%g' % v for v in got_mid], want_w,
                          ['%g' % v for v in want_mid], off))

    # (3) SELF-SIMILAR — the crest RUN LENGTHS are the quarter each hoop's own canon gives it.
    # This clause is a statement about the INSIDE of a hoop and nothing else, and FIXED-CREST is
    # the one control that reaches it with the proportion already right.
    if len(runs) == len(CANON) and got_c != want_c:
        failed.append('SELF-SIMILAR')
        why.append('crest runs %s over hoops %s — the hoop canon gives them %s'
                   % (got_c, want_w, want_c))

    # (4) CANONICAL — the umbrella: row for row, the whole painted profile is the canon.
    if len(rows) == E:
        bad = [t for t in range(E) if rows[t] != want_r[t]]
        if bad:
            t = bad[0]
            failed.append('CANONICAL')
            why.append('%d of %d rows off the canon, first at row %d: reads %s, canon puts %s'
                       % (len(bad), E, t, ROLENAME[rows[t]], ROLENAME[want_r[t]]))

    if failed:
        return False, sorted(set(failed)), '; '.join(why), None
    gauge = got_mid[1] - got_mid[0]
    return True, [], ('hoops %s over %d rows, crests %s — a quarter of each'
                      % (want_w, E, got_c)), gauge


def scale_report(gauges):
    """Clause 4, plus the histogram that is the axis's own evidence."""
    lines = []
    if not gauges:
        return False, ['   no component carried the canon — nothing to report']
    lo, hi = min(gauges), max(gauges)
    span = hi / max(lo, 1e-9)
    hist = {}
    for g in gauges:
        hist[g] = hist.get(g, 0) + 1
    lines.append('   gauge (crest centre to crest centre, px): ' +
                 '  '.join('%g:%d' % (k, hist[k]) for k in sorted(hist)))
    lines.append('   min %g  max %g  span x%.2f  (>= %.1f required) -> %s'
                 % (lo, hi, span, SCALE_MIN, 'PASS' if span >= SCALE_MIN else 'FAIL'))
    return span >= SCALE_MIN, lines


# --- sheet machinery --------------------------------------------------------------------------
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


def comps_of(a, largest):
    lbl, n = label4(a)
    if n < 1:
        return []
    if largest:
        counts = np.bincount(lbl.ravel())
        counts[0] = 0
        return [(lbl == int(counts.argmax()))]
    return [(lbl == i) for i in range(1, n + 1)]


def build(base, cfg, cls, ratio=CANON, inner=True, mode=None):
    D, M, L = BODY[cls]
    stops = CANONPAL[cls]
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
        # ONE CANON PER CONNECTED COMPONENT, and on this axis that is not a stylistic choice the way
        # it is on the 54th through 60th — it is forced. The canon divides an EXTENT, and two
        # chausse legs have two extents. Dividing their union would give each leg a fraction of
        # somebody else's proportion, which is precisely the thing the acceptance test is looking
        # for.
        for comp in comps_of(a, largest):
            paint_canon(fr, comp, stops, ratio=ratio, inner=inner, mode=mode)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ------------------------------------------------------------------------------
def _test_plate(w=26, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch."""
    m = np.zeros((h, w), dtype=bool)
    _, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = w * 0.38 - w * 0.18 * abs(ty - 0.55) - w * 0.11 * max(0.0, 0.18 - ty) * 6.0
        m[y, :] = np.abs(xx[y, :] - cx) <= max(hw, 1.5)
    if h >= 10:
        # the neck notch, and only on a plate tall enough to have a neck, and never on ROW 0. Cut
        # at 0:3 it clears the whole top row of a short plate, which shortens the EXTENT — and the
        # extent is the one thing this axis reads, so a diagnostic that let it happen would be
        # measuring its own scenery. The first version of this panel was labelled "10 rows" over a
        # plate that was eight.
        m[1:4, int(cx) - 2:int(cx) + 3] = False
    return m


def _scaled_plate(h):
    """A plate h rows tall. The width floor is 9, not h*0.85: a six-row plate scaled in BOTH
    directions would come out under MIN_PX and be refused as too small to be armour at all, which
    would say something about the pixel budget and nothing about the canon. The canon divides an
    EXTENT, so the diagnostic varies the extent and holds the width where a sabaton's is."""
    w = max(9, int(round(h * 0.85)))
    return _test_plate(w, h)


def _big_comp(arr, fi=0):
    r, c = fi // COLS, fi % COLS
    src = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def canon_report():
    """The canon at every extent the batch can produce, and the five controls beside it."""
    print('== THE CANON  %s   sum %d = the shortest component that can carry it'
          % (' : '.join('%g' % r for r in CANON), MIN_EXTENT))
    print('== THE HOOP   %s   crest is a QUARTER of the hoop at every size'
          % ' : '.join('%g' % r for r in INNER))
    print()
    print('   extent   canon        sums   |  fixed-3        equal      golden     remainder')
    for E in range(MIN_EXTENT, 41):
        w = parts(E, CANON)
        rows = []
        for m in ('fixed-3', 'equal', 'golden', 'remainder'):
            _, ws = control_profile(m, E)
            rows.append(','.join(str(v) for v in ws))
        print('   %-8d %-12s %-6s | %-14s %-10s %-10s %-10s'
              % (E, ','.join(str(v) for v in w), 'ok' if sum(w) == E else 'NO',
                 rows[0] if len(rows[0]) < 14 else rows[0][:11] + '...',
                 rows[1], rows[2], rows[3] + ('' if sum(
                     control_profile('remainder', E)[1]) == E else '  <- %+d'
                     % (sum(control_profile('remainder', E)[1]) - E))))
    bad = [E for E in range(MIN_EXTENT, 200) if sum(control_profile('remainder', E)[1]) != E]
    print()
    print('   REMAINDER control leaves a row over on %d of the %d extents from %d to 199'
          % (len(bad), 200 - MIN_EXTENT, MIN_EXTENT))
    print('   the canon leaves a row over on 0 of them, because its parts are differences of')
    print('   integers and differences of integers sum to the last integer')


def _case_report(comp, stops, ratio=CANON, inner=True, mode=None):
    fr = np.zeros(comp.shape + (4,), dtype=np.uint8)
    info = paint_canon(fr, comp, stops, ratio=ratio, inner=inner, mode=mode)
    if info is None:
        return fr, None, [], True, [], 'too short to carry the canon (reported)', None
    runs, rows, E = read_hoops(fr, comp, stops)
    ok, clauses, why, gauge = accepts_component(runs, rows, E)
    return fr, info, runs, ok, clauses, why, gauge


def dump_cells():
    """ASCII dump of five real components, the clauses on each, then the five controls."""
    legend = {R_CREST: '^', R_FIELD: '-', R_SHADE: 'v', -1: ' '}
    cases = []
    for label, fname in (('warrior chest', 'armor_chest_4.png'),
                         ('mage chest', 'shirt_mage4.png'),
                         ('warrior legs', 'armor_pants_4.png'),
                         ('warrior helm', 'helmet_rare1.png'),
                         ('warrior boot', 'armor_boots_4.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    stops = CANONPAL['warrior']
    allpass = True
    gauges = []
    for label, comp in cases:
        fr, info, runs, ok, clauses, why, gauge = _case_report(comp, stops)
        if info is None:
            print('== %s   %s' % (label, why))
            continue
        pal = np.array(stops, dtype=np.int32)
        role = np.full(comp.shape, -1, dtype=np.int8)
        ys, xs = np.nonzero(comp)
        px = fr[ys, xs, :3].astype(np.int32)
        role[ys, xs] = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
        print('== %s   area=%d  extent=%d rows' % (label, info['area'], info['E']))
        print('   the canon says  hoops %s   crests %s'
              % (info['widths'], [crest_part(w) for w in info['widths']]))
        print('   the pixels say  %d crest run%s at %s'
              % (len(runs), '' if len(runs) == 1 else 's',
                 ', '.join('row %d x%d' % (s, n) for s, n in runs)))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL (%s)' % ', '.join(clauses)))
        allpass = allpass and ok
        if gauge:
            gauges.append(gauge)

    print()
    print('== CLAUSE 5 — SCALE-FREE over the five cases above')
    sok, lines = scale_report(gauges)
    for ln in lines:
        print(ln)
    allpass = allpass and sok

    print()
    print('== THE FIVE CONTROLS, each over the same five cases through the same code path')
    for m in CONTROLS:
        fails, clauses = [], set()
        for label, comp in cases:
            _, info, runs, ok, cl, why, _ = _case_report(comp, stops, mode=m)
            if info is None:
                continue
            if not ok:
                fails.append('%s: %s' % (label, why))
                clauses |= set(cl)
        print('   %-12s fails on %d of %d components, on clause(s): %s'
              % (m, len(fails), len(cases), ', '.join(sorted(clauses)) if clauses else '-'))
        if fails:
            print('       e.g. %s' % fails[0])
        allpass = allpass and bool(fails)
        if not fails:
            print('       DID NOT FAIL - investigate')

    print()
    print('legend: ^ crest   - field   v shade')
    print('ACCEPTANCE (a SIMILARITY, by measurement — not a statistic, a topology, an algebra, a')
    print('conservation law, a physical law, a group action, a census or a formal language):')
    print('(1) PARTITION     exactly %d crest runs, one per hoop, over a fully readable extent;'
          % len(CANON))
    print('(2) PLACED        the crest centres are where the canon of %s puts them;'
          % ' : '.join('%g' % r for r in CANON))
    print('(3) SELF-SIMILAR  each crest RUN is the quarter its own hoop\'s canon of %s gives it;'
          % ' : '.join('%g' % r for r in INNER))
    print('(4) CANONICAL     row for row, the whole profile is the canon (implies 1-3);')
    print('(5) SCALE-FREE    the batch spans at least a factor of %.0f in gauge.' % SCALE_MIN)
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def swatch(path='_diag_canon_swatch.png', zoom=10):
    """The axis drawn: the SAME ornament on plates of five different heights, per class."""
    heights = (6, 10, 15, 22, 30)
    plates = [_scaled_plate(h) for h in heights]
    pad = 4
    cw = max(p.shape[1] for p in plates) * zoom
    ch = max(p.shape[0] for p in plates) * zoom
    img = Image.new('RGBA', (pad + len(plates) * (cw + pad), pad + 3 * (ch + pad)), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        for j, m in enumerate(plates):
            a = np.zeros(m.shape + (4,), dtype=np.uint8)
            paint_canon(a, m, CANONPAL[cls])
            im = Image.fromarray(a).resize((m.shape[1] * zoom, m.shape[0] * zoom), Image.NEAREST)
            img.paste(im, (pad + j * (cw + pad), pad + k * (ch + pad)))
    img.save(path)
    print('wrote %s (hooping only - no sheets written): the same drawing at %s rows'
          % (path, ', '.join(str(h) for h in heights)))


def sweep(path='_diag_canon_sweep.png', zoom=10):
    """A warrior chest and a boot under the axis and under the FIVE CONTROLS.

    EQUAL is the one to look at. Three equal hoops is the 12th axis's banded lamellar; on a
    six-row sabaton it differs from this axis by a single pixel, and that pixel is the axis."""
    cases = [('chest', _big_comp(load_any('armor_chest_4.png'))),
             ('legs', _big_comp(load_any('armor_pants_4.png'))),
             ('boot', _big_comp(load_any('armor_boots_4.png')))]
    cols = [None] + list(CONTROLS)
    stops = CANONPAL['warrior']
    crops = []
    for label, comp in cases:
        ys, xs = np.nonzero(comp)
        sub = comp[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        row = []
        for m in cols:
            a = np.zeros(sub.shape + (4,), dtype=np.uint8)
            paint_canon(a, sub, stops, mode=m)
            row.append(Image.fromarray(a))
        crops.append(row)
    pad = 6
    cw = max(im.width for r in crops for im in r) * zoom
    ch = max(im.height for r in crops for im in r) * zoom
    img = Image.new('RGBA', (pad + len(cols) * (cw + pad), pad + len(crops) * (ch + pad)),
                    (24, 24, 28, 255))
    for i, row in enumerate(crops):
        for j, im in enumerate(row):
            img.paste(im.resize((im.width * zoom, im.height * zoom), Image.NEAREST),
                      (pad + j * (cw + pad), pad + i * (ch + pad)))
    img.save(path)
    print('wrote %s   columns: CANON, %s' % (path, ', '.join(CONTROLS)))


def slots_diag(path='_diag_canon_slots.png', zoom=8):
    """One idle frame of every slot and class, hooped, before the finishing pass."""
    cells = []
    for kind, cfg in SLOTS.items():
        for cls, stem in cfg['srcs'].items():
            base = load_any('%s.png' % stem)
            arr = build(base, cfg, cls)
            cells.append(arr[:FH, :FW])
    pad = 6
    img = Image.new('RGBA', (pad + len(cells) * (FW * zoom // 2 + pad), pad + FH * zoom // 2 + pad),
                    (24, 24, 28, 255))
    for i, c in enumerate(cells):
        im = Image.fromarray(c).resize((FW * zoom // 2, FH * zoom // 2), Image.NEAREST)
        img.paste(im, (pad + i * (FW * zoom // 2 + pad), pad))
    img.save(path)
    print('wrote %s' % path)


def visor_diag(path='_diag_canon_visor.png', zoom=12):
    """The helmet head zone before and after the finishing pass — the visor must survive the
    hooping, which is why no stop in the palette goes near black."""
    cfg = SLOTS['helmet']
    outs = []
    for cls, stem in cfg['srcs'].items():
        base = load_any('%s.png' % stem)
        arr = build(base, cfg, cls)
        raw = arr[16:40, 28:56].copy()
        fin, _ = finish_array(arr.copy(), 'helmet_%s_legendary61.png' % cls)
        outs.append((raw, fin[16:40, 28:56]))
    pad = 6
    h, w = outs[0][0].shape[:2]
    img = Image.new('RGBA', (pad + 2 * len(outs) * (w * zoom + pad), pad + h * zoom + pad),
                    (24, 24, 28, 255))
    for i, (a, b) in enumerate(outs):
        for j, c in enumerate((a, b)):
            im = Image.fromarray(c).resize((w * zoom, h * zoom), Image.NEAREST)
            img.paste(im, (pad + (2 * i + j) * (w * zoom + pad), pad))
    img.save(path)
    print('wrote %s   (raw, finished) x warrior/mage/ranger' % path)


def accept_all():
    """The acceptance test over EVERY component of EVERY active frame of all 24 sheets."""
    ncomp = nhooped = nshort = nfail = 0
    gauges = []
    extents = {}
    byclause = {}
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            stops = CANONPAL[cls]
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                for fi in range(60):
                    r, c = fi // COLS, fi % COLS
                    src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
                    a = src[..., 3] > 0
                    if not a.any():
                        continue
                    fr = np.zeros_like(src)
                    for comp_full in comps_of(a, largest):
                        if comp_full.sum() < MIN_PX:
                            continue
                        ncomp += 1
                        info = paint_canon(fr, comp_full, stops)
                        if info is None:
                            nshort += 1
                            continue
                        runs, rows, E = read_hoops(fr, comp_full, stops)
                        ok, clauses, why, gauge = accepts_component(runs, rows, E)
                        if not ok:
                            nfail += 1
                            for cl in clauses:
                                byclause[cl] = byclause.get(cl, 0) + 1
                            if nfail <= 20:
                                print('   VIOLATION [%s] %s %s%s frame %d: %s'
                                      % (', '.join(clauses), kind, cls, suffix, fi, why))
                            continue
                        nhooped += 1
                        gauges.append(gauge)
                        extents[E] = extents.get(E, 0) + 1
    sok, lines = scale_report(gauges)
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components                 %d' % ncomp)
    print('    carrying the canon       %d' % nhooped)
    print('    shorter than %d rows      %d   (cannot carry six parts; reported, not failed)'
          % (MIN_EXTENT, nshort))
    print('  clause 1-4 violations      %d%s' % (nfail,
          ('   ' + ', '.join('%s:%d' % (k, byclause[k]) for k in sorted(byclause)))
          if byclause else ''))
    print('  distinct extents hooped    %d   (%d .. %d rows)'
          % (len(extents), min(extents) if extents else 0, max(extents) if extents else 0))
    print('  CLAUSE 5 — SCALE-FREE:')
    for ln in lines:
        print(ln)
    allpass = (nfail == 0) and sok
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def main():
    if '--canon' in sys.argv:
        canon_report()
        return
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
