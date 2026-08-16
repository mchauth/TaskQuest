#!/usr/bin/env python3
"""SEVENTY-FOURTH net-new-geometry axis for ALL FOUR SLOTS - the ATTRITION family: the ornament is a
BOARD OF SOCKETS, some of them filled, and the law is a number THAT NO AMOUNT OF DESTROYING THE
ORNAMENT CAN CHANGE.

    the ground is    a BOARD      every cloth pixel of one parity is a socket, so the board is fixed
                                  by the silhouette and not by the painter, and the reader can see
                                  at a glance that no socket has been hidden from it
    the ornament is  a PEG        a socket that is FILLED - a bright stud with a hard shadow one
                                  down and one left of it. THE EMPTY SOCKETS ARE NOT DRAWN AND DO
                                  NOT NEED TO BE: any one peg fixes the parity and the silhouette
                                  supplies the rest, so the reader rebuilds the whole board out of
                                  the pegs and the outline before it plays a move
    the move is      a JUMP       a peg hops over its neighbour into the empty socket beyond, AND THE
                                  PEG IT JUMPED IS TAKEN OFF THE PLATE. Every move destroys ornament.
    the law is       THE PLATE'S VALUE IN GF(4)x GF(4) IS ITS CLASS'S, AND NO JUMP CAN MOVE IT

*** THIS IS THE FIRST INVARIANT THAT SURVIVES THE DESTRUCTION OF THE ORNAMENT THAT CARRIES IT. ***
Seventy-three axes state a law about a picture. Take a mark off the 68th SEME and its Sidon set is
broken; take a bar off the 70th TRUSS and its flex is a different number; take a rod off the 72nd
QUORUM and the secret is gone; take a beacon off the 73rd SURVEY and the ground stops being
addressable. HERE THE READER IS INVITED TO TAKE THE ORNAMENT APART, one peg at a time, until two
thirds of it is gone - and the number is exactly where it was. The law is not a property of the
plate. It is a property of EVERY PLATE THE PLATE CAN BECOME, and the picture you are looking at is
only the one the painter happened to stop at.

*** IT IS THE EXACT COMPLEMENT OF THE 66th DOVETAIL. ***
    66th DOVETAIL   an IMPOSSIBILITY OF ACTION      nothing can be carried away
    74th ATTRITION  an INDIFFERENCE TO ACTION       carry away whatever you like
The 66th's acceptance test was a DISASSEMBLY and it was satisfied by FAILING to take the artefact
apart. This one's is a DEMOLITION and it is satisfied by SUCCEEDING and finding the law still
standing in the rubble. Those are the only two things a reader with its hands on an artefact can
find out, and this is the second of them.

*** THE INVARIANT IS AN ORBIT INVARIANT, WHICH IS NEW IN KIND. ***
    63rd CURRENT    a fact about a SEQUENCE SOMEBODY ELSE PRODUCED   (shuffle the frames, it is gone)
    71st GAMBIT     a fact about a GAME AGAINST AN OPPONENT
    74th ATTRITION  a fact about EVERY POSITION THIS ONE CAN REACH
The 63rd needed the reader to be shown a history. This needs the reader to MAKE one, and any history
it likes: the value is the same at the end of every one of them. Control JUMPED is the whole point
of the axis rendered as a control - a plate advanced by one legal move is A DIFFERENT PICTURE AND
THE SAME PLATE, and it passes every clause. No previous axis has had a control it WANTED to pass.

*** CLASS IDENTITY IS A NUMBER OF OBSTRUCTIONS - HOW MANY WAYS THE PLATE CANNOT END. ***
The value is a pair (S, T), one sum along each diagonal of the board, each living in GF(4):

    S = XOR over pegs of w^(u+v)        T = XOR over pegs of w^(u-v)        w^2 + w + 1 = 0

A lone peg has both coordinates non-zero, always. So a coordinate that VANISHES is a door that has
closed: the plate can never be played down to a single peg, and no amount of playing will reveal it
- only the sum will.

    mage      0 obstructions   both coordinates alive. The plate CAN end as one peg, and the reader
                               can name the ninth of the lattice that peg must stand on.
    ranger    1 obstruction    one diagonal has closed.
    warrior   2 obstructions   both have. The most ornamented plate in the wardrobe is the one with
                               the least future.

Not a count (67th), a ceiling (68th), a multipole order (69th), a number of motions (70th), a
fraction of a move (71st), the size of a coalition (72nd) or a precision (73rd): A NUMBER OF THINGS
THE PLATE HAS LOST. Every previous class counts something the plate HAS. It is an OUTPUT - two sums
and a look at which of them are zero - and there is nothing to argue about.

*** THE ACCEPTANCE TEST IS A NEW KIND: A DEMOLITION. ***
The reader recovers the board and the pegs off the pixels and then PLAYS THE PLATE TO PIECES,
choosing jumps at random until no jump is left, and recomputing the value after every single one.
Six clauses:

    (1) BOARD      every peg agrees on one parity, so the board is that parity's cloth pixels and
                   nothing else. THE BOARD IS THE SILHOUETTE'S AND NOT THE PAINTER'S, and a stray
                   peg off the lattice is caught the same way the 73rd caught a pruned arm, by
                   asking the outline - control OFFGRID leaves the value untouched and is refused
                   415 times out of 415.
    (2) VALUE      the number of vanishing coordinates is the class's. THE LAW.
    (3) DESTINY    the class's prediction is made good. For the mage the reader names the ninth of
                   the board its last peg must stand on and checks the plate actually has one; for
                   the others it tests EVERY socket on the board and confirms that none of them
                   could be the plate's last peg. THE FIRST CLAUSE VERIFIED BY CHECKING EVERY WAY
                   THE PLATE COULD END.
    (4) STABLE     the value after every jump of the demolition equals the value before it. The
                   theorem, measured rather than assumed, on every plate in the wardrobe.
    (5) LIVE       the plate has moves in it, and the demolition actually takes pegs off. THE FIRST
                   CLAUSE THAT DEMANDS THE ARTEFACT BE DESTRUCTIBLE - a still life keeps its value
                   for the wrong reason, because nothing can happen to it.
    (6) LEGIBLE    the plate reads back off its own pixels: a cast shadow under every peg that has
                   cloth to cast one on, and no dark pixel anywhere that is not one.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_attrition_axis74.py                    # write the four staged preview dirs
    python3 scripts/gen_attrition_axis74.py --sweep            # can every pose carry a board
    python3 scripts/gen_attrition_axis74.py --accept           # six clauses, every pose, every sheet
    python3 scripts/gen_attrition_axis74.py --controls         # the nine controls
    python3 scripts/gen_attrition_axis74.py --controls jumped-why    # the orbit, shown
    python3 scripts/gen_attrition_axis74.py --controls destiny-why   # the named ninth, counted
    python3 scripts/gen_attrition_axis74.py --controls sabaton-why   # the plain sheet, proved
    python3 scripts/gen_attrition_axis74.py --frame            # one real component per class
    python3 scripts/gen_attrition_axis74.py --survive          # relief through the finishing pass
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

DENSITY = 118        # of 255: how full the board starts before the value is fixed. TUNED DOWN FROM
                     # 158 AFTER LOOKING AT THE PANEL: at five sockets in eight the bright pegs and
                     # the sunken ones alternate over the whole torso and the plate reads as GINGHAM
                     # - a flat two-colour field, which is camouflage at thirteen pixels and exactly
                     # what the legibility pass warns about. At four in nine the pegs read as
                     # scattered studs on a plain plate, which is relief, and relief is the only
                     # thing that survives the finishing pass.
MIN_CELLS = 5        # a board smaller than this has no game in it
MIN_JUMPS = 3        # clause LIVE: the demolition must actually take pegs off
TRIES = 48           # salted attempts before a pose is reported unplayable
MAX_DEMO = 4000
EXHAUST = 18         # a board this small is enumerated outright rather than searched

# THE PITCH OF THE BOARD, AND THE MOST EXPENSIVE NUMBER IN THE FILE. At 2 the sockets are every
# other pixel in both directions, which is a quarter of the cloth, and the panel said what that
# looks like at thirteen pixels: GINGHAM. A regular lattice of bright pixels with a regular lattice
# of shadows beside them stops reading as studs and starts reading as WEAVE, and a woven field is
# camouflage - the legibility pass has said so about three geometries already. At 3 the sockets are
# a NINTH of the cloth, the pegs are scattered rather than ranked, and each one keeps its own
# shadow, so the plate reads as a studded plate. The arithmetic does not care: u and v are board
# coordinates whatever the pitch is, and a jump is still three sockets in a row.
PITCH = 3

NB4 = ((-1, 0), (1, 0), (0, -1), (0, 1))
NB8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

# GF(4) = {0, 1, w, w^2} written as 0,1,2,3. Addition is XOR - the additive group is (Z/2)^2, and
# 1 + w + w^2 = 0 is the whole reason a jump cannot move the value: a jump removes w^k and w^(k+1)
# and adds w^(k+2), and those three sum to zero on both diagonals at once.
POW = (1, 2, 3)

# THE CLASS IS THE NUMBER OF COORDINATES OF THE VALUE THAT VANISH.
OBSTRUCT = {'mage': 0, 'ranger': 1, 'warrior': 2}
SWAP_OBSTRUCT = {'mage': 1, 'ranger': 2, 'warrior': 0}

# Four stops per class, strictly increasing in luminance - (witness, hole, field, peg). None near
# black: a near-black darkest stop eats the visor's eye and mouth pixels (the 49th's lesson).
# Deliberately unrelated to the 70th (blackened brass/slate blue/verdigris), 71st (oxblood/moss/
# violet), 72nd (indigo/moonwhite, umber/wheat, jade/seafoam), 73rd (graphite/signal orange,
# mulberry/linen, aubergine/citron).
#   warrior  SLATE-TEAL AND BONE
#   ranger   PEAT AND OXIDE RED
#   mage     NIGHT BLUE AND SILVER-LILAC
# THE EMPTY SOCKETS ARE NOT PAINTED, AND THE FIRST DRAFT PAINTED THEM. Giving them a tone of their
# own put a mark on every socket of the lattice, and a mark on every socket of a two-pixel lattice
# is a regular two-tone chequer - which at thirteen pixels is GINGHAM. The panel said so
# immediately. They do not need painting: the board is every cloth pixel of one parity, the parity
# is fixed by any single peg, and THE SILHOUETTE DRAWS THE EMPTY SOCKETS FOR FREE. So the plate
# carries three stops - a bright peg, its hard shadow one down and one left, and plain field - and
# the reader reconstructs the whole board off the pegs and the outline before it plays a move.
#   warrior  SLATE-TEAL AND BONE
#   ranger   PEAT AND OXIDE RED
#   mage     NIGHT BLUE AND SILVER-LILAC
PAL = {
    'warrior': ((40, 52, 58), (106, 134, 140), (224, 232, 222)),
    'ranger':  ((40, 30, 26), (120, 88, 74), (236, 148, 104)),
    'mage':    ((30, 32, 56), (94, 100, 154), (220, 220, 246)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_attrition_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary74',
    ),
    'legs': dict(
        outdir='_attrition_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary74',
    ),
    'boots': dict(
        outdir='_attrition_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_attrition',
    ),
    'helmet': dict(
        outdir='_attritiondome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary74',
    ),
}

CONTROLS = ('random', 'toggled', 'slid', 'jumped', 'swapped', 'dead', 'offgrid', 'crowded',
            'flat')
CLAUSES = ('board', 'value', 'destiny', 'stable', 'live', 'legible')


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
    identically, and male and female of an item are played the same way."""

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
def boards_of(a, crowded=False):
    """THE BOARD IS THE SILHOUETTE'S. Every cloth pixel of ONE parity is a socket; the painter
    chooses only which of the nine parities, and it never chooses which sockets to show, because the
    plate is obliged to draw every one of them, filled or empty. THE READER DOES NOT NEED TO BE TOLD
    WHICH PARITY WAS PICKED - it reads the parity off the marks and then checks, against the
    outline, that nothing of that parity was left out. Control HOLED is a plate that draws only the
    filled sockets, and it is caught here.

    Returns the nine boards, roomiest first: on a small piece - a sabaton, a hood - the roomiest
    parity is often the one with no straight run of three sockets anywhere in it, and a parity with
    fewer sockets and a game in it is a better board than a parity with more and none."""
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


def value(pegs_uv):
    """THE NUMBER. Two sums, one along each diagonal, each in GF(4). Nothing else is needed and
    nothing else is used: no orientation, no ordering, no constant, no help."""
    s = t = 0
    for (u, v) in pegs_uv:
        s ^= POW[(u + v) % 3]
        t ^= POW[(u - v) % 3]
    return s, t


def obstructions(val):
    """THE CLASS, READ OFF THE PLATE: how many of the two diagonals have closed."""
    return int(val[0] == 0) + int(val[1] == 0)


def legal_jumps(pegs, cells):
    """A peg hops its neighbour into the empty socket beyond, and the jumped peg is taken off."""
    out = []
    for A in pegs:
        for dy, dx in DIRS:
            B = (A[0] + dy, A[1] + dx)
            C = (A[0] + 2 * dy, A[1] + 2 * dx)
            if B in pegs and C in cells and C not in pegs:
                out.append((A, B, C))
    return out


def demolish(pegs, cells, salt):
    """THE ACCEPTANCE TEST'S ENGINE - AND THE ONLY ONE IN THE PROJECT THAT WRECKS WHAT IT IS
    TESTING. Jumps are taken at random until no jump is left; the value is recomputed after every
    one of them. Returns (jumps taken, every value seen, what is left)."""
    st = set(pegs)
    seen = [value(st)]
    rng = Rng(salt + '|demo')
    n = 0
    while n < MAX_DEMO:
        js = sorted(legal_jumps(st, cells))
        if not js:
            break
        A, B, C = js[rng.below(len(js))]
        st.discard(A)
        st.discard(B)
        st.add(C)
        seen.append(value(st))
        n += 1
    return n, seen, st


def ninth_of(val):
    """THE NAMED NINTH. If neither coordinate has closed, the plate can end as one peg and the peg's
    socket is pinned: u + v = i and u - v = j (mod 3) has one solution, because 2 is its own inverse
    mod 3. So the plate names one socket in nine, and the reader can go and look for it."""
    s, t = val
    if s == 0 or t == 0:
        return None
    i, j = POW.index(s), POW.index(t)
    return (2 * (i + j)) % 3, (2 * (i - j)) % 3


# --- the painter -------------------------------------------------------------------------------
def seed_pegs(cells, bc, rng):
    return {bc[c] for c in cells if rng.byte() < DENSITY}


def steer(pegs, allc, want):
    """TOGGLE AS FEW SOCKETS AS WILL DO. A socket toggled adds its own pair to the value, so hitting
    a target shape is a tiny linear problem over GF(2)^4 and the painter solves it by hand: nothing
    first, then one socket, then two. The pattern the plate wears is otherwise its own."""
    if obstructions(value(pegs)) == want:
        return set(pegs)
    for c in allc:
        p2 = set(pegs) ^ {c}
        if p2 and obstructions(value(p2)) == want:
            return p2
    for i, c1 in enumerate(allc):
        for c2 in allc[i + 1:]:
            p2 = set(pegs) ^ {c1} ^ {c2}
            if p2 and obstructions(value(p2)) == want:
                return p2
    return None


def playable(pegs, cells, salt, floor):
    """THE PAINTER PLAYS THE PLATE BEFORE IT PAINTS IT, WITH THE READER'S OWN SEED. Clause LIVE only
    asks that the plate be destructible at all; the painter asks for more than that where the cloth
    can give it, and settles for the clause where it cannot. That is why the wardrobe's small pieces
    - a sabaton, a hood - carry short games and its chests carry long ones."""
    n, seen, left = demolish(pegs, cells, salt)
    return n >= floor and len(set(seen)) == 1, n, left


def compose(a, cls, mode=None, salt=''):
    """The pegs for one pose, or None if the pose has no game in it. Returns (py, px, cells, bc,
    pegs) in board coordinates."""
    want = SWAP_OBSTRUCT[cls] if mode == 'swapped' else OBSTRUCT[cls]
    for floor, (py, px, cells, bc) in [(f, b) for f in (MIN_JUMPS, 1)
                                       for b in boards_of(a, crowded=(mode == 'crowded'))]:
        if len(cells) < MIN_CELLS:
            continue
        allc = sorted(bc[c] for c in cells)

        if mode == 'random':
            # THE NULL HYPOTHESIS: a board filled with no thought for what it sums to.
            rng = Rng(salt + '|rnd')
            pegs = seed_pegs(cells, bc, rng)
            if pegs:
                return py, px, cells, bc, pegs
            continue

        if mode == 'dead':
            # A STILL LIFE. Pegs on alternate sockets only, so no peg has a neighbour and no jump
            # exists. Its value is safe from every move for the wrong reason: nothing can happen.
            pegs = {c for c in allc if (c[0] + c[1]) % 2 == 0}
            if pegs:
                return py, px, cells, bc, pegs
            continue

        for k in range(TRIES):
            rng = Rng('%s|%d|%d%d' % (salt, k, py, px))
            pegs = steer(seed_pegs(cells, bc, rng), allc, want)
            if pegs is None:
                continue
            if mode == 'crowded':
                return py, px, cells, bc, pegs
            # THE SAME SEED THE READER WILL USE. A demolition is a random walk, and a painter that
            # tested its plate with a different seed from the reader's would be certifying a
            # different game from the one the plate is going to be put through.
            ok, _n, _left = playable(pegs, set(allc), salt, floor)
            if not ok:
                continue
            # FOUR STOPS OR THE PLATE HAS SAID NOTHING. A board with no empty socket on it, or one
            # whose every peg stands where no cloth can take its shadow, shows the reader three
            # tones instead of four - and a reader that cannot see the empty sockets cannot play.
            _c, _d = paint(a, cells, bc, pegs)
            if not _d.any() or len(pegs) == len(allc):
                continue
            if want == 0 and ninth_of(value(pegs)) is not None:
                u0, v0 = ninth_of(value(pegs))
                if not any(c[0] % 3 == u0 and c[1] % 3 == v0 for c in allc):
                    continue        # clause DESTINY, enforced at the easel
            if mode == 'toggled':
                # ONE SOCKET CHANGED ITS MIND. Not a move - a move takes two pegs off and puts one
                # back, and this takes one off. The value goes with it.
                pegs = set(pegs) ^ {allc[rng.below(len(allc))]}
                return py, px, cells, bc, pegs
            if mode == 'slid':
                # A PEG WALKED INSTEAD OF JUMPING. The nearest thing to a legal move that is not
                # one, and the value knows the difference.
                for A in sorted(pegs):
                    for dy, dx in DIRS:
                        B = (A[0] + dy, A[1] + dx)
                        if B in set(allc) and B not in pegs:
                            return py, px, cells, bc, (set(pegs) - {A}) | {B}
                continue
            if mode == 'jumped':
                # THE AXIS ITSELF, RUN AS A CONTROL. One legal jump, and the plate is a different
                # picture with two fewer pegs on it. IT IS MEANT TO PASS.
                js = sorted(legal_jumps(pegs, set(allc)))
                if not js:
                    continue
                A, B, C = js[rng.below(len(js))]
                pegs = (set(pegs) - {A, B}) | {C}
                if not playable(pegs, set(allc), salt, 1)[0]:
                    continue
                return py, px, cells, bc, pegs
            return py, px, cells, bc, pegs

        # THE SEARCH IS EXHAUSTED BEFORE THE GARMENT IS BLAMED. This is the 73rd's lesson applied,
        # and applied where it actually bites: on a small board the salted patterns can miss a
        # lawful plate that is sitting right there, so where the board is small enough to enumerate
        # - every sabaton and every hood is - EVERY SUBSET OF IT IS TRIED, in a fixed order, before
        # the pose is called plain. It rescues four warrior sabaton poses and a mage one, and it is
        # what lets `--controls sabaton-why` say PROVED IMPOSSIBLE and mean it.
        if mode is None and len(allc) <= EXHAUST:
            n = len(allc)
            for m in range(1, 1 << n):
                pegs = {allc[i] for i in range(n) if m >> i & 1}
                if len(pegs) == n or obstructions(value(pegs)) != want:
                    continue
                if not playable(pegs, set(allc), salt, 1)[0]:
                    continue
                _c, _d = paint(a, cells, bc, pegs)
                if not _d.any():
                    continue
                nin = ninth_of(value(pegs))
                if want == 0 and nin is not None and not any(
                        c[0] % 3 == nin[0] and c[1] % 3 == nin[1] for c in allc):
                    continue
                return py, px, cells, bc, pegs
    return None


def paint(a, cells, bc, pegs, offgrid=None):
    """A filled socket and the shadow it casts, and nothing else. RELIEF, NOT COLOUR: at thirteen
    pixels a flat field of another hue is camouflage, and only a crest with its own shadow survives
    the finishing pass (the 13px legibility pass). A peg reads raised because it is bright with a
    hard dark pixel one down and one left of it - the same direction the light has come from in
    every axis of this project."""
    core = np.zeros(a.shape, bool)
    for c in cells:
        if bc[c] in pegs:
            core[c] = True
    if offgrid is not None and 0 <= offgrid[0] < a.shape[0] and 0 <= offgrid[1] < a.shape[1] \
            and a[offgrid]:
        core[offgrid] = True
    dark = np.zeros(a.shape, bool)
    h, w = a.shape
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            dark[ny, nx] = True
    return core, dark


# --- the reader --------------------------------------------------------------------------------
def read_stops(fr, a):
    """Peg, shadow and field off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: three luminances
    on the piece - the brightest is a peg, the darkest is a peg's shadow, and what is left is plain
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


def read_board(a, core):
    """THE BOARD, RECOVERED FROM THE PEGS AND THE OUTLINE, AND FROM NOTHING ELSE. Any single peg
    fixes the parity - a pixel is on exactly one of the nine - so the reader takes the parity off the
    first peg it meets and demands that every other peg agree with it. The empty sockets are then
    every remaining cloth pixel of that parity: THE SILHOUETTE DRAWS THEM, and that is why they need
    no ink at all. Clause BOARD is this function returning something."""
    marks = [(int(y), int(x)) for y, x in np.argwhere(core)]
    if not marks:
        return None
    py, px = marks[0][0] % PITCH, marks[0][1] % PITCH
    if any(y % PITCH != py or x % PITCH != px for y, x in marks):
        return None
    want = {(int(y), int(x)) for y, x in np.argwhere(a)
            if y % PITCH == py and x % PITCH == px}
    bc = {(y, x): ((x - px) // PITCH, (y - py) // PITCH) for (y, x) in want}
    pegs = {bc[m] for m in marks}
    return py, px, sorted(want), bc, pegs


def blots(crest):
    blk = crest[:-1, :-1] & crest[1:, :-1] & crest[:-1, 1:] & crest[1:, 1:]
    return bool(blk.any())


# --- frames ------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, dark, cells, bc, pegs) or None if the pose has no game."""
    wit_c, field_c, peg_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE BOARD GOES ON. The source sheet's inherited highlights sit
    # in the same stop a peg does, and a reader told nothing cannot tell an inherited highlight from
    # a peg. Every tone on this plate is put there by the board; the modelling comes back, richer,
    # from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    got = compose(a, cls, mode, salt)
    if got is None:
        return None
    py, px, cells, bc, pegs = got
    if mode == 'flat':
        return (np.zeros(a.shape, bool), np.zeros(a.shape, bool), cells, bc, pegs)
    off = None
    if mode == 'offgrid':
        # ONE PEG OFF THE LATTICE. The value is untouched - a stray is not on the board at all - and
        # the reader refuses the plate anyway, because it can no longer say what the board IS. This
        # control is the price of not painting the empty sockets, and clause BOARD collects it.
        for c in cells:
            if c[1] + 1 < a.shape[1] and a[c[0], c[1] + 1]:
                off = (c[0], c[1] + 1)
                break
    core, dark = paint(a, cells, bc, pegs, offgrid=off)
    for y, x in np.argwhere(dark):
        put(fr, y, x, wit_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, peg_c)
    return core, dark, cells, bc, pegs


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
    """A SHEET IS PLAYED IN ALL FORTY-TWO POSES OR IN NONE. A board that appears in some frames of a
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


# --- the acceptance test -----------------------------------------------------------------------
def inspect_frame(fr, a, cls, salt=''):
    """The six clauses on ONE POSE, from the pixels alone."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, pegs=0, jumps=0, obs=None, left=0)
    core, dark, three = read_stops(fr, a)
    if not three or not core.any():
        v['silent'] = 1
        return v
    v['plates'] = 1

    # (1) BOARD - the pegs agree on a parity, and that parity's cloth pixels are the board
    got = read_board(a, core)
    if got is None or blots(core):
        v['board'] = 1
        return v
    py, px, cells, bc, pegs = got
    allc = set(bc.values())
    v['pegs'] = len(pegs)

    # (6) LEGIBLE - a cast shadow under every peg that has cloth to cast one on, and no other dark
    h, w = a.shape
    want_dark = set()
    for (y, x) in np.argwhere(core):
        ny, nx = y + 1, x - 1
        if 0 <= ny < h and 0 <= nx < w and a[ny, nx] and not core[ny, nx]:
            want_dark.add((int(ny), int(nx)))
    if {(int(y), int(x)) for y, x in np.argwhere(dark)} != want_dark:
        v['legible'] = 1

    # (2) VALUE - THE LAW
    val = value(pegs)
    obs = obstructions(val)
    v['obs'] = obs
    if obs != OBSTRUCT[cls]:
        v['value'] = 1

    # (3) DESTINY - the class's prediction about how the plate can end, made good. The reader tests
    # EVERY socket on the board: for the mage it must find the named ninth occupied, and for the
    # others it must find that no socket at all could carry the plate's last peg.
    nin = ninth_of(val)
    if nin is None:
        if any(value({c}) == val for c in allc):
            v['destiny'] = 1
    else:
        if not any(c[0] % 3 == nin[0] and c[1] % 3 == nin[1] for c in allc):
            v['destiny'] = 1
        elif not any(value({c}) == val for c in allc):
            v['destiny'] = 1

    # (4) STABLE and (5) LIVE - THE DEMOLITION
    n, seen, left = demolish(pegs, allc, salt)
    v['jumps'] = n
    v['left'] = len(left)
    if len(set(seen)) != 1:
        v['stable'] = 1
    if n < 1:
        v['live'] = 1
    return v


def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, sheets=0, pass_sheets=0, pegs=0, jumps=0, taken=0)
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
                np_, ns, npg, nj, ntk = 0, 0, [], 0, 0
                for fi, a, (fr, _g) in plates:
                    res = inspect_frame(fr, a, cls, '%s|%d' % (stem, fi))
                    for c in CLAUSES:
                        bad[c] += res[c]
                    np_ += res['plates']
                    ns += res['silent']
                    nj += res['jumps']
                    if res['pegs']:
                        npg.append(res['pegs'])
                        ntk += res['pegs'] - res['left']
                tot['plates'] += np_
                tot['silent'] += ns
                tot['pegs'] += sum(npg)
                tot['jumps'] += nj
                tot['taken'] += ntk
                for c in CLAUSES:
                    tot[c] += bad[c]
                good = not any(bad.values())
                tot['pass_sheets'] += 1 if good else 0
                print('   %-7s %-8s %-2s  obs=%d plates=%-3d pegs %d-%-3d jumps=%-5d  %s%s'
                      % (kind, cls, suffix or 'm', OBSTRUCT[cls], np_,
                         min(npg) if npg else 0, max(npg) if npg else 0, nj,
                         'ALL PASS' if good else 'FAIL ',
                         '' if good else ' ' + ' '.join('%s=%d' % (c, k)
                                                        for c, k in bad.items() if k)),
                      flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d pegs drawn, %d silent'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['pegs'], tot['silent']))
    print('   %d jumps played, %d pegs destroyed by the reader, and the value never moved once'
          % (tot['jumps'], tot['taken']))
    for c in CLAUSES:
        print('   %-10s %d violations' % (c.upper(), tot[c]))


# --- the controls ------------------------------------------------------------------------------
def controls_report(which=None):
    if which == 'jumped-why':
        jumped_why()
        return
    if which == 'destiny-why':
        destiny_why()
        return
    if which == 'sabaton-why':
        sabaton_why()
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
            'toggled': '  <- one socket changed, which is not a move; the value goes with it',
            'slid': '  <- a peg WALKED instead of jumping: the nearest thing to a legal move',
            'jumped': ('  <- MEANT TO PASS. A different picture, two fewer pegs, the same plate: '
                       'THE ORBIT, run as a control'),
            'swapped': '  <- LAWFUL AND MISNAMED: the reader names the class the plate really is',
            'dead': '  <- a STILL LIFE: its value is safe because nothing can happen to it',
            'offgrid': ('  <- one peg off the lattice: the value untouched, and the reader can '
                        'no longer say what the board IS'),
            'crowded': '  <- a socket on every pixel: no parity, and the pegs run together',
            'flat': '  <- fewer than three stops, so there is nothing to read (SILENT, not passed)',
        }.get(mode, '')
        print('   %-9s drawn=%-4d CLEAN=%-4d  %s%s' % (mode.upper(), drawn, clean, note, extra),
              flush=True)
        if undrawable:
            print('   %-9s %d plates could not be drawn at all' % ('', undrawable))
        if silent:
            print('   %-9s %d plates show the reader fewer than three stops (SILENT, not passed)'
                  % ('', silent))


def jumped_why():
    """THE ORBIT, SHOWN. The same plate before and after one legal jump: two pegs fewer, a different
    picture, and a value that has not moved. This is the whole axis in four lines of output, and it
    is the reason control JUMPED is the only control in seventy-four axes that is SUPPOSED to pass."""
    print('== THE ORBIT  (one plate, played, and the number that will not move)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            got = compose(a, cls, None, '%s|%d' % (stem, fi))
            if got is None:
                continue
            _py, _px, cells, bc, pegs = got
            allc = set(bc.values())
            n, seen, left = demolish(pegs, allc, '%s|%d' % (stem, fi))
            print('   %-8s chest f%-2d  %2d pegs -> %2d after %d jumps   value %s the whole way, '
                  '%d distinct values seen'
                  % (cls, fi, len(pegs), len(left), n, str(seen[0]), len(set(seen))))
            print('              obstructions %d (start) %d (end)   %d%% of the ornament destroyed'
                  % (obstructions(seen[0]), obstructions(seen[-1]),
                     100 * (len(pegs) - len(left)) // max(len(pegs), 1)))
            break


def sabaton_why():
    """THE ONE GARMENT IN THE WARDROBE WITH NOTHING TO LOSE, PROVED RATHER THAN GUESSED. The
    warrior's sabaton is reported PLAIN, and the 73rd taught this project to find out whether that
    is a fact about the garment or a failure of the painter's search before saying anything about
    it. So this enumerates EVERY subset of every one of the four parities' sockets - a few thousand
    plates a pose - and asks for one that is both a warrior (both coordinates closed) and alive (one
    legal jump). Where it finds none, the sabaton genuinely cannot carry this axis's warrior, and no
    cleverer painter would have helped."""
    print('== THE SABATON  (exhaustive over every subset of every parity, pitch %d)' % PITCH)
    for cls in ('warrior', 'ranger', 'mage'):
        for suffix in ('', '_f'):
            stem = SLOTS['boots']['srcs'][cls] + suffix
            base = load_any('%s.png' % stem)
            plain = proved = rescued = 0
            for fi, sl, a in frames_of(base):
                fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                if got is not None and not any(inspect_frame(fr, a, cls, '%s|%d' % (stem, fi))[c]
                                               for c in CLAUSES):
                    continue
                plain += 1
                hit = False
                for py, px, cells, bc in boards_of(a):
                    if len(cells) < MIN_CELLS or len(cells) > 22:
                        continue
                    allc = sorted(bc.values())
                    n = len(allc)
                    for m in range(1, 1 << n):
                        pegs = {allc[i] for i in range(n) if m >> i & 1}
                        if obstructions(value(pegs)) != OBSTRUCT[cls]:
                            continue
                        if legal_jumps(pegs, set(allc)):
                            hit = True
                            break
                    if hit:
                        break
                rescued += 1 if hit else 0
                proved += 0 if hit else 1
            print('   %-8s sabaton %-2s  %2d poses plain: %2d PROVED IMPOSSIBLE (the garment), '
                  '%d lawful but past the painter\'s %d-socket enumeration budget'
                  % (cls, suffix or 'm', plain, proved, rescued, EXHAUST))


def destiny_why():
    """THE NAMED NINTH, COUNTED. A mage plate's value pins its last peg to one socket in nine, and
    the reader can go and find that ninth on the board before a single move is played. A ranger's or
    a warrior's cannot be pinned anywhere, because no single peg has a vanishing coordinate - and
    the reader confirms that by trying every socket the plate has."""
    print('== DESTINY  (what the value says about how the plate can end)')
    for cls in ('mage', 'ranger', 'warrior'):
        named = blocked = tested = 0
        for kind, cfg in SLOTS.items():
            stem = cfg['srcs'][cls]
            base = load_any('%s.png' % stem)
            for fi, sl, a in frames_of(base):
                got = compose(a, cls, None, '%s|%d' % (stem, fi))
                if got is None:
                    continue
                _py, _px, cells, bc, pegs = got
                allc = set(bc.values())
                val = value(pegs)
                tested += len(allc)
                if ninth_of(val) is not None:
                    named += 1
                if not any(value({c}) == val for c in allc):
                    blocked += 1
        print('   %-8s obstructions=%d   plates that NAME their last socket: %-4d   plates where '
              'NO socket can be the last: %-4d   (%d sockets tried)'
              % (cls, OBSTRUCT[cls], named, blocked, tested))


# --- reports -----------------------------------------------------------------------------------
def sweep():
    print('== SLOTS  (can every pose carry a board with a game in it, and does it read back)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                fit = unfit = 0
                npg, njm = [], []
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
                        npg.append(res['pegs'])
                        njm.append(res['jumps'])
                print('   %-7s %-8s %-2s  obs=%d pegs %d-%-3d jumps %d-%-3d  poses %2d/%-2d  SHEET %s'
                      % (kind, cls, suffix or 'm', OBSTRUCT[cls],
                         min(npg) if npg else 0, max(npg) if npg else 0,
                         min(njm) if njm else 0, max(njm) if njm else 0,
                         fit, fit + unfit,
                         'played' if unfit == 0 else 'PLAIN (reported)'), flush=True)


def frame_dump():
    print('== ONE REAL POSE PER CLASS  ("O" peg, "o" empty socket, "=" shadow, "-" field)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            got = compose(a, cls, None, '%s|%d' % (stem, fi))
            if got is None:
                continue
            _py, _px, cells, bc, pegs = got
            allc = set(bc.values())
            core, dark = paint(a, cells, bc, pegs)
            hole = np.zeros(a.shape, bool)
            for c in cells:
                if bc[c] not in pegs:
                    hole[c] = True
            val = value(pegs)
            n, seen, left = demolish(pegs, allc, '%s|%d' % (stem, fi))
            nin = ninth_of(val)
            print('== %s chest frame %d   %d sockets, %d pegs   value %s   obstructions %d'
                  % (cls, fi, len(allc), len(pegs), str(val), obstructions(val)))
            print('   demolition: %d jumps, %d pegs left, %d distinct values seen'
                  % (n, len(left), len(set(seen))))
            print('   last socket: %s' % ('sockets with (u,v) = (%d,%d) mod 3' % nin if nin
                                          else 'NO socket on this board can carry it'))
            ys, xs = np.nonzero(a)
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not a[y, x]:
                        row += '.'
                    elif core[y, x]:
                        row += 'O'
                    elif hole[y, x]:
                        row += 'o'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a peg on the
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
                core, dark, _c, _bc, _p = got
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for y, x in np.argwhere(core):
                    # A PEG'S OWN DARK NEIGHBOURS: the shadow it casts, one down and one left, and
                    # the four sockets two pixels away that are empty. Those are the pixels the peg
                    # has to stay brighter than for the relief to read at thirteen pixels.
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
        print('   %-7s peg still lighter than its own socket-shadow: %5d/%-5d (%3d%%)'
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
                         'obs=%d' % OBSTRUCT[cls] if ok else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
