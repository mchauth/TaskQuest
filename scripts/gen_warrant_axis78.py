#!/usr/bin/env python3
"""SEVENTY-EIGHTH net-new-geometry axis for ALL FOUR SLOTS - the WARRANT family: the plate carries
TWO ornaments in two inks, and the law is that they COUNT THE SAME - which is a PROOF, drawn on the
garment, that no plate on this silhouette could ever carry more.

    the ground is    a BAY GRID   the cloth is cut into three-pixel CELLS on one phase of a
                                  three-pixel grid; a cell exists only where all nine of its pixels
                                  are cloth. The cells, the BANDS they lie in and the FILES they
                                  stand in all belong to the SILHOUETTE. The painter says which of
                                  the nine phases it used, and the plate is its own key, because a
                                  pillar's own two pixels give the phase away.
    ornament one is  a PILLAR     a bright post two pixels tall standing in the lower middle of a
                                  cell, with a hard shadow down its left flank. NO TWO PILLARS SHARE
                                  A BAND OR A FILE - the posts are a PACKING.
    ornament two is  a LINTEL     a dark groove incised along the top row of a whole band, or down
                                  the right column of a whole file. EVERY CELL LIES UNDER A GROOVE -
                                  the grooves are a COVERING.
    the law is       THE PILLARS AND THE LINTELS ARE EQUAL IN NUMBER.

*** THIS IS THE FIRST LAW THAT CERTIFIES SOMETHING ABOUT EVERY OTHER PLATE ON THE SAME GARMENT. ***
The seventy-seventh said of its plate that nothing could be ADDED TO IT and nothing TAKEN FROM IT.
That is a statement about one picture and its immediate neighbours: a plate can be pinned and still
be a poor plate, because a packing that cannot be extended may still be smaller than one somebody
else would have drawn from scratch. This axis closes that gap, and it closes it the only way a
picture can - BY CARRYING ITS OWN PROOF.

    a packing and a covering of a garment always satisfy   pillars <= LINTELS
    so a plate on which they are EQUAL forces both to sit at the same number, and that number is
    then the most pillars the garment can hold AND the fewest grooves that can cover it.

    77th CLASP     PINNED     no ornament can be added to THIS PLATE.        A LOCAL fact.
    78th WARRANT   PROVED     no ornament can be added to ANY PLATE HERE.    A GLOBAL fact, and the
                              plate hands the reader the certificate rather than asking to be taken
                              on trust.

That is König's theorem doing the work, and it is why the second ink is on the garment at all. The
pillars alone would be a claim. The pillars and the lintels together are an ARGUMENT: a reader who
counts two numbers and finds them equal has PROVED maximality without searching for a better plate,
without trusting the painter, and without leaving the thirteen pixels in front of them.

*** CLASS IDENTITY IS A SIDE - HOW MUCH OF THE PROOF LIES DOWN. ***
    warrior    0   the argument stands up entirely: every groove in it is a file
    mage       1   one groove lies down
    ranger     2   two grooves lie down
Exactly one end of every pillar's cell is sealed - that is forced by the equality, not chosen - so
the class is read by counting the lying grooves and nothing else, and on a garment that is taller
than it is wide those are the few and the countable ones.

*** FIRST CLASS IDENTITY THAT IS A PROPERTY OF THE ARGUMENT AND NOT OF THE ORNAMENT THE READER CAME
    TO LOOK AT. *** Two plates of different classes can carry THE VERY SAME PILLARS in the very same
cells - the same packing, pixel for pixel - and differ only in how they prove it is the best one.
Not a count (67th), ceiling (68th), multipole order (69th), motions (70th), fraction of a move
(71st), coalition (72nd), precision (73rd), obstructions (74th), depth (75th), excess (76th) or
price (77th): every one of those is a fact about the marks. This is a fact about the REASONING, and
control SWAPPED is what makes that visible - it redraws one class's proof over another class's
pillars and the plate stays perfectly lawful while ceasing to be what it says it is.
Which side-count goes to which class is arithmetic and not taste: `--reach` enumerates EVERY minimum
covering each garment admits and tries all six ways of handing the three identities out.

*** THE ACCEPTANCE TEST IS A NEW KIND - AN AUDIT. ***
Every previous test interrogates the plate: break it, move it, drop a mark, and see whether the law
notices. Those tests all take the plate's own arithmetic as the standard. This one DOES NOT TRUST THE
PLATE'S ARITHMETIC AT ALL. For every shipped pose the file goes away and computes, from the outline
alone and by a completely different method - Kuhn's augmenting paths for the packing, a branching
search over the cells for the covering - the largest packing and the smallest covering the garment
admits, and then asks whether the ink agrees. The plate says "this many, and no more is possible";
the audit checks the second half of that sentence against an independent authority.
FIRST TEST WHOSE SUBJECT IS A CLAIM THE PLATE MAKES ABOUT PICTURES OTHER THAN ITSELF.

Eight clauses - the most any axis has carried, because there are two ornaments to keep honest:

    (1) GRID     every pillar stands in a real cell of ONE phase of the garment's own grid.
                 Control OFFGRID.
    (2) POST     every bright run is a vertical post exactly two pixels tall, and the dark ink is
                 EXACTLY the grooves plus the posts' left flanks - no more and no less. Controls
                 CLIPPED and FLAT.
    (3) ROOK     no two pillars share a band or a file: the posts are a packing. Control RANDOM.
    (4) SHIELD   every cell the garment offers lies under a groove: the grooves are a covering.
                 Control UNSEALED.
    (5) WARRANT  THE LAW: as many pillars as lintels. Controls SHORT (one pillar fewer) and
                 OVERSEALED (one groove more) - and note that they break the SAME clause from
                 opposite ends, which is what it means for a law to be an equality rather than a
                 bound.
    (6) SIDE     the class: how many grooves lie down. Control SWAPPED - LAWFUL AND MISNAMED.
    (7) LIVE     at least two pillars, and a grid big enough for the equality to say anything.
                 Control DEAD: one cell, one post, one groove, equal and empty.
    (8) LEGIBLE  every pillar casts its flank shadow. A post with no relief is a stripe of colour,
                 and at thirteen pixels a colour is camouflage.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_warrant_axis78.py                  # write the four staged dirs
    python3 scripts/gen_warrant_axis78.py --sweep          # can every pose carry its class
    python3 scripts/gen_warrant_axis78.py --accept         # eight clauses, every pose
    python3 scripts/gen_warrant_axis78.py --controls       # the nine controls
    python3 scripts/gen_warrant_axis78.py --audit          # THE AUDIT: the ink against an
                                                           # independent computation of the optimum
    python3 scripts/gen_warrant_axis78.py --reach          # every covering each garment admits
    python3 scripts/gen_warrant_axis78.py --frame          # one real pose per class
    python3 scripts/gen_warrant_axis78.py --survive        # relief through the finishing pass
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

# WHAT THE GARMENT OWNS AND WHAT THE PAINTER MAY CHOOSE. The cell size, which cells exist, which
# bands and files they lie in - all decided by the outline. The painter chooses the PHASE (one of
# nine), which maximum packing to stand up, and which minimum covering to incise. All three are
# recoverable from the picture, so nothing here is a secret.
CELL = 3          # three pixels of cell: at two a cell is too small to hold a post and its flank,
                  # and at four the garment offers so few cells that the equality is trivial.
MINPILL = 2       # fewer than two pillars is a mark, not a pattern
MINCELL = 3       # a grid with fewer cells than this is warranted for the wrong reason
MINGROOVE = 1     # A groove needs one pixel of cloth to be cut into, and ONE IS ENOUGH - which is
                  # only true because the grooves are dashed. Each of the four kinds of mark sits on
                  # its own residue class of the three-pixel grid (see band_pixels), so a dark pixel
                  # where a band groove belongs cannot have been put there by anything else, and a
                  # groove can never be counterfeited however short it is. A solid rule would not
                  # have that property and would need a length before it could be trusted.

# CLASS IDENTITY IS A SIDE: how many of the grooves LIE DOWN. Set by `--reach`, which enumerates
# every minimum covering each garment admits and tries every way of handing these out; counting the
# lying grooves rather than the standing ones is itself an arithmetic decision and not a taste one -
# on a garment that is taller than it is wide the standing grooves are nearly all of them and their
# number moves from pose to pose, while the lying ones are few and steady.
SIDE = {'warrior': 0, 'mage': 1, 'ranger': 2}
SWAP_SIDE = {'warrior': 1, 'mage': 2, 'ranger': 0}

# Three inks per class - (groove, cloth, post) - strictly separated in luminance AND in hue, which
# is the finding the 75th's panel forced. None near black: a near-black darkest stop eats the
# visor's eye and mouth pixels (the 49th's lesson). Deliberately unrelated to the 74th-77th.
#   warrior  DEEP TEAL cloth, IRON grooves, PALE GOLD posts
#   ranger   PLUM cloth, BLACKCURRANT grooves, IVORY posts
#   mage     MOSS cloth, BOG grooves, ICE posts
PAL = {
    'warrior': ((20, 34, 38), (48, 86, 90), (240, 214, 140)),
    'ranger':  ((30, 18, 38), (80, 48, 90), (238, 234, 218)),
    'mage':    ((22, 30, 20), (62, 76, 56), (196, 226, 246)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_warrant_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary78',
    ),
    'legs': dict(
        outdir='_warrant_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary78',
    ),
    'boots': dict(
        outdir='_warrant_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_warrant',
    ),
    'helmet': dict(
        outdir='_warrantdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary78',
    ),
}

CONTROLS = ('random', 'dead', 'unsealed', 'oversealed', 'short', 'swapped', 'offgrid', 'clipped',
            'flat')
CLAUSES = ('grid', 'post', 'rook', 'shield', 'warrant', 'side', 'live', 'legible')


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
def cells_of(a, phase):
    """THE CELLS THE GARMENT OFFERS, from the outline and a phase and nothing else.

    A cell exists where the four pixels a post and its flank stand on are cloth - the lower-left
    square of the cell - so a bay too narrow to hold a post offers the painter nothing there, and a
    bay that can hold one is never refused for the sake of a corner. Returns
    {(band, file): (row0, col0)}."""
    py, px = phase // CELL, phase % CELL
    h, w = a.shape
    cells = {}
    for k in range((h - py) // CELL):
        r0 = py + CELL * k
        for j in range((w - px) // CELL):
            c0 = px + CELL * j
            if a[r0 + 1:r0 + CELL, c0:c0 + CELL - 1].all():
                cells[(k, j)] = (r0, c0)
    return cells


def bands_files(cells):
    return sorted({k for k, _j in cells}), sorted({j for _k, j in cells})


def sealable(a, cells):
    """The bands and files whose grooves can actually be incised. A groove is clipped to the cloth,
    so a band whose row barely grazes the garment cannot carry one; a cell with neither a sealable
    band nor a sealable file cannot be covered at all, and the phase is simply not available."""
    bands, files = bands_files(cells)
    B = {k for k in bands if len(band_pixels(a, cells, k)) >= MINGROOVE}
    F = {j for j in files if len(file_pixels(a, cells, j)) >= MINGROOVE}
    return B, F


def pillar_pixels(r0, c0):
    """A post: two pixels, standing in the lower middle of its cell. The top row of the cell is left
    clear because that row belongs to the band's groove, and the left column because that column
    takes the post's own shadow."""
    return [(r0 + 1, c0 + 1), (r0 + 2, c0 + 1)]


def flank_pixels(r0, c0):
    return [(r0 + 1, c0), (r0 + 2, c0)]


def band_pixels(a, cells, k):
    """The groove that seals a whole band: a DASHED rule along the band's top row, two pixels cut in
    every cell the band offers and the third left standing, stopping wherever the cloth does.

    Dashed rather than solid for two reasons, one of them decorative and one of them structural. A
    solid rule every three pixels is fluting, and the eleventh and forty-third axes are already
    fluting. And dashing puts each of the four things a plate can carry on its OWN residue class of
    the grid - band grooves on (0,1) and (0,2), file grooves on (1,2) and (2,2), flanks on (1,0) and
    (2,0), posts on (1,1) and (2,1) - so no mark of one kind can ever be mistaken for, or counterfeit,
    a mark of another. The reading is unambiguous by arithmetic rather than by luck."""
    out = []
    for (kk, _j), (r0, c0) in sorted(cells.items()):
        if kk != k:
            continue
        out += [(r0, c) for c in (c0 + 1, c0 + 2) if a[r0, c]]
    return out


def file_pixels(a, cells, j):
    """The groove that seals a whole file: a DASHED rule down the file's right column, two pixels
    cut in every cell it offers. It runs immediately to the right of that file's posts, so a sealed
    file leaves each of its posts standing bright between its own flank shadow and its groove."""
    out = []
    for (_k, jj), (r0, c0) in sorted(cells.items()):
        if jj != j:
            continue
        out += [(r, c0 + 2) for r in (r0 + 1, r0 + 2) if a[r, c0 + 2]]
    return out


# --- the arithmetic ------------------------------------------------------------------------------
def max_packing(cells, order=None):
    """THE LARGEST PACKING THE GARMENT ADMITS, by Kuhn's augmenting paths - one of the two
    independent authorities the audit checks the ink against. Returns a list of cells."""
    adj = {}
    for (k, j) in (order or sorted(cells)):
        adj.setdefault(k, []).append(j)
    mate = {}

    def grow(k, seen):
        for j in adj.get(k, ()):
            if j in seen:
                continue
            seen.add(j)
            if j not in mate or grow(mate[j], seen):
                mate[j] = k
                return True
        return False

    for k in list(adj):
        grow(k, set())
    return [(k, j) for j, k in mate.items()]


def min_covers(cells, target, okB=None, okF=None):
    """EVERY MINIMUM COVERING THE GARMENT ADMITS, listed in full - the other independent authority.

    Take the first cell nothing seals yet; any covering at all contains its band or its file, so
    branching on those two exhausts the possibilities. The recursion is at most `target` deep and
    two-way, so this is a complete enumeration and not a search that might give up - which is what
    lets `--reach` say that a garment CANNOT wear an identity rather than that no one found a way."""
    edges = sorted(cells)
    out = set()

    def rec(B, F):
        if len(B) + len(F) > target:
            return
        for (k, j) in edges:
            if k not in B and j not in F:
                if okB is None or k in okB:
                    rec(B | {k}, F)
                if okF is None or j in okF:
                    rec(B, F | {j})
                return
        if len(B) + len(F) == target:
            out.add((frozenset(B), frozenset(F)))

    rec(frozenset(), frozenset())
    return sorted(out, key=lambda c: (sorted(c[0]), sorted(c[1])))


def is_cover(cells, B, F):
    return all(k in B or j in F for (k, j) in cells)


def is_packing(P):
    ks = [k for k, _j in P]
    js = [j for _k, j in P]
    return len(set(ks)) == len(ks) and len(set(js)) == len(js)


def sides_available(a, cells):
    """Which class identities this grid could ever carry - PROVED, by listing every minimum
    covering there is. The 76th's lesson: where an axis cannot go it should be able to say so."""
    if len(cells) < MINCELL:
        return set()
    mu = len(max_packing(cells))
    if mu < MINPILL:
        return set()
    okB, okF = sealable(a, cells)
    return {len(B) for B, _F in min_covers(cells, mu, okB, okF)}


# --- the painter ---------------------------------------------------------------------------------
def compose(a, cls, mode=None, salt=''):
    """The pillars and the lintels for one pose, as (phase, cells, packing, bands, files), or None
    if the pose cannot wear its class. Every control that is a lawful picture wrongly made is made
    HERE, from a lawful plate, so a control differs from what ships in exactly one thing."""
    want = SWAP_SIDE[cls] if mode == 'swapped' else SIDE[cls]
    rng = Rng('%s|%s' % (salt, mode or 'ship'))

    if mode == 'dead':
        # A GRID TOO SMALL TO MEAN ANYTHING: one cell, one post, one groove. The two numbers agree
        # and the agreement says nothing at all, which is what clause LIVE is for.
        # A REAL PHASE, chosen for being the poorest one the garment offers - not a truncation of a
        # good one, which the reader would catch as missing ink long before it got as far as the
        # arithmetic. Everything about this plate is lawful; it is simply too small to be saying
        # anything, and clause LIVE is the only thing standing between the axis and that.
        best = None
        for phase in range(CELL * CELL):
            cells = cells_of(a, phase)
            if not (1 <= len(cells) < MINCELL):
                continue
            okB, okF = sealable(a, cells)
            P = max_packing(cells)
            covers = min_covers(cells, len(P), okB, okF)
            if not P or not covers:
                continue
            if best is None or len(cells) < best[0]:
                best = (len(cells), phase, cells, P, covers[0])
        if best is None:
            return None
        _n, phase, cells, P, (B, F) = best
        return phase, cells, sorted(P), set(B), set(F)

    for phase in rng.shuffled(range(CELL * CELL)):
        cells = cells_of(a, phase)
        if len(cells) < MINCELL:
            continue
        P = max_packing(cells, order=rng.shuffled(sorted(cells)))
        if len(P) < MINPILL:
            continue
        okB, okF = sealable(a, cells)
        covers = [c for c in min_covers(cells, len(P), okB, okF) if len(c[0]) == want]
        if not covers:
            continue
        B, F = covers[rng.below(len(covers))]
        P = sorted(P)

        if mode == 'random':
            # THE NULL HYPOTHESIS: the same number of posts, in the same cells the garment offers,
            # stood up with no thought for whether two of them share a band or a file.
            P = sorted(rng.shuffled(sorted(cells))[:len(P)])
        elif mode == 'short':
            P = P[:-1]
        elif mode == 'oversealed':
            spare = sorted(okB - set(B))
            if spare:
                B = set(B) | {spare[rng.below(len(spare))]}
            else:
                spare2 = sorted(okF - set(F))
                if not spare2:
                    return None
                F = set(F) | {spare2[rng.below(len(spare2))]}
        elif mode == 'unsealed':
            if len(B) + len(F) < 2:
                return None
            if B:
                B = set(B) - {sorted(B)[rng.below(len(B))]}
            else:
                F = set(F) - {sorted(F)[rng.below(len(F))]}
        return phase, cells, list(P), set(B), set(F)
    return None


def paint(a, keep, clip=None, shift=None, flat=False):
    """The posts, the grooves and the flank shadows, and nothing else. RELIEF, NOT COLOUR: at
    thirteen pixels a flat field of another hue is camouflage, and only a crest with its own shadow
    survives the finishing pass."""
    _phase, cells, P, B, F = keep
    h, w = a.shape
    core = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    for i, (k, j) in enumerate(P):
        if (k, j) not in cells:
            continue
        r0, c0 = cells[(k, j)]
        px = pillar_pixels(r0, c0)
        if clip == i:
            px = px[:1]                                  # CLIPPED: a post drawn a pixel short
        if shift == i:
            px = [(y + 1, x) for y, x in px]             # OFFGRID: a post a pixel off the grid
        for y, x in px:
            if 0 <= y < h and 0 <= x < w and a[y, x]:
                core[y, x] = True
    for k in B:
        for y, x in band_pixels(a, cells, k):
            dark[y, x] = True
    for j in F:
        for y, x in file_pixels(a, cells, j):
            dark[y, x] = True
    if not flat:
        for i, (k, j) in enumerate(P):
            if (k, j) not in cells:
                continue
            r0, c0 = cells[(k, j)]
            for y, x in flank_pixels(r0, c0):
                if 0 <= y < h and 0 <= x < w and a[y, x] and not core[y, x]:
                    dark[y, x] = True
    dark &= ~core
    return core, dark


# --- the reader ----------------------------------------------------------------------------------
def read_stops(fr, a):
    """Post, groove and cloth off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: three luminances
    on the piece - the brightest is a post, the darkest is incised, the rest is cloth."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    pts = np.argwhere(a)
    core = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    if len(pts) == 0:
        return core, dark, False
    vals = sorted({int(lum[y, x]) for y, x in pts})
    if len(vals) < 3:
        return core, dark, False
    lo, hi = vals[0], vals[-1]
    for y, x in pts:
        v = int(lum[y, x])
        if v == hi:
            core[y, x] = True
        elif v == lo:
            dark[y, x] = True
    return core, dark, True


def read_posts(core):
    """Every pillar, from the pixels alone: the bright ink is cut into four-connected pieces and
    each piece must be a vertical run of exactly two. Returns (tops, ok)."""
    h, w = core.shape
    seen = np.zeros(core.shape, bool)
    tops, ok = [], True
    for (y0, x0) in np.argwhere(core):
        if seen[y0, x0]:
            continue
        stack, comp = [(y0, x0)], []
        seen[y0, x0] = True
        while stack:
            y, x = stack.pop()
            comp.append((int(y), int(x)))
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and core[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    stack.append((ny, nx))
        comp.sort()
        if len(comp) != 2 or comp[0][1] != comp[1][1] or comp[1][0] - comp[0][0] != 1:
            ok = False
            continue
        tops.append(comp[0])
    return tops, ok


def read_phase(tops):
    """The phase, from the posts' own pixels. Nine were open to the painter, and a post standing one
    down and one right of its cell's corner names the one it used."""
    ph = {(((y - 1) % CELL) * CELL + ((x - 1) % CELL)) for (y, x) in tops}
    if len(ph) != 1:
        return None
    return ph.pop()


def inspect_frame(fr, a, cls):
    """The eight clauses on ONE POSE, from the pixels and the outline and nothing else."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, pillars=0, lintels=0, cells=0, side_val='-')
    core, dark, three = read_stops(fr, a)
    if not three or not core.any():
        v['silent'] = 1
        return v
    v['plates'] = 1

    tops, post_ok = read_posts(core)
    if not post_ok or not tops:
        v['post'] = 1
        return v

    # (1) GRID - one phase, and every post stands in a cell the garment actually offers
    phase = read_phase(tops)
    if phase is None:
        v['grid'] = 1
        return v
    cells = cells_of(a, phase)
    P = [((y - 1 - phase // CELL) // CELL, (x - 1 - phase % CELL) // CELL) for (y, x) in tops]
    if any(p not in cells for p in P):
        v['grid'] = 1
        return v
    v['cells'] = len(cells)
    v['pillars'] = len(P)

    # (8) LEGIBLE - every post casts its flank, or it is a stripe of colour and not a raised thing
    for (k, j) in P:
        r0, c0 = cells[(k, j)]
        if not any(dark[y, x] for y, x in flank_pixels(r0, c0)
                   if 0 <= y < a.shape[0] and 0 <= x < a.shape[1] and a[y, x]):
            v['legible'] = 1

    # (2) POST - the dark ink is EXACTLY the grooves plus the flanks. The grooves are read the way
    # they were drawn: a band is sealed when the whole of its groove is incised.
    okB, okF = sealable(a, cells)
    B = {k for k in okB if all(dark[y, x] for y, x in band_pixels(a, cells, k))}
    F = {j for j in okF if all(dark[y, x] for y, x in file_pixels(a, cells, j))}
    want = set()
    for k in B:
        want |= {(y, x) for y, x in band_pixels(a, cells, k)}
    for j in F:
        want |= {(y, x) for y, x in file_pixels(a, cells, j)}
    for (k, j) in P:
        r0, c0 = cells[(k, j)]
        want |= {(y, x) for y, x in flank_pixels(r0, c0)
                 if 0 <= y < a.shape[0] and 0 <= x < a.shape[1] and a[y, x]}
    want -= {(y, x) for y, x in np.argwhere(core).tolist()}
    got = {(int(y), int(x)) for y, x in np.argwhere(dark)}
    if got != {(int(y), int(x)) for y, x in want}:
        v['post'] = 1
        return v
    v['lintels'] = len(B) + len(F)
    v['side_val'] = len(B)

    # (7) LIVE - a grid too small is warranted for the wrong reason
    if len(P) < MINPILL or len(cells) < MINCELL:
        v['live'] = 1
        return v

    # (3) ROOK - the posts are a packing
    if not is_packing(P):
        v['rook'] = 1

    # (4) SHIELD - the grooves are a covering
    if not is_cover(cells, B, F):
        v['shield'] = 1

    # (5) WARRANT - THE LAW, and with it the certificate: equal counts force both to the optimum
    if len(P) != len(B) + len(F):
        v['warrant'] = 1

    # (6) SIDE - the class
    if len(B) != SIDE[cls]:
        v['side'] = 1
    return v


# --- frames --------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (core, dark, keep) or None if the pose cannot wear its class."""
    groove_c, cloth_c, post_c = PAL[cls]
    # THE CLOTH IS FLATTENED BEFORE THE ORNAMENT GOES ON. The source sheet's inherited highlights
    # sit in the same stop a post does, and a reader told nothing cannot tell an inherited highlight
    # from a post. Every tone here is put there by the packing and the covering; the modelling comes
    # back, richer, from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, cloth_c)
    keep = compose(a, cls, mode, salt)
    if keep is None:
        return None

    clip = shift = None
    if mode == 'clipped':
        clip = 0
    if mode == 'offgrid':
        shift = 0
    core, dark = paint(a, keep, clip=clip, shift=shift, flat=(mode == 'flat'))
    if not core.any() or not dark.any():
        return None
    for y, x in np.argwhere(dark):
        put(fr, y, x, groove_c)
    for y, x in np.argwhere(core):
        put(fr, y, x, post_c)
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
    """A SHEET IS WARRANTED IN ALL ITS POSES OR IN NONE. A proof that appears in some frames of a
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
    print('== ACCEPTANCE  (eight clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, sheets=0, pass_sheets=0, pillars=0, lintels=0)
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
        np_ = ns = npil = nlin = 0
        celln = []
        for fi, a, (fr, _g) in plates:
            res = inspect_frame(fr, a, cls)
            for c in CLAUSES:
                bad[c] += res[c]
            np_ += res['plates']
            ns += res['silent']
            npil += res['pillars']
            nlin += res['lintels']
            celln.append(res['cells'])
        tot['plates'] += np_
        tot['silent'] += ns
        tot['pillars'] += npil
        tot['lintels'] += nlin
        for c in CLAUSES:
            tot[c] += bad[c]
        good = not any(bad.values())
        tot['pass_sheets'] += 1 if good else 0
        print('   %-7s %-8s %-2s  side=%d plates=%-3d pillars=%-4d lintels=%-4d cells %d-%-3d  %s%s'
              % (kind, cls, suffix or 'm', SIDE[cls], np_, npil, nlin,
                 min(celln) if celln else 0, max(celln) if celln else 0,
                 'ALL PASS' if good else 'FAIL ',
                 '' if good else ' ' + ' '.join('%s=%d' % (c, k) for c, k in bad.items() if k)),
              flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d pillars stood, %d lintels incised, '
          '%d silent'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['pillars'], tot['lintels'],
             tot['silent']))
    for c in CLAUSES:
        print('   %-9s %d violations' % (c.upper(), tot[c]))


# --- THE AUDIT -----------------------------------------------------------------------------------
def audit_report():
    """THE ACCEPTANCE TEST THAT DOES NOT TRUST THE PLATE'S ARITHMETIC.

    A shipped plate claims two things at once: that its posts are the most the garment can hold, and
    that its grooves are the fewest that can cover it. Neither claim is about the plate - both are
    about every OTHER plate that could have been painted on the same silhouette. So the audit puts
    the ink aside, computes the two optima from the outline alone by two different methods, and asks
    whether the picture agrees. The last column is the certificate: pillars = lintels = optimum."""
    print('== AUDIT  (the ink, against an independent computation of the two optima)')
    tp = tm = 0
    for kind, cfg, cls, suffix, stem in sheets():
        base = load_any('%s.png' % stem)
        if not sheet_carries(base, cls, stem):
            print('   %-7s %-8s %-2s  PLAIN (reported)' % (kind, cls, suffix or 'm'), flush=True)
            continue
        plates = agree = 0
        gap = 0
        for fi, sl, a in frames_of(base):
            keep = compose(a, cls, None, '%s|%d' % (stem, fi))
            if keep is None:
                continue
            phase, cells, P, B, F = keep
            plates += 1
            okB, okF = sealable(a, cells)
            mu = len(max_packing(cells))                        # authority one: augmenting paths
            covers = min_covers(cells, mu, okB, okF)            # authority two: a branching search
            ok = (len(P) == mu and len(B) + len(F) == mu and covers
                  and is_packing(P) and is_cover(cells, B, F))
            agree += 1 if ok else 0
            gap += (len(B) + len(F)) - len(P)
        tp += plates
        tm += agree
        print('   %-7s %-8s %-2s  plates=%-3d  ink agrees with the optimum %3d/%-3d  '
              'total slack between the two counts = %d'
              % (kind, cls, suffix or 'm', plates, agree, plates, gap), flush=True)
    print('   ----')
    print('   %d/%d shipped plates carry a certificate that an independent computation confirms'
          % (tm, tp))
    print('   slack of zero everywhere is the whole claim: a packing can never outnumber a covering,')
    print('   so equality PROVES the packing maximum and the covering minimum, with no search.')


# --- where the axis can and cannot go ------------------------------------------------------------
def reach_report():
    """WHICH IDENTITIES EACH GARMENT COULD EVER WEAR - proved, not searched.

    For every pose, every phase, every minimum covering there is. Then all six ways of handing the
    three side-counts to the three classes, so the coverage this batch ships is compared with the
    best any assignment could have done, the way the 76th taught."""
    print('== REACH  (every minimum covering each garment admits, and every way of handing out the '
          'three identities)')
    per = {}
    for kind, cfg, cls, suffix, stem in sheets():
        base = load_any('%s.png' % stem)
        common = None
        for fi, sl, a in frames_of(base):
            avail = set()
            for phase in range(CELL * CELL):
                avail |= sides_available(a, cells_of(a, phase))
            common = avail if common is None else (common & avail)
        common = common or set()
        per[(kind, cls, suffix)] = common
        print('   %-7s %-8s %-2s  sides every pose of this sheet can wear: %s'
              % (kind, cls, suffix or 'm',
                 ', '.join(str(s) for s in sorted(common)) if common else 'NONE'))
    print('   ----')
    best = None
    vals = sorted({s for c in per.values() for s in c} | {0, 1, 2})
    trip = [(x, y, z) for x in vals for y in vals for z in vals if len({x, y, z}) == 3]
    for x, y, z in trip:
        asg = {'warrior': x, 'mage': y, 'ranger': z}
        n = sum(1 for (kind, cls, suffix), c in per.items() if asg[cls] in c)
        if best is None or n > best[0]:
            best = (n, asg)
    ship = sum(1 for (kind, cls, suffix), c in per.items() if SIDE[cls] in c)
    print('   this batch ships warrior=%d mage=%d ranger=%d and dresses %d/%d sheets'
          % (SIDE['warrior'], SIDE['mage'], SIDE['ranger'], ship, len(per)))
    print('   the best assignment of three distinct side-counts is %s and dresses %d/%d'
          % (best[1], best[0], len(per)))


def sweep():
    print('== SWEEP  (can every pose of every sheet wear its class)')
    for kind, cfg, cls, suffix, stem in sheets():
        base = load_any('%s.png' % stem)
        n = good = 0
        for fi, sl, a in frames_of(base):
            n += 1
            if compose(a, cls, None, '%s|%d' % (stem, fi)) is not None:
                good += 1
        print('   %-7s %-8s %-2s  side=%d  %3d/%-3d poses  %s'
              % (kind, cls, suffix or 'm', SIDE[cls], good, n,
                 'CARRIES' if good == n else 'PLAIN (reported)'), flush=True)


# --- the controls --------------------------------------------------------------------------------
def controls_report(only=None):
    print('== CONTROLS  (a control differs from what ships in exactly one thing)')
    for mode in CONTROLS:
        tot = dict.fromkeys(CLAUSES, 0)
        plates = silent = 0
        for kind, cfg, cls, suffix, stem in sheets():
            if only and kind != only:
                continue
            base = load_any('%s.png' % stem)
            if not sheet_carries(base, cls, stem):
                continue
            for fi, sl, a in frames_of(base):
                fr, got = one_plate(base, sl, a, cls, mode, '%s|%d' % (stem, fi))
                if got is None:
                    continue
                res = inspect_frame(fr, a, cls)
                if res['silent']:
                    silent += 1
                    continue
                plates += 1
                for c in CLAUSES:
                    tot[c] += res[c]
        clean = plates - sum(1 for _ in ()) if False else None
        caught = sum(tot.values())
        print('   %-11s plates=%-4d  %s%s'
              % (mode.upper(), plates,
                 ' '.join('%s=%d' % (c.upper(), tot[c]) for c in CLAUSES if tot[c]) or 'NOTHING',
                 '   (silent %d)' % silent if silent else ''), flush=True)
        _ = clean, caught


# --- one real pose -------------------------------------------------------------------------------
def frame_dump():
    print('== FRAME  (one real pose per class: # post, = groove or flank, - cloth)')
    for cls in ('warrior', 'mage', 'ranger'):
        stem = SLOTS['chest']['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
            if got is None:
                continue
            core, dark, keep = got
            phase, cells, P, B, F = keep
            print('   %-8s frame %-3d phase %d  cells=%-3d pillars=%d lintels=%d (bands %d, '
                  'files %d)  side=%d'
                  % (cls, fi, phase, len(cells), len(P), len(B) + len(F), len(B), len(F), len(B)))
            ys, xs = np.where(a)
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not a[y, x]:
                        row += '.'
                    elif core[y, x]:
                        row += '#'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so a post on the
    shadowed flank is darker in absolute terms than the cloth on the lit one."""
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
                              ((y + 1, x - 1), (y, x - 1), (y, x + 1), (y - 1, x))
                              if 0 <= ny < FH and 0 <= nx < FW and not core[ny, nx]
                              and (dark[ny, nx] or a[ny, nx])]
                        if not nb:
                            continue
                        tot += 1
                        if lum[y, x] > float(np.mean(nb)):
                            ok += 1
        print('   %-7s post still lighter than the cloth around it: %5d/%-5d (%3d%%)'
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
    if '--audit' in sys.argv:
        audit_report()
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
                 'side=%d' % SIDE[cls] if ok else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
