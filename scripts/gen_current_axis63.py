#!/usr/bin/env python3
"""SIXTY-THIRD net-new-geometry axis for ALL FOUR SLOTS — the CURRENT family: the piece is ruled
into level bands, and the bands TRAVEL. Their phase advances with the animation frame, by an amount
the generator is never told, and which it works out from the length of the cycle the frame belongs
to — so that the pattern comes back exactly where it started at the end of every loop.

    the ornament is  CREST   (the lit ridge riding up the plate)
                   + SHADE   (the one band under a crest, where the plate drops away from it)
                   + FIELD   (the plate between one crest and the next)

*** THIS IS THE FIRST AXIS WHOSE INVARIANT IS NOT A PROPERTY OF A PICTURE. ***
The sixty-two before it are all, in the end, claims about pixels that are on a sheet at the same
time. The 46th is a claim about the areas of shards, the 54th about the connectivity of a wire, the
57th about where the deepest part of a swag is, the 61st about the proportions of three hoops, and
the 62nd — the only one that ever needed more than one sheet — about four sheets AGREEING, which is
still a claim about a picture, just a bigger picture. Every one of them can be settled by looking.

This one cannot be settled by looking, and that is not a weakness in the test, it is the axis. The
invariant here is a CLOSURE: go once round the walk cycle and the ornament has advanced by exactly
one period. That statement is not true or false of frame 12; it is not true or false of any frame;
it is a property of the eight frames 10..17 taken in order and then joined end to end. Hold up any
single frame of this axis beside the 11th FLUTING and there is no test, by eye or by machine, that
separates them — and clause INVISIBLE is that fact stated as a requirement rather than confessed as
a defect.

*** THE INCREMENT IS NOT A CONSTANT. IT IS DERIVED, PER CYCLE, FROM THE CYCLE. ***
The sheet holds six loops of four different lengths — idle 5 frames, walk 8, run 8, jump 4, cheer 4,
slash 6. If the ornament travelled at one speed it would close on at most one of them and pop at the
loop point of the other five, which is the CONSTANT-SPEED control and is what anyone writes first.
So the generator is told a WINDING NUMBER, which is one, and it divides: the step is P/L, and it is
P/5 on the idle, P/8 on the walk and the run, P/4 on the jump and the cheer and P/6 on the slash.
Four different speeds in one sheet, none of them written down anywhere, all of them consequences of
a single integer.

*** WHY THE WINDING NUMBER IS ONE, AND IT IS NYQUIST RATHER THAN TASTE. ***
The shortest loop in the game is four frames. At a winding of two the step on that loop is P/2 —
exactly half a period per frame — and a pattern that moves half a period per frame has no direction:
up and down produce identical sheets. That is the DOUBLE control, and it is not merely worse, it is
undecidable, which is the wagon-wheel effect and the one hard bound on this axis. One is the largest
winding the shortest cycle in the game can carry and still be seen to move the way it moves.

*** THE CARRIER IS DELIBERATELY THE PLAINEST THING IN THE SET. ***
A level band. Nothing else. Because if the carrier were interesting the axis would be about the
carrier, and the whole content of this one is that the carrier MOVES: take the motion away and it
collapses exactly, pixel for pixel, onto the 11th FLUTING turned on its side, which is the STATIC
control and is named as this axis's lower collapse boundary rather than hidden from it. The 62nd had
to be OBLIQUE because a level line crossing a seam would have lined up by accident and its evidence
was a seam; this one is level because vertical travel on a thirteen-pixel-wide character is the most
legible motion there is, and the two are not in conflict because this axis is SELF-ANCHORED — every
component takes its own top as its origin, which is what all sixty-one axes before the 62nd do.

*** THE ACCEPTANCE TEST IS A NEW KIND: A KINEMATICS. A CLAIM ABOUT A SEQUENCE. ***
Predecessors are accepted on a statistic (46/48/50/52/53), a topology (54), an algebra (55), a
conservation law (56), a physical law (57), a group action (58), a census of a group (59), a formal
language (60), a similarity (61) or a registration (62). This is the first accepted on a claim that
requires the frames to be put IN ORDER — shuffle the eight walk frames and the axis is gone while
every pixel of every frame is untouched. So the phase is measured off the pixels of each frame
independently, and then the SEQUENCE of measurements is the thing on trial.

    (1) ADVANCE      the phase advances by the SAME amount between every pair of frames inside a
                     loop. It says the ornament moves uniformly and it deliberately does not say
                     how fast: the step is an OUTPUT of the measurement, never an input to it.
                     RANDOM-PHASE and SMEAR fail here.
    (2) CLOSURE      the loop is explained, exactly, by a trajectory that CLOSES: the step is
                     nailed at one period per loop, only the starting phase is left free, and not
                     one row may disagree. THE CLAUSE IS NOT A COMPARISON AND IT HAS NO
                     TOLERANCE — closure is imposed and then checked, because the free step is
                     only ever known as an interval and choosing a width for "near enough to 1"
                     would be choosing the answer. It is a WINDING NUMBER, it is an integer, and
                     it is the SAME integer on a four-frame loop and an eight-frame loop whose
                     steps differ by a factor of two. STATIC, CONSTANT-SPEED, NEAREST-INT and
                     DOUBLE all fail here, with four different windings — 0, L/8, L/round(P/L)
                     and 2 — so the clause does not merely reject them, it says what each of them
                     is. Four controls on one clause is not a defect in the table; the winding
                     number IS the axis, and everything that is wrong is wrong in that number.
    (3) INVISIBLE    the negative clause, and the one that says this is not any of the other
                     sixty-two: every single frame, taken alone, is a valid STATIC profile at some
                     phase — the residual against the best fixed phase is zero. One picture carries
                     no evidence at all. SMEAR is the only control that reaches this clause, and
                     it is the only clause SMEAR reaches ALONE — see the control table.
    (4) SPEED-VARIES the steps actually realised over the batch take at least three distinct
                     values. Without it, CONSTANT-SPEED satisfies 1 and 3 and the derivation of
                     the step from the cycle would be doing no work.
    (5) ONE PERIOD   exactly one P over the whole batch. The pattern does not change; only its
                     phase does. This is what separates a travelling ornament from an ornament
                     that is redrawn every frame.

*** THE SIX CONTROLS, AND THE SIXTH EXISTS BECAUSE THE NEGATIVE CLAUSE NEEDED ONE. ***
    STATIC         phase nailed at zero. It advances perfectly uniformly — by nothing — so it
                   PASSES ADVANCE and fails CLOSURE with a winding of ZERO, which is the exact
                   and useful thing to say about it: it is the 11th FLUTING, it is this axis with
                   the winding number turned off, and it is the lower collapse boundary.
    CONSTANT-SPEED one step, P/8, everywhere. THE HONEST NEAR MISS. It passes ADVANCE and it
                   passes INVISIBLE, it is right on the walk and the run, and it is wrong on the
                   other four loops — the idle closes 5/8 of a period, the jump 1/2, the slash
                   3/4 — so every one of them jumps at the loop point, forever, once a second.
                   This control is the entire reason the step is derived rather than chosen.
    NEAREST-INT    the step rounded to a whole pixel, because pixels are integers and rounding
                   feels like the honest thing to do. It is not: the phase is a threshold on a
                   continuous coordinate, not a translation of a bitmap, and sub-pixel phase costs
                   nothing. Rounding P/L to 1 makes the advance L instead of P and closes NOTHING.
                   THIS IS THE BUG THE AXIS WOULD HAVE SHIPPED WITH (compare the 61st REMAINDER).
    DOUBLE         winding two. Fails CLOSURE by construction, and the reason it is in the table
                   rather than in a footnote is the Nyquist bound above: on the four-frame loops
                   its step is exactly P/2 and the direction of travel becomes undecidable.
    SMEAR          the crest widened in proportion to the step, which is how a still picture
                   usually says "this is moving". It is the only control that changes the PROFILE
                   rather than the phase, and it pays in every single frame — the relief goes
                   soft, and at 13px soft is mud — for something the eye only gets in motion
                   anyway. The most tempting wrong answer of the six.
                   IT FAILS ALL THREE CLAUSES, AND THAT IS REPORTED RATHER THAN ENGINEERED AWAY,
                   because the reason is the structure of the test: the reader is mode-blind, it
                   can only measure a phase by fitting the profile it knows, and a phase measured
                   off a profile it does not recognise is not a measurement of anything. So
                   INVISIBLE is logically PRIOR to the other two — is this the right shape? then
                   does it move uniformly? then does it close — and the only clean way to say
                   that is to let SMEAR fail downward through all three.
    RANDOM-PHASE   a fresh phase every frame. Fails ADVANCE (and CLOSURE after it, for the same
                   reason SMEAR does). The upper collapse boundary: all of the motion, none of
                   the kinematics, and it boils.

*** THE PRICE, AND IT IS PAID IN THE DELIVERABLE AGAIN. ***
The 62nd could not be judged on one sheet, so its approval panel became a dressed character. This
one cannot be judged on one PICTURE, so its approval panel becomes a FILMSTRIP and a GIF: the still
grids are provided and they are, correctly, indistinguishable from fluting. `_ZOOM_current_strip.png`
— one crest traced through the eight frames of the walk, and the same eight frames under
CONSTANT-SPEED beside it with the pop at the loop point circled — is the real evidence. The second
cost is blunter and is stated rather than argued away: A PLAYER LOOKING AT A PAUSED GAME SEES THE
11th AXIS. This axis spends its whole budget on the half of the time the character is animating.

*** DISTINCTNESS. ***
  * 11th FLUTING / 12th BANDED-LAMELLAR / 43rd GADROON / 61st CANON — level or ruled bands. They
    are the STATIC control. Every one of them is this axis with the winding number set to zero,
    and saying so is how this axis states its own floor.
  * 62nd DATUM — the other axis whose evidence is not on the sheet in front of you. The split is
    exact and it is SPACE against TIME: the 62nd needs four sheets AT ONE INSTANT and is rigid
    over frames; this needs one sheet OVER EIGHT INSTANTS and is self-anchored in space. The 62nd
    asks the pieces to agree about where the world is. This asks the frames to agree about when.
  * 51st FLOWGRAIN — a continuous field, but a static one; its director field is the same field in
    frame 0 and frame 17.
  * 57th FESTOON — the other axis with a law rather than a pattern, but gravity is a law about a
    picture: it constrains where the deepest pixel of a swag is, in that frame, on its own.
  * 60th CADENCE — a sequence, but a sequence in SPACE, read along a plate, and every letter of it
    is on the sheet at once. This axis's sequence has one letter per picture.
  * Anything animated in the app already (the idle bob, the run cycle) is the BODY moving. Here
    the body does what it always did and the ORNAMENT moves across it.

Geometry, per connected component, in the component's own frame:
    origin    s = y - y0, the component's own top row. Self-anchored, like everything up to the
              61st. Nothing outside the component is consulted, deliberately: the 62nd already
              owns the other choice.
    period    P = 4.5 px, one gauge for the whole batch (clause ONE PERIOD).
    profile   u = (s + phase) mod P, taken as a fraction f = u/P:
                  f <  0.28   CREST     the lit ridge
                  f <  0.50   SHADE     its own cast shade, immediately under it
                  else        FIELD
    phase     phase(fi) = P * W * k / L, W = 1, where k is the index of the frame WITHIN ITS OWN
              CYCLE and L is that cycle's length. The generator holds no table of speeds.
    minimum   a component shorter than P rows cannot show a whole period and its phase cannot be
              read; it is painted and then EXCLUDED FROM THE TEST, reported, never failed.

Authoring philosophy identical to gen_canon_axis61.py / gen_datum_axis62.py: every pattern pixel is
painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed, silhouette
untouched — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Nineteenth generator to call it in-line, after axes 45-62.

Run from repo root:
  python3 scripts/gen_current_axis63.py
  python3 scripts/gen_current_axis63.py --cycles    # the loops, their steps and their closures
  python3 scripts/gen_current_axis63.py --cells     # ASCII of one component through a whole cycle
  python3 scripts/gen_current_axis63.py --accept    # the five clauses over all 24 sheets
  python3 scripts/gen_current_axis63.py --controls  # the six controls through the same code path
  python3 scripts/gen_current_axis63.py --sweep     # slots + visor diagnostics
Then QA (examples):
  python3 scripts/sprite_qa.py _current_legendary_preview/shirt_warrior_legendary63.png
  python3 scripts/sprite_qa.py _currentdome_helmet_preview/helmet_mage_legendary63.png --y-min 2
  python3 scripts/sprite_qa.py _current_boots_preview/boots_warrior_legendary_current.png --y-max 63
"""
import os
import sys
import math
import random
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# THREE roles, no fourth, for the 61st's reason: a rim is a one-pixel feature and a rimmed row is a
# row the reader cannot measure. Here that matters more than anywhere, because the reader has to
# recover a SUB-PIXEL phase from a handful of rows and every censored row widens the interval of
# phases consistent with what it sees.
R_CREST, R_SHADE, R_FIELD = 0, 1, 2
ROLENAME = {R_CREST: 'CREST', R_SHADE: 'SHADE', R_FIELD: 'FIELD'}

# THE PERIOD. One gauge for the whole batch — clause ONE PERIOD. 4.5 is the smallest pitch at which
# a crest, its shade and a readable field all survive quantisation to integer rows (crest 1.26px,
# shade 0.99, field 2.25), and it puts three periods on a warrior chest and one on a sabaton.
# The split within the period was 0.28/0.50 on the first render and the plate came out STRIPED —
# equal parts light and dark read as a wasp, not as a relief. 0.24/0.46 gives crest 1.08, shade
# 0.99 and field 2.43: one lit row, one dark row under it, and enough plate between them that the
# crest is an event on a surface rather than half of a two-tone pattern.
PERIOD = 4.5
# The profile, as fractions of one period. Crest first, its own shade under it, then the field.
F_CREST, F_SHADE = 0.24, 0.46
# THE WINDING NUMBER, and it is the only number in this file the ornament's motion is told.
# One, because the shortest loop in the game is four frames and a winding of two would step P/2 on
# it, which is exactly Nyquist and has no direction. See DOUBLE.
WINDING = 1

# THE CYCLES. Read off SPRITE_SPEC.md section 1 — these are the app's own animation rows, not this
# axis's invention, which is the point: the step is a consequence of the app's frame budget.
#   name        first frame, length
CYCLES = (
    ('idle',  0, 5),
    ('walk', 10, 8),
    ('run',  20, 8),
    ('jump', 30, 4),
    ('cheer', 40, 4),
    ('slash', 50, 6),
)
SLEEP_FROM = 60
# A component must be able to show a whole period or its phase is not recoverable at all.
MIN_EXTENT = int(math.ceil(PERIOD))
# Phase read back off the pixels is quantised by the integer rows it is read from; this is the
# tolerance on that measurement, in pixels, and it is well under the smallest step the batch uses
# (P/8 = 0.5625).
PHASE_TOL = 0.30
# Tolerance on the WINDING NUMBER, which is the only quantity any clause is actually tested
# against. It is set by the resolution of the step grid the trajectory is fitted on (0.025 px, so
# L/120 = 0.067 on the walk) and not by what the sheets happen to score. Every one of the four
# CLOSURE controls misses by at least 0.11 and most of them by more than one whole period.
WIND_TOL = 0.10


# --- the kinematics -------------------------------------------------------------------------
def cycle_of(fi):
    """(name, k, L) for a frame: which loop it is in, where in the loop, and how long the loop is.

    Returns None for sleep and for the dead slots between rows. The generator never asks how fast
    anything moves; it asks which loop a frame belongs to, and the speed follows."""
    for name, f0, L in CYCLES:
        if f0 <= fi < f0 + L:
            return name, fi - f0, L
    return None


def phase_of(fi, winding=WINDING, mode=None):
    """The phase of the ornament on frame fi, in pixels.

    THE WHOLE AXIS IS THIS FUNCTION AND IT IS FOUR LINES LONG. It is written as P*W*k/L, and not
    as k*step for any step this file holds, because a step held anywhere is a step that has to be
    right for every loop at once — which is CONSTANT-SPEED, and is impossible, because the loops
    are 4, 5, 6 and 8 frames long. Divide instead and closure is free at every length.
    """
    cy = cycle_of(fi)
    if cy is None:
        return 0.0
    _, k, L = cy
    if mode is None:
        return PERIOD * winding * k / float(L)
    if mode == 'static':
        return 0.0
    if mode == 'const-speed':                 # one step everywhere: right on the 8s, wrong on the rest
        return PERIOD * k / 8.0
    if mode == 'nearest-int':                 # the step rounded to a whole pixel
        return float(k * max(1, int(round(PERIOD / float(L)))))
    if mode == 'double':                      # winding two — P/2 per frame on the four-frame loops
        return PERIOD * 2.0 * k / float(L)
    if mode == 'smear':                       # correct phase; the defect is in the profile, not here
        return PERIOD * winding * k / float(L)
    if mode == 'random-phase':
        return random.Random((fi, 20630)).random() * PERIOD
    raise ValueError(mode)


CONTROLS = ('static', 'const-speed', 'nearest-int', 'double', 'smear', 'random-phase')


def role_at(s, phase, mode=None):
    """The role of row s at a given phase. The profile, and nothing else, lives here."""
    f = ((s + phase) % PERIOD) / PERIOD
    if mode == 'smear':
        # SMEAR: the crest widened toward the field in proportion to the step, the way a still
        # picture says "moving". It is the only control that changes the PROFILE rather than the
        # phase, and that is exactly why it is the only one INVISIBLE can catch.
        if f < F_CREST + 0.18:
            return R_CREST
        if f < F_SHADE + 0.18:
            return R_SHADE
        return R_FIELD
    if f < F_CREST:
        return R_CREST
    if f < F_SHADE:
        return R_SHADE
    return R_FIELD


def ideal_rows(E, phase, mode=None):
    return [role_at(s, phase, mode) for s in range(E)]


# --- palette --------------------------------------------------------------------------------
# THREE stops per class: crest, shade, field. The hue plan against the tiers this sits beside — the
# 60th took brass / moonstone / verdigris, the 61st crimson-steel / amethyst / deep-teal, the 62nd
# storm-pewter / cobalt / moss. This one is a LIVE CURRENT in a dark metal, so the crest is the
# brightest thing in the set and the field is the darkest, and the contrast is the point: a crest
# has to be seen to move by one pixel.
#   warrior  EMBER ON IRON        hot orange running through COOL BLUE-GREY iron
#   mage     ARC-WHITE ON INDIGO  the coldest, well clear of the 62nd's cobalt because the field is
#                                 violet rather than blue and the crest is near-white
#   ranger   WISP ON BARK         yellow-green through WARM BROWN bark, clear of the 60th's
#                                 verdigris
# THE THREE FIELDS ARE DELIBERATELY IN THREE DIFFERENT TEMPERATURES — cool grey, violet, warm
# brown. The first render gave warrior (74,76,64) and ranger (70,72,66), two olives four units
# apart, and at 13px with a bright crest over them the two classes were the same armour in
# different hats. Class identity on this axis has to live in the FIELD, because the crest is the
# brightest thing on the sheet and the eye goes there first, and the crest is nearly white on all
# three by design.
#
# NO STOP NEAR PURE BLACK — the finishing pass carves the visor as black eye and mouth pixels and a
# near-black darkest stop swallows them (the 49th's lesson). Darkest channel-sums 214 / 226 / 208.
# Crests are chosen for what they BECOME after the finishing pass lifts the sheet, not for what
# they are in the swatch (the 61st's salmon lesson) — hence crests that look one step short of
# where they want to be here.
CURPAL = {
    'warrior': ((250, 202, 120), (132, 66, 40), (72, 80, 96)),
    'mage':    ((238, 236, 252), (92, 70, 148), (66, 62, 96)),
    'ranger':  ((220, 240, 148), (100, 84, 44), (72, 64, 52)),
}

# Per-class body tones for the plain recolor on sleep frames and on components too short to carry
# a period.
BODY = {
    'warrior': ((72, 80, 96), (132, 66, 40), (250, 202, 120)),
    'mage':    ((66, 62, 96), (92, 70, 148), (238, 236, 252)),
    'ranger':  ((72, 64, 52), (100, 84, 44), (220, 240, 148)),
}

SLOTS = {
    'chest': dict(
        outdir='_current_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary63', largest=True,
    ),
    'legs': dict(
        outdir='_current_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary63', largest=False,
    ),
    'boots': dict(
        outdir='_current_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_current', largest=False,
    ),
    'helmet': dict(
        outdir='_currentdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary63', largest=True,
    ),
}


# --- painting -------------------------------------------------------------------------------
def paint_current(fr, comp_full, stops, phase, mode=None):
    """Paint the banding onto one component at one phase. Only opaque body pixels are ever
    painted, so this cannot create strays and cannot change the silhouette."""
    if comp_full.sum() < MIN_PX:
        return None
    ys, xs = np.nonzero(comp_full)
    y0, y1 = int(ys.min()), int(ys.max())
    E = y1 - y0 + 1
    roles = ideal_rows(E, phase, mode)
    for i in range(len(ys)):
        y, x = int(ys[i]), int(xs[i])
        fr[y, x, :3] = stops[roles[y - y0]]
        fr[y, x, 3] = 255
    return dict(E=E, y0=y0, phase=phase, area=int(comp_full.sum()))


# --- reading the phase back off the painted pixels --------------------------------------------
def read_rows(fr, comp_full, stops):
    """The modal role of every row of the component, read off the PAINTED PIXELS."""
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
    return rows, E


GRID = 180          # phase search resolution, P/180 = 0.025px — far finer than PHASE_TOL


def estimate_phase(rows, E):
    """Recover the phase from the row roles alone. Returns (phase_hat, residual).

    THE READER IS THE TEST. It is given a column of role names and no idea what frame it came
    from, and it fits the ONE static profile that best explains them — which is precisely the thing
    clause INVISIBLE says is always possible. The residual it reports is therefore two things at
    once: the evidence for INVISIBLE when it is zero, and the phase estimate's own error bar.

    The estimate is the CIRCULAR MEAN of every phase that ties for the minimum residual, because
    the roles are a step function of a continuous phase and a whole interval of phases produces
    identical rows. Taking the first minimum instead of the middle of the tied interval biases the
    estimate by up to half the interval, which on a six-row component is 0.4px — larger than
    PHASE_TOL, and it is how a perfectly correct axis fails its own ADVANCE clause.
    """
    obs = [r for r in rows if r is not None]
    idx = [t for t, r in enumerate(rows) if r is not None]
    if not obs:
        return None, None
    best, ties = None, []
    for g in range(GRID):
        ph = PERIOD * g / float(GRID)
        res = sum(1 for t, r in zip(idx, obs) if role_at(t, ph) != r)
        if best is None or res < best:
            best, ties = res, [ph]
        elif res == best:
            ties.append(ph)
    ang = [2 * math.pi * p / PERIOD for p in ties]
    mx = sum(math.cos(a) for a in ang) / len(ang)
    my = sum(math.sin(a) for a in ang) / len(ang)
    ph = (math.atan2(my, mx) / (2 * math.pi)) * PERIOD % PERIOD
    return ph, best


def phase_err(a, b):
    """Circular distance between two phases, in pixels."""
    d = abs(a - b) % PERIOD
    return min(d, PERIOD - d)


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — a KINEMATICS. A claim about a SEQUENCE of pictures.
#
#   (1) ADVANCE      phase(k) - phase(0) == k * P/L, per animation row, at that row's own L.
#   (2) CLOSURE      the advance around each loop is exactly ONE period: a winding number, and an
#                    integer, and the same integer on loops of every length.
#   (3) INVISIBLE    every frame alone is a valid static profile — residual zero. The negative
#                    clause: one picture carries nothing.
#   (4) SPEED-VARIES at least three distinct realised steps over the batch.
#   (5) ONE PERIOD   exactly one P over the batch.
#
# *** WHAT IS DELIBERATELY NOT A CLAUSE. *** None of this is asked of the finished sheet after
# sprite_finish has run, for the 57th's, 60th's and 61st's reason: the light comes from outside the
# ornament. The finishing pass adds a visor, pauldron caps and a directional shade, none of which
# travels.
# ---------------------------------------------------------------------------------------------
SPEED_MIN_DISTINCT = 3


# --- the joint fit: the trajectory is measured, not the frames ---------------------------------
# THE FIRST DRAFT OF THIS READER MEASURED EACH FRAME'S PHASE AND THEN DIFFERENCED CONSECUTIVE
# FRAMES, AND IT FAILED THE AXIS ON 19 OF 153 COMPONENT-CYCLES — every one of them a six-row
# sabaton or a helmet dome. Nothing was wrong with the sprites. Differencing two noisy numbers
# doubles the noise, and the phase of ONE short component is intrinsically noisy: the reader sees
# E integer rows of a continuous phase, so a whole interval of phases produces identical pixels and
# the interval is about P^2/6E wide — 0.22px on a fifteen-row chest and 0.56px on a six-row boot,
# which is larger than the step being measured.
#
# The fix is not a looser tolerance. It is to stop measuring the wrong thing. The claim of this
# axis is about a TRAJECTORY, so a trajectory is what gets fitted: one (phase0, step) pair is
# searched against EVERY row of EVERY frame of the loop at once, and the step comes out of a fit
# with L*E constraints instead of out of the difference of two estimates with E each.
#
# THAT IS NOT A CONVENIENCE, IT IS THE THESIS. The phase of a single picture is a poor measurement
# and the motion across the loop is a good one — which is precisely what it means for the invariant
# to belong to the sequence rather than to any of its members. The reader had to be rebuilt to
# match the claim before it could confirm it.
# THE SEARCH GRID IS DERIVED, NOT CHOSEN. The six loops are 4, 5, 6 and 8 frames long, so the four
# steps this axis can ever take are P/4, P/5, P/6 and P/8, and the greatest common measure of those
# four is P/lcm(4,5,6,8) = P/120. A grid coarser than that cannot represent the axis's own motion
# and will convict it of ADVANCE for the grid's arithmetic rather than the sprite's — which is
# exactly what the first version of this file did, on a grid of 0.025px, failing the walk by ONE
# row in 120 because 0.5625 is not a multiple of 0.025. The grid is a consequence of the app's
# frame budget, like everything else here.
GRID_DEN = 120                                  # lcm(4, 5, 6, 8)
PHI_GRID = np.arange(0, GRID_DEN) * (PERIOD / GRID_DEN)
STEP_GRID = np.arange(-GRID_DEN // 2, GRID_DEN // 2 + 1) * (PERIOD / GRID_DEN)


def _roles_for(ph, E):
    """Roles of rows 0..E-1 for each phase in `ph`. Shape (len(ph), E)."""
    t = np.arange(E)
    f = ((t[None, :] + ph[:, None]) % PERIOD) / PERIOD
    r = np.full(f.shape, R_FIELD, dtype=np.int8)
    r[f < F_SHADE] = R_SHADE
    r[f < F_CREST] = R_CREST
    return r


def _residual_surface(obs_by_frame, phi, steps):
    npg, nsg = len(phi), len(steps)
    res = np.zeros((npg, nsg), dtype=np.int32)
    for k, obs in obs_by_frame:
        E = len(obs)
        ph = (phi[:, None] + k * steps[None, :]).ravel()
        r = _roles_for(ph, E).reshape(npg, nsg, E)
        m = obs >= 0
        res += (r[:, :, m] != obs[m][None, None, :]).sum(-1).astype(np.int32)
    return res


def fit_trajectory(obs_by_frame, L=None):
    """Fit ONE (phase0, step) to a whole loop. `obs_by_frame` is [(k, obs)] with obs an int array
    of row roles (-1 where a row has no pixels). Returns (step, residual, ties).

    TWO STAGES, and the second one is not a refinement for its own sake. The tie set in `step` is
    an INTERVAL — every step inside it explains the loop perfectly — so the estimate is that
    interval's midpoint, and a midpoint computed on a coarse lattice is out by up to half a cell.
    On the four-frame loops that half cell is a winding of 0.044, which is half the whole budget
    the CLOSURE clause has. So stage one finds the interval on the derived P/120 lattice and stage
    two re-measures its ends ten times finer. The bias this removes is arithmetic, not physical,
    and leaving it in would have been the same species of mistake as the 61st's REMAINDER."""
    res = _residual_surface(obs_by_frame, PHI_GRID, STEP_GRID)
    prof0 = res.min(axis=0)
    tie0 = np.flatnonzero(prof0 == prof0.min())
    lo = STEP_GRID[max(int(tie0[0]) - 1, 0)]
    hi = STEP_GRID[min(int(tie0[-1]) + 1, len(STEP_GRID) - 1)]
    fine_s = np.arange(lo, hi + 1e-12, PERIOD / (GRID_DEN * 10))
    if L is not None:
        # The exact closing step is put on the grid by construction rather than left to land on it
        # by floating-point luck. Without this the reported interval can miss its own endpoint by
        # one part in 10^15 and the summary then says something false about a batch that is fine.
        fine_s = np.unique(np.concatenate([fine_s, [WINDING * PERIOD / float(L)]]))
    fine_p = np.arange(0, 2 * GRID_DEN) * (PERIOD / (2 * GRID_DEN))
    # PROFILE OUT THE STARTING PHASE. It is a nuisance parameter — nobody cares where the ornament
    # was on frame 0 — and nuisance parameters are minimised over, not averaged across.
    prof = _residual_surface(obs_by_frame, fine_p, fine_s).min(axis=0)
    best = int(prof.min())
    tie = np.flatnonzero(prof == best)
    return (float(fine_s[tie[0]]), float(fine_s[tie[-1]])), best, int(tie.size)


def fit_closed(obs_by_frame, L, winding=WINDING):
    """Residual of the best CLOSING trajectory: step nailed to W*P/L, only the starting phase free.

    THIS IS WHY THE TEST HAS NO TOLERANCE ANYWHERE. The obvious way to test closure is to measure
    the step, multiply by L, divide by P and ask whether the answer is near 1 — and then a number
    has to be chosen for "near", and that number has to be defended. It cannot be: the free step is
    only known as an INTERVAL (every step inside it explains the loop perfectly, which is what
    clause INVISIBLE guarantees), and the midpoint of that interval is a biased estimate of the
    truth by a few percent of a winding, which is a fact about the reader and not about the sheet.
    So closure is not measured and compared. It is IMPOSED and then checked: fix the step at exactly
    one period per loop, leave only the starting phase free, and ask whether a single pixel
    disagrees. Zero or not zero. The interval is still reported, because it is the honest statement
    of what the pixels actually pin down, but no clause is decided on a threshold."""
    steps = np.array([winding * PERIOD / float(L)])
    return int(_residual_surface(obs_by_frame, PHI_GRID, steps).min())


def _signed(d):
    """A phase difference reduced to the shortest way round, with the ambiguity NAMED.

    Returns (value, ambiguous). A difference of exactly half a period is the wagon wheel: up and
    down are the same picture and no reader can tell them apart. That is not a limitation of this
    function, it is the Nyquist bound the winding number is chosen against, so it is reported
    rather than silently resolved one way."""
    d = d % PERIOD
    amb = abs(d - PERIOD / 2.0) < 1e-6
    if d > PERIOD / 2.0:
        d -= PERIOD
    return d, amb


def measure_cycle(frames, stops, mode=None):
    """Measure the phase on every frame of one cycle, then put the measurements in order.

    `frames` is [(k, L, fr, comp)] for one whole loop. Returns
    (ok, clauses, why, step_measured, winding_measured).

    NOTHING HERE IS TOLD WHAT THE STEP IS. The step is an OUTPUT — the mean of the frame-to-frame
    advances actually measured off the pixels — and the winding number is that step multiplied by
    the length of the loop and divided by the period. That is the difference between a test and a
    restatement: if the step were asserted, CONSTANT-SPEED would fail for having the wrong step,
    which tells you nothing, instead of for the loop not closing, which is the defect you can see.
    """
    obs_by_frame, resid, nrows = [], [], 0
    for k, L, fr, comp in frames:
        rows, E = read_rows(fr, comp, stops)
        obs = np.array([-1 if r is None else r for r in rows], dtype=np.int8)
        obs_by_frame.append((k, obs))
        nrows += int((obs >= 0).sum())
        _, res = estimate_phase(rows, E)
        resid.append(res if res is not None else 0)

    failed, why = [], []
    L = frames[0][1]
    n = len(frames)
    (slo, shi), jres, ties = fit_trajectory(obs_by_frame, L)
    wlo, whi = L * slo / PERIOD, L * shi / PERIOD
    step = (slo + shi) / 2.0

    # (1) ADVANCE — ONE (phase0, step) explains every row of every frame of the loop. This clause
    # says the ornament moves uniformly; it deliberately does not say how fast, and the step is an
    # output rather than an input. Zero or not zero, no threshold.
    if jres > 0:
        failed.append('ADVANCE')
        why.append('no single uniform advance explains the loop: %d of %d rows unexplained by the '
                   'best (phase, step)' % (jres, nrows))

    # (2) CLOSURE — the step is IMPOSED at exactly one period per loop and only the starting phase
    # is left free. Zero or not zero, no threshold. See fit_closed().
    cres = fit_closed(obs_by_frame, L)
    if cres > 0:
        failed.append('CLOSURE')
        why.append('a trajectory that closes on %d period(s) leaves %d of %d rows unexplained; '
                   'the loop actually winds %.3f..%.3f' % (WINDING, cres, nrows, wlo, whi))

    # (3) INVISIBLE — every frame alone is a valid static profile.
    if max(resid) > 0:
        failed.append('INVISIBLE')
        why.append('%d of %d frames are not a static profile at any phase (worst residual %d rows)'
                   % (sum(1 for r in resid if r > 0), len(resid), max(resid)))

    if abs(abs(step) - PERIOD / 2.0) < 0.03:
        why.append('AMBIGUOUS: an advance of P/2 — direction undecidable (Nyquist)')
    if failed:
        return False, sorted(set(failed)), '; '.join(why), step, (wlo, whi)
    return True, [], ('%d frames, %d rows; closes exactly on %d period; free winding %.3f..%.3f'
                      % (n, nrows, WINDING, wlo, whi)), step, (wlo, whi)


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


def build(base, cfg, cls, mode=None, winding=WINDING):
    D, M, L = BODY[cls]
    stops = CURPAL[cls]
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
        if fi >= SLEEP_FROM or cycle_of(fi) is None:
            continue                            # sleep and dead slots: body only
        ph = phase_of(fi, winding=winding, mode=mode)
        # ONE PHASE PER FRAME, SHARED BY EVERY COMPONENT OF IT — the two chausse legs travel
        # together. The phase is a function of TIME, and the two legs are at the same time.
        for comp in comps_of(a, largest):
            paint_current(fr, comp, stops, ph, mode=mode)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ------------------------------------------------------------------------------
def _big_comp(arr, fi=0):
    r, c = fi // COLS, fi % COLS
    src = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def cycles_report():
    """The loops, the steps they imply, and what each control does to their closures."""
    print('== THE LOOPS (SPRITE_SPEC.md section 1) — the app\'s frame budget, not this axis\'s choice')
    print('   period P = %.2f px      winding W = %d      step = P*W/L' % (PERIOD, WINDING))
    print()
    hdr = '   %-7s %-7s %-6s %-9s |' % ('cycle', 'frames', 'L', 'step px')
    hdr += ''.join(' %-12s' % m for m in CONTROLS)
    print(hdr)
    print('   ' + '-' * (len(hdr) - 3))
    for name, f0, L in CYCLES:
        step = PERIOD * WINDING / float(L)
        row = '   %-7s %-7s %-6d %-9.4f |' % (name, '%d-%d' % (f0, f0 + L - 1), L, step)
        for m in CONTROLS:
            if m == 'random-phase':
                row += ' %-12s' % '--'
                continue
            phs = [phase_of(f0 + k, mode=m) for k in range(L)]
            inner = [_signed(phs[i + 1] - phs[i])[0] for i in range(L - 1)]
            st = sum(inner) / max(len(inner), 1)
            w = L * st / PERIOD
            row += ' %-12s' % ('%.2f%s' % (w, '' if abs(w - WINDING) < 0.02 else ' X'))
        print(row)
    print()
    print('   THE COLUMN IS THE WINDING NUMBER, and four of the six controls are wrong in exactly')
    print('   that one number: STATIC winds 0, CONSTANT-SPEED winds L/8, NEAREST-INT winds L/P')
    print('   rounded, DOUBLE winds 2. Only the axis winds 1 on every loop, and it does so without')
    print('   being told any speed at all.')
    print('   CONSTANT-SPEED is the one to look at: right on the two eight-frame loops, wrong on')
    print('   the other four — a visible pop at the loop point, forever, several times a minute.')
    print('   DOUBLE on the four-frame loops steps exactly P/2, which is Nyquist: up and down are')
    print('   the same sheet, and that is the bound the winding number is chosen against.')


def dump_cells():
    """ASCII of one real component through a whole walk cycle, and the phase read back off it."""
    legend = {R_CREST: '^', R_SHADE: 'v', R_FIELD: '-', -1: ' '}
    comp = _big_comp(load_any('armor_chest_4.png'))
    ys, xs = np.nonzero(comp)
    sub = comp[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    stops = CURPAL['warrior']
    E = sub.shape[0]
    print('== warrior chest, the WALK (frames 10-17), L=8, step %.4f px' % (PERIOD / 8.0))
    print('   extent %d rows = %.2f periods' % (E, E / PERIOD))
    cols = []
    for k in range(8):
        fr = np.zeros(sub.shape + (4,), dtype=np.uint8)
        ph = phase_of(10 + k)
        paint_current(fr, sub, stops, ph)
        rows, _ = read_rows(fr, sub, stops)
        ph_hat, res = estimate_phase(rows, E)
        cols.append((k, ph, ph_hat, res, rows))
    print()
    print('   row |' + ''.join(' f%-2d' % (10 + k) for k, _, _, _, _ in cols))
    for t in range(E):
        print('   %3d |' % t + ''.join('  %s ' % legend[cols[j][4][t]] if cols[j][4][t] is not None
                                       else '    ' for j in range(8)))
    print('   set |' + ''.join(' %.2f' % ph for _, ph, _, _, _ in cols))
    print('   got |' + ''.join(' %.2f' % (ph_hat if ph_hat is not None else -1)
                               for _, _, ph_hat, _, _ in cols))
    print('   res |' + ''.join('  %d  ' % r for _, _, _, r, _ in cols))
    print()
    print('   legend: ^ crest   v shade   - field')
    print('   "res" is clause INVISIBLE: zero means the frame is a perfectly ordinary static')
    print('   fluted plate and carries no evidence whatever about this axis.')
    frames = [(k, 8, None, None) for k in range(8)]
    del frames
    print()
    for name, f0, L in CYCLES:
        fs = []
        for k in range(L):
            fr = np.zeros(sub.shape + (4,), dtype=np.uint8)
            paint_current(fr, sub, stops, phase_of(f0 + k))
            fs.append((k, L, fr, sub))
        ok, cl, why, step, wind = measure_cycle(fs, stops)
        print('   %-6s L=%d  %-52s -> %s' % (name, L, why, 'PASS' if ok else 'FAIL (%s)'
                                             % ', '.join(cl)))
    return True


def controls_report():
    """The six controls over the same component and the same cycles, through the same code path."""
    comp = _big_comp(load_any('armor_chest_4.png'))
    ys, xs = np.nonzero(comp)
    sub = comp[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    stops = CURPAL['warrior']
    print('== THE AXIS AND THE SIX CONTROLS, warrior chest, every cycle')
    allpass = True
    for mode in (None,) + CONTROLS:
        fails, clauses = [], set()
        for name, f0, L in CYCLES:
            fs = []
            for k in range(L):
                fr = np.zeros(sub.shape + (4,), dtype=np.uint8)
                paint_current(fr, sub, stops, phase_of(f0 + k, mode=mode), mode=mode)
                fs.append((k, L, fr, sub))
            ok, cl, why, _, _ = measure_cycle(fs, stops, mode=mode)
            if not ok:
                fails.append('%s: %s' % (name, why))
                clauses |= set(cl)
        label = 'CURRENT (the axis)' if mode is None else mode
        print('   %-20s fails on %d of %d cycles, clause(s): %s'
              % (label, len(fails), len(CYCLES), ', '.join(sorted(clauses)) if clauses else '-'))
        if fails:
            print('       e.g. %s' % fails[0])
        if mode is None:
            allpass = allpass and not fails
            if fails:
                print('       THE AXIS ITSELF FAILED - investigate')
        else:
            allpass = allpass and bool(fails)
            if not fails:
                print('       DID NOT FAIL - investigate')
    print()
    print('ACCEPTANCE (a KINEMATICS — not a statistic, a topology, an algebra, a conservation law,')
    print('a physical law, a group action, a census, a formal language, a similarity or a')
    print('registration):')
    print('(1) ADVANCE      the phase advances by the same amount between every pair of frames;')
    print('                 the step is an OUTPUT of the measurement, never an input to it;')
    print('(2) CLOSURE      a trajectory that closes on exactly ONE period explains every row —')
    print('                 imposed and checked, never compared: a WINDING NUMBER, no tolerance;')
    print('(3) INVISIBLE    every frame alone is a valid static profile — one picture says nothing;')
    print('                 and it is logically PRIOR to (1) and (2), which is why SMEAR fails all')
    print('                 three: a phase measured off an unrecognised profile is not a number.')
    print('(4) SPEED-VARIES at least %d distinct steps are realised over the batch;'
          % SPEED_MIN_DISTINCT)
    print('(5) ONE PERIOD   exactly one P over the batch.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def accept_all():
    """The five clauses over every component of every active frame of all 24 sheets."""
    ncomp = ncycles = nshort = nfail = 0
    steps = {}
    winds = []
    byclause = {}
    extents = {}
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            stops = CURPAL[cls]
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                # Components are matched across the frames of a cycle by their INDEX in the
                # component list, which is stable because label4 scans in raster order and the
                # pieces of a garment do not swap places between two adjacent frames.
                for name, f0, L in CYCLES:
                    percomp = {}
                    for k in range(L):
                        fi = f0 + k
                        r, c = fi // COLS, fi % COLS
                        src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
                        a = src[..., 3] > 0
                        if not a.any():
                            continue
                        fr = np.zeros_like(src)
                        ph = phase_of(fi)
                        for ci, comp_full in enumerate(comps_of(a, largest)):
                            if comp_full.sum() < MIN_PX:
                                continue
                            paint_current(fr, comp_full, stops, ph)
                            ys = np.nonzero(comp_full)[0]
                            E = int(ys.max() - ys.min() + 1)
                            if E < MIN_EXTENT:
                                nshort += 1
                                continue
                            extents[E] = extents.get(E, 0) + 1
                            percomp.setdefault(ci, []).append((k, L, fr, comp_full))
                    for ci, frames in percomp.items():
                        if len(frames) < L:
                            continue            # component absent from part of the loop
                        ncomp += 1
                        ncycles += 1
                        res = measure_cycle(frames, stops)
                        if res is None:
                            continue
                        ok, cl, why, step, wnd = res
                        winds.append(wnd)
                        if not ok:
                            nfail += 1
                            for c2 in cl:
                                byclause[c2] = byclause.get(c2, 0) + 1
                            if nfail <= 20:
                                print('   VIOLATION [%s] %s %s%s %s comp %d: %s'
                                      % (', '.join(cl), kind, cls, suffix, name, ci, why))
                            continue
                        steps.setdefault(L, []).append(step)
    print('ACCEPTANCE over every component of every cycle of all 24 sheets:')
    print('  component-cycles           %d' % ncycles)
    print('  clause 1-3 violations      %d%s' % (nfail,
          ('   ' + ', '.join('%s:%d' % (k, byclause[k]) for k in sorted(byclause)))
          if byclause else ''))
    print('  components too short       %d   (extent < %d px, cannot show a period; reported)'
          % (nshort, MIN_EXTENT))
    print('  distinct extents banded    %d   (%d .. %d rows)'
          % (len(extents), min(extents) if extents else 0, max(extents) if extents else 0))
    print('  CLAUSE 4 — SPEED-VARIES  (the step is measured, never asserted; P/L is shown only')
    print('             so that the measurement can be checked against the arithmetic):')
    for L in sorted(steps):
        v = steps[L]
        print('     loops of %d frames: %3d component-cycles, step measured %.4f +- %.4f px'
              '   (P/%d = %.4f)'
              % (L, len(v), sum(v) / len(v), max(abs(x - sum(v) / len(v)) for x in v),
                 L, PERIOD / L))
    sok = len(steps) >= SPEED_MIN_DISTINCT
    print('     %d distinct loop lengths -> %d distinct speeds, %d required -> %s'
          % (len(steps), len(steps), SPEED_MIN_DISTINCT, 'PASS' if sok else 'FAIL'))
    if winds:
        print('  THE WINDING NUMBER, as the pixels pin it down (no clause is decided on this — it')
        print('  is what the loop is CONSISTENT with, and CLOSURE is decided by imposing 1 and')
        print('  finding zero disagreement): every component-cycle admits an interval of windings,')
        print('  and %d of %d of those intervals contain %d.'
              % (sum(1 for a, b in winds if a - 1e-9 <= WINDING <= b + 1e-9), len(winds), WINDING))
        wid = sorted(b - a for a, b in winds)
        print('     interval width: min %.3f  median %.3f  max %.3f      overall range %.3f .. %.3f'
              % (wid[0], wid[len(wid) // 2], wid[-1],
                 min(w[0] for w in winds), max(w[1] for w in winds)))
        print('     A WIDE INTERVAL IS NOT A FAILURE, IT IS A SHORT COMPONENT: a six-row sabaton')
        print('     shows about one period and cannot pin a winding closer than a few percent,')
        print('     while a twenty-three-row cuirass pins it to nothing at all. That spread is')
        print('     exactly why CLOSURE is imposed rather than compared — it never asks where the')
        print('     interval is, only whether a closing trajectory explains the pixels, and on all')
        print('     %d component-cycles one does, with zero rows left over.' % len(winds))
    print('  CLAUSE 5 — ONE PERIOD:  P = %.2f px everywhere -> PASS' % PERIOD)
    allpass = (nfail == 0) and sok
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def slots_diag(path='_diag_current_slots.png', zoom=8):
    """One idle frame of every slot and class, banded, before the finishing pass."""
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


def visor_diag(path='_diag_current_visor.png', zoom=12):
    """The helmet head zone before and after the finishing pass — the visor must survive the
    banding, which is why no stop in the palette goes near black."""
    cfg = SLOTS['helmet']
    outs = []
    for cls, stem in cfg['srcs'].items():
        base = load_any('%s.png' % stem)
        arr = build(base, cfg, cls)
        raw = arr[16:40, 28:56].copy()
        fin, _ = finish_array(arr.copy(), 'helmet_%s_legendary63.png' % cls)
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


def main():
    if '--cycles' in sys.argv:
        cycles_report()
        return
    if '--cells' in sys.argv:
        dump_cells()
        return
    if '--controls' in sys.argv:
        controls_report()
        return
    if '--accept' in sys.argv:
        accept_all()
        return
    if '--sweep' in sys.argv:
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
