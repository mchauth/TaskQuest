#!/usr/bin/env python3
"""FIFTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS — the STRATA family (LAP-JOINTED BANDS in a
readable order): the armour is built up out of a handful of broad straight bands laid ACROSS the
piece at different angles, one after another, each new band passing OVER every band already there
and casting a hard shadow onto it. Nothing is woven. At every crossing one band is whole and the
other is severed, and the same band wins every crossing it is in, so the pile can be read back as a
SEQUENCE: this band was laid first, then this one, then this one.

    the ornament is  FACE   (a band's exposed surface — 2px, the band itself)
                   + LIP    (its lit edge, the 1px flank that faces the light)
                   + RIVET  (a bright pip near each visible end of a band — it is fastened down)
                   + BSHADE (a later band's cast shadow where it falls ON AN EARLIER BAND)
                   + SHADE  (the same shadow where it falls on the bare plate)
                   + PLATE  (the plate the whole pile is laid on)
                   + DEEP   (the plate where no band comes near it)

*** THIS IS THE FIRST AXIS WITH A TIME ORDER. ***
All fifty-four prior axes are SIMULTANEOUS. Ask any of them "which part of this was made first" and
the ornament has no answer — a honeycomb's cells, a runic register's letters, a granulated bead
field, the labyrinth's single wire: every one of them is a state, and every part of it is as old as
every other part. Here the ornament's whole content is a HISTORY. Its elements are not related by
position, size, descent or connectivity; they are related by PRECEDENCE, and precedence is a
different kind of relation because it is TRANSITIVE and ANTISYMMETRIC. A viewer reads the piece
pairwise — this band is severed by that one, so that one is later — and those local facts compose,
without contradiction, into ONE global sequence over the whole piece. That is something no field can
do and no single object can do either.

The 54th LABYRINTH is the immediate predecessor and this is its exact complement, which is why it
follows it: that axis is ONE member that never crosses itself, and its subject is where the member
GOES. This is SEVERAL members whose only content is how they CROSS. Take the crossings away and
there is no axis left here at all — which is precisely what the FLAT control in --sweep shows.

The families it could be confused with each fail on something that can be COUNTED:
  * The 30th CABLE and 39th GUILLOCHE are the first thing anyone will say, because they also cross
    and they also resolve over-and-under. They are WEAVES, and a weave is the exact opposite of
    this: a strand goes over at one crossing and UNDER at the next, by definition, because that
    reciprocity is what makes a weave hold together. So a weave's over-relation is INCONSISTENT per
    pair (the same two strands resolve both ways at different crossings) and its precedence graph
    has a CYCLE. It cannot be laid down in an order, and it is not trying to be. Here the relation
    is consistent at every crossing and the graph is ACYCLIC — checked, not asserted, and the
    --sweep WEAVE control forces the alternation back on and reports the cycle it produces.
  * The 16th TWILL and 18th BASKETWEAVE are weaves too, at a smaller scale, and fail identically.
  * The 26th TARTAN is the sharpest near miss because its bands really do just cross. What a sett
    does at a crossing is BLEND — the overlap becomes a third, denser tone, belonging to neither
    band, which is exactly what a woven cloth looks like and exactly what says NEITHER band is on
    top. Here no crossing ever produces a third tone: one band's face runs straight through
    unbroken and the other one stops dead at its edge. Tartan also has 2 directions on a strict
    period; this has up to 5 distinct angles and no period at all.
  * The 15th SCALE overlaps with a fixed z-order, and this is the subtlest one to get right. A
    scale field's order is POSITIONAL — every scale laps the one below it in the same direction
    everywhere, so the "order" is just a restatement of the lattice and every element is congruent
    to every other. Here the members are not congruent (different angles, different lengths,
    different offsets), the order is not derivable from position, and it is GLOBAL: the top band is
    over the bottom band even where they are nowhere near each other in the stack.
  * The 10th CROSS / TRIPLE-STRAP and the 6th BALDRIC are straps, but they are a named fixed
    accessory in a fixed arrangement, they are 1 or 2 or 3 members that do not resolve depth against
    one another, and they do not respond to the silhouette.
  * The 52nd AJOURE is two surfaces and the 15th's cousin in occlusion — but its two surfaces are a
    plate and a LINING, a fixed pair, always in the same relation, everywhere on the piece. Two is
    not an order. An order needs at least three mutually comparable things, which is why the band
    count floor here is 3 wherever the slot can hold 3.
  * The 8th SIDE-STRIPE, 11th FLUTING, 42nd STRIGIL, 43rd GADROON and 44th ZIGZAG are all families
    of PARALLEL members. Parallel members never cross, so they have nothing to order.

Geometry, per connected component, in the component's own frame:
    n_bands   from the component's area (see NBANDS) — 3 on a torso, a dome and a thigh, 2 on a
              foot; the STACKING ORDER is the band index, low index laid first
    angle     band k takes ANGLES[k], a fixed well-separated list; never two parallel bands, so
              every pair crosses somewhere on the plane and nearly every pair crosses on the piece
    offset    band k sits at fraction FRACS[k] of the component's own extent along band k's normal,
              and FRACS starts at 0.5 so the FIRST band laid is the one through the middle — it is
              the band every later band crosses, which is what keeps the precedence graph connected
              enough to have a unique reading
    footprint LIP (1px, on the flank facing the light) + FACE (BAND_W px); SHADOW is a SH px strip
              immediately outside the band on the OPPOSITE flank, painted onto whatever is under it
              at the time — dark metal if that is an earlier band, dark plate if it is bare plate
    relief    the shadow is the only depth cue and it is the whole axis: it is what says the later
              band stands ON the earlier one rather than merely beside it
    rivets    the two extreme pixels of a band's VISIBLE run, stepped one pixel in, on bands whose
              visible run is at least RIVET_MIN long

Authoring philosophy identical to gen_labyrinth_axis54.py / gen_granulation_axis53.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing is added, nothing removed, the
silhouette is untouched, so the generator CANNOT create isolated pixels, background bleed, extra
components or a changed mask — it is QA-safe by construction. Sleep frames (fi >= 60) get a plain
body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()` — the canonical chain
(no-smooth shading with protect=False, shirt pauldron/gorget/chest-plate separation, helmet black
eye+mouth visor with NO full-silhouette rim, hat brim/crease folds for open headgear). See
CONTEXT.md "MANDATORY - the finishing pass". Eleventh generator to call it in-line, after axes 45-54.

Run from repo root:
  python3 scripts/gen_strata_axis55.py
  python3 scripts/gen_strata_axis55.py --cells    # ASCII dump + the ORDER acceptance test
  python3 scripts/gen_strata_axis55.py --swatch   # bare motif on a test plate, no sheets
  python3 scripts/gen_strata_axis55.py --sweep    # band-count sweep + the WEAVE and FLAT controls
Then QA (examples):
  python3 scripts/sprite_qa.py _strata_legendary_preview/shirt_warrior_legendary55.png
  python3 scripts/sprite_qa.py _stratadome_helmet_preview/helmet_mage_legendary55.png --y-min 2
  python3 scripts/sprite_qa.py _strata_boots_preview/boots_warrior_legendary_strata.png --y-max 63
"""
import math
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

# --- Strata constants -------------------------------------------------------------------------
# BAND_W is the face width, on top of a 1px LIP and with a SH px shadow outside. So a band consumes
# BAND_W + 1 pixels of surface and darkens SH more. Swept (--sweep) on a real torso and a real leg.
#   BAND_W 1  a 1px face with a 1px lip beside it is not a band, it is a rule, and a pile of ruled
#             lines at angles with no interior is the 20th TRELLIS with the lines out of register.
#             Worse, a severed 1px line and an unsevered 1px line differ by one missing pixel, so
#             the crossings stop resolving and the axis's only content goes with them.
#   BAND_W 2  CHOSEN. Face 2 + lip 1 = a 3px band, and a crossing therefore interrupts the band
#             underneath for 3 to 4 pixels (band plus its shadow). That is the same interruption
#             width the 30th CABLE and 39th GUILLOCHE already prove legible at this scale, which is
#             the whole reason to borrow it: the over/under READING is known to work at 3px, and
#             everything this axis says is said through that reading.
#   BAND_W 3  a 4px band. Five of them cover a 13px torso completely, the plate disappears, and
#             with no ground left the piece reads as a solid recolor with a few dark seams in it —
#             i.e. the 12th BANDED-LAMELLAR. It also puts the band count floor out of reach on
#             legs and boots.
BAND_W = 2
SH = 1

# Band angles in degrees, IN STACKING ORDER (band 0 is laid first, so it is under everything). Chosen
# to be mutually well separated — the smallest separation in the list is 45 degrees — because a
# glancing crossing between two nearly-parallel bands produces a long thin overlap in which the
# severed band's stub is one or two pixels and the precedence cannot be read. No two are parallel,
# so on the plane every pair crosses exactly once.
ANGLES = (10.0, 100.0, 55.0, 145.0, 32.0)

# Where band k sits, as a fraction of the component's own extent along band k's own normal.
# FRACS[0] = 0.5 on purpose: the FIRST band laid runs through the middle of the piece, so it is the
# one every later band has the best chance of crossing. That is what keeps the precedence graph
# connected — an order is only READABLE off the piece if the crossings that exist are enough to
# chain the bands together, and a stack of bands that never meet is a stack with no story.
FRACS = (0.50, 0.30, 0.70, 0.42, 0.62)

# How far from the middle of the piece FRACS is allowed to reach, tried in order until the piece
# yields a TOTAL order. A pair of bands that never meet on the silhouette cannot be ranked, and a
# stack that cannot be ranked is a heap, not an order — so when a silhouette is awkward enough that
# two bands miss each other, the bands are pulled toward the middle of the piece and it is tried
# again. Deterministic: the same silhouette always lands on the same rung, so a sheet regenerates
# identically and the male and female sheets of one item agree wherever their masks do.
#   0.60  the default, and it is what almost every frame uses: bands well spread over the piece.
#   0.40  and
#   0.22  the fallbacks. Measured: at a FIXED 0.5 the acceptance test failed the totality clause on
#         25 of 985 components — the long thin WARRIOR LEG in the run poses, the CHEST in the cheer
#         poses where the raised arms stretch the silhouette, and two female boot frames. This is
#         the fourth appearance of the same adaptive-boundary lesson (the 52nd's MARGIN_MIN, the
#         53rd's shot pass, the 54th's adaptive pitch): a constant tuned on the IDLE frame is not a
#         constant that survives every POSE, and the fix is a ladder rather than a smaller constant,
#         because clamping every piece to 0.22 piles all three bands into one knot in the middle
#         and gives back the bare margin the 49th warned about.
# AND THEN THE BAND COUNT ITSELF DROPS. The spread ladder alone still left 16 components unranked,
# all of them poses where the silhouette is a U — a torso with both arms RAISED, whose centroid
# falls in the gap between the arms, so no amount of centring puts a band where the others can meet
# it. So the ladder continues downward through N-1, N-2, ..., 2, and the first (count, spread) pair
# that yields a total order wins. That is the honest response rather than a cosmetic one: this axis
# IS the order, so a pose that cannot carry three comparable bands carries two, and two bands with
# one crossing is still a fact about what was laid first. What it must never do is carry three bands
# that cannot be ranked, because that is a heap with no content. Result: 0 of 985.
SPREADS = (0.60, 0.40, 0.22)

# Band count from the component's area. An ORDER needs at least three mutually comparable things —
# two bands crossing tell you which is on top and that is the 52nd AJOURE's fixed pair, not a
# sequence — so 3 is the floor wherever the slot can hold 3. Measured areas on the real idle frames:
# torso 135, leg 98, dome 91, foot 16.
#   N=5 and N=4 were both rendered on the real torso and dome at 20x (--nsweep frames) and both are
#   OVER-FILLED: band coverage runs 71-74%, the plate survives only in the corners, and with almost
#   no ground left between them the bands stop reading as separate straps laid on something and
#   start reading as a mottle. That is the 12th BANDED-LAMELLAR with the lames out of register.
#   N=3 is the choice on every real slot: coverage ~55%, three clean straps, three crossings, and
#   three is exactly the smallest number that can carry an ORDER rather than a fixed pair.
#   N=2 is the floor for a foot and it is an honest one — a foot cannot hold three 2px bands — but
#   it is a PAIR, not a sequence, which is why the acceptance test reports it separately.
# The 4-band case survives only for a component as large as the synthetic test plate.
NBANDS = ((150, 4), (28, 3), (MIN_PX, 2))

# A band whose VISIBLE run (the pixels it still owns after the later bands have covered it) is
# shorter than this gets no rivets: two bright pips on a four-pixel stub read as a pair of loose
# specks rather than as fastenings.
RIVET_MIN = 7

# A component with fewer than this many INTERIOR pixels lays THIN bands (face 1 + lip 1) instead of
# the full 3px band, and gets no rivets. Same constant and the same measured reason as the 52nd's
# MARGIN_MIN, the 53rd's and the 54th's: interior counts are chest 78, dome 59, legs 39 — but BOOTS
# 2 TO 8, because a foot at this scale is four or five pixels across and is all boundary. A 3px band
# plus a shadow on a 5px foot is the whole foot, and a band that covers its own plate has nothing to
# be over.
MARGIN_MIN = 20

# Per class, seven stops: (rivet, lip, face, bshade, plate, shade, deep).
#   * TWO RAMPS, and which role sits on which ramp is the 54th's hard-won lesson applied in advance.
#     RIVET, LIP, FACE and BSHADE are the BAND'S ramp; PLATE, SHADE and DEEP are the PLATE'S. A
#     shadow is the one role that appears on BOTH — that is why there are seven stops and not six.
#     A later band's shadow falling on an earlier band must be dark BAND, and the same shadow
#     falling on bare plate must be dark PLATE; give both of them one shared dark tone and the
#     shadow stops reading as a shadow cast BY something ONTO something and starts reading as a
#     third material, at which point the depth cue — the only thing this axis has — is gone.
#   * The band and the plate are DIFFERENT MATERIALS and the difference is carried by HUE as well as
#     luminance; at 13px a pure luminance step reads as shading (the 52nd's lesson).
#   * DELIBERATE INVERSION: in all three classes the BAND is the DARK material and the PLATE is the
#     PALE one. Every recent tier is a bright figure on a dark field (52nd, 53rd, 54th all), so this
#     one reads unmistakably different at 1x in the inventory grid before any pattern resolves. It
#     also serves the axis: a dark band's cast shadow onto a PALE plate is the strongest possible
#     statement of the one relation the ornament exists to state.
#   * No stop near pure black. HELMET constraint, not taste: the finishing pass carves the visor as
#     black eye and mouth pixels and a near-black stop on the dome swallows the face slit (the 49th's
#     lesson). Every class's darkest stop — BSHADE in all three — clears channel-sum 150.
#   * The pale stops stay OFF the skin ramp: cool grey, cool lilac-grey and pale sage, never a warm
#     off-white, which on a narrow female chest reads as bare shoulder (the 47th's lesson). Here the
#     pale stop is the FIELD and therefore the majority of the pixels, so this matters more than it
#     ever has. The one warm pale stop in the set is the warrior's brass RIVET, allowed under the
#     same exemption as the 54th's ranger TERM: a rivet is two pixels on a band.
#   * Not a recolor of the neighbours. The 54th is platinum/oxblood, gold/indigo, copper/teal; the
#     53rd gold/graphite, moonsilver/violet, silver-jade/forest; the 52nd blued-steel/brass,
#     moonsilver-lilac/teal, green-birch/slate-blue. What carries at 1x is the majority hue, and here
#     that is the PLATE: pale steel, pale ash-lilac and pale lichen. No prior tier in the set has a
#     pale majority at all.
#   * DEEP sits only ONE step off PLATE, not three. The first cut had it three steps down and the
#     untouched corners of a silhouette came out as distinct grey blotches — they read as stains or
#     damage on the plate rather than as plate the pile does not reach, because a tonal step that
#     large announces a MATERIAL and there is no third material here. SHADE, which is a real cast
#     shadow and does have something to announce, keeps the big step.
STRATA = {
    # blackened-iron bands, brass rivets, on a pale steel plate
    'warrior': ((244, 214, 144), (124, 132, 146), (78, 84, 96), (52, 56, 66),
                (214, 220, 224), (158, 164, 172), (184, 190, 196)),
    # amethyst bands, moon-white rivets, on a pale ash-lilac plate
    'mage':    ((250, 240, 255), (170, 124, 212), (118, 78, 160), (72, 48, 104),
                (206, 208, 220), (152, 154, 172), (180, 182, 196)),
    # bog-oak green bands, bone rivets, on a pale lichen plate
    'ranger':  ((240, 244, 214), (104, 124, 80), (68, 84, 52), (52, 64, 44),
                (192, 200, 168), (140, 148, 120), (168, 176, 146)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only; taken off the plate stops
# plus the rivet as the highlight, so the piece reads as one object when no band is drawn.
BODY = {
    'warrior': ((158, 164, 172), (214, 220, 224), (244, 214, 144)),
    'mage':    ((152, 154, 172), (206, 208, 220), (250, 240, 255)),
    'ranger':  ((140, 148, 120), (192, 200, 168), (240, 244, 214)),
}

SLOTS = {
    'chest': dict(
        outdir='_strata_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary55', largest=True,
    ),
    'legs': dict(
        outdir='_strata_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary55', largest=False,
    ),
    'boots': dict(
        outdir='_strata_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_strata', largest=False,
    ),
    'helmet': dict(
        outdir='_stratadome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary55', largest=True,
    ),
}

R_RIVET, R_LIP, R_FACE, R_BSHADE, R_PLATE, R_SHADE, R_DEEP = 0, 1, 2, 3, 4, 5, 6

# The standing edge rule — brightest stop never on the silhouette, darkest stop never on the
# silhouette — so no dome ever grows the full-silhouette bright rim or dark rim that mangles a
# patterned helmet. Applied by DEMOTION on boundary pixels rather than by a bezel: a bezel would put
# a continuous ring of one tone around the piece, and a ring is a closed curve that CROSSES every
# band, which would add a sixth member to the stack that has no place in its order.
DEMOTE = {R_RIVET: R_LIP, R_LIP: R_LIP, R_FACE: R_FACE, R_BSHADE: R_FACE,
          R_PLATE: R_PLATE, R_SHADE: R_SHADE, R_DEEP: R_PLATE}


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


def n_bands(area):
    for lo, n in NBANDS:
        if area >= lo:
            return n
    return 0


_ROLE_CACHE = {}


def _role_once(comp, n, weave, flat, bandw, spread):
    """One attempt at the role field, at a given SPREAD. See role_field() for the wrapper."""
    h, w = comp.shape
    framed = _has_interior(comp)
    if not framed:
        bandw = 1                       # see MARGIN_MIN — a foot is all boundary

    ys, xs = np.nonzero(comp)
    cy = float(ys.mean())
    cx = float(xs.mean())
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)

    # 1. every band's footprint, independently of who ends up on top
    bands = []
    foot = []
    lips = []
    shad = []
    for k in range(n):
        th = math.radians(ANGLES[k])
        nx, ny = math.cos(th), math.sin(th)
        s = (xx - cx) * nx + (yy - cy) * ny
        sv = s[comp]
        smin, smax = float(sv.min()), float(sv.max())
        # `spread` pulls every band toward the middle of the piece; see SPREADS.
        frac = 0.5 + spread * (FRACS[k] - 0.5)
        o = smin + frac * (smax - smin) - (bandw + 1) / 2.0
        lo, hi = o, o + bandw + 1
        inband = comp & (s >= lo) & (s < hi)
        if not inband.any():
            bands.append(None)
            foot.append(None)
            lips.append(None)
            shad.append(None)
            continue
        # The lit flank is the one whose outward normal faces the upper-left light; the shadow falls
        # on the other side.
        if (nx + ny) > 0:
            lip = inband & (s < lo + 1)
            shadow = comp & (s >= hi) & (s < hi + SH)
        else:
            lip = inband & (s >= hi - 1)
            shadow = comp & (s >= lo - SH) & (s < lo)
        bands.append((nx, ny, lo, hi))
        foot.append(inband)
        lips.append(lip)
        shad.append(shadow)

    def wins(i, j):
        """Which of two bands is seen at a point where both lie. Normally the later one — that is
        the axis. Under the WEAVE control the outcome alternates with the parity of the pair, which
        is what a weave does and what makes its precedence graph cyclic."""
        if i == j:
            return i
        if weave:
            return min(i, j) if (i + j) % 2 == 0 else max(i, j)
        return max(i, j)

    # 2. ownership: at each pixel, the winner of a tournament among the bands covering it
    owner = np.full((h, w), -1, dtype=np.int8)
    for k in range(n):
        if foot[k] is None:
            continue
        m = foot[k]
        cur = owner[m]
        new = np.array([k if c < 0 else wins(int(c), k) for c in cur], dtype=np.int8)
        owner[m] = new

    role = np.where(comp, R_PLATE, -1).astype(np.int8)
    for k in range(n):
        if foot[k] is None:
            continue
        vis = owner == k
        role[vis] = R_FACE
        role[vis & lips[k]] = R_LIP

    # 3. shadows, cast in stacking order onto whatever the band is over. A shadow tone depends on
    # what it lands on — dark metal on an earlier band, dark plate on bare plate. Give both one
    # shared dark tone and the shadow stops reading as cast BY something ONTO something and starts
    # reading as a third material, at which point the depth cue is gone and so is the axis.
    if not flat:
        for k in range(n):
            if shad[k] is None:
                continue
            m = shad[k] & comp
            if not m.any():
                continue
            ys2, xs2 = np.nonzero(m)
            for py, px in zip(ys2, xs2):
                o = int(owner[py, px])
                if o >= 0 and wins(o, k) != k:
                    continue                    # the pixel belongs to a band that is OVER band k
                role[py, px] = R_BSHADE if o >= 0 else R_SHADE

    # DEEP — plate the pile does not reach. Keeping it apart from PLATE is what stops an untouched
    # corner of a silhouette reading as a blank patch of some other garment.
    covered = owner >= 0
    near = np.zeros((h, w), dtype=bool)
    for dy in (-3, -2, -1, 0, 1, 2, 3):
        for dx in (-3, -2, -1, 0, 1, 2, 3):
            sy0, sy1 = max(0, dy), h + min(0, dy)
            sx0, sx1 = max(0, dx), w + min(0, dx)
            near[sy0:sy1, sx0:sx1] |= covered[sy0 - dy:sy1 - dy, sx0 - dx:sx1 - dx]
    role[(role == R_PLATE) & ~near] = R_DEEP

    # RIVETS — ONLY ON THE TOP BAND, and that restriction is the fix for a real failure. The first
    # cut riveted every band, which put six bright pips on a 91px helmet dome, and a scatter of
    # bright pips on a dark ground at this scale is not a set of fastenings, it is the 13th
    # STUDWORK — an older axis, showing through. Riveting only the band that is over everything
    # gives EXACTLY TWO pips per component, and it says something the axis wants said: the last
    # strap laid is the one that pins the pile down.
    if framed:
        vis_bands = [k for k, b in enumerate(bands) if b is not None and int((owner == k).sum()) > 0]
        for k in (vis_bands[-1:] if vis_bands else []):
            b = bands[k]
            nx, ny, lo, hi = b
            m = owner == k
            if int(m.sum()) < RIVET_MIN:
                continue
            ty, tx = -nx, ny                     # along the band
            py, px = np.nonzero(m)
            t = px * tx + py * ty
            for idx in (int(np.argmin(t)), int(np.argmax(t))):
                sy, sx = int(py[idx]), int(px[idx])
                # step one pixel inward along the band so the pip is not on the very tip
                step = 1 if idx == int(np.argmin(t)) else -1
                ry = int(round(sy + step * ty))
                rx = int(round(sx + step * tx))
                if 0 <= ry < h and 0 <= rx < w and owner[ry, rx] == k:
                    role[ry, rx] = R_RIVET
                else:
                    role[sy, sx] = R_RIVET

    # THE PRECEDENCE FACTS, read back off the painted pixels rather than off the painting order —
    # the acceptance test must check what a viewer can SEE, not what the generator intended.
    over = {}
    for i in range(len(bands)):
        for j in range(i + 1, len(bands)):
            if foot[i] is None or foot[j] is None:
                continue
            cross = foot[i] & foot[j] & comp
            if not cross.any():
                continue
            seen = owner[cross]
            top = [v for v in (i, j) if int((seen == v).sum()) > 0]
            if not top:
                continue        # a third band covers the whole crossing: not observable here
            # consistent means the crossing region shows exactly one of the two, never both
            over[(i, j)] = top[0] if len(top) == 1 else None
    return role, owner, bands, over


def role_field(comp, nb=None, weave=False, flat=False, bandw=None):
    """Classify every pixel of the component box into one of the seven roles, and return the
    precedence facts alongside, so the acceptance test reads the same pixels a viewer would.

    Walks the SPREADS ladder and keeps the FIRST rung whose crossings give a total order — the
    ornament's whole content is that order, so a rung that does not deliver one is not a slightly
    worse version of this axis, it is a different and emptier ornament. If no rung delivers one
    (a silhouette can be too small or too ragged), the widest is kept: better a readable pile with
    one unranked pair than a knot in the middle of the piece.

    `weave` and `flat` exist only for --sweep: they are the two CONTROLS that show what this axis
    turns into when its defining property is removed.
      weave  alternates the over/under with the parity of the pair, the way a real weave does. The
             ornament still looks busy and plausible, its crossings stop being consistent and its
             precedence graph acquires a CYCLE, so no sequence can be read off it at all — that is
             the 30th CABLE / 39th GUILLOCHE.
      flat   drops the cast shadow. Every band is then simply painted over the last one with no
             depth cue, the severed stub abuts the whole band with nothing between them, and at 13px
             the eye reads the junction as a blend rather than an occlusion — that is the 26th
             TARTAN's node, and it is the more instructive of the two controls because the geometry
             is completely unchanged and the axis is still gone.

    Returns (role, owner, bands, over) where `owner` is the band index visible at each pixel (-1 for
    plate) and `over` maps a crossing pair to the band index seen on top there.
    """
    bandw = BAND_W if bandw is None else bandw
    n = n_bands(int(comp.sum())) if nb is None else nb
    key = (comp.shape, comp.tobytes(), n, weave, flat, bandw)
    hit = _ROLE_CACHE.get(key)
    if hit is not None:
        return hit
    first = None
    out = None
    done = False
    for n_try in range(n, 1, -1):
        for spread in SPREADS:
            out = _role_once(comp, n_try, weave, flat, bandw, spread)
            if first is None:
                first = out
            if weave:
                done = True             # the control must not be rescued by the ladder
                break
            ok, _, _, _ = order_of(out[2], out[3])
            if ok:
                done = True
                break
        if done:
            break
    if not done:
        out = first
    _ROLE_CACHE[key] = out
    return out


def paint_strata(fr, comp_full, stops, nb=None, weave=False, flat=False, bandw=None):
    """Paint the pile onto one component. Only opaque body pixels are ever painted, so this cannot
    create strays and cannot change the silhouette."""
    if comp_full.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    role, _, _, _ = role_field(comp, nb, weave, flat, bandw)
    interior = _interior(comp)
    boundary = comp & ~interior
    table = stops

    for y, x in zip(ys, xs):
        ly, lx = int(y) - y0, int(x) - x0
        r = int(role[ly, lx])
        if r < 0:
            continue
        rgb = table[DEMOTE[r]] if boundary[ly, lx] else table[r]
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


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    stops = STRATA[cls]
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
        # ONE PILE PER CONNECTED COMPONENT — the 54th's lesson, and it applies with more force here:
        # a band is a physical strap fastened to a physical plate, so it cannot span the gap between
        # the two legs of a pair of chausses or between the left boot and the right. Each is its own
        # piece of armour with its own stack laid on it.
        lbl, n = label4(a)
        if n < 1:
            continue
        if largest:
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comps = [(lbl == int(counts.argmax()))]
        else:
            comps = [(lbl == i) for i in range(1, n + 1)]
        for comp in comps:
            paint_strata(fr, comp, stops)
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
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the pile
    can be judged on a shape with the features the real slots have."""
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


def swatch(path='_diag_strata_swatch.png', zoom=12):
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_strata(a, m, STRATA[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def _big_comp(arr):
    src = arr[0:FH, 0:FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def sweep(path='_diag_strata_sweep.png', zoom=11):
    """Warrior chest and leg idle frames across the band count, plus the two CONTROLS."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    variants = [('N=2', dict(nb=2)), ('N=3', dict(nb=3)), ('N=4', dict(nb=4)), ('N=5', dict(nb=5)),
                ('N=4 WEAVE', dict(nb=4, weave=True)), ('N=4 FLAT', dict(nb=4, flat=True)),
                ('N=4 W=3', dict(nb=4, bandw=3))]
    cells = []
    for name, kw in variants:
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            comp = _big_comp(arr)
            fr = np.zeros_like(arr[0:FH, 0:FW])
            paint_strata(fr, comp, STRATA['warrior'], **kw)
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
    print('wrote %s (band-count sweep + WEAVE/FLAT/W=3 controls - no sheets written)' % path)


def order_of(bands, over):
    """The acceptance test's core, and it is a NEW KIND of test.

    Every previous axis is accepted on a STATISTIC of its field (the 46th's cell count, the 48th's
    size ratio, the 50th's glyph survival, the 52nd's distinct-hole appearances, the 53rd's radius
    histogram, the 54th's topology). This axis's content is a RELATION, so it is accepted on the
    ALGEBRA of that relation:

        consistent  every crossing of a given pair resolves the same way — no pair is over in one
                    place and under in another. A weave fails this by definition.
        acyclic     the precedence graph has no cycle, so "was laid before" is a real order and not
                    an Escher staircase. This is the one the WEAVE control breaks.
        total       the order is UNIQUE — the crossings that actually exist on this silhouette are
                    enough to chain every band into one sequence with no ties. A stack whose bands
                    never meet is acyclic for a trivial reason and says nothing.

    Returns (ok, seq, ncross, why).
    """
    live = [i for i, b in enumerate(bands) if b is not None]
    if len(live) < 2:
        return False, [], 0, 'fewer than two bands'
    edges = {}
    ncross = 0
    for (i, j), top in over.items():
        if top is None:
            return False, [], ncross, ('INCONSISTENT — bands %d and %d are BOTH visible in their '
                                       'own crossing, so the pair resolves two ways at once. This '
                                       'is what a weave does and it is not an order.' % (i, j))
        ncross += 1
        edges[(i, j)] = top
    # cycle check by Kahn, and uniqueness by "exactly one source at every step"
    succ = {i: set() for i in live}
    indeg = {i: 0 for i in live}
    for (i, j), top in edges.items():
        under = j if top == i else i
        if under not in succ[top]:
            succ[top].add(under)
            indeg[under] += 1
    seq = []
    unique = True
    avail = sorted([i for i in live if indeg[i] == 0])
    while avail:
        if len(avail) > 1:
            unique = False
        v = avail[0]
        seq.append(v)
        for u in sorted(succ[v]):
            indeg[u] -= 1
            if indeg[u] == 0:
                avail.append(u)
        avail = sorted([u for u in avail[1:]])
    if len(seq) != len(live):
        return False, seq, ncross, 'CYCLE — the precedence graph is not an order (this is a weave)'
    if not unique:
        return False, seq, ncross, 'order not total — some bands never meet, so they cannot be ranked'
    return True, seq, ncross, 'consistent, acyclic, total'


def dump_cells():
    legend = {R_RIVET: '@', R_LIP: '+', R_FACE: '#', R_BSHADE: ',',
              R_PLATE: '-', R_SHADE: ':', R_DEEP: '.'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    allpass = True
    for label, comp in cases:
        role, owner, bands, over = role_field(comp)
        ok, seq, ncross, why = order_of(bands, over)
        cov = float((owner >= 0).sum()) / max(1, int(comp.sum()))
        print('== %s   area=%d bands=%d framed=%s'
              % (label, int(comp.sum()), sum(1 for b in bands if b is not None),
                 _has_interior(comp)))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        allpass = allpass and ok
        print('   crossings=%d  band coverage=%.0f%%  reading (first laid -> last) = %s'
              % (ncross, 100 * cov, ' < '.join(str(s) for s in seq)))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL'))

    # the WEAVE control, on the real torso, to show the failure is real and not rhetorical
    comp = cases[1][1]
    _, _, wb, wo = role_field(comp, weave=True)
    wok, wseq, wn, wwhy = order_of(wb, wo)
    print('== CONTROL: the same torso woven (over/under alternating)')
    print('   crossings=%d  -> %s  (%s)' % (wn, 'PASS' if wok else 'FAIL', wwhy))
    # and the cycle itself, stated from the weave's own rule rather than from its pixels, so the
    # failure is visible as an algebraic fact and not just as a rendering accident
    live = [k for k, b in enumerate(wb) if b is not None]
    rel = []
    for i in live:
        for j in live:
            if i < j:
                top = min(i, j) if (i + j) % 2 == 0 else max(i, j)
                rel.append('%d over %d' % (top, i if top == j else j))
    print('   the weave rule itself: %s  -> follow it round and it closes on itself; there is no'
          ' first band.' % ', '.join(rel))
    print('legend: @ rivet  + lit lip  # band face  , shadow ON A BAND  - plate  : shadow on plate'
          '  . deep plate')
    print('ACCEPTANCE (the algebra of a relation, not a statistic): every crossing consistent, the')
    print('precedence graph acyclic, and the order TOTAL — one unique sequence in which the bands')
    print('were laid, readable off the pixels. A cycle is the 30th cable/39th guilloche; a')
    print('non-total order is a stack of bands that never meet and has nothing to say.')
    print('OVERALL: %s' % ('ALL PASS' if allpass and not wok else 'FAIL'))
    return allpass and not wok


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
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
