#!/usr/bin/env python3
"""SEVENTY-THIRD net-new-geometry axis for ALL FOUR SLOTS - the SURVEY family: the ornament is a set
of BEACONS, and the law is that they give every pixel of the garment AN ADDRESS OF ITS OWN.

    the ornament is  a BEACON    a bright CORE pixel with its four orthogonal ARMS, drawn wherever
                                 the cloth has room for them - and EVERY ARM THAT IS MISSING IS
                                 MISSING BECAUSE THERE IS NO CLOTH TO PUT IT ON, which the reader
                                 can check against the silhouette and which is the whole of what
                                 makes the figure's centre nameable
    the address of   ANY PIXEL   its list of distances to the beacon centres, in the plate's own
                                 order (nearest first is not needed: the law is symmetric in the
                                 beacons, which no previous axis's has been)
    the law is       NO TWO PIXELS OF THE PIECE SHARE AN ADDRESS

*** THIS IS THE FIRST INVARIANT WHOSE SUBJECT IS THE PIXELS THAT CARRY NO ORNAMENT. ***
Seventy-two axes state a law about the marks. The 68th SEME's displacements, the 70th TRUSS's bars,
the 71st GAMBIT's stalks, the 72nd QUORUM's rods: in every one of them, delete the ornament and you
have deleted the thing the law is about. HERE THE ORNAMENT IS THE INSTRUMENT AND THE PLAIN FIELD IS
THE SUBJECT. Every beacon pixel exists only to be measured FROM; what the law constrains is the
cloth between them, which carries no crest at all and which no previous axis has ever said anything
about. The 69th ANNEAL came nearest and came from the other side - there the interior was the part
NOBODY AUTHORED; here it is the part the law is entirely about.

*** IT IS THE EXACT COMPLEMENT OF THE 68th SEME, AND THE TWO ARE INDISTINGUISHABLE BY EYE. ***
    68th SEME     no two displacements BETWEEN THE MARKS repeat        - a law about the ornament
    73rd SURVEY   no two addresses OF THE GROUND repeat                - a law about everything else
Both are scattered dots on a plain field. One forbids the marks to say the same thing twice about
each other; the other forbids the CLOTH to say the same thing twice about the marks. There is no
third half of a picture for a law to be about.

*** IT IS THE EXACT COMPLEMENT OF THE 62nd DATUM. ***
The 62nd had ONE origin and it lay OUTSIDE the piece (the wearer's skull crown), and what it fixed
was where the ornament goes. This has SEVERAL origins, all of them ON the piece, and what they fix
is where the PIECE goes - not on the body, but in a system of coordinates the plate carries with it.

*** THIS IS THE FIRST INVARIANT THAT DEPENDS ON THE FINENESS OF THE READER'S INSTRUMENT. ***
    71st GAMBIT   the answer needs an OPPONENT      - a fact about a mind
    72nd QUORUM   the answer needs a HOLDING        - a fact about how much of the plate you have
    73rd SURVEY   the answer needs an INSTRUMENT    - a fact about how well you can MEASURE
Three consecutive axes in which the invariant is partly a fact about the reader, and this is the
third and last kind: what the reader wants, what the reader holds, WHAT THE READER CAN SEE.

*** CLASS IDENTITY IS A PRECISION - THE COARSEST RULE UNDER WHICH THE SURVEY STILL STANDS. ***
Four rules, each a function of the one above it, so they form a CHAIN and "the coarsest that works"
is a well-defined thing to read off a plate:

    EXACT    q                     the squared distance itself
    HALF     floor(2*sqrt(q))      distances known to the half pixel
    STEP     floor(sqrt(q))        distances known to the whole pixel
    COARSE   floor(sqrt(q)) // 2   distances known to within two pixels

    warrior  STEP     legible to a reader who can only count whole pixels
    ranger   HALF     legible to a reader with half a pixel in hand
    mage     EXACT    legible only to a reader who measures exactly, and to nobody else

Not a count (67th), a ceiling (68th), a multipole order (69th), a number of motions (70th), a
fraction of a move (71st) or the size of a coalition (72nd): A TOLERANCE ON SOMEBODY ELSE'S RULER.
It is an OUTPUT - the reader tries the rules coarsest-first and reports the first that works - and
because the rules are nested, THE ANSWER IS UNIQUE AND CANNOT BE ARGUED WITH.

*** THE AMOUNT OF ORNAMENT IS DERIVED AND NOT CHOSEN, WHICH IS NEW. ***
Nobody tells this axis how many beacons to draw. The class fixes the precision; the precision and
the body between them fix the count, and the painter draws exactly as many as the law needs and
then TAKES BACK every one it can do without. Measured over the wardrobe: THE BLUNTER THE
INSTRUMENT, THE MORE BEACONS THE PLATE MUST CARRY - the mage settles at two on almost every pose,
the ranger at three, the warrior at four to six. In seventy-two axes the quantity of ornament has
been a constant, a class identity or a fit to the body. Here it is a CONSEQUENCE, and the sweep
prints it as one.

*** THE CLASS THAT IS HARDEST TO DRAW IS THE EASIEST TO READ, WHICH INVERTS THE WHOLE PROJECT. ***
Every previous axis's expensive class is expensive on its own account - the 71st's warrior needs
two stalks because of what a stalk is worth, the 72nd's needs four rods because four is what a
warrior means. THE WARRIOR HERE IS EXPENSIVE ON BEHALF OF SOMEBODY ELSE: it carries the extra
beacons so that a careless reader, one who cannot tell 4.9 pixels from 5.1, can still find out
where he is standing. The mage's plate is the cheapest to draw and the only one a careless reader
cannot read at all. THE COST OF THE PLATE IS THE READER'S COMFORT.

*** THE ACCEPTANCE TEST IS A NEW KIND: A SURVEY. ***
The reader recovers the beacons off the pixels, takes their centres, and then STANDS ON EVERY PIXEL
OF THE PIECE IN TURN and writes down what it can see. Six clauses:

    (1) GROUND     every crest figure is a beacon: exactly one core, arms exactly on those four
                   neighbours that are cloth and on no others, and at least one full opposite pair
                   of them so the figure has an axis. THE MISSING ARMS ARE CHECKED AGAINST THE
                   SILHOUETTE - a clipped beacon is lawful, a PRUNED one is not, and the reader can
                   tell the difference without being told which is which.
    (2) SURVEY     no two pixels of the piece share an address under the class's rule. THE LAW.
    (3) PRECISION  the survey FAILS one rule coarser. THE FIRST CLAUSE IN THE PROJECT THAT DEMANDS
                   THE ORNAMENT BE INSUFFICIENT FOR SOMETHING - the plate must be exactly as legible
                   as its class and not one step more, or it is a different class wearing this one's
                   colours. This is what makes the class an output rather than a label.
    (4) TIGHT      no proper subset of the beacons resolves. NOTHING ON THE PLATE IS SPARE.
    (5) CLEAR      beacons stand a pixel apart, account for every crest pixel, and no 2x2 block of
                   crest anywhere.
    (6) LEGIBLE    a dark witness beside every beacon.

*** THE MAGE IS LEGIBLE BY ARITHMETIC AND NOT BY DESIGN, AND THE FILE WOULD RATHER SAY SO. ***
Two pixels share an EXACT address under two beacons if and only if they are reflections of one
another in the line through the two beacon centres. Reflection in a line of direction (a,b) takes
the integer lattice into itself only when the lattice respects that direction - horizontal,
vertical, or either 45 degree diagonal; for any other direction it maps all but a sparse sublattice
OFF the lattice altogether, so there is nothing for a pixel to collide with. THE MAGE'S TWO BEACONS
RESOLVE ITS PLATE BECAUSE THEY DO NOT LIE ALONG A DIRECTION THE PIXEL GRID RESPECTS, and control
ALIGNED is that sentence switched off. Run `--controls aligned-why` for the direction of every
mage pair in the wardrobe and the count of lawful ones that are axis-parallel or diagonal.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_survey_axis73.py                     # write the four staged preview dirs
    python3 scripts/gen_survey_axis73.py --sweep             # can every pose carry a survey
    python3 scripts/gen_survey_axis73.py --accept            # six clauses, every pose, every sheet
    python3 scripts/gen_survey_axis73.py --controls          # the nine controls
    python3 scripts/gen_survey_axis73.py --controls aligned-why   # the lattice theorem, measured
    python3 scripts/gen_survey_axis73.py --frame             # one real component per class
    python3 scripts/gen_survey_axis73.py --survive           # relief through the finishing pass
"""
import hashlib
import itertools
import os
import sys

import numpy as np
from PIL import Image  # noqa: F401  (kept for parity with the other generators)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
SLEEP_FROM = 60
Q_LO, Q_HI = 0.85, 1.18

MIN_PX = 10
POOL = 28            # how many well-spread candidate centres the painter is offered
RESTARTS = 28        # how many of them are tried as a FORCED first beacon (see greedy())
MAXB = 7             # a plate that needs more beacons than this has no room for them anyway

NB4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
NB8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

# THE CHAIN OF RULES. Each is a function of the one below it, which is what makes "the coarsest
# rule that still resolves" a thing a reader can read off a plate rather than a thing a painter has
# to declare. COARSE exists only so that every class - the warrior included - has a rule one step
# below its own for clause PRECISION to break.
RULES = ('coarse', 'step', 'half', 'exact')
R = {'warrior': 1, 'ranger': 2, 'mage': 3}
SWAP_R = {'warrior': 2, 'ranger': 3, 'mage': 1}

# Four stops per class, strictly increasing in luminance - (witness, field, arm, core). None near
# black: a near-black darkest stop eats the visor's eye and mouth pixels (the 49th's lesson).
# Deliberately unrelated to the 69th (copper/plum/smoked steel), 70th (blackened brass/slate
# blue/verdigris), 71st (oxblood/moss/violet), 72nd (indigo/moonwhite, umber/wheat, jade/seafoam).
#   warrior  GRAPHITE AND SIGNAL ORANGE   - the colour a surveyor paints a benchmark
#   ranger   MULBERRY AND LINEN
#   mage     AUBERGINE AND CITRON
PAL = {
    'warrior': ((40, 42, 48), (92, 96, 106), (176, 116, 58), (255, 190, 96)),
    'ranger':  ((58, 36, 48), (116, 72, 92), (172, 120, 132), (248, 240, 228)),
    'mage':    ((44, 32, 56), (88, 68, 104), (150, 152, 90), (238, 246, 150)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_survey_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary73',
    ),
    'legs': dict(
        outdir='_survey_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary73',
    ),
    'boots': dict(
        outdir='_survey_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_survey',
    ),
    'helmet': dict(
        outdir='_surveydome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary73',
    ),
}

CONTROLS = ('random', 'huddled', 'aligned', 'swapped', 'spare', 'nudged', 'clipped', 'crowded',
            'flat')
CLAUSES = ('ground', 'survey', 'precision', 'tight', 'clear', 'legible')


# --- sheet machinery ---------------------------------------------------------------------------
def label8(mask):
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
                    for dy, dx in NB8:
                        ny, nx = y + dy, x + dx
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


# --- the arithmetic of an address --------------------------------------------------------------
def address_col(pts, b, r):
    """One beacon's column of the address table, under rule r. THE READER NEEDS NOTHING BUT THE
    PIXEL POSITIONS: no orientation, no ordering, no constant of any kind."""
    q = (pts[:, 0] - b[0]) ** 2 + (pts[:, 1] - b[1]) ** 2
    if r == 3:
        return q
    s = np.floor(np.sqrt(q.astype(np.float64))).astype(np.int64)
    if r == 2:
        return np.floor(2.0 * np.sqrt(q.astype(np.float64))).astype(np.int64)
    if r == 1:
        return s
    return s // 2


def resolves(pts, centres, r):
    """THE LAW, in one line: every pixel of the piece has an address of its own."""
    if len(centres) == 0:
        return False
    M = np.stack([address_col(pts, b, r) for b in centres], 1)
    return len(np.unique(M, axis=0)) == len(pts)


def ndistinct(M):
    return len(np.unique(M, axis=0)) if M.shape[1] else 1


def coarsest_that_resolves(pts, centres):
    """THE CLASS, READ OFF THE PLATE. The rules are nested, so this walks up from the crudest and
    stops at the first that works - and there is exactly one answer, never a choice between two."""
    for r in range(len(RULES)):
        if resolves(pts, centres, r):
            return r
    return None


# --- the beacons -------------------------------------------------------------------------------
def arms_of(a, c):
    """The arms a beacon at c is ENTITLED to: those of its four neighbours that are cloth. A beacon
    never chooses how much of itself to draw; the silhouette chooses for it, and clause GROUND is
    the reader checking that choice against the same silhouette."""
    h, w = a.shape
    return [(c[0] + dy, c[1] + dx) for dy, dx in NB4
            if 0 <= c[0] + dy < h and 0 <= c[1] + dx < w and a[c[0] + dy, c[1] + dx]]


def has_axis(a, c):
    """A full opposite pair, so the figure has an axis and its centre is not a matter of taste."""
    h, w = a.shape
    y, x = c
    vert = (y - 1 >= 0 and a[y - 1, x]) and (y + 1 < h and a[y + 1, x])
    horz = (x - 1 >= 0 and a[y, x - 1]) and (x + 1 < w and a[y, x + 1])
    return bool(vert or horz)


def candidates(a):
    """Every pixel that could carry a beacon."""
    return [(int(y), int(x)) for y, x in np.argwhere(a) if has_axis(a, (int(y), int(x)))]


def figure(a, c):
    """The pixels of the beacon at c."""
    return [tuple(c)] + arms_of(a, c)


def conflict(a, c, chosen, tight=False):
    """Beacons stand a pixel apart - clause CLEAR. Two touching beacons are one crest figure, and a
    figure with two bright cores is not a beacon at all: the reader refuses it and the plate has
    said nothing. Control CROWDED is exactly this line switched off."""
    if tight:
        return any(tuple(c) == tuple(d) for d in chosen)
    fig = set(figure(a, c))
    for d in chosen:
        for (y, x) in figure(a, d):
            for dy, dx in ((0, 0),) + NB8:
                if (y + dy, x + dx) in fig:
                    return True
    return False


def spread_pool(cand, a, m, skip=0, huddled=False):
    """Farthest-point sampling: m candidate centres as far from one another as the cloth allows.

    Seeded from the MIDDLE, not from an extremity - the 72nd paid for that lesson. A survey seeded
    at the rim pins every beacon to the outline, and a beacon lying along a silhouette reads as a
    ragged edge rather than as a mark. Control HUDDLED is this routine run backwards."""
    if not cand:
        return []
    ys = np.array([p[0] for p in cand], float)
    xs = np.array([p[1] for p in cand], float)
    cy, cx = ys.mean(), xs.mean()
    seed = min(cand, key=lambda p: ((p[0] - cy) ** 2 + (p[1] - cx) ** 2, p[0], p[1]))
    out = [seed]
    while len(out) < m and len(out) < len(cand):
        rest = [p for p in cand if p not in out]
        if not rest:
            break
        key = (lambda p: (min((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 for q in out), -p[0], -p[1]))
        out.append(min(rest, key=key) if huddled else max(rest, key=key))
    return out[skip:] + out[:skip]


def greedy(pts, a, pool, r, tight=False, cap=MAXB, seed=None):
    """Beacons are added, one at a time, wherever they cut the most ties - until every pixel of the
    piece has an address of its own. THE PAINTER SEARCHES AND THE LAW DOES NOT: unlike the 72nd,
    whose arithmetic could be dealt and never failed, here the whole question is geometric and the
    answer is found or it is not.

    THE FIRST BEACON IS FORCED AND THE REST ARE GREEDY, which is the single most expensive lesson
    this axis paid for. Pure greed puts its first mark where it cuts the most ties on its own, and
    on a small piece - the ranger's hood, 47 pixels in six rows - that first mark leaves nowhere
    legal for a third: every remaining candidate is 8-adjacent to something already drawn, so two
    beacons touching would be ONE figure with two cores and the reader would refuse it. The hood was
    reported PLAIN in 35 poses out of 35 for that reason alone, and an exhaustive search proved a
    lawful survey existed in all 35. Restarting the greed from every well-spread candidate in turn
    recovers them. THE FAILURE WAS IN THE SEARCH AND NOT IN THE GARMENT, and the two are worth
    telling apart before anything is called impossible."""
    chosen = [] if seed is None else [seed]
    M = np.zeros((len(pts), 0), np.int64) if seed is None \
        else address_col(pts, seed, r)[:, None]
    if seed is not None and ndistinct(M) == len(pts):
        return chosen
    for _ in range(cap - len(chosen)):
        best = None
        for b in pool:
            if b in chosen or conflict(a, b, chosen, tight):
                continue
            M2 = np.concatenate([M, address_col(pts, b, r)[:, None]], 1)
            d = ndistinct(M2)
            if best is None or d > best[0]:
                best = (d, b, M2)
        if best is None:
            return None
        chosen.append(best[1])
        M = best[2]
        if best[0] == len(pts):
            return chosen
    return None


def trim(pts, centres, r):
    """CLAUSE TIGHT, DONE BY THE PAINTER RATHER THAN DEMANDED OF IT. A greedy survey often carries
    a beacon it no longer needs by the time it has finished; every one that can go, goes, and what
    is left is a plate with nothing spare on it. This is the axis TAKING ORNAMENT BACK, which no
    previous generator has had a reason to do."""
    out = list(centres)
    changed = True
    while changed and len(out) > 1:
        changed = False
        for b in list(out):
            rest = [c for c in out if c != b]
            if rest and resolves(pts, rest, r):
                out = rest
                changed = True
                break
    return out


def nudge_of(a, c, salt, chosen):
    for dy, dx in NB8:
        d = (c[0] + dy, c[1] + dx)
        if 0 <= d[0] < a.shape[0] and 0 <= d[1] < a.shape[1] and a[d] and has_axis(a, d) \
                and not conflict(a, d, [q for q in chosen if q != c]):
            return d
    return None


def compose(a, cls, mode=None, salt=''):
    """The beacon centres for one pose, or None if the pose cannot be surveyed to its class's
    precision. Returns (centres, r, drop) - drop is the arm control CLIPPED steals."""
    r = SWAP_R[cls] if mode == 'swapped' else R[cls]
    cand = candidates(a)
    if len(cand) < 2:
        return None
    pts = np.argwhere(a)

    if mode == 'random':
        h = hashlib.md5(('%s|rnd' % salt).encode()).digest()
        chosen = []
        for i in range(4):
            b = cand[h[i] % len(cand)]
            if b not in chosen and not conflict(a, b, chosen):
                chosen.append(b)
        return (chosen, r, None) if len(chosen) >= 2 else None

    if mode == 'huddled':
        # THE BEACONS PACKED INTO ONE PLACE, AND NOT CHOSEN FOR WHAT THEY SETTLE. The first draft of
        # this control ran the same greed over a huddled pool and scored 273 clean out of 278, which
        # is not a control at all: greed will find a lawful survey inside a huddle if one is there.
        # What the axis actually relies on is that each beacon is chosen for the TIES IT CUTS, so
        # that is what this switches off - nearest candidates to the centroid, first come first
        # served, nothing asked of them.
        hpool = spread_pool(cand, a, POOL, 0, huddled=True)
        chosen = []
        for b in hpool:
            if not conflict(a, b, chosen):
                chosen.append(b)
            if len(chosen) >= 4:
                break
        return (chosen, r, None) if len(chosen) >= 2 else None

    if mode == 'aligned':
        # ALL BEACONS ON ONE ROW. The lattice respects a horizontal line, so reflection in it takes
        # pixels to pixels and the garment's own left-right likeness supplies the collisions.
        rows = {}
        for p in cand:
            rows.setdefault(p[0], []).append(p)
        best = max(rows.values(), key=len)
        chosen = []
        for b in sorted(best, key=lambda p: p[1]):
            if not conflict(a, b, chosen):
                chosen.append(b)
        return (chosen[:4], r, None) if len(chosen) >= 2 else None

    pool = spread_pool(cand, a, POOL, 0, huddled=(mode == 'huddled'))
    for seed in [None] + pool[:RESTARTS]:
        chosen = greedy(pts, a, pool, r, tight=(mode == 'crowded'), seed=seed)
        if chosen is None:
            continue
        chosen = trim(pts, chosen, r)
        if mode == 'spare':
            # ONE BEACON MORE THAN THE LAW NEEDS. Not wrong about the ground - wrong about the
            # plate: a survey with something spare in it is a survey the reader cannot date.
            for b in pool:
                if b not in chosen and not conflict(a, b, chosen):
                    chosen = chosen + [b]
                    break
        if mode == 'nudged':
            i = int(hashlib.md5(('%s|nudge' % salt).encode()).digest()[0]) % len(chosen)
            d = nudge_of(a, chosen[i], salt, chosen)
            if d is None:
                continue
            chosen = [d if j == i else c for j, c in enumerate(chosen)]
        drop = None
        if mode == 'clipped':
            # AN ARM PRUNED WHERE THE CLOTH WOULD HAVE TAKEN ONE. The only control that leaves the
            # law itself untouched and is caught anyway, by the reader comparing the figure against
            # the silhouette it stands on.
            for i, c in enumerate(chosen):
                if len(arms_of(a, c)) >= 3:
                    drop = (i, 0)
                    break
            if drop is None:
                continue
        if mode in ('huddled', 'crowded', 'spare', 'nudged', 'clipped', 'random', 'aligned',
                    'flat'):
            return chosen, r, drop
        if not resolves(pts, chosen, r):
            continue
        # CLAUSE PRECISION, ENFORCED AT THE EASEL. A plate that reads one rule coarser is a
        # different class in this one's colours, so the painter throws it away and spreads the
        # beacons differently.
        if r > 0 and resolves(pts, chosen, r - 1):
            continue
        if not legible(a, chosen, None):
            continue
        return chosen, r, None
    return None


def paint(a, centres, drop=None):
    """Core, arms, and a dark witness laid against the figure wherever the cloth has room for one.
    RELIEF, NOT COLOUR: at thirteen pixels a flat field of another hue is camouflage, and only a
    crest with its own shadow survives the finishing pass (the 13px legibility pass)."""
    core = np.zeros(a.shape, bool)
    arm = np.zeros(a.shape, bool)
    for i, c in enumerate(centres):
        core[c] = True
        ar = arms_of(a, c)
        if drop is not None and drop[0] == i and len(ar) > drop[1]:
            ar = ar[:drop[1]] + ar[drop[1] + 1:]
        for p in ar:
            arm[p] = True
    crest = core | arm
    dark = np.zeros(a.shape, bool)
    h, w = a.shape
    for (y, x) in np.argwhere(crest):
        for dy, dx in NB8:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not crest[ny, nx]:
                dark[ny, nx] = True
                break
    return core, arm, dark


def blots(crest):
    blk = crest[:-1, :-1] & crest[1:, :-1] & crest[:-1, 1:] & crest[1:, 1:]
    return bool(blk.any())


def legible(a, centres, drop, mode=None):
    """Can the picture be read back off its own pixels? THE LAW IS ARITHMETIC AND THE LEGIBILITY IS
    A SEARCH, and the file is honest about which is which."""
    core, arm, dark = paint(a, centres, drop)
    crest = core | arm
    if not crest.any():
        return False
    if mode != 'crowded' and blots(crest):
        return False
    h, w = a.shape
    for c in centres:
        if not any(0 <= c[0] + dy < h and 0 <= c[1] + dx < w and dark[c[0] + dy, c[1] + dx]
                   for dy, dx in NB8):
            return False
    if mode in ('crowded', 'clipped'):
        return True
    got = recover(a, core, arm)
    return got is not None and sorted(got) == sorted(tuple(c) for c in centres)


# --- the reader --------------------------------------------------------------------------------
def read_stops(fr, a):
    """Witness, field, arm and core off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: the
    brightest luminance on the piece is a core, the next is arm, the darkest is the witness, and
    what is left over is field. A plate showing fewer than four stops has no beacons on it."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    pts = np.argwhere(a)
    core = np.zeros(a.shape, bool)
    arm = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    if len(pts) == 0:
        return core, arm, dark
    vals = sorted({int(lum[y, x]) for y, x in pts})
    if len(vals) < 4:
        return core, arm, dark
    cv, av, dv = vals[-1], vals[-2], vals[0]
    for y, x in pts:
        v = int(lum[y, x])
        if v == cv:
            core[y, x] = True
        elif v == av:
            arm[y, x] = True
        elif v == dv:
            dark[y, x] = True
    return core, arm, dark


def read_beacon(a, pts, core):
    """One crest figure, turned into a beacon centre - or None if it is not one.

    CLAUSE GROUND IN ITS ENTIRETY. The figure qualifies only if it has exactly one core; if its
    other pixels are exactly the cloth-neighbours of that core, none missing and none extra; and if
    the core has a full opposite pair among them. The reader never learns what the painter wanted:
    IT CHECKS THE FIGURE AGAINST THE SILHOUETTE, and a beacon clipped by the edge of the cloth
    passes for the same reason a beacon pruned by a careless hand fails."""
    cs = [p for p in pts if core[p]]
    if len(cs) != 1:
        return None
    c = cs[0]
    if not has_axis(a, c):
        return None
    want = set(arms_of(a, c)) | {c}
    if set(pts) != want:
        return None
    return c


def recover(a, core, arm):
    """The beacon centres of the plate, off the pixels, with no help of any kind."""
    crest = (core | arm) & a
    lab, n = label8(crest)
    out = []
    for i in range(1, n + 1):
        pts = [(int(y), int(x)) for y, x in np.argwhere(lab == i)]
        c = read_beacon(a, pts, core)
        if c is None:
            return None
        out.append(c)
    if not out or len(set(out)) != len(out):
        return None
    return sorted(out)


def touching(crest, lab, n):
    h, w = crest.shape
    for y, x in np.argwhere(crest):
        for dy, dx in NB8:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and crest[ny, nx] and lab[ny, nx] != lab[y, x]:
                return True
    return False


# --- frames ------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, arm, dark, centres, r) or None if the pose cannot be surveyed."""
    dark_c, field_c, arm_c, core_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE BEACONS GO ON. The source sheet's inherited highlights sit
    # in the same stop a core does, and a reader told nothing cannot tell an inherited highlight
    # from a beacon. Every tone on this plate is put there by the survey; the modelling comes back,
    # richer, from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    got = compose(a, cls, mode, salt)
    if got is None:
        return None
    centres, r, drop = got
    if mode == 'flat':
        for y, x in np.argwhere(a):
            put(fr, y, x, field_c)
        return np.zeros(a.shape, bool), np.zeros(a.shape, bool), np.zeros(a.shape, bool), \
            centres, r
    core, arm, dark = paint(a, centres, drop)
    for y, x in np.argwhere(dark):
        put(fr, y, x, dark_c)
    for y, x in np.argwhere(arm):
        put(fr, y, x, arm_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, core_c)
    return core, arm, dark, centres, r


def frames_of(base):
    for fi in range(SLEEP_FROM):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a = base[sl][..., 3] > 0
        if a.any():
            yield fi, sl, a


def one_plate(base, sl, a, cls, mode=None, salt=''):
    fr = np.zeros((FH, FW, 4), base.dtype)
    D, M, L = BODY[cls]
    recolor(base[sl], fr, a, D, M, L)
    got = build_frame(fr, a, cls, mode, salt)
    return fr, got


def sheet_carries(base, cls, stem, mode=None):
    """A SHEET IS SURVEYED IN ALL FORTY-TWO POSES OR IN NONE. Beacons that appear in some frames of
    a walk and not others read as a bug, not as a hard case."""
    for fi, sl, a in frames_of(base):
        _fr, got = one_plate(base, sl, a, cls, mode, '%s|%d' % (stem, fi))
        if got is None:
            return False
    return True


def build(base, cls, stem, mode=None, force=None):
    D, M, L = BODY[cls]
    ok = sheet_carries(base, cls, stem, mode) if force is None else force
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
        build_frame(out[sl], a, cls, mode, '%s|%d' % (stem, fi))
    return out, ok


# --- the acceptance test -----------------------------------------------------------------------
def inspect_frame(fr, a, cls):
    """The six clauses on ONE POSE."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, beacons=0, rread=None)
    core, arm, dark = read_stops(fr, a)
    crest = (core | arm) & a
    if not crest.any():
        v['silent'] = 1
        return v
    v['plates'] = 1
    pts = np.argwhere(a)

    # (1) GROUND - every crest figure is a beacon, and every missing arm is missing because the
    # silhouette has nowhere to put it
    centres = recover(a, core, arm)
    if centres is None:
        v['ground'] = 1
        return v
    v['beacons'] = len(centres)

    # (5) CLEAR - the beacons account for every crest pixel and stand a pixel apart
    lab, n = label8(crest)
    if n != len(centres) or touching(crest, lab, n) or blots(crest):
        v['clear'] = 1

    # (2) SURVEY - THE LAW
    r = R[cls]
    if not resolves(pts, centres, r):
        v['survey'] = 1

    # (3) PRECISION - and it must fail one rule coarser. THE CLASS IS AN OUTPUT: this is the line
    # that reads it off the plate.
    got = coarsest_that_resolves(pts, centres)
    v['rread'] = got
    if got != r:
        v['precision'] = 1

    # (4) TIGHT - nothing on the plate is spare
    if len(centres) > 1:
        for b in centres:
            if resolves(pts, [c for c in centres if c != b], r):
                v['tight'] = 1
                break

    # (6) LEGIBLE - a dark witness beside every beacon
    h, w = a.shape
    for c in centres:
        if not any(0 <= c[0] + dy < h and 0 <= c[1] + dx < w and dark[c[0] + dy, c[1] + dx]
                   for dy, dx in NB8):
            v['legible'] = 1
            break
    return v


def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, sheets=0, pass_sheets=0, beacons=0)
    for kind, cfg in SLOTS.items():
        if only and kind != only:
            continue
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                plates = [(fi, a, one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi)))
                          for fi, sl, a in frames_of(base)]
                ok = all(p[2][1] is not None for p in plates)
                tot['sheets'] += 1
                if not ok:
                    print('   %-7s %-8s %-2s  PLAIN (reported)' % (kind, cls, suffix or 'm'),
                          flush=True)
                    continue
                bad = dict.fromkeys(CLAUSES, 0)
                np_, ns, nb = 0, 0, []
                for fi, a, (fr, _g) in plates:
                    res = inspect_frame(fr, a, cls)
                    for c in CLAUSES:
                        bad[c] += res[c]
                    np_ += res['plates']
                    ns += res['silent']
                    if res['beacons']:
                        nb.append(res['beacons'])
                tot['plates'] += np_
                tot['silent'] += ns
                tot['beacons'] += sum(nb)
                for c in CLAUSES:
                    tot[c] += bad[c]
                good = not any(bad.values())
                tot['pass_sheets'] += 1 if good else 0
                print('   %-7s %-8s %-2s  %-6s plates=%-3d beacons %d-%-2d  %s%s'
                      % (kind, cls, suffix or 'm', RULES[R[cls]].upper(), np_,
                         min(nb) if nb else 0, max(nb) if nb else 0,
                         'ALL PASS' if good else 'FAIL ',
                         '' if good else ' ' + ' '.join('%s=%d' % (c, k)
                                                        for c, k in bad.items() if k)),
                      flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d beacons drawn, %d silent'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['beacons'], tot['silent']))
    for c in CLAUSES:
        print('   %-10s %d violations' % (c.upper(), tot[c]))


# --- the controls ------------------------------------------------------------------------------
def controls_report(which=None):
    if which == 'aligned-why':
        aligned_why()
        return
    print('== CONTROLS  (a plate is CLEAN only if it trips no clause at all)')
    for mode in (CONTROLS if which is None else (which,)):
        drawn = clean = silent = undrawable = 0
        bad = dict.fromkeys(CLAUSES, 0)
        for kind, cfg in SLOTS.items():
            for cls in cfg['srcs']:
                stem = cfg['srcs'][cls]
                base = load_any('%s.png' % stem)
                for fi, sl, a in frames_of(base):
                    fr, got = one_plate(base, sl, a, cls, mode, '%s|%d' % (stem, fi))
                    if got is None:
                        undrawable += 1
                        continue
                    res = inspect_frame(fr, a, cls)
                    if res['silent']:
                        silent += 1
                        continue
                    drawn += 1
                    for c in CLAUSES:
                        bad[c] += res[c]
                    if not any(res[c] for c in CLAUSES):
                        clean += 1
        note = ' '.join('%s=%d' % (c, k) for c, k in bad.items() if k)
        extra = ''
        if mode == 'swapped':
            extra = '  <- LAWFUL AND MISNAMED: the reader names the class the plate really is'
        if mode == 'spare':
            extra = '  <- not wrong about the ground, wrong about the PLATE (a beacon it can do without)'
        if mode == 'clipped':
            extra = '  <- the law untouched; caught by the figure disagreeing with the silhouette'
        if mode == 'aligned':
            extra = '  <- beacons on one row: the lattice respects that line. See --controls aligned-why'
        if mode == 'huddled':
            extra = '  <- beacons taken for where they are and not for the TIES THEY CUT'
        if mode == 'nudged':
            extra = ('  <- WEAK AND INFORMATIVE: a survey SURVIVES a beacon moving one pixel where '
                     'the 72nd\'s shares could not. Geometry has slack; arithmetic has none')
        if mode == 'crowded':
            extra = ('  <- weak, and should be: it only bites where the crowding actually produced '
                     'a collision, and greed spreads its marks anyway')
        if mode == 'random':
            extra = '  <- the null hypothesis. THE NUMBER TO BEAT, and the axis beats it 700 to 0'
        if mode == 'flat':
            extra = '  <- fewer than four stops, so there is nothing to read (SILENT, not passed)'
        print('   %-10s drawn=%-4d CLEAN=%-4d  %s%s' % (mode.upper(), drawn, clean, note, extra),
              flush=True)
        if undrawable:
            print('   %-10s %d plates could not be drawn at all' % ('', undrawable))
        if silent:
            print('   %-10s %d plates show the reader fewer than four stops (SILENT, not passed)'
                  % ('', silent))


def aligned_why():
    """THE LATTICE THEOREM, MEASURED. Two pixels share an EXACT address under two beacons iff they
    are reflections in the line through the beacon centres. That reflection carries the integer
    lattice into itself only when the line is horizontal, vertical or at 45 degrees; for any other
    direction almost every pixel's mirror image lands between pixels and there is nothing for it to
    collide with. So the mage's plate - which carries exactly two beacons - is legible BECAUSE ITS
    PAIR LIES ALONG A DIRECTION THE GRID DOES NOT RESPECT. Counted over the wardrobe."""
    print('== THE LATTICE THEOREM  (mage plates: two beacons, and the direction between them)')
    respected = oblique = 0
    dirs = {}
    for kind, cfg in SLOTS.items():
        stem = cfg['srcs']['mage']
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            got = compose(a, 'mage', None, '%s|%d' % (stem, fi))
            if got is None or len(got[0]) != 2:
                continue
            (y0, x0), (y1, x1) = got[0][0], got[0][1]
            dy, dx = y1 - y0, x1 - x0
            g = int(np.gcd(abs(dy), abs(dx))) or 1
            d = (int(dy) // g, int(dx) // g)
            dirs[d] = dirs.get(d, 0) + 1
            if 0 in d or abs(d[0]) == abs(d[1]):
                respected += 1
            else:
                oblique += 1
    print('   two-beacon mage plates: %d' % (respected + oblique))
    print('   direction the grid RESPECTS (axis-parallel or 45 deg): %d' % respected)
    print('   direction the grid does NOT respect (oblique):         %d' % oblique)
    for d, n in sorted(dirs.items(), key=lambda t: -t[1])[:8]:
        print('      %-10s %d' % (str(d), n))


# --- reports -----------------------------------------------------------------------------------
def sweep():
    print('== SLOTS  (can every pose be surveyed to its class\'s precision, and does it read back)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                fit = unfit = 0
                nb = []
                for fi, sl, a in frames_of(base):
                    fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                    if got is None:
                        unfit += 1
                        continue
                    res = inspect_frame(fr, a, cls)
                    if any(res[c] for c in CLAUSES):
                        unfit += 1
                    else:
                        fit += 1
                        nb.append(res['beacons'])
                print('   %-7s %-8s %-2s  %-6s beacons %d-%-2d  poses %2d/%-2d  SHEET %s'
                      % (kind, cls, suffix or 'm', RULES[R[cls]].upper(),
                         min(nb) if nb else 0, max(nb) if nb else 0,
                         fit, fit + unfit,
                         'surveyed' if unfit == 0 else 'PLAIN (reported)'), flush=True)


def frame_dump():
    print('== ONE REAL POSE PER CLASS  ("O" core, "+" arm, "=" witness, "-" field)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            got = compose(a, cls, None, '%s|%d' % (stem, fi))
            if got is None:
                continue
            centres, r, _drop = got
            core, arm, dark = paint(a, centres)
            pts = np.argwhere(a)
            print('== %s chest frame %d   %d beacons %s   rule %s   coarsest that works: %s'
                  % (cls, fi, len(centres), [tuple(c) for c in centres], RULES[r].upper(),
                     RULES[coarsest_that_resolves(pts, centres)].upper()))
            for rr in range(len(RULES)):
                print('   %-7s %s' % (RULES[rr].upper(),
                                      'resolves' if resolves(pts, centres, rr) else 'ties'))
            ys, xs = np.nonzero(a)
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not a[y, x]:
                        row += '.'
                    elif core[y, x]:
                        row += 'O'
                    elif arm[y, x]:
                        row += '+'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a core on the
    shadowed flank is darker in absolute terms than the field on the lit one."""
    print('== SURVIVAL through the finishing pass (reported, local contrast)')
    for kind, cfg in SLOTS.items():
        tot = ok = 0
        for cls in cfg['srcs']:
            stem = cfg['srcs'][cls]
            base = load_any('%s.png' % stem)
            if not sheet_carries(base, cls, stem):
                continue
            arr, _ = build(base, cls, stem)
            fin, _i = finish_array(arr.copy(), '_tmp/%s_%s.png' % (cfg['dst'] % cls, kind))
            for fi, sl, a in frames_of(base):
                _fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                if got is None:
                    continue
                core, arm, dark, _c, _r = got
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for y, x in np.argwhere(core | arm):
                    nb = [lum[ny, nx] for ny, nx in
                          ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                          if 0 <= ny < FH and 0 <= nx < FW and dark[ny, nx]]
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
        for cls, stem0 in cfg['srcs'].items():
            for suffix in ('', '_f'):
                stem = '%s%s' % (stem0, suffix)
                base = load_any('%s.png' % stem)
                arr, ok = build(base, cls, stem)
                dst = '%s/%s%s.png' % (cfg['outdir'], cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-58s opaque_px=%-6d finish=%s/%s  %s'
                      % (dst, int((arr[..., 3] > 0).sum()), info['slot'], info['variant'],
                         RULES[R[cls]].upper() if ok else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
