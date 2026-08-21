#!/usr/bin/env python3
"""SEVENTIETH net-new-geometry axis for ALL FOUR SLOTS - the TRUSS family: the ornament is a
BAR FRAMEWORK, and the law is about what it would do IF YOU PUSHED IT.

    the ornament is  a BAR       a straight run of crest pixels between two joints, with a dark
                                 witness laid alongside it
    the node is      a JOINT     one pixel of the brightest stop; a bar may end on one and may
                                 pass through none
    the law is       THE FRAMEWORK HAS EXACTLY 3 + k INFINITESIMAL MOTIONS, AND NO BAR IN IT
                     IS REDUNDANT

*** THIS IS THE FIRST INVARIANT THAT IS A BEHAVIOUR RATHER THAN A FACT. ***
Sixty-nine axes state something that is TRUE OF THE PIXELS AS THEY LIE. A statistic holds among the
shards (46th CRAQUELURE). A wire is connected (54th LABYRINTH). Three hoops stand in 3:2:1 (61st
CANON). The studs exclusive-or to zero (64th TALLY). Each row is the image of the row above (65th
CASCADE). No piece can be carried away (66th DOVETAIL). The registers count themselves (67th
COLOPHON). No displacement repeats (68th SEME). Every free pixel is the mean of its neighbours (69th
ANNEAL). Every one of those sentences can be checked by an inspector who is forbidden to touch the
plate. THIS ONE CANNOT. The claim here is not about the ornament's positions, it is about its
VELOCITIES: hold the bars rigid, allow the joints to move, and ask how many ways the figure can be
set going. Nothing on the plate is moving, nothing on the plate ever moves, and the entire content of
the axis is the answer to a question about motion that is never actually asked of it.
THE PLATE IS NOT DESCRIBED, IT IS LOADED.

*** THE PAIR WITH THE 66th, WHICH IS ITS EXACT COMPLEMENT. ***
    the 66th DOVETAIL   NO PART CAN BE REMOVED. Its ornament is a spanning tree of keys and its
                        acceptance test is a DISASSEMBLY: the reader tries to carry a stone away and
                        cannot. It is a statement about TAKING THINGS APART.
    the 70th TRUSS      NO PART CAN MOVE - or exactly k of them can. A spanning tree is the 66th's
                        answer and it is this axis's control TREE, where it scores a DOF of n-2:
                        A TREE HOLDS ITSELF TOGETHER AND HOLDS NOTHING ELSE. Connected is not rigid.
                        The 66th's own ornament, drawn by this axis's painter and put through this
                        axis's reader, is a rag.
Connectivity and rigidity are the two things people mean by "solid" and they are not the same thing;
control TREE is the difference stated as an integer.

*** THE ACCEPTANCE TEST IS A NEW KIND: A FLEX. ***
The reader takes the plate, recovers the joints (the brightest stop) and the bars (the pairs of
joints joined by an unbroken run of the second stop), writes down the RIGIDITY MATRIX

    R(i,j) row:   ( ... , p_i - p_j , ... , p_j - p_i , ... )        one row per bar, 2n columns

and takes its RANK. Everything the axis claims is a statement about that rank and nothing else. It is
the first acceptance test in the project that is a piece of LINEAR ALGEBRA ON THE PLATE'S OWN
COORDINATES, and the first whose verdict would change if the ornament were drawn the same but PLACED
differently - see control COLLINEAR, which is lawful as a graph and false as a picture.

    (1) FLEX       dim ker R = 3 + k. Three of those motions are the two translations and the
                   rotation that every framework in the plane has for free; the rest are the class.
                   k IS AN OUTPUT: the reader is not told which class it is holding, it counts the
                   motions and reads the class off them.
    (2) TIGHT      rank R = |E| exactly - the rows are independent, so EVERY BAR IS LOAD-BEARING.
                   Delete any one bar and the framework gains exactly one motion. This is the 66th's
                   question ("is any of this ornament merely ornament?") and here the answer is that
                   there is nothing on the plate that is only decoration.
    (3) SPARSE     the Laman count, checked over EVERY subset of joints: no set of s joints spans
                   more than 2s-3 bars. Combinatorial, coordinate-free, and the reason control DENSE
                   is caught even where its extra bars happen to be geometrically independent.
    (4) CLOSED     every joint has degree at least two and the framework is connected. A bar with a
                   free end is a whisker, not a strut: it carries no load, it cannot be part of a
                   count, and it is the shape a TREE is made of.
    (5) CLEAR      the recovered bars have pairwise DISJOINT interiors and together they account for
                   every crest pixel on the plate. This is the clause that makes the recovery
                   HONEST: a spurious bar - three joints that happen to line up along two real bars -
                   would have to share pixels with the bars it was mistaken for, so it cannot pass.
                   The reader does not have to be trusted about what it read, because a wrong reading
                   fails a clause of its own.
    (6) LEGIBLE    every bar pixel carries a dark witness beside it and no four crest pixels form a
                   2x2 block. A strut is a LINE.

*** THE CONSTRUCTION IS A THEOREM, NOT A SEARCH. ***
The painter never checks whether a plate is lawful; it cannot draw an unlawful one. It lays a SEED
CYCLE of 3+k joints and then adds every further joint with EXACTLY TWO BARS to joints already
placed - a Henneberg type-I extension, which is known to change neither the independence of the
framework nor its number of motions. So

    |E| = (3+k) + 2(n-3-k) = 2n-3-k        and        DOF = 2n - |E| - 3 = k

for every n, and THE ORNAMENT GROWS WITHOUT EVER CHANGING HOW FREE IT IS. That is the axis in one
line: a torso carries eleven bars and a pauldron carries three, and the two are the same object,
because the freedom is in the SEED and every later bar is spent buying a joint rather than buying
stiffness.

*** CLASS IDENTITY IS THE FREEDOM OF THE SEED, AND IT IS A SHAPE YOU CAN COUNT. ***
    warrior   k = 0   the seed is a TRIANGLE        it cannot move
    ranger    k = 1   the seed is a QUADRILATERAL   it can lozenge, one way
    mage      k = 2   the seed is a PENTAGON        it can lozenge two ways at once
Not an integer written on the plate (67th), not a ceiling (68th), not the order of a multipole
(69th) - THE NUMBER OF WAYS THE FIGURE COULD FALL DOWN. And like the 69th's it is visible without
being told: the warrior's figure is triangulated to the last cell, the ranger's has one four-sided
bay in it, the mage's one five-sided bay.

*** THE MINIMUM IS A THEOREM AND IT IS DIFFERENT FOR EVERY CLASS. ***
A framework with every joint of degree at least two and k motions needs |E| >= n, so
2n-3-k >= n, so n >= 3+k: a warrior can be held in three joints, a ranger needs four, a mage five.
THIS IS THE FIRST AXIS WHOSE MINIMUM SIZE DEPENDS ON THE CLASS, and it runs the same way round as
the 68th's did: the FREEST class is the EXPENSIVE one. A warrior sabaton is a triangle and speaks;
a mage sabaton would need a pentagon inside fourteen pixels and there is no such pentagon, so the
mage's boots are PLAIN AND REPORTED rather than faked. Reported, with the theorem beside it.

*** THE EIGHT CONTROLS, AND WHAT EACH ONE IS FOR (measured numbers, 48 sampled plates each). ***
    TREE       a spanning tree over the same joints - THE 66th DOVETAIL's own structure, drawn by
               this painter with this palette and this relief. 40 drawable, and every one of them
               false: FLEX 41, CLOSED 41, AND NOTHING ELSE. Connected, tidy, and it reads a DOF of
               1, 2 or 3 where the class wants 0, 1 or 2, because CONNECTED IS NOT RIGID; it fails
               CLOSED as well, because a tree has leaves and a leaf is a whisker. THE ONLY CONTROL
               THAT IS A PREVIOUS AXIS, and the distinctness argument stated as a number instead of
               as an opinion.
    GRID       the 14th LATTICE: joints on a sublattice, bars along the lattice edges. A net of
               QUADRILATERALS, the most obviously "structural" picture in the whole project, and a
               MECHANISM in every cell it has - FLEX 39, and the DOFs it reads are 2, 3, 5, 7, 8, 9.
               IT LOOKS THE STIFFEST AND IT IS THE FLOPPIEST THING IN THE FILE.
    TRELLIS    the 20th TRELLIS: the same net with a diagonal in every cell. It IS rigid, and it
               fails anyway - FLEX 26, TIGHT 3, SPARSE 0, CLOSED 36, CLEAR 13 - because it is rigid
               MANY TIMES OVER and most of its bars carry nothing. THE TWO NEAREST VISUAL
               NEIGHBOURS IN THE PROJECT FAIL THIS AXIS'S READER FOR EXACTLY OPPOSITE REASONS, and
               that is the cleanest distinctness result in the batch.
    COLLINEAR  the same graph with the joints slid onto one row of the part. THE ONLY CONTROL IN
               SEVENTY AXES THAT IS ABOUT WHERE THE ORNAMENT IS RATHER THAN WHAT IT IS, and AS A
               PICTURE IT IS DEAD: collinear bars lie on top of one another, 0 of 48 plates can be
               drawn, and a control that cannot be drawn cannot be read. So it is MEASURED instead
               (`--controls collinear`): take each shipped framework, keep its graph exactly - same
               joints, same bars, same Laman count - and move the joints onto the part's widest row.
               355 OF 355 FRAMEWORKS GAIN MOTIONS, one, two or three of them. The graph did not
               change; the positions did. That is why clause FLEX is the rank of R at the plate's
               real coordinates and not the Laman count of its graph.
               (It also cost a draft: sliding the joints onto the principal AXIS and rounding to
               pixels leaves them NEAR a line and not ON one, integer rounding restores general
               position, and the control scored 0 of 355. A degeneracy has to be exact.)
    DENSE      every extension made with three bars instead of two. 3 of 48 drawable and all three
               false (FLEX 2, TIGHT 1, SPARSE 1) - AND THE 45 UNDRAWABLE ONES ARE THE RESULT: on a
               thirteen-pixel torso there is usually nowhere to put a third bar that is not already
               on top of another bar, so over-bracing this axis mostly does not produce a picture
               at all.
    BRACED     one extra bar on the shipped framework. 24 of 48 drawable, ALL 24 FALSE, all of them
               on FLEX - which is the finding, and it is not the one that was expected: an extra bar
               that can be drawn on a hinged piece always REMOVES A HINGE, so BRACED on a ranger is
               a warrior with an extra joint, and clause FLEX says so. TIGHT catches the other kind
               of extra bar, the dependent one, and DENSE is where that shows up.
    WHISKER    one joint hung off the framework by a single bar. FLEX 41, CLOSED 41. A whisker adds
               a joint (+2) and a bar (+1 of rank) and therefore ADDS EXACTLY ONE MOTION - the bar
               swings - so FLEX does see it. CLOSED is in the file anyway, because the motion a
               whisker adds is indistinguishable from a class: without CLOSED, a warrior with one
               whisker IS a ranger.
    SWAPPED    another class's k. 40 drawable, FLEX 41 AND NOTHING ELSE - LAWFUL AND MISNAMED. It
               breaks no clause about frameworks; it is a perfectly good framework of the wrong
               class, and clause FLEX names the class it actually is. Same finding as the 69th's
               SWAPPED: the class is not a decoration on the law, IT IS THE WHOLE OF WHAT A CLASS
               IS HERE.

*** DISTINCTNESS. ***
  * 66th DOVETAIL - control TREE, and the pair above. Removal vs motion.
  * 14th LATTICE and 20th TRELLIS - controls GRID and TRELLIS. Both are FIELDS of cells at a pitch;
    this axis draws ONE IRREGULAR FIGURE PER PART, sized to the part, and it has no pitch anywhere.
  * 54th LABYRINTH - one continuous wire. A path has no rigidity at all (it is control TREE's worse
    half) and the 54th's law is topological: it does not care where its wire goes, only that there
    is one of it. This axis cares about nothing else.
  * 69th ANNEAL - also derives everything from the mask, and is a FIELD: continuous, dense, no
    combinatorics. Its joints would be this axis's poles and its picture is level lines. Where the
    69th solves, this one BUILDS.
  * 49th DENDRITE - branching, and a branch is a tree, and control TREE is what a tree scores.

Repaint only: every pattern pixel is painted onto an already-opaque body pixel, the silhouette is
never touched, and the sheets are QA-safe by construction. Sleep frames (fi >= 60) get a plain
recolor. Twenty-sixth generator to call sprite_finish.finish_array in-line.

    python3 scripts/gen_truss_axis70.py             # write the 24 staged sheets
    python3 scripts/gen_truss_axis70.py --frame     # ASCII of one real component per class
    python3 scripts/gen_truss_axis70.py --accept    # the six clauses over all 24 sheets
    python3 scripts/gen_truss_axis70.py --controls  # the eight controls through the same reader
    python3 scripts/gen_truss_axis70.py --sweep     # per-slot affordability
    python3 scripts/gen_truss_axis70.py --survive   # relief through the finishing pass
Then QA (examples):
    python3 scripts/sprite_qa.py _truss_legendary_preview/shirt_warrior_legendary70.png
    python3 scripts/sprite_qa.py _trussdome_helmet_preview/helmet_mage_legendary70.png --y-min 2
    python3 scripts/sprite_qa.py _truss_boots_preview/boots_warrior_legendary_truss.png --y-max 63
"""
import os
import sys
import math
import itertools
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
SLEEP_FROM = 60
Q_LO, Q_HI = 0.85, 1.18

# A part smaller than this is a speck left by a pose (a fingertip, a buckle corner). It is painted
# plain, and it is not counted against the sheet: there is nothing in four pixels to hold.
MIN_PX = 12

# CLASS IDENTITY IS THE NUMBER OF MOTIONS THE SEED HAS, and there is nothing else in it.
KDOF = {'warrior': 0, 'ranger': 1, 'mage': 2}
KNOWN_K = (0, 1, 2)
SWAP_K = {'warrior': 1, 'ranger': 2, 'mage': 0}

# The joint count is an OUTPUT of the part's area, exactly as the 69th's band count and the 53rd's
# bead size are. There is no pitch in this axis: sqrt(area)/JDIV is about one joint every two pixels
# along the part's own diameter, clamped where a sabaton and a torso stop being comparable objects,
# and floored at the class's own theoretical minimum 3+k.
JDIV, JMAX = 2.3, 7
# A bar shorter than this is a domino and its direction cannot be read; small parts are allowed
# shorter bars because on a fourteen-pixel sabaton the alternative is no ornament at all.
MINLEN_BIG, MINLEN_SMALL, SMALL_AREA = 3, 2, 40
# Ink is capped so that a plate keeps a FIELD to show its relief against. Extensions stop at INK_STOP
# and a seed that is already over INK_MAX is refused outright - that is what leaves a mage's sabaton
# plain instead of solid.
INK_STOP, INK_MAX = 0.55, 0.72
SEED_BREADTH, SEED_STARTS, SEED_BUDGET = 8, 32, 60000
EXT_POOL = 40

# Four stops per class, none of them near black (a near-black darkest stop swallows the visor's eye
# and mouth pixels - the 49th's lesson). Deliberately unrelated to the 66th (basalt/porphyry/
# sandstone), 67th (garnet/celadon/olive brass), 68th (periwinkle/amber/pale teal) and 69th
# (copper/plum/smoked steel) so the five most recent axes cannot be mistaken for a recolor set.
#   warrior  BLACKENED BRASS
#   ranger   SLATE BLUE STEEL
#   mage     VERDIGRIS
# (witness, field, bar, joint) - strictly increasing in luminance, which is the whole of the
# reader's discovery rule.
PAL = {
    'warrior': ((72, 60, 32), (150, 124, 62), (214, 186, 104), (250, 236, 180)),
    'ranger':  ((52, 64, 86), (104, 124, 156), (168, 190, 220), (232, 242, 255)),
    'mage':    ((40, 78, 76), (84, 142, 136), (150, 206, 196), (226, 250, 244)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}   # (dark, mid, light) for the recolor

SLOTS = {
    'chest': dict(
        outdir='_truss_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary70',
    ),
    'legs': dict(
        outdir='_truss_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary70',
    ),
    'boots': dict(
        outdir='_truss_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_truss',
    ),
    'helmet': dict(
        outdir='_trussdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary70',
    ),
}

NB8 = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

CONTROLS = ('tree', 'grid', 'trellis', 'collinear', 'dense', 'braced', 'whisker', 'swapped')


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
    """The parts of the piece big enough to be held at all.

    EVERY PART IS TRUSSED SEPARATELY. A framework is a local object - two legs are two structures,
    and a pauldron that is not touching the torso is not braced by it. Same reasoning as the 69th's
    (a potential is local) and the exact opposite of the 67th's (a census must be of everything)."""
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


def bres(a, b):
    """The pixels of the bar between two joints. A bar is STRAIGHT - that is not a stylistic choice,
    a bent bar is two bars and a joint, and the joint would be one the reader could not see.

    THE RUN IS CANONICAL IN ITS ENDPOINTS AND THAT COST A DAY. Bresenham breaks its ties toward the
    end it started from, so the same two joints traced the other way round give a DIFFERENT run of
    pixels on any bar whose slope lands on a half-pixel. The painter walks a bar from the joint it
    placed first and the reader walks it from the joint it happened to find first, so a reader that
    did not canonicalise lost one bar in five - and lost it silently, as a framework with a
    degree-one joint. Both ends now agree because both sort the endpoints before they start."""
    if (b[0], b[1]) < (a[0], a[1]):
        return list(reversed(bres(b, a)))
    y0, x0 = a
    y1, x1 = b
    dy, dx = abs(y1 - y0), abs(x1 - x0)
    sy = 1 if y1 > y0 else -1
    sx = 1 if x1 > x0 else -1
    err = dx - dy
    out = []
    y, x = y0, x0
    while True:
        out.append((y, x))
        if (y, x) == (y1, x1):
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return out


# --- the rigidity matrix -----------------------------------------------------------------------
def rigidity(J, E):
    """One row per bar, two columns per joint. THE WHOLE AXIS IS A STATEMENT ABOUT THIS MATRIX."""
    n = len(J)
    R = np.zeros((len(E), 2 * n))
    for r, (i, j) in enumerate(E):
        dy = float(J[i][0] - J[j][0])
        dx = float(J[i][1] - J[j][1])
        R[r, 2 * i] = dy
        R[r, 2 * i + 1] = dx
        R[r, 2 * j] = -dy
        R[r, 2 * j + 1] = -dx
    return R


def rank_of(J, E):
    if not E:
        return 0
    return int(np.linalg.matrix_rank(rigidity(J, E), tol=1e-7))


def dof_of(J, E):
    """dim ker R. Three of these are the plane's own translations and rotation; the rest are k."""
    return 2 * len(J) - rank_of(J, E)


# --- the construction --------------------------------------------------------------------------
def _vis(comp, js, a, b, minlen, used):
    """Is there a bar from a to b? It must lie inside the part, must not pass through a third
    joint, must be long enough to have a direction, and must not tread on another bar's pixels."""
    if max(abs(a[0] - b[0]), abs(a[1] - b[1])) < minlen:
        return None
    px = bres(a, b)
    for (y, x) in px:
        if not comp[y, x]:
            return None
    for p in px[1:-1]:
        if p in js or p in used:
            return None
    return px


def validate(comp, J, E, PX):
    """Can this framework be READ BACK off its own pixels, and does it read as a line drawing?

    THE LAW IS A THEOREM AND THE LEGIBILITY IS A SEARCH, and the file is honest about which is
    which. |E| = 2n-3-k and DOF = k are consequences of the construction: the painter cannot draw a
    framework with the wrong number of motions. But whether the picture SURVIVES BEING LOOKED AT is
    not a theorem about frameworks, it is a fact about a thirteen-pixel torso, so it is checked -
    and when it fails the part is drawn again with one joint fewer rather than shipped."""
    bar, joint, dark = paint(comp, J, E, PX)
    crest = bar | joint
    if blots(crest, joint):
        return False                     # a strut is a LINE and four crest pixels in a square is a blot
    h, w = comp.shape
    for (y, x) in np.argwhere(crest):
        if not any(0 <= y + dy < h and 0 <= x + dx < w and dark[y + dy, x + dx]
                   for dy, dx in NB8):
            return False                 # relief with no shadow is colour, and colour is camouflage
    rJ, rE, rPX = recover(comp, joint, bar)
    if len(rJ) != len(J):
        return False
    idx = {p: i for i, p in enumerate(rJ)}
    want = {tuple(sorted((idx[J[i]], idx[J[j]]))) for (i, j) in E}
    got = {tuple(sorted(e)) for e in rE}
    if want != got:
        return False                     # a bar the reader cannot see, or one it invents
    seen = set()
    for e in rE:
        for p in rPX[e][1:-1]:
            if p in seen:
                return False             # two bars treading on one pixel - clause CLEAR
            seen.add(p)
    return True


def _still_a_control(mode, J, E, k):
    if mode in ('dense', 'braced'):
        return len(E) > 2 * len(J) - 3 - k
    if mode == 'whisker':
        deg = [0] * len(J)
        for (i, j) in E:
            deg[i] += 1
            deg[j] += 1
        return min(deg) < 2
    if mode == 'tree':
        return len(E) == len(J) - 1
    return True


def truss_of(comp, k, mode=None):
    """The framework actually drawn on a part: the largest one that can be read back.

    The joint count comes down a step at a time, and within a count the seed is tried from a
    different starting pixel, until the picture is legible. It is the same shape of concession the
    69th makes when it lowers its band count until every band has a field to stand on, and for the
    same reason: THE BODY DISPOSES."""
    if mode in ('grid', 'trellis'):
        return build_truss(comp, k, mode)
    area = int(comp.sum())
    m = 3 + k
    top = max(m, min(JMAX, int(math.sqrt(area) / JDIV + 0.5)))
    if area < 3 * top:
        top = m
    for nwant in range(top, m - 1, -1):
        for skip in range(SEED_STARTS):
            got = build_truss(comp, k, mode, nwant=nwant, seed_skip=skip)
            if got is None:
                continue
            J, E, PX = got[0], got[1], got[2]
            # THE CONTROLS GET THE SAME PAINTER, INCLUDING THE SAME RETRIES. A control that was
            # denied the legibility search would fail LEGIBLE for a reason that has nothing to do
            # with its law, and the comparison would be worthless.
            #
            # BUT A CONTROL MUST STAY A CONTROL. The retry drops a joint at a time, and dropping
            # joints from an over-braced framework eventually lands on the seed, which is lawful:
            # controls DENSE and BRACED silently turned into the axis and scored zero violations,
            # which is the most flattering result in the file and completely meaningless. A retry
            # that has abolished the very thing the control is testing is not a retry, it is a
            # different control, so it is refused and the plate is reported undrawable instead.
            if validate(comp, J, E, PX) and _still_a_control(mode, J, E, k):
                return J, E, PX
    return None


def build_truss(comp, k, mode=None, nwant=None, seed_skip=0):
    """The framework of one part, from the mask and k and nothing else.

    Returns (J, E, PX) or None if the part cannot be held. THE PAINTER CANNOT DRAW AN UNLAWFUL
    PLATE: the seed is a (3+k)-cycle and every extension is a Henneberg type-I, so |E| = 2n-3-k and
    DOF = k are consequences of the construction rather than things that are checked afterwards."""
    area = int(comp.sum())
    minlen = MINLEN_SMALL if area < SMALL_AREA else MINLEN_BIG
    pts = [(int(y), int(x)) for y, x in np.argwhere(comp)]
    ys, xs = np.nonzero(comp)
    cy, cx = ys.mean(), xs.mean()

    if mode in ('grid', 'trellis'):
        return _lattice_control(comp, pts, mode, minlen)

    m = 3 + k
    if nwant is None:
        nwant = max(m, min(JMAX, int(math.sqrt(area) / JDIV + 0.5)))
        if area < 3 * nwant:
            nwant = m
    nwant = max(m, nwant)

    # THE SEED STARTS ARE SPREAD, NOT STACKED. Ordering the whole mask by distance from its own
    # centroid and taking the first six candidates gives six pixels in the SAME CORNER, so six
    # retries were one retry six times and two classes in three could not find a seed at all. The
    # starts are farthest-point samples of the part instead: six pixels as far from each other as
    # the mask allows, which is six genuinely different attempts.
    starts = [max(pts, key=lambda p: ((p[0] - cy) ** 2 + (p[1] - cx) ** 2, -p[0], -p[1]))]
    while len(starts) < SEED_STARTS and len(starts) < len(pts):
        starts.append(max((p for p in pts if p not in starts),
                          key=lambda p: (min((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                                             for q in starts), -p[0], -p[1])))
    budget = [SEED_BUDGET]

    def seed():
        """A CYCLE OF 3+k JOINTS. This is the class, and it is the only thing on the plate that is
        chosen rather than derived - and even it is derived, because the search order is a total
        order on the mask's own pixels."""
        # Each retry is a different STARTING PIXEL and a different DIRECTION ROUND THE
        # PART. Walking the seed only anticlockwise lost five walk poses of the mage's
        # and the ranger's chausses, where the leg the tour reaches first decides
        # whether the tour can get back.
        for start in starts[seed_skip // 2:seed_skip // 2 + 1]:
            J = [start]
            PX = {}
            used = set()

            def rec():
                if budget[0] <= 0:
                    return False
                if len(J) == m:
                    px = _vis(comp, set(J), J[-1], J[0], minlen, used)
                    if px is None:
                        return False
                    PX[(m - 1, 0)] = px
                    return True
                cur = J[-1]
                js = set(J)
                # VISIBILITY FIRST, SPREAD SECOND. Sorting the whole mask by spread and then
                # keeping the top eight threw away every pixel this joint could actually reach on a
                # concave part - a torso has an armpit in it, and the eight most distant pixels are
                # all on the other side of it.
                seen = []
                for p in pts:
                    if p in js:
                        continue
                    budget[0] -= 1
                    if budget[0] <= 0:
                        break
                    px = _vis(comp, js | {p}, cur, p, minlen, used)
                    if px is not None:
                        seen.append((p, px))
                # THE SEED IS WALKED ROUND, NOT SCATTERED. Ordering the candidates by "farthest
                # from everything chosen so far" builds a zigzag: the tour crosses itself, the
                # closing bar treads on the opening one, and a ranger hat forty-five pixels wide
                # could not be given a quadrilateral at all. Preferring the candidate whose ANGLE
                # about the part's centroid is one step of 2*pi/m ahead of the current joint walks
                # the seed round the part instead, and a simple polygon comes out.
                step = (1 if seed_skip % 2 == 0 else -1) * 2 * math.pi / m
                th0 = math.atan2(cur[0] - cy, cur[1] - cx)

                def akey(t):
                    p = t[0]
                    d = (math.atan2(p[0] - cy, p[1] - cx) - th0) % (2 * math.pi)
                    if step < 0:
                        d -= 2 * math.pi
                    return (abs(d - step), -((p[0] - cur[0]) ** 2 + (p[1] - cur[1]) ** 2),
                            p[0], p[1])
                seen.sort(key=akey)
                for p, px in seen[:SEED_BREADTH]:
                    J.append(p)
                    for q in px[1:-1]:
                        used.add(q)
                    PX[(len(J) - 2, len(J) - 1)] = px
                    if rec():
                        return True
                    PX.pop((len(J) - 2, len(J) - 1), None)
                    for q in px[1:-1]:
                        used.discard(q)
                    J.pop()
                return False

            if rec():
                E = [(i, i + 1) for i in range(m - 1)] + [(m - 1, 0)]
                # A cycle is independent and has exactly m-3 motions ONLY IF its joints are in
                # general position; a degenerate seed is refused here rather than shipped.
                if rank_of(J, E) == len(E) and dof_of(J, E) - 3 == k:
                    return J, E, PX, used
        return None

    s = seed()
    if s is None:
        return None
    J, E, PX, used = s
    if _ink(PX, area) > INK_MAX:
        return None
    js = set(J)

    def extend(nbars):
        """A HENNEBERG TYPE-I EXTENSION: one new joint, exactly two bars to joints already placed.
        It changes neither the independence of the framework nor its number of motions - that is a
        theorem, and it is why this axis has no search in it."""
        cands = sorted((p for p in pts if p not in js),
                       key=lambda p: (-min((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 for q in J),
                                      p[0], p[1]))[:EXT_POOL]
        for p in cands:
            seen = []
            for i, q in enumerate(J):
                px = _vis(comp, js | {p}, p, q, minlen, used)
                if px is not None:
                    seen.append((len(px), i, px))
            if len(seen) < nbars:
                continue
            seen.sort(key=lambda t: (t[0], t[1]))
            for combo in itertools.combinations(seen, nbars):
                inner = [set(t[2][1:-1]) for t in combo]
                if any(inner[x] & inner[y] for x in range(nbars) for y in range(x + 1, nbars)):
                    continue
                J2 = J + [p]
                E2 = E + [(t[1], len(J)) for t in combo]
                if nbars == 2:
                    # THE ONLY TWO CHECKS IN THE PAINTER, AND BOTH ARE ABOUT DEGENERACY RATHER
                    # THAN ABOUT THE LAW: a Henneberg type-I extension is independent and
                    # motion-preserving by theorem, unless the new joint happens to land ON the
                    # line through the two it attaches to, in which case the theorem's general
                    # position hypothesis fails and this is exactly what control COLLINEAR is.
                    if rank_of(J2, E2) != len(E2):
                        continue
                    if dof_of(J2, E2) - 3 != k:
                        continue
                return p, combo
        return None

    nbars = 3 if mode == 'dense' else 2
    while len(J) < nwant:
        if _ink(PX, area) > INK_STOP:
            break
        got = extend(nbars)
        if got is None:
            break
        p, combo = got
        J.append(p)
        js.add(p)
        for (_l, i, px) in combo:
            E.append((i, len(J) - 1))
            PX[(i, len(J) - 1)] = px
            for q in px[1:-1]:
                used.add(q)

    if mode == 'tree':
        # THE 66th's OWN STRUCTURE: keep a spanning tree of the bars, in the order they were laid.
        keep, seen = [], {0}
        for (i, j) in E:
            if (i in seen) != (j in seen):
                keep.append((i, j))
                seen.add(i)
                seen.add(j)
        E = keep
        PX = {e: PX[e] for e in E}
    elif mode == 'braced':
        for i in range(len(J)):
            for j in range(i + 1, len(J)):
                if (i, j) in PX or (j, i) in PX:
                    continue
                px = _vis(comp, js, J[i], J[j], minlen, used)
                if px is None:
                    continue
                E.append((i, j))
                PX[(i, j)] = px
                return J, E, PX
    elif mode == 'whisker':
        got = extend(1)
        if got is not None:
            p, combo = got
            J.append(p)
            for (_l, i, px) in combo:
                E.append((i, len(J) - 1))
                PX[(i, len(J) - 1)] = px
    elif mode == 'collinear':
        # SAME GRAPH, JOINTS SLID ONTO THE PART'S PRINCIPAL AXIS. Combinatorially identical to the
        # shipped item; geometrically a different object, and the rank knows it.
        pca = _axis_points(comp, len(J))
        if pca is None:
            return None
        J2 = pca
        PX2 = {}
        for (i, j) in E:
            px = bres(J2[i], J2[j])
            if not all(comp[y, x] for y, x in px):
                return None
            PX2[(i, j)] = px
        return J2, E, PX2

    return J, E, PX


def _ink(PX, area):
    s = set()
    for px in PX.values():
        s |= set(px)
    return 2.0 * len(s) / max(area, 1)


def _axis_points(comp, n):
    """n joints spread along ONE ROW of the part - control COLLINEAR.

    THE POINTS HAVE TO BE EXACTLY COLLINEAR OR THE CONTROL MEASURES NOTHING. The first draft slid
    the joints onto the part's principal axis and then rounded them to the nearest pixel, which put
    them NEAR a line and not ON one: integer rounding is enough to restore general position, the
    rank never dropped, and the control scored 0 of 355. Putting every joint on the part's widest
    row is exact, and the rank knows it immediately."""
    ys, xs = np.nonzero(comp)
    rows = {}
    for y, x in zip(ys, xs):
        rows.setdefault(int(y), []).append(int(x))
    y0 = max(rows, key=lambda r: (len(rows[r]), -r))
    cols = sorted(rows[y0])
    if len(cols) < n:
        return None
    picks = [cols[int(round(i * (len(cols) - 1) / (n - 1)))] for i in range(n)]
    out = [(y0, c) for c in picks]
    if len(set(out)) < n:
        return None
    return out


def _lattice_control(comp, pts, mode, minlen):
    """Controls GRID (= the 14th LATTICE) and TRELLIS (= the 20th), drawn by this painter."""
    ys, xs = np.nonzero(comp)
    y0, x0 = int(ys.min()), int(xs.min())
    step = 3
    grid = {}
    for p in pts:
        if (p[0] - y0) % step == 0 and (p[1] - x0) % step == 0:
            grid[((p[0] - y0) // step, (p[1] - x0) // step)] = p
    if len(grid) < 4:
        return None
    keys = sorted(grid)
    J = [grid[kk] for kk in keys]
    idx = {kk: i for i, kk in enumerate(keys)}
    E, PX = [], {}

    def add(ka, kb):
        if ka not in idx or kb not in idx:
            return
        a, b = J[idx[ka]], J[idx[kb]]
        px = bres(a, b)
        if not all(comp[y, x] for y, x in px):
            return
        E.append((idx[ka], idx[kb]))
        PX[(idx[ka], idx[kb])] = px

    for (r, c) in keys:
        add((r, c), (r, c + 1))
        add((r, c), (r + 1, c))
        if mode == 'trellis':
            add((r, c), (r + 1, c + 1))
    if not E:
        return None
    return J, E, PX


# --- painting ----------------------------------------------------------------------------------
def paint(comp, J, E, PX):
    """Bars in the third stop, joints in the fourth, and a dark witness laid against every crest
    pixel that can have one. RELIEF, NOT COLOUR - a flat field of a different hue reads as
    camouflage at 13px and only a crest with its own shadow survives the finishing pass."""
    bar = np.zeros(comp.shape, bool)
    joint = np.zeros(comp.shape, bool)
    for e in E:
        for (y, x) in PX[e]:
            bar[y, x] = True
    for (y, x) in J:
        joint[y, x] = True
        bar[y, x] = False
    dark = np.zeros(comp.shape, bool)
    h, w = comp.shape
    for (y, x) in np.argwhere(bar | joint):
        for (ny, nx) in NB8:
            ny, nx = y + ny, x + nx
            if 0 <= ny < h and 0 <= nx < w and comp[ny, nx] and not bar[ny, nx] \
                    and not joint[ny, nx]:
                dark[ny, nx] = True
                break
    return bar, joint, dark


def blots(crest, joint):
    """2x2 blocks of crest that are NOT at a joint.

    A BLOT AT A JOINT IS NOT A BLOT, IT IS A JOINT, and that distinction is the whole reason this
    clause survived contact with a thirteen-pixel torso. Three bars meeting at a pixel necessarily
    thicken there - a Bresenham run leaves a staircase, and two staircases arriving from different
    quarters put four crest pixels in a square whether you like it or not. Refusing every such
    square cost 174 of the first 200 warrior torsos their ornament. Refusing them only where no
    joint is within one pixel keeps the rule that matters (A STRUT IS A LINE) and drops the rule
    that was only ever an accident of rasterisation."""
    h, w = crest.shape
    near = joint.copy()
    for dy, dx in NB8:
        near |= np.roll(np.roll(joint, dy, 0), dx, 1)
    blk = crest[:-1, :-1] & crest[1:, :-1] & crest[:-1, 1:] & crest[1:, 1:]
    safe = near[:-1, :-1] | near[1:, :-1] | near[:-1, 1:] | near[1:, 1:]
    return bool((blk & ~safe).any())


def build_frame(fr, a, cls, mode=None, k_override=None):
    """One pose. Returns (bar, joint, dark) or None if no part of the pose could be held."""
    k = KDOF[cls] if k_override is None else k_override
    if mode == 'swapped':
        k = SWAP_K[cls]
    dark_c, field_c, bar_c, joint_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE BARS GO ON. The source sheet's inherited highlights are the
    # same stop the bars are painted in, and a reader told nothing cannot tell an inherited
    # highlight from a strut. Every tone on a trussed plate is put there by the framework; the
    # modelling comes back, richer, from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    allb = np.zeros(a.shape, bool)
    allj = np.zeros(a.shape, bool)
    alld = np.zeros(a.shape, bool)
    parts = parts_of(a)
    for comp in parts:
        got = truss_of(comp, k, mode)
        if got is None:
            # A PART THAT CANNOT BE HELD IS LEFT PLAIN AND COUNTED, NOT FAKED. A mage needs five
            # joints and a warrior three; a fourteen-pixel sabaton has a triangle in it and no
            # pentagon, and that is a theorem rather than a shortfall.
            continue
        J, E, PX = got[0], got[1], got[2]
        b, j, d = paint(comp, J, E, PX)
        allb |= b
        allj |= j
        alld |= d
    if not allj.any() and parts:
        return None
    for y, x in np.argwhere(alld):
        put(fr, y, x, dark_c)
    for y, x in np.argwhere(allb):
        put(fr, y, x, bar_c)
    for y, x in np.argwhere(allj):
        put(fr, y, x, joint_c)
    return allb, allj, alld


def frames_of(base):
    for fi in range(SLEEP_FROM):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a = base[sl][..., 3] > 0
        if a.any():
            yield fi, sl, a


def one_plate(base, sl, a, cls, mode=None, k_override=None):
    fr = np.zeros((FH, FW, 4), base.dtype)
    D, M, L = BODY[cls]
    recolor(base[sl], fr, a, D, M, L)
    got = build_frame(fr, a, cls, mode, k_override)
    return fr, got


def sheet_carries(base, cls, mode=None):
    """A SHEET IS TRUSSED IN ALL FORTY-TWO POSES OR IN NONE. An ornament that appears in some frames
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

    # FIX: compute the truss framework from the intersection of the IDLE frames
    # (row 0, fr0-4).  The all-frames intersection gave only ~11 stable pixels
    # because arm movement across walk/run heavily changes the shirt silhouette.
    # The idle-only intersection gives ~120 stable pixels — enough for a full
    # truss — and those pixels are present in every idle frame, so the pattern
    # never flickers during idle.  Other poses get the same fixed grid clipped
    # to their own alpha, keeping the bars visually anchored.
    k = KDOF[cls] if mode != 'swapped' else SWAP_K[cls]
    dark_c, field_c, bar_c, joint_c = PAL[cls]

    IDLE_FRAMES = range(5)   # row 0, cols 0-4

    ref_a = None
    for fi in IDLE_FRAMES:
        r, c = fi // COLS, fi % COLS
        sl0 = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a0 = base[sl0][..., 3] > 0
        if not a0.any():
            continue
        ref_a = a0.copy() if ref_a is None else (ref_a & a0)

    ref_allb = ref_allj = ref_alld = None
    if ref_a is not None and ok:
        allb = np.zeros(ref_a.shape, bool)
        allj = np.zeros(ref_a.shape, bool)
        alld = np.zeros(ref_a.shape, bool)
        for comp in parts_of(ref_a):
            got = truss_of(comp, k, mode)
            if got is None:
                continue
            J, E, PX = got[0], got[1], got[2]
            b, j, d = paint(comp, J, E, PX)
            allb |= b; allj |= j; alld |= d
        if allb.any() or allj.any() or alld.any():
            ref_allb, ref_allj, ref_alld = allb, allj, alld

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
        for y, x in np.argwhere(a):
            put(out[sl], y, x, field_c)
        if ref_allb is not None:
            for y, x in np.argwhere(ref_alld):
                if a[y, x]:
                    put(out[sl], y, x, dark_c)
            for y, x in np.argwhere(ref_allb):
                if a[y, x]:
                    put(out[sl], y, x, bar_c)
            for y, x in np.argwhere(ref_allj):
                if a[y, x]:
                    put(out[sl], y, x, joint_c)
    return out, ok


# --- the reader --------------------------------------------------------------------------------
def read_stops(fr, a):
    """Joints, bars and witnesses off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: the
    brightest luminance on the piece is the joints, the next is the bars, the darkest is the
    witness. A plate with fewer than three stops has no ornament on it."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    pts = np.argwhere(a)
    joint = np.zeros(a.shape, bool)
    bar = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    if len(pts) == 0:
        return joint, bar, dark
    vals = sorted({int(lum[y, x]) for y, x in pts})
    if len(vals) < 3:
        return joint, bar, dark
    jv, bv, dv = vals[-1], vals[-2], vals[0]
    for y, x in pts:
        v = int(lum[y, x])
        if v == jv:
            joint[y, x] = True
        elif v == bv:
            bar[y, x] = True
        elif v == dv:
            dark[y, x] = True
    return joint, bar, dark


def recover(comp, joint, bar):
    """The framework, recovered from the pixels of one part with no help of any kind.

    A pair of joints is a BAR if the straight run between them is entirely crest and holds no third
    joint in its interior. Spurious pairs are possible in principle - three joints in a row - and
    clause CLEAR is what catches them: a spurious bar necessarily treads on the pixels of the bars
    it was mistaken for, and the recovered bars are required to have disjoint interiors."""
    J = [(int(y), int(x)) for y, x in np.argwhere(joint & comp)]
    js = set(J)
    crest = (joint | bar) & comp
    E, PX = [], {}
    for i in range(len(J)):
        for j in range(i + 1, len(J)):
            px = bres(J[i], J[j])
            if not all(crest[y, x] for y, x in px):
                continue
            if any(p in js for p in px[1:-1]):
                continue
            E.append((i, j))
            PX[(i, j)] = px
    return J, E, PX


def laman_sparse(n, E):
    """No set of s joints spans more than 2s-3 bars. Coordinate-free, and exhaustive for n <= 12."""
    if n > 12:
        return 0
    bad = 0
    idx = range(n)
    for s in range(2, n + 1):
        for S in itertools.combinations(idx, s):
            SS = set(S)
            cnt = sum(1 for (i, j) in E if i in SS and j in SS)
            if cnt > 2 * s - 3:
                bad += 1
    return bad


# --- the acceptance test -----------------------------------------------------------------------
def inspect_frame(fr, a, k):
    """The six clauses on ONE POSE. Returns a dict of violation counts plus what was read."""
    v = dict(flex=0, tight=0, sparse=0, closed=0, clear=0, legible=0,
             parts=0, silent=0, bars=0, joints=0, kread=[])
    joint, bar, dark = read_stops(fr, a)
    for comp in parts_of(a):
        v['parts'] += 1
        cj = joint & comp
        cb = bar & comp
        if not cj.any():
            v['silent'] += 1
            continue
        J, E, PX = recover(comp, joint, bar)
        n = len(J)
        v['joints'] += n
        v['bars'] += len(E)
        # (5) CLEAR - disjoint interiors, and the bars account for every crest pixel
        seen = set()
        overlap = 0
        for e in E:
            for p in PX[e][1:-1]:
                if p in seen:
                    overlap += 1
                seen.add(p)
        cover = np.zeros(a.shape, bool)
        for e in E:
            for (y, x) in PX[e]:
                cover[y, x] = True
        if overlap or ((cj | cb) != (cover & comp)).any():
            v['clear'] += 1
        # (4) CLOSED - degree >= 2 everywhere, one piece
        deg = [0] * n
        for (i, j) in E:
            deg[i] += 1
            deg[j] += 1
        adj = {i: set() for i in range(n)}
        for (i, j) in E:
            adj[i].add(j)
            adj[j].add(i)
        reach, st = {0} if n else set(), [0] if n else []
        while st:
            u = st.pop()
            for w in adj[u]:
                if w not in reach:
                    reach.add(w)
                    st.append(w)
        if n < 3 or min(deg) < 2 or len(reach) != n:
            v['closed'] += 1
        # (2) TIGHT - every bar independent
        r = rank_of(J, E)
        if r != len(E):
            v['tight'] += 1
        # (1) FLEX - dim ker R = 3 + k, and k is an OUTPUT
        kk = 2 * n - r - 3
        v['kread'].append(kk)
        if kk != k:
            v['flex'] += 1
        # (3) SPARSE - the Laman count
        if laman_sparse(n, E):
            v['sparse'] += 1
        # (6) LEGIBLE - a witness for every crest pixel, and no 2x2 crest block
        crest = cj | cb
        h, w = a.shape
        for (y, x) in np.argwhere(crest):
            if not any(0 <= y + dy < h and 0 <= x + dx < w and dark[y + dy, x + dx]
                       for dy, dx in NB8):
                v['legible'] += 1
                break
        if blots(crest, cj):
            v['legible'] += 1
    return v


def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict(flex=0, tight=0, sparse=0, closed=0, clear=0, legible=0,
               plates=0, silent=0, sheets=0, pass_sheets=0)
    for kind, cfg in SLOTS.items():
        if only and kind != only:
            continue
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (cfg['srcs'][cls], suffix))
                # THE POSES ARE BUILT ONCE. sheet_carries() would build all forty-two of them a
                # second time, and a rigidity solve per part per pose is not cheap enough to pay
                # for twice.
                plates_of_sheet = [(fi, a, one_plate(base, sl, a, cls))
                                   for fi, sl, a in frames_of(base)]
                ok = all(p[2][1] is not None for p in plates_of_sheet)
                tot['sheets'] += 1
                if not ok:
                    print('   %-7s %-8s %-2s  PLAIN (reported)' % (kind, cls, suffix or 'm'),
                          flush=True)
                    continue
                bad = dict.fromkeys(('flex', 'tight', 'sparse', 'closed', 'clear', 'legible'), 0)
                plates = silent = 0
                for fi, a, (fr, _got) in plates_of_sheet:
                    v = inspect_frame(fr, a, KDOF[cls])
                    for c in bad:
                        bad[c] += v[c]
                    plates += v['parts']
                    silent += v['silent']
                tot['plates'] += plates
                tot['silent'] += silent
                for c in bad:
                    tot[c] += bad[c]
                good = not any(bad.values())
                tot['pass_sheets'] += 1 if good else 0
                print('   %-7s %-8s %-2s  k=%d  plates=%-4d silent=%-3d  %s%s'
                      % (kind, cls, suffix or 'm', KDOF[cls], plates, silent,
                         'ALL PASS' if good else 'FAIL ',
                         '' if good else ' ' + ' '.join('%s=%d' % (c, n)
                                                        for c, n in bad.items() if n)),
                      flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d silent (too small to hold)'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['silent']))
    for c in ('flex', 'tight', 'sparse', 'closed', 'clear', 'legible'):
        print('   clause %-8s violations %d' % (c.upper(), tot[c]))


def collinear_probe():
    """CONTROL COLLINEAR, MEASURED RATHER THAN DRAWN.

    Sliding a framework's joints onto the part's own principal axis produces a picture in which
    every bar lies on top of every other bar, so the control is DEAD: not one plate in forty-eight
    can be drawn at all, and a control that cannot be drawn cannot be put through the reader. The
    geometric point it exists to make survives anyway, and this is the measurement: take each
    SHIPPED framework, keep its graph exactly - same joints, same bars, same class - and move the
    joints onto the axis. The graph is untouched and the LAMAN COUNT IS UNTOUCHED, so any framework
    that gains a motion here has gained it from its POSITIONS. That is the whole reason clause FLEX
    is the rank of R at the plate's real coordinates and not a combinatorial count."""
    print('== COLLINEAR, MEASURED  (same graph, joints slid onto the part\'s principal axis)')
    for kind, cfg in SLOTS.items():
        moved = same = 0
        gained = []
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            for fi, sl, a in frames_of(base):
                for comp in parts_of(a):
                    got = truss_of(comp, KDOF[cls])
                    if got is None:
                        continue
                    J, E, _PX = got
                    flat = _axis_points(comp, len(J))
                    if flat is None:
                        continue
                    d0 = dof_of(J, E) - 3
                    d1 = dof_of(flat, E) - 3
                    if d1 != d0:
                        moved += 1
                        gained.append(d1 - d0)
                    else:
                        same += 1
        print('   %-7s frameworks that GAIN motions from the slide: %4d, unchanged %4d  '
              '(extra motions %s)'
              % (kind, moved, same, sorted(set(gained)) or '-'), flush=True)


def controls_report(only=None):
    if only == 'collinear':
        collinear_probe()
        return
    print('== CONTROLS  (the same reader, the same relief, the same palette)')
    print('   %-10s %-8s %s' % ('control', 'drawn', 'violations / note'))
    for mode in (CONTROLS if not only else [only]):
        agg = dict.fromkeys(('flex', 'tight', 'sparse', 'closed', 'clear', 'legible'), 0)
        drawn = undrawable = 0
        kreads = []
        for kind, cfg in SLOTS.items():
            for cls in cfg['srcs']:
                base = load_any('%s.png' % cfg['srcs'][cls])
                for fi, sl, a in frames_of(base):
                    if fi % 7:
                        continue
                    fr, got = one_plate(base, sl, a, cls, mode)
                    if got is None:
                        undrawable += 1
                        continue
                    drawn += 1
                    v = inspect_frame(fr, a, KDOF[cls])
                    for c in agg:
                        agg[c] += v[c]
                    kreads += v['kread']
        note = ' '.join('%s=%d' % (c.upper(), n) for c, n in agg.items() if n) or 'NOTHING FAILS'
        extra = ''
        if mode == 'swapped':
            extra = '  <- lawful and MISNAMED: FLEX reads k=%s, the class it actually is' % \
                    sorted(set(kreads))
        if mode in ('tree', 'grid'):
            extra = '  <- DOF read %s (class wants 0/1/2)' % sorted(set(kreads))[:6]
        print('   %-10s %-8d %s%s' % (mode.upper(), drawn, note, extra), flush=True)
        if undrawable:
            print('   %-10s %-8s %d plates could not be drawn at all' % ('', '', undrawable))


def sweep():
    print('== SLOTS  (can every pose be held, and does it read back)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (cfg['srcs'][cls], suffix))
                fit = unfit = 0
                bars = []
                for fi, sl, a in frames_of(base):
                    fr, got = one_plate(base, sl, a, cls)
                    if got is None:
                        unfit += 1
                        continue
                    v = inspect_frame(fr, a, KDOF[cls])
                    if any(v[c] for c in ('flex', 'tight', 'sparse', 'closed', 'clear', 'legible')):
                        unfit += 1
                    else:
                        fit += 1
                        bars.append(v['bars'])
                print('   %-7s %-8s %-2s  k=%d  bars %2d-%-3d  poses %2d/%-2d  SHEET %s'
                      % (kind, cls, suffix or 'm', KDOF[cls],
                         min(bars) if bars else 0, max(bars) if bars else 0,
                         fit, fit + unfit,
                         'trussed' if unfit == 0 else 'PLAIN (reported)'))


def frame_dump():
    print('== ONE REAL COMPONENT PER CLASS  ("*" joint, "O" bar, "=" witness, "-" field)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        base = load_any('%s.png' % cfg['srcs'][cls])
        for fi, sl, a in frames_of(base):
            parts = parts_of(a)
            if not parts:
                continue
            comp = max(parts, key=lambda c: c.sum())
            got = truss_of(comp, KDOF[cls])
            if got is None:
                continue
            J, E, PX = got[0], got[1], got[2]
            bar, joint, dark = paint(comp, J, E, PX)
            ys, xs = np.nonzero(comp)
            print('== %s chest frame %d   seed=%d-gon  %d joints  %d bars  DOF-3 = %d'
                  % (cls, fi, 3 + KDOF[cls], len(J), len(E), dof_of(J, E) - 3))
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not comp[y, x]:
                        row += '.'
                    elif joint[y, x]:
                        row += '*'
                    elif bar[y, x]:
                        row += 'O'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a bar on the
    shadowed flank is darker in absolute terms than the field on the lit one."""
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
                b, j, d = got
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for y, x in np.argwhere(b | j):
                    nb = [lum[ny, nx] for ny, nx in
                          ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                          if 0 <= ny < FH and 0 <= nx < FW and d[ny, nx]]
                    if not nb:
                        continue
                    tot += 1
                    if lum[y, x] > float(np.mean(nb)):
                        ok += 1
        print('   %-7s crest still lighter than its own witness: %5d/%-5d (%3d%%)'
              % (kind, ok, tot, (100 * ok // tot) if tot else 0))


def main():
    if '--frame' in sys.argv:
        frame_dump()
        return
    if '--accept' in sys.argv:
        i = sys.argv.index('--accept')
        accept(sys.argv[i + 1] if len(sys.argv) > i + 1 else None)
        return
    if '--controls' in sys.argv:
        i = sys.argv.index('--controls')
        controls_report(sys.argv[i + 1] if len(sys.argv) > i + 1 else None)
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
                         'k=%d' % KDOF[cls] if ok else 'PLAIN (reported)'))


if __name__ == '__main__':
    main()
