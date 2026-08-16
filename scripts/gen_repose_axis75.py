#!/usr/bin/env python3
"""SEVENTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS - the REPOSE family: the ornament is a
field of HEAPS, some of them heaped too high to stand, and the law is that HOWEVER THE READER LETS
THEM FALL, THE PLATE ALWAYS COMES TO REST AS THE SAME PICTURE.

    the ground is    a TERRACE   every cloth pixel of one phase of a 6x3 lattice is a pan, so the
                                 terrace belongs to the silhouette and not to the painter, who
                                 chooses only which of the eighteen phases
    the ornament is  a HEAP      a pan holding k grains is a bright COLUMN k pixels tall rising out
                                 of the pan, with one hard seat pixel down and left of its foot.
                                 AN EMPTY PAN CARRIES NO INK: any one heap fixes the phase and the
                                 outline supplies every other pan for nothing
    the move is      a COLLAPSE  a pan holding four or more spills FOUR grains, one into each of its
                                 four neighbours, and a grain that spills off the edge of the cloth
                                 IS GONE. Nothing is destroyed and nothing is added; the plate only
                                 rearranges itself and loses what falls off it
    the law is       EVERY ORDER OF COLLAPSE ENDS AT ONE PICTURE, AND IT IS THE SAME PICTURE

*** THIS IS THE FIRST INVARIANT THAT IS A PICTURE. ***
Seventy-four axes state a law that comes out as a NUMBER or as a YES: a count (67th), a ceiling
(68th), a multipole order (69th), a number of motions (70th), a game value (71st), a coalition size
(72nd), a precision (73rd), a pair of sums in GF(4) (74th). Every one of them is a lossy reading of
the plate - a hundred different plates share the 74th's value and the axis is content that they
should. HERE THE INVARIANT IS ANOTHER PLATE. It is the strongest invariant an artefact can have,
because every other invariant of the settled picture is a function of it, and the reader does not
compute it so much as ARRIVE at it. The plate is not a picture with a number attached. It is a
picture ON ITS WAY TO ANOTHER PICTURE, and the law is about the one it is going to.

*** IT IS THE EXACT COMPLEMENT OF THE 74th ATTRITION, AND THE TWO OF THEM CLOSE A DOOR. ***
    74th ATTRITION  DESTRUCTIVE moves in a free order   ONE NUMBER survives, everything else goes
    75th REPOSE     REDISTRIBUTIVE moves in a free order  NOTHING is lost - the whole picture survives
Both hand the reader the artefact and let it choose the history. The 74th's answer is that almost
all of the plate is disposable and a residue of four bits is not. This one's answer is that NONE of
it is disposable, because the destination remembers every grain that was ever on the plate. Between
them there is no third answer: either the orbit collapses onto a coarse invariant or it collapses
onto a point, and the 74th found the first and this finds the second.

*** THE ARTEFACT IS REQUIRED TO BE UNFINISHED. ***
Clause UNSTABLE refuses any plate that has nowhere left to fall - and control SETTLED, which ships
the plate's own destination, is refused by it. IT IS THE FIRST CONTROL IN SEVENTY-FIVE AXES THAT IS
REFUSED FOR BEING CORRECT. The 74th's clause LIVE asked the artefact to be DESTRUCTIBLE, which is a
capacity; this asks it to be INCOMPLETE, which is a debt. A plate that has already settled satisfies
the law for the wrong reason - it is its own destination and has nothing to prove - and this axis
will not ship it. THE ORNAMENT IS AN OBLIGATION THE PLATE HAS NOT YET DISCHARGED.

*** CLASS IDENTITY IS A DEPTH ON A PICTURE THE PLATE DOES NOT SHOW. ***
The class is the deepest heap standing when everything has finished falling:

    mage      1    it settles flat - one grain in the deepest pan and no more anywhere
    ranger    2
    warrior   3    the deepest a pan can hold and still stand, in the plate with most on it

Not a count, a ceiling, an order, a number of motions, a fraction of a move, a coalition size, a
precision or a number of obstructions: A DEPTH, and one measured somewhere else. NOTHING ON THE
SHIPPED PLATE STATES THE CLASS. The 71st's class could not be seen because it was a fraction of a
move; this one could be seen perfectly well, on a picture the batch does not contain and the reader
has to produce for itself. It is an OUTPUT twice over - the destination is computed, and the class
is then read off it with a maximum.

*** THE ACCEPTANCE TEST IS A NEW KIND: A SETTLEMENT. ***
The reader recovers the terrace and the heaps off the pixels, then lets the plate fall FIVE
independent times, choosing at each step at random which overfull pan to spill next, and compares
what it gets. Six clauses:

    (1) HEAP       every mark is a legal column: one pixel wide, unbroken, no taller than five,
                   standing in a pan, seated by exactly one dark pixel wherever there is cloth to
                   seat it - and no ink anywhere that is not a column or a seat.
    (2) TERRACE    every column foot agrees on one phase of the lattice, so the pans are that
                   phase's cloth pixels and nothing else. THE TERRACE IS THE SILHOUETTE'S. Control
                   SHIFTED puts one column a pixel off the lattice and is caught here.
    (3) UNSTABLE   some pan holds four or more. THE ARTEFACT MUST BE UNFINISHED.
    (4) CONFLUENT  five independent collapse orders end at the identical settled picture AND at the
                   identical tally of spills per pan. THE LAW, MEASURED RATHER THAN ASSUMED, on
                   every pose of every sheet in the wardrobe.
    (5) CLASS      the deepest heap of the settled picture is the class's.
    (6) SATURATED  no grain can be added to any pan without moving the destination. THE ORNAMENT IS
                   MAXIMAL: the painter did not choose how full the plate is, it added grains until
                   one more would have changed where the plate comes to rest, and stopped.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_repose_axis75.py                    # write the four staged preview dirs
    python3 scripts/gen_repose_axis75.py --sweep            # can every pose carry a terrace
    python3 scripts/gen_repose_axis75.py --accept           # six clauses, every pose, every sheet
    python3 scripts/gen_repose_axis75.py --controls         # the nine controls
    python3 scripts/gen_repose_axis75.py --frame            # one real component per class
    python3 scripts/gen_repose_axis75.py --survive          # relief through the finishing pass
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

# THE PITCH IS ANISOTROPIC AND HALF-DROPPED, AND THAT IS THE WHOLE OF THE GEOMETRY. A heap is a
# COLUMN, so the pans have to be far enough apart VERTICALLY that the tallest legal column cannot
# reach the pan above it (five apart, columns at most four) and close enough HORIZONTALLY that a
# register of them reads as a register (three apart, one clear pixel between a column and its
# neighbour's seat). THE HALF-DROP IS NOT DECORATION AND IT IS NOT FREE - it is what keeps this
# axis out of the 11th FLUTING and the 43rd GADROON. Ranked one above another on a square lattice,
# four-pixel columns line up into continuous vertical reeds and the plate reads as fluted metal,
# which is a family this project has already shipped twice. Dropped one pixel per register they
# interleave, every column is bounded above by the SEAT of the heap up and right of it, and the eye
# stops joining them: what it sees is a scatter of heaps of visibly different heights, which is the
# one thing a field of identical studs (13th, 68th, 74th) can never show.
PY, PX, OFFS = 5, 3, 1
KMAX = PY - 1        # the tallest column that still leaves a clear row under the pan above it
THRESH = 4           # a pan spills when it holds four - one grain for each lattice direction
MIN_SITES = 5        # a terrace smaller than this has no collapse in it
TRIES = 10           # salted attempts before a pose is reported unplayable
CLIMB = 40           # hill-climb steps per attempt
FILL = 160           # settle-budget for the saturation pass
MAX_SPILL = 6000
ORDERS = 5           # independent collapse orders per plate in clause CONFLUENT

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

# THE CLASS IS THE DEEPEST HEAP OF THE SETTLED PICTURE.
DEPTH = {'mage': 1, 'ranger': 2, 'warrior': 3}
SWAP_DEPTH = {'mage': 2, 'ranger': 3, 'warrior': 1}

# Three stops per class, strictly increasing in luminance - (seat, field, column). None near black:
# a near-black darkest stop eats the visor's eye and mouth pixels (the 49th's lesson). Deliberately
# unrelated to the 71st (oxblood/moss/violet), 72nd (indigo/moonwhite, umber/wheat, jade/seafoam),
# 73rd (graphite/signal orange, mulberry/linen, aubergine/citron) and 74th (slate-teal/bone,
# peat/oxide red, night blue/silver-lilac):
#   warrior  IRON AND MARIGOLD
#   ranger   BOG GREEN AND CHALK
#   mage     DEEP PLUM AND MOONSTONE
PAL = {
    'warrior': ((38, 36, 34), (98, 92, 84), (246, 196, 96)),
    'ranger':  ((26, 38, 30), (74, 100, 78), (228, 234, 216)),
    'mage':    ((44, 28, 52), (108, 72, 124), (226, 214, 246)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_repose_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary75',
    ),
    'legs': dict(
        outdir='_repose_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary75',
    ),
    'boots': dict(
        outdir='_repose_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_repose',
    ),
    'helmet': dict(
        outdir='_reposedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary75',
    ),
}

CONTROLS = ('order', 'toppled', 'settled', 'random', 'shifted', 'clipped', 'seatless',
            'crowded', 'flat')
CLAUSES = ('heap', 'terrace', 'unstable', 'confluent', 'class', 'saturated')


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
    identically, and male and female of an item settle the same way."""

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


# --- the terrace -------------------------------------------------------------------------------
def pans_of(a, oy, ox, py=None, px=None):
    """THE TERRACE IS THE SILHOUETTE'S. Every cloth pixel of one phase is a pan, and the painter
    never chooses which pans exist - only which of the eighteen phases it works on. The reader takes
    the phase off the first column foot it meets and then asks the OUTLINE for every other pan, so
    the empty pans need no ink at all."""
    py = PY if py is None else py
    px = PX if px is None else px
    h_, w_ = a.shape
    pix = {}
    for y in range(oy, h_, py):
        for x in range(ox, w_, px):
            if a[y, x]:
                pix[((x - ox) // px, (y - oy) // py)] = (y, x)
    return pix


def caps_of(a, pix, kmax=None):
    """How tall a column a pan can carry: the run of cloth straight up out of it, capped at KMAX.
    A pan under a shoulder edge can hold one grain and draw it; a pan in the middle of a cuirass can
    draw five. THE CAP IS THE GARMENT'S, NOT THE PAINTER'S."""
    kmax = KMAX if kmax is None else kmax
    caps = {}
    for s, (y, x) in pix.items():
        c = 0
        while c < kmax and y - c >= 0 and a[y - c, x]:
            c += 1
        caps[s] = c
    return caps


def degrees(pix):
    return {s: sum(1 for d in DIRS if (s[0] + d[0], s[1] + d[1]) in pix) for s in pix}


def settle(h0, pix, rng=None):
    """LET IT FALL. A pan holding four or more spills four grains, one into each lattice direction;
    a grain aimed at a direction with no pan in it falls off the plate and is gone. Which overfull
    pan spills next is chosen AT RANDOM when a stream is supplied, and that is the whole point:
    clause CONFLUENT runs this five times with five different streams and demands the same picture
    every time. Returns (settled heights, spills per pan, grains lost, total spills)."""
    h = dict(h0)
    fires = {s: 0 for s in h}
    lost = 0
    total = 0
    un = [s for s in h if h[s] >= THRESH]
    while un:
        i = rng.below(len(un)) if rng is not None else len(un) - 1
        s = un.pop(i)
        if h[s] < THRESH:
            continue
        h[s] -= THRESH
        fires[s] += 1
        total += 1
        if total > MAX_SPILL:
            return None
        for d in DIRS:
            n = (s[0] + d[0], s[1] + d[1])
            if n in h:
                h[n] += 1
                if h[n] >= THRESH:
                    un.append(n)
            else:
                lost += 1
        if h[s] >= THRESH:
            un.append(s)
    return h, fires, lost, total


def depth_of(h, pix, rng=None):
    got = settle(h, pix, rng)
    if got is None:
        return None, None
    fin = got[0]
    return (max(fin.values()) if fin else 0), fin


def seed_heaps(pix, caps, deg, want, salt):
    """FIND A PLATE WHOSE DESTINATION HAS THE CLASS'S DEPTH, THEN FILL IT UNTIL IT CANNOT TAKE
    ANOTHER GRAIN.

    Two phases, and the second is the interesting one. The first walks a hill-climb: start from a
    single overfull pan, and add a grain when the destination is too shallow or take one off the
    tallest heap when it is too deep. The second is clause SATURATED made rather than checked - go
    round every pan in turn and pour grains into it for as long as the destination does not move.
    THE DENSITY OF THIS AXIS IS NOT A TUNED CONSTANT. There is no DENSITY in this file, because the
    painter is not allowed an opinion about how full the plate is: it is as full as the law lets it
    be, and where it stops is a fact about the garment."""
    order = sorted(pix, key=lambda s: (-deg[s], -caps[s], s))
    inner = order[:max(4, len(order) // 2)]
    for t in range(TRIES):
        rng = Rng('%s|%d' % (salt, t))
        h = {s: 0 for s in pix}
        hot = order[rng.below(min(len(order), 6))]
        if caps[hot] < THRESH:
            continue
        h[hot] = THRESH
        ok = False
        for _ in range(CLIMB):
            m, _fin = depth_of(h, pix)
            if m is None:
                break
            if m == want and any(v >= THRESH for v in h.values()):
                ok = True
                break
            if m < want:
                cands = [s for s in inner if h[s] < caps[s]] or \
                        [s for s in order if h[s] < caps[s]]
                if not cands:
                    break
                h[cands[rng.below(len(cands))]] += 1
            else:
                cands = [s for s in order if h[s] > 0]
                if not cands:
                    break
                mx = max(h[s] for s in cands)
                tall = [s for s in cands if h[s] == mx]
                h[tall[rng.below(len(tall))]] -= 1
                if not any(v >= THRESH for v in h.values()):
                    break
        if not ok:
            continue
        # --- clause SATURATED, made. Pour into every pan until one more grain would move the
        # destination. The plate that ships is the last one that still goes where it was going.
        budget = FILL
        for s in order:
            while h[s] < caps[s] and budget > 0:
                h[s] += 1
                budget -= 1
                m, _fin = depth_of(h, pix)
                if m != want:
                    h[s] -= 1
                    break
        return h
    return None


def saturated(h, pix, caps, want):
    """Clause SATURATED, checked: every pan with room in it would move the destination."""
    for s in pix:
        if h.get(s, 0) >= caps[s]:
            continue
        g = dict(h)
        g[s] = g.get(s, 0) + 1
        m, _fin = depth_of(g, pix)
        if m == want:
            return False, s
    return True, None


# --- composition -------------------------------------------------------------------------------
def phases(a, py=None, px=None):
    """The eighteen phases, roomiest first. On a sabaton or a hood the roomiest phase is often the
    one whose pans are all on the boundary, so the search tries them in turn rather than trusting
    the first."""
    py = PY if py is None else py
    px = PX if px is None else px
    out = []
    for oy in range(py):
        for ox in range(px):
            pix = pans_of(a, oy, ox, py, px)
            if len(pix) >= MIN_SITES:
                out.append((oy, ox, pix))
    out.sort(key=lambda t: -len(t[2]))
    return out


def compose(a, cls, mode=None, salt=''):
    """Returns (oy, ox, pix, caps, heights) or None if this pose has no collapse in it."""
    want = DEPTH[cls]
    if mode == 'swapped':
        want = SWAP_DEPTH[cls]
    py, px = (3, 3) if mode == 'crowded' else (PY, PX)
    kmax = KMAX if mode != "crowded" else 2
    for oy, ox, pix in phases(a, py, px):
        caps = caps_of(a, pix, kmax)
        deg = degrees(pix)
        if not any(caps[s] >= THRESH for s in pix):
            continue
        if mode == 'random':
            rng = Rng('rnd|%s' % salt)
            h = {s: rng.below(caps[s] + 1) for s in pix}
            if not any(h[s] >= THRESH for s in h):
                hot = max(pix, key=lambda s: caps[s])
                h[hot] = caps[hot]
            return oy, ox, pix, caps, h
        h = seed_heaps(pix, caps, deg, want, '%s|%d|%d' % (salt, oy, ox))
        if h is None:
            continue
        if mode == 'settled':
            got = settle(h, pix)
            if got is not None:
                h = {s: min(v, caps[s]) for s, v in got[0].items()}
        elif mode == 'toppled':
            un = [s for s in h if h[s] >= THRESH]
            if un:
                s = sorted(un)[0]
                g = dict(h)
                g[s] -= THRESH
                for d in DIRS:
                    n = (s[0] + d[0], s[1] + d[1])
                    if n in g:
                        g[n] += 1
                if all(g[q] <= caps[q] for q in g):
                    h = g
        elif mode == 'clipped':
            tall = [s for s in h if h[s] >= 2]
            if tall:
                h = dict(h)
                h[sorted(tall)[0]] -= 1
        return oy, ox, pix, caps, h
    return None


def paint(a, pix, h, shifted=False, seatless=False):
    """A COLUMN AND THE SEAT IT STANDS ON, AND NOTHING ELSE. Relief, not colour: at thirteen pixels a
    flat field of another hue is camouflage, and only a crest with its own shadow survives the
    finishing pass (the 13px legibility pass). A heap reads raised because it is a bright stack with
    one hard dark pixel down and left of its foot - the same direction the light has come from in
    every axis of this project - and because the stacks are of visibly different heights, which is
    the one thing a field of identical studs can never do."""
    core = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    hh, ww = a.shape
    off = None
    if shifted:
        for s in sorted(h):
            if h[s] > 0:
                y, x = pix[s]
                if x + 1 < ww and a[y, x + 1]:
                    off = (s, (y, x + 1))
                    break
    for s, k in h.items():
        if k <= 0:
            continue
        y, x = pix[s]
        if off is not None and off[0] == s:
            y, x = off[1]
        for i in range(k):
            if 0 <= y - i < hh and a[y - i, x]:
                core[y - i, x] = True
    for s, k in h.items():
        if k <= 0:
            continue
        y, x = pix[s]
        if off is not None and off[0] == s:
            y, x = off[1]
        ny, nx = y + 1, x - 1
        if not seatless and 0 <= ny < hh and 0 <= nx < ww and a[ny, nx] and not core[ny, nx]:
            dark[ny, nx] = True
    return core, dark


# --- the reader --------------------------------------------------------------------------------
def read_stops(fr, a):
    """Column, seat and field off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: three luminances
    on the piece - the brightest is a column, the darkest is a seat, and what is left is plain
    cloth. A plate showing fewer than three has nothing on it to read."""
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


def read_runs(core):
    """Every bright mark, resolved into columns. A run is a maximal unbroken vertical stack in one
    pixel column; its FOOT is its lowest pixel and its DEPTH is its length."""
    runs = []
    cols = {}
    for y, x in np.argwhere(core):
        cols.setdefault(int(x), set()).add(int(y))
    for x, S in cols.items():
        for y in sorted(S):
            if y + 1 not in S:
                k = 1
                while y - k in S:
                    k += 1
                runs.append((y, x, k))
    return runs


def read_terrace(a, core):
    """THE TERRACE, RECOVERED FROM THE COLUMN FEET AND THE OUTLINE, AND FROM NOTHING ELSE. Any one
    foot fixes the phase; every other foot must agree with it; and the pans are then every remaining
    cloth pixel of that phase, which the silhouette draws for free. Clause TERRACE is this function
    returning something."""
    runs = read_runs(core)
    if not runs:
        return None
    oy, ox = runs[0][0] % PY, runs[0][1] % PX
    if any(y % PY != oy or x % PX != ox for y, x, _k in runs):
        return None
    pix = pans_of(a, oy, ox)
    h = {s: 0 for s in pix}
    for y, x, k in runs:
        s = ((x - ox) // PX, (y - oy) // PY)
        if s not in pix:
            return None
        h[s] = k
    return oy, ox, pix, h, runs


def blots(crest):
    blk = crest[:-1, :-1] & crest[1:, :-1] & crest[:-1, 1:] & crest[1:, 1:]
    return bool(blk.any())


# --- frames ------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, dark, pix, caps, h) or None if the pose has no collapse."""
    seat_c, field_c, col_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE TERRACE GOES ON. The source sheet's inherited highlights sit
    # in the same stop a column does, and a reader told nothing cannot tell an inherited highlight
    # from a grain. Every tone on this plate is put there by the terrace; the modelling comes back,
    # richer, from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    got = compose(a, cls, mode, salt)
    if got is None:
        return None
    oy, ox, pix, caps, h = got
    if mode == 'flat':
        return (np.zeros(a.shape, bool), np.zeros(a.shape, bool), pix, caps, h)
    core, dark = paint(a, pix, h, shifted=(mode == 'shifted'), seatless=(mode == 'seatless'))
    for y, x in np.argwhere(dark):
        put(fr, y, x, seat_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, col_c)
    return core, dark, pix, caps, h


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
    """A SHEET IS HEAPED IN ALL FORTY-TWO POSES OR IN NONE. A terrace that appears in some frames of
    a walk and not others reads as a bug, not as a hard case."""
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
def inspect_frame(fr, a, cls, salt=''):
    """The six clauses on ONE POSE, from the pixels alone."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, grains=0, spills=0, lost=0, depth=None, pans=0)
    core, dark, three = read_stops(fr, a)
    if not three or not core.any():
        v['silent'] = 1
        return v
    v['plates'] = 1

    # (1) HEAP - the drawing discipline
    if bool((core[:, :-1] & core[:, 1:]).any()) or blots(core):
        v['heap'] += 1
    runs = read_runs(core)
    if any(k > KMAX for _y, _x, k in runs):
        v['heap'] += 1

    got = read_terrace(a, core)
    if got is None:
        v['terrace'] += 1
        v['heap'] += 1
        return v
    _oy, _ox, pix, h, runs = got
    v['pans'] = len(pix)
    v['grains'] = sum(h.values())

    # (1) HEAP, continued - every seat is a seat and every seat that is owed is paid
    want_dark = set()
    hh, ww = a.shape
    for y, x, _k in runs:
        ny, nx = y + 1, x - 1
        if 0 <= ny < hh and 0 <= nx < ww and a[ny, nx] and not core[ny, nx]:
            want_dark.add((ny, nx))
    have_dark = {(int(y), int(x)) for y, x in np.argwhere(dark)}
    if have_dark != want_dark:
        v['heap'] += 1

    # (3) UNSTABLE - the artefact must be unfinished
    if not any(k >= THRESH for k in h.values()):
        v['unstable'] += 1

    # (4) CONFLUENT - five independent orders, one destination
    ref = None
    for r in range(ORDERS):
        out = settle(h, pix, Rng('%s|order|%d' % (salt, r)))
        if out is None:
            v['confluent'] += 1
            return v
        fin, fires, lost, total = out
        key = (tuple(sorted(fin.items())), tuple(sorted(fires.items())))
        if ref is None:
            ref = key
            v['spills'], v['lost'] = total, lost
        elif key != ref:
            v['confluent'] += 1
    fin = dict(ref[0])
    v['depth'] = max(fin.values()) if fin else 0

    # (5) CLASS
    if v['depth'] != DEPTH[cls]:
        v['class'] += 1

    # (6) SATURATED
    caps = caps_of(a, pix)
    sat, _s = saturated(h, pix, caps, DEPTH[cls])
    if not sat:
        v['saturated'] += 1
    return v


def accept(only=None):
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, grains=0, spills=0, lost=0, sheets=0, clean=0, pans=0)
    print('%-46s %-7s %s' % ('sheet', 'poses', 'clauses tripped (of six)'))
    print('-' * 104)
    for kind, cfg in SLOTS.items():
        if only and only != kind:
            continue
        for cls, stem0 in cfg['srcs'].items():
            for suffix in ('', '_f'):
                stem = '%s%s' % (stem0, suffix)
                base = load_any('%s.png' % stem)
                s = dict.fromkeys(CLAUSES, 0)
                s.update(plates=0, silent=0, grains=0, spills=0, lost=0, pans=0)
                for fi, sl, a in frames_of(base):
                    salt = '%s|%d' % (stem, fi)
                    fr, got = one_plate(base, sl, a, cls, None, salt)
                    if got is None:
                        s['silent'] += 1
                        continue
                    v = inspect_frame(fr, a, cls, salt)
                    for k in v:
                        if k == 'depth':
                            continue
                        s[k] = s.get(k, 0) + (v[k] or 0)
                tot['sheets'] += 1
                bad = sum(s[c] for c in CLAUSES)
                if bad == 0 and s['plates'] > 0:
                    tot['clean'] += 1
                for k in s:
                    tot[k] = tot.get(k, 0) + s[k]
                flag = 'ALL PASS' if bad == 0 and s['plates'] else \
                    ' '.join('%s=%d' % (c, s[c]) for c in CLAUSES if s[c])
                print('%-46s %-7s %s%s' % ('%s/%s%s' % (kind, cls, suffix),
                                           '%d/42' % s['plates'], flag,
                                           '' if not s['silent'] else '  silent=%d' % s['silent']))
    print('-' * 104)
    print('sheets ALL PASS  %d/%d' % (tot['clean'], tot['sheets']))
    print('plates read      %d   pans %d   grains %d   spills %d   grains lost off the plate %d'
          % (tot['plates'], tot['pans'], tot['grains'], tot['spills'], tot['lost']))
    print('clause totals    ' + '  '.join('%s=%d' % (c, tot[c]) for c in CLAUSES))
    print('silent plates    %d' % tot['silent'])


def controls_report(which=None):
    print('%-10s %-9s %s' % ('control', 'clean', 'what it is'))
    print('-' * 100)
    WHAT = {
        'order': 'the same plate let fall in a different random order - MEANT TO PASS, the law run '
                 'as a control',
        'toppled': 'the plate advanced by one legal collapse - a DIFFERENT PICTURE and the SAME '
                   'destination',
        'settled': "the plate's own destination shipped in its place - refused for being FINISHED",
        'random': 'heaps poured without regard to where the plate would come to rest',
        'shifted': 'one column stood a pixel off the lattice',
        'clipped': 'one column a pixel shorter than the grains it stands for',
        'seatless': 'the seats taken away, columns left floating',
        'crowded': 'the terrace at a three-pixel vertical pitch, so the columns fuse',
        'flat': 'no ornament at all',
    }
    for mode in CONTROLS:
        if which and which != mode:
            continue
        good = seen = 0
        for kind, cfg in SLOTS.items():
            for cls, stem0 in cfg['srcs'].items():
                base = load_any('%s.png' % stem0)
                for fi, sl, a in frames_of(base):
                    salt = '%s|%d' % (stem0, fi)
                    use = None if mode == 'order' else mode
                    fr, got = one_plate(base, sl, a, cls, use, salt)
                    if got is None:
                        continue
                    seen += 1
                    v = inspect_frame(fr, a, cls,
                                      salt + ('|alt' if mode == 'order' else ''))
                    if v['silent']:
                        continue
                    trip = sum(v[c] for c in CLAUSES)
                    if mode == 'toppled':
                        trip -= v['saturated']   # saturation is where the painter stopped, not law
                    if trip == 0:
                        good += 1
        print('%-10s %-9s %s' % (mode.upper(), '%d/%d' % (good, seen), WHAT[mode]))
    print('-' * 100)
    print('ORDER and TOPPLED are meant to pass. TOPPLED is scored on the five clauses the law is')
    print('about: it fails SATURATED by construction, because saturation records where the painter')
    print('stopped and a plate that has already spilled once is not where the painter stopped.')


def sweep():
    print('%-46s %s' % ('sheet', 'poses that can carry a terrace'))
    print('-' * 90)
    for kind, cfg in SLOTS.items():
        for cls, stem0 in cfg['srcs'].items():
            for suffix in ('', '_f'):
                stem = '%s%s' % (stem0, suffix)
                base = load_any('%s.png' % stem)
                n = ok = 0
                for fi, sl, a in frames_of(base):
                    n += 1
                    _fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                    if got is not None:
                        ok += 1
                print('%-46s %d/%d%s' % ('%s/%s%s' % (kind, cls, suffix), ok, n,
                                         '   ALL' if ok == n else ''))


def frame_dump():
    os.makedirs('_tmp', exist_ok=True)
    for cls in ('warrior', 'mage', 'ranger'):
        stem = SLOTS['chest']['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            if fi:
                continue
            fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
            if got is None:
                print('%-8s no terrace' % cls)
                continue
            core, dark, pix, caps, h = got
            fin = settle(h, pix)[0]
            print('%-8s pans=%-4d grains=%-4d tallest heap=%d  settles to depth %d (class %d)'
                  % (cls, len(pix), sum(h.values()), max(h.values()),
                     max(fin.values()), DEPTH[cls]))
            Image.fromarray(fr).resize((FW * 8, FH * 8), Image.NEAREST).save(
                '_tmp/repose_%s.png' % cls)


def survive():
    """Does the relief survive the finishing pass? A column pixel must still be brighter than the
    seat under its foot after finish_array has had it."""
    for cls in ('warrior', 'mage', 'ranger'):
        stem = SLOTS['chest']['srcs'][cls]
        base = load_any('%s.png' % stem)
        arr, ok = build(base, cls, stem)
        before = arr.copy()
        dst = '_tmp/_survive_%s.png' % cls
        arr, _info = finish_array(arr, dst)
        kept = tot = 0
        for fi, sl, a in frames_of(base):
            c0, d0, three = read_stops(before[sl], a)
            if not three:
                continue
            lum = arr[sl][..., :3].astype(np.int32).sum(-1)
            for y, x in np.argwhere(c0):
                ny, nx = y + 1, x - 1
                if 0 <= ny < FH and 0 <= nx < FW and d0[ny, nx]:
                    tot += 1
                    if lum[y, x] > lum[ny, nx]:
                        kept += 1
        print('%-8s relief kept through the finishing pass: %d/%d  (%.0f%%)%s'
              % (cls, kept, tot, 100.0 * kept / max(tot, 1), '' if ok else '  [PLAIN]'))


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
                         'depth=%d' % DEPTH[cls] if ok else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
