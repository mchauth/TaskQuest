#!/usr/bin/env python3
"""SIXTY-NINTH net-new-geometry axis for ALL FOUR SLOTS - the ANNEAL family: the plate is pinned at
a handful of points on its own outline and then LET GO, and the ornament is where it stopped.

    the ornament is  a RIB      one pixel of crest with a dark witness across the level it stands
                                on, drawn where the equilibrium changes band
    the fixture is   a POLE     one boundary pixel of the part, held at a fixed potential; there
                                are n of them, at n equal angles about the part's own centroid
    the law is       EVERY PIXEL THAT IS NOT A POLE IS THE MEAN OF ITS NEIGHBOURS

*** THIS IS THE FIRST INVARIANT THAT IS AN EQUILIBRIUM. ***
Sixty-eight axes are CONSTRUCTIONS. Somebody decided where the ornament went: a pitch (11th
FLUTING), a lattice (13th STUDWORK), a hung chain (57th FESTOON), a growth rule applied row after
row (65th CASCADE), a spanning tree of keys (66th DOVETAIL), a word that describes itself (67th
COLOPHON), a scatter with no repeated relation (68th SEME). In all sixty-eight the interior of the
plate is AUTHORED - if not pixel by pixel then rule by rule, and the rule is ours. Here nothing in
the interior is authored and there is nothing to author. n pixels of the outline are held, every
other pixel of the plate is free, and the ornament is the unique state in which no pixel has any
reason left to move. THE PLATE IS NOT DRAWN, IT IS SOLVED.

*** THE PAIR WITH THE 65th, WHICH IS ITS EXACT COMPLEMENT. ***
    the 65th CASCADE   the plate's vertical direction is a HISTORY. Every row is the image of the
                       row above under one fixed rule, the reader RECOVERS THE GENERATOR, and the
                       plate remembers exactly how it was made: flip one cell of the seed and the
                       damage runs to the hem.
    the 69th ANNEAL    the plate has NO history and cannot be given one. Start the relaxation from
                       zero, from noise, from the 47th's distance transform, from twenty different
                       random interiors - every one of them arrives at the same picture, pixel for
                       pixel, and clause AMNESIA is the measurement. THE ORNAMENT DOES NOT REMEMBER
                       HOW IT WAS MADE, BECAUSE NOTHING THAT HAPPENED TO IT ON THE WAY SURVIVED.
The 65th is a plate with a direction of time in it. This one is a plate in which time has run out.

*** THE ACCEPTANCE TEST IS A NEW KIND: A RECOMPUTATION. ***
Every reader before this one was handed a picture and asked a question about it - is this statistic
held, is this wire connected, do these hoops stand in 3:2:1, does this word describe itself. This
reader is handed the MASK, is told nothing else, and DRAWS THE ORNAMENT ITSELF. Then it demands the
plate. Not "is the plate lawful" but "is the plate THE ONE", and the answer is an image compared
pixel for pixel with an image. It is the first acceptance test in sixty-nine whose expected value is
not a predicate but a picture, and the first that could have produced the item it is inspecting.

    (1) RECOMPUTE    from the mask alone - no class, no palette, no poles, no band count - the
                     reader solves the equilibrium for every n it knows and derives the rib set.
                     EXACTLY ONE n may reproduce the plate, and that n is therefore an OUTPUT: THE
                     CLASS IS NOT TOLD TO THE READER, IT IS READ OFF THE ORNAMENT. Plates that
                     admit two n are counted and reported.
    (2) MEAN-VALUE   every free pixel of the solved field equals the average of its in-mask
                     neighbours, and no free pixel is a strict local maximum or minimum. The second
                     half is the discrete maximum principle and it is checked EXACTLY, with strict
                     integer comparisons and no tolerance: an ornament at equilibrium HAS NO
                     ISOLATED BRIGHT PIP ANYWHERE, which is a clause an eye can also check.
    (3) AMNESIA      the same plate re-relaxed from a zero start, from uniform noise, from the
                     distance transform and from three seeded random interiors. All six histories
                     must give the SAME RIBS. This is the clause that says the plate is a LIMIT and
                     not a process, and control HALFWAY is what a process looks like.
    (4) DEPENDENCE   one pole is raised by one and the plate is re-solved: EVERY FREE PIXEL MUST
                     MOVE. Not most of them, not the ones nearby - all of them, because on a
                     connected body at equilibrium the Green's function is strictly positive. THIS
                     IS THE CLAUSE THAT SEPARATES THIS AXIS FROM THE 47th: a contour of the distance
                     transform is a fact about a pixel's own neighbourhood and cannot hear a change
                     on the other side of the plate, and control DISTANCE scores 13175 deaf pixels
                     out of 13175 - the distinctness argument stated as a number instead of as an
                     opinion. The comparison is bit-for-bit and there is no tolerance in it. The one
                     exception is stated rather than hidden: a pixel with a SINGLE neighbour takes
                     that neighbour's value and nothing else's, so a hangnail hanging off a pole IS
                     that pole and is correctly deaf to the others; 557 such pixels are excluded and
                     counted. (A one-pixel SLIDE of a pole was the first draft of this clause and it
                     was a bad clause: 115 probes of 200 moved nothing at all, which measures the
                     coarseness of a band and not the reach of a field. It survives as a reported
                     number beside the clause: a pole slid one pixel moves 916 rib pixels, a third
                     of them in the far half of the part.)
    (5) LEGIBLE      every rib pixel is crest, carries a dark witness across its own level, and no
                     four rib pixels form a 2x2 block - a rib is a LINE and a blot is not a rib.
    (6) POLES        the n recovered by clause RECOMPUTE is the class's n on every plate of that
                     class - 838 of 838 - so the item names its own class and does not need a label.
                     Two plates in the batch are MUTE (a jumping warrior leaves four pixels of toe
                     and there is nothing there to anneal); a plate that says nothing is not asked
                     what class it is, and the count is reported.

*** THE EIGHT CONTROLS, AND WHAT EACH ONE IS FOR. ***
    DISTANCE   the bands taken from the distance transform instead of the equilibrium - that is,
               THE 47th MOKUME, drawn by this axis's painter, same relief, same palette, same pixel
               budget. THE HONEST NEAR MISS AND THE ONLY CONTROL THAT IS A PREVIOUS AXIS. It fails
               MEAN-VALUE, because the distance transform has a RIDGE down the middle of every limb
               and a ridge is a line of local maxima (683 violations); it is deaf on every pixel of
               clause DEPENDENCE; and 18 of its 24 sheets cannot be drawn at all. Its ribs are
               CLOSED CURVES that hug the outline. This axis's ribs are OPEN and run from
               rim to rim. They do not look alike and they are not alike, and the file measures both.
    HALFWAY    the relaxation stopped after 25 sweeps instead of run to equilibrium. AT 13px IT IS
               INVISIBLE. It is false, and it is false in the only way this axis can be false: it is
               a plate that was still moving. THE CONTROL THAT PROVES THE AXIS IS THE LIMIT AND NOT
               THE PROCESS, and the exact thing the 65th CASCADE is made of.
    LINEAR     a flat ramp between the two farthest poles. It IS harmonic, it passes MEAN-VALUE and
               it passes the maximum principle, and it is still not the plate: it is not the
               equilibrium OF THIS BODY, it is the equilibrium of a rectangle. AND ON A CONVEX PIECE
               WITH TWO POLES THE TWO COINCIDE - so LINEAR is where this axis DEGENERATES INTO THE
               11th FLUTING, and the amount by which the axis is not fluting is exactly the amount
               by which the body is not a box. The one control that is lawful in itself.
    PINNED     one interior pixel held at the crest value: a source. ONE PIXEL OF BROKEN LAW, the
               smallest violation this axis can express, 905 maximum-principle violations, and it
               was NOT CAUGHT AT ALL until the reader stopped being handed the painter's list of
               what was held. A reader that is told which pixels are poles will forgive any pin you
               like; a reader that derives the poles from the mask - which is all a reader can
               honestly do here - sees a bright pip in the middle of a field and knows an
               equilibrium cannot have one. THE FIRST DRAFT OF CLAUSE MEAN-VALUE SCORED THIS CONTROL
               ZERO, and that near miss is the reason the reader is told nothing anywhere else
               either.
    NOISE      the solved field jittered by a hair before it is banded. Fails the maximum principle
               and looks it: the ribs grow blots. What clause LEGIBLE is for.
    GROUNDED   the whole outline held at zero instead of left free, poles still driven. A perfectly
               respectable field that is not this one - the ribs pull off the rim and close into
               rings. THE CONTROL THAT SHOWS THE FREE RIM IS LOAD-BEARING: an insulated boundary is
               why a rib can END on the outline, and a rib that cannot end on the outline is a
               closed curve, and a closed curve is the 47th.
    SWAPPED    another class's n. IT FAILS NOTHING - it is a lawful annealed plate of the wrong
               class, and clause RECOMPUTE names the class it actually is. That is its finding: n is
               not a decoration on the law, IT IS THE WHOLE OF WHAT A CLASS IS HERE.
    ONEPOLE    n = 1. The equilibrium of a body with one held pixel and an insulated rim is the
               CONSTANT FIELD, and a constant field has no contour anywhere. NOT A PLATE IN
               TWENTY-FOUR SHEETS HAS A SINGLE RIB ON IT. It is DEAD rather than false, and it is
               the axis's minimum stated as a theorem: A POTENTIAL NEEDS A DIFFERENCE. You cannot
               make a picture out of one number, and no smaller pixel would have helped - the 66th
               missed a sabaton because a dovetail is four pixels across and one could imagine a
               smaller dovetail; nothing can be imagined smaller than two.

*** CLASS IDENTITY IS THE ORDER OF A MULTIPOLE. ***
    warrior   n = 2   a DIPOLE       one hot pole, one cold, and the ribs run across the piece
    ranger    n = 3   a TRIPOLE      one hot, two cool, and the ribs band the piece the short way
    mage      n = 4   a QUADRUPOLE   hot, neutral, cold, neutral - a saddle, and the ribs stand up
The pole values are cos(2*pi*j/n), so they sum to zero for every n and no class is secretly a
brighter version of another. Not a word (67th), not a ceiling (68th), not a rule (65th), not a graph
(66th) - AN INTEGER THAT IS THE NUMBER OF PLACES THE BODY IS HELD. And it is VISIBLE, which is rare:
the three classes do not merely obey different laws, they hang differently. A dipole's ribs cross the
plate. A tripole's stack. A quadrupole's stand on end. Nobody has to be told which class is which.

*** WHY THE LEVELS ARE QUANTILES AND NOT A LADDER. ***
The first draft cut the field at equal VALUES and the middle of every torso came out blank: an
insulated boundary makes a field that moves fast near its poles and hardly at all in the interior, so
an even ladder of values puts every contour round the rim and none across the chest. The levels are
therefore the field's OWN QUANTILES - the plate is cut into bands of equal AREA, and the ribs go
where the ornament is rather than where the arithmetic is. This costs nothing in rigour, because a
quantile of a solved field is as derivable from the mask as the field, and the reader recomputes it.
It is the same lesson the 47th paid for from the other side (run the RIM band BRIGHT, pitch set by
the THINNEST part) and the 53rd paid for as its whole subject (element size is an OUTPUT).

*** DISTINCTNESS. ***
  * 47th MOKUME - contour laminae of the distance transform. The nearest neighbour in the project and
    it is control DISTANCE. Closed contours vs open; local vs global (clause NONLOCAL measures it);
    a ridge of local maxima vs a field with none (clause MEAN-VALUE measures that).
  * 51st FLOWGRAIN - a continuous director field with defects. Also a field, and AUTHORED: its knot
    and its delta are put where we like, and its interior is a formula. Change the 51st's rim and
    its interior does not move. Change one pole here and the far side of the plate moves.
  * 11th FLUTING / 43rd GADROON - parallel reeds. Control LINEAR is the statement that they are this
    axis on a body that is a box, and no body in this project is a box.
  * 55th STRATA / 40th DENTIL - bands and courses at an authored pitch. HERE THERE IS NO PITCH. The
    spacing is |grad u| and nobody chose it.
  * 65th CASCADE - see the pair above.
  * 61st CANON - 3:2:1 among three hoops. A relation between authored parts.

Repaint only: every pattern pixel is painted onto an already-opaque body pixel, the silhouette is
never touched, and the sheets are QA-safe by construction. Sleep frames (fi >= 60) get a plain
recolor. Twenty-fifth generator to call sprite_finish.finish_array in-line.

    python3 scripts/gen_anneal_axis69.py             # write the 24 staged sheets
    python3 scripts/gen_anneal_axis69.py --field     # ASCII of one real component
    python3 scripts/gen_anneal_axis69.py --accept    # the six clauses over all 24 sheets
    python3 scripts/gen_anneal_axis69.py --controls  # the eight controls through the same reader
    python3 scripts/gen_anneal_axis69.py --sweep     # per-slot affordability
    python3 scripts/gen_anneal_axis69.py --survive   # relief through the finishing pass
Then QA (examples):
    python3 scripts/sprite_qa.py _anneal_legendary_preview/shirt_warrior_legendary69.png
    python3 scripts/sprite_qa.py _annealdome_helmet_preview/helmet_mage_legendary69.png --y-min 2
    python3 scripts/sprite_qa.py _anneal_boots_preview/boots_warrior_legendary_anneal.png --y-max 63
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
SLEEP_FROM = 60
Q_LO, Q_HI = 0.85, 1.18

# A part smaller than this is a speck left by a pose (a fingertip, a buckle corner) and is painted
# plain. It is not annealed and it is not counted against the sheet: a part with four pixels in it
# has no interior to relax.
MIN_PX = 12

# CLASS IDENTITY IS THE ORDER OF A MULTIPOLE, and there is nothing else in it.
NPOLE = {'warrior': 2, 'ranger': 3, 'mage': 4}
KNOWN_N = (2, 3, 4)          # every n the reader knows; clause RECOMPUTE tries all of them

# How many bands the piece is cut into. NOT A PITCH AND NOT A TASTE - it is a function of the part's
# own area, so the reader derives it from the mask exactly as the painter did. sqrt(area)/2 is one
# rib every two pixels along the part's own diameter, clamped where a sabaton and a torso stop being
# comparable objects.
NB_LO, NB_HI, NB_DIV = 3, 7, 2.0

# The relaxation's stopping rule, used only by the AMNESIA histories - the plate itself is solved
# exactly. A sweep that moves nothing by more than this has stopped, and the bands are integers so
# the last few 1e-10 cannot change a rib.
JACOBI_TOL = 1e-11
JACOBI_MAX = 40000

# Three metals, none of them near black (the visor's eye and mouth pixels are black and a near-black
# darkest stop swallows them - the 49th's lesson). Deliberately unrelated to the 66th
# (basalt/porphyry/sandstone), the 67th (garnet/celadon/olive brass) and the 68th
# (periwinkle/amber/pale teal) so the four most recent axes cannot be mistaken for a recolor set.
#   warrior  COPPER        hot oxidised copper
#   mage     PLUM          cold violet enamel
#   ranger   SMOKED STEEL  neutral grey, the crispest ground for a rib
PAL = {
    'warrior': ((238, 178, 132), (170, 102, 64), (100, 58, 38)),
    'mage':    ((216, 168, 232), (146, 96, 176), (86, 54, 106)),
    'ranger':  ((206, 210, 214), (128, 134, 142), (72, 78, 86)),
}
BODY = {cls: (p[2], p[1], p[0]) for cls, p in PAL.items()}   # (dark, mid, light) for the recolor

SLOTS = {
    'chest': dict(
        outdir='_anneal_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary69',
    ),
    'legs': dict(
        outdir='_anneal_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary69',
    ),
    'boots': dict(
        outdir='_anneal_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_anneal',
    ),
    'helmet': dict(
        outdir='_annealdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary69',
    ),
}

CONTROLS = ('distance', 'halfway', 'linear', 'pinned', 'noise', 'grounded', 'swapped', 'onepole')
SWAP_N = {'warrior': 3, 'ranger': 4, 'mage': 2}


# --- sheet machinery ---------------------------------------------------------------------------
def label4(mask):
    """Self-contained 4-connectivity labelling (scipy-free)."""
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    n = 0
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and lab[sy, sx] == 0:
                n += 1
                lab[sy, sx] = n
                st = [(sy, sx)]
                while st:
                    y, x = st.pop()
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n
                            st.append((ny, nx))
    return lab, n


def load_any(fname):
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def parts_of(a):
    """The parts of the piece that are big enough to have an interior.

    EVERY PART IS ANNEALED SEPARATELY AND WITH THE SAME n. That is not a compromise, it is what the
    law says: a part of a garment is a body with an outline, and an outline is all this ornament
    needs. It is also the exact opposite of the 67th COLOPHON, whose census had to be of the whole
    garment because a count is only a count of something; a potential is a local object and two
    sleeves are two bodies."""
    lab, n = label4(a)
    return [lab == i for i in range(1, n + 1) if int((lab == i).sum()) >= MIN_PX]


def put(fr, y, x, rgb):
    if 0 <= y < fr.shape[0] and 0 <= x < fr.shape[1]:
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


# --- the poles ---------------------------------------------------------------------------------
def pole_value(j, n):
    """What the j-th of n poles is held at: THE HIGHEST HARMONIC n POLES CAN EXPRESS.

        v(j) = cos(2*pi*j*floor(n/2)/n)
        n=2  +1, -1                     a dipole
        n=3  +1, -1/2, -1/2             a tripole
        n=4  +1, -1, +1, -1             a quadrupole

    The values sum to zero for every n, so no class is secretly a brighter version of another.
    THE FLOOR(n/2) IS NOT DECORATION AND IT WAS PAID FOR. The first draft used the FIRST harmonic,
    cos(2*pi*j/n), which for n=4 is (+1, 0, -1, 0) - two live poles and two neutral ones - and on a
    body that happens to be symmetric about the line joining the live pair the two neutral poles do
    nothing at all AND THE QUADRUPOLE DRAWS EXACTLY THE PICTURE THE DIPOLE DRAWS. One mage torso in
    mid-slash out of eight hundred and thirty-eight was in that position, and the plate could not
    say what class it was. Taking the fastest alternation the star will hold puts every pole to
    work and the collision cannot occur: a plate on which n poles alternate is not a plate on which
    two do."""
    return math.cos(2 * math.pi * j * (n // 2) / n)


def poles_of(comp, n):
    """n pixels of the part's own outline, at n equal angles about its own centroid, held at
    cos(2*pi*j/n).

    THE ORIGIN IS THE PART AND NOTHING ELSE. There is no grid, no phase and no up in this axis: the
    poles are found by asking the part which of its pixels is farthest in a direction, which is a
    question with the same answer however the part is translated. Ties go to the lowest (row, col),
    so the answer is a function and not a choice.

    Returns None if two poles land on the same pixel - a part too small or too thin to be held in n
    places cannot carry the class, and the sheet is REPORTED rather than quietly given a different
    ornament."""
    ys, xs = np.nonzero(comp)
    if len(ys) < n:
        return None
    cy, cx = ys.mean(), xs.mean()
    out, taken = [], set()
    for j in range(n):
        th = 2 * math.pi * j / n
        sc = (ys - cy) * math.sin(th) + (xs - cx) * math.cos(th)
        # THE FARTHEST PIXEL IN THIS DIRECTION THAT IS NOT ALREADY HELD. The conflict rule earns
        # its keep on exactly the parts that have no room: a chausse is four pixels wide and comes
        # to a point at the hip, so its topmost pixel and its rightmost pixel ARE THE SAME PIXEL,
        # and a first draft that simply refused the collision lost twelve poses of the mage's legs
        # and twenty-nine of the mage's sabatons. Taking the next pixel along is still a function of
        # the mask - nothing is chosen, the order is total - and it costs a pole a fraction of a
        # pixel of extremity instead of costing the sheet its ornament.
        order = sorted(range(len(ys)), key=lambda i: (-float(sc[i]), int(ys[i]), int(xs[i])))
        pick = None
        for i in order:
            p = (int(ys[i]), int(xs[i]))
            if p not in taken:
                pick = p
                break
        if pick is None:
            return None
        taken.add(pick)
        out.append((pick[0], pick[1], pole_value(j, n)))
    return out


# --- the equilibrium ---------------------------------------------------------------------------
def _system(comp, fixed):
    """The discrete Laplacian of the part, with an INSULATED outline.

    A pixel's neighbours are only those inside the part, so no flux leaves the silhouette. That is
    the whole reason a rib can END on the outline instead of turning and closing - see control
    GROUNDED, which is this axis with a Dirichlet rim and rings instead of ribs."""
    pts = [(int(y), int(x)) for y, x in np.argwhere(comp)]
    free = [p for p in pts if p not in fixed]
    idx = {p: i for i, p in enumerate(free)}
    m = len(free)
    A = np.zeros((m, m))
    b = np.zeros(m)
    h, w = comp.shape
    for p in free:
        i = idx[p]
        y, x = p
        deg = 0
        for q in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if not (0 <= q[0] < h and 0 <= q[1] < w) or not comp[q]:
                continue
            deg += 1
            if q in fixed:
                b[i] += fixed[q]
            else:
                A[i, idx[q]] -= 1.0
        A[i, i] = deg if deg else 1.0
    return free, idx, A, b


def solve_field(comp, fixed):
    """The equilibrium, exactly - one linear solve, no iteration, no history."""
    free, idx, A, b = _system(comp, fixed)
    u = np.full(comp.shape, np.nan)
    if free:
        try:
            sol = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            sol = np.linalg.lstsq(A, b, rcond=None)[0]
        for p, i in idx.items():
            u[p] = sol[i]
    for (y, x), v in fixed.items():
        u[y, x] = v
    return u


def relax_field(comp, fixed, start, sweeps=JACOBI_MAX, tol=JACOBI_TOL):
    """The same equilibrium, reached instead of computed. Used only by clause AMNESIA and by control
    HALFWAY, which is this function stopped early."""
    h, w = comp.shape
    u = np.where(comp, start, 0.0).astype(np.float64)
    for (y, x), v in fixed.items():
        u[y, x] = v
    hold = np.zeros((h, w), bool)
    for (y, x) in fixed:
        hold[y, x] = True
    nb = np.zeros((h, w))
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nb += np.roll(np.roll(comp.astype(float), dy, 0), dx, 1)
    nb[~comp] = 1.0
    nb[nb == 0] = 1.0
    for _ in range(sweeps):
        s = np.zeros((h, w))
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            s += np.roll(np.roll(np.where(comp, u, 0.0), dy, 0), dx, 1)
        nxt = s / nb
        nxt[hold] = u[hold]
        nxt[~comp] = 0.0
        d = float(np.abs(nxt[comp] - u[comp]).max()) if comp.any() else 0.0
        u = nxt
        if d < tol:
            break
    out = np.full((h, w), np.nan)
    out[comp] = u[comp]
    return out


def distance_field(comp):
    """Distance to the outside of the part - THE 47th MOKUME's field, for control DISTANCE."""
    h, w = comp.shape
    d = np.where(comp, np.inf, 0.0)
    for _ in range(max(h, w)):
        s = d.copy()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            s = np.minimum(s, np.roll(np.roll(d, dy, 0), dx, 1) + 1)
        s[~comp] = 0.0
        if np.array_equal(s, d):
            break
        d = s
    out = np.full((h, w), np.nan)
    out[comp] = d[comp]
    return out


def linear_field(comp, pol):
    """A flat ramp between the two farthest poles - harmonic, and not this body's equilibrium."""
    pts = [(y, x) for y, x, _ in pol]
    if len(pts) < 2:
        return np.full(comp.shape, np.nan)
    (ay, ax), (by, bx) = pts[0], pts[len(pts) // 2]
    vy, vx = by - ay, bx - ax
    n2 = float(vy * vy + vx * vx) or 1.0
    out = np.full(comp.shape, np.nan)
    for y, x in np.argwhere(comp):
        out[y, x] = ((y - ay) * vy + (x - ax) * vx) / n2
    return out


# --- the bands and the ribs --------------------------------------------------------------------
def nbands(area):
    return max(NB_LO, min(NB_HI, int(round(math.sqrt(area) / NB_DIV))))


def _quantile_bands(comp, u, nb):
    fin = np.isfinite(u) & comp
    k = int(fin.sum())
    vals = u[fin]
    pts = np.argwhere(fin)
    order = sorted(range(k), key=lambda i: (float(vals[i]), int(pts[i][0]), int(pts[i][1])))
    q = np.full(comp.shape, -1, np.int32)
    for rank, i in enumerate(order):
        y, x = pts[i]
        q[y, x] = min(rank * nb // k, nb - 1)
    return q


def bands_of(comp, u):
    """EQUAL-AREA bands: the levels are the field's own quantiles.

    A ladder of equal VALUES puts every contour round the rim and leaves the chest blank, because an
    insulated field moves fast at its poles and slowly in the middle. Quantiles put the ribs where
    the ornament is. Ties are broken by (row, col) so the banding is a function of the field and the
    mask and of nothing else."""
    fin = np.isfinite(u) & comp
    k = int(fin.sum())
    if k == 0:
        return None
    vals = u[fin]
    if float(vals.max() - vals.min()) < 1e-12:
        return None                      # a constant field has no contour - see control ONEPOLE
    # THE PLATE IS CUT AS FINE AS IT WILL TAKE, AND NO FINER. nbands() proposes; the body disposes.
    # A pixel that is on the high side of one level and the low side of another is a pixel with no
    # field left to stand on - the band there is one pixel thick, the rib has no witness and the
    # crest fuses into a blot. So the count comes down a step at a time until every band is at least
    # two pixels through, and the number that survives is an OUTPUT of the mask, not a pitch. It is
    # the 53rd GRANULATION's lesson (element size is an output) applied to a spacing instead of to a
    # size, and it is why this axis has no pitch anywhere in it.
    for nb in range(nbands(k), 1, -1):
        q = _quantile_bands(comp, u, nb)
        crest, dark = _raw_sides(comp, q)
        if (crest & dark).any():
            continue
        if _blots(crest):
            # A 2x2 of crest is not two ribs crossing, it is a BLOT: four pixels each of which has
            # a lower neighbour somewhere outside the block and none of which has one inside it.
            # It happens where a band wraps a neck. Same remedy, same reason - the ruling is finer
            # than the body.
            continue
        return q
    return None


def _raw_sides(comp, q):
    """The two sides of every level: higher and lower. They may overlap, and where they do the band
    is one pixel thick and the ruling is too fine - see bands_of."""
    h, w = comp.shape
    hi = np.zeros((h, w), bool)
    lo = np.zeros((h, w), bool)
    for y, x in np.argwhere(q >= 0):
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and q[ny, nx] >= 0:
                if q[y, x] > q[ny, nx]:
                    hi[y, x] = True
                elif q[y, x] < q[ny, nx]:
                    lo[y, x] = True
    return hi, lo


def ribs_of(comp, q):
    """The ribs: a pixel is CREST where its band is higher than a neighbour's, and the neighbour
    across that level is its DARK witness. A rib therefore always comes with its own shadow, which
    is the only kind of relief that survives 13px."""
    return _raw_sides(comp, q)


def ornament(comp, n, mode=None, rng=None):
    """The whole ornament of one part, from the mask and n and nothing else.

    Returns (crest, dark, u, fixed) or None if the part cannot be held in n places."""
    if mode == 'distance':
        u = distance_field(comp)
        fixed = {}
    else:
        pol = poles_of(comp, 1 if mode == 'onepole' else n)
        if pol is None:
            return None
        fixed = {(y, x): v for y, x, v in pol}
        if mode == 'grounded':
            h, w = comp.shape
            for y, x in np.argwhere(comp):
                edge = False
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if not (0 <= ny < h and 0 <= nx < w) or not comp[ny, nx]:
                        edge = True
                if edge and (y, x) not in fixed:
                    fixed[(y, x)] = 0.0
        if mode == 'pinned':
            ys, xs = np.nonzero(comp)
            cy, cx = int(round(ys.mean())), int(round(xs.mean()))
            best = min(((int(y), int(x)) for y, x in np.argwhere(comp)),
                       key=lambda p: (p[0] - cy) ** 2 + (p[1] - cx) ** 2)
            fixed[best] = 1.0
        if mode == 'linear':
            u = linear_field(comp, pol)
        elif mode == 'halfway':
            u = relax_field(comp, fixed, np.zeros(comp.shape), sweeps=25, tol=0.0)
        else:
            u = solve_field(comp, fixed)
        if mode == 'noise':
            r = rng if rng is not None else np.random.RandomState(7)
            u = u + np.where(comp, r.uniform(-0.06, 0.06, comp.shape), 0.0)
    q = bands_of(comp, u)
    if q is None:
        return None
    crest, dark = ribs_of(comp, q)
    return crest, dark, u, fixed


def build_frame(fr, a, cls, mode=None, n_override=None):
    """Paint one pose. Returns the crest/dark sets actually painted, or None if some part of the
    piece could not be annealed - in which case the SHEET goes plain and is reported."""
    n = n_override if n_override is not None else NPOLE[cls]
    if mode == 'swapped':
        n = SWAP_N[cls]
    crest_c, mid_c, dark_c = PAL[cls]
    parts = parts_of(a)
    # A POSE WITH NOTHING BIG ENOUGH IN IT IS NOT A FAILURE. Two frames of a jumping warrior leave
    # nothing of the sabatons but a few pixels of toe; there is no interior there to relax and no
    # ornament is owed. The plate is flattened and reported as empty, not as unlawful, and the
    # reader agrees because it applies the same MIN_PX to the same mask.
    # THE FIELD IS FLAT BEFORE THE RIBS GO ON. The source sheet's own highlights are the same
    # lightest stop the ribs are painted in, and a reader that is told nothing cannot tell an
    # inherited highlight from a rib - it would read a crest set that is not the ornament. Every
    # tone on an annealed plate is put there by the equilibrium and by nothing else; the relief
    # comes back, richer, from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, mid_c)
    allc = np.zeros(a.shape, bool)
    alld = np.zeros(a.shape, bool)
    for comp in parts:
        got = ornament(comp, n, mode)
        if got is None:
            # A PART THE RULING WILL NOT TAKE IS LEFT PLAIN AND COUNTED, NOT FAKED. Seven poses of
            # the female mage's sabatons are a twelve-pixel wedge on which every band count from
            # seven down to two puts a blot; there is no honest ornament there, so there is none.
            # The pose still speaks if any other part of it does, and the SHEET is what has to
            # speak in all forty-two poses.
            continue
        crest, dark, _u, _f = got
        allc |= crest
        alld |= dark
    if not allc.any() and parts:
        return None
    for y, x in np.argwhere(alld):
        put(fr, y, x, dark_c)
    for y, x in np.argwhere(allc):
        put(fr, y, x, crest_c)
    return allc, alld


def frames_of(base):
    for fi in range(SLEEP_FROM):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a = base[sl][..., 3] > 0
        if a.any():
            yield fi, sl, a


def one_plate(base, sl, a, cls, mode=None, n_override=None):
    fr = np.zeros((FH, FW, 4), base.dtype)
    D, M, L = BODY[cls]
    recolor(base[sl], fr, a, D, M, L)
    got = build_frame(fr, a, cls, mode, n_override)
    return fr, got


def sheet_carries(base, cls, mode=None):
    """A SHEET IS ANNEALED IN ALL FORTY-TWO POSES OR IN NONE. An ornament that appears in some frames
    of a walk and not others reads as a BUG, not as a hard case."""
    for fi, sl, a in frames_of(base):
        _fr, got = one_plate(base, sl, a, cls, mode)
        if got is None:
            return False
    return True


def build(base, cls, mode=None, force=None):
    D, M, L = BODY[cls]
    ok = sheet_carries(base, cls, mode) if force is None else force
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        recolor(src, out[sl], a, D, M, L)
        if fi >= SLEEP_FROM or not ok:
            continue
        build_frame(out[sl], a, cls, mode)
    return out, ok


# --- the reader --------------------------------------------------------------------------------
def read_ribs(fr, a):
    """The crest set, off the pixels. The three stops are discovered from the plate, never told."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    pts = np.argwhere(a)
    if len(pts) == 0:
        return np.zeros(a.shape, bool), np.zeros(a.shape, bool)
    vals = sorted({int(lum[y, x]) for y, x in pts})
    crest = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    # THE STOPS ARE DISCOVERED, NEVER TOLD, AND THEY ARE COUNTED RATHER THAN MEASURED.
    #   one tone   a plate with nothing on it: no rib, no witness. (A jumping warrior leaves four
    #              pixels of toe and there is nothing there to anneal.)
    #   two tones  a rib and its witness ALWAYS come together - a band boundary has two sides - so
    #              two tones can only be dark and crest, with no field left over. This happens on
    #              sabatons, where the ornament uses every pixel there is.
    #   three      dark, field, crest.
    # A first draft took the ground to be whatever there was MOST of, which is true of a torso and
    # false of a boot: on a twelve-pixel sabaton the ribs outnumber the field and the reader read
    # the ornament as the ground and the ground as the ornament, costing nine poses of ranger
    # sabatons that were perfectly lawful.
    if len(vals) < 2:
        return crest, dark
    lo, hi = vals[0], vals[-1]
    for y, x in pts:
        v = int(lum[y, x])
        if v == hi:
            crest[y, x] = True
        elif v == lo:
            dark[y, x] = True
    return crest, dark


def predict(a, n, mode=None):
    """What the ornament WOULD be, from the mask and n alone. This is the reader's whole method: it
    does not inspect the plate, it draws one."""
    allc = np.zeros(a.shape, bool)
    alld = np.zeros(a.shape, bool)
    parts = parts_of(a)
    for comp in parts:
        got = ornament(comp, n, mode)
        if got is None:
            continue
        crest, dark, _u, _f = got
        allc |= crest
        alld |= dark
    if not allc.any() and parts:
        return None
    return allc, alld


# --- the acceptance test -----------------------------------------------------------------------
def _maximum_principle(comp, u, fixed):
    """Violations of the discrete maximum principle: free pixels that are strict local extrema.

    Exact, strict comparisons, NO TOLERANCE CONSTANT. It is a theorem that an equilibrium has none,
    so on the axis this clause is a test of the SOLVER; on control DISTANCE it is a massacre,
    because the distance transform's ridge is a line of local maxima and that ridge is the whole
    difference between a contour of a shape and a contour of a field."""
    h, w = comp.shape
    bad = 0
    for y, x in np.argwhere(comp):
        if (y, x) in fixed:
            continue
        nb = []
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and comp[ny, nx] and np.isfinite(u[ny, nx]):
                nb.append(float(u[ny, nx]))
        if not nb:
            continue
        v = float(u[y, x])
        if v > max(nb) + 1e-9 or v < min(nb) - 1e-9:
            bad += 1
    return bad


def _mean_value(comp, u, fixed):
    """max |u(p) - mean of u over p's in-mask neighbours| over the free pixels. Reported, not a
    clause: this is the one number in the file that is floating point, and the file says so."""
    h, w = comp.shape
    worst = 0.0
    for y, x in np.argwhere(comp):
        if (y, x) in fixed:
            continue
        nb = []
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and comp[ny, nx] and np.isfinite(u[ny, nx]):
                nb.append(float(u[ny, nx]))
        if nb:
            worst = max(worst, abs(float(u[y, x]) - sum(nb) / len(nb)))
    return worst


def _blots(crest):
    """2x2 blocks of crest. A rib is a LINE."""
    c = crest.astype(np.int8)
    s = c[:-1, :-1] + c[:-1, 1:] + c[1:, :-1] + c[1:, 1:]
    return int((s == 4).sum())


def _widow_ribs(crest, dark):
    """Crest pixels with no dark witness 4-adjacent."""
    h, w = crest.shape
    bad = 0
    for y, x in np.argwhere(crest):
        ok = False
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and dark[ny, nx]:
                ok = True
        if not ok:
            bad += 1
    return bad


AMNESIA_STARTS = 6
NONLOCAL_FAR = 4        # "far from the pole that moved", in Chebyshev pixels


def _dependence(comp, n, mode=None):
    """EVERY FREE PIXEL HEARS EVERY POLE.

    Raise one pole by one and re-solve: on a connected body at equilibrium the Green's function is
    strictly positive, so EVERY free pixel moves - not most of them, not the ones nearby, all of
    them. That is what it means for the ornament to be a fact about the whole plate rather than
    about a neighbourhood, and it is exact, threshold-free and provable, which a perturbation
    measured in pixels is not.

    A one-pixel radius was the first draft of this clause and it was a bad clause: a one-pixel move
    of a pole does not always cross a quantile, so on 115 probes of 200 it measured nothing at all
    and on 12 more it measured only that the change had not travelled - which is a fact about the
    coarseness of a band, not about the reach of a field. Returns (pixels that failed to move,
    pixels tested).

    THE COMPARISON IS EXACT AND THE FILE MEANS IT: a pixel counts as deaf only if its value comes
    back BIT FOR BIT UNCHANGED. A tolerance here would be measuring the solver, not the field - the
    smallest honest motion in this batch is 1.2e-03 and the largest is order one, so nothing is
    hiding under an epsilon."""
    if mode == 'distance':
        # THE CONTROL HAS NO POLES TO HEAR. Its field is a fact about each pixel's own
        # neighbourhood; raise a pole and the plate does not move a hair. Every pixel fails.
        u = distance_field(comp)
        k = int((np.isfinite(u) & comp).sum())
        return k, k, 0
    pol = poles_of(comp, n)
    if pol is None:
        return None
    fixed = {(y, x): v for y, x, v in pol}
    u0 = solve_field(comp, fixed)
    h, w = comp.shape

    def deg(y, x):
        return sum(1 for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                   if 0 <= ny < h and 0 <= nx < w and comp[ny, nx])

    bad = tested = leaves = 0
    for j in range(len(pol)):
        f2 = dict(fixed)
        f2[(pol[j][0], pol[j][1])] = pol[j][2] + 1.0
        u1 = solve_field(comp, f2)
        for y, x in np.argwhere(comp):
            if (y, x) in fixed:
                continue
            if deg(int(y), int(x)) < 2:
                # A HANGNAIL IS NOT AN INTERIOR. A pixel with exactly one neighbour takes that
                # neighbour's value and nothing else's; when the neighbour is a pole, the pixel IS
                # that pole and is deaf to the others - correctly, and by arithmetic rather than by
                # any failure of the field. Three poses of a ranger torso have one such pixel where
                # the shoulder ends in a single square. They are excluded and counted, not excused.
                leaves += 1
                continue
            tested += 1
            if float(u1[y, x]) == float(u0[y, x]):
                bad += 1
    return bad, tested, leaves


def _nonlocal_probe(comp, n):
    """Move one pole one pixel along the outline and count the rib pixels that change FAR AWAY."""
    pol = poles_of(comp, n)
    if pol is None:
        return None
    base = ornament(comp, n)
    if base is None:
        return None
    y0, x0, _v = pol[0]
    h, w = comp.shape
    alt = None
    for ny, nx in ((y0, x0 + 1), (y0, x0 - 1), (y0 + 1, x0), (y0 - 1, x0),
                   (y0 + 1, x0 + 1), (y0 - 1, x0 - 1)):
        if 0 <= ny < h and 0 <= nx < w and comp[ny, nx] and (ny, nx) not in \
                {(p[0], p[1]) for p in pol}:
            alt = (ny, nx)
            break
    if alt is None:
        return None
    fixed = {(p[0], p[1]): p[2] for p in pol[1:]}
    fixed[alt] = pol[0][2]
    u = solve_field(comp, fixed)
    q = bands_of(comp, u)
    if q is None:
        return None
    crest2, _d2 = ribs_of(comp, q)
    diff = base[0] ^ crest2
    # "FAR" IS A PROPERTY OF THE PART AND NOT A NUMBER IN THIS FILE. The far half of a part is the
    # half of its pixels that lie beyond the MEDIAN distance from the pole that moved - an output of
    # the mask, so a sabaton and a cuirass are asked the same question in their own units. A fixed
    # radius was the first draft and it asked a twelve-pixel sabaton whether its ornament had
    # changed four pixels away, where the sabaton does not go.
    ds = [max(abs(int(y) - y0), abs(int(x) - x0)) for y, x in np.argwhere(comp)]
    med = float(np.median(ds))
    far = 0
    for y, x in np.argwhere(diff):
        if max(abs(int(y) - y0), abs(int(x) - x0)) > med:
            far += 1
    return int(diff.sum()), far


def accept(mode=None, verbose=True, limit=None, amnesia_cap=90, nonlocal_cap=200):
    res = dict(sheets=0, silent=0, plates=0, parts=0, ribs=0, mute=0,
               recompute=0, ambiguous=0, maxprinc=0, amnesia=0, amnesia_n=0,
               nonlocal_bad=0, nonlocal_n=0, nonlocal_vac=0, nonlocal_far=0, nonlocal_tot=0,
               blots=0, widows=0, poles=0, mv=0.0, leaves=0, ns={})
    rng = np.random.RandomState(20260810)
    for kind, cfg in SLOTS.items():
        for cls, stem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (stem, suffix))
                res['sheets'] += 1
                if not sheet_carries(base, cls, mode):
                    res['silent'] += 1
                    continue
                seen = 0
                for fi, sl, a in frames_of(base):
                    if limit is not None and seen >= limit:
                        break
                    seen += 1
                    fr, got = one_plate(base, sl, a, cls, mode)
                    if got is None:
                        continue
                    res['plates'] += 1
                    crest, dark = got
                    res['ribs'] += int(crest.sum())
                    parts = parts_of(a)
                    res['parts'] += len(parts)

                    # (1) RECOMPUTE - the reader draws the ornament and demands the plate.
                    # A PLATE WITH NO RIB ON IT IS NOT ASKED WHAT CLASS IT IS. Two poses of a
                    # jumping warrior leave four pixels of toe; every n predicts the same empty
                    # ornament there, and a plate that says nothing cannot say it ambiguously. The
                    # count is reported instead of excused.
                    rc, rd = read_ribs(fr, a)
                    if not rc.any():
                        res['mute'] += 1
                        continue
                    hits = []
                    for n in KNOWN_N:
                        p = predict(a, n, mode)
                        if p is not None and np.array_equal(p[0], rc) and np.array_equal(p[1], rd):
                            hits.append(n)
                    if len(hits) != 1:
                        res['recompute'] += 1
                        if len(hits) > 1:
                            res['ambiguous'] += 1
                    else:
                        res['ns'][hits[0]] = res['ns'].get(hits[0], 0) + 1
                        # (6) POLES - and the class falls out of the ornament
                        want = SWAP_N[cls] if mode == 'swapped' else NPOLE[cls]
                        if mode not in ('distance', 'onepole') and hits[0] != want:
                            res['poles'] += 1

                    # (5) LEGIBLE
                    res['blots'] += _blots(crest)
                    res['widows'] += _widow_ribs(crest, dark)

                    # (2) MEAN-VALUE + the maximum principle, per part
                    for comp in parts:
                        nn = SWAP_N[cls] if mode == 'swapped' else NPOLE[cls]
                        got2 = ornament(comp, nn, mode)
                        if got2 is None:
                            continue
                        _c, _d, u, _painters_fixed = got2
                        # THE READER DOES NOT GET THE PAINTER'S LIST OF WHAT WAS HELD. It knows only
                        # what it can derive: n poles at n angles about the part's own centroid.
                        # Anything else the painter pinned is, to the reader, an ordinary pixel that
                        # ought to be the mean of its neighbours - which is exactly how control
                        # PINNED is caught, and the first draft of this clause, which trusted the
                        # painter's list, did not catch it at all.
                        pol = poles_of(comp, 1 if mode == 'onepole' else nn)
                        held = {} if pol is None else {(y, x): v for y, x, v in pol}
                        res['maxprinc'] += _maximum_principle(comp, u, held)
                        res['mv'] = max(res['mv'], _mean_value(comp, u, held))

                    # (3) AMNESIA - six histories, one picture (sampled, and the count is reported)
                    if res['amnesia_n'] < amnesia_cap and mode is None:
                        for comp in parts[:1]:
                            pol = poles_of(comp, NPOLE[cls])
                            if pol is None:
                                continue
                            fixed = {(y, x): v for y, x, v in pol}
                            ref = ornament(comp, NPOLE[cls])
                            if ref is None:
                                continue
                            starts = [np.zeros(comp.shape),
                                      np.ones(comp.shape),
                                      -np.ones(comp.shape),
                                      np.nan_to_num(distance_field(comp))]
                            for _ in range(AMNESIA_STARTS - len(starts)):
                                starts.append(rng.uniform(-3, 3, comp.shape))
                            for s in starts:
                                res['amnesia_n'] += 1
                                u2 = relax_field(comp, fixed, s)
                                q2 = bands_of(comp, u2)
                                if q2 is None:
                                    res['amnesia'] += 1
                                    continue
                                c2, _dd = ribs_of(comp, q2)
                                if not np.array_equal(c2, ref[0]):
                                    res['amnesia'] += 1

                    # (4) DEPENDENCE, with the one-pixel reach reported beside it
                    if res['nonlocal_n'] < nonlocal_cap:
                        for comp in parts[:1]:
                            nn = SWAP_N[cls] if mode == 'swapped' else NPOLE[cls]
                            dep = _dependence(comp, nn, mode)
                            if dep is None:
                                continue
                            res['nonlocal_n'] += 1
                            res['nonlocal_bad'] += dep[0]
                            res['nonlocal_vac'] += dep[1]
                            res['leaves'] += dep[2]
                            pr = _nonlocal_probe(comp, nn) if mode != 'distance' else None
                            if pr is not None:
                                res['nonlocal_tot'] += pr[0]
                                res['nonlocal_far'] += pr[1]
    if verbose:
        _report(mode, res)
    return res


def _report(mode, res):
    name = 'AXIS' if mode is None else ('CONTROL ' + mode.upper())
    print('== %s' % name)
    print('   sheets speaking %2d of %2d   (plain and reported, never tested: %d)'
          % (res['sheets'] - res['silent'], res['sheets'], res['silent']))
    print('   plates %4d   parts %5d   rib pixels %6d   (mute plates, never questioned: %d)'
          % (res['plates'], res['parts'], res['ribs'], res['mute']))
    print('   (1) RECOMPUTE   %4d violations   (%d plates admitted two n)'
          % (res['recompute'], res['ambiguous']))
    print('   (2) MEAN-VALUE  %4d maximum-principle violations   (worst residual %.2e, reported)'
          % (res['maxprinc'], res['mv']))
    print('   (3) AMNESIA     %4d of %4d histories reached a different picture'
          % (res['amnesia'], res['amnesia_n']))
    print('   (4) DEPENDENCE  %4d of %6d free pixels did not hear a pole move, over %d parts   '
          '(%d one-neighbour hangnails excluded)'
          % (res['nonlocal_bad'], res['nonlocal_vac'], res['nonlocal_n'], res['leaves']))
    print('       reported:   a pole slid ONE pixel moved %d rib pixels, %d of them in the part\'s '
          'far half' % (res['nonlocal_tot'], res['nonlocal_far']))
    print('   (5) LEGIBLE     %4d 2x2 rib blots, %4d ribs with no dark witness'
          % (res['blots'], res['widows']))
    print('   (6) POLES       %4d plates whose recovered n is not the class\'s'
          % res['poles'])
    print('   n recovered: %s' % (', '.join('n=%d x%d' % (n, c)
                                            for n, c in sorted(res['ns'].items())) or '(none)'))
    bad = (res['recompute'] + res['maxprinc'] + res['amnesia'] + res['nonlocal_bad']
           + res['blots'] + res['widows'] + res['poles'])
    if res['plates'] == 0:
        verdict = ('DEAD - not one plate in twenty-four sheets carries a rib, so there is nothing '
                   'to be right or wrong about')
    elif bad:
        verdict = 'FAIL (%d clause violations)' % bad
    elif mode == 'swapped':
        verdict = ('LAWFUL AND MISNAMED - every clause holds and clause RECOMPUTE names the class '
                   'it actually is, which is not the one it was made for')
    elif res['silent'] and mode is not None:
        verdict = 'LAWFUL BUT UNPAYABLE - %d of %d sheets go plain' % (res['silent'], res['sheets'])
    else:
        verdict = 'ALL PASS'
    print('   >>> %s' % verdict)
    return bad


def controls_report():
    print('The axis, then the eight controls, through the same reader.\n')
    accept(None)
    for m in CONTROLS:
        print()
        accept(m)


# --- diagnostics -------------------------------------------------------------------------------
def field_dump():
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        base = load_any('%s.png' % cfg['srcs'][cls])
        for fi, sl, a in frames_of(base):
            parts = parts_of(a)
            comp = max(parts, key=lambda c: c.sum())
            got = ornament(comp, NPOLE[cls])
            crest, dark, u, fixed = got
            ys, xs = np.nonzero(comp)
            y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
            print('== %s chest frame %d   n=%d poles, %d bands, %d rib px'
                  % (cls, fi, NPOLE[cls], nbands(int(comp.sum())), int(crest.sum())))
            for y in range(y0, y1 + 1):
                row = ''
                for x in range(x0, x1 + 1):
                    if not comp[y, x]:
                        row += '.'
                    elif (y, x) in fixed:
                        row += '@'
                    elif crest[y, x]:
                        row += 'O'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            print('   ("@" pole, "O" rib crest, "=" its dark witness, "-" field)')
            break


def sweep():
    print('== SLOTS  (can every pose be annealed in n places, and does it read back)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (cfg['srcs'][cls], suffix))
                fit = unfit = 0
                ribs = []
                for fi, sl, a in frames_of(base):
                    fr, got = one_plate(base, sl, a, cls)
                    if got is None:
                        unfit += 1
                        continue
                    rc, rd = read_ribs(fr, a)
                    p = predict(a, NPOLE[cls])
                    if p is not None and np.array_equal(p[0], rc) and np.array_equal(p[1], rd):
                        fit += 1
                        ribs.append(int(got[0].sum()))
                    else:
                        unfit += 1
                print('   %-7s %-8s %-2s  n=%d  ribs %2d-%-3d  poses %2d/%-2d  SHEET %s'
                      % (kind, cls, suffix or 'm', NPOLE[cls],
                         min(ribs) if ribs else 0, max(ribs) if ribs else 0,
                         fit, fit + unfit,
                         'annealed' if unfit == 0 else 'PLAIN (reported)'))


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a rib on the
    shadowed flank is darker in absolute terms than the field on the lit one and an absolute reader
    would report nonsense. What a player sees is whether a rib is lighter than the pixels beside
    it."""
    print('== SURVIVAL through the finishing pass (reported, local contrast)')
    for kind, cfg in SLOTS.items():
        tot = ok = 0
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            if not sheet_carries(base, cls):
                continue
            arr, _ = build(base, cls)
            fin, _info = finish_array(arr.copy(), '_tmp/%s_%s.png' % (cfg['dst'] % cls, kind))
            for fi, sl, a in frames_of(base):
                _fr, got = one_plate(base, sl, a, cls)
                if got is None:
                    continue
                crest, dark = got
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for y, x in np.argwhere(crest):
                    nb = [lum[ny, nx] for ny, nx in
                          ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                          if 0 <= ny < FH and 0 <= nx < FW and dark[ny, nx]]
                    if not nb:
                        continue
                    tot += 1
                    if lum[y, x] > float(np.mean(nb)):
                        ok += 1
        print('   %-7s ribs still lighter than their own witness: %5d/%-5d (%3d%%)'
              % (kind, ok, tot, (100 * ok // tot) if tot else 0))


def main():
    if '--field' in sys.argv:
        field_dump()
        return
    if '--accept' in sys.argv:
        accept()
        return
    if '--controls' in sys.argv:
        controls_report()
        return
    if '--sweep' in sys.argv:
        sweep()
        return
    if '--survive' in sys.argv:
        os.makedirs('_tmp', exist_ok=True)
        survive()
        return
    for kind, cfg in SLOTS.items():
        os.makedirs(cfg['outdir'], exist_ok=True)
        for cls, stem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (stem, suffix))
                arr, ok = build(base, cls)
                dst = '%s/%s%s.png' % (cfg['outdir'], cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-58s opaque_px=%-6d finish=%s/%s  %s'
                      % (dst, int((arr[..., 3] > 0).sum()), info['slot'], info['variant'],
                         'n=%d' % NPOLE[cls] if ok else 'PLAIN (reported)'))


if __name__ == '__main__':
    main()
