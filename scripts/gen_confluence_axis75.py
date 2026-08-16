#!/usr/bin/env python3
"""SEVENTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS - the CONFLUENCE family: the ornament is a
set of LOADED PILES, and the law is that THE PICTURE THEY BECOME IS THE SAME PICTURE WHOEVER RUNS
THEM - and that picture is nowhere on the plate.

    the ground is    a BOARD      every cloth pixel of one lattice is a socket. The painter picks
                                  one of the nine lattices; it does not get to say which, because
                                  THE PLATE IS ITS OWN DECODER - exactly one lattice makes the
                                  picture parse at all, and the reader finds it by trying all nine.
    the ornament is  a PILE       a socket holding 1, 2 or 3 chips, drawn as a bright cluster that
                                  grows in a FIXED ORDER - centre, then right, then down - so a stud
                                  is one chip, a dash is two and an L is three, and the count reads
                                  straight off the pixels. Each chip casts a hard shadow one down
                                  and one left. Empty sockets carry no ink: the outline draws them.
                                  A pile of one is settled and a pile of two or three is loaded, so
                                  THE READER CAN SEE AT A GLANCE WHICH SOCKETS ARE ABOUT TO GO OFF.
    the move is      a TOPPLE     a socket holding two or more gives one chip to the socket on its
                                  right and one to the socket below it, and keeps the rest. Chips
                                  aimed off the cloth are gone.
    the law is       EVERY SCHEDULE HALTS, AND EVERY SCHEDULE ENDS AT THE SAME PICTURE AND THE SAME
                     TALLY OF TOPPLES - a plate cannot choose its own destination

*** THIS IS THE FIRST INVARIANT THAT IS A UNIQUENESS OF OUTCOME RATHER THAN A CONSTANCY. ***
Seventy-four axes name something that DOES NOT MOVE. The 74th ATTRITION is the extreme case of it:
wreck the ornament however you like and a number is still standing. This one names something that
MOVES, and says the reader has no say in where it moves TO. The two are exact complements and they
are the only two things a reader who is allowed to act on an artefact can be told:

    74th ATTRITION   an INVARIANCE     do what you like: this number will not change
    75th CONFLUENCE  a CONFLUENCE      do what you like: you will end up in the same place

*** IT IS THE FIRST LAW WHOSE SUBJECT IS A PICTURE THAT WAS NEVER PAINTED. ***
The plate ships a loaded, unstable arrangement. The arrangement the law is about is the one it
settles into, and that one is not on the plate, is not in the file, and was drawn by nobody. The
69th ANNEAL came nearest and from the other side - there the interior was the part nobody AUTHORED,
but it was still the part you could see. Here the subject of the law is invisible until a reader
does the work, and then every reader has the same one.

*** THE HALT IS PROVED, NOT BUDGETED. ***
Give every chip a weight equal to how far it still has to travel - the columns to its right plus the
rows below it, plus two. A topple takes two chips of weight w off a socket and puts back one of
weight w-1 to the right and one of weight w-1 below, so the total weight falls by exactly two every
single time, and it cannot fall below zero. Clause HALT therefore carries a bound THE PLATE COMPUTES
ABOUT ITSELF rather than a constant somebody chose: the first termination argument in the project,
and the reason this axis has no MAX_ITERS anywhere in it.

*** CLASS IDENTITY IS A DEPTH - THE GREATEST NUMBER OF TIMES ANY ONE SOCKET HAS TO TOPPLE. ***
    mage      1   one socket goes off, once, and the plate is quiet
    ranger    2   somewhere on the plate a socket goes off, is fed by its neighbours, and goes again
    warrior   3   and is fed, and goes again

Not a count (67th), a ceiling (68th), a multipole order (69th), a number of motions (70th), a
fraction of a move (71st), a coalition size (72nd), a precision (73rd) or a number of obstructions
(74th). Every one of those is a number of THINGS. THIS IS THE FIRST CLASS IDENTITY THAT IS A NUMBER
OF TIMES. It is an output - run the plate and look at the busiest socket - and it is well defined
only because the tally of topples is itself order-independent, which is the strong half of the law
and which clause CONFLUENCE measures directly rather than taking on trust.

*** THE PAIR OF CONTROLS THAT INVERT THE 74th, AND WHAT THEY TURNED UP. ***
Control TOPPLED ships a plate advanced by ONE LEGAL MOVE, chosen at random. In the 74th the same
control was the only one in the project MEANT to pass, and nothing could break its number. Here it
passes 301 times in 377 - and the 76 failures are the interesting half, because they say the class
is not a property of the whole avalanche after all:

    the DESTINATION is untouched by the move   377/377   THE LAW, and no move can reach it
    the CLASS is untouched by the move         301/377   and the other 76 are all the same move

A topple only shortens the journey of THE SOCKET IT HAPPENS AT, so the only move that can spend the
class is a topple at the socket that is carrying it. Control SPENT looks for exactly that move and
takes it: 0/377 clean, every failure on DEPTH.

`--controls toppled-why` enumerates EVERY legal move of EVERY shipped plate rather than sampling
one, and the two numbers are worth the whole axis:

    1299 legal moves, and 1299 of them leave the destination exactly where it was    (100%)
     221 of them spend the class, spread over 221 different plates                   (17%)

*** WHERE A PLATE HAS A WEAK POINT IT HAS EXACTLY ONE. *** Two hundred and twenty-one plates have a
single stud that is the difference between a warrior and a ranger, a hundred and fifty-six have none
at all, and no plate in the wardrobe has two. Nothing in the 74th had a weak point of any kind: that
is what an invariance buys, and what a confluence does not.

THE ACCEPTANCE TEST IS A RACE. The reader stabilises the same plate under six deliberately hostile
schedules - lowest socket first, highest first, fullest first, and three different random orders -
and demands that all six agree pixel for pixel AND socket for socket. Six clauses:

    (1) BOARD       exactly one of the nine lattices parses the picture. Every bright pixel belongs
                    to exactly one pile, and the painter is not allowed to say which lattice it
                    used. Control OFFGRID puts one chip where no pile can own it.
    (2) PILE        every pile is a PREFIX of centre/right/down and holds one, two or three; its
                    shadows are exactly where they must be and nowhere else; and no four chips make
                    a solid block, which the lattice forbids outright and the clause checks anyway.
                    Control MALFORMED leaves a gap in a pile.
    (3) LIVE        the plate as shipped has a socket that is about to go off. A settled plate is
                    confluent for the wrong reason - there is only one schedule and it is empty.
                    Control DEAD is a plate of nothing but single studs, and it is refused here.
    (4) HALT        every schedule stops, inside the weight bound the plate proves for itself.
    (5) CONFLUENCE  all six schedules agree on the final picture AND on the tally of topples. THE
                    LAW, measured on every plate in the wardrobe.
    (6) DEPTH       the busiest socket toppled the class's number of times.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_confluence_axis75.py                     # write the four staged dirs
    python3 scripts/gen_confluence_axis75.py --sweep             # can every pose carry an avalanche
    python3 scripts/gen_confluence_axis75.py --accept            # six clauses, every pose
    python3 scripts/gen_confluence_axis75.py --controls          # the nine controls
    python3 scripts/gen_confluence_axis75.py --controls toppled-why   # destination vs journey
    python3 scripts/gen_confluence_axis75.py --controls halt-why      # the weight bound, measured
    python3 scripts/gen_confluence_axis75.py --ceiling           # what each garment could ever carry
    python3 scripts/gen_confluence_axis75.py --frame             # one real pose per class
    python3 scripts/gen_confluence_axis75.py --survive           # relief through the finishing pass
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

# THE PITCH, settled by the 74th and not re-argued here. At 2 a lattice of bright pixels with a
# lattice of shadows beside it stops reading as relief and reads as GINGHAM, which the 13px
# legibility pass has rejected three geometries for. At 3 the sockets are a ninth of the cloth, the
# piles scatter, and each keeps its own shadow.
PITCH = 3

# A PILE GROWS IN A FIXED ORDER, and that order is the whole of how a count becomes a picture.
# Every glyph is a PREFIX of this list, so 1 is a stud, 2 a horizontal pair, 3 an L, 4 a T lying on
# its back. Every offset is within one pixel of the socket, so a pile never reaches its neighbour's
# socket, and NO FOUR CHIPS CAN EVER MAKE A SOLID 2x2 BLOCK - the pixel down-and-right of a socket
# is at no legal offset from any socket of the same lattice. That is a theorem about the lattice,
# not a rule the painter follows, and clause PILE checks it anyway.
OFFS = ((0, 0), (0, 1), (1, 0))
MAXCHIPS = 3

# THE TOPPLE. Three chips leave, one to the right, one to the left, one downwards; anything aimed
# off the cloth is lost. Three directions and a threshold of three, so chips are conserved except
# where they leave the garment - and because one of the three always goes DOWN, the plate cannot
# circulate forever. See the weight argument in the docstring: clause HALT is a proof.
THRESH = 2
FIRE = ((1, 0), (0, 1))                  # right and down, in board coords (u, v); v grows down

SCHEDULES = ('first', 'last', 'loaded', 'rand0', 'rand1', 'rand2')

# CLASS IDENTITY IS A DEPTH: the greatest number of times any one socket has to topple.
DEPTH = {'mage': 1, 'ranger': 2, 'warrior': 3}
SWAP_DEPTH = {'mage': 2, 'ranger': 3, 'warrior': 1}

MIN_CELLS = 4        # a board smaller than this has no avalanche in it
SEED_DENS = 74       # of 255: how many sockets get a chip before the painter starts loading. TUNED
                     # DOWN FROM 96 AFTER THE FIRST FRAME DUMP: at 96 the warrior's every socket
                     # came out loaded and the plate read as a full field again, which is the
                     # gingham the 13px legibility pass exists to refuse. At 74 the seed is a thin
                     # scatter and THE PAINTER HAS TO BUILD ITS AVALANCHE SOMEWHERE IN PARTICULAR -
                     # so the plate reads as plain cloth with one hot cluster on it, which is
                     # relief, and relief is the only thing that survives the finishing pass.
SEED_PAIR = 64       # of 255: and how many of those get a second, so the field reads as studs AND
                     # dashes rather than a uniform stipple - the 74th is uniform studs and this
                     # axis has to be told apart from it across a room
FILL = 1.0           # chips per socket the painter aims for once its class's depth is secured -
                     # about six sockets in ten carrying a stud or a dash. It is a DENSITY and not
                     # a count, so a sabaton and a cuirass wear the same cloth; and it is spent
                     # inside the interval of loads that all mean the same class, so it never
                     # argues with the law.
TRIES = 160          # salted chip orders tried before a pose is reported plain. It can afford to
                     # be large: bisecting one monotone chain costs about six settlings, so a whole
                     # pose is a few hundred, and the project has twice paid for a painter that
                     # gave up before the garment did (the 73rd, the 74th).

# Three stops per class - (shadow, field, chip) - strictly increasing in luminance, none near black
# (a near-black darkest stop eats the visor's eye and mouth pixels; the 49th's lesson). Deliberately
# unrelated to the 71st (oxblood/moss/violet), 72nd (indigo/umber/jade), 73rd (graphite-orange/
# mulberry-linen/aubergine-citron) and 74th (slate-teal/peat-oxide/night blue).
# THE WARRIOR WAS OLIVE WITH PALE JADE CHIPS AND THE PANEL REFUSED IT: a green field with green
# marks on it is LICHEN, which is a mottle, which is camouflage - the same finding the 13px
# legibility pass has already made about three geometries, arrived at this time through the hue and
# not the geometry. Density was not the fault; the warrior carries the same chips a mage does. A
# gunmetal field with WARM GOLD chips separates in hue as well as in value and the studs come off
# the plate.
#   warrior  GUNMETAL AND PALE GOLD
#   ranger   BLACK CHERRY AND MINT
#   mage     SEA GREEN AND ICE PINK
PAL = {
    'warrior': ((30, 34, 42), (86, 96, 112), (242, 220, 152)),
    'ranger':  ((46, 24, 32), (118, 66, 80), (206, 240, 214)),
    'mage':    ((26, 46, 44), (76, 114, 110), (246, 216, 228)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_confluence_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary75',
    ),
    'legs': dict(
        outdir='_confluence_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary75',
    ),
    'boots': dict(
        outdir='_confluence_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_confluence',
    ),
    'helmet': dict(
        outdir='_confluencedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary75',
    ),
}

CONTROLS = ('random', 'dead', 'toppled', 'spent', 'swapped', 'offgrid', 'malformed',
            'crowded', 'flat')
CLAUSES = ('board', 'pile', 'live', 'halt', 'confluence', 'depth')


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


# --- the board ---------------------------------------------------------------------------------
def lattices_of(a, crowded=False):
    """The nine lattices, roomiest first. THE PAINTER PICKS ONE AND NEVER SAYS WHICH: the reader
    recovers it by finding the only one of the nine under which the picture parses at all."""
    if crowded:
        cells = [(int(y), int(x)) for y, x in np.argwhere(a)]
        return [(0, 0, cells, {c: (c[1], c[0]) for c in cells})]
    out = []
    for py in range(PITCH):
        for px in range(PITCH):
            cells = [(int(y), int(x)) for y, x in np.argwhere(a)
                     if y % PITCH == py and x % PITCH == px]
            bc = {(y, x): ((x - px) // PITCH, (y - py) // PITCH) for (y, x) in cells}
            out.append((py, px, cells, bc))
    return sorted(out, key=lambda b: -len(b[2]))


def weight(chips, B):
    """THE PLATE'S OWN BOUND ON ITS OWN AVALANCHE. Every chip is worth the number of board rows at
    or below its own, so a topple - three chips off row v, at most two back onto row v and one onto
    row v+1 - costs at least one. The weight is a non-negative integer, so the avalanche is over in
    at most `weight` topples. Nothing here is a tuned constant."""
    if not B:
        return 0
    umax = max(u for u, _v in B)
    vmax = max(v for _u, v in B)
    return sum(k * ((umax - c[0]) + (vmax - c[1]) + 2) for c, k in chips.items())


def stabilise(chips, B, sched='first', salt=''):
    """Topple until nothing is loaded. Returns (final chips, tally of topples, number of topples)
    or None if the plate outran the weight bound, which is a bug and not a possibility."""
    ch = {c: k for c, k in chips.items() if k}
    od = {}
    rng = Rng(salt + '|' + sched)
    budget = weight(ch, B)
    n = 0
    while True:
        loaded = [c for c, k in ch.items() if k >= THRESH]
        if not loaded:
            return ch, od, n
        if sched == 'first':
            c = min(loaded)
        elif sched == 'last':
            c = max(loaded)
        elif sched == 'loaded':
            c = max(loaded, key=lambda z: (ch[z], z))
        else:
            c = sorted(loaded)[rng.below(len(loaded))]
        ch[c] -= THRESH
        if not ch[c]:
            del ch[c]
        for du, dv in FIRE:
            t = (c[0] + du, c[1] + dv)
            if t in B:
                ch[t] = ch.get(t, 0) + 1
        od[c] = od.get(c, 0) + 1
        n += 1
        if n > budget:
            return None


def depth_of(chips, B, salt=''):
    got = stabilise(chips, B, 'first', salt)
    if got is None:
        return -1
    _ch, od, _n = got
    return max(od.values()) if od else 0


# --- the painter -------------------------------------------------------------------------------
def caps_of(a, bc_inv, B):
    """HOW MANY CHIPS EACH SOCKET CAN ACTUALLY SHOW. A pile grows in a fixed order, so a socket can
    hold k chips only if the first k offsets all have cloth under them. A pile the cloth cannot hold
    is a pile the reader will read as a smaller one, so the painter never writes one."""
    h, w = a.shape
    cap = {}
    for c in B:
        y0, x0 = bc_inv[c]
        k = 0
        for i in range(MAXCHIPS):
            dy, dx = OFFS[i]
            y, x = y0 + dy, x0 + dx
            if 0 <= y < h and 0 <= x < w and a[y, x]:
                k = i + 1
            else:
                break
        if k:
            cap[c] = k
    return cap


def ceiling_of(a, bc_inv, B, salt=''):
    """THE DEEPEST AVALANCHE THIS GARMENT COULD EVER CARRY, IN ONE SETTLING. Adding a chip can never
    make a socket topple fewer times - the tally is monotone in the load, which is the same fact
    that makes the tally well defined at all - so filling EVERY socket to the most its cloth can
    show gives a genuine UPPER BOUND on the depth, not an estimate.

    That is why this axis's impossibility report is a theorem and not a search: where the ceiling is
    below the class's depth, no painter however clever could have loaded the piece, and the report
    says so after one settling instead of the 74th's enumeration over every subset."""
    return depth_of(caps_of(a, bc_inv, B), B, salt)


def seed_chips(B, cap, rng, ceil=None):
    out = {}
    for c in sorted(B):
        if rng.byte() < SEED_DENS:
            k = 2 if rng.byte() < SEED_PAIR else 1
            k = min(k, cap.get(c, 0), ceil if ceil else MAXCHIPS)
            if k:
                out[c] = k
    return out


def load_to_depth(B, cap, target, rng, salt='', want_n=None):
    """THE PAINTER RIDES A MONOTONE CHAIN AND FINDS THE RUNG ITS CLASS IS ON.

    Order the chips - every socket contributes as many as its cloth can show - and fill them one at
    a time. Because the tally of topples is monotone in the load, the depth along that chain never
    goes down, so the chain is SORTED and the painter can BISECT it: six settlings find the shortest
    prefix that reaches the class's depth, instead of thirty greedy passes over every socket.

    The first draft did the greedy thing and came out PLAIN on two thirds of the warrior's poses -
    not because the garments could not carry a depth of three, but because a greedy painter walks
    into an overshoot and has no way back. Here an overshoot is simply a chain that skips the rung,
    and the painter shuffles and tries another; the order is salted, so what the plate ends up
    wearing is still its own."""
    slots = [(c, j) for c in sorted(cap) for j in range(cap[c])]
    N = len(slots)
    if not N:
        return None
    for i in range(N - 1, 0, -1):
        k = rng.below(i + 1)
        slots[i], slots[k] = slots[k], slots[i]

    def cfg(n):
        ch = {}
        for c, _j in slots[:n]:
            ch[c] = ch.get(c, 0) + 1
        return ch

    def first_at(d):
        """The shortest prefix of the chain whose depth is at least d, or N + 1 if there is none."""
        lo, hi = 0, N
        if depth_of(cfg(N), B, salt) < d:
            return N + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if depth_of(cfg(mid), B, salt) >= d:
                hi = mid
            else:
                lo = mid + 1
        return lo

    lo = first_at(target)
    if lo > N:
        return None            # the garment's ceiling is below the class: not the painter's fault
    hi = first_at(target + 1) - 1
    if hi < lo:
        return None            # this chain steps straight over the rung; another one may not
    # THE CLASS IS AN INTERVAL OF LOADS, NOT A LOAD. Between the shortest prefix that reaches the
    # depth and the longest that does not exceed it, every chip count is the same class - so the
    # painter is free to choose how much ornament the plate wears WITHOUT touching what it means.
    # It spends that freedom on a constant density across all three classes, which is why a mage
    # plate and a warrior plate look like the same family and read as different laws. The first
    # draft minimised instead, and the mage came out carrying two chips in total: lawful, and not
    # a pattern.
    want = int(round(FILL * len(B))) if want_n is None else want_n
    return cfg(min(max(want, lo), hi))


def paint(a, bc_inv, chips, offgrid=None, malformed=False):
    """A pile and the shadow it casts, and nothing else. RELIEF, NOT COLOUR: at thirteen pixels a
    flat field of another hue is camouflage, and only a crest with its own shadow survives the
    finishing pass. A chip reads raised because it is bright with a hard dark pixel one down and one
    left - the light direction every axis in this project has used."""
    h, w = a.shape
    core = np.zeros(a.shape, bool)
    for c, k in chips.items():
        if c not in bc_inv:
            continue
        y0, x0 = bc_inv[c]
        idx = list(range(min(k, MAXCHIPS)))
        if malformed and k >= 2:
            idx = [i for i in idx if i != 1] + [min(k, MAXCHIPS - 1)]
        for i in idx:
            dy, dx = OFFS[i % len(OFFS)]
            y, x = y0 + dy, x0 + dx
            if 0 <= y < h and 0 <= x < w and a[y, x]:
                core[y, x] = True
    if offgrid is not None and 0 <= offgrid[0] < h and 0 <= offgrid[1] < w and a[offgrid]:
        core[offgrid] = True
    dark = np.zeros(a.shape, bool)
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            dark[ny, nx] = True
    return core, dark


def drawable(a, bc_inv, chips):
    """A pile the cloth cannot hold is a pile the reader will read as a smaller one. The painter
    only ships piles whose every chip has cloth under it."""
    h, w = a.shape
    for c, k in chips.items():
        y0, x0 = bc_inv[c]
        for i in range(min(k, MAXCHIPS)):
            dy, dx = OFFS[i]
            y, x = y0 + dy, x0 + dx
            if not (0 <= y < h and 0 <= x < w and a[y, x]):
                return False
    return True


def compose(a, cls, mode=None, salt=''):
    """The piles for one pose, or None if the pose has no avalanche in it.
    Returns (py, px, cells, bc, bc_inv, B, chips)."""
    want = SWAP_DEPTH[cls] if mode == 'swapped' else DEPTH[cls]
    for py, px, cells, bc in lattices_of(a, crowded=(mode == 'crowded')):
        if len(cells) < MIN_CELLS:
            continue
        bc_inv = {v: k for k, v in bc.items()}
        B = set(bc.values())
        cap = caps_of(a, bc_inv, B)
        if not cap:
            continue

        if mode == 'random':
            # THE NULL HYPOTHESIS: sockets loaded with no thought for what they settle into.
            rng = Rng(salt + '|rnd')
            ch = seed_chips(B, cap, rng)
            for c in sorted(cap):
                if rng.byte() < 90:
                    ch[c] = min(ch.get(c, 0) + 2, cap[c])
            ch = {c: k for c, k in ch.items() if k}
            if ch:
                return py, px, cells, bc, bc_inv, B, ch
            continue

        if mode == 'dead':
            # A SETTLED PLATE. Nothing is loaded, so there is exactly one schedule and it is empty:
            # confluent for the wrong reason, and clause LIVE is what collects it.
            rng = Rng(salt + '|dead')
            ch = seed_chips(B, cap, rng, ceil=THRESH - 1)
            if ch:
                return py, px, cells, bc, bc_inv, B, ch
            continue

        # THE PLATE WEARS THE SAME AMOUNT OF ORNAMENT WHATEVER ITS CLASS. Every salted chip order
        # that works is costed by how far its load is from FILL chips a socket, and the closest is
        # the one that ships. The first draft let the load fall out of the search and the warrior -
        # the only class deep enough to sit near its garment's ceiling - came back from the panel
        # reading as LICHEN, a mottle, which is the camouflage the 13px legibility pass exists to
        # refuse; the second draft minimised the load instead and the mage came back carrying two
        # chips on the whole plate. Density is chosen, depth is measured, and the two do not meet.
        best = None
        for k in range(TRIES):
            rng = Rng('%s|%d|%d%d' % (salt, k, py, px))
            ch = load_to_depth(B, cap, want, rng, salt)
            if ch is None:
                continue
            ch = {c: v for c, v in ch.items() if v}
            if not ch or not drawable(a, bc_inv, ch):
                continue
            if len(ch) == len(B):
                continue        # no empty socket left: the reader cannot see the board breathe
            cost = abs(sum(ch.values()) - int(round(FILL * len(B))))
            if best is not None and cost >= best[0] and mode is None:
                continue
            core, dark = paint(a, bc_inv, ch)
            if not dark.any():
                continue        # three stops or the plate has said nothing
            if mode is None or mode in ('swapped', 'toppled', 'spent', 'offgrid', 'malformed',
                                        'flat'):
                # THE LATTICE MUST BE THE ONLY ONE THAT WORKS, checked at the easel with the
                # reader's own parser. This is the constraint that lets the painter keep its choice
                # of lattice to itself.
                if len(weak_parses(a, core)) != 1:
                    continue
            if mode is None:
                if best is None or cost < best[0]:
                    best = (cost, ch)
                continue
            if mode in ('toppled', 'spent'):
                # THE PLATE, ADVANCED BY ONE LEGAL MOVE.
                #   TOPPLED   any legal move, taken at random. Its destination is the original's,
                #             every time; its class it usually keeps, because a topple only shortens
                #             the journey of the socket it happens AT.
                #   SPENT     the one move that does change the class - a topple at the socket that
                #             is carrying it. THE CLASS OF A PLATE HANGS ON A SINGLE SOCKET, and
                #             this control is what proves it, by looking for the move that spends it
                #             and reporting how often such a move is even available.
                loaded = sorted([c for c, v in ch.items() if v >= THRESH])
                if not loaded:
                    continue
                cand = []
                for c in loaded:
                    t = dict(ch)
                    t[c] -= THRESH
                    if not t[c]:
                        del t[c]
                    for du, dv in FIRE:
                        q = (c[0] + du, c[1] + dv)
                        if q in B:
                            t[q] = t.get(q, 0) + 1
                    if any(v > MAXCHIPS for v in t.values()) or not drawable(a, bc_inv, t):
                        continue
                    cand.append((depth_of(t, B, salt), t))
                if mode == 'spent':
                    cand = [c for c in cand if c[0] != want]
                if not cand:
                    continue
                return py, px, cells, bc, bc_inv, B, cand[rng.below(len(cand))][1]
            return py, px, cells, bc, bc_inv, B, ch
        if best is not None:
            return py, px, cells, bc, bc_inv, B, best[1]
    return None


# --- the reader --------------------------------------------------------------------------------
def read_stops(fr, a):
    """Chip, shadow and field off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: three luminances
    on the piece - the brightest is a chip, the darkest is a chip's shadow, the rest is plain
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


def weak_parses(a, core):
    """EVERY LATTICE UNDER WHICH THE PICTURE IS A SET OF PILES AT ALL - the weak reading, which asks
    only that every bright pixel be owned by exactly one socket at one of the four legal offsets.
    It does NOT ask that the piles be well formed; that is clause PILE's business, so that a plate
    with a gap in a pile is caught for the right reason.

    An offset pixel can never have two owners: the three non-zero offsets put their owners at
    (y, x-1), (y-1, x) and (y, x+1), and no two of those are congruent to the same lattice."""
    marks = {(int(y), int(x)) for y, x in np.argwhere(core)}
    if not marks:
        return []
    out = []
    for py in range(PITCH):
        for px in range(PITCH):
            anchors = {m for m in marks if m[0] % PITCH == py and m[1] % PITCH == px}
            if not anchors or any(not a[m] for m in anchors):
                continue
            held = {m: set() for m in anchors}
            ok = True
            for m in marks - anchors:
                owner = None
                for i in range(1, len(OFFS)):
                    dy, dx = OFFS[i]
                    cand = (m[0] - dy, m[1] - dx)
                    if cand in anchors:
                        owner = (cand, i)
                        break
                if owner is None:
                    ok = False
                    break
                held[owner[0]].add(owner[1])
            if ok:
                out.append((py, px, held))
    return out


def well_formed(a, py, px, held, core, dark):
    """Clause PILE. Every pile is a PREFIX of centre/right/down/left and holds no more than four;
    every chip casts its shadow where there is cloth to take it and nowhere else; and no four chips
    make a solid block (which the lattice forbids outright - checked anyway)."""
    for _anc, s in held.items():
        k = len(s) + 1
        if k > MAXCHIPS or s != set(range(1, k)):
            return False
    h, w = a.shape
    want = set()
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            want.add((int(ny), int(nx)))
    if {(int(y), int(x)) for y, x in np.argwhere(dark)} != want:
        return False
    blk = core[:-1, :-1] & core[1:, :-1] & core[:-1, 1:] & core[1:, 1:]
    return not blk.any()


def read_plate(a, core, dark):
    """THE WHOLE READING, from the pixels and the outline and nothing else. Returns
    (status, py, px, B, chips): status is 'ok', 'board' (no lattice, or more than one that is well
    formed) or 'pile' (one lattice, and the piles on it are not legal)."""
    weak = weak_parses(a, core)
    if not weak:
        return 'board', None, None, None, None
    good = [p for p in weak if well_formed(a, p[0], p[1], p[2], core, dark)]
    if len(good) == 1:
        py, px, held = good[0]
        status = 'ok'
    elif len(weak) == 1:
        py, px, held = weak[0]
        status = 'pile'
    else:
        return 'board', None, None, None, None
    pts = [(int(yy), int(xx)) for yy, xx in np.argwhere(a)]
    B = {((x - px) // PITCH, (y - py) // PITCH) for (y, x) in pts
         if y % PITCH == py and x % PITCH == px}
    chips = {((m[1] - px) // PITCH, (m[0] - py) // PITCH): len(s) + 1 for m, s in held.items()}
    return status, py, px, B, chips


# --- frames ------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, dark, B, chips) or None if the pose has no avalanche in it."""
    shadow_c, field_c, chip_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE PILES GO ON. The source sheet's inherited highlights sit in
    # the same stop a chip does, and a reader told nothing cannot tell an inherited highlight from
    # a chip. Every tone here is put there by the board; the modelling comes back, richer, from the
    # finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    got = compose(a, cls, mode, salt)
    if got is None:
        return None
    py, px, cells, bc, bc_inv, B, chips = got
    if mode == 'flat':
        return np.zeros(a.shape, bool), np.zeros(a.shape, bool), B, chips
    off = None
    if mode == 'offgrid':
        # ONE CHIP WHERE NO PILE CAN OWN IT - down and to the right of a socket, which is the one
        # place on the lattice no offset reaches. Clause BOARD collects it.
        for c in sorted(chips):
            y0, x0 = bc_inv[c]
            if y0 + 1 < a.shape[0] and x0 + 1 < a.shape[1] and a[y0 + 1, x0 + 1]:
                off = (y0 + 1, x0 + 1)
                break
    core, dark = paint(a, bc_inv, chips, offgrid=off, malformed=(mode == 'malformed'))
    for y, x in np.argwhere(dark):
        put(fr, y, x, shadow_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, chip_c)
    return core, dark, B, chips


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
    """A SHEET IS LOADED IN ALL FORTY-TWO POSES OR IN NONE. An avalanche that appears in some frames
    of a walk and not others reads as a bug, not as a hard case."""
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
    v.update(plates=0, silent=0, chips=0, topples=0, depth_val=None, dest=None, budget=0)
    core, dark, three = read_stops(fr, a)
    if not three or not core.any():
        v['silent'] = 1
        return v
    v['plates'] = 1

    status, py, px, B, chips = read_plate(a, core, dark)
    if status == 'board':
        v['board'] = 1
        return v
    if status == 'pile':
        v['pile'] = 1
        return v
    v['chips'] = sum(chips.values())
    v['budget'] = weight(chips, B)

    # (3) LIVE - something on this plate is about to go off
    if not any(k >= THRESH for k in chips.values()):
        v['live'] = 1
        return v

    # (4) HALT and (5) CONFLUENCE - THE RACE
    runs = []
    for sched in SCHEDULES:
        got = stabilise(chips, B, sched, salt)
        if got is None:
            v['halt'] = 1
            return v
        runs.append(got)
    dests = {tuple(sorted(r[0].items())) for r in runs}
    tallies = {tuple(sorted(r[1].items())) for r in runs}
    if len(dests) != 1 or len(tallies) != 1:
        v['confluence'] = 1
    v['topples'] = runs[0][2]
    v['dest'] = sorted(runs[0][0].items())

    # (6) DEPTH - the busiest socket, and how many times it went off. The measured number is kept
    # under `depth_val`; `depth` is the CLAUSE, and is 1 only when the number is not the class's.
    od = runs[0][1]
    d = max(od.values()) if od else 0
    v['depth_val'] = d
    v['depth'] = 1 if d != DEPTH[cls] else 0
    return v


def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, sheets=0, pass_sheets=0, chips=0, topples=0, races=0)
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
                np_ = ns = ntp = 0
                nch, dpt = [], []
                for fi, a, (fr, _g) in plates:
                    res = inspect_frame(fr, a, cls, '%s|%d' % (stem, fi))
                    for c in CLAUSES:
                        bad[c] += res[c]
                    np_ += res['plates']
                    ns += res['silent']
                    ntp += res['topples']
                    if res['chips']:
                        nch.append(res['chips'])
                    if res.get('depth_val') is not None:
                        dpt.append(res['depth_val'])
                tot['plates'] += np_
                tot['silent'] += ns
                tot['chips'] += sum(nch)
                tot['topples'] += ntp
                tot['races'] += np_ * len(SCHEDULES)
                for c in CLAUSES:
                    tot[c] += bad[c]
                good = not any(bad.values())
                tot['pass_sheets'] += 1 if good else 0
                print('   %-7s %-8s %-2s  depth=%d plates=%-3d chips %d-%-3d topples=%-5d  %s%s'
                      % (kind, cls, suffix or 'm', DEPTH[cls], np_,
                         min(nch) if nch else 0, max(nch) if nch else 0, ntp,
                         'ALL PASS' if good else 'FAIL ',
                         '' if good else ' ' + ' '.join('%s=%d' % (c, k)
                                                        for c, k in bad.items() if k)),
                      flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d chips drawn, %d silent'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['chips'], tot['silent']))
    print('   %d topples played over %d races, and every race ended in the same place'
          % (tot['topples'], tot['races']))
    for c in CLAUSES:
        print('   %-11s %d violations' % (c.upper(), tot[c]))


# --- the controls ------------------------------------------------------------------------------
def controls_report(which=None):
    if which == 'toppled-why':
        toppled_why()
        return
    if which == 'halt-why':
        halt_why()
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
                    res = inspect_frame(fr, a, cls, '%s|%d' % (stem, fi))
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
            'dead': '  <- a SETTLED plate: confluent because there is only one schedule, the empty one',
            'toppled': ('  <- ANY legal move: the destination is the original\'s every time, and '
                        'the class survives four times in five'),
            'spent': ('  <- THE ONE MOVE THAT SPENDS THE CLASS, a topple at the socket carrying '
                      'it. The exact inverse of the 74th\'s JUMPED, which nothing could break'),
            'swapped': '  <- LAWFUL AND MISNAMED: the reader names the class the plate really is',
            'offgrid': '  <- one chip down-and-right of a socket, where no pile can own it',
            'malformed': '  <- a gap in a pile: the count no longer reads off the pixels',
            'crowded': '  <- a socket on every pixel: no lattice, and the piles run together',
            'flat': '  <- fewer than three stops, so there is nothing to read (SILENT, not passed)',
        }.get(mode, '')
        print('   %-10s drawn=%-4d CLEAN=%-4d  %s%s' % (mode.upper(), drawn, clean, note, extra),
              flush=True)
        if undrawable:
            print('   %-10s %d plates could not be drawn at all' % ('', undrawable))
        if silent:
            print('   %-10s %d plates show fewer than three stops (SILENT, not passed)'
                  % ('', silent))


def toppled_why():
    """THE DESTINATION IS SHARED AND THE JOURNEY IS NOT. A plate advanced by one legal move settles
    into exactly the picture the original settles into - that is the law, and it holds - and it is
    no longer its class, because its busiest socket has one topple fewer left to do. The 74th's
    equivalent control was the only one in the project meant to PASS; this one is meant to fail, and
    the two facts together are what separates an invariance from a confluence."""
    print('== TOPPLED  (EVERY legal move of every shipped plate, destination and journey apart)')
    same = moves = shallower = plates = withweak = 0
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            stem = cfg['srcs'][cls]
            base = load_any('%s.png' % stem)
            for fi, sl, a in frames_of(base):
                salt = '%s|%d' % (stem, fi)
                g0 = compose(a, cls, None, salt)
                if g0 is None:
                    continue
                B, ch0 = g0[5], g0[6]
                r0 = stabilise(ch0, B, 'first', salt)
                if r0 is None:
                    continue
                plates += 1
                d0 = max(r0[1].values()) if r0[1] else 0
                weak = 0
                # EVERY MOVE THE PLATE HAS, not a sample of one. This is the whole orbit one step
                # out, and it is cheap enough to enumerate outright.
                for c in sorted([c for c, v in ch0.items() if v >= THRESH]):
                    t = dict(ch0)
                    t[c] -= THRESH
                    if not t[c]:
                        del t[c]
                    for du, dv in FIRE:
                        q = (c[0] + du, c[1] + dv)
                        if q in B:
                            t[q] = t.get(q, 0) + 1
                    r1 = stabilise(t, B, 'last', salt)
                    if r1 is None:
                        continue
                    moves += 1
                    if sorted(r1[0].items()) == sorted(r0[0].items()):
                        same += 1
                    d1 = max(r1[1].values()) if r1[1] else 0
                    if d1 < d0:
                        shallower += 1
                        weak += 1
                withweak += 1 if weak else 0
    print('   plates %d, legal moves enumerated %d' % (plates, moves))
    print('   destination preserved by the move:  %d/%d (%d%%)   <- THE LAW, and NO move reaches it'
          % (same, moves, 100 * same // max(moves, 1)))
    print('   class spent by the move:            %d/%d (%d%%)   <- and it is always the same '
          'socket' % (shallower, moves, 100 * shallower // max(moves, 1)))
    print('   plates with a move that spends the class: %d/%d   and those plates have %d such '
          'move(s) between them' % (withweak, plates, shallower))
    print('   <- WHERE A PLATE HAS A WEAK POINT IT HAS EXACTLY ONE. The rest of the plate can be '
          'played without consequence.')


def halt_why():
    """THE BOUND THE PLATE PROVES ABOUT ITSELF. Weight every chip by the number of board rows at or
    below its own; a topple costs at least one unit of weight and the weight cannot go negative, so
    the plate carries its own certificate of termination. Reported as how much of its own bound each
    plate actually spends - the bound is not tight, and it does not have to be, because it is a
    proof and not a budget."""
    print('== HALT  (every plate\'s own weight bound, against what it actually spends)')
    for kind, cfg in SLOTS.items():
        spend, bound, n, worst = 0, 0, 0, 0
        for cls in cfg['srcs']:
            stem = cfg['srcs'][cls]
            base = load_any('%s.png' % stem)
            for fi, sl, a in frames_of(base):
                salt = '%s|%d' % (stem, fi)
                got = compose(a, cls, None, salt)
                if got is None:
                    continue
                B, ch = got[5], got[6]
                w = weight(ch, B)
                mx = 0
                for sched in SCHEDULES:
                    r = stabilise(ch, B, sched, salt)
                    if r is None:
                        print('   %-7s BOUND EXCEEDED - this is a bug' % kind)
                        return
                    mx = max(mx, r[2])
                spend += mx
                bound += w
                worst = max(worst, (100 * mx) // max(w, 1))
                n += 1
        print('   %-7s %4d plates   topples spent %5d of a proved bound of %5d (%2d%% mean, '
              '%2d%% worst)  0 overruns'
              % (kind, n, spend, bound, (100 * spend) // max(bound, 1), worst))


# --- reports -----------------------------------------------------------------------------------
def sweep():
    print('== SLOTS  (can every pose carry an avalanche of its class\'s depth, and does it read back)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                fit = unfit = 0
                nch, ntp = [], []
                for fi, sl, a in frames_of(base):
                    fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                    if got is None:
                        unfit += 1
                        continue
                    res = inspect_frame(fr, a, cls, '%s|%d' % (stem, fi))
                    if any(res[c] for c in CLAUSES):
                        unfit += 1
                    else:
                        fit += 1
                        nch.append(res['chips'])
                        ntp.append(res['topples'])
                print('   %-7s %-8s %-2s  depth=%d chips %d-%-3d topples %d-%-3d  poses %2d/%-2d  '
                      'SHEET %s'
                      % (kind, cls, suffix or 'm', DEPTH[cls],
                         min(nch) if nch else 0, max(nch) if nch else 0,
                         min(ntp) if ntp else 0, max(ntp) if ntp else 0,
                         fit, fit + unfit,
                         'loaded' if unfit == 0 else 'PLAIN (reported)'), flush=True)


def ceiling_report():
    """WHERE A GARMENT CANNOT CARRY ITS CLASS, THAT IS A THEOREM ABOUT THE GARMENT.

    The tally of topples is monotone in the load: put another chip on a plate and no socket topples
    fewer times than it did. So loading EVERY socket to the most chips its cloth can show, and
    settling that once, gives the deepest avalanche the piece could ever be made to carry - an upper
    bound, not a sample. Where that ceiling is under the class's depth, no painter however patient
    would have found a plate, and this report is entitled to say IMPOSSIBLE and mean it.

    The 73rd had to learn this the hard way and the 74th paid for it in an enumeration over every
    subset of every parity; here monotonicity hands it over for the price of one settling a pose."""
    print('== CEILING  (the deepest avalanche each garment could EVER carry, and its class\'s depth)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                ceils = []
                for fi, sl, a in frames_of(base):
                    best = 0
                    for py, px, cells, bc in lattices_of(a):
                        if len(cells) < MIN_CELLS:
                            continue
                        bc_inv = {v: k for k, v in bc.items()}
                        best = max(best, ceiling_of(a, bc_inv, set(bc.values()),
                                                    '%s|%d' % (stem, fi)))
                    ceils.append(best)
                need = DEPTH[cls]
                able = sum(1 for d in ceils if d >= need)
                print('   %-7s %-8s %-2s  needs %d   ceiling %d-%-2d   poses that could ever carry '
                      'it %2d/%-2d  %s'
                      % (kind, cls, suffix or 'm', need, min(ceils), max(ceils), able, len(ceils),
                         'ok' if able == len(ceils)
                         else 'PROVED IMPOSSIBLE on %d pose(s)' % (len(ceils) - able)))


def frame_dump():
    print('== ONE REAL POSE PER CLASS  (digit = chips on that socket, "o" empty socket, '
          '"=" shadow, "-" field)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            salt = '%s|%d' % (stem, fi)
            got = compose(a, cls, None, salt)
            if got is None:
                continue
            py, px, cells, bc, bc_inv, B, chips = got
            core, dark = paint(a, bc_inv, chips)
            r = stabilise(chips, B, 'first', salt)
            d = max(r[1].values()) if r[1] else 0
            print('== %s chest frame %d   %d sockets, %d chips on %d piles   %d topples, depth %d'
                  % (cls, fi, len(B), sum(chips.values()), len(chips), r[2], d))
            print('   destination: %d chips on %d sockets, and every schedule finds it'
                  % (sum(r[0].values()), len(r[0])))
            ys, xs = np.nonzero(a)
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    c = bc.get((y, x))
                    if not a[y, x]:
                        row += '.'
                    elif c is not None and c in chips:
                        row += str(chips[c])
                    elif c is not None:
                        row += 'o'
                    elif core[y, x]:
                        row += '+'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a chip on the
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
            fin, _i = finish_array(arr.copy(), '_tmp/%s%s_%s.png' % (cfg['dst'] % cls, suffix, kind))
            for fi, sl, a in frames_of(base):
                _fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                if got is None:
                    continue
                core, dark, _B, _ch = got
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for y, x in np.argwhere(core):
                    nb = [lum[ny, nx] for ny, nx in
                          ((y + 1, x - 1), (y - PITCH, x), (y + PITCH, x),
                           (y, x - PITCH), (y, x + PITCH))
                          if 0 <= ny < FH and 0 <= nx < FW and not core[ny, nx]
                          and (dark[ny, nx] or a[ny, nx])]
                    if not nb:
                        continue
                    tot += 1
                    if lum[y, x] > float(np.mean(nb)):
                        ok += 1
        print('   %-7s chip still lighter than the cloth around it: %5d/%-5d (%3d%%)'
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
    if '--ceiling' in sys.argv:
        ceiling_report()
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
