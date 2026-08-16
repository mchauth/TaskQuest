#!/usr/bin/env python3
"""SIXTY-SECOND net-new-geometry axis for ALL FOUR SLOTS — the VERMICULE family: the piece is ruled
into square cells, every cell is one of exactly TWO tiles, each tile is a pair of quarter-turns, and
every quarter-turn meets the cell edge at the SAME POINT — the middle. Nothing else is specified.
What appears is a population of long wandering inlaid cords, and not one of them is drawn anywhere
in this file.

    the ornament is  CORD    (the inlaid wire — a bright second metal laid into the ground)
                   + SHADE   (the one row under a cord, where the ground drops away from it)
                   + GROUND  (the dark field the wire is laid into)

*** THIS IS THE FIRST AXIS WHOSE ORNAMENT IS NOT DRAWN. ONLY ITS JOINTS ARE. ***
Every one of the sixty-one before it draws its element. The 11th draws a flute, the 40th a tooth,
the 41st a bead, the 46th a shard, the 50th a rune, the 53rd a granule, the 54th a wire it routes
itself end to end, the 61st a hoop. In each case there is a place in the generator where the element
exists as an object: it has a start, a length, a centre, a size, and the code computes them.

There is no such place in this file. This generator writes TILES. A cord — the thing you actually
see, the wandering line four or forty pixels long that crosses the plate and comes back — is never
represented here at all. It has no variable, no length, no origin, no route. It exists only in the
finished picture, as a consequence of two neighbours having agreed at their shared edge. Ask this
generator how long the cords are and it does not know; the acceptance test has to TRACE them off the
pixels to find out, which is a new kind of reading and the reason clause POPULATION exists.

*** THE RULE IS LOCAL AND THE PROPERTY IS GLOBAL, AND THAT IS THE WHOLE POINT. ***
The rule is: a quarter-turn meets the cell edge at the middle. That is a statement about ONE edge,
five pixels long, and it is the only thing this ornament is told. From it, continuity across an
entire cuirass follows for free — every turn that arrives at an edge meets the turn arriving from
the other side, because both are at the middle, and neither cell was consulted about the other. The
cords are as long as they are, and nobody chose it.

This is exactly what the 54th LABYRINTH is not, and the pair is worth stating precisely because they
are the two axes in the set that both come out as wandering line. The 54th AUTHORS one wire: it is
routed deliberately, end to end, it is ONE object, and its acceptance is a topology — one component,
two terminal beads. This one authors NOTHING. It has many cords, it does not know how many, no cord
has an end inside the plate (every one either closes into a loop or leaves at the silhouette), and
its acceptance is that a LOCAL RULE HELD EVERYWHERE, audited by tracing what the rule produced.
The 54th is a drawing. This is a rule that happens to draw.

*** THE ACCEPTANCE TEST IS A NEW KIND: A LOCAL RULE, AUDITED GLOBALLY. ***
The 54th is accepted on a topology, the 55th on the algebra of an order, the 56th on a conservation
law read along a traversal, the 57th on a physical law, the 58th on a group action, the 59th on a
census of a group, the 60th on the complexity of a formal language, the 61st on a similarity across
sizes. Every one of those is a property of the finished picture, checked against a specification of
the finished picture. This one checks a picture against a specification that never mentions the
picture: the rule is about a five-pixel edge, and the evidence for it is a cuirass.

    (1) MATCHED       every interior cell edge whose crossing pair is on the body carries the
                      crossing — both pixels cord, at the middle of the edge and nowhere else.
                      This is the rule itself, and it is the only thing the generator was told.
                      SLIPPED and FREEHAND fail here.
    (2) DEGREE        every cord pixel with a fully on-body neighbourhood has EXACTLY two cord
                      neighbours. No forks, no dead ends, no crossings: the cords are simple
                      curves. This is not asked of the tiles, it is asked of what they made, and
                      it is the clause that says the tile alphabet is closed under joining.
                      FREEHAND fails here, badly and interestingly.
    (3) ORIGINLESS    the tile field, READ BACK OFF THE PIXELS, is balanced between the two tiles
                      and has no periodicity: max normalised autocorrelation over every nonzero
                      lag below threshold. Without this an axis satisfying (1) and (2) can be a
                      plain diagonal twill. PERIODIC, UNIFORM and ROWWISE fail here and only here.
    (4) CANONICAL     the umbrella: pixel for pixel, every painted role is the role the tile field
                      puts there. It implies 1 and 2, and is stated separately because a test that
                      only reports its umbrella cannot say WHAT went wrong.
    (5) POPULATION    a BATCH clause, and the one that has to trace. Over the batch the cords have
                      a spread of lengths and at least one of them CLOSES — a cord with no end at
                      all, which is the plainest evidence there is that no one drew it. UNIFORM
                      passes 1, 2 and 4 and fails this: its cords are all the same cord.

*** THE FIVE CONTROLS. TWO OF THEM ARE REAL ORNAMENTS AND ONE OF THEM IS THIS AXIS MISSED BY ONE
    PIXEL. ***
    UNIFORM     every cell the same tile. Passes MATCHED, DEGREE and CANONICAL — it is a perfectly
                legal edge-matched field — and fails ORIGINLESS and POPULATION. It is the 16th
                TWILL: parallel diagonal ribbons, all congruent. This is the axis's lower collapse
                boundary and it is not a straw man, it is a shipped axis.
    PERIODIC    tile = (cy + cx) odd. Also perfectly matched, also continuous, and it is the
                classical Truchet chequer: closed rings, the same ring everywhere. Fails
                ORIGINLESS at lag (1,1) with autocorrelation 1.0. THE CONTROL THE AXIS EXISTS
                AGAINST — it is what anyone doing this would write first, and everything about it
                is right except that it has an origin.
    ROWWISE     the tile chosen per ROW and held along it. Balanced, aperiodic down the piece,
                perfectly periodic across it — it fails ORIGINLESS on the x lags only, which is
                why the clause has to look at both axes and not at a single scalar.
    SLIPPED     THE SHARPEST NEAR MISS, AND THE REASON THIS AXIS IS ABOUT ITS EDGES. Same two
                tiles, same random field, same everything — except each cell's turns meet the edge
                one pixel off the middle, jittered per cell. It looks like the axis. Every cord in
                it is in pieces. Continuity is not a property of what the turns look like; it is a
                property of WHERE THEY MEET, and one pixel is the whole of it.
    FREEHAND    cords as independent random walks at the same density, no tile set at all. Fails
                MATCHED and DEGREE: walks cross each other into forks and stop in the middle of the
                plate into dead ends. It exists to say that "wandering lines" is not the axis. The
                alphabet is the axis; the wandering is what the alphabet does.

*** THE PRICE, AND IT IS ONE NO OTHER AXIS IN THE SET PAYS. THE ORNAMENT CANNOT BE ALIGNED. ***
Every other axis can be phased. The 11th's flutes can be slid half a pitch to sit symmetric on a
sternum; the 44th's chevron can be centred; the 60th's word can be started at whatever letter makes
the plate balance. Phase is the one dial they all have. This axis has no phase, because it has no
origin: move the lattice one cell and you do not get this pattern shifted, you get A DIFFERENT
PATTERN — the cells now hash to different tiles and every cord in the piece is rerouted. There is
nothing to slide.

The consequence, stated plainly rather than hidden: THIS IS THE FIRST AXIS THAT CANNOT BE MADE
SYMMETRIC ABOUT THE STERNUM, and it never will be. On an axis with a motif that is a defect; here
it is the claim. A damascened ground is not laid out, it is filled, and a filled ground that came
out symmetric would be evidence somebody had drawn it.

A second price, smaller and worth naming because it constrains the geometry rather than the look:
THE CELL MUST BE ODD. An even cell has no centre row, so its two quarter-turns are not mirror images
about the centre and they collide — measured, not asserted: at CELL=4 the tile pair puts 48 pixels
of a 6x6 field at degree 3, and at CELL=6, 38. At CELL=5 it is 0. The axis does not have a free
scale parameter; it has odd ones.

*** DISTINCTNESS. ***
  * 54th LABYRINTH — see above. One authored wire with two ends, accepted on a topology; this is an
    unauthored population with no ends, accepted on a local rule. They are the same picture arrived
    at from opposite directions and the difference is the whole of both axes.
  * 16th TWILL / 29th HOUNDSTOOTH — diagonal ribbon fields. They are the UNIFORM control exactly,
    which is how this axis states its lower boundary rather than pretending it has none.
  * 39th GUILLOCHE / 30th CABLE — braided ribbons that go OVER and UNDER. Those are authored
    interlaces with a fixed repeat and a stated crossing order; nothing here ever crosses anything,
    by clause DEGREE.
  * 46th CRAQUELURE — the other axis in the set with no repeating unit. Its aperiodicity is in the
    CELL SHAPES (a Voronoi of jittered sites) and its acceptance is a statistic over them. Here
    every cell is one of two shapes and identical in size; the aperiodicity is entirely in the
    ORDER, and the acceptance is not a statistic at all but a rule that must hold everywhere.
  * 51st FLOWGRAIN — a continuous director field with defects. It is computed pointwise: ask it the
    direction at (x, y) and it answers. Ask this axis which cord a pixel is on and it cannot answer
    without walking to the silhouette.
  * 60th CADENCE — a formal language, where the ORDER of two widths is the ornament. The nearest
    prior claim, and the distinction is locality again: cadence's word is one global sequence and
    every plate is a window on the same one, which is why adaptation is forbidden there. Here there
    is no sequence at all, only a rule about a shared edge, and two plates that never touch have
    nothing in common but the rule.

Geometry, in FRAME coordinates so the lattice is common to every component of a frame:
    cell      CELL x CELL, CELL odd. Edge midpoints at (0,m), (CELL-1,m), (m,0), (m,CELL-1).
    tiles     TILE 0 joins N-W and S-E; TILE 1 joins N-E and S-W. Each turn is a 4-connected
              staircase hugging its own corner, so the two turns of a tile never touch.
    field     tile = one bit of a hash of the CELL COORDINATES only. Not of the sheet, not of the
              class, not of the frame — so male and female of an item are identical, the pattern
              does not crawl under the animation, and the ornament is common to every piece of a
              suit the way a damascened ground would be.
    relief    a cord pixel is CORD; the pixel directly under a cord pixel is SHADE; everything else
              is GROUND. One row of shade, because the wire is one row proud.

Authoring philosophy identical to gen_canon_axis61.py / gen_cadence_axis60.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed, silhouette
untouched, so the generator cannot create isolated pixels, background bleed, extra components or a
changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Eighteenth generator to call it in-line, after axes 45-61.

Run from repo root:
  python3 scripts/gen_vermicule_axis62.py
  python3 scripts/gen_vermicule_axis62.py --tiles    # the alphabet, the odd-cell proof, the field
  python3 scripts/gen_vermicule_axis62.py --cells    # ASCII dump of real components + the clauses
  python3 scripts/gen_vermicule_axis62.py --accept   # the clauses over every component, 24 sheets
  python3 scripts/gen_vermicule_axis62.py --swatch   # bare cording on test plates
  python3 scripts/gen_vermicule_axis62.py --sweep    # slots + visor + the five controls
Then QA (examples):
  python3 scripts/sprite_qa.py _vermicule_legendary_preview/shirt_warrior_legendary62.png
  python3 scripts/sprite_qa.py _vermiculedome_helmet_preview/helmet_mage_legendary62.png --y-min 2
  python3 scripts/sprite_qa.py _vermicule_boots_preview/boots_warrior_legendary_vermicule.png \
      --y-max 63
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

# THE CELL. Odd, and it has to be — see the module docstring and tile_report(). Five is the smallest
# odd cell whose quarter-turn has a bend in it at all: at CELL=3 the turn is a bare corner pixel and
# the field degenerates to the 14th LATTICE, which was measured and rejected before this was written.
CELL = 5
assert CELL % 2 == 1, 'the cell must be odd or the two turns of a tile collide'
MID = CELL // 2
BEND = MID - 1

# THREE roles. The ground is dark and the cord is a second, brighter metal, and that is deliberate
# rather than the one-ramp relief of the 61st: this axis's whole claim is that a LINE runs
# uninterrupted across a plate, and a line the eye has to infer from relief alone is a line the
# claim cannot be checked on. Vermiculé is an inlay; inlay is two metals.
R_CORD, R_GROUND, R_SHADE = 0, 1, 2
ROLENAME = {R_CORD: 'CORD', R_GROUND: 'GROUND', R_SHADE: 'SHADE'}

# The seed is a constant of the axis, not of a sheet. Male and female of an item must hash the same
# (the finishing-pass rule) and a suit should read as one ground, so nothing about the sheet, the
# class, the slot or the frame enters here. Only the cell's coordinates.
SEED = 0x5645524D


# --- the alphabet ----------------------------------------------------------------------------
def tile_bit(cy, cx):
    """Which of the two tiles cell (cy, cx) carries. A hash, and deliberately nothing else.

    It is worth being exact about what is and is not claimed. The BIT is a function of position:
    it has to be, or the sheet would not regenerate identically and male and female of an item
    would differ. What is not a function of position — what is not computed anywhere in this file —
    is the CORD. Clause ORIGINLESS is the honest form of the claim: the bit field carries no
    periodicity, so no cord can be predicted from a coordinate without tracing its neighbours out
    to the silhouette.
    """
    h = ((cy * 0x9E3779B1) ^ (cx * 0x85EBCA77) ^ SEED) & 0xFFFFFFFF
    h ^= h >> 15
    h = (h * 0x2C1B3C6D) & 0xFFFFFFFF
    h ^= h >> 12
    h = (h * 0x297A2D39) & 0xFFFFFFFF
    h ^= h >> 15
    return h & 1


def _stair(a, b, corner):
    """A 4-connected staircase from a to b that hugs `corner`. Four-connected and not an arc.

    A true circular quarter-arc is prettier and is wrong here: at this radius it is 8-connected, so
    two of its pixels touch only diagonally, and a cord that is only diagonally connected cannot be
    traced or degree-counted under the repo's own connectivity convention (label4, sprite_qa, the
    auto-fixer are all 4-connected). The ornament is measured under the same connectivity the rest
    of the pipeline uses, which is worth one slightly squarer corner.
    """
    pts = [a]
    y, x = a
    (by, bx), (cy, cx) = b, corner
    for tgt, axis in ((cy, 'y'), (cx, 'x'), (by, 'y'), (bx, 'x')):
        while (y if axis == 'y' else x) != tgt:
            if axis == 'y':
                y += 1 if tgt > y else -1
            else:
                x += 1 if tgt > x else -1
            if (y, x) not in pts:
                pts.append((y, x))
    return pts


def tiles(cell=CELL, slip=0):
    """The two tiles, as pixel lists in cell-local coordinates.

    `slip` is the SLIPPED control and it is the only parameter: it moves the point at which every
    turn meets the cell edge off the middle. Everything else about the tile is untouched, which is
    what makes it the sharpest control in the set — the alphabet still has two letters, the letters
    still look like quarter-turns, and nothing joins.
    """
    m = cell // 2
    m2 = min(max(m + slip, 1), cell - 2)
    N, S, W, E = (0, m2), (cell - 1, m2), (m2, 0), (m2, cell - 1)
    kA = max(m - 1, 1)
    kB = cell - 1 - kA
    return {
        0: _stair(N, W, (kA, kA)) + _stair(S, E, (kB, kB)),
        1: _stair(N, E, (kA, cell - 1 - kA)) + _stair(S, W, (kB, cell - 1 - kB)),
    }


CONTROLS = ('uniform', 'periodic', 'rowwise', 'slipped', 'freehand')


def field_bit(cy, cx, mode=None):
    """The tile field, for the axis (mode=None) and for the three field controls."""
    if mode == 'uniform':
        return 0
    if mode == 'periodic':
        return (cy + cx) & 1
    if mode == 'rowwise':
        return tile_bit(cy, 0)
    return tile_bit(cy, cx)


def cord_mask(shape, mode=None):
    """The cord, over a whole frame. Painted later only where the body already is."""
    h, w = shape
    c = np.zeros((h, w), dtype=bool)
    if mode == 'freehand':
        return _freehand_mask(shape)
    base = tiles()
    for cy in range(h // CELL + 2):
        for cx in range(w // CELL + 2):
            T = tiles(slip=(1 if ((cy * 7 + cx * 13) & 1) else -1)) if mode == 'slipped' else base
            for dy, dx in T[field_bit(cy, cx, mode)]:
                y, x = cy * CELL + dy, cx * CELL + dx
                if 0 <= y < h and 0 <= x < w:
                    c[y, x] = True
    return c


def _freehand_mask(shape):
    """The FREEHAND control: independent random walks at the axis's own density, no tile set.

    It is the control that answers "isn't this just squiggles?". The squiggles are here, at the same
    coverage, and they fork where two walks touch and stop where a walk ends. Both are visible in
    the DEGREE count and neither can happen to the axis.
    """
    h, w = shape
    c = np.zeros((h, w), dtype=bool)
    want = int(0.40 * h * w)
    rng = np.random.RandomState(SEED & 0xFFFF)
    while c.sum() < want:
        y, x = rng.randint(h), rng.randint(w)
        for _ in range(rng.randint(6, 30)):
            c[y, x] = True
            dy, dx = ((0, 1), (0, -1), (1, 0), (-1, 0))[rng.randint(4)]
            y, x = min(max(y + dy, 0), h - 1), min(max(x + dx, 0), w - 1)
    return c


def roles_of(shape, body, mode=None):
    """Role per pixel over a frame: CORD, the SHADE row under it, GROUND everywhere else."""
    cord = cord_mask(shape, mode) & body
    below = np.zeros_like(cord)
    below[1:, :] = cord[:-1, :]
    shade = below & body & ~cord
    r = np.full(shape, R_GROUND, dtype=np.int8)
    r[shade] = R_SHADE
    r[cord] = R_CORD
    return r, cord


# --- palette --------------------------------------------------------------------------------
# Two metals per class: a dark GROUND and a bright CORD laid into it, plus the one shade row that
# makes the wire sit proud. Chosen against the neighbours it will be seen beside — the 60th took
# brass / moonstone / verdigris, the 61st crimson steel / amethyst / deep teal:
#   warrior  NIELLO        silver wire in blackened blue-grey steel
#   mage     GOLD ON PLUM  gold wire in a plum ground — the strongest read of the three
#   ranger   WHEAT ON OLIVE pale wheat wire in olive bronze, yellow-green and clear of both the
#                          60th's verdigris and the 61st's teal
#
# NO STOP NEAR PURE BLACK: the finishing pass carves the visor as black eye and mouth pixels and a
# near-black darkest stop swallows them (the 49th's lesson). Darkest channel-sums 206 / 202 / 202.
#
# The 61st's lesson applied without having to relearn it: the finishing pass LIFTS a sheet before
# anything else touches it, so every stop here was picked one step darker than it looked right in
# the swatch, and the grounds were darkened again after the first render came back washed — a
# ground and a cord too close in value turn a continuous line into a dotted one, which on this axis
# would be a palette destroying the only thing the axis has to say.
VERMPAL = {
    'warrior': ((222, 228, 240), (88, 100, 126), (56, 64, 86)),
    'mage':    ((250, 222, 150), (128, 72, 124), (78, 44, 80)),
    'ranger':  ((236, 240, 206), (100, 116, 66), (70, 82, 50)),
}

# Per-class body tones for the plain recolor, visible on sleep frames and on components too small
# to carry the cording.
BODY = {
    'warrior': ((56, 64, 86), (88, 100, 126), (222, 228, 240)),
    'mage':    ((78, 44, 80), (128, 72, 124), (250, 222, 150)),
    'ranger':  ((70, 82, 50), (100, 116, 66), (236, 240, 206)),
}

SLOTS = {
    'chest': dict(
        outdir='_vermicule_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary62', largest=True,
    ),
    'legs': dict(
        outdir='_vermicule_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary62', largest=False,
    ),
    'boots': dict(
        outdir='_vermicule_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_vermicule', largest=False,
    ),
    'helmet': dict(
        outdir='_vermiculedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary62', largest=True,
    ),
}


# --- painting -------------------------------------------------------------------------------
def paint_vermicule(fr, comp_full, stops, mode=None):
    """Lay the cording onto one component. Only opaque body pixels are ever painted, so this cannot
    create strays and cannot change the silhouette.

    Note what is NOT here: no loop over cords, no length, no route, no start. The function paints
    tiles and stops. The cords are what is left over."""
    if comp_full.sum() < MIN_PX:
        return None
    r, cord = roles_of(comp_full.shape, comp_full, mode)
    for y, x in np.argwhere(comp_full):
        fr[y, x, :3] = stops[int(r[y, x])]
        fr[y, x, 3] = 255
    return dict(area=int(comp_full.sum()), cord=int((cord & comp_full).sum()), shape=comp_full.shape)


# --- reading the cording back off the painted pixels ------------------------------------------
def read_roles(fr, comp_full, stops):
    """Read the roles off the PAINTED PIXELS. The acceptance test is run on what is ON THE SHEET.

    Every stop is distinct in all three channels and no role is ever one pixel wide in isolation,
    so this is a measurement and not an estimate — there is no censored sample here, unlike the
    60th, and no estimator to correct.
    """
    got = np.full(comp_full.shape, -1, dtype=np.int8)
    ys, xs = np.nonzero(comp_full)
    px = fr[ys, xs, :3].astype(np.int32)
    pal = np.array(stops, dtype=np.int32)
    got[ys, xs] = ((px[:, None, :] - pal[None, :, :]) ** 2).sum(-1).argmin(1)
    return got


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — a LOCAL RULE, AUDITED GLOBALLY.
#
#   (1) MATCHED     every interior cell edge whose crossing pair is on the body carries the
#                   crossing. The rule itself, and the only thing the generator was told.
#   (2) DEGREE      every cord pixel with a fully on-body neighbourhood has exactly two cord
#                   neighbours. Asked of what the tiles MADE, not of the tiles.
#   (3) ORIGINLESS  the tile field read back off the pixels is balanced and has no periodicity.
#   (4) CANONICAL   pixel for pixel the painted role is the role the tile field puts there.
#   (5) POPULATION  batch clause: the cords have a spread of lengths and at least one CLOSES.
#
# *** WHAT IS DELIBERATELY NOT A CLAUSE. *** None of this is asked of the finished sheet after
# sprite_finish has run, for the 57th's, 60th's and 61st's reason: the light comes from outside the
# ornament. The finishing pass adds a visor, pauldron caps and a directional shade, none of which is
# part of the rule.
#
# *** AND WHY PIXELS AT THE SILHOUETTE ARE EXEMPT FROM DEGREE RATHER THAN COUNTED AS FAILURES. ***
# A cord that reaches the edge of the plate leaves it. That is not a dead end, it is the piece
# ending, and counting it as one would make the clause a measurement of how ragged the silhouette
# is. The exemption is exactly "the 4-neighbourhood is fully on-body" and nothing looser; it is the
# same reason the 60th refused to score reeds the silhouette had cut in half.
# ---------------------------------------------------------------------------------------------
AUTOCORR_MAX = 0.50
BALANCE = (0.35, 0.65)
POP_LENGTHS = 8


def _crossings(shape):
    """Every interior cell edge, as the pair of pixels that must both be cord if the rule held."""
    h, w = shape
    out = []
    for cy in range(h // CELL + 1):
        for cx in range(w // CELL + 1):
            y0, x0 = cy * CELL, cx * CELL
            a, b = (y0 - 1, x0 + MID), (y0, x0 + MID)             # horizontal edge, N of the cell
            if 0 <= a[0] and b[0] < h and x0 + MID < w:
                out.append((a, b))
            a, b = (y0 + MID, x0 - 1), (y0 + MID, x0)             # vertical edge, W of the cell
            if 0 <= a[1] and b[1] < w and y0 + MID < h:
                out.append((a, b))
    return out


def _trace(cord):
    """Trace the cords off the pixels: returns (lengths, n_closed).

    This function exists because nothing else in this file knows what a cord is. It is the only
    place in the generator where a cord becomes an object, and it is in the TEST, which is the whole
    claim of the axis stated as a fact about its own source code.
    """
    h, w = cord.shape
    seen = np.zeros_like(cord)
    lengths, closed = [], 0
    for sy, sx in np.argwhere(cord):
        if seen[sy, sx]:
            continue
        stack, comp = [(sy, sx)], []
        seen[sy, sx] = True
        while stack:
            y, x = stack.pop()
            comp.append((y, x))
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and cord[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    stack.append((ny, nx))
        lengths.append(len(comp))
        ends = 0
        for y, x in comp:
            d = sum(1 for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                    if 0 <= ny < h and 0 <= nx < w and cord[ny, nx])
            if d < 2:
                ends += 1
        if ends == 0 and len(comp) >= 4 * CELL:
            closed += 1
    return lengths, closed


def read_field(got, comp_full):
    """Read the TILE FIELD back off the painted pixels.

    Tile 0 puts a cord pixel at cell-local (BEND, BEND) and tile 1 at (BEND, CELL-1-BEND). Those
    two are never both cord, so one look at each tells which letter is there — a cell is only read
    where both probes are on the body, so a cell the silhouette has clipped is not guessed at.
    """
    h, w = comp_full.shape
    out = {}
    for cy in range(h // CELL + 1):
        for cx in range(w // CELL + 1):
            p0 = (cy * CELL + BEND, cx * CELL + BEND)
            p1 = (cy * CELL + BEND, cx * CELL + CELL - 1 - BEND)
            if not (0 <= p0[0] < h and 0 <= p0[1] < w and 0 <= p1[1] < w):
                continue
            if not (comp_full[p0] and comp_full[p1]):
                continue
            a, b = got[p0] == R_CORD, got[p1] == R_CORD
            if a != b:
                out[(cy, cx)] = 0 if a else 1
    return out


def autocorr(field):
    """Max normalised autocorrelation of the tile field over every nonzero lag it can measure.

    +-1 per cell rather than 0/1, so a perfectly balanced field has mean zero and the statistic is
    a correlation and not a coincidence rate. Lags with fewer than MIN_PAIRS overlapping cells are
    not reported, because a lag measured on three cells is noise wearing the clause's clothes.
    """
    MIN_PAIRS = 6
    if len(field) < 12:
        return None, None
    v = {k: (1 if b else -1) for k, b in field.items()}
    best, at = 0.0, None
    for ly in range(-3, 4):
        for lx in range(-3, 4):
            if (ly, lx) == (0, 0):
                continue
            pairs = [(v[k], v[(k[0] + ly, k[1] + lx)]) for k in v
                     if (k[0] + ly, k[1] + lx) in v]
            if len(pairs) < MIN_PAIRS:
                continue
            c = abs(sum(a * b for a, b in pairs) / float(len(pairs)))
            if c > best:
                best, at = c, (ly, lx)
    return best, at


def accepts_component(got, comp_full, mode=None):
    """Clauses 1, 2 and 4 on ONE COMPONENT, plus the material clauses 3 and 5 need.

    ALL failing clauses are reported, not just the first — the 61st's lesson: a test that reports
    the first thing it trips over is reporting the order of its own source code.
    """
    failed, why = [], []
    h, w = comp_full.shape
    cord = (got == R_CORD)

    # (1) MATCHED — the rule itself, on every interior edge the body actually covers.
    tot = bad = 0
    for a, b in _crossings(comp_full.shape):
        if not (comp_full[a] and comp_full[b]):
            continue
        tot += 1
        if not (cord[a] and cord[b]):
            bad += 1
    if bad:
        failed.append('MATCHED')
        why.append('%d of %d on-body cell edges do not carry the crossing' % (bad, tot))

    # (2) DEGREE — no forks, no dead ends, no crossings, on pixels the silhouette has not clipped.
    forks = ends = interior = 0
    for y, x in np.argwhere(cord):
        nb = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        if not all(0 <= ny < h and 0 <= nx < w and comp_full[ny, nx] for ny, nx in nb):
            continue
        interior += 1
        d = sum(1 for ny, nx in nb if cord[ny, nx])
        if d > 2:
            forks += 1
        elif d < 2:
            ends += 1
    if forks or ends:
        failed.append('DEGREE')
        why.append('%d fork%s and %d dead end%s among %d interior cord pixels'
                   % (forks, '' if forks == 1 else 's', ends, '' if ends == 1 else 's', interior))

    # (4) CANONICAL — the umbrella: pixel for pixel, the painted role is the role the field puts
    # there. For a control this is asked against the CONTROL's own field, so a control cannot fail
    # it by being itself; every control below fails on the clauses that are about the axis.
    want, _ = roles_of(comp_full.shape, comp_full, mode)
    off = int(((got != want) & comp_full).sum())
    if off:
        failed.append('CANONICAL')
        why.append('%d of %d body pixels carry a role the tile field does not put there'
                   % (off, int(comp_full.sum())))

    field = read_field(got, comp_full)
    lengths, closed = _trace(cord & comp_full)
    if failed:
        return False, sorted(set(failed)), '; '.join(why), field, lengths, closed
    return True, [], ('%d on-body cell edges all crossed, %d interior cord pixels all of degree 2'
                      % (tot, interior)), field, lengths, closed


def originless(field):
    """Clause 3, over a pooled tile field. Returns (ok, lines)."""
    lines = []
    if len(field) < 12:
        return False, ['   tile field too small to test (%d cells)' % len(field)]
    ones = sum(1 for v in field.values() if v)
    bal = ones / float(len(field))
    c, at = autocorr(field)
    okb = BALANCE[0] <= bal <= BALANCE[1]
    okc = c is not None and c <= AUTOCORR_MAX
    lines.append('   tile field %d cells   balance %.3f (want %.2f..%.2f) -> %s'
                 % (len(field), bal, BALANCE[0], BALANCE[1], 'PASS' if okb else 'FAIL'))
    lines.append('   max |autocorrelation| over nonzero lags %.3f at lag %s (want <= %.2f) -> %s'
                 % (c if c is not None else -1, at, AUTOCORR_MAX, 'PASS' if okc else 'FAIL'))
    return (okb and okc), lines


def population(lengths, closed):
    """Clause 5, over the batch. Returns (ok, lines)."""
    lines = []
    n = len(set(lengths))
    ok = (n >= POP_LENGTHS) and (closed >= 1)
    lines.append('   %d cords traced, %d distinct lengths (want >= %d), %d .. %d px'
                 % (len(lengths), n, POP_LENGTHS,
                    min(lengths) if lengths else 0, max(lengths) if lengths else 0))
    lines.append('   cords that CLOSE (no end at all): %d (want >= 1) -> %s'
                 % (closed, 'PASS' if ok else 'FAIL'))
    return ok, lines


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


def build(base, cfg, cls, mode=None):
    D, M, L = BODY[cls]
    stops = VERMPAL[cls]
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
        # ONE LATTICE PER FRAME, NOT ONE PER COMPONENT — and on this axis that is forced, where on
        # the 61st the opposite was forced. The 61st divides an EXTENT, so two chausse legs are two
        # extents and must be hooped separately. Here the ornament is a GROUND, common to the whole
        # suit; giving each leg its own lattice would give each leg its own origin, and the one
        # thing this axis does not have is an origin.
        for comp in comps_of(a, largest):
            paint_vermicule(fr, comp, stops, mode=mode)
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
        m[1:4, int(cx) - 2:int(cx) + 3] = False
    return m


def _big_comp(arr, fi=0):
    r, c = fi // COLS, fi % COLS
    src = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def _degree_of_field(cell, mode=None, n=6):
    """Degree census of a bare n x n tile field at a given cell size, interior pixels only.

    This is the measurement behind "the cell must be odd". It is run, not asserted.
    """
    m = np.zeros((cell * n, cell * n), dtype=bool)
    T = tiles(cell)
    for cy in range(n):
        for cx in range(n):
            for dy, dx in T[field_bit(cy, cx, mode)]:
                m[cy * cell + dy, cx * cell + dx] = True
    bad = 0
    for y in range(1, cell * n - 1):
        for x in range(1, cell * n - 1):
            if m[y, x]:
                d = int(m[y - 1, x]) + int(m[y + 1, x]) + int(m[y, x - 1]) + int(m[y, x + 1])
                if d != 2:
                    bad += 1
    return bad, float(m.sum()) / m.size


def tile_report():
    """The alphabet, the odd-cell measurement, and the field statistics."""
    T = tiles()
    print('== THE ALPHABET   cell %dx%d, edge midpoints at row/col %d' % (CELL, CELL, MID))
    for b in (0, 1):
        grid = [['.'] * CELL for _ in range(CELL)]
        for y, x in T[b]:
            grid[y][x] = '#'
        print('   tile %d:' % b)
        for row in grid:
            print('      ' + ''.join(row))
    print()
    print('== THE CELL MUST BE ODD — degree census of a bare 6x6 field, interior pixels only')
    for c in (3, 4, 5, 6, 7):
        bad, dens = _degree_of_field(c)
        print('   cell %d   pixels at degree != 2: %-4d   coverage %.2f%s'
              % (c, bad, dens, '   <- the cell this axis uses' if c == CELL else
                 ('   (even: the two turns collide)' if c % 2 == 0 else '')))
    print()
    print('== THE FIELD   16x16 cells of the hash, and of the three field controls')
    for mode in (None, 'uniform', 'periodic', 'rowwise'):
        f = {(cy, cx): field_bit(cy, cx, mode) for cy in range(16) for cx in range(16)}
        ones = sum(f.values())
        c, at = autocorr(f)
        print('   %-9s balance %.3f   max |autocorr| %.3f at lag %s'
              % (mode or 'AXIS', ones / 256.0, c, at))


def dump_cells():
    """ASCII dump of real components, the clauses on each, then the five controls."""
    legend = {R_CORD: '#', R_SHADE: 'v', R_GROUND: '.', -1: ' '}
    cases = []
    for label, fname in (('warrior chest', 'armor_chest_4.png'),
                         ('mage chest', 'shirt_mage4.png'),
                         ('warrior legs', 'armor_pants_4.png'),
                         ('warrior helm', 'helmet_rare1.png'),
                         ('warrior boot', 'armor_boots_4.png')):
        a = _big_comp(load_any(fname))
        cases.append((label, a))

    stops = VERMPAL['warrior']
    allpass = True
    field, lens, closed = {}, [], 0
    for label, comp in cases:
        fr = np.zeros(comp.shape + (4,), dtype=np.uint8)
        info = paint_vermicule(fr, comp, stops)
        if info is None:
            print('== %s   too small to card (reported)' % label)
            continue
        got = read_roles(fr, comp, stops)
        ok, clauses, why, f, ln, cl = accepts_component(got, comp)
        ys, xs = np.nonzero(comp)
        y0, y1, x0, x1 = int(ys.min()), int(ys.max()), int(xs.min()), int(xs.max())
        print('== %s   area=%d  cord=%d px (%.0f%%)'
              % (label, info['area'], info['cord'], 100.0 * info['cord'] / info['area']))
        for y in range(y0, y1 + 1):
            print('   ' + ''.join(legend[int(got[y, x])] if comp[y, x] else ' '
                                  for x in range(x0, x1 + 1)))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL (%s)' % ', '.join(clauses)))
        allpass = allpass and ok
        field.update(f)
        lens += ln
        closed += cl

    print()
    print('== CLAUSE 3 — ORIGINLESS over the pooled tile field of the cases above')
    ook, lines = originless(field)
    for ln in lines:
        print(ln)
    print('== CLAUSE 5 — POPULATION over the cords traced from the cases above')
    pok, lines = population(lens, closed)
    for ln in lines:
        print(ln)
    allpass = allpass and ook and pok

    print()
    print('== THE FIVE CONTROLS, each over the same cases through the same code path')
    for m in CONTROLS:
        fails, clauses = [], set()
        cf, cl_, cc = {}, [], 0
        for label, comp in cases:
            fr = np.zeros(comp.shape + (4,), dtype=np.uint8)
            if paint_vermicule(fr, comp, stops, mode=m) is None:
                continue
            got = read_roles(fr, comp, stops)
            ok, cls_, why, f, ln, c2 = accepts_component(got, comp, mode=m)
            cf.update(f)
            cl_ += ln
            cc += c2
            if not ok:
                fails.append('%s: %s' % (label, why))
                clauses |= set(cls_)
        cok, _ = originless(cf)
        if not cok:
            clauses.add('ORIGINLESS')
        pk, _ = population(cl_, cc)
        if not pk:
            clauses.add('POPULATION')
        print('   %-10s fails on clause(s): %s' % (m, ', '.join(sorted(clauses)) or '-'))
        if fails:
            print('       e.g. %s' % fails[0])
        allpass = allpass and bool(clauses)
        if not clauses:
            print('       DID NOT FAIL - investigate')

    print()
    print('legend: # cord   v shade under a cord   . ground')
    print('ACCEPTANCE (a LOCAL RULE, AUDITED GLOBALLY — not a statistic, a topology, an algebra, a')
    print('conservation law, a physical law, a group action, a census, a formal language or a')
    print('similarity):')
    print('(1) MATCHED     every on-body cell edge carries the crossing at its middle;')
    print('(2) DEGREE      every interior cord pixel has exactly two cord neighbours;')
    print('(3) ORIGINLESS  the tile field read off the pixels is balanced and has no period;')
    print('(4) CANONICAL   pixel for pixel the role is the one the field puts there (implies 1,2);')
    print('(5) POPULATION  the cords have a spread of lengths and at least one of them CLOSES.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def swatch(path='_diag_vermicule_swatch.png', zoom=10):
    """The axis drawn: the cording on test plates, per class."""
    plates = [_test_plate(26, 30), _test_plate(16, 20), _test_plate(11, 13), _test_plate(9, 7)]
    pad = 4
    cw = max(p.shape[1] for p in plates) * zoom
    ch = max(p.shape[0] for p in plates) * zoom
    img = Image.new('RGBA', (pad + len(plates) * (cw + pad), pad + 3 * (ch + pad)), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        for j, m in enumerate(plates):
            a = np.zeros(m.shape + (4,), dtype=np.uint8)
            paint_vermicule(a, m, VERMPAL[cls])
            im = Image.fromarray(a).resize((m.shape[1] * zoom, m.shape[0] * zoom), Image.NEAREST)
            img.paste(im, (pad + j * (cw + pad), pad + k * (ch + pad)))
    img.save(path)
    print('wrote %s (cording only - no sheets written)' % path)


def sweep(path='_diag_vermicule_sweep.png', zoom=10):
    """A warrior chest, legs and boot under the axis and under the FIVE CONTROLS.

    SLIPPED is the one to look at: same alphabet, same field, the meeting point one pixel off, and
    every cord in the piece is in pieces."""
    cases = [('chest', _big_comp(load_any('armor_chest_4.png'))),
             ('legs', _big_comp(load_any('armor_pants_4.png'))),
             ('boot', _big_comp(load_any('armor_boots_4.png')))]
    cols = [None] + list(CONTROLS)
    stops = VERMPAL['warrior']
    crops = []
    for label, comp in cases:
        ys, xs = np.nonzero(comp)
        sub = comp[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        row = []
        for m in cols:
            a = np.zeros(sub.shape + (4,), dtype=np.uint8)
            paint_vermicule(a, sub, stops, mode=m)
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
    print('wrote %s   columns: VERMICULE, %s' % (path, ', '.join(CONTROLS)))


def slots_diag(path='_diag_vermicule_slots.png', zoom=8):
    """One idle frame of every slot and class, corded, before the finishing pass."""
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


def visor_diag(path='_diag_vermicule_visor.png', zoom=12):
    """The helmet head zone before and after the finishing pass — the visor must survive the
    cording, which is why no stop in the palette goes near black."""
    cfg = SLOTS['helmet']
    outs = []
    for cls, stem in cfg['srcs'].items():
        base = load_any('%s.png' % stem)
        arr = build(base, cfg, cls)
        raw = arr[16:40, 28:56].copy()
        fin, _ = finish_array(arr.copy(), 'helmet_%s_legendary62.png' % cls)
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
    ncomp = ncarded = nsmall = nfail = 0
    byclause = {}
    field, lens, closed = {}, [], 0
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            stops = VERMPAL[cls]
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
                            nsmall += 1
                            continue
                        ncomp += 1
                        paint_vermicule(fr, comp_full, stops)
                        got = read_roles(fr, comp_full, stops)
                        ok, clauses, why, f, ln, cl = accepts_component(got, comp_full)
                        field.update(f)
                        lens += ln
                        closed += cl
                        if not ok:
                            nfail += 1
                            for c2 in clauses:
                                byclause[c2] = byclause.get(c2, 0) + 1
                            if nfail <= 20:
                                print('   VIOLATION [%s] %s %s%s frame %d: %s'
                                      % (', '.join(clauses), kind, cls, suffix, fi, why))
                            continue
                        ncarded += 1
    ook, olines = originless(field)
    pok, plines = population(lens, closed)
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components                 %d' % ncomp)
    print('    carrying the cording     %d' % ncarded)
    print('    under %d px               %d   (too small to card; reported, not failed)'
          % (MIN_PX, nsmall))
    print('  clause 1-2-4 violations    %d%s' % (nfail,
          ('   ' + ', '.join('%s:%d' % (k, byclause[k]) for k in sorted(byclause)))
          if byclause else ''))
    print('  CLAUSE 3 — ORIGINLESS:')
    for ln in olines:
        print(ln)
    print('  CLAUSE 5 — POPULATION:')
    for ln in plines:
        print(ln)
    allpass = (nfail == 0) and ook and pok
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def main():
    if '--tiles' in sys.argv:
        tile_report()
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
