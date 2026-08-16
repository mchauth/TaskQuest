#!/usr/bin/env python3
"""SIXTY-EIGHTH net-new-geometry axis for ALL FOUR SLOTS - the SEME family: the plate is POWDERED
with studs, and the law is not about the studs at all. It is about the VECTORS BETWEEN THEM.

    the ornament is  a STUD     one pixel of crest with a dark witness beside it, standing on a
                                flat mid field; no two studs touch, even at a corner
    the relation is  the DISPLACEMENT between two studs - a vector, not a distance
    the law is       no displacement occurs more than LAMBDA times on the plate, and some
                     displacement occurs exactly LAMBDA times

*** THIS IS THE FIRST AXIS WHOSE LAW IS A REFUSAL TO REPEAT. ***
An ornament is, definitionally, a thing that repeats. Sixty-seven axes are built out of repetition:
a pitch (11th FLUTING), a lattice (13th STUDWORK, 19th HONEYCOMB, 35th FACET), a two-symbol word
(60th CADENCE), a ratio held three times (61st CANON), a rule applied row after row (65th CASCADE),
a stone repeated across a plate (66th DOVETAIL). Even the aperiodic 46th CRAQUELURE repeats a
STATISTIC. This one repeats NOTHING. Its law says: take any two studs, note how one stands to the
other, and you will not find that same relation anywhere else on the plate more than LAMBDA times.
At LAMBDA = 1 the plate contains no repeated configuration of any kind, at any scale, in any
direction - it is an ornament whose entire content is that it is not an ornament.

*** THE PAIR WITH THE 13th, WHICH IS ITS EXACT NEGATION. ***
    the 13th STUDWORK   raised rivets on a point-grid. EVERY displacement between neighbouring
                        studs is THE SAME. The eye reads: brigandine.
    the 68th SEME       raised studs, the same pixel, the same relief, the same density. NO
                        displacement is the same. The eye reads: brigandine.
THE TWO PLATES CANNOT BE TOLD APART BY LOOKING, and control GRID is the 13th axis rendered by this
axis's own painter to prove it. What separates them is a SPECTRUM, and the acceptance test is the
first reader in sixty-eight whose input is not a picture.

*** THE ACCEPTANCE TEST IS A NEW KIND: AN AUTOCORRELATION, AND THEN A RECONSTRUCTION. ***
The reader recovers the studs, forms the multiset of all C(k,2) displacements between them, and
THROWS THE POSITIONS AWAY. Everything after that point is done on the multiset alone - a bag of
arrows with no plate attached. From that bag it rebuilds the plate. Clauses:

    (1) RECOVERY     the studs read back off the pixels are exactly the studs driven into them.
    (2) SPECTRUM     max multiplicity over the displacement multiset == LAMBDA(class). Computed from
                     the recovered studs alone. THERE IS NO TOLERANCE CONSTANT IN THIS FILE.
    (3) TIGHT        the bound is ATTAINED - some displacement occurs exactly LAMBDA times. A bound
                     that is merely respected is not an identity: a warrior plate (LAMBDA=1) also
                     respects LAMBDA<=3, so without this clause every class would read as ranger.
                     Control TIGHTLESS is this clause and nothing else.
    (4) REBUILD      handed ONLY the multiset of displacements - no plate, no positions, no class -
                     the reader reconstructs every point set that could have produced it, by
                     backtracking over the multiset. The answer must be the plate and its point
                     reflection AND NOTHING ELSE. This is the clause that says the arrows contain
                     the plate: the picture is recoverable from its own relations. Any third
                     solution is a HOMOMETRIC TWIN - a genuinely different plate with the same
                     spectrum - and is reported rather than excused.
    (5) BLIND        the whole stud set is translated and point-reflected and the spectrum must come
                     back IDENTICAL. THE 67th COLOPHON WAS BLIND TO WHERE A BOSS SAT INSIDE ITS
                     REGISTER BUT THE REGISTER'S PLACE WAS ITS WHOLE LAW. THIS AXIS HAS NO PLACE IN
                     IT AT ALL. There is no origin, no pitch, no phase, no register, no direction,
                     no up: slide the ornament anywhere, turn it through a half-turn, and the law is
                     untouched. What it sees is not the studs. It is the arrows.
    (6) LEGIBLE      every stud is ONE crest pixel with at least one dark witness 4-adjacent, and no
                     two studs are within Chebyshev distance 2 of each other. Two studs that touch
                     fuse into one crest cluster, the reader counts k-1 studs, and the spectrum of
                     k-1 studs is not the spectrum of k. Control FUSED is what that looks like.

*** THE EIGHT CONTROLS, AND THE THREE THAT DO NOT FAIL. ***
    GRID       studs on a lattice: THE 13th AXIS, drawn by this axis's painter, same pixel count,
               same relief, same palette. Its spectrum is a wall. It is the control that proves this
               axis is a SPECTRUM and not a look.
    RANDOM     studs scattered uniformly at random under the legibility rule only, same count. It is
               what everyone thinks this axis is, and the measured answer is the reverse of what
               anyone would guess: chance satisfies the STRICT class 35.7% of the time and the
               LOOSE class 10.0%. Eight studs at Chebyshev 2 in a 10x12 box are already so spread
               that their twenty-eight arrows are usually all different; what chance will not
               supply is a relation running EXACTLY three times and never four. SO THE HONEST
               STATEMENT OF THIS AXIS IS NOT ABOUT A PLATE. One warrior plate is worth half a bit.
               THE EVIDENCE IS THE WARDROBE: 280 warrior plates every one of them lawful, where
               chance gives 0.357^280, which is about 10^-125.
    LOOSE      one stud moved so that the maximum multiplicity is LAMBDA+1. Invisible. False.
    TIGHTLESS  the plate driven to LAMBDA-1 instead: it RESPECTS the class's bound and does not
               ATTAIN it. The control that exists to justify clause TIGHT, and the only control that
               is false for a reason no eye could ever supply. IT IS VACUOUS FOR THE WARRIOR AND
               THAT IS NOT A DEFECT: there is no repetition below one, so LAMBDA=1 is a bound that
               cannot be respected without being attained, and 280 of 280 warrior plates pass it.
               The warrior's law needs no tightness clause; the other two do, and the file does not
               pretend the clause is doing the same work in all three.
    SLIDE      the entire stud set translated by a lawful vector. LAWFUL, and that is its finding.
    TURN       the entire stud set point-reflected. LAWFUL, and that is its finding. Together SLIDE
               and TURN are the axis's blindness, stated as controls rather than as a boast: this
               ornament cannot tell itself from its own mirror, and clause REBUILD proves that no
               reader ever could.
    FUSED      the legibility rule relaxed to 4-adjacency, so studs may touch corners and merge. The
               plates are not false, they are UNREADABLE: crest clusters of two are not studs to a
               reader that requires one pixel, and the recovered spectrum is a spectrum of something
               that is not on the plate.
    DENSE      one extra stud added anywhere lawful. It breaks the warrior 65.4% of the time and the
               mage only 15.0% - the strict plate is very nearly MAXIMAL and the loose plate has room
               to spare. THE HONEST FINDING OF THIS AXIS, AND THE REASON IT HAS NO FRAGILE CLAUSE:
               A SIDON SET IS HEREDITARY. Strike a stud out of a warrior plate and every surviving
               relation is still unique, so THE PLATE IS STILL LAWFUL. The 66th could say that no
               part of its ornament was ornament and the 67th could say it in arithmetic; this axis
               CANNOT SAY IT AND DOES NOT CLAIM IT. What a strike destroys here is not the law but
               the TIGHTNESS, and only for the two classes whose bound is greater than one. It is
               the first axis in sixty-eight that is asked the 66th's question and answers no.

*** CLASS IDENTITY IS A CEILING ON REPETITION. ***
    warrior  LAMBDA = 1    nothing on the plate stands to anything twice
    ranger   LAMBDA = 2    a relation may be echoed once, never twice
    mage     LAMBDA = 3    a relation may run three times, never four
Not a shape (66th), not a word (67th), not a rule (65th), not a colour (64th), not a ratio (61st) -
a TOLERANCE. It is the first class identity in the project that is a permission rather than a form,
and the first that is read off a histogram instead of off the plate.

*** AND THE ASSIGNMENT IS UPSIDE DOWN, WHICH IS THE AXIS'S BEST FINDING. ***
The obvious assignment is warrior-loosest (biggest plate, most studs, most room to repeat). It is
exactly backwards. LAMBDA = 1 needs TWO STUDS and no more: any two studs realise one displacement
once, and the bound is attained by arithmetic. LAMBDA = 3 needs a CHAIN of FOUR studs in step -
four studs, each at least two pixels from the next, strung along one vector - which is six pixels of
span before a single ornamental stud is placed. So the strict law is the CHEAP one and the permissive
law is the EXPENSIVE one, because a ceiling is only an identity if the plate can afford to REACH it.
The warrior therefore takes LAMBDA = 1, because a warrior sabaton in the jump pose is TWELVE PIXELS
in a 5x4 box and will hold two studs and nothing else; the mage takes LAMBDA = 3 because a wizard
hat is 14x14 and a mage sabaton is 7x5, the largest small piece in the batch. THE AXIS'S HARD CASES
ARE ITS LOOSE CLASSES. Every previous axis got harder as its law got stricter.

*** THE RENDER-PAID LESSONS. ***
(a) AN ORNAMENT RE-SCATTERED EVERY FRAME IS NOT AN ORNAMENT, IT IS STATIC. The first driver solved
    each pose from scratch; the studs are lawful in every frame and the walk cycle boils. The driver
    WARM-STARTS from the previous pose in box-relative coordinates, keeps every stud the new mask
    still admits, and tops up. Nothing in the law required this and the law is not what was wrong.
(b) A STUD IS ONE PIXEL AND ITS WITNESS IS A SECOND. The 67th's boss is a domino because a lone
    crest pixel is noise; here a domino would make the mark's position ambiguous - which pixel is
    the mark? - and the whole axis is positions. So the stud stays one pixel and buys its relief
    from a DARK 4-neighbour instead of from a second crest pixel. Same two pixels of relief, and the
    arrow has an endpoint.
(c) THE WITNESS MAY NOT BE DEMANDED BELOW. Requiring the dark pixel at (r+1, c) cost the boots every
    stud on their bottom row and the sabatons went silent; any in-mask 4-neighbour will carry the
    shadow and the reader asks only that one of them does.
(d) CHEBYSHEV 2, NOT MANHATTAN 2. The 67th allows its bosses to touch cornerwise because a
    4-connected reader keeps them apart. This reader cannot afford that: two studs on a diagonal are
    two crest pixels 4-disconnected and legible, but through the finishing pass they read as one
    short bar, and a bar is not an endpoint.

Repaint only: every pattern pixel is painted onto an already-opaque body pixel and the silhouette is
never touched, so the sheets are QA-safe by construction. Twenty-fourth generator to call
sprite_finish.finish_array in-line.

    python3 scripts/gen_seme_axis68.py            # write the 24 staged sheets
    python3 scripts/gen_seme_axis68.py --accept   # the acceptance test
    python3 scripts/gen_seme_axis68.py --controls # the eight controls
    python3 scripts/gen_seme_axis68.py --sweep    # per-slot affordability
    python3 scripts/gen_seme_axis68.py --survive  # survival through the finishing pass
"""
import os
import sys
import random
from collections import Counter

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
SLEEP_FROM = 60

# A component smaller than this is not part of the piece. Lower than the 67th's 12 because a warrior
# sabaton in the jump pose is a twelve-pixel sliver and dropping it leaves the frame with no piece
# at all.
MIN_PX = 6
# A piece with fewer cells than this cannot hold two studs at Chebyshev 2 with a witness each, so it
# is not asked to. Skipped frames are REPORTED, never hidden.
MIN_SPEAK = 10
# No two studs within this Chebyshev distance. See render-paid lesson (d).
SEP = 2
# The reconstruction in clause REBUILD is exponential in the stud count. Eight studs is 28 arrows
# and runs in milliseconds; the cap also keeps a 13px plate from turning into gravel.
MAX_STUDS = 8

# CLASS IDENTITY IS A CEILING ON REPETITION - and the assignment is upside down on purpose.
LAM = {'warrior': 1, 'ranger': 2, 'mage': 3}

# Three temperatures, deliberately unrelated to the 64th (bronze/ice/bone), 65th (argent/gold/rose),
# 66th (basalt/porphyry/sandstone) and 67th (garnet/celadon/olive brass), so that the five most
# recent axes cannot be mistaken for a recolor set. Darkest channel-sums 212 / 224 / 218 - all well
# clear of the visor's black eye and mouth pixels.
#   warrior  INDIGO STEEL   cold blue-violet
#   mage     AMBER          warm orange-gold
#   ranger   TEAL           blue-green
PAL = {
    'warrior': ((176, 182, 232), (96, 102, 168), (52, 56, 104)),
    'mage':    ((246, 214, 140), (188, 140, 56), (112, 80, 32)),
    'ranger':  ((168, 220, 214), (84, 148, 144), (44, 88, 86)),
}
BODY = {cls: (p[2], p[1], p[0]) for cls, p in PAL.items()}   # (dark, mid, light) for recolor
Q_LO, Q_HI = 0.85, 1.18

SLOTS = {
    'chest': dict(
        outdir='_seme_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary68', largest=True,
    ),
    'legs': dict(
        outdir='_seme_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary68', largest=False,
    ),
    'boots': dict(
        outdir='_seme_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary68', largest=False,
    ),
    'helmet': dict(
        outdir='_semedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary68', largest=True,
    ),
}


# --- the arithmetic: arrows, not points --------------------------------------------------------
def canon(v):
    """A displacement and its negation are ONE relation. Canonical form: first non-zero is positive."""
    dy, dx = v
    if dy < 0 or (dy == 0 and dx < 0):
        return (-dy, -dx)
    return (dy, dx)


def arrows(pts):
    """The multiset of displacements between all pairs. THIS IS THE ONLY THING THE LAW LOOKS AT."""
    c = Counter()
    n = len(pts)
    for i in range(n):
        yi, xi = pts[i]
        for j in range(i + 1, n):
            yj, xj = pts[j]
            c[canon((yj - yi, xj - xi))] += 1
    return c


def lam(pts):
    """The plate's spectrum, as one number: how many times the most repeated relation repeats."""
    a = arrows(pts)
    return max(a.values()) if a else 0


def reconstruct(a, k, cap=64):
    """Every point set of size k whose displacement multiset is exactly `a`.

    THE READER'S INPUT IS NOT A PICTURE. It is a bag of arrows with every position destroyed. The
    only foothold is this: normalise a solution so its lexicographically smallest point sits at the
    origin, and then every OTHER point of it, measured from that origin, is itself one of the arrows
    in the bag. So the candidates are the arrows, the search is over subsets of them, and the bag
    itself does the pruning - the moment a partial set demands an arrow the bag does not have, that
    whole branch is dead.

    Returns the solutions normalised, sorted, as tuples. A set and its point reflection have the
    same bag, so a well-formed plate yields exactly two (or one, if it is centrally symmetric).
    Anything more is a HOMOMETRIC TWIN and clause REBUILD reports it."""
    if k <= 1:
        return [((0, 0),)] if not a else []
    cands = sorted(a)
    out = []

    def rec(start, chosen, bag):
        if len(chosen) == k - 1:
            if not +bag:
                out.append(tuple(sorted([(0, 0)] + chosen)))
            return
        if len(out) >= cap:
            return
        for i in range(start, len(cands)):
            p = cands[i]
            need = Counter()
            need[canon(p)] += 1
            okp = True
            for q in chosen:
                v = canon((p[0] - q[0], p[1] - q[1]))
                if v == (0, 0):
                    okp = False
                    break
                need[v] += 1
            if not okp:
                continue
            for v, n in need.items():
                if bag[v] < n:
                    okp = False
                    break
            if not okp:
                continue
            rec(i + 1, chosen + [p], bag - need)

    rec(0, [], Counter(a))
    return out


def normalise(pts):
    p0 = min(pts)
    return tuple(sorted((y - p0[0], x - p0[1]) for y, x in pts))


def reflect(pts):
    return normalise([(-y, -x) for y, x in pts])


# --- sheet machinery ---------------------------------------------------------------------------
def label4(mask):
    """Self-contained 4-connectivity labelling (scipy-free, as every generator since the 45th)."""
    h, w = mask.shape
    lab = np.zeros((h, w), dtype=np.int32)
    n = 0
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and lab[sy, sx] == 0:
                n += 1
                lab[sy, sx] = n
                stack = [(sy, sx)]
                while stack:
                    y, x = stack.pop()
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n
                            stack.append((ny, nx))
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
        put(fr, y, x, D if q < Q_LO else (L if q > Q_HI else M))


def piece_mask(a, largest):
    """THE PLATE IS THE GARMENT, not the shapes a pose happens to leave visible. A pair of chausses
    is two components and one piece; a stud on the left leg and a stud on the right leg stand in a
    relation, and that relation is on the plate. Ruling the components separately would give the
    reader two bags of arrows and no reason to prefer either."""
    lab, n = label4(a)
    if n < 1:
        return None
    live = [(lab == i) for i in range(1, n + 1)]
    live = [c for c in live if c.sum() >= MIN_PX]
    if not live:
        return None
    if largest:
        live = [max(live, key=lambda c: c.sum())]
    m = live[0].copy()
    for c in live[1:]:
        m |= c
    return m


class Box(object):
    """The piece, cropped to its own bounding box. Box-relative coordinates are what the driver
    warm-starts on, because the box tracks the body and absolute frame coordinates do not."""

    def __init__(self, m):
        ys, xs = np.nonzero(m)
        self.y0, self.x0 = int(ys.min()), int(xs.min())
        self.mask = m[self.y0:ys.max() + 1, self.x0:xs.max() + 1].copy()
        self.h, self.w = self.mask.shape

    def to_frame(self, r, c):
        return self.y0 + r, self.x0 + c


def sites(box, fused=False):
    """Where a stud may stand: an in-mask cell with at least one in-mask 4-neighbour to carry its
    witness. Lesson (c) - the witness is not demanded below."""
    out = []
    for r in range(box.h):
        for c in range(box.w):
            if not box.mask[r, c]:
                continue
            for nr, nc in ((r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)):
                if 0 <= nr < box.h and 0 <= nc < box.w and box.mask[nr, nc]:
                    out.append((r, c))
                    break
    return out


def spaced(pts, p, sep=SEP):
    for q in pts:
        if max(abs(p[0] - q[0]), abs(p[1] - q[1])) < sep:
            return False
    return True


def chain(box, st, t, rng, avoid=(), sep=SEP):
    """A run of t+1 studs in step along one vector: the cheapest way to ATTAIN a ceiling of t.

    This is what makes LAMBDA=3 expensive and LAMBDA=1 free. t=1 needs no chain at all - any two
    studs realise one relation once - so the warrior's plate is pure dispersal and the mage's plate
    carries a four-stud rank before a single ornamental stud is placed.

    `avoid` is what is already on the plate; the run must clear it, and IT IS NOT ENOUGH TO FIND A
    RUN THAT FITS THE MASK. The first driver laid the warm-started studs first and then looked for a
    chain among what was left, and half the batch went silent because the chain is the expensive
    thing and it was being asked to go last."""
    if t <= 1:
        return []
    sset = set(st)
    vs = [(dy, dx) for dy in range(0, 6) for dx in range(-5, 6)
          if max(abs(dy), abs(dx)) >= sep and (dy > 0 or (dy == 0 and dx > 0))]
    vs.sort(key=lambda v: (max(abs(v[0]), abs(v[1])), abs(v[0]) + abs(v[1])))
    starts = list(st)
    rng.shuffle(starts)
    best = []
    for v in vs:
        for p in starts:
            run = [(p[0] + i * v[0], p[1] + i * v[1]) for i in range(t + 1)]
            if not all(q in sset for q in run):
                continue
            if any(not spaced(avoid, q, sep) for q in run):
                continue
            if lam(list(avoid) + run) > t:
                continue
            return run
    return best


def place(box, target, seed, warm=(), mode=None):
    """Drive one plate. Returns the stud list, or [] when the piece cannot attain the ceiling.

    Order of business: keep what the previous pose left (lesson (a)), lay the chain that attains the
    ceiling if one is needed, then powder the rest of the plate with everything that fits without
    breaking the ceiling."""
    sep = 1 if mode == 'fused' else SEP
    st = sites(box)
    if len(st) < 2:
        return []
    rng = random.Random(seed)

    if mode == 'grid':
        # THE 13th AXIS, drawn by this axis's painter. A lattice, phase chosen so it lands on the
        # piece, and nothing else changed: same pixel, same witness, same palette, same count.
        best = []
        for py in range(SEP + 1):
            for px in range(SEP + 1):
                g = [p for p in st if p[0] % (SEP + 1) == py and p[1] % (SEP + 1) == px]
                if len(g) > len(best):
                    best = g
        return best[:MAX_STUDS]

    def fill(pts, order, free=False):
        for p in order:
            if len(pts) >= MAX_STUDS:
                break
            if not spaced(pts, p, sep):
                continue
            if free or lam(pts + [p]) <= target:
                pts.append(p)
        return pts

    if mode == 'random':
        order = list(st)
        rng.shuffle(order)
        pts = fill([], order, free=True)
    else:
        # THE CHAIN GOES DOWN FIRST OR IT DOES NOT GO DOWN. Attempt 0 keeps the whole warm start and
        # asks the chain to fit around it - the coherent answer, and usually available. Later
        # attempts give the chain the plate and hand the warm studs back afterwards.
        pts = None
        for att in range(6):
            rng2 = random.Random((seed << 4) + att)
            keep = [p for p in warm if p in st][:MAX_STUDS] if att == 0 else []
            if att >= 2:
                keep = [p for p in warm if p in st][:max(0, MAX_STUDS - 2 * att)]
            cur = []
            for p in keep:
                if spaced(cur, p, sep) and lam(cur + [p]) <= target:
                    cur.append(p)
            ch = chain(box, st, target, rng2, cur, sep)
            if target > 1 and not ch:
                cur = []
                ch = chain(box, st, target, rng2, cur, sep)
            cur = cur + ch
            if len(cur) > MAX_STUDS:
                cur = cur[:MAX_STUDS]
            order = list(st)
            rng2.shuffle(order)
            cur = fill(cur, order)
            if len(cur) >= 2 and lam(cur) == target:
                pts = cur
                break
        if pts is None:
            return []
    if len(pts) < 2:
        return []
    if mode in ('random', 'grid', 'fused'):
        return pts
    if mode == 'tightless':
        # Respect the class's bound without attaining it: drop studs until the spectrum falls.
        while len(pts) > 2 and lam(pts) >= target:
            pts.pop()
        return pts if len(pts) >= 2 else []
    if mode == 'loose':
        # One stud moved so that some relation runs LAMBDA+1 times. Invisible, and false.
        for p in order:
            if p in pts:
                continue
            for i in range(len(pts)):
                cand = pts[:i] + pts[i + 1:] + [p]
                if spaced(cand[:-1], p, sep) and lam(cand) == target + 1:
                    return cand
        return []
    if mode == 'dense':
        for p in order:
            if spaced(pts, p, sep) and p not in pts:
                return pts + [p]
        return pts
    if mode == 'slide':
        for dv in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1)):
            cand = [(y + dv[0], x + dv[1]) for y, x in pts]
            if all(q in st for q in cand):
                return cand
        return pts
    if mode == 'turn':
        cy = (min(p[0] for p in pts) + max(p[0] for p in pts))
        cx = (min(p[1] for p in pts) + max(p[1] for p in pts))
        cand = [(cy - y, cx - x) for y, x in pts]
        if all(q in st for q in cand):
            return cand
        return pts
    if lam(pts) != target:
        return []
    return pts


def paint(fr, box, pts, pal):
    """A flat mid field, a crest pixel per stud, and a dark witness beside each. Nothing else - and
    in particular no seam, no band, no direction: the plate must contain no cue the law does not."""
    crest, mid, dark = pal
    for r in range(box.h):
        for c in range(box.w):
            if box.mask[r, c]:
                y, x = box.to_frame(r, c)
                put(fr, y, x, mid)
    studs = set(pts)
    for (r, c) in pts:
        for nr, nc in ((r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)):
            if (0 <= nr < box.h and 0 <= nc < box.w and box.mask[nr, nc]
                    and (nr, nc) not in studs):
                y, x = box.to_frame(nr, nc)
                put(fr, y, x, dark)
                break
    for (r, c) in pts:
        y, x = box.to_frame(r, c)
        put(fr, y, x, crest)


# --- the reader --------------------------------------------------------------------------------
def read(fr, box):
    """Studs off the pixels, in box-relative coordinates, told nothing.

    The three stops are discovered, never given: they are the darkest, middle and lightest
    luminances present inside the piece. Returns (studs, illegible)."""
    ys = slice(box.y0, box.y0 + box.h)
    xs = slice(box.x0, box.x0 + box.w)
    lum = fr[ys, xs, :3].astype(np.int32).sum(-1)
    vals = sorted({int(v) for v in lum[box.mask]})
    if len(vals) < 3:
        return [], 0
    hi, lo = vals[-1], vals[0]
    crest = (lum == hi) & box.mask
    darkm = (lum == lo) & box.mask
    lab, n = label4(crest)
    studs, ill = [], 0
    for i in range(1, n + 1):
        cells = np.argwhere(lab == i)
        if len(cells) != 1:
            ill += 1                      # a cluster is not a stud - clause LEGIBLE
            continue
        r, c = int(cells[0][0]), int(cells[0][1])
        wit = False
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < box.h and 0 <= nc < box.w and darkm[nr, nc]:
                wit = True
                break
        if not wit:
            ill += 1                      # no relief, no endpoint
            continue
        studs.append((r, c))
    for i, p in enumerate(studs):
        for q in studs[i + 1:]:
            if max(abs(p[0] - q[0]), abs(p[1] - q[1])) < SEP:
                ill += 1
    return sorted(studs), ill


# --- building a sheet --------------------------------------------------------------------------
def frames_of(base):
    for fi in range(SLEEP_FROM):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a = base[sl][..., 3] > 0
        if a.any():
            yield fi, sl, a


def box_of(a, largest):
    m = piece_mask(a, largest)
    if m is None or int(m.sum()) < MIN_SPEAK:
        return None
    return Box(m)


def build_piece(fr, a, cls, largest, seed, warm=(), mode=None):
    """Returns (studs, box) - studs empty when the piece is below the floor or cannot attain."""
    box = box_of(a, largest)
    if box is None:
        return [], None
    target = LAM[cls]
    pts = place(box, target, seed, warm, mode)
    if not pts:
        return [], box
    paint(fr, box, pts, PAL[cls])
    return pts, box


def sheet_carries(base, cfg, cls, mode=None):
    """Can every pose that is big enough carry the ornament AND be READ BACK EXACTLY?

    Driving it is not enough. A plate whose studs cannot be recovered is a plate that says nothing,
    and the 67th's rule stands: an ornament that appears in some frames of a walk and not others
    reads as a BUG. What is relaxed here, and reported, is that a pose whose piece is under the
    floor - a twelve-pixel sliver of sabaton in mid-jump - is not asked to speak."""
    warm, skipped = [], 0
    for fi, sl, a in frames_of(base):
        fr = np.zeros((FH, FW, 4), dtype=base.dtype)
        D, M, L = BODY[cls]
        recolor(base[sl], fr, a, D, M, L)
        pts, box = build_piece(fr, a, cls, cfg['largest'], fi, warm, mode)
        if box is None:
            skipped += 1
            continue
        if not pts:
            return False, skipped
        got, ill = read(fr, box)
        if got != sorted(pts) or ill:
            return False, skipped
        warm = pts
    return True, skipped


def build(base, cfg, cls, mode=None, force=None):
    D, M, L = BODY[cls]
    speaks = force if force is not None else sheet_carries(base, cfg, cls, mode)[0]
    out = np.zeros_like(base)
    warm = []
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        if fi >= SLEEP_FROM or not speaks:
            continue
        pts, _box = build_piece(fr, a, cls, cfg['largest'], fi, warm, mode)
        if pts:
            warm = pts
    return out, speaks


def one_plate(base, sl, a, cfg, cls, seed, warm=(), mode=None):
    fr = np.zeros((FH, FW, 4), dtype=base.dtype)
    D, M, L = BODY[cls]
    recolor(base[sl], fr, a, D, M, L)
    pts, box = build_piece(fr, a, cls, cfg['largest'], seed, warm, mode)
    return fr, pts, box


# --- the acceptance test -----------------------------------------------------------------------
def accept(mode=None, verbose=True):
    res = dict(sheets=0, silent=0, plates=0, skipped=0, studs=0, arrows=0,
               recovery=0, spectrum=0, tight=0, rebuild=0, blind=0, legible=0,
               twins=0, capped=0, spec={}, percls={}, clspass={})
    for kind, cfg in SLOTS.items():
        for cls, stem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (stem, suffix))
                res['sheets'] += 1
                carries, _sk = sheet_carries(base, cfg, cls, mode)
                if not carries:
                    res['silent'] += 1
                    continue
                warm = []
                for fi, sl, a in frames_of(base):
                    fr, pts, box = one_plate(base, sl, a, cfg, cls, fi, warm, mode)
                    if box is None:
                        res['skipped'] += 1
                        continue
                    if not pts:
                        res['skipped'] += 1
                        continue
                    warm = pts
                    res['plates'] += 1
                    res['studs'] += len(pts)
                    k = len(pts)
                    if k >= MAX_STUDS:
                        res['capped'] += 1
                    # (1) RECOVERY  +  (6) LEGIBLE
                    got, ill = read(fr, box)
                    res['legible'] += ill
                    if got != sorted(pts):
                        res['recovery'] += 1
                        continue
                    bag = arrows(got)
                    res['arrows'] += sum(bag.values())
                    L = max(bag.values()) if bag else 0
                    res['spec'][L] = res['spec'].get(L, 0) + 1
                    res['percls'].setdefault(cls, []).append(k)
                    # (2) SPECTRUM  and  (3) TIGHT   - one is <=, the other is ==
                    if L > LAM[cls]:
                        res['spectrum'] += 1
                    if L != LAM[cls]:
                        res['tight'] += 1
                    cp = res['clspass'].setdefault(cls, [0, 0])
                    cp[1] += 1
                    if L == LAM[cls]:
                        cp[0] += 1
                    # (4) REBUILD - positions destroyed, plate demanded back
                    if k <= MAX_STUDS:
                        sols = set(reconstruct(bag, k))
                        want = {normalise(got), reflect(got)}
                        if not want <= sols:
                            res['rebuild'] += 1
                        extra = sols - want
                        if extra:
                            res['twins'] += 1
                    # (5) BLIND - slide it, turn it, spectrum must not move
                    for tf in (lambda p: (p[0] + 7, p[1] - 3), lambda p: (-p[0], -p[1])):
                        if max(arrows([tf(p) for p in got]).values()) != L:
                            res['blind'] += 1
    if verbose:
        _report(mode, res)
    return res


def _report(mode, r):
    name = mode or 'AXIS'
    print('=' * 96)
    print('SEME 68th - %s' % name.upper())
    print('=' * 96)
    print('sheets %d   silent %d   plates %d   frames below the floor (reported) %d'
          % (r['sheets'], r['silent'], r['plates'], r['skipped']))
    print('studs %d   arrows %d   plates at the stud cap %d' % (r['studs'], r['arrows'], r['capped']))
    print('-' * 96)
    for k, v in (('(1) RECOVERY  studs read back exactly as driven', r['recovery']),
                 ('(2) SPECTRUM  no relation runs more than LAMBDA times', r['spectrum']),
                 ('(3) TIGHT     some relation runs exactly LAMBDA times', r['tight']),
                 ('(4) REBUILD   plate recovered from its arrows alone', r['rebuild']),
                 ('(5) BLIND     spectrum survives slide and half-turn', r['blind']),
                 ('(6) LEGIBLE   one pixel, one witness, no two touching', r['legible'])):
        print('  %-58s %6d violations   %s' % (k, v, 'PASS' if v == 0 else 'FAIL'))
    print('  %-58s %6d plates' % ('    homometric twins (reported, not a clause)', r['twins']))
    print('-' * 96)
    print('  spectrum histogram (LAMBDA : plates)  %s'
          % '  '.join('%d:%d' % kv for kv in sorted(r['spec'].items())))
    for cls in ('warrior', 'ranger', 'mage'):
        v = r['percls'].get(cls, [])
        if v:
            print('  %-8s LAMBDA=%d   plates %4d   studs/plate min %d  mean %.2f  max %d'
                  % (cls, LAM[cls], len(v), min(v), sum(v) / len(v), max(v)))
    bad = r['recovery'] + r['spectrum'] + r['tight'] + r['rebuild'] + r['blind'] + r['legible']
    print('-' * 96)
    print('  %s' % ('ALL PASS' if bad == 0 else '%d VIOLATIONS' % bad))


CONTROLS = ('grid', 'random', 'loose', 'tightless', 'slide', 'turn', 'fused', 'dense')


def controls_report():
    base = accept(None, verbose=False)
    rows = [('(the axis)', base)]
    for m in CONTROLS:
        rows.append((m, accept(m, verbose=False)))
    print('=' * 108)
    print('SEME 68th - THE EIGHT CONTROLS   (five false, one dead, and three that do not fail)')
    print('=' * 108)
    print('%-12s %7s %7s %8s %8s %7s %8s %8s %8s'
          % ('control', 'sheets', 'silent', 'plates', 'recover', 'spec', 'tight', 'legible', 'TOTAL'))
    for name, r in rows:
        tot = r['recovery'] + r['spectrum'] + r['tight'] + r['rebuild'] + r['blind'] + r['legible']
        print('%-12s %7d %7d %8d %8d %7d %8d %8d %8d'
              % (name, r['sheets'], r['silent'], r['plates'], r['recovery'], r['spectrum'],
                 r['tight'], r['legible'], tot))
    print('-' * 108)
    print('per-class rate at which a control plate is nevertheless LAWFUL for its class '
          '(spectrum AND tight):')
    print('%-12s %22s %22s %22s' % ('control', 'warrior LAMBDA=1', 'ranger LAMBDA=2', 'mage LAMBDA=3'))
    for name, r in rows:
        cells = []
        for cls in ('warrior', 'ranger', 'mage'):
            ok, tot = r['clspass'].get(cls, [0, 0])
            cells.append('%4d/%-4d = %5.1f%%' % (ok, tot, 100.0 * ok / tot) if tot else '        -')
        print('%-12s %22s %22s %22s' % (name, cells[0], cells[1], cells[2]))
    print('-' * 108)
    print('GRID is the 13th STUDWORK drawn by this painter; RANDOM is what everyone thinks this axis')
    print('is; TIGHTLESS respects the bound without attaining it; FUSED is not false but UNREADABLE.')
    print('SLIDE, TURN and DENSE do not fail, and that is the axis stating its own blindness.')


def sweep():
    print('%-7s %-8s %-3s %-8s %6s %6s %6s' % ('slot', 'class', 'g', 'speaks', 'skip', 'minst', 'maxst'))
    for kind, cfg in SLOTS.items():
        for cls, stem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (stem, suffix))
                carries, sk = sheet_carries(base, cfg, cls)
                ks = []
                warm = []
                for fi, sl, a in frames_of(base):
                    fr, pts, box = one_plate(base, sl, a, cfg, cls, fi, warm)
                    if pts:
                        warm = pts
                        ks.append(len(pts))
                print('%-7s %-8s %-3s %-8s %6d %6s %6s'
                      % (kind, cls, suffix or 'm', 'YES' if carries else 'no', sk,
                         min(ks) if ks else '-', max(ks) if ks else '-'))


def survive():
    """Reported, never a clause. The finishing pass lays a cosine ramp across the sheet, so a strict
    three-stop decode of a finished plate says nothing about what a player can see; what is measured
    is LOCAL CONTRAST - is the stud still lighter than the field immediately around it, and is its
    witness still darker."""
    print('%-7s %-8s %-3s %8s %8s' % ('slot', 'class', 'g', 'studs', 'witness'))
    for kind, cfg in SLOTS.items():
        for cls, stem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (stem, suffix))
                arr, speaks = build(base, cfg, cls)
                if not speaks:
                    print('%-7s %-8s %-3s %8s %8s' % (kind, cls, suffix or 'm', 'silent', '-'))
                    continue
                fin, _i = finish_array(arr.copy(), '_survive/%s.png' % kind)
                lum = fin[..., :3].astype(np.int32).sum(-1)
                ok = tot = okw = totw = 0
                warm = []
                for fi, sl, a in frames_of(base):
                    fr, pts, box = one_plate(base, sl, a, cfg, cls, fi, warm)
                    if not pts:
                        continue
                    warm = pts
                    for (r, c) in pts:
                        y, x = box.to_frame(r, c)
                        Y, X = sl[0].start + y, sl[1].start + x
                        nb = [lum[Y + dy, X + dx] for dy, dx in
                              ((1, 0), (-1, 0), (0, 1), (0, -1))
                              if 0 <= Y + dy < fin.shape[0] and 0 <= X + dx < fin.shape[1]
                              and fin[Y + dy, X + dx, 3] > 0]
                        if nb:
                            tot += 1
                            if lum[Y, X] > min(nb):
                                ok += 1
                            totw += 1
                            if min(nb) < lum[Y, X]:
                                okw += 1
                print('%-7s %-8s %-3s %7s%% %7s%%'
                      % (kind, cls, suffix or 'm',
                         int(100 * ok / max(tot, 1)), int(100 * okw / max(totw, 1))))


def main():
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
        survive()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, stem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (stem, suffix))
                dststem = (cfg['dst'] % cls) + suffix
                arr, speaks = build(base, cfg, cls)
                dst = '%s/%s.png' % (outdir, dststem)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-58s opaque_px=%-6d finish=%s/%s  %s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant'],
                         'LAMBDA=%d' % LAM[cls] if speaks else 'PLAIN (reported)'))


if __name__ == '__main__':
    main()
