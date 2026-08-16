#!/usr/bin/env python3
"""SEVENTY-SEVENTH net-new-geometry axis for ALL FOUR SLOTS - the CLASP family: the ornament is a
set of CLASPS on the garment's own lattice, and the law is that the plate is a KNIFE EDGE - NOTHING
CAN BE ADDED TO IT AND NOTHING CAN BE TAKEN AWAY.

    the ground is    a LATTICE    every cloth pixel on one phase of a three-pixel grid is a SOCKET.
                                  The pitch and the sockets belong to the SILHOUETTE; the painter
                                  says only which of the nine phases it used, and the plate is its
                                  own key, because a clasp's two ends are sockets and give the phase
                                  away.
    the ornament is  a CLASP      a straight bright bar four pixels long joining two NEIGHBOURING
                                  sockets - lying down or standing up - with a hard shadow one down
                                  and one left. A socket with no clasp on it carries no ink at all.
    the reading is   a PAIRING    every clasp marries two sockets. A socket is either MARRIED or
                                  BARE, and the reader can see which without being told.
    the law is       NO TWO CLASPS MEET, AND NO TWO BARE SOCKETS MEET. You cannot draw another
                     clasp anywhere on the plate without two clasps sharing a socket, and you cannot
                     rub one out without leaving two bare sockets side by side.

*** THIS IS THE FIRST LAW IN THE PROJECT THAT IS NOT MONOTONE. ***
Every law so far leans one way, and the two clearest cases are next door to each other:

    68th SEME    a SIDON SET        broken by ADDING a mark.     Every SUBSET is still lawful.
    76th GAUGE   a COMPLETE RULER   broken by TAKING one away.   Every SUPERSET is still lawful.
    77th CLASP   a KNIFE EDGE       broken by EITHER.            No subset and no superset survives.

The 76th said of the 68th that a law about a set of marks may forbid a repeat or forbid a gap and
there is no third thing to say. That is true of laws about DISPLACEMENTS and it is the wrong level.
One level up there are exactly three sensitivities a law can have to the marks themselves - it can
be closed downwards, closed upwards, or closed neither way - and the first seventy-six axes are all
of the first two kinds. THIS IS THE THIRD, AND WITH IT THE SENTENCE IS FINISHED.

The consequence is the thing to look at: on a lawful plate there is no ornament that could have been
added and no ornament that could be spared. THE PICTURE IS PINNED.

*** CLASS IDENTITY IS A PRICE - WHAT IT WOULD COST TO CARRY ONE MORE CLASP - AND ONE CLASS CANNOT
    BUY ONE AT ANY PRICE. ***
    warrior    1   break one clasp and two can be made where it was: one clasp better, for one loss
    mage       2   two must come off before three can go on
    ranger     -   NOTHING WILL DO IT. The plate already carries the most clasps the garment can
                   ever hold, and no amount of breaking and re-making beats it.

Which identity goes to which class is settled by arithmetic and not by taste - `--reach` tries all
six ways of handing them out and this is the one that dresses the most garments.

Not a count (67th), ceiling (68th), multipole order (69th), motions (70th), fraction of a move
(71st), coalition (72nd), precision (73rd), obstructions (74th), depth (75th) or excess (76th).
Two things make it new. It is the first class identity that is a COST OF AN IMPROVEMENT THE READER
IS INVITED TO PLAN AND FORBIDDEN TO MAKE - the plate is pinned, so the price is about a picture that
is better than the one shipped and that the law will not let anybody paint. And it is THE FIRST
CLASS IDENTITY WHOSE THIRD VALUE IS NOT A NUMBER: two classes answer "one" and "two", and the
ranger answers "there is no such number". Berge's theorem is what lets the reader say so out loud -
a pairing is the largest there is exactly when no alternating path runs between two bare sockets -
so the ranger's identity is a NON-EXISTENCE the reader can verify, not a failure to find one.

*** THE ACCEPTANCE TEST IS A NEW KIND - A SQUEEZE. ***
Every previous axis is tested by breaking its plates ONE WAY: drop a mark, move a mark, swap a
tincture. This one is squeezed from both sides at once. For every shipped plate the file tries
EVERY clasp the lattice would allow and EVERY clasp the plate carries: each addition must produce
two clasps that meet, and each removal must produce two bare sockets that meet. A plate passes only
if the whole of both lists breaks it. `--pinned` prints the two totals, and they are the axis in one
line: nothing can go on, nothing can come off.

*** WHERE THE AXIS CANNOT GO IT SAYS SO. ***
A price of two needs an alternating path with two clasps in it, which needs six sockets in a row on
the lattice, and a boot at three pixels of pitch is four sockets on its best pose. `--reach`
searches every phase of every pose for each of the three identities and prints which sheets could
ever have worn which, then tries all six ways of handing the three identities to the three classes -
so the coverage this batch ships is compared with the best any assignment could have done, the way
the 76th taught.

Six clauses:

    (1) LATTICE  every clasp joins two sockets of ONE phase of the garment's own three-pixel grid,
                 and lies wholly on cloth. Control OFFGRID moves a clasp a pixel off the grid.
    (2) BAR      every bright run is straight, exactly four pixels long, and casts its shadow one
                 down and one left wherever there is cloth to take it and nowhere else. Controls
                 CLIPPED and MALFORMED.
    (3) KNIFE    THE LAW. No two clasps share a socket; no two bare sockets are neighbours.
                 Controls DOUBLED (one clasp added) and BROKEN (one clasp taken off) - THE PAIR NO
                 PREVIOUS AXIS COULD HAVE RUN, because no previous law was broken by both. The two
                 halves are refused in different places and that is worth watching: an addition is
                 caught by the EYE, because two clasps that meet are drawn as one long or one bent
                 bright thing and the plate stops being made of clasps at all, while a removal is
                 caught by the ARITHMETIC, because what it leaves behind still looks like clasps.
    (4) PRICE    the class: the fewest clasps that must be broken before the plate can carry one
                 more, or NONE for a plate that already carries the most it can. Controls SWAPPED
                 (lawful and misnamed) and NUDGED (one clasp re-married).
    (5) LIVE     the plate carries at least two clasps and stands on a lattice big enough to have a
                 price at all. Control DEAD: two sockets and one clasp is pinned for the wrong
                 reason.
    (6) LEGIBLE  every clasp casts shadow - a bar with no relief is a stripe of colour, and at
                 thirteen pixels a colour is camouflage.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_clasp_axis77.py                  # write the four staged dirs
    python3 scripts/gen_clasp_axis77.py --sweep          # can every pose carry its class
    python3 scripts/gen_clasp_axis77.py --accept         # six clauses, every pose
    python3 scripts/gen_clasp_axis77.py --controls       # the nine controls
    python3 scripts/gen_clasp_axis77.py --pinned         # THE SQUEEZE: every addition, every removal
    python3 scripts/gen_clasp_axis77.py --reach          # which identity each garment could ever wear
    python3 scripts/gen_clasp_axis77.py --frame          # one real pose per class
    python3 scripts/gen_clasp_axis77.py --survive        # relief through the finishing pass
"""
import hashlib
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

# WHAT THE GARMENT OWNS AND WHAT THE PAINTER MAY CHOOSE. The pitch, the sockets and which pairs of
# them a clasp could join are all decided by the outline; the painter chooses the PHASE (one of
# nine) and the pairing. Both are recoverable from the picture, so nothing here is a secret.
PITCH = 3         # three pixels between sockets: at two the pairing has to cover so much of the
                  # cloth that the plate comes out a bright field, which is camouflage (rendered,
                  # looked at, and rejected); at four the lattice is too coarse for a garment to
                  # hold an alternating path.
BARLEN = PITCH + 1   # a clasp is a straight bar this long: two sockets and the pixels between them
MINCLASP = 2      # fewer than two clasps is a mark, not a pattern
MINSOCK = 5       # a lattice with fewer sockets than this is pinned for the wrong reason

# CLASS IDENTITY IS A PRICE. None means NO PRICE AT ALL - the plate already carries the most clasps
# the garment can hold, and Berge's theorem is what lets the reader say so rather than merely fail
# to find an improvement.
# WHICH IDENTITY GOES TO WHICH CLASS IS ARITHMETIC AND NOT TASTE: `--reach` tries all six ways and
# this is the one that dresses the most garments (17/24 against 14 for the worst).
PRICE = {'warrior': 1, 'mage': 2, 'ranger': None}
SWAP_PRICE = {'warrior': 2, 'mage': None, 'ranger': 1}

TRIES = 8         # restarts of the painter's local search per phase
STEPS = 900       # local-search steps per restart

# Three stops per class - (shadow, field, bar) - strictly increasing in luminance, none near black
# (a near-black darkest stop eats the visor's eye and mouth pixels; the 49th's lesson). Deliberately
# unrelated to the 73rd, 74th, 75th and 76th, and every pair separates in HUE as well as in value,
# which is the finding the 75th's panel forced: a field and a mark of the same hue is a mottle, and
# a mottle is camouflage.
#   warrior  OXBLOOD AND PEWTER
#   ranger   SLATE BLUE AND WHEAT
#   mage     BRONZE AND ORCHID
PAL = {
    'warrior': ((34, 14, 16), (112, 42, 44), (198, 204, 212)),
    'ranger':  ((16, 22, 44), (58, 74, 116), (238, 222, 164)),
    'mage':    ((34, 24, 10), (104, 78, 34), (224, 180, 246)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_clasp_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary77',
    ),
    'legs': dict(
        outdir='_clasp_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary77',
    ),
    'boots': dict(
        outdir='_clasp_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_clasp',
    ),
    'helmet': dict(
        outdir='_claspdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary77',
    ),
}

CONTROLS = ('random', 'dead', 'doubled', 'broken', 'nudged', 'swapped', 'offgrid', 'clipped', 'flat')
CLAUSES = ('lattice', 'bar', 'knife', 'price', 'live', 'legible')


# --- sheet machinery -----------------------------------------------------------------------------
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
    """A deterministic stream of bytes, hashed from the plate's name, so every plate regenerates
    identically and male and female of an item are run the same way."""

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

    def shuffled(self, seq):
        out = list(seq)
        for i in range(len(out) - 1, 0, -1):
            j = self.below(i + 1)
            out[i], out[j] = out[j], out[i]
        return out


# --- the ground ----------------------------------------------------------------------------------
def lattice(a, phase):
    """THE SOCKETS AND THE PAIRS A CLASP COULD JOIN, from the outline and a phase and nothing else.

    A socket is a cloth pixel whose row and column both sit on the phase. Two sockets are NEIGHBOURS
    when the straight bar between them lies wholly on cloth - so what the plate is allowed to say is
    decided by the shape of the garment, and a bay of cloth too narrow to take a bar simply offers
    the painter nothing there."""
    py, px = phase // PITCH, phase % PITCH
    h, w = a.shape
    S = [(y, x) for y in range(h) for x in range(w)
         if a[y, x] and (y - py) % PITCH == 0 and (x - px) % PITCH == 0]
    ss = set(S)
    E = []
    for (y, x) in S:
        if (y, x + PITCH) in ss and all(a[y, xx] for xx in range(x, x + PITCH + 1)):
            E.append(((y, x), (y, x + PITCH)))
        if (y + PITCH, x) in ss and all(a[yy, x] for yy in range(y, y + PITCH + 1)):
            E.append(((y, x), (y + PITCH, x)))
    g = {v: [] for v in S}
    for u, v in E:
        g[u].append(v)
        g[v].append(u)
    return S, E, g


def bar_pixels(e):
    (y0, x0), (y1, x1) = e
    if y0 == y1:
        return [(y0, x) for x in range(min(x0, x1), max(x0, x1) + 1)]
    return [(y, x0) for y in range(min(y0, y1), max(y0, y1) + 1)]


# --- the arithmetic ------------------------------------------------------------------------------
def price_of(S, g, M):
    """THE CLASS, computed the way the reader computes it: the fewest clasps that must be broken
    before the plate can carry one more.

    An alternating walk out of a bare socket - unmatched edge, matched edge, unmatched edge, ... -
    that ends at another bare socket is an AUGMENTING PATH; breaking the k clasps on it and
    re-marrying along it leaves k+1. Berge's theorem: there is no such path exactly when the plate
    already carries the most clasps the garment can hold, which is what None means here and is why
    the warrior's identity is a fact and not a failure to search."""
    mate = {}
    for u, v in M:
        mate[u] = v
        mate[v] = u
    best = None
    for s in [v for v in S if v not in mate]:
        seen = {s: 0}
        q = [(s, 0)]
        while q and best is None:
            nq = []
            for u, k in q:
                for w in g[u]:
                    if w in seen:
                        continue
                    if w not in mate:
                        if best is None or k < best:
                            best = k
                        continue
                    m = mate[w]
                    if m in seen:
                        continue
                    seen[w] = k
                    seen[m] = k + 1
                    nq.append((m, k + 1))
            q = nq
        if best == 0:
            break
    return best


def augment_path(S, g, M):
    """The cheapest improvement there is, as a list of sockets - bare, then alternately unmatched
    and matched, then bare - or None if the plate already carries the most it can. This is the
    picture the class is ABOUT and the law will not let anybody paint; the evidence panel draws it
    over the plate that is forbidden to become it."""
    mate = {}
    for u, v in M:
        mate[u] = v
        mate[v] = u
    best = None
    for s in [v for v in S if v not in mate]:
        prev = {s: None}
        q = [(s, 0)]
        while q:
            nq = []
            for u, k in q:
                for w in g[u]:
                    if w in prev:
                        continue
                    if w not in mate:
                        if best is None or k < best[0]:
                            path, cur = [w], u
                            while cur is not None:
                                path.append(cur)
                                cur = prev[cur]
                            best = (k, list(reversed(path)))
                        continue
                    m = mate[w]
                    if m in prev:
                        continue
                    prev[w] = u
                    prev[m] = w
                    nq.append((m, k + 1))
            q = nq
            if best is not None:
                break
    return best[1] if best else None


def knife(S, E, M):
    """THE LAW, in two lines: no socket is married twice, and no pair the lattice offers is left
    entirely bare."""
    used = set()
    for u, v in M:
        if u in used or v in used:
            return False
        used.add(u)
        used.add(v)
    for u, v in E:
        if u not in used and v not in used:
            return False
    return True


def extend(M, E, rng):
    """Marry off whatever is still free, in a salted order. The result is always PINNED - which is
    the only way this axis has of drawing anything at all."""
    used = set()
    for u, v in M:
        used.add(u)
        used.add(v)
    for u, v in rng.shuffled(E):
        if u in used or v in used:
            continue
        used.add(u)
        used.add(v)
        M.append((u, v))
    return M


def shadowless(a, M):
    """How many clasps cast no shadow at all. RELIEF IS NOT DECORATION: a bar with nothing dark
    under it is a stripe of colour, and at thirteen pixels a colour is camouflage - the finding the
    legibility pass has made three times. The painter is told about it here rather than left to trip
    over clause LEGIBLE, because whether a clasp has anywhere to cast depends on the WHOLE pairing:
    the pixel down and left of one bar is often the next bar along."""
    h, w = a.shape
    core = {p for e in M for p in bar_pixels(e)}
    n = 0
    for e in M:
        if not any(0 <= y + 1 < h and 0 <= x - 1 < w and a[y + 1, x - 1]
                   and (y + 1, x - 1) not in core for y, x in bar_pixels(e)):
            n += 1
    return n


def cost_of(p, want, n=MINCLASP, dull=0):
    """Distance from what was asked for, in the order the clauses matter. A pairing with fewer than
    MINCLASP clasps is a mark and not a pattern, so the search is told about clause LIVE rather than
    left to trip over it, and the same for clause LEGIBLE."""
    c = 20 * max(0, MINCLASP - n) + dull
    if want is None:
        return c + (0 if p is None else 40 * (1 + p))
    return c + (40 * 99 if p is None else 40 * abs(p - want))


EXHAUST_EDGES = 20     # above this the enumeration is not worth its time and `--reach` says so
EXHAUST_BUDGET = 400000


def all_pinned(S, E, budget=EXHAUST_BUDGET):
    """EVERY PINNED PAIRING THIS LATTICE ADMITS, or None if there are too many to be worth listing.

    Each vertex in turn is either left bare or married to a LATER neighbour, so every pairing is
    reached exactly once; a pairing counts only if no edge has both ends bare, which is the law.
    On the small lattices - a boot, a sleeve, a hip - this turns `--reach` from a search that gave
    up into a statement about every picture that could have been painted there."""
    idx = {v: i for i, v in enumerate(S)}
    adj = {v: [] for v in S}
    for u, v in E:
        adj[u].append(v)
        adj[v].append(u)
    out = []
    nodes = [0]

    def rec(i, matched, M):
        if nodes[0] > budget:
            return False
        nodes[0] += 1
        if i == len(S):
            if all(u in matched or v in matched for u, v in E):
                out.append(list(M))
            return True
        v = S[i]
        if v in matched:
            return rec(i + 1, matched, M)
        if not rec(i + 1, matched, M):
            return False
        for w in adj[v]:
            if w in matched or idx[w] < i:
                continue
            if not rec(i + 1, matched | {v, w}, M + [(v, w)]):
                return False
        return True

    return out if rec(0, frozenset(), []) else None


def could_wear(a, S, E, g, want):
    """Could ANY pinned pairing on this lattice have worn this identity? PROVED where the
    enumeration is affordable, and honestly reported as unknown where it is not."""
    if len(E) > EXHAUST_EDGES:
        return None
    every = all_pinned(S, E)
    if every is None:
        return None
    for M in every:
        if len(M) < MINCLASP or len(S) < MINSOCK:
            continue
        if shadowless(a, M):
            continue
        if price_of(S, g, M) == want:
            return True
    return False


def find_pairing(a, S, E, g, want, rng, steps=STEPS):
    """A pinned pairing whose price is the one asked for, or None.

    The search walks the pinned pairings: force one clasp on, throw out whatever it collides with,
    marry off the rest. Every step lands on a lawful plate - the awkward thing is never legality but
    the PRICE, which is a global property and moves in jumps."""
    if len(E) < MINCLASP or len(S) < MINSOCK:
        return None
    M = extend([], E, rng)
    c = cost_of(price_of(S, g, M), want, len(M), shadowless(a, M))
    if c == 0:
        return M
    for _ in range(steps):
        e = E[rng.below(len(E))]
        N = [f for f in M if f[0] not in e and f[1] not in e]
        N.append(e)
        N = extend(N, E, rng)
        d = cost_of(price_of(S, g, N), want, len(N), shadowless(a, N))
        if d <= c:
            M, c = N, d
            if c == 0:
                return M
    return None


# --- the painter ---------------------------------------------------------------------------------
def compose(a, cls, mode=None, salt=''):
    """The clasps for one pose, as (phase, list of edges), or None if the pose cannot wear its
    class. Every control that is a lawful picture wrongly made is made HERE, from a lawful plate, so
    that a control differs from what ships in exactly one thing."""
    want = SWAP_PRICE[cls] if mode == 'swapped' else PRICE[cls]
    rng = Rng('%s|%s' % (salt, mode or 'ship'))

    if mode == 'dead':
        # A LATTICE TOO SMALL TO MEAN ANYTHING: a pair of sockets with a clasp on them is pinned,
        # and says nothing at all. Clause LIVE is what collects it.
        for phase in range(PITCH * PITCH):
            S, E, _g = lattice(a, phase)
            if E:
                return phase, [E[rng.below(len(E))]]
        return None

    keep = None
    for phase in rng.shuffled(range(PITCH * PITCH)):
        S, E, g = lattice(a, phase)
        for t in range(TRIES):
            r2 = Rng('%s|%s|%d|%d' % (salt, mode or 'ship', phase, t))
            M = find_pairing(a, S, E, g, want, r2)
            if M is None:
                continue
            if mode == 'random':
                # THE NULL HYPOTHESIS: the same number of clasps, on the same lattice, married with
                # no thought for what is left over.
                n = len(M)
                N, used = [], set()
                for u, v in r2.shuffled(E):
                    if len(N) >= n:
                        break
                    if u in used or v in used:
                        continue
                    used.add(u)
                    used.add(v)
                    N.append((u, v))
                M = N
            if not all(a[y, x] for e in M for y, x in bar_pixels(e)):
                continue
            keep = (phase, M)
            break
        if keep:
            break
    if keep is None:
        return None

    phase, M = keep
    S, E, g = lattice(a, phase)

    if mode == 'doubled':
        # ONE CLASP TOO MANY. There is no lawful place for it - that is the law - so this is the
        # ADD half of the squeeze, and it must trip clause KNIFE every time.
        free = [e for e in E if e not in M]
        if not free:
            return None
        M = M + [free[rng.below(len(free))]]
    elif mode == 'broken':
        # ONE CLASP TOO FEW: the REMOVE half of the squeeze. It leaves two bare sockets side by
        # side, and must trip the same clause.
        if len(M) < 2:
            return None
        i = rng.below(len(M))
        M = [e for j, e in enumerate(M) if j != i]
    elif mode == 'nudged':
        # ONE CLASP RE-MARRIED: still one clasp, still on the lattice, joined to a different
        # neighbour. Sometimes lawful and misnamed, sometimes not lawful at all.
        i = rng.below(len(M))
        u, v = M[i]
        alt = [e for e in E if (u in e) != (v in e) and e not in M]
        if not alt:
            return None
        M = [e for j, e in enumerate(M) if j != i] + [alt[rng.below(len(alt))]]

    return phase, M


def paint(a, keep, clip=None, shift=None):
    """The clasps and the shadows they cast, and nothing else. RELIEF, NOT COLOUR: at thirteen
    pixels a flat field of another hue is camouflage, and only a crest with its own shadow survives
    the finishing pass."""
    h, w = a.shape
    _phase, M = keep
    core = np.zeros(a.shape, bool)
    for i, e in enumerate(M):
        px = bar_pixels(e)
        if clip == i:
            px = px[:-1]                    # CLIPPED: a clasp drawn a pixel short
        if shift == i:
            px = [(y + 1, x) for y, x in px]  # OFFGRID: a clasp a pixel off the lattice
        for y, x in px:
            if 0 <= y < h and 0 <= x < w and a[y, x]:
                core[y, x] = True
    dark = np.zeros(a.shape, bool)
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            dark[ny, nx] = True
    return core, dark


# --- the reader ----------------------------------------------------------------------------------
def read_stops(fr, a):
    """Bar, shadow and field off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: three luminances
    on the piece - the brightest is a clasp, the darkest is a clasp's shadow, the rest is cloth."""
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


def read_bars(core):
    """Every clasp, from the pixels alone. The bright pixels are cut into four-connected pieces and
    each piece must be a straight run exactly BARLEN long. Two clasps sharing a socket would come
    back as ONE bent or over-long piece, so the reader sees the law being broken before it has done
    any arithmetic at all."""
    h, w = core.shape
    seen = np.zeros(core.shape, bool)
    bars, ok, merged = [], True, 0
    for (y0, x0) in np.argwhere(core):
        if seen[y0, x0]:
            continue
        stack, comp = [(y0, x0)], []
        seen[y0, x0] = True
        while stack:
            y, x = stack.pop()
            comp.append((y, x))
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and core[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    stack.append((ny, nx))
        ys = {p[0] for p in comp}
        xs = {p[1] for p in comp}
        if len(comp) > BARLEN:
            # TOO MUCH BRIGHT IN ONE PIECE. Two clasps that share a socket are drawn as one long or
            # one bent thing, so the ADD half of the squeeze is refused by the PICTURE before any
            # arithmetic is done - the plate simply stops being made of clasps.
            merged += 1
            continue
        if len(comp) != BARLEN or (len(ys) != 1 and len(xs) != 1):
            ok = False
            continue
        comp.sort()
        bars.append((comp[0], comp[-1]))
    return bars, ok, merged


def read_phase(bars):
    """The phase, from the clasps' own ends. Nine were open to the painter and the plate names the
    one it used by standing on it."""
    ph = {((y % PITCH) * PITCH + (x % PITCH)) for e in bars for (y, x) in e}
    if len(ph) != 1:
        return None
    return ph.pop()


def inspect_frame(fr, a, cls):
    """The six clauses on ONE POSE, from the pixels and the outline and nothing else."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, clasps=0, sockets=0, bare=0, price_val='-')
    core, dark, three = read_stops(fr, a)
    if not three or not core.any():
        v['silent'] = 1
        return v
    v['plates'] = 1

    bars, bar_ok, merged = read_bars(core)
    if merged:
        # Clasps that MEET. The law again, caught by the eye rather than by the arithmetic.
        v['knife'] = 1
        return v
    if not bar_ok or not bars:
        v['bar'] = 1
        return v

    # (2) BAR - the shadow is where it must be and nowhere else
    h, w = a.shape
    want = set()
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            want.add((int(ny), int(nx)))
    if {(int(y), int(x)) for y, x in np.argwhere(dark)} != want:
        v['bar'] = 1
        return v

    # (1) LATTICE - one phase, and every clasp is a pair the garment offers
    phase = read_phase(bars)
    if phase is None:
        v['lattice'] = 1
        return v
    S, E, g = lattice(a, phase)
    es = {tuple(sorted(e)) for e in E}
    M = [tuple(sorted(e)) for e in bars]
    if any(e not in es for e in M):
        v['lattice'] = 1
        return v
    v['sockets'] = len(S)
    v['clasps'] = len(M)

    # (5) LIVE - a lattice too small is pinned for the wrong reason
    if len(M) < MINCLASP or len(S) < MINSOCK:
        v['live'] = 1
        return v

    # (6) LEGIBLE - every clasp casts shadow, or it is a stripe of colour and not a raised thing
    for e in M:
        if not any(0 <= y + 1 < h and 0 <= x - 1 < w and a[y + 1, x - 1] and not core[y + 1, x - 1]
                   for y, x in bar_pixels(e)):
            v['legible'] = 1

    # (3) KNIFE - THE LAW
    if not knife(S, E, M):
        v['knife'] = 1
        return v
    married = {u for e in M for u in e}
    v['bare'] = len(S) - len(married)

    # (4) PRICE - the class
    p = price_of(S, g, M)
    v['price_val'] = '-' if p is None else p
    if p != PRICE[cls]:
        v['price'] = 1
    return v


# --- frames --------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, dark, keep) or None if the pose cannot wear its class."""
    shadow_c, field_c, bar_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE CLASPS GO ON. The source sheet's inherited highlights sit in
    # the same stop a clasp does, and a reader told nothing cannot tell an inherited highlight from
    # a clasp. Every tone here is put there by the pairing; the modelling comes back, richer, from
    # the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    keep = compose(a, cls, mode, salt)
    if keep is None:
        return None
    if mode == 'flat':
        return np.zeros(a.shape, bool), np.zeros(a.shape, bool), keep

    clip = shift = None
    if mode == 'clipped':
        clip = 0
    if mode == 'offgrid':
        _phase, M = keep
        for i, e in enumerate(M):
            if all(a[y + 1, x] for y, x in bar_pixels(e) if y + 1 < a.shape[0]) and \
                    all(y + 1 < a.shape[0] for y, x in bar_pixels(e)):
                shift = i
                break
        if shift is None:
            return None

    core, dark = paint(a, keep, clip=clip, shift=shift)
    if not core.any() or not dark.any():
        return None
    for y, x in np.argwhere(dark):
        put(fr, y, x, shadow_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, bar_c)
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
    """A SHEET IS CLASPED IN ALL ITS POSES OR IN NONE. A pairing that appears in some frames of a
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


def sheets():
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                yield kind, cfg, cls, suffix, '%s%s' % (cfg['srcs'][cls], suffix)


# --- the acceptance test -------------------------------------------------------------------------
def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, sheets=0, pass_sheets=0, clasps=0, bare=0)
    for kind, cfg, cls, suffix, stem in sheets():
        if only and kind != only:
            continue
        base = load_any('%s.png' % stem)
        plates = [(fi, a, one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi)))
                  for fi, sl, a in frames_of(base)]
        ok = all(p[2][1] is not None for p in plates)
        tot['sheets'] += 1
        if not ok:
            print('   %-7s %-8s %-2s  PLAIN (reported)' % (kind, cls, suffix or 'm'), flush=True)
            continue
        bad = dict.fromkeys(CLAUSES, 0)
        np_ = ns = nc = nb = 0
        socks = []
        prices = set()
        for fi, a, (fr, _g) in plates:
            res = inspect_frame(fr, a, cls)
            for c in CLAUSES:
                bad[c] += res[c]
            np_ += res['plates']
            ns += res['silent']
            nc += res['clasps']
            nb += res['bare']
            socks.append(res['sockets'])
            prices.add(res['price_val'])
        tot['plates'] += np_
        tot['silent'] += ns
        tot['clasps'] += nc
        tot['bare'] += nb
        for c in CLAUSES:
            tot[c] += bad[c]
        good = not any(bad.values())
        tot['pass_sheets'] += 1 if good else 0
        print('   %-7s %-8s %-2s  price=%-4s plates=%-3d clasps=%-4d bare=%-4d sockets %d-%-3d  %s%s'
              % (kind, cls, suffix or 'm',
                 'none' if PRICE[cls] is None else PRICE[cls], np_, nc, nb,
                 min(socks) if socks else 0, max(socks) if socks else 0,
                 'ALL PASS' if good else 'FAIL ',
                 '' if good else ' ' + ' '.join('%s=%d' % (c, k) for c, k in bad.items() if k)),
              flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d clasps drawn, %d sockets left bare, '
          '%d silent'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['clasps'], tot['bare'],
             tot['silent']))
    for c in CLAUSES:
        print('   %-9s %d violations' % (c.upper(), tot[c]))


# --- THE SQUEEZE ---------------------------------------------------------------------------------
def pinned_report():
    """THE ACCEPTANCE TEST THAT NO PREVIOUS AXIS COULD HAVE RUN.

    For every shipped plate: try every clasp the lattice would allow and is not drawn, and try
    taking off every clasp that is. The law must refuse all of both. A monotone law can only be
    tested one way - a Sidon set survives every deletion, a complete ruler survives every addition -
    so this table is the axis's whole claim in two columns."""
    print('== PINNED  (THE SQUEEZE: every clasp that could go on, every clasp that could come off)')
    ta = tb = ka = kb = 0
    for kind, cfg, cls, suffix, stem in sheets():
        base = load_any('%s.png' % stem)
        if not sheet_carries(base, cls, stem):
            continue
        adds = rems = adds_ok = rems_ok = 0
        for fi, sl, a in frames_of(base):
            keep = compose(a, cls, None, '%s|%d' % (stem, fi))
            if keep is None:
                continue
            phase, M = keep
            S, E, _g = lattice(a, phase)
            ms = {tuple(sorted(e)) for e in M}
            for e in E:
                if tuple(sorted(e)) in ms:
                    continue
                adds += 1
                if knife(S, E, list(ms) + [tuple(sorted(e))]):
                    adds_ok += 1
            for i in range(len(M)):
                rems += 1
                if knife(S, E, [e for j, e in enumerate(M) if j != i]):
                    rems_ok += 1
        ta += adds
        ka += adds_ok
        tb += rems
        kb += rems_ok
        print('   %-7s %-8s %-2s  additions tried %-4d still lawful %-3d   removals tried %-4d '
              'still lawful %-3d'
              % (kind, cls, suffix or 'm', adds, adds_ok, rems, rems_ok), flush=True)
    print('   ----')
    print('   %d additions tried, %d left a lawful plate' % (ta, ka))
    print('   %d removals  tried, %d left a lawful plate' % (tb, kb))
    print('   NOTHING CAN GO ON AND NOTHING CAN COME OFF. The 68th survives every deletion and the')
    print('   76th survives every addition; this is the first plate in the project that survives')
    print('   neither, and the two columns above are the whole of the claim.')


# --- the controls --------------------------------------------------------------------------------
def controls_report(which=None):
    print('== CONTROLS  (a plate is CLEAN only if it trips no clause at all)')
    for mode in (CONTROLS if which is None else (which,)):
        drawn = clean = silent = undrawable = 0
        bad = dict.fromkeys(CLAUSES, 0)
        for kind, cfg, cls, suffix, stem in sheets():
            if suffix:
                continue
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
            'dead': '  <- two sockets and one clasp: pinned, and it says nothing',
            'doubled': '  <- ONE CLASP ADDED. The ADD half - the SAME LAW, caught by the eye',
            'broken': '  <- ONE CLASP TAKEN OFF. The REMOVE half - the SAME LAW, caught by the arithmetic',
            'nudged': '  <- one clasp re-married to a different neighbour',
            'swapped': '  <- LAWFUL AND MISNAMED: the reader names the class the plate really is',
            'offgrid': '  <- one clasp a pixel off the lattice',
            'clipped': '  <- one clasp drawn a pixel short',
            'flat': '  <- no ornament at all: SILENT, never CLEAN',
        }.get(mode, '')
        print('   %-9s clean %4d / %-4d   silent %-4d  undrawable %-4d %s%s'
              % (mode.upper(), clean, drawn, silent, undrawable, note, extra), flush=True)


# --- reports -------------------------------------------------------------------------------------
def sweep():
    print('== SWEEP  (can every pose of every sheet carry its class)')
    for kind, cfg, cls, suffix, stem in sheets():
        base = load_any('%s.png' % stem)
        fit = unfit = 0
        nc = []
        for fi, sl, a in frames_of(base):
            keep = compose(a, cls, None, '%s|%d' % (stem, fi))
            if keep is None:
                unfit += 1
                continue
            fit += 1
            nc.append(len(keep[1]))
        print('   %-7s %-8s %-2s  price %-4s  clasps %d-%-3d   %2d/%-2d  %s'
              % (kind, cls, suffix or 'm', 'none' if PRICE[cls] is None else PRICE[cls],
                 min(nc) if nc else 0, max(nc) if nc else 0, fit, fit + unfit,
                 'clasped' if unfit == 0 else 'PLAIN (reported)'), flush=True)


def reach_report():
    """WHICH OF THE THREE IDENTITIES EACH GARMENT COULD EVER HAVE WORN, and what the best possible
    assignment of the three to the three classes would have shipped."""
    from itertools import permutations
    print('== REACH  (every phase of every pose, searched - and where the search fails, PROVED)')
    can = {}
    for kind, cfg, cls, suffix, stem in sheets():
        base = load_any('%s.png' % stem)
        row, hard = {}, {}
        for want in (1, 2, None):
            n = 0
            proved = unknown = 0
            for fi, sl, a in frames_of(base):
                got = False
                salt = '%s|%d' % (stem, fi)
                for phase in range(PITCH * PITCH):
                    S, E, g = lattice(a, phase)
                    for t in range(TRIES):
                        if find_pairing(a, S, E, g, want, Rng('%s|reach|%d|%d' % (salt, phase, t))):
                            got = True
                            break
                    if got:
                        break
                if got:
                    n += 1
                    continue
                # THE SEARCH GAVE UP. Now ask the lattice itself, phase by phase, by listing every
                # pinned pairing there is. Where that is affordable the answer is a theorem.
                verdict = False
                for phase in range(PITCH * PITCH):
                    S, E, g = lattice(a, phase)
                    v = could_wear(a, S, E, g, want)
                    if v is None:
                        verdict = None
                        break
                    if v:
                        verdict = True
                        break
                if verdict is True:
                    n += 1
                elif verdict is False:
                    proved += 1
                else:
                    unknown += 1
            row[want] = n
            hard[want] = (proved, unknown)
        tot = sum(1 for _ in frames_of(base))
        can[(kind, cls, suffix)] = {k: (v == tot) for k, v in row.items()}
        mine = PRICE[cls]
        p, u = hard[mine]
        print('   %-7s %-8s %-2s  poses %-2d   price1 %-2d  price2 %-2d  none %-2d   wears %-14s %s'
              % (kind, cls, suffix or 'm', tot, row[1], row[2], row[None],
                 ', '.join(str(k if k is not None else 'none') for k in (1, 2, None)
                           if row[k] == tot) or 'nothing',
                 'ok' if row[mine] == tot
                 else 'PROVED IMPOSSIBLE on %d pose(s)%s'
                      % (p, '' if not u else ', %d not enumerable' % u)), flush=True)
    print('   ----')
    print('   == COULD THE THREE IDENTITIES HAVE BEEN HANDED OUT BETTER?')
    best = None
    for p in permutations((1, 2, None)):
        asg = dict(zip(('mage', 'ranger', 'warrior'), p))
        n = sum(1 for (kind, cls, suffix), row in can.items() if row[asg[cls]])
        best = n if best is None or n > best else best
        print('      mage %-4s ranger %-4s warrior %-4s  ->  %2d/24 sheets clasped'
              % (asg['mage'], asg['ranger'], asg['warrior'], n))
    cur = sum(1 for (kind, cls, suffix), row in can.items() if row[PRICE[cls]])
    print('      ----')
    print('      SHIPPED %d/24, BEST POSSIBLE %d/24 - %s'
          % (cur, best,
             'the batch is at its ceiling and the missing sheets are the garments, not the '
             'assignment' if cur >= best else 'RETUNE'))


def frame_dump():
    print('== ONE REAL POSE PER CLASS  ("#" a clasp, "=" its shadow, "o" a bare socket, "-" cloth)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            salt = '%s|%d' % (stem, fi)
            keep = compose(a, cls, None, salt)
            if keep is None:
                continue
            phase, M = keep
            S, E, g = lattice(a, phase)
            core, dark = paint(a, keep)
            married = {u for e in M for u in e}
            bare = [s for s in S if s not in married]
            print('== %s chest frame %d   phase %d, %d sockets, %d clasps, %d bare, price %s'
                  % (cls, fi, phase, len(S), len(M), len(bare),
                     'NONE (already the most it can hold)' if price_of(S, g, M) is None
                     else price_of(S, g, M)))
            ys, xs = np.nonzero(a)
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not a[y, x]:
                        row += '.'
                    elif core[y, x]:
                        row += '#'
                    elif dark[y, x]:
                        row += '='
                    elif (y, x) in bare:
                        row += 'o'
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a clasp on
    the shadowed flank is darker in absolute terms than the cloth on the lit one."""
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
                              ((y + 1, x - 1), (y + 1, x), (y, x - 1), (y, x + 1))
                              if 0 <= ny < FH and 0 <= nx < FW and not core[ny, nx]
                              and (dark[ny, nx] or a[ny, nx])]
                        if not nb:
                            continue
                        tot += 1
                        if lum[y, x] > float(np.mean(nb)):
                            ok += 1
        print('   %-7s clasp still lighter than the cloth around it: %5d/%-5d (%3d%%)'
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
    if '--pinned' in sys.argv:
        pinned_report()
        return
    if '--sweep' in sys.argv:
        sweep()
        return
    if '--reach' in sys.argv:
        reach_report()
        return
    if '--survive' in sys.argv:
        os.makedirs('_tmp', exist_ok=True)
        survive()
        return
    for kind, cfg, cls, suffix, stem in sheets():
        os.makedirs(cfg['outdir'], exist_ok=True)
        base = load_any('%s.png' % stem)
        arr, ok = build(base, cls, stem)
        dst = '%s/%s%s.png' % (cfg['outdir'], cfg['dst'] % cls, suffix)
        # MANDATORY finishing pass - never a bespoke shade() in a generator.
        arr, info = finish_array(arr, dst)
        save_finished(arr, dst)
        print('wrote %-58s opaque_px=%-6d finish=%s/%s  %s'
              % (dst, int((arr[..., 3] > 0).sum()), info['slot'], info['variant'],
                 'price=%s' % ('none' if PRICE[cls] is None else PRICE[cls]) if ok
                 else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
