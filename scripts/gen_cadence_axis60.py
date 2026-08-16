#!/usr/bin/env python3
"""SIXTIETH net-new-geometry axis for ALL FOUR SLOTS — the CADENCE family: the piece is ruled edge
to edge with raised reeds of exactly TWO widths, and the ORDER in which the two widths follow one
another is the whole ornament. Nothing else varies. Both widths are the same metal, the same relief,
the same light. There is one kind of element, it comes in two sizes, and everything this axis has to
say is in the sequence.

    the ornament is  CREST  (the lit ridge that opens every reed — one row, always)
                   + FIELD  (the flat of a WIDE reed — one row, and the ONLY thing that
                             distinguishes the two letters: a NARROW reed has no field)
                   + SHADE  (the closing row of every reed, where it turns away from the light)
                   + EDGE   (the quietest tone, on the silhouette of a piece thick enough to have one)

and there is deliberately NO fifth element and no second colour. A wide reed and a narrow reed are
the same object at two lengths. If they were told apart by tincture the word would be readable off
the palette and this would be the 59th; they are told apart by EXTENT and by nothing else.

*** THIS IS THE FIRST AXIS WHOSE DEFINING CONSTANT IS IRRATIONAL. ***
Every one of the fifty-nine before it has a pitch, and every pitch is a whole number of pixels: the
11th flutes every 3, the 40th hangs a tooth every 4, the 51st takes 3.6 and the 46th takes 4.5 and
both of them mean "3.6 pixels of the same thing over and over". A pitch that is a ratio of whole
numbers is a promise that the ornament REPEATS, and all fifty-nine keep it. This one has a pitch of
(1+sqrt5)/2 reeds per wide reed, and there are no two whole numbers in that ratio, so the ornament
cannot repeat — not on a torso, not on a tabard the size of a wall, not ever.

The word the reeds spell is the mechanical word of slope alpha = (sqrt5 - 1)/2:

    s_k = floor((k+1)*alpha) - floor(k*alpha)        s_k = 1 -> NARROW reed (2 rows)
                                                     s_k = 0 -> WIDE   reed (3 rows)
    0 1 0 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 0 1 1 ...

which is the Fibonacci word, and it is not an arbitrary aperiodic sequence. Among all sequences over
two letters that never repeat, it is the one with the FEWEST distinct subwords it is possible to
have: exactly n+1 of each length n. A periodic word runs out of subwords (it can never have more
than its period). A random word has 2^n of them. n+1 is the unique value in between and it is the
signature of an irrational slope. That number is this axis's acceptance test.

*** THE ACCEPTANCE TEST IS A NEW KIND: IT IS A STATEMENT ABOUT A FORMAL LANGUAGE. ***
The 54th is accepted on a TOPOLOGY, the 55th on the ALGEBRA of an order, the 56th on a CONSERVATION
LAW read off a traversal, the 57th on a PHYSICAL LAW, the 58th on a GROUP ACTION, the 59th on a
CENSUS OF A GROUP. This one reads the ornament off the painted pixels AS A WORD — a finite string
over the two letters WIDE and NARROW — collects every such string the batch produces, and asks which
LANGUAGE they all belong to by counting the distinct subwords of each length. No axis in the set has
been accepted on a property of a language before, and nothing weaker will do here, because the thing
being claimed is not about any one piece: it is about what the pieces have in common.

    complexity   the number of distinct length-n subwords over the WHOLE batch is exactly n+1,
                 for every n the batch is long enough to speak about. This is the axis.
    balanced     any two subwords of the same length contain the same number of wide reeds to
                 within one. Equivalently: no two WIDE reeds ever touch, and no three NARROW reeds
                 ever run in a row. Both are visible at a glance, which is the point of choosing a
                 law that has a picture.
    ratio        wide reeds to narrow reeds, over the batch, is the golden ratio.

and the four controls each fail a DIFFERENT clause at a different length, which is what makes the
test a test rather than a formality:

    UNIFORM      one width everywhere. |F(1)| = 1, not 2. This control is not a straw man — it is
                 the 11th FLUTING, exactly, and naming it is how this axis states its own lower
                 collapse boundary: take the second letter away and you are back at axis 11.
    ALTERNATING  slope 1/2, wide-narrow-wide-narrow. |F(2)| = 2, not 3. The rational anyone would
                 reach for first, and the 38th EGG-AND-DART is its ornament.
    RATIONAL     slope 3/5 — a Fibonacci convergent, i.e. the closest a whole-number pitch can come
                 to this axis without being it. It is balanced, it looks almost right, and its
                 subword count saturates: |F(5)| = 5, not 6. THIS is the control the axis exists
                 against, and the only one of the four that a viewer could mistake for a pass.
    RANDOM       letters drawn independently at the correct frequency. |F(2)| = 4, not 3, and two
                 WIDE reeds turn up touching. This is aperiodicity WITHOUT a law, which is to say
                 it is the 46th CRAQUELURE, and it is the axis's upper collapse boundary.

Read the two ends together and the axis is pinned from both sides: rationalise the slope and it
collapses into 11 / 38 / 40; randomise it and it collapses into 46. It lives in the one place that
is neither, and there is exactly one such place per irrational number.

*** WHAT THAT COSTS, AND IT IS THE OPPOSITE OF EVERY PRECEDENT IN THE SET. ***
Nine axes now carry some version of the adaptive-boundary lesson: choose the gauge, the phase, the
pitch PER COMPONENT, from what that component can show. This axis is forbidden to. A word that
re-phased itself to suit each plate would be a DIFFERENT word on each plate, and then there would be
no one word for the pieces to be windows of and no language to test. So the reeds are laid from one
infinite word with no search and no scoring anywhere in this file, and each component takes the
window of it that its own position in the figure selects: a component whose banding coordinate
begins at k shows the word from letter k on. The pieces are attached to the body — the reeds are
anchored to each component's own leading edge, so nothing slides under the walk cycle — and they are
still all quotations from one text. That is the first time in sixty axes that ADAPTATION HAS BEEN
THE ERROR.

*** DISTINCTNESS, and this axis has more near misses than most because stripes are the oldest
ornament there is. Every one of them fails on the ORDER and nothing else. ***
  * The 11th FLUTING and the 43rd GADROON — parallel reeds, and the 43rd is the 11th's relief
    inverted. Both are one width at one pitch. They are the UNIFORM control, and this axis is what
    happens when fluting is given a second reed and a rule about when to use it.
  * The 38th EGG-AND-DART and the 41st BEAD-AND-REEL — two elements alternating, which is the
    obvious way to have two of something. Alternation is a period of two. It is the ALTERNATING
    control.
  * The 40th DENTIL and the 50th RUNIC — ruled registers, and the 50th is the sharpest near miss in
    the whole set for the opposite of the obvious reason. The 50th is the VOCABULARY axis: sixteen
    letters, and no law whatever about the order they come in. This axis has TWO letters and nothing
    at all except a law about the order they come in. They are the same idea taken to its two
    extremes and they look nothing alike.
  * The 46th CRAQUELURE — the aperiodic axis, and the distinction is exact: craquelure is aperiodic
    because it is RANDOM, and randomness is the absence of a law. This is aperiodic BY a law, and a
    strict one. Craquelure has no two cells alike; here there are only two kinds of thing in the
    entire ornament.
  * The 51st FLOWGRAIN — "no repeating unit", because a continuous field bends every ridge into a
    different shape. Nothing is bent here. Every reed is congruent to one of exactly two reeds; what
    fails to repeat is the SEQUENCE, not the shape, and that is a much stronger kind of not
    repeating, because it survives being drawn perfectly.
  * The 55th STRATA — broad bands, but the subject is PRECEDENCE: which band was laid over which.
    These reeds never overlap and there is no order of laying. The subject is which band comes NEXT.
  * The 48th COSMATI — three ranks at 8:5:2, and 8:5 is a convergent of the golden ratio. Cosmati is
    a rational approximation to the number this axis is built out of, applied to scale instead of to
    sequence, and it is periodic exactly because 8, 5 and 2 are whole numbers.
  * The 52nd AJOURE — two periods deliberately kept COPRIME so the liner never phase-locks into a
    coffer. That is a real solution and it is an arithmetic dodge: coprime whole numbers still have a
    common multiple, so ajoure has a period, it is merely a long one. This axis's ratio has no
    denominator, so there is nothing to lock.
  * The 59th COUNTERCHANGE — the immediately preceding axis. Its content is a property of a PAIR
    (element, tincture) and dies if either half is considered alone. This one is blind to tincture by
    construction: both letters are the same metal, and the acceptance test reads WIDTH and never
    colour, exactly as the 59th's reads tincture and never tone.

Geometry, per connected component, in the component's own frame:
    banding    a raked coordinate t = (x + 3y)/sqrt(10) — bands lie across the figure with a shallow
               rake, so they are neither the 11th's verticals nor the 50th's horizontals.
    window     k0 = round(min t over the component). The component shows the infinite word from
               letter k0 on. No search, no scoring, no per-component tuning: see above.
    reeds      cut at t = 0, 0+w0, 0+w0+w1, ... with w_j = 2 if s_{k0+j} else 3, measured from the
               component's own leading edge so the ornament rides with the body.
    relief     row 0 of a reed CREST, last row SHADE, and the middle row of a wide reed FIELD. The
               field row is the letter.
    edge       the silhouette takes the quietest tone, but ONLY on a component with at least
               MARGIN_MIN interior pixels. A four-pixel chausse leg is all boundary, and demoting all
               of it would leave a piece with no reeds on it and no word to read.

Authoring philosophy identical to gen_counterchange_axis59.py / gen_vortice_axis58.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed,
silhouette untouched, so the generator cannot create isolated pixels, background bleed, extra
components or a changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Sixteenth generator to call it in-line, after axes 45-59.

Run from repo root:
  python3 scripts/gen_cadence_axis60.py
  python3 scripts/gen_cadence_axis60.py --word      # the word, its complexity, its three distances
  python3 scripts/gen_cadence_axis60.py --cells     # ASCII dump + the LANGUAGE test + 4 controls
  python3 scripts/gen_cadence_axis60.py --accept    # that test over every component of all 24
  python3 scripts/gen_cadence_axis60.py --swatch    # bare reeding on a test plate, no sheets
  python3 scripts/gen_cadence_axis60.py --sweep     # slots + visor + UNIFORM/ALT/RATIONAL/RANDOM
Then QA (examples):
  python3 scripts/sprite_qa.py _cadence_legendary_preview/shirt_warrior_legendary60.png
  python3 scripts/sprite_qa.py _cadencedome_helmet_preview/helmet_mage_legendary60.png --y-min 2
  python3 scripts/sprite_qa.py _cadence_boots_preview/boots_warrior_legendary_cadence.png --y-max 63
"""
import os
import sys
import math
import bisect
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# Roles. FOUR, and the count is load-bearing: there is no per-letter role anywhere in this table,
# because a role that belonged to one letter would let the eye read the word off the palette.
R_CREST, R_FIELD, R_SHADE, R_EDGE = 0, 1, 2, 3

# The two letters and their reeds. NARROW is the common letter (frequency alpha = 0.618) and WIDE
# the rare one, so a wide reed reads as an ACCENT in a run of narrow ones rather than as a ground
# with stripes on it. WIDE is 3 rows and NARROW 2 because 3:2 is the smallest pair of reed heights
# that can be told apart across a 13-pixel torso after the finishing pass has shaded both of them —
# measured; at 4:3 a warrior chest holds five reeds and a boot holds one.
NARROW, WIDE = 1, 0
WIDTH = {NARROW: 2, WIDE: 3}
LETTER = {NARROW: 'N', WIDE: 'W'}
# The relief of a reed, row by row from its leading edge. The WIDE reed is the NARROW reed with ONE
# ROW OF FIELD INSERTED, which is the entire visible difference between the two letters.
BARROLE = {2: (R_CREST, R_SHADE), 3: (R_CREST, R_FIELD, R_SHADE)}
assert BARROLE[2][0] == BARROLE[3][0] and BARROLE[2][-1] == BARROLE[3][-1], \
    'the two letters must open and close identically, or the width is not what tells them apart'


# --- the word -----------------------------------------------------------------------------------
# alpha = (sqrt5 - 1)/2, the reciprocal of the golden ratio. Its continued fraction is all ones,
# which is the precise sense in which it is the WORST-approximable number there is — the number
# furthest from every rational, and therefore the slope whose word is furthest from every periodic
# one. Choosing it is not decoration; a slope close to a rational produces long stretches that look
# like the RATIONAL control and the axis becomes hard to see on a piece the size of a boot.
ALPHA = (math.sqrt(5.0) - 1.0) / 2.0
PHI = (1.0 + math.sqrt(5.0)) / 2.0


class Word(object):
    """s_k for a mechanical word of slope alpha, or one of the four controls.

    Rational slopes are evaluated in INTEGER arithmetic, not floating point. floor(k*3/5) with 0.6
    as a double lands on the wrong side of an integer for some k, which would perturb the RATIONAL
    control into something that is not periodic — i.e. would hand the control a free pass on the one
    clause it exists to fail.
    """

    def __init__(self, mode='cadence'):
        self.mode = mode
        if mode == 'random':
            rng = np.random.RandomState(60)
            self._r = (rng.random_sample(4096) < ALPHA).astype(np.int8)

    def letter(self, k):
        m = self.mode
        if m == 'uniform':
            return NARROW
        if m == 'random':
            return int(self._r[k % len(self._r)])
        if m == 'alternating':                    # slope 1/2, exactly
            return int((k + 1) // 2 - k // 2)
        if m == 'rational':                       # slope 3/5, exactly
            return int(((k + 1) * 3) // 5 - (k * 3) // 5)
        return int(math.floor((k + 1) * ALPHA) - math.floor(k * ALPHA))

    def run(self, k0, n):
        return [self.letter(k0 + j) for j in range(n)]


WORD = Word('cadence')
CONTROLS = ('uniform', 'alternating', 'rational', 'random')


def bars_for(word, k0, tmax):
    """Cut positions and letters of the reeds covering t in [0, tmax], measured from the
    component's own leading edge. cuts[0] is always 0, so reed j is letters[j] — the alignment the
    read-back below depends on."""
    cuts, letters = [0], []
    j = 0
    while cuts[-1] <= tmax:
        s = word.letter(k0 + j)
        letters.append(s)
        cuts.append(cuts[-1] + WIDTH[s])
        j += 1
    return cuts, letters


def role_table(cuts, letters, n):
    """role of every integer band index 0..n-1."""
    out = np.full(n, R_SHADE, dtype=np.int8)
    for t in range(n):
        j = bisect.bisect_right(cuts, t) - 1
        if j < 0 or j >= len(letters):
            continue
        out[t] = BARROLE[WIDTH[letters[j]]][t - cuts[j]]
    return out


# --- the banding coordinate ---------------------------------------------------------------------
# A shallow rake rather than a square band. (1,3) puts the reeds across the figure at about 18
# degrees off horizontal: enough that they are plainly not the 50th's registers, little enough that
# a 13-pixel torso still fits whole reeds. The SAME direction is used for every slot, so the chest,
# the legs and the boots are ruled by one cadence running down the whole figure.
DIRV = (1, 3)
DIRN = math.hypot(*DIRV)


def t_real(xs, ys, d=DIRV):
    return (xs * d[0] + ys * d[1]) / math.hypot(*d)


# A component with fewer than this many INTERIOR pixels is all boundary. Same constant and the same
# measured reason as the 52nd through 59th — and here it also decides whether the silhouette may be
# demoted at all, because a piece that is all boundary would otherwise come back with no reeds on it
# and no word to read.
MARGIN_MIN = 20
# A component showing fewer complete reeds than this cannot be asked whether it uses both letters —
# a two-reed window of a word in which the rare letter appears 38% of the time is perfectly entitled
# to be NN. Reported, never failed. Three is the shortest window in which BOTH letters are more
# likely than not.
MIN_LETTERS = 3
# The batch-level language test runs to this length. Five is not arbitrary: it is the shortest
# length at which the RATIONAL control (slope 3/5, period 5) is obliged to saturate, and a test that
# stopped at four would pass it.
NMAX = 5


# --- palette ------------------------------------------------------------------------------------
# FOUR stops per class: crest, field, shade, edge. One ramp — no second family anywhere, because the
# two letters must not be distinguishable by colour.
#
# THE HUE PLAN, against the tiers this will sit beside. 54-58 ran through oxblood, pale steel, hide,
# textile and enamel; the 59th took azure / purpure / vert against or and argent. This axis is
# reeded metal and reads best as a burnished ramp with a wide crest-to-shade gap, so the classes are
# separated by TEMPERATURE rather than by hue family:
#   warrior  oxidised BRASS      warm, the brightest crest in the set
#   mage     MOONSTONE           cold blue-white
#   ranger   VERDIGRIS BRONZE    green-gold, kept clear of the warrior by pushing green above red
#
# NO STOP NEAR PURE BLACK: the finishing pass carves the visor as black eye and mouth pixels and a
# near-black darkest stop swallows them (the 49th's lesson). Darkest stops clear channel-sum 150 —
# warrior 218, mage 312, ranger 206.
CADENCE = {
    'warrior': ((238, 212, 146), (182, 154, 94), (128, 104, 58), (96, 78, 44)),
    'mage':    ((238, 242, 252), (178, 188, 216), (120, 130, 166), (88, 96, 128)),
    'ranger':  ((212, 226, 168), (150, 172, 112), (98, 118, 70), (68, 86, 52)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only.
BODY = {
    'warrior': ((96, 78, 44), (182, 154, 94), (238, 212, 146)),
    'mage':    ((88, 96, 128), (178, 188, 216), (238, 242, 252)),
    'ranger':  ((68, 86, 52), (150, 172, 112), (212, 226, 168)),
}

SLOTS = {
    'chest': dict(
        outdir='_cadence_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary60', largest=True,
    ),
    'legs': dict(
        outdir='_cadence_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary60', largest=False,
    ),
    'boots': dict(
        outdir='_cadence_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_cadence', largest=False,
    ),
    'helmet': dict(
        outdir='_cadencedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary60', largest=True,
    ),
}


# --- layout helpers -----------------------------------------------------------------------------
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


# --- painting -----------------------------------------------------------------------------------
def paint_cadence(fr, comp_full, stops, word=WORD, d=DIRV):
    """Paint the reeding onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette.

    There is no search in this function and there is no scoring. That is the axis enforcing itself:
    the moment a phase is chosen to suit a plate, the plate stops being a quotation."""
    if comp_full.sum() < MIN_PX:
        return None
    ys, xs = np.nonzero(comp_full)
    tr = t_real(xs, ys, d)
    tmin = float(tr.min())
    k0 = int(round(tmin))
    T = np.floor(tr - tmin).astype(np.int64)
    n = int(T.max()) + 1
    cuts, letters = bars_for(word, k0, n - 1)
    rt = role_table(cuts, letters, n)
    interior = _interior(comp_full)
    use_edge = int(interior.sum()) >= MARGIN_MIN
    for i in range(len(ys)):
        y, x = int(ys[i]), int(xs[i])
        r = int(rt[T[i]])
        if use_edge and not interior[y, x]:
            r = R_EDGE
        fr[y, x, :3] = stops[r]
        fr[y, x, 3] = 255
    return dict(k0=k0, cuts=cuts, letters=letters, n=n, edged=use_edge,
                shape=comp_full.shape, area=int(comp_full.sum()))


# --- reading the word back off the painted pixels ------------------------------------------------
def read_word(fr, comp_full, stops, info, d=DIRV):
    """Read the reeds off the PAINTED PIXELS and return the word they spell, aligned reed by reed to
    the word the painter was working from.

    This is the counterpart of the 59th's read_tint() and the 58th's hand_of(): the acceptance test
    is run on what is ON THE SHEET. If the silhouette demotion, a neighbouring component's paint, or
    an arithmetic slip in the cut table had put a field row inside a narrow reed, this is where it
    would show up — as a reed three rows wide where the word says two.

    Returns (letters_by_reed, n_unreadable), where letters_by_reed[j] is the letter of reed j or
    None if that reed is clipped by the silhouette or buried under the edge tone.
    """
    ys, xs = np.nonzero(comp_full)
    tr = t_real(xs, ys, d)
    tmin = float(tr.min())
    T = np.floor(tr - tmin).astype(np.int64)
    px = fr[ys, xs, :3].astype(np.int32)
    pal = np.array(stops, dtype=np.int32)
    role = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
    n = int(T.max()) + 1

    # The role of each band index, taken over its non-EDGE pixels. A band that is nothing but
    # silhouette is unreadable and is reported as such rather than guessed at.
    band = [None] * n
    for t in range(n):
        sel = (T == t) & (role != R_EDGE)
        if not sel.any():
            continue
        band[t] = int(np.bincount(role[sel], minlength=4).argmax())

    cuts = info['cuts']
    cut_at = dict((c, j) for j, c in enumerate(cuts[:-1]))
    crests = [t for t in range(n) if band[t] == R_CREST]
    out = [None] * len(info['letters'])
    nbad = 0
    for a, b in zip(crests, crests[1:]):
        j = cut_at.get(a)
        if j is None:                       # a crest where the word puts no reed boundary
            nbad += 1
            continue
        if any(band[t] is None for t in range(a, b)):
            continue                        # clipped or buried: not readable, not a violation
        w = b - a
        if w == 2:
            out[j] = NARROW
        elif w == 3:
            out[j] = WIDE
        else:
            nbad += 1
    return out, nbad


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — a LANGUAGE, by subword complexity.
#
#   (1) QUOTED       every reed whose width can be read off the painted pixels carries the letter
#                    the word puts at that position, and no reed comes out a width the alphabet does
#                    not contain. This is the per-component clause: the piece is a genuine window
#                    onto the word and not merely something striped.
#   (2) BALANCED     over the batch, any two subwords of the same length differ by at most one in
#                    their count of wide reeds. Equivalently and visibly: WW never occurs and NNN
#                    never occurs. The RANDOM control fails here.
#   (3) COMPLEX      over the batch, the number of distinct subwords of length n is exactly n+1, for
#                    every n up to NMAX that the batch is long enough to speak about. This is the
#                    axis. UNIFORM fails at n=1, ALTERNATING at n=2, RATIONAL at n=5.
#   (4) GOLDEN       over the batch, narrow reeds to wide reeds is PHI within tolerance. A word can
#                    be balanced and aperiodic at the wrong frequency; this is what says WHICH
#                    irrational the ornament is built on. Measured on RUN INTERIORS and NOT on every
#                    readable reed — see the note on RATIO_TOL, where asking it of the censored
#                    sample was the one thing this axis got wrong on the first render.
#
# *** WHAT IS DELIBERATELY NOT A CLAUSE. *** Clause 1 is not asked of the finished sheet after
# sprite_finish has run, for the 57th's reason: the light comes from outside the ornament. The
# finishing pass adds a visor, pauldron caps and a directional shade, none of which is part of the
# word. The reader reads WIDTH and is blind to colour by construction, exactly as the 59th's reader
# is blind to tone.
#
# *** AND CLAUSES 2-4 ARE ASKED OF THE BATCH AND NOT OF A PIECE, WHICH IS NOT A WEAKENING. *** A
# five-reed boot cannot exhibit six distinct subwords of length five; demanding that it did would be
# demanding that a quotation contain the book. What the batch can be asked — and this is the whole
# claim — is whether every window any piece anywhere shows is drawn from one language of complexity
# n+1. The 46th's random control and this axis are indistinguishable on any single boot. They are
# not remotely confusable over 24 sheets, and that is the correct place to look.
# ---------------------------------------------------------------------------------------------
# *** CLAUSE 4 IS NOT ASKED OF THE SAME SAMPLE AS CLAUSES 2-3, AND THE FIRST DRAFT HAD THAT WRONG.
# It read the frequency off every reed it could READ, and came back 1.7519 against phi = 1.6180 — a
# FAIL, on a batch whose ornament is in fact golden. The defect was in the estimator, not the
# armour. A reed is dropped as unreadable when the silhouette clips any of its rows, and a WIDE reed
# is three rows where a NARROW reed is two, so a wide reed is systematically likelier to be clipped.
# The readable sample is therefore censored by an event whose probability depends on the very
# quantity being estimated — length-biased sampling, and the bias is toward the narrow letter by
# construction. Measured over this batch (`scripts/_diag_cadence_ratio.py`):
#
#     readable reeds          narrow 2062 / wide 1177 = 1.7519    err +0.1339   <- the silhouette
#     reeds INTERIOR to a run narrow  813 / wide  504 = 1.6131    err -0.0049   <- the ornament
#     the word AS PLACED      narrow 3182 / wide 1947 = 1.6343    err +0.0163   <- ground truth
#
# The fix is not a wider tolerance — that is tuning a test until it passes. It is to ask clause 4 of
# a sample the censoring cannot bias: the reeds INTERIOR to a maximal run of readable reeds. Such a
# reed was admitted because its NEIGHBOURS were readable, not because of its own width, and the
# estimator then agrees with the uncensored ground truth to 0.005. Clauses 2-3 stay on the full runs,
# which have five times the windows and are unaffected by the bias because complexity counts DISTINCT
# subwords and is blind to how often each turns up.
#
# Because the estimator is now 25x more accurate the tolerance is tightened from 0.12 to 0.05 — which
# STRENGTHENS the test in the one place it matters: the RATIONAL control, slope 3/5, has frequency
# 3/2 = 1.5, err 0.118, and now fails clause 4 as well as clause 3. The nearest rational to this
# axis is excluded on frequency AND on complexity instead of on complexity alone.
RATIO_TOL = 0.05
RATIO_MIN = 200          # interior reeds needed before clause 4 is asserted rather than reported


def runs_of(read):
    """Split a per-reed read-back into MAXIMAL CONTIGUOUS runs of readable reeds.

    The first draft flattened `read` with `[v for v in read if v is not None]`, which SPLICES the
    reeds either side of an unreadable one into a single string. On this batch the gaps are terminal
    and the two agree exactly, so nothing was wrong on the sheets — but a gap in the middle of a
    component would have manufactured an adjacency that is not in the word, and clause 3 would have
    counted the spliced pair as a legitimate subword and accepted it. A window onto a text is a
    CONTIGUOUS piece of it; two fragments are two windows.
    """
    out, cur = [], []
    for v in read:
        if v is None:
            if cur:
                out.append(cur)
            cur = []
        else:
            cur.append(v)
    if cur:
        out.append(cur)
    return out


def interiors_of(runs):
    """The reeds of each run that have a readable neighbour on BOTH sides — the unbiased sample."""
    return [r[1:-1] for r in runs if len(r) > 2]


def factors(words, n):
    s = set()
    for w in words:
        for i in range(len(w) - n + 1):
            s.add(tuple(w[i:i + n]))
    return s


def runs_ok(words):
    """WW never occurs and NNN never occurs — the visible face of balance."""
    bad = []
    for w in words:
        for i in range(len(w) - 1):
            if w[i] == WIDE and w[i + 1] == WIDE:
                bad.append('WW')
        for i in range(len(w) - 2):
            if w[i] == w[i + 1] == w[i + 2] == NARROW:
                bad.append('NNN')
    return bad


def balanced(words, n):
    f = factors(words, n)
    if not f:
        return True, 0
    counts = [sum(1 for c in u if c == WIDE) for u in f]
    return (max(counts) - min(counts)) <= 1, max(counts) - min(counts)


def language_report(words, interiors=None, nmax=NMAX, min_obs=40):
    """Clauses 2-4. Returns (ok, lines).

    `words` are the maximal readable runs and carry clauses 2-3. `interiors` is the censoring-free
    sample that carries clause 4 (see the note on RATIO_TOL); when it is not supplied or is too
    small to speak with, the frequency is REPORTED off `words` and not asserted.
    """
    lines = []
    ok = True
    rat = interiors if interiors is not None else words
    flat = [c for w in rat for c in w]
    nn = sum(1 for c in flat if c == NARROW)
    nw = len(flat) - nn
    for n in range(1, nmax + 1):
        obs = sum(max(0, len(w) - n + 1) for w in words)
        f = factors(words, n)
        bal, spread = balanced(words, n)
        verdict = 'n+1'
        if obs < min_obs:
            verdict = 'too few windows of this length to speak about (reported, not asserted)'
        elif len(f) != n + 1:
            verdict = 'EXPECTED %d' % (n + 1)
            ok = False
        if not bal:
            verdict += '  UNBALANCED spread=%d' % spread
            ok = False
        lines.append('   length %d: %-4d windows, %d distinct subwords  -> %s'
                     % (n, obs, len(f), verdict))
    bad = runs_ok(words)
    lines.append('   forbidden subwords WW / NNN: %d occurrences -> %s'
                 % (len(bad), 'PASS' if not bad else 'FAIL'))
    ok = ok and not bad
    ratio = nn / float(max(nw, 1))
    good = abs(ratio - PHI) <= RATIO_TOL
    src = 'run interiors' if interiors is not None else 'readable reeds, CENSORED'
    if nn + nw < RATIO_MIN or interiors is None:
        lines.append('   narrow %d / wide %d = %.4f   phi = %.4f  (%s; too small a sample to '
                     'assert — reported, not asserted)' % (nn, nw, ratio, PHI, src))
    else:
        lines.append('   narrow %d / wide %d = %.4f   phi = %.4f  (%s, tolerance %.2f) -> %s'
                     % (nn, nw, ratio, PHI, src, RATIO_TOL, 'PASS' if good else 'FAIL'))
        ok = ok and good
    return ok, lines


def accepts_component(read, info):
    """Clause 1 on ONE COMPONENT."""
    letters = info['letters']
    nread = sum(1 for v in read if v is not None)
    for j, v in enumerate(read):
        if v is None:
            continue
        if v != letters[j]:
            return False, ('reed %d comes off the pixels %s but the word puts %s there'
                           % (j, LETTER[v], LETTER[letters[j]])), nread
    if nread == 0:
        return True, 'no complete reed on this component (too small to quote; reported)', 0
    return True, ('%d complete reed%s, every one the letter the word puts there'
                  % (nread, '' if nread == 1 else 's')), nread


# --- sheet machinery ----------------------------------------------------------------------------
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


def build(base, cfg, cls, word=WORD):
    D, M, L = BODY[cls]
    stops = CADENCE[cls]
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
        # ONE WINDOW PER CONNECTED COMPONENT. Reeds are a property of a PLATE; running one cut table
        # across two chausse legs at once asserts a continuity the viewer cannot use — the 54th's
        # lesson, the 57th's, the 58th's, the 59th's. Here it is also what keeps the language test
        # honest, since a word is read along one connected body.
        for comp in comps_of(a, largest):
            paint_cadence(fr, comp, stops, word=word)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics --------------------------------------------------------------------------------
def _test_plate(w=44, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the
    reeding can be judged on a shape with the features the real slots have."""
    m = np.zeros((h, w), dtype=bool)
    _, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        m[y, :] = np.abs(xx[y, :] - cx) <= max(hw, 1.5)
    m[0:3, int(cx) - 2:int(cx) + 3] = False
    return m


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


def swatch(path='_diag_cadence_swatch.png', zoom=12):
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_cadence(a, m, CADENCE[cls])
        img.paste(Image.fromarray(a).resize((tw, th), Image.NEAREST), (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (reeding only - no sheets written)' % path)


def sweep(path='_diag_cadence_sweep.png', zoom=11):
    """Warrior chest and leg idle frames under the axis and under the FOUR CONTROLS.

    RATIONAL is the one to look at. It is slope 3/5 — a Fibonacci convergent, the nearest a
    whole-number pitch gets to this axis — and on a single plate it is nearly indistinguishable.
    That is the honest situation and it is why the acceptance test counts subwords over a batch
    instead of looking at a torso."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    variants = [('CADENCE', 'cadence'), ('UNIFORM', 'uniform'),
                ('ALTERNATING', 'alternating'), ('RATIONAL 3/5', 'rational'),
                ('RANDOM', 'random')]
    cells = []
    for name, mode in variants:
        wd = Word(mode)
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            comp = _big_comp(arr)
            fr = np.zeros_like(arr[0:FH, 0:FW])
            paint_cadence(fr, comp, CADENCE['warrior'], word=wd)
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
    print('wrote %s (axis + UNIFORM/ALTERNATING/RATIONAL/RANDOM controls - no sheets written)'
          % path)


def slots_diag(path='_diag_cadence_slots.png', zoom=10):
    """All three classes x all four slots, bare reeding, no finishing pass."""
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
            for comp in comps_of(a, largest):
                paint_cadence(fr, comp, CADENCE[cls])
            cell = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
            x, y = pad + ci * (cw + pad), pad + ri * (chh + lab)
            img.alpha_composite(cell, (x, y))
            d.text((x + 2, y + chh), '%s %s' % (cls, kind), font=f, fill=(210, 210, 220, 255))
    img.convert('RGB').save(path)
    print('wrote %s (all classes x all slots, bare reeding)' % path)


def visor_diag(path='_diag_cadence_visor.png', zoom=14):
    """The warrior dome's black eye and mouth slits reading through the reeding, m and f.

    Built with build() on the WHOLE SHEET, never on a lone frame: the 58th paid twice for handing
    finish_array a 70-frame array with one frame in it, and it is written down there, in the 59th,
    and here."""
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
    print('wrote %s (visor slits reading through the reeding)' % path)


def word_report():
    """The word itself, before any armour: what it is, what it is not, and the three distances."""
    w = WORD.run(0, 72)
    print('== THE WORD, slope alpha = (sqrt5-1)/2 = %.12f' % ALPHA)
    print('   ' + ''.join(LETTER[c] for c in w))
    print('   N narrow reed (2 rows, frequency alpha)   W wide reed (3 rows, frequency 1-alpha)')
    print('== SUBWORD COMPLEXITY of the first 4000 letters — the number this axis is built on')
    long = [WORD.run(0, 4000)]
    for n in range(1, 9):
        f = sorted(factors(long, n))
        show = ' '.join(''.join(LETTER[c] for c in u) for u in f) if n <= 4 else ''
        print('   length %d: %d distinct  (n+1 = %d)  %s' % (n, len(f), n + 1, show))
    print('== THE SAME COUNT FOR EACH CONTROL — every one fails at a different length')
    for m in CONTROLS:
        wd = Word(m)
        seq = [wd.run(0, 4000)]
        row = ', '.join('|F(%d)|=%d' % (n, len(factors(seq, n))) for n in range(1, NMAX + 1))
        first = next((n for n in range(1, NMAX + 1) if len(factors(seq, n)) != n + 1), None)
        print('   %-12s %s   -> first departure at length %s' % (m, row, first))
    print('== THREE-DISTANCE: the gaps between consecutive WIDE reeds take at most three values')
    pos = [i for i, c in enumerate(WORD.run(0, 4000)) if c == WIDE]
    gaps = sorted(set(b - a for a, b in zip(pos, pos[1:])))
    print('   gaps observed: %s  (%d distinct)' % (gaps, len(gaps)))
    flat = WORD.run(0, 4000)
    nn = flat.count(NARROW)
    print('== FREQUENCY: narrow %d / wide %d = %.6f, phi = %.6f'
          % (nn, 4000 - nn, nn / float(4000 - nn), PHI))


def _case_report(comp, stops, word=WORD):
    fr = np.zeros((comp.shape[0], comp.shape[1], 4), dtype=np.uint8)
    info = paint_cadence(fr, comp, stops, word=word)
    read, nbad = read_word(fr, comp, stops, info)
    ok, why, nread = accepts_component(read, info)
    if nbad:
        ok = False
        why = '%d reed(s) came off the pixels at a width the alphabet does not contain' % nbad
    return fr, info, read, ok, why, nread


def dump_cells():
    legend = {R_CREST: '^', R_FIELD: '=', R_SHADE: 'v', R_EDGE: '.'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    print('== THE ALPHABET: one element at two lengths, opening and closing identically')
    for s in (NARROW, WIDE):
        print('   %-6s %d rows  %s' % (LETTER[s], WIDTH[s],
                                       ' '.join({R_CREST: 'CREST', R_FIELD: 'FIELD',
                                                 R_SHADE: 'SHADE'}[r]
                                                for r in BARROLE[WIDTH[s]])))
    print('   the WIDE reed is the NARROW reed with one FIELD row inserted, and that is the only')
    print('   difference between the two letters anywhere in this file')

    allpass = True
    words = []
    stops = CADENCE['warrior']
    for label, comp in cases:
        fr, info, read, ok, why, nread = _case_report(comp, stops)
        pal = np.array(stops, dtype=np.int32)
        role = np.full(comp.shape, -1, dtype=np.int8)
        ys, xs = np.nonzero(comp)
        px = fr[ys, xs, :3].astype(np.int32)
        role[ys, xs] = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
        pred = ''.join(LETTER[c] for c in info['letters'])
        got = ''.join(LETTER[c] if c is not None else '-' for c in read)
        print('== %s   area=%d  window starts at letter k0=%d  %d bands'
              % (label, info['area'], info['k0'], info['n']))
        print('   word says   %s' % pred)
        print('   pixels say  %s        (- = reed clipped by the silhouette, not readable)' % got)
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL'))
        allpass = allpass and ok
        words.extend(runs_of(read))

    print('== CLAUSES 2-4 over the words the five cases above spell')
    lok, lines = language_report(words, interiors=interiors_of(words), min_obs=8)
    for ln in lines:
        print(ln)
    allpass = allpass and lok

    print('== THE CONTROLS, each run over the same five cases through the same code path')
    print('   (each is reported at the length where it first departs from n+1 — they are all')
    print('    different lengths, which is what makes the test discriminating rather than a')
    print('    formality)')
    for m in CONTROLS:
        wd = Word(m)
        cw = []
        for _, comp in cases:
            _, info, read, _, _, _ = _case_report(comp, stops, word=wd)
            cw.extend(runs_of(read))
        seq = [wd.run(0, 4000)]
        first = next((n for n in range(1, NMAX + 1) if len(factors(seq, n)) != n + 1), None)
        bad = runs_ok(cw)
        print('   %-12s on the armour: %s' % (m, ', '.join(
            '|F(%d)|=%d' % (n, len(factors(cw, n))) for n in range(1, 4))))
        print('   %-12s in the limit : first departure from n+1 at length %s%s  -> %s'
              % ('', first, ('; %d forbidden subwords' % len(bad)) if bad else '',
                 'PASS (correctly fails the axis)' if first is not None or bad
                 else 'DID NOT FAIL - investigate'))
        allpass = allpass and (first is not None or bool(bad))

    print('legend: ^ crest  = field (a WIDE reed only)  v shade  . silhouette')
    print('ACCEPTANCE (a LANGUAGE, by subword complexity — not a statistic, a topology, an algebra,')
    print('a conservation law, a physical law, a group action or a census of a group):')
    print('(1) QUOTED    every readable reed carries the letter the word puts at that position;')
    print('(2) BALANCED  WW never occurs, NNN never occurs, subwords of a length differ by <= 1;')
    print('(3) COMPLEX   exactly n+1 distinct subwords of length n — aperiodic, and minimally so;')
    print('(4) GOLDEN    narrow to wide is phi within %.2f, measured on RUN INTERIORS — a reed the'
          % RATIO_TOL)
    print('              silhouette clipped is dropped, and a wide reed is 3 rows where a narrow is')
    print('              2, so the readable sample is censored toward narrow and cannot be used.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def accept_all():
    """The acceptance test over EVERY component of EVERY active frame of all 24 sheets."""
    ncomp = nquote = nfail = nshort = 0
    words = []
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            stops = CADENCE[cls]
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
                        info = paint_cadence(fr, comp_full, stops)
                        read, nbad = read_word(fr, comp_full, stops, info)
                        ok, why, nread = accepts_component(read, info)
                        ncomp += 1
                        if nbad:
                            ok, why = False, ('%d reed(s) at a width the alphabet does not '
                                              'contain' % nbad)
                        if not ok:
                            nfail += 1
                            print('   VIOLATION %s %s%s frame %d: %s'
                                  % (kind, cls, suffix, fi, why))
                            continue
                        if nread >= MIN_LETTERS:
                            nquote += 1
                        else:
                            nshort += 1
                        words.extend(runs_of(read))
    ok, lines = language_report(words, interiors=interiors_of(words))
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components                 %d' % ncomp)
    print('    quoting >= %d reeds       %d' % (MIN_LETTERS, nquote))
    print('    shorter windows          %d   (too small to be asked clause 3; reported, not failed)'
          % nshort)
    print('  letters read off pixels    %d' % sum(len(w) for w in words))
    print('  clause 1 violations        %d' % nfail)
    print('  THE LANGUAGE (clauses 2-4), over every window the batch shows:')
    for ln in lines:
        print(ln)
    allpass = ok and nfail == 0
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def main():
    if '--word' in sys.argv:
        word_report()
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
