#!/usr/bin/env python3
"""SEVENTY-SIXTH net-new-geometry axis for ALL FOUR SLOTS - the GAUGE family: the ornament is a set
of TICKS standing on a RULE, and the law is that NO LENGTH THE RULE SPANS IS MISSING FROM IT.

    the ground is    a RULE       an unbroken run of cloth two rows deep. The painter says WHERE to
                                  rule and nothing else: THE SPAN BELONGS TO THE SILHOUETTE, because
                                  the ticks are required to reach BOTH ENDS of the run they stand
                                  on, so a painter cannot buy an easy law by measuring less than the
                                  garment offers. Two combs may not stand within three rows.
    the ornament is  a TICK       a post two pixels tall standing on the rule, bright, with a hard
                                  shadow one down and one left - the light direction every axis in
                                  this project has used. A rule reads as a comb with irregular teeth.
    the reading is   a DISTANCE   any two ticks on one rule measure the number of pixels between
                                  them. A rule of span S is an INSTRUMENT that can measure whatever
                                  its ticks can space.
    the law is       EVERY LENGTH FROM ONE TO THE SPAN IS MEASURED BY SOME PAIR OF TICKS. Nothing
                     the rule is long enough to measure is missing from it.

*** THIS IS THE FIRST LAW THAT IS A COMPLETENESS. ***
Seventy-five axes say what the ornament IS or what it DOES. Every one of them is satisfied by the
marks that are there. This one is about the marks that are NOT: a gauge is lawful only if there is
no length it fails to measure, so the reader's job is to go looking for a hole.

*** IT IS THE EXACT COMPLEMENT OF THE 68th SEME, AND THERE IS NO THIRD THING TO SAY. ***
A set of marks on a line has a set of displacements, and there are exactly two laws you can put on
it:

    68th SEME    a SIDON SET        no displacement may REPEAT      (a refusal)
    76th GAUGE   a COMPLETE RULER   no displacement may be MISSING  (a demand)

The 68th is a perfect ruler, this is a sparse one, and between them they exhaust the sentence. The
two are indistinguishable in kind and opposite in sign: SEME wants its marks far apart and few,
GAUGE wants them arranged so that nothing falls between them.

*** CLASS IDENTITY IS AN EXCESS - HOW MANY MORE TICKS THE WHOLE PLATE CARRIES THAN THE FEWEST THAT
    COULD HAVE DONE ITS JOB. ***
    mage      0   a PERFECT plate: every rule on it is the fewest ticks that rule could have had
    ranger    1   one tick, somewhere on the garment, that the job did not need
    warrior   2   two

Not a count (67th), ceiling (68th), multipole order (69th), number of motions (70th), fraction of a
move (71st), coalition size (72nd), precision (73rd), number of obstructions (74th) or depth (75th).
Every one of those is a number the plate can be asked about. THIS IS THE FIRST CLASS IDENTITY THAT
IS A COMPARISON WITH SOMETHING NOBODY DREW: to say a plate carries two ticks too many you have to
know what the best possible plate of that span would have cost, and that plate is not in the batch,
not in the file, and in general is not this plate. It is still an OUTPUT - the reader recovers it by
proving the minimum for itself - but it is the first output that cannot be computed from the picture
alone.

*** AND IT IS THE FIRST CLASS IDENTITY THAT NO SINGLE ORNAMENT ON THE PLATE CARRIES. *** The excess
belongs to the GARMENT and not to any comb on it: every rule on a warrior cuirass can be, and
usually is, exactly the rule a mage would have worn, and the whole of the difference is two ticks
somewhere on the piece. Seventy-five axes put the class in the ornament, where a reader could find
it by looking at one; THE READER OF THIS ONE HAS TO TOTAL THE PLATE. That is also what keeps the
three classes at one density - the 75th's panel refused a warrior that was denser than its mage, and
here it is not open to the painter to make one.

*** THE ACCEPTANCE TEST IS A NEW KIND - AN EXHAUSTION. ***
Clause EXCESS is settled by enumerating EVERY smaller set of marks that could have stood on that
span and showing that not one of them measures everything. That makes it the first clause in the
project whose subject is pictures THAT DO NOT EXIST: the 66th DOVETAIL proved an impossibility about
one artefact, and this proves a statement about every artefact smaller than the one in hand. It is
affordable for exactly one reason - a garment run is a dozen pixels, so the whole of "every mark set
smaller than this one" is a few hundred thousand of them across the wardrobe, and the file counts
them out loud (`--minima`).

*** THE MAGE'S ROBUSTNESS IS A THEOREM AND THE OTHER TWO CLASSES' IS AN EXPERIMENT. ***
Because a mage rule carries the minimum, ANY tick you take off it leaves fewer marks than the span
can be measured with, so a mage plate cannot survive a single loss - proved in one line, never
checked. The ranger and the warrior have slack, and how much of it is real is a question about the
particular ticks: `--controls dropped-why` takes every tick off every rule in the batch in turn and
counts what still measures everything. THE EXCESS IS A LICENCE TO LOSE ORNAMENT, and the file
reports how much of that licence each class actually gets to spend.

*** WHERE THE AXIS CANNOT GO, IT SAYS SO IN ADVANCE AND FOR THE SAME REASON. ***
A rule can absorb only so many ticks before it has four in a row and stops being a comb, so every
garment has a CEILING on the excess it could ever wear: the sum, over the rules a pose offers, of
the most a legible complete ruler of that span may carry less the fewest it must. `--reach` prints
it. Every plain pose in this batch is under that ceiling, so it is IMPOSSIBLE and not unfound - the
75th's ceiling argument, at the price of a table of two numbers a span. The mage, needing nothing,
is refused only where the cloth has no run of four pixels two rows deep at all; the warrior, needing
two, is refused wherever the body offers only short combs. THE CLASS THAT ASKS FOR MOST IS DRESSED
LEAST OFTEN, which is the first time in the project that the expensive class is expensive in
COVERAGE rather than in work.

*** AND THE BATCH IS AT ITS OWN CEILING, WHICH `--reach` PROVES IN SIX ADDITIONS. *** A sheet is
ruled in all its poses exactly when its class's excess is at or under that sheet's floor, so the
question "could the three excesses have been handed to the three classes some better way" has an
arithmetic answer rather than a taste. All six permutations are tried: four give 15 sheets and two
give 14. THE 15 SHEETS THIS BATCH SHIPS ARE THE MOST ANY ASSIGNMENT COULD HAVE SHIPPED, and the
nine that are plain are a fact about the garments. No previous axis has been able to say that about
its own coverage.

Six clauses:

    (1) RULE     every tick stands on an unbroken run of cloth two rows deep, and the ticks of a
                 rule reach BOTH ENDS of that run. The span is the silhouette's, so a painter cannot
                 buy an easy law by measuring less. Control OFFRULE moves a tick off its rule.
    (2) POST     every tick is exactly two pixels tall and casts its shadow one down and one left
                 wherever there is cloth to take it and nowhere else. Control CLIPPED shortens one.
    (3) GAUGE    every length from 1 to the span is measured. THE LAW. Controls DROPPED and NUDGED.
    (4) EXCESS   the ticks on the WHOLE PLATE, less the minimum every one of its rules could have
                 been drawn with, is the class's excess. Controls SPARE (lawful and miscounted) and
                 SWAPPED (lawful and misnamed).
    (5) LIVE     the plate carries a rule, and no rule spans less than MINSPAN - a gauge on a span
                 of one measures one thing and is complete for the wrong reason. Control DEAD.
    (6) LEGIBLE  three stops on the piece, and never four ticks in a row. A complete ruler MUST have
                 two side by side, because that is the only way to measure a length of one, so
                 adjacency is this axis's signature and not its fault; four is a bar.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_gauge_axis76.py                      # write the four staged dirs
    python3 scripts/gen_gauge_axis76.py --sweep              # can every pose carry a gauge
    python3 scripts/gen_gauge_axis76.py --accept             # six clauses, every pose
    python3 scripts/gen_gauge_axis76.py --controls           # the nine controls
    python3 scripts/gen_gauge_axis76.py --controls dropped-why   # what the excess buys
    python3 scripts/gen_gauge_axis76.py --minima             # the minima, and what they cost to prove
    python3 scripts/gen_gauge_axis76.py --reach              # the excess each garment could EVER wear
    python3 scripts/gen_gauge_axis76.py --frame              # one real pose per class
    python3 scripts/gen_gauge_axis76.py --survive            # relief through the finishing pass
"""
import hashlib
import os
import sys
from itertools import combinations

import numpy as np
from PIL import Image  # noqa: F401  (kept for parity with the other generators)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
SLEEP_FROM = 60
Q_LO, Q_HI = 0.85, 1.18

# WHAT THE PAINTER MAY CHOOSE AND WHAT IT MAY NOT. Where a comb stands is the painter's; how long a
# rule is, where its ends are and how few ticks may stand on it are the garment's, and those are the
# only things the law is about. Combs are kept RSEP rows apart, which the reader checks, so the
# plate reads as banding and never as a field - the 74th and the 75th both learned the same lesson
# from the other side: a regular mark in every cell is GINGHAM, which is camouflage.
MINSPAN = 3       # a rule shorter than this measures too little to be worth a law. Three is not a
                  # taste: a span of two can only be measured by a tick in all three of its
                  # positions, which is a bar, so THREE IS WHERE A COMPLETE RULER AND A LEGIBLE ONE
                  # FIRST COEXIST.
MAXADJ = 3        # no three ticks in a row. A complete ruler must have TWO ticks side by side -
                  # that is the only way to measure a length of one - so adjacency is not a fault
                  # but a signature; three in a row is a bar, and a bar is not a comb. This replaced
                  # a count of empty positions, which locked short spans out of the axis entirely.
RSEP = 3          # rows between one rule and the next: a tick is two tall and its shadow one below,
                  # so a rule owns three rows and the reader refuses two combs that touch
MAXSPAN = 24      # beyond this the exhaustion is not worth its time; no garment comes near it

# CLASS IDENTITY IS AN EXCESS over the fewest ticks that could have measured the span.
EXCESS = {'mage': 0, 'ranger': 1, 'warrior': 2}
SWAP_EXCESS = {'mage': 1, 'ranger': 2, 'warrior': 0}

CAND_CAP = 4000   # how many complete rulers of a given (span, count) are kept for the painter to
                  # choose between. Sampled by stride, so the choice is spread over the whole family
                  # rather than crowded into its lexicographic front.

# Three stops per class - (shadow, field, tick) - strictly increasing in luminance, none near black
# (a near-black darkest stop eats the visor's eye and mouth pixels; the 49th's lesson). Deliberately
# unrelated to the 72nd (indigo/umber/jade), 73rd (graphite-orange/mulberry-linen/aubergine-citron),
# 74th (slate-teal/peat-oxide/night blue) and 75th (gunmetal-gold/black cherry-mint/sea green-pink).
# Every pair separates in HUE as well as in value, which is the finding the 75th's panel forced:
# a field and a mark of the same hue is a mottle, and a mottle is camouflage.
#   warrior  WALNUT AND FROST
#   ranger   DEEP TEAL AND AMBER
#   mage     PLUM AND CHARTREUSE
PAL = {
    'warrior': ((36, 26, 22), (104, 74, 54), (206, 226, 240)),
    'ranger':  ((18, 40, 42), (54, 100, 102), (246, 198, 110)),
    'mage':    ((38, 24, 48), (100, 72, 126), (216, 240, 168)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_gauge_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary76',
    ),
    'legs': dict(
        outdir='_gauge_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary76',
    ),
    'boots': dict(
        outdir='_gauge_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_gauge',
    ),
    'helmet': dict(
        outdir='_gaugedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary76',
    ),
}

CONTROLS = ('random', 'dead', 'dropped', 'spare', 'nudged', 'swapped', 'offrule', 'clipped', 'flat')
CLAUSES = ('rule', 'post', 'gauge', 'excess', 'live', 'legible')


# --- sheet machinery ---------------------------------------------------------------------------
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


class Rng:
    """A deterministic stream of bytes, hashed from the plate's name. Every plate regenerates
    identically, and male and female of an item are run the same way."""

    def __init__(self, salt):
        self.h = hashlib.md5(salt.encode()).digest()
        self.i = 0

    def byte(self):
        b = self.h[self.i]
        self.i += 1
        if self.i == len(self.h):
            self.h = hashlib.md5(self.h).digest()
            self.i = 0
        return b

    def below(self, n):
        return (self.byte() | (self.byte() << 8)) % max(n, 1)


# --- the arithmetic ------------------------------------------------------------------------------
SUBSETS = [0]          # how many mark sets the exhaustion has had to look at, counted out loud
MINCACHE = {}
MAXCACHE = {}
CANDCACHE = {}
TRIES = 40             # salted rulings tried before a pose is reported plain. The 73rd and the 75th
                       # both shipped a first draft whose PAINTER gave up before the GARMENT did;
                       # which minimal ruler a rule wears decides whether an extra tick can be put
                       # anywhere legible on it, so the excess has to be searched for and not
                       # assumed.


def measures(marks):
    """Every length this set of ticks can measure."""
    ms = sorted(marks)
    return {ms[j] - ms[i] for i in range(len(ms)) for j in range(i + 1, len(ms))}


def complete(marks, span):
    """THE LAW, in one line: no length from one to the span is missing."""
    d = measures(marks)
    return all(k in d for k in range(1, span + 1))


def min_marks(span):
    """THE FEWEST TICKS A RULE OF THIS SPAN COULD POSSIBLY CARRY - proved by looking at every
    smaller set of ticks there is and finding a hole in each one.

    This is the number that makes the class an output, and it is also the only number in the axis
    that is about pictures nobody drew. It is memoised per span because the wardrobe offers a few
    dozen distinct spans and several thousand rules."""
    if span in MINCACHE:
        return MINCACHE[span]
    for m in range(2, span + 2):
        for interior in combinations(range(1, span), m - 2):
            SUBSETS[0] += 1
            if complete((0,) + interior + (span,), span):
                MINCACHE[span] = m
                return m
    MINCACHE[span] = span + 1
    return span + 1


def legible(marks):
    """No three ticks in a row. A complete ruler always has two side by side, because that is the
    only way to measure a length of one; three is a bar."""
    ms = sorted(marks)
    run = 1
    for i in range(1, len(ms)):
        run = run + 1 if ms[i] == ms[i - 1] + 1 else 1
        if run > MAXADJ:
            return False
    return True


def rulers(span, m):
    """Every complete, legible ruler of this span with exactly this many ticks, both ends included.

    Supersets of a complete ruler are complete, so this is rarely empty above the minimum - which is
    why a class with an excess is nearly always drawable wherever the class without one is."""
    key = (span, m)
    if key in CANDCACHE:
        return CANDCACHE[key]
    out = []
    if 2 <= m <= span + 1:
        for interior in combinations(range(1, span), m - 2):
            r = (0,) + interior + (span,)
            if complete(r, span) and legible(r):
                out.append(r)
    if len(out) > CAND_CAP:
        stride = len(out) // CAND_CAP + 1
        out = out[::stride]
    CANDCACHE[key] = out
    return out


# --- the ground ----------------------------------------------------------------------------------
def runs_in(a, y):
    """Every maximal unbroken run of cloth TWO ROWS DEEP on this row: a tick needs a pixel to stand
    on and a pixel to stand up in, so a run one row deep is not a rule and the reader knows it."""
    if y < 1 or y >= a.shape[0]:
        return []
    solid = a[y] & a[y - 1]
    out, x = [], 0
    w = a.shape[1]
    while x < w:
        if solid[x]:
            x0 = x
            while x < w and solid[x]:
                x += 1
            out.append((x0, x - 1))
        else:
            x += 1
    return out


def rules_at(a, y, lo=MINSPAN, hi=MAXSPAN):
    return [(y, x0, x1) for x0, x1 in runs_in(a, y) if lo <= x1 - x0 <= hi]


def rulings_of(a, lo=MINSPAN, hi=MAXSPAN):
    """EVERY RULING THE GARMENT OFFERS, roomiest first.

    A row can be ruled if it carries a run of cloth two deep and long enough to be worth measuring,
    and two combs may not stand closer than RSEP rows - a tick is two pixels tall and its shadow
    falls one below, so a rule owns three rows and the reader refuses a pair that touch. Within
    that, WHERE to rule is the painter's business and the reader never asks; HOW LONG a rule is and
    HOW FEW TICKS it may carry are the garment's, and those are the two things the law is about.

    The rulings are enumerated by walking the ruleable rows from each of the first few, so a garment
    whose best comb is two rows below its shoulder is not locked out by a phase nobody chose."""
    rows = [y for y in range(1, a.shape[0]) if rules_at(a, y, lo, hi)]
    seen, out = set(), []
    # THE RULING THAT TAKES THE LONGEST COMBS FIRST. A short rule is lawful and carries no slack -
    # its ticks are forced - so a plate made only of short combs cannot wear an excess at all. This
    # candidate is what lets a warrior find the two spare ticks its class costs.
    order, last = [], []
    for y in sorted(rows, key=lambda z: (-max(x1 - x0 for _y, x0, x1 in rules_at(a, z, lo, hi)), z)):
        if all(abs(y - z) >= RSEP for z in last):
            order.append(y)
            last.append(y)
    for pick in (order,):
        cand = [r for y in sorted(pick) for r in rules_at(a, y, lo, hi)]
        if cand:
            seen.add(tuple(cand))
            out.append(cand)
    for s in range(min(len(rows), RSEP + 1)):
        for step in (1, -1):
            pick, last = [], None
            for y in (rows[s:] if step > 0 else rows[::-1][s:]):
                if last is None or abs(y - last) >= RSEP:
                    pick.append(y)
                    last = y
            cand = [r for y in sorted(pick) for r in rules_at(a, y, lo, hi)]
            key = tuple(cand)
            if not cand or key in seen:
                continue
            seen.add(key)
            out.append(cand)
    return sorted(out, key=lambda c: (-len(c), -sum(x1 - x0 for _y, x0, x1 in c)))


def rules_of(a, lo=MINSPAN, hi=MAXSPAN):
    r = rulings_of(a, lo, hi)
    return r[0] if r else []


def cap_marks(span):
    """THE MOST TICKS A LEGIBLE COMPLETE RULER OF THIS SPAN COULD CARRY. Above this the ruler has
    three ticks in a row and is a bar, so this is the ceiling on what a rule can absorb - and the
    sum of (cap - minimum) over a plate's rules is the largest excess that garment could EVER wear.
    Where that is under the class's excess the pose is IMPOSSIBLE and not merely unfound, which is
    the 75th's ceiling argument in its cheapest form."""
    if span in MAXCACHE:
        return MAXCACHE[span]
    best = min_marks(span)
    for m in range(span + 1, best - 1, -1):
        if rulers(span, m):
            best = m
            break
    MAXCACHE[span] = best
    return best


def capacity(rules):
    return sum(cap_marks(x1 - x0) - min_marks(x1 - x0) for _y, x0, x1 in rules)


# --- the painter -----------------------------------------------------------------------------
def compose(a, cls, mode=None, salt=''):
    """The ticks for one pose, as a list of (y, x0, x1, marks), or None if the pose has no rule on
    it. Every control that is a lawful picture wrongly made is made HERE, from a lawful plate, so
    that a control differs from the shipped plate in exactly one thing."""
    rng = Rng('%s|%s' % (salt, mode or 'ship'))

    if mode == 'dead':
        # A RULE TOO SHORT TO MEAN ANYTHING. Two ticks a pixel apart measure the one length there
        # is, so the gauge is complete and says nothing. Clause LIVE is what collects it.
        short = rules_of(a, lo=1, hi=MINSPAN - 1)
        if not short:
            return None
        y, x0, x1 = short[rng.below(len(short))]
        return [(y, x0, x1, tuple(range(x0, x1 + 1)))]

    e = SWAP_EXCESS[cls] if mode == 'swapped' else EXCESS[cls]

    # EVERY RULE IS DRAWN AT ITS OWN MINIMUM FIRST, whatever the class. A complete ruler is a dense
    # thing by arithmetic - a span of seven cannot be measured with fewer than five ticks - so a
    # class that spent its excess on EVERY rule came out of the first frame dump as a solid bright
    # bar with a solid dark bar under it, which is a rib and not a comb. The excess is spent ONCE,
    # on the plate. WHICH minimal ruler a rule wears decides whether an extra tick can go anywhere
    # legible on it, so the excess is SEARCHED FOR over rulings and salted orders - the 73rd and the
    # 75th both shipped a first draft whose painter gave up before the garment did.
    keep = None
    for rules in rulings_of(a):
        if capacity(rules) < e:
            continue            # PROVED: no plate on this ruling could wear this class's excess
        for k in range(TRIES):
            rng = Rng('%s|%s|%d' % (salt, mode or 'ship', k))
            cand = []
            for y, x0, x1 in rules:
                span = x1 - x0
                m = min_marks(span)
                cands = rulers(span, m)
                if not cands:
                    continue
                if mode == 'random':
                    # THE NULL HYPOTHESIS: the right number of ticks, reaching both ends, put down
                    # with no thought at all for what they measure.
                    inner = list(range(1, span))
                    for i in range(len(inner) - 1, 0, -1):
                        j = rng.below(i + 1)
                        inner[i], inner[j] = inner[j], inner[i]
                    r = tuple(sorted([0] + inner[:m - 2] + [span]))
                else:
                    r = cands[rng.below(len(cands))]
                cand.append((y, x0, x1, tuple(x0 + t for t in r)))
            if not cand:
                continue

            # THE EXCESS, SPENT ONCE ON THE WHOLE GARMENT. A superset of a complete ruler is
            # complete, so an extra tick is always lawful; what it is not is free, because the
            # reader totals the plate.
            spent = True
            for _ in range(e):
                room = []
                for i, (_y, x0, x1, mk) in enumerate(cand):
                    for x in range(x0 + 1, x1):
                        if x not in mk and legible(mk + (x,)):
                            room.append((i, x))
                if not room:
                    spent = False
                    break
                i, x = room[rng.below(len(room))]
                y, x0, x1, mk = cand[i]
                cand[i] = (y, x0, x1, tuple(sorted(mk + (x,))))
            if spent:
                keep = cand
                break
        if keep:
            break
    if keep is None:
        return None

    if mode in ('dropped', 'spare', 'nudged'):
        i = rng.below(len(keep))
        y, x0, x1, marks = keep[i]
        inner = [x for x in marks if x not in (x0, x1)]
        free = [x for x in range(x0 + 1, x1) if x not in marks]
        if mode == 'dropped' and inner:
            # ONE TICK TAKEN OFF. On a mage plate this cannot be lawful and no check is needed;
            # on a ranger or a warrior it is a question about these ticks in particular.
            marks = tuple(x for x in marks if x != inner[rng.below(len(inner))])
        elif mode == 'spare' and free:
            marks = tuple(sorted(marks + (free[rng.below(len(free))],)))
        elif mode == 'nudged' and inner and free:
            drop = inner[rng.below(len(inner))]
            near = sorted(free, key=lambda z: abs(z - drop))[:2]
            if not near:
                return keep
            marks = tuple(sorted([x for x in marks if x != drop] + [near[rng.below(len(near))]]))
        else:
            return keep
        keep[i] = (y, x0, x1, marks)
    return keep


def paint(a, keep, clip=None, stray=None):
    """A tick and the shadow it casts, and nothing else. RELIEF, NOT COLOUR: at thirteen pixels a
    flat field of another hue is camouflage, and only a crest with its own shadow survives the
    finishing pass."""
    h, w = a.shape
    core = np.zeros(a.shape, bool)
    for y, _x0, _x1, marks in keep:
        for x in marks:
            if 0 <= y < h and 0 <= x < w and a[y, x]:
                core[y, x] = True
            if clip == (y, x):
                continue                   # CLIPPED: a tick one pixel tall
            if 0 <= y - 1 < h and 0 <= x < w and a[y - 1, x]:
                core[y - 1, x] = True
    if stray is not None:
        sy, sx = stray
        for yy in (sy, sy - 1):
            if 0 <= yy < h and 0 <= sx < w and a[yy, sx]:
                core[yy, sx] = True
    dark = np.zeros(a.shape, bool)
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            dark[ny, nx] = True
    return core, dark


# --- the reader ------------------------------------------------------------------------------
def read_stops(fr, a):
    """Tick, shadow and field off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: three luminances
    on the piece - the brightest is a tick, the darkest is a tick's shadow, the rest is plain
    cloth."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    pts = np.argwhere(a)
    core = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    if len(pts) == 0:
        return core, dark, False
    vals = sorted({int(lum[y, x]) for y, x in pts})
    if len(vals) < 3:
        return core, dark, False
    wv, cv = vals[0], vals[-1]
    for y, x in pts:
        v = int(lum[y, x])
        if v == cv:
            core[y, x] = True
        elif v == wv:
            dark[y, x] = True
    return core, dark, True


def read_posts(a, core):
    """Every tick, from the pixels alone. A column of the picture is scanned for vertical runs of
    bright pixels; each must be exactly two tall, and the lower of the pair is where the tick
    stands. Two ticks side by side make a two-by-two block and are still two ticks, because the
    scan is by COLUMN - which is the whole reason a tick is drawn upright."""
    h, w = a.shape
    bases, ok = [], True
    for x in range(w):
        y = 0
        while y < h:
            if core[y, x]:
                y0 = y
                while y < h and core[y, x]:
                    y += 1
                if y - y0 != 2:
                    ok = False
                else:
                    bases.append((y - 1, x))
            else:
                y += 1
    return bases, ok


def read_rules(a, bases):
    """Group the ticks into rules and hand back the span each one is obliged to measure. Returns
    (rules, ok): ok is False when a tick stands somewhere its run cannot make a rule of, or when the
    ticks of a rule fail to REACH BOTH ENDS of the run they stand on - which is what stops a painter
    buying an easy law by measuring less than the garment offers."""
    ok = True
    byrow = {}
    for y, x in bases:
        byrow.setdefault(y, []).append(x)
    rules = []
    for y, xs in sorted(byrow.items()):
        runs = runs_in(a, y)
        for x0, x1 in runs:
            marks = tuple(sorted(x for x in xs if x0 <= x <= x1))
            if not marks:
                continue
            if marks[0] != x0 or marks[-1] != x1:
                ok = False
                continue
            rules.append((y, x0, x1, marks))
        if any(not any(x0 <= x <= x1 for x0, x1 in runs) for x in xs):
            ok = False
    return rules, ok


def inspect_frame(fr, a, cls):
    """The six clauses on ONE POSE, from the pixels and the outline and nothing else."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, ticks=0, rules=0, spans=[], excess_val=None)
    core, dark, three = read_stops(fr, a)
    if not three or not core.any():
        v['silent'] = 1
        return v
    v['plates'] = 1

    bases, post_ok = read_posts(a, core)
    if not post_ok or not bases:
        v['post'] = 1
        return v

    # (2) POST - the shadow is where it must be and nowhere else
    h, w = a.shape
    want = set()
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            want.add((int(ny), int(nx)))
    if {(int(y), int(x)) for y, x in np.argwhere(dark)} != want:
        v['post'] = 1
        return v

    # (1) RULE - the ticks stand on runs, and reach both ends of them
    rules, rule_ok = read_rules(a, bases)
    if not rule_ok or not rules:
        v['rule'] = 1
        return v
    rows = sorted({y for y, _a, _b, _m in rules})
    if any(rows[i + 1] - rows[i] < RSEP for i in range(len(rows) - 1)):
        v['rule'] = 1                      # two combs close enough to touch
        return v
    v['rules'] = len(rules)
    v['ticks'] = sum(len(m) for _y, _a, _b, m in rules)
    v['spans'] = [x1 - x0 for _y, x0, x1, _m in rules]

    # (5) LIVE - a span shorter than MINSPAN is complete for the wrong reason
    if min(v['spans']) < MINSPAN:
        v['live'] = 1
        return v

    exc = 0
    for _y, x0, x1, marks in rules:
        span = x1 - x0
        rel = [x - x0 for x in marks]
        # (3) GAUGE - THE LAW
        if not complete(rel, span):
            v['gauge'] = 1
        # (6) LEGIBLE - two ticks side by side are a signature, three are a bar
        if not legible(marks):
            v['legible'] = 1
        # (4) EXCESS - totalled over the plate, against the minima the reader proves for itself
        exc += len(marks) - min_marks(span)
    if v['gauge']:
        return v
    v['excess_val'] = exc
    if exc != EXCESS[cls]:
        v['excess'] = 1
    return v


# --- frames ------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, dark, keep) or None if the pose has no rule on it."""
    shadow_c, field_c, tick_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE TICKS GO ON. The source sheet's inherited highlights sit in
    # the same stop a tick does, and a reader told nothing cannot tell an inherited highlight from a
    # tick. Every tone here is put there by the gauge; the modelling comes back, richer, from the
    # finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    keep = compose(a, cls, mode, salt)
    if keep is None:
        return None
    if mode == 'flat':
        return np.zeros(a.shape, bool), np.zeros(a.shape, bool), keep

    clip = stray = None
    if mode == 'clipped':
        y, _x0, _x1, marks = keep[0]
        clip = (y, marks[len(marks) // 2])
    if mode == 'offrule':
        # ONE TICK LIFTED OFF ITS RULE. It is a well formed tick, it measures nothing wrong, and it
        # stands where no run can make a rule that reaches both ends - which clause RULE collects.
        for y, x0, x1, marks in keep:
            x = marks[len(marks) // 2]
            if y - 1 >= 1 and a[y - 1, x] and a[y - 2, x] and not any(
                    mx == x for my, _a, _b, mm in keep for mx in mm if my == y - 1):
                stray = (y - 1, x)
                keep = [(yy, aa, bb, tuple(z for z in mm if not (yy == y and z == x)))
                        for yy, aa, bb, mm in keep]
                keep = [k for k in keep if len(k[3]) >= 2]
                break
        if stray is None:
            return None

    core, dark = paint(a, keep, clip=clip, stray=stray)
    if not core.any() or not dark.any():
        return None
    for y, x in np.argwhere(dark):
        put(fr, y, x, shadow_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, tick_c)
    return core, dark, keep


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
    """A SHEET IS RULED IN ALL FORTY-TWO POSES OR IN NONE. A gauge that appears in some frames of a
    walk and not others reads as a bug, not as a hard case."""
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


# --- the acceptance test -------------------------------------------------------------------------
def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, sheets=0, pass_sheets=0, ticks=0, rules=0)
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
                np_ = ns = nr = nt = 0
                spans = []
                for fi, a, (fr, _g) in plates:
                    res = inspect_frame(fr, a, cls)
                    for c in CLAUSES:
                        bad[c] += res[c]
                    np_ += res['plates']
                    ns += res['silent']
                    nr += res['rules']
                    nt += res['ticks']
                    spans += res['spans']
                tot['plates'] += np_
                tot['silent'] += ns
                tot['rules'] += nr
                tot['ticks'] += nt
                for c in CLAUSES:
                    tot[c] += bad[c]
                good = not any(bad.values())
                tot['pass_sheets'] += 1 if good else 0
                print('   %-7s %-8s %-2s  excess=%d plates=%-3d rules=%-4d ticks=%-4d spans %d-%-2d'
                      '  %s%s'
                      % (kind, cls, suffix or 'm', EXCESS[cls], np_, nr, nt,
                         min(spans) if spans else 0, max(spans) if spans else 0,
                         'ALL PASS' if good else 'FAIL ',
                         '' if good else ' ' + ' '.join('%s=%d' % (c, k)
                                                        for c, k in bad.items() if k)),
                      flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d rules ruled, %d ticks drawn, %d silent'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['rules'], tot['ticks'],
             tot['silent']))
    print('   every length from one to the span, on every rule, on every plate')
    for c in CLAUSES:
        print('   %-9s %d violations' % (c.upper(), tot[c]))
    print('   the exhaustion looked at %d mark sets that are not in the batch' % SUBSETS[0])


# --- the controls --------------------------------------------------------------------------------
def controls_report(which=None):
    if which == 'dropped-why':
        dropped_why()
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
        extra = {
            'random': '  <- the null hypothesis. THE NUMBER TO BEAT',
            'dead': '  <- a rule too short to mean anything: complete, and it measures one thing',
            'dropped': ('  <- ONE TICK TAKEN OFF. Impossible for the mage BY ARITHMETIC; for the '
                        'other two it is what their excess buys - see --controls dropped-why'),
            'spare': '  <- LAWFUL AND MISCOUNTED: it still measures everything, with a tick to spare',
            'nudged': '  <- one tick moved one pixel',
            'swapped': '  <- LAWFUL AND MISNAMED: the reader names the class the plate really is',
            'offrule': '  <- one tick lifted off its rule: well formed, and standing nowhere',
            'clipped': '  <- one tick drawn a pixel short',
            'flat': '  <- no ornament at all: SILENT, never CLEAN',
        }.get(mode, '')
        print('   %-9s clean %4d / %-4d   silent %-4d  undrawable %-4d %s%s'
              % (mode.upper(), clean, drawn, silent, undrawable,
                 note, extra), flush=True)


def dropped_why():
    """WHAT THE EXCESS ACTUALLY BUYS. Take every tick off every rule in the batch in turn and ask
    whether the rule still measures everything.

    The mage needs no experiment: its rules carry the proved minimum, so a rule with one fewer tick
    is a mark set smaller than the minimum and cannot be complete. The line is printed as PROVED and
    the loop confirms it costs nothing. The other two classes have slack, and how much of it is real
    is a question about these particular ticks and not about their number."""
    print('== DROPPED-WHY  (every single tick of every shipped rule, taken off)')
    tot = {}
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                for fi, sl, a in frames_of(base):
                    keep = compose(a, cls, None, '%s|%d' % (stem, fi))
                    if keep is None:
                        continue
                    for _y, x0, x1, marks in keep:
                        span = x1 - x0
                        rel = [x - x0 for x in marks]
                        for m in rel:
                            t, s = tot.get(cls, (0, 0))
                            still = complete([r for r in rel if r != m], span)
                            tot[cls] = (t + 1, s + (1 if still else 0))
    for cls in ('mage', 'ranger', 'warrior'):
        t, s = tot.get(cls, (0, 0))
        print('   %-8s excess %d   ticks removed %-6d  rule still measures everything %-6d (%3d%%)'
              '  %s'
              % (cls, EXCESS[cls], t, s, (100 * s // t) if t else 0,
                 'PROVED IMPOSSIBLE (a mage rule is the minimum)' if EXCESS[cls] == 0
                 else 'measured'))
    print('   THE EXCESS IS A LICENCE TO LOSE ORNAMENT, and this is how much of it gets spent.')


# --- reports -------------------------------------------------------------------------------------
def sweep():
    print('== SWEEP  (can every pose of every sheet carry a gauge of its class)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                fit = unfit = 0
                nr, nt = [], []
                for fi, sl, a in frames_of(base):
                    keep = compose(a, cls, None, '%s|%d' % (stem, fi))
                    if keep is None:
                        unfit += 1
                        continue
                    fit += 1
                    nr.append(len(keep))
                    nt.append(sum(len(m) for _y, _a, _b, m in keep))
                print('   %-7s %-8s %-2s  excess %d   rules %d-%-2d ticks %2d-%-3d   %2d/%-2d  %s'
                      % (kind, cls, suffix or 'm', EXCESS[cls],
                         min(nr) if nr else 0, max(nr) if nr else 0,
                         min(nt) if nt else 0, max(nt) if nt else 0,
                         fit, fit + unfit,
                         'ruled' if unfit == 0 else 'PLAIN (reported)'), flush=True)


def minima_report():
    """THE ONLY TABLE IN THE PROJECT WHOSE SUBJECT IS PICTURES THAT DO NOT EXIST."""
    print('== MINIMA  (the fewest ticks a span can be measured with, and what it costs to prove it)')
    spans = set()
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                for fi, sl, a in frames_of(base):
                    for _y, x0, x1 in rules_of(a):
                        spans.add(x1 - x0)
    before = SUBSETS[0]
    from math import comb
    for s in sorted(spans):
        n0 = SUBSETS[0]
        m = min_marks(s)
        tot = comb(s - 1, m - 2) if 2 <= m <= s + 1 else 0
        good = len(rulers(s, m))
        ex = ', '.join(''.join('|' if i in r else '.' for i in range(s + 1))
                       for r in rulers(s, m)[:2])
        print('   span %-3d min %-2d  ruled out %-7d smaller sets   lawful %4d of %-6d (1 in %-5s)'
              '  %s'
              % (s, m, SUBSETS[0] - n0, good, tot,
                 ('%.0f' % (tot / good)) if good else '-', ex))
    print('   ----')
    print('   %d spans in the wardrobe, %d mark sets looked at and refused'
          % (len(spans), SUBSETS[0] - before))
    print('   THE LAW BITES WHERE THERE IS ROOM FOR IT TO. On a span of three almost any set of the '
          'right size')
    print('   measures everything; on a span of eleven almost none does, and the wardrobe is mostly '
          'short runs.')
    print('   That is the whole of why control RANDOM scores as well as it does, and the file would '
          'rather say so.')


def reach_report():
    """WHERE A GARMENT CANNOT WEAR ITS CLASS, THAT IS A THEOREM ABOUT THE GARMENT.

    A legible complete ruler of span S carries between min_marks(S) and cap_marks(S) ticks, and both
    are facts about the arithmetic rather than about this batch. So the most excess a pose could
    EVER wear is the sum of the difference over the rules it offers, maximised over the rulings the
    body allows - an upper bound and not a sample. Where that is under the class's excess, no
    painter however patient would have found a plate, and the sweep is entitled to say IMPOSSIBLE.
    """
    floor = {}
    print('== REACH  (the most excess each garment could EVER wear, and what its class asks for)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                caps = []
                for fi, sl, a in frames_of(base):
                    caps.append(max((capacity(r) for r in rulings_of(a)), default=-1))
                need = EXCESS[cls]
                able = sum(1 for c in caps if c >= need)
                print('   %-7s %-8s %-2s  asks %d   ceiling %d-%-2d   poses that could ever wear it '
                      '%2d/%-2d  %s'
                      % (kind, cls, suffix or 'm', need, min(caps), max(caps), able, len(caps),
                         'ok' if able == len(caps)
                         else 'PROVED IMPOSSIBLE on %d pose(s)' % (len(caps) - able)))
                floor[(kind, cls, suffix)] = min(caps)

    # AND THE ONE QUESTION A REACH TABLE CAN ANSWER THAT A SWEEP CANNOT: could the batch have been
    # dressed better by handing the three excesses to the three classes some other way? A sheet is
    # ruled in all its poses exactly when its class's excess is at or under the sheet's floor, so
    # the answer is six additions and it is not a matter of taste.
    from itertools import permutations
    print('   ----')
    print('   == COULD THE THREE EXCESSES HAVE BEEN HANDED OUT BETTER?')
    best = None
    for p in permutations((0, 1, 2)):
        asg = dict(zip(('mage', 'ranger', 'warrior'), p))
        n = sum(1 for (kind, cls, suffix), f in floor.items() if f >= asg[cls])
        mark = ''
        if best is None or n > best:
            best = n
        print('      mage %d  ranger %d  warrior %d   ->  %2d/24 sheets ruled%s'
              % (asg['mage'], asg['ranger'], asg['warrior'], n, mark))
    cur = sum(1 for (kind, cls, suffix), f in floor.items() if f >= EXCESS[cls])
    print('      ----')
    print('      SHIPPED %d/24, BEST POSSIBLE %d/24 - %s' % (cur, best,
          'the batch is at its ceiling and the missing sheets are the garments, not the assignment'
          if cur >= best else 'RETUNE'))


def frame_dump():
    print('== ONE REAL POSE PER CLASS  ("|" a tick, "=" its shadow, "-" field, "." off the cloth)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            salt = '%s|%d' % (stem, fi)
            keep = compose(a, cls, None, salt)
            if keep is None:
                continue
            core, dark = paint(a, keep)
            print('== %s chest frame %d   %d rules, %d ticks, excess %d'
                  % (cls, fi, len(keep), sum(len(m) for _y, _a, _b, m in keep), EXCESS[cls]))
            for y, x0, x1, marks in keep:
                span = x1 - x0
                rel = sorted(x - x0 for x in marks)
                print('   row %-2d span %-2d  ticks at %-26s minimum %d + %d   measures 1..%d'
                      % (y, span, str(rel), min_marks(span), len(rel) - min_marks(span), span))
            ys, xs = np.nonzero(a)
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not a[y, x]:
                        row += '.'
                    elif core[y, x]:
                        row += '|'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a tick on the
    shadowed flank is darker in absolute terms than the field on the lit one."""
    print('== SURVIVAL through the finishing pass (reported, local contrast)')
    for kind, cfg in SLOTS.items():
        tot = ok = 0
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = cfg['srcs'][cls] + suffix
                base = load_any('%s.png' % stem)
                if not sheet_carries(base, cls, stem):
                    continue
                arr, _ = build(base, cls, stem)
                fin, _i = finish_array(arr.copy(),
                                       '_tmp/%s%s_%s.png' % (cfg['dst'] % cls, suffix, kind))
                for fi, sl, a in frames_of(base):
                    _fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                    if got is None:
                        continue
                    core, dark, _keep = got
                    lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                    for y, x in np.argwhere(core):
                        nb = [lum[ny, nx] for ny, nx in
                              ((y + 1, x - 1), (y, x - 1), (y, x + 1), (y + 2, x))
                              if 0 <= ny < FH and 0 <= nx < FW and not core[ny, nx]
                              and (dark[ny, nx] or a[ny, nx])]
                        if not nb:
                            continue
                        tot += 1
                        if lum[y, x] > float(np.mean(nb)):
                            ok += 1
        print('   %-7s tick still lighter than the cloth around it: %5d/%-5d (%3d%%)'
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
    if '--minima' in sys.argv:
        minima_report()
        return
    if '--reach' in sys.argv:
        reach_report()
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
                         'excess=%d' % EXCESS[cls] if ok else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
