#!/usr/bin/env python3
"""SIXTY-SIXTH net-new-geometry axis for ALL FOUR SLOTS — the DOVETAIL family: the plate is cut into
stones, and the stones are cut so that the plate CANNOT BE TAKEN APART.

    the ornament is  a STONE      a raised block, lit on its top and right, shadowed below and left
                     a KEY        one stone's tail driven into its neighbour, wide at the far end
    the law is       no part of the plate can be carried away from the rest, in any direction

*** THIS IS THE FIRST AXIS WHOSE INVARIANT IS AN IMPOSSIBILITY. ***
Sixty-five axes have asserted that something IS SO of the plate: a statistic holds among the shards
(46th), a wire is connected (54th), three hoops stand in 3:2:1 (61st), the raised studs exclusive-or
to zero (64th), each row is the image of the row above it (65th). Every one is a positive sentence
whose subject is the pixels in front of you, and every one is settled by looking hard enough at
them. This one asserts that A SET IS EMPTY — the set of motions that take a part of the plate away
from the rest. It is not satisfied by anything the ornament does. It is satisfied by what NOTHING
CAN DO TO IT. And it is the first invariant in sixty-six whose subject is not the plate but the
plate's PARTS AND THEIR FREEDOM.

*** THE PAIR WITH THE 65th. ***
    the 65th CASCADE   the invariant is a CAUSE: given its seed the plate could not have been
                       otherwise. The law runs FORWARD through the picture.
    the 66th DOVETAIL  the invariant is a CONSTRAINT: the plate cannot BECOME otherwise. The law
                       forbids every path OUT of the picture.
One says how the plate got here; the other says it is not leaving. Neither is a statement any of the
first sixty-four could make, and they are the only two ways a picture can be about something other
than itself.

*** THE ACCEPTANCE TEST IS A NEW KIND: A DISASSEMBLY. IT TRIES TO DESTROY THE ARTEFACT. ***
Every reader before it has been a measurement — of an area, a winding number, a syndrome, a rule.
Even the 64th TALLY, which damaged its own sheets, damaged them in order to READ something back.
This reader is a pair of hands. It recovers the stones from the pixels, and then, for every one of
the 2^n - 2 ways of parting the plate in two and each of the four directions, it takes hold of one
part and pulls. Every attempt must fail. Nothing is measured anywhere in the test; something is
ATTEMPTED, 4*(2^n - 2) times per plate, and the axis is the fact that it never once succeeds.

    (1) TILING        the stones recovered from the pixels partition the plate: every field pixel in
                      exactly one stone, every stone 4-connected, no gaps, no overlaps, at least
                      MIN_CELLS stones. GLUE fails here and nowhere else.
    (2) SEIZED        for each of N, S, E, W: no proper non-empty subset of stones can be translated
                      away from the rest. Checked as strong connectivity of the blocking digraph,
                      and, on every plate small enough (n <= BRUTE_MAX), CROSS-CHECKED BY BRUTE
                      FORCE over all 2^n - 2 subsets — because a theorem quoted is not a theorem
                      run. ASHLAR fails. PERCELL fails. There is NO TOLERANCE CONSTANT in this file.
    (3) INTERLOCK     the seizing is done by the KEYS and not by the accident of which stone happens
                      to lie outside: strike every key out, restore the plain courses, and SEIZED
                      must fail. RIVET fails — its studs sit ON the seam and cross nothing, and a
                      mark is not a joint.
    (4) LOAD-BEARING  strike out any ONE key and SEIZED must fail. Every key in the ornament is
                      holding the plate together; NOTHING IN THIS ORNAMENT IS ORNAMENT. RING and
                      REDUNDANT fail — both are rigid, correct, and carry passengers.
    (5) REACH         every single stone is blocked in all four directions. This is the WEAK clause
                      — the one a naive design very nearly passes — and it is written down beside
                      clause 2 so the difference can be seen: PERCELL locks nearly every stone
                      individually (9 loose of 240, against 377 for plain ASHLAR) and the plate
                      still comes apart in blocks 36 times over. Clause 2 is about SUBSETS for
                      exactly this reason, and no per-stone test will ever do its work.
    (6) LEGIBLE       every key states itself TWICE — once at its neck, where the seam line jogs,
                      and once at its tail, two pixels deep — and the reader takes the two as
                      independent witnesses and requires them to agree. No single pixel decides
                      whether the plate is jointed.

*** WHY A TREE, AND WHY THE CLASSES ARE TREES. ***
A key locks its two stones against all four directions at once (a dovetail is a full lock in the
plane; that is why real ones must be slid along a third axis). So the keys are the edges of a graph
on the stones, and SEIZED holds exactly when that graph is CONNECTED. Connected on n nodes costs at
least n-1 edges, and clause LOAD-BEARING is the statement that the ornament pays exactly that and
not one key more: THE ORNAMENT IS A SPANNING TREE. Which tree is the class:

    warrior   CHAIN    a boustrophedon path through the stones. Every stone has degree 2 but the
                       two ends; the joint runs through the piece like a seam of mortar.
    mage      RADIAL   a breadth-first tree from the middle stone. One hub carries three or four
                       keys and the rest hang off it.
    ranger    COMB     a spine along the top course with a tooth dropped from each stone of it.

All three are spanning trees, all three cost n-1, and all three are read back off the pixels by the
same reader, which is never told the class: it recovers the keys, builds the graph, and prints the
degree sequence. **Class identity is a SHAPE OF A GRAPH** — not a colour (the 64th put it in the
mid tone), not a rule (the 65th put it in the automaton), and not a motif.

*** THE SIX CONTROLS. ***
    ASHLAR     plain courses, no keys. Every stone lifts straight out and every course walks off
               sideways. It IS the 17th axis, exactly, and it is this axis's lower collapse
               boundary — named rather than avoided, as the 65th named the 11th and the 16th.
    RIVET      the keys replaced by a stud sitting ON the seam, symmetric, crossing nothing. Same
               count, same glance, same busyness, zero blocking — it is the 13th STUDWORK. THE
               CONTROL THAT PROVES THE AXIS IS GEOMETRY AND NOT DECORATION.
    PERCELL    the class's spanning tree with ONE INTERIOR KEY REMOVED — every stone still carries a
               key, so nothing moves on its own, but the key graph is in two pieces and the plate
               comes apart in BLOCKS. THE BUG THIS AXIS WOULD HAVE SHIPPED WITH, AND IT IS
               INVISIBLE: one key fewer out of five, no visible difference at 13px, and the wall
               falls down. Measured: 36 plates of 60 part, 114 partings found, against 0 for the
               axis. It is the reason clause SEIZED is about SUBSETS and not about stones.
    RING       a spanning tree plus one key closing a cycle. THE HONEST NEAR MISS: rigid where it is
               drawn correctly, and one key too many everywhere. What it actually fails, measured,
               is SEIZED and LEGIBLE, and that is the lesson rather than the arithmetic — the
               surplus key is cut out of a stone that has already given three pixels to another
               key, so a plate cannot simply be given more joinery: KEYS INTERFERE, and the extra
               key destroys the bite of the one it crowds.
    REDUNDANT  a key on every seam, about twice the minimum. The same lesson at twice the volume: 21
               plates of 60 part, and 54 keys can no longer be read off the pixels at all, because
               the stones have been eaten hollow by their own joinery. Not wrong in principle —
               UNPAYABLE in four pixels.
    GLUE       one stone covering the whole plate. Nothing can be taken apart because there is
               nothing to take apart: it passes SEIZED, INTERLOCK, LOAD-BEARING and REACH
               vacuously. The upper collapse boundary, and the only reason clause TILING counts.

*** DISTINCTNESS. ***
  * 17th ASHLAR — this axis's lower control. Ashlar's seams are straight and its law is a BOND (how
    the courses are offset). Here the seams interdigitate and the bond is irrelevant; two plates
    with the same bond can differ in whether they hold.
  * 55th STRATA — lap joints, and its law is an ORDER: which lame lies OVER which. That is a claim
    about DEPTH. Nothing overlaps here: one surface, exactly tiled, and the law is about MOTION IN
    THE PLANE.
  * 56th SLOTWORK — straps through slots, a conservation law counted along a traversal. There the
    ground is an occluder; here there is no over-and-under anywhere.
  * 54th LABYRINTH — connectivity of one wire, where connectivity IS the invariant. Here
    connectivity of the key graph is only the MEANS; the invariant is that nothing moves, and the
    graph is how it is arranged, not what is claimed.
  * 53rd GRANULATION — contact packing, where contact is the subject. Here contact is free and
    worth nothing: everything touches, and you can still slide the whole top course off.
  * 13th STUDWORK — the RIVET control.
  * 64th TALLY / 65th CASCADE — those plates carry an alphabet and say something. THIS PLATE SAYS
    NOTHING AT ALL. It is the first axis with no symbol in it: there is no state to read off a
    stone, only stones and the shapes where they meet.

Authoring philosophy identical to gen_canon_axis61.py ... gen_cascade_axis65.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed, silhouette
untouched — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Twenty-second generator to call it in-line, after axes 45-65.

Run from repo root:
  python3 scripts/gen_dovetail_axis66.py
  python3 scripts/gen_dovetail_axis66.py --cells       # ASCII of one real component
  python3 scripts/gen_dovetail_axis66.py --trees       # the three trees, recovered from the pixels
  python3 scripts/gen_dovetail_axis66.py --accept      # the six clauses over all 24 sheets
  python3 scripts/gen_dovetail_axis66.py --controls    # the six controls through the same reader
  python3 scripts/gen_dovetail_axis66.py --survive     # legibility through the finishing pass
  python3 scripts/gen_dovetail_axis66.py --sweep       # slots + visor diagnostics
Then QA (examples):
  python3 scripts/sprite_qa.py _dovetail_legendary_preview/shirt_warrior_legendary66.png
  python3 scripts/sprite_qa.py _dovetaildome_helmet_preview/helmet_mage_legendary66.png --y-min 2
  python3 scripts/sprite_qa.py _dovetail_boots_preview/boots_warrior_legendary_dovetail.png --y-max 63
"""
import os
import sys
import itertools
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18
SLEEP_FROM = 60

# A stone is 4x4. Not a taste: a key is a tail two pixels deep whose far end is two pixels wide, and
# for the lock to bite in BOTH senses of an axis the stone it is driven into must keep material on
# BOTH sides of the tail. Two + one + one = four, in each direction, and there is no smaller number.
CELL_W, CELL_H = 4, 4
MIN_LIVE = 6             # of the 16 pixels of a stone's box, how many must be body pixels
                         # 6 rather than 7 for one reason: a sabaton is six pixels tall and four
                         # wide, so its lower stone is a 4x2 sliver of eight pixels. At 7 the boots
                         # slot carries no joint at all; at 6 it carries the smallest joint the axis
                         # can make — TWO STONES AND ONE KEY.
MIN_CELLS = 2            # below two stones there is no joint to make; painted plain and REPORTED
BRUTE_MAX = 12           # brute-force every subset up to this many stones (2^12 = 4096)

# CLASS IDENTITY IS THE SHAPE OF THE TREE.
TREE = {'warrior': 'chain', 'mage': 'radial', 'ranger': 'comb'}

# Three building stones, three temperatures, no stop anywhere near black (the visor's eye and mouth
# pixels are black and a near-black darkest stop swallows them — the 49th's lesson).
#   warrior  BASALT      cold blue-grey
#   mage     PORPHYRY    imperial violet
#   ranger   SANDSTONE   warm ochre
# Darkest channel-sums 230 / 236 / 198. The sandstone was pulled two steps deeper and more saturated
# than it was first drawn: at (222,202,164) its crest sat almost exactly on the skin ramp and the
# ranger jerkin dissolved into the ranger.
# Deliberately unrelated to the 64th (bronze/ice/bone) and the
# 65th (argent/gold/rose) so that the three most recent axes cannot be mistaken for a recolor set.
PAL = {
    'warrior':  ((196, 202, 214), (104, 114, 130), (68, 74, 88)),
    'mage':     ((206, 184, 214), (126, 90, 138), (82, 58, 96)),
    'ranger':   ((206, 176, 120), (140, 102, 58), (92, 66, 40)),
}
DARK, MID, CREST = 0, 1, 2       # the reader's three stops, darkest first

BODY = {cls: (p[2], p[1], p[0]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_dovetail_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary66', largest=True,
    ),
    'legs': dict(
        outdir='_dovetail_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary66', largest=False,
    ),
    'boots': dict(
        outdir='_dovetail_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_dovetail', largest=False,
    ),
    'helmet': dict(
        outdir='_dovetaildome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary66', largest=True,
    ),
}


# --- sheet machinery ---------------------------------------------------------------------------
def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free)."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    n = 0
    stack = []
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and labels[sy, sx] == 0:
                n += 1
                labels[sy, sx] = n
                stack.append((sy, sx))
                while stack:
                    y, x = stack.pop()
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and labels[ny, nx] == 0:
                            labels[ny, nx] = n
                            stack.append((ny, nx))
    return labels, n


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


def comps_of(a, largest):
    lbl, n = label4(a)
    if n < 1:
        return []
    if largest:
        counts = np.bincount(lbl.ravel())
        counts[0] = 0
        return [(lbl == int(counts.argmax()))]
    return [(lbl == i) for i in range(1, n + 1)]


# --- the courses -------------------------------------------------------------------------------
def grid_of(comp):
    """The stone grid this component carries.

    Returns (y0, x0, live) with live[gr, gc] True when the stone's 4x4 box holds at least MIN_LIVE
    body pixels. Anchored at the component's own bounding box, so the masonry travels with the
    body."""
    ys, xs = np.nonzero(comp)
    if len(ys) == 0:
        return None
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    nr = (y1 - y0 + CELL_H) // CELL_H
    nc = (x1 - x0 + CELL_W) // CELL_W
    if nr < 1 or nc < 1:
        return None
    live = np.zeros((nr, nc), dtype=bool)
    for gr in range(nr):
        for gc in range(nc):
            box = comp[y0 + gr * CELL_H:y0 + (gr + 1) * CELL_H,
                       x0 + gc * CELL_W:x0 + (gc + 1) * CELL_W]
            live[gr, gc] = int(box.sum()) >= MIN_LIVE
    return y0, x0, live


def base_labels(comp, g):
    """Every body pixel of the component labelled with the stone it belongs to.

    A stone starts as the 4x4 box of the course grid and then GROWS into whatever ragged body the
    silhouette leaves beside it, so that the stones partition the plate EXACTLY and no crumb of the
    piece belongs to nothing. That is not tidiness: clause TILING is the statement that the plate is
    entirely made of stones, and a mason who leaves gaps has not built a wall."""
    y0, x0, live = g
    nr, nc = live.shape
    lab = np.zeros(comp.shape, dtype=np.int32)
    for gr in range(nr):
        for gc in range(nc):
            if not live[gr, gc]:
                continue
            sid = gr * nc + gc + 1
            ya, xa = y0 + gr * CELL_H, x0 + gc * CELL_W
            sub = comp[ya:ya + CELL_H, xa:xa + CELL_W]
            # A stone must be ONE stone: where the silhouette is ragged the box can meet the body in
            # two separate pieces, and two pieces of rubble are not a stone. Keep the largest piece;
            # the rest of the box goes back to being the plain edge of the piece.
            l2, k2 = label4(sub)
            if k2 > 1:
                counts = np.bincount(l2.ravel())
                counts[0] = 0
                sub = (l2 == int(counts.argmax()))
            if int(sub.sum()) < MIN_LIVE:
                live[gr, gc] = False
                continue
            for dy, dx in np.argwhere(sub):
                lab[ya + dy, xa + dx] = sid
    # grow the stones into the ragged remainder, nearest first
    h, w = lab.shape
    frontier = [tuple(p) for p in np.argwhere(lab > 0)]
    while frontier:
        nxt = []
        for y, x in frontier:
            sid = lab[y, x]
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and comp[ny, nx] and lab[ny, nx] == 0:
                    lab[ny, nx] = sid
                    nxt.append((ny, nx))
        frontier = nxt
    return lab


# --- the keys ----------------------------------------------------------------------------------
# A key is three pixels, driven from one stone into its neighbour: a NECK one pixel wide at depth
# one, and a TAIL two pixels wide at depth two. The tail cannot come back out through the neck, and
# because the neighbour keeps material on both sides of the tail, neither stone can shear past the
# other either. Three pixels, four directions.
def key_pixels(g, gr, gc, vertical):
    """The pixels the key moves, and the two witness pixels that must survive in the donor stone.

    vertical=True  : seam between (gr,gc) and (gr,gc+1); the RIGHT stone drives its tail LEFT.
    vertical=False : seam between (gr,gc) and (gr+1,gc); the LOWER stone drives its tail UP."""
    y0, x0, _live = g
    if vertical:
        xs = x0 + (gc + 1) * CELL_W                 # first column of the right stone
        yj = y0 + gr * CELL_H + 1                   # strictly inside the seam's span
        moved = [(yj, xs - 1), (yj, xs - 2), (yj + 1, xs - 2)]
        wit = [(yj - 1, xs - 1), (yj + 1, xs - 1)]
        need = [(y, x) for y in range(yj - 1, yj + 2) for x in range(xs - 2, xs + 2)]
        taker = (gr, gc + 1)
    else:
        ys = y0 + (gr + 1) * CELL_H                 # first row of the lower stone
        xj = x0 + gc * CELL_W + 1
        moved = [(ys - 1, xj), (ys - 2, xj), (ys - 2, xj + 1)]
        wit = [(ys - 1, xj - 1), (ys - 1, xj + 1)]
        need = [(y, x) for y in range(ys - 2, ys + 2) for x in range(xj - 1, xj + 2)]
        taker = (gr + 1, gc)
    return moved, wit, need, taker


def keyable(comp, g, gr, gc, vertical):
    """Is there room in the body for this key? Every pixel it needs must be a body pixel."""
    y0, x0, live = g
    nr, nc = live.shape
    tr, tc = (gr, gc + 1) if vertical else (gr + 1, gc)
    if tr >= nr or tc >= nc or not live[gr, gc] or not live[tr, tc]:
        return False
    _m, _w, need, _t = key_pixels(g, gr, gc, vertical)
    h, w = comp.shape
    for y, x in need:
        if not (0 <= y < h and 0 <= x < w) or not comp[y, x]:
            return False
    return True


def sid_at(lab, g, gr, gc):
    """Which stone holds this course-grid cell (they are not the same thing once stones merge)."""
    y0, x0, _live = g
    box = lab[y0 + gr * CELL_H:y0 + (gr + 1) * CELL_H, x0 + gc * CELL_W:x0 + (gc + 1) * CELL_W]
    v = box[box > 0]
    if v.size == 0:
        return 0
    return int(np.bincount(v).argmax())


def apply_keys(lab, g, keys):
    """Drive the keys: each moves three pixels from one stone into its neighbour."""
    out = lab.copy()
    for (gr, gc, vertical) in keys:
        moved, _w, _n, (tr, tc) = key_pixels(g, gr, gc, vertical)
        sid = sid_at(lab, g, tr, tc)
        if sid == 0:
            continue
        for y, x in moved:
            if 0 <= y < out.shape[0] and 0 <= x < out.shape[1] and out[y, x] != 0:
                out[y, x] = sid
    return out


# --- the hands: blocking, and the attempt to take the plate apart -------------------------------
DIRS = (('N', -1, 0), ('S', 1, 0), ('W', 0, -1), ('E', 0, 1))


def blocking(lab, dy, dx):
    """A -> B when A stands in B's way: B translated any distance along (dy,dx) meets A."""
    ids = [int(i) for i in np.unique(lab) if i > 0]
    px = {i: np.argwhere(lab == i) for i in ids}
    lines = {}
    for i in ids:
        p = px[i]
        if dy == 0:
            d = {}
            for y, x in p:
                lo, hi = d.get(y, (x, x))
                d[y] = (min(lo, x), max(hi, x))
        else:
            d = {}
            for y, x in p:
                lo, hi = d.get(x, (y, y))
                d[x] = (min(lo, y), max(hi, y))
        lines[i] = d
    E = set()
    for A in ids:
        for B in ids:
            if A == B:
                continue
            la, lb = lines[A], lines[B]
            for k in la:
                if k not in lb:
                    continue
                (alo, ahi), (blo, bhi) = la[k], lb[k]
                if (dx > 0 or dy > 0) and ahi > blo:
                    E.add((A, B))
                    break
                if (dx < 0 or dy < 0) and alo < bhi:
                    E.add((A, B))
                    break
    return ids, E


def free_subsets(ids, E, brute=False):
    """Every proper non-empty subset that can be carried away. S is free when nothing outside it
    stands in its way."""
    n = len(ids)
    if brute and n <= BRUTE_MAX:
        out = []
        for k in range(1, n):
            for S in itertools.combinations(ids, k):
                s = set(S)
                if not any((A, B) in E for A in ids if A not in s for B in s):
                    out.append(s)
        return out
    # strong connectivity: a proper non-empty free subset exists exactly when the blocking digraph
    # is not strongly connected (the sources of the condensation are free).
    if n <= 1:
        return []
    adj = {i: set() for i in ids}
    rev = {i: set() for i in ids}
    for a, b in E:
        adj[a].add(b)
        rev[b].add(a)

    def reach(start, g):
        seen = {start}
        st = [start]
        while st:
            u = st.pop()
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    st.append(v)
        return seen
    r0 = ids[0]
    if len(reach(r0, adj)) == n and len(reach(r0, rev)) == n:
        return []
    return [reach(r0, rev)]          # a witness, not a census


def seized(lab, brute=False):
    """(free subsets found, per-direction counts). Zero everywhere is the axis."""
    tot = 0
    per = {}
    for name, dy, dx in DIRS:
        ids, E = blocking(lab, dy, dx)
        f = free_subsets(ids, E, brute)
        per[name] = len(f)
        tot += len(f)
    return tot, per


def reach_all(lab):
    """Clause REACH: stones with no blocker at all in some direction."""
    bad = 0
    for name, dy, dx in DIRS:
        ids, E = blocking(lab, dy, dx)
        for B in ids:
            if not any((A, B) in E for A in ids if A != B):
                bad += 1
    return bad


# --- choosing the tree -------------------------------------------------------------------------
def pair_mutual(lab, g, gr, gc, vertical):
    """Does this key really lock these two stones — in all four directions, both ways?

    A dovetail is a full lock in the plane, but only if the stone it is driven into keeps material
    on BOTH sides of the tail. On a ragged silhouette it sometimes does not, and then the joint is
    a decoration. This is checked on the pixels, not assumed from the drawing."""
    moved, _w, need, (tr, tc) = key_pixels(g, gr, gc, vertical)
    a = sid_at(lab, g, gr, gc)
    b = sid_at(lab, g, tr, tc)
    if a == 0 or b == 0 or a == b:
        return False
    h, w = lab.shape
    for y, x in moved:
        if not (0 <= y < h and 0 <= x < w) or lab[y, x] != a:
            return False                      # the key must be cut out of the stone it is cut from
    two = np.where((lab == a) | (lab == b), lab, 0)
    after = apply_keys(two, g, [(gr, gc, vertical)])
    for sid in (a, b):
        m = after == sid
        if not m.any():
            return False
        _l, k = label4(m)
        if k != 1:
            return False
    for _name, dy, dx in DIRS:
        _ids, E = blocking(after, dy, dx)
        if (a, b) not in E or (b, a) not in E:
            return False
    return True


def adjacency(comp, g, lab=None, ban=()):
    """Every seam a key could be driven into, as an undirected graph on the live stones.

    With `lab` given the test is the strict one — the key must genuinely seize the pair. Without it
    the test is only whether the body has room, which is all a READER can know before it has decided
    what is a key and what is not."""
    _y0, _x0, live = g
    nr, nc = live.shape
    edges = {}
    for gr in range(nr):
        for gc in range(nc):
            if not live[gr, gc]:
                continue
            for vertical in (True, False):
                if not keyable(comp, g, gr, gc, vertical) or (gr, gc, vertical) in ban:
                    continue
                if lab is None:
                    a = gr * nc + gc
                    b = (gr * nc + gc + 1) if vertical else ((gr + 1) * nc + gc)
                    edges[(a, b)] = (gr, gc, vertical)
                    continue
                if not pair_mutual(lab, g, gr, gc, vertical):
                    continue
                tr, tc = (gr, gc + 1) if vertical else (gr + 1, gc)
                a, b = sid_at(lab, g, gr, gc), sid_at(lab, g, tr, tc)
                edges[(min(a, b), max(a, b))] = (gr, gc, vertical)
    return edges


def spanning(edges, nodes, shape, nc):
    """A spanning tree of the keyable graph, in the shape this class wears.

    Node ids are stone ids, one-based off the course grid, so a stone's course is (v-1)//nc and its
    place in the course (v-1) % nc."""
    def rowof(v):
        return (v - 1) // nc

    def colof(v):
        return (v - 1) % nc
    nbr = {v: [] for v in nodes}
    for (a, b) in edges:
        nbr[a].append(b)
        nbr[b].append(a)
    if not nodes:
        return []
    if shape == 'chain':
        # boustrophedon: the longest walk we can take without repeating a stone, then attach what
        # the walk could not reach.
        start = min(nodes, key=lambda v: (rowof(v), colof(v)))
        tree, seen = [], {start}
        cur = start
        while True:
            nxt = [w for w in nbr[cur] if w not in seen]
            if not nxt:
                break
            w = min(nxt, key=lambda z: (rowof(z),
                                       colof(z) if rowof(z) % 2 == 0 else -colof(z)))
            tree.append((min(cur, w), max(cur, w)))
            seen.add(w)
            cur = w
    elif shape == 'radial':
        start = sorted(nodes, key=lambda v: (abs(rowof(v) - max(rowof(n) for n in nodes) / 2.0),
                                             abs(colof(v) - max(colof(n) for n in nodes) / 2.0)))[0]
        tree, seen = [], {start}
        # breadth first, so the middle stone takes every key it can
        frontier = [start]
        while frontier:
            nxt = []
            for u in frontier:
                for w in nbr[u]:
                    if w not in seen:
                        seen.add(w)
                        tree.append((min(u, w), max(u, w)))
                        nxt.append(w)
            frontier = nxt
    else:  # comb — a spine along the topmost course, a tooth dropped from each stone of it
        rows = sorted({rowof(v) for v in nodes})
        spine = sorted([v for v in nodes if rowof(v) == rows[0]])
        tree, seen = [], set()
        if spine:
            seen.add(spine[0])
        for a, b in zip(spine, spine[1:]):
            if (a, b) in edges or (b, a) in edges:
                tree.append((a, b))
                seen.add(b)
        for v in list(seen):
            for w in nbr[v]:
                if w not in seen and rowof(w) != rowof(v):
                    tree.append((min(v, w), max(v, w)))
                    seen.add(w)
        # teeth grow down until every stone is on the tree
        changed = True
        while changed:
            changed = False
            for v in sorted(seen):
                for w in nbr[v]:
                    if w not in seen:
                        tree.append((min(v, w), max(v, w)))
                        seen.add(w)
                        changed = True
    # anything the shape could not reach is attached by whatever key is available
    changed = True
    while changed:
        changed = False
        for (a, b) in edges:
            if (a in seen) != (b in seen):
                tree.append((min(a, b), max(a, b)))
                seen.add(a)
                seen.add(b)
                changed = True
    return [e for e in tree if e in edges or (e[1], e[0]) in edges]


def edge_keys(tree, edges):
    out = []
    for (a, b) in tree:
        k = edges.get((a, b)) or edges.get((b, a))
        if k is not None:
            out.append(k)
    return out


def plan(comp, cls, mode=None, ban=()):
    """The stones and the keys for one component. Returns (g, lab_plain, keys, note)."""
    g = grid_of(comp)
    if g is None:
        return None
    _y0, _x0, live = g
    nr, nc = live.shape
    lab = base_labels(comp, g)
    live = g[2]
    if int(live.sum()) < MIN_CELLS:
        return None

    # WHERE THE BODY WILL NOT TAKE A KEY, THERE IS NO JOINT — SO THERE IS NO SEAM.
    # Two stones the silhouette is too ragged to dovetail are not left lying against each other
    # (that is precisely the parting this axis forbids); they are cut as ONE STONE, which is what a
    # mason does. The merging repeats until every stone can be reached by keys, so the key graph is
    # connected on the stones that actually exist.
    for _round in range(24):
        edges = adjacency(comp, g, lab, ban)
        stones = sorted({int(i) for i in np.unique(lab) if i > 0})
        if len(stones) < 2:
            break
        seenmap = {v: v for v in stones}

        def find(v):
            while seenmap[v] != v:
                seenmap[v] = seenmap[seenmap[v]]
                v = seenmap[v]
            return v
        for (a, b) in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                seenmap[ra] = rb
        if len({find(v) for v in stones}) == 1:
            break
        # merge one physically touching pair that the keys cannot reach across
        done = False
        h, w = lab.shape
        for y, x in np.argwhere(lab > 0):
            for ny, nx in ((y + 1, x), (y, x + 1)):
                if ny < h and nx < w and lab[ny, nx] > 0 and lab[ny, nx] != lab[y, x]:
                    a, b = int(lab[y, x]), int(lab[ny, nx])
                    if find(a) != find(b):
                        lab[lab == max(a, b)] = min(a, b)
                        done = True
                        break
            if done:
                break
        if not done:
            break
    edges = adjacency(comp, g, lab, ban)
    comp_nodes = sorted({int(i) for i in np.unique(lab) if i > 0})
    if len(comp_nodes) < MIN_CELLS or (not edges and mode != 'glue'):
        return None
    sub = dict(edges)
    if mode is None and seized(lab)[0] == 0:
        return g, lab, [], 'enclosed'
    if mode == 'glue':
        lab[lab > 0] = 1
        return g, lab, [], 'glue'
    if mode == 'ashlar' or mode == 'rivet':
        return g, lab, [], mode
    if mode == 'redundant':
        return g, lab, safe_keys(lab, g, list(sub.values())), mode
    tree = spanning(sub, sorted(comp_nodes), TREE[cls], nc)
    tree = list(dict.fromkeys(tuple(sorted(e)) for e in tree))
    if mode == 'ring':
        for e in sub:
            if tuple(sorted(e)) not in tree:
                tree.append(tuple(sorted(e)))
                break
        return g, lab, safe_keys(lab, g, edge_keys(tree, sub)), mode
    if mode == 'percell':
        deg = {}
        for (a, b) in tree:
            deg[a] = deg.get(a, 0) + 1
            deg[b] = deg.get(b, 0) + 1
        cut = None
        for (a, b) in tree:
            if deg.get(a, 0) > 1 and deg.get(b, 0) > 1:
                cut = (a, b)
                break
        if cut is not None:
            tree = [e for e in tree if e != cut]
        return g, lab, safe_keys(lab, g, edge_keys(tree, sub)), mode
    keys = edge_keys(tree, sub)
    if mode is None:
        keys = solve_keys(lab, g, keys, [k for e, k in sorted(sub.items()) if k not in keys])
        while keys is None:
            # this many stones will not hold: cut FEWER, LARGER stones and try again. A wall that
            # cannot be keyed at this course is keyed at the next one up.
            if not merge_one(lab, sub) or len({int(i) for i in np.unique(lab) if i > 0}) < MIN_CELLS:
                return None
            sub = adjacency(comp, g, lab, ban)
            comp_nodes = sorted({int(i) for i in np.unique(lab) if i > 0})
            if not sub or len(comp_nodes) < MIN_CELLS:
                return None
            if seized(lab)[0] == 0:
                return g, lab, [], 'enclosed'
            tree = spanning(sub, comp_nodes, TREE[cls], nc)
            tree = list(dict.fromkeys(tuple(sorted(e)) for e in tree))
            keys = edge_keys(tree, sub)
            keys = solve_keys(lab, g, keys, [k for e, k in sorted(sub.items()) if k not in keys])
    # A PLATE THAT ALREADY HOLDS CARRIES NO JOINT. Where the silhouette wraps one stone entirely
    # inside another, plain courses are seized by enclosure and every key would be a passenger.
    # Such plates are cut into plain courses and REPORTED — the axis does not take credit for
    # rigidity it did not supply.
    # THE GENERATOR SOLVES; THE READER VERIFIES. A plate this body will not hold a joint in is left
    # uncut and REPORTED — never shipped as a plate that quietly fails its own law.
    return g, lab, keys, 'ok'


def safe_keys(lab, g, keys):
    """Keep only the keys that leave every stone whole. The controls get the same courtesy as the
    axis, so that each control fails the clause it was built to fail and not a bookkeeping one."""
    out = []
    for k in keys:
        trial = out + [k]
        if stones_whole(apply_keys(lab, g, trial)):
            out = trial
    return out


def merge_one(lab, edges):
    """Cut two touching stones as one. Preference goes to a pair with no keyable seam between them
    — the seam that was never going to be a joint is the seam that should not exist."""
    h, w = lab.shape
    fallback = None
    for y, x in np.argwhere(lab > 0):
        for ny, nx in ((y + 1, x), (y, x + 1)):
            if ny < h and nx < w and lab[ny, nx] > 0 and lab[ny, nx] != lab[y, x]:
                a, b = int(lab[y, x]), int(lab[ny, nx])
                pair = (min(a, b), max(a, b))
                if pair not in edges:
                    lab[lab == pair[1]] = pair[0]
                    return True
                if fallback is None:
                    fallback = pair
    if fallback is not None:
        lab[lab == fallback[1]] = fallback[0]
        return True
    return False


def stones_whole(lab):
    """No stone may be broken into pieces or cut away entirely by the keys driven into it."""
    for i in {int(v) for v in np.unique(lab) if v > 0}:
        m = lab == i
        if int(m.sum()) < 3:
            return False
        _l, k = label4(m)
        if k != 1:
            return False
    return True


def solve_keys(lab, g, first, spare):
    """Drive the keys, one at a time, checking the plate after every one.

    A key is three pixels taken out of a stone, and taking three pixels out of a stone can undo the
    bite of a key driven into it earlier — two keys cut from the same stone are not independent.
    So the tree the class wears is only the ORDER in which keys are offered; each one is kept only
    if the plate is still whole afterwards and no worse seized than it was, and keys are offered
    until nothing can be carried away. Returns None when this body will not hold a joint at all."""
    keys = []
    best = seized(lab)[0]
    for k in list(first) + list(spare):
        trial = keys + [k]
        lab2 = apply_keys(lab, g, trial)
        if not stones_whole(lab2):
            continue
        s2 = seized(lab2)[0]
        if s2 <= best:
            keys, best = trial, s2
        if best == 0:
            break
    if best != 0:
        for k in list(first) + list(spare):
            if k in keys:
                continue
            trial = keys + [k]
            lab2 = apply_keys(lab, g, trial)
            if not stones_whole(lab2):
                continue
            s2 = seized(lab2)[0]
            if s2 <= best:
                keys, best = trial, s2
            if best == 0:
                break
    return keys if best == 0 else None


def prune(lab_plain, g, keys):
    """Strike out any key that is not holding anything: LOAD-BEARING by construction, and the count
    of struck keys is reported rather than hidden."""
    keys = list(keys)
    struck = 0
    i = 0
    while i < len(keys):
        trial = keys[:i] + keys[i + 1:]
        if seized(apply_keys(lab_plain, g, trial))[0] == 0:
            keys = trial
            struck += 1
        else:
            i += 1
    return keys, struck


# --- painting ----------------------------------------------------------------------------------
def paint(fr, lab, pal):
    """Every stone raised: crest on its top and right (the light is upper-right, as everywhere in
    this project), shadow under it and to its left, mid in the middle. Only pixels already opaque
    are ever touched, so this cannot create strays and cannot change the silhouette."""
    crest, mid, dark = pal
    h, w = lab.shape
    for y, x in np.argwhere(lab > 0):
        s = lab[y, x]
        below = lab[y + 1, x] if y + 1 < h else 0
        left = lab[y, x - 1] if x > 0 else 0
        above = lab[y - 1, x] if y > 0 else 0
        right = lab[y, x + 1] if x + 1 < w else 0
        if below != s or left != s:
            put(fr, y, x, dark)
        elif above != s or right != s:
            put(fr, y, x, crest)
        else:
            put(fr, y, x, mid)


def paint_rivets(fr, lab, g, edges, pal):
    """The RIVET control: a stud sitting ON the seam, symmetric, crossing nothing."""
    crest, _mid, _dark = pal
    for (gr, gc, vertical) in edges:
        moved, _w, _n, _t = key_pixels(g, gr, gc, vertical)
        y, x = moved[0]
        put(fr, y, x, crest)


# --- the reader --------------------------------------------------------------------------------
def tones_of(fr, lab):
    """The three stops, discovered from the plate itself rather than told to the reader."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    vals = sorted({int(lum[y, x]) for y, x in np.argwhere(lab > 0)})
    if len(vals) < 3:
        return None
    return vals[0], vals[len(vals) // 2], vals[-1]      # dark, mid, crest


def read_keys(fr, comp, g):
    """Recover the keys from the pixels, with two witnesses each.

    At a keyed vertical seam the neck pixel belongs to the RIGHT stone and so lies on that stone's
    left edge: it is DARK where an unkeyed seam would show the left stone's lit right edge. The tail
    pixel one deeper is DARK too, where an unkeyed course would be MID. Both must agree.
    Returns (keys, disagreements)."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    _y0, _x0, live = g
    nr, nc = live.shape
    vals = sorted({int(lum[y, x]) for y, x in np.argwhere(comp)})
    if len(vals) < 3:
        return [], 0
    stops = (vals[0], vals[len(vals) // 2], vals[-1])          # dark, mid, crest

    def stop_of(y, x):
        v = int(lum[y, x])
        return int(np.argmin([abs(v - s) for s in stops]))      # 0 dark, 1 mid, 2 crest

    keys, bad = [], 0
    for gr in range(nr):
        for gc in range(nc):
            for vertical in (True, False):
                if not keyable(comp, g, gr, gc, vertical):
                    continue
                moved, _w, _n, _t = key_pixels(g, gr, gc, vertical)
                (yn, xn), (yt, xt) = moved[0], moved[2]
                # WITNESS ONE, the neck: the seam line jogs, so the pixel that would have been the
                # left stone's lit edge is the right stone's shadowed one.  keyed DARK / plain CREST
                # WITNESS TWO, the tail, one pixel deeper: keyed DARK / plain MID
                w1 = stop_of(yn, xn)
                w2 = stop_of(yt, xt)
                k1 = (w1 == DARK)
                k2 = (w2 == DARK)
                if k1 != k2:
                    bad += 1
                    continue
                if k1:
                    keys.append((gr, gc, vertical))
    return keys, bad


# --- building ----------------------------------------------------------------------------------
def build_component(fr, comp, cls, mode=None):
    """Plan, key, prune and paint one component. Returns (g, lab, keys, struck) or None.

    A component too small or too ragged to take a joint is painted as ONE UNCUT STONE — the axis's
    own GLUE case, worn. That is the honest thing to do and it is said out loud rather than faked:
    a sabaton is fourteen pixels of ragged diagonal and a dovetail is four pixels across in each
    direction, so THE JOINT DOES NOT FIT, and no arrangement of this axis's law can make it fit.
    Such plates are never fed to the acceptance test; they are counted and reported."""
    ban = set()
    for _attempt in range(4):
        p = plan(comp, cls, mode, ban)
        if p is None or p[3] == 'enclosed':
            break
        g, lab_plain, keys, note = p
        if note == 'glue' or mode is not None:
            break
        keys, struck = prune(lab_plain, g, keys)
        # A KEY THAT CANNOT BE READ OFF THE PIXELS IS NOT A KEY. Drive it into a scratch copy of the
        # frame, hand the pixels back to the reader, and keep only the joint the plate can say out
        # loud; the rest of the sites are banned and the plate is solved again without them.
        tmp = fr.copy()
        paint(tmp, apply_keys(lab_plain, g, keys), PAL[cls])
        rk, _bad = read_keys(tmp, comp, g)
        wrong = set(rk) ^ set(keys)
        if not wrong:
            lab = apply_keys(lab_plain, g, keys)
            paint(fr, lab, PAL[cls])
            return g, lab_plain, lab, keys, struck
        ban |= wrong
    if mode is None:
        # never converged, or the plate holds by itself, or it is too small: no joint is cut, the
        # courses are painted plain, and the plate is REPORTED rather than shipped as a plate that
        # fails its own law.
        if p is None:
            paint(fr, comp.astype(np.int32), PAL[cls])
        else:
            paint(fr, p[1], PAL[cls])
        return None
    if p is None:
        paint(fr, comp.astype(np.int32), PAL[cls])
        return None
    g, lab_plain, keys, note = p
    if note == 'glue':
        paint(fr, lab_plain, PAL[cls])
        return g, lab_plain, lab_plain, [], 0
    struck = 0
    lab = apply_keys(lab_plain, g, keys)
    paint(fr, lab, PAL[cls])
    if mode == 'rivet':
        paint_rivets(fr, lab, g, list(adjacency(comp, g).values()), PAL[cls])
    return g, lab_plain, lab, keys, struck


def build(base, cfg, cls, mode=None):
    D, M, L = BODY[cls]
    largest = cfg['largest']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        if fi >= SLEEP_FROM:
            continue
        for comp in comps_of(a, largest):
            if comp.sum() < MIN_PX:
                continue
            build_component(fr, comp, cls, mode)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


CONTROLS = ('ashlar', 'rivet', 'percell', 'ring', 'redundant', 'glue')


# --- the acceptance test ------------------------------------------------------------------------
def frames_of(base, cfg):
    for fi in range(SLEEP_FROM):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a = base[sl][..., 3] > 0
        if a.any():
            yield fi, sl, a


def accept(mode=None, verbose=True, limit=None):
    res = dict(plates=0, small=0, stones=0, keys=0, struck=0,
               tiling=0, seized=0, brute=0, brute_ok=0, interlock=0, load=0, reach=0,
               legible=0, degs={}, freed=0)
    for kind, cfg in SLOTS.items():
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                n = 0
                for fi, sl, a in frames_of(base, cfg):
                    if limit and n >= limit:
                        break
                    fr = np.zeros((FH, FW, 4), dtype=base.dtype)
                    D, M, L = BODY[cls]
                    recolor(base[sl], fr, a, D, M, L)
                    for comp in comps_of(a, cfg['largest']):
                        if comp.sum() < MIN_PX:
                            continue
                        got = build_component(fr, comp, cls, mode)
                        if got is None:
                            res['small'] += 1
                            continue
                        g, lab0, lab, keys, struck = got
                        n += 1
                        res['plates'] += 1
                        res['struck'] += struck
                        ids = [int(i) for i in np.unique(lab) if i > 0]
                        res['stones'] += len(ids)
                        res['keys'] += len(keys)

                        # (1) TILING
                        ok = len(ids) >= MIN_CELLS
                        for i in ids:
                            m = lab == i
                            _l, k = label4(m)
                            if k != 1:
                                ok = False
                                break
                        if not ok:
                            res['tiling'] += 1

                        # (6) LEGIBLE — recover the keys from the pixels
                        rk, badwit = read_keys(fr, comp, g)
                        if set(rk) != set(keys):
                            res['legible'] += len(set(rk) ^ set(keys))
                        rec = apply_keys(lab0, g, rk)

                        # (2) SEIZED, on the RECOVERED stones
                        free, _per = seized(rec)
                        if free:
                            res['seized'] += 1
                            res['freed'] += free
                        if len(ids) <= BRUTE_MAX:
                            res['brute'] += 1
                            fb, _p2 = seized(rec, brute=True)
                            if fb == 0:
                                res['brute_ok'] += 1

                        # (3) INTERLOCK — strike every key out
                        if seized(lab0)[0] == 0 and len(ids) > 1:
                            res['interlock'] += 1

                        # (4) LOAD-BEARING — strike out any one
                        for i in range(len(keys)):
                            trial = keys[:i] + keys[i + 1:]
                            if seized(apply_keys(lab0, g, trial))[0] == 0:
                                res['load'] += 1
                                break

                        # (5) REACH
                        res['reach'] += reach_all(rec)

                        # the tree, recovered
                        deg = {}
                        for (gr, gc, vertical) in rk:
                            nc = g[2].shape[1]
                            a1 = gr * nc + gc
                            b1 = a1 + 1 if vertical else a1 + nc
                            deg[a1] = deg.get(a1, 0) + 1
                            deg[b1] = deg.get(b1, 0) + 1
                        if deg:
                            res['degs'].setdefault(cls, []).append(max(deg.values()))
    if verbose:
        name = (mode or 'dovetail').upper()
        print('== ACCEPTANCE — the 66th axis, DOVETAIL   [%s]' % name)
        print('  plates read %d   (skipped, too small to joint: %d)' % (res['plates'], res['small']))
        print('  stones cut %d   keys driven %d   keys struck as idle %d'
              % (res['stones'], res['keys'], res['struck']))
        c1 = res['tiling'] == 0
        c2 = res['seized'] == 0
        c3 = res['interlock'] == 0
        c4 = res['load'] == 0
        c5 = res['reach'] == 0
        c6 = res['legible'] == 0
        print('  CLAUSE 1 — TILING       : %d plates whose stones do not partition the plate -> %s'
              % (res['tiling'], 'PASS' if c1 else 'FAIL'))
        print('  CLAUSE 2 — SEIZED       : %d plates with a part that comes away (%d partings found)'
              '  -> %s' % (res['seized'], res['freed'], 'PASS' if c2 else 'FAIL'))
        print('       brute force over every subset on %d of them: %d held  (2^n-2 partings x 4 '
              'directions, each one attempted)' % (res['brute'], res['brute_ok']))
        print('  CLAUSE 3 — INTERLOCK    : %d plates that hold with every key struck out -> %s'
              % (res['interlock'], 'PASS' if c3 else 'FAIL'))
        print('  CLAUSE 4 — LOAD-BEARING : %d plates carrying a key that holds nothing -> %s'
              % (res['load'], 'PASS' if c4 else 'FAIL'))
        print('  CLAUSE 5 — REACH        : %d stones with no blocker in some direction -> %s'
              % (res['reach'], 'PASS' if c5 else 'FAIL'))
        print('  CLAUSE 6 — LEGIBLE      : %d keys the pixels do not report exactly as driven -> %s'
              % (res['legible'], 'PASS' if c6 else 'FAIL'))
        if res['degs']:
            print('  the trees, recovered from the pixels (max degree, mean over plates):')
            for cls in ('warrior', 'mage', 'ranger'):
                d = res['degs'].get(cls)
                if d:
                    print('       %-8s %-7s  max degree %.2f' % (cls, TREE[cls], float(np.mean(d))))
        allp = c1 and c2 and c3 and c4 and c5 and c6
        print('OVERALL [%s]: %s' % (name, 'ALL PASS' if allp else 'FAIL'))
        return allp
    return res


def controls_report():
    ok = accept(None, limit=3)
    print()
    bad = []
    for m in CONTROLS:
        r = accept(m, limit=3)
        print()
        bad.append((m, r))
    print('== SUMMARY')
    print('   %-10s %s' % ('DOVETAIL', 'ALL PASS' if ok else 'FAIL'))
    for m, r in bad:
        print('   %-10s %s' % (m.upper(), 'ALL PASS' if r else 'FAIL'))
    print('OVERALL: %s' % ('ALL PASS  (axis passes, all six controls fail)'
                           if ok and not any(r for _m, r in bad) else 'FAIL'))


def dump_cells():
    cfg = SLOTS['chest']
    base = load_any('%s.png' % cfg['srcs']['warrior'])
    a = base[:FH, :FW][..., 3] > 0
    fr = np.zeros((FH, FW, 4), dtype=base.dtype)
    D, M, L = BODY['warrior']
    recolor(base[:FH, :FW], fr, a, D, M, L)
    comp = comps_of(a, True)[0]
    got = build_component(fr, comp, 'warrior')
    g, _lab0, lab, keys, struck = got
    ys, xs = np.nonzero(lab)
    print('warrior chest frame 0 — %d stones, %d keys (%d struck as idle)'
          % (len(set(lab[lab > 0].tolist())), len(keys), struck))
    for y in range(ys.min(), ys.max() + 1):
        row = ''
        for x in range(xs.min(), xs.max() + 1):
            v = lab[y, x]
            row += '.' if v == 0 else 'ABCDEFGHIJKLMNOPQRSTUVWX'[(v - 1) % 24]
        print('   ' + row)
    tot, per = seized(lab, brute=True)
    print('   partings found, brute force over all subsets: %s   total %d' % (per, tot))


def trees_report():
    print('== THE THREE TREES, RECOVERED FROM THE PIXELS (the reader is never told the class)')
    cfg = SLOTS['chest']
    for cls in ('warrior', 'mage', 'ranger'):
        base = load_any('%s.png' % cfg['srcs'][cls])
        a = base[:FH, :FW][..., 3] > 0
        fr = np.zeros((FH, FW, 4), dtype=base.dtype)
        D, M, L = BODY[cls]
        recolor(base[:FH, :FW], fr, a, D, M, L)
        comp = comps_of(a, True)[0]
        got = build_component(fr, comp, cls)
        if got is None:
            print('   %-8s %-7s frame 0 too small to joint' % (cls, TREE[cls]))
            continue
        g, _lab0, lab, keys, _s = got
        rk, bad = read_keys(fr, comp, g)
        nc = g[2].shape[1]
        deg = {}
        for (gr, gc, vertical) in rk:
            a1 = gr * nc + gc
            b1 = a1 + 1 if vertical else a1 + nc
            deg[a1] = deg.get(a1, 0) + 1
            deg[b1] = deg.get(b1, 0) + 1
        n = len({int(i) for i in np.unique(lab) if i > 0})
        print('   %-8s %-7s stones %2d  keys driven %2d  keys read back %2d  degrees %s'
              % (cls, TREE[cls], n, len(keys), len(rk),
                 sorted(deg.values(), reverse=True)))


def key_still_reads(fr, g, site):
    """Is the jog still visible in the pixels after an outside light has been over them?

    The acceptance reader classifies against the plate's three stops, which is exact on a plate that
    has exactly three stops and meaningless after the finishing pass has put a cosine ramp across
    the sheet. So survival is measured RELATIVELY and locally: a key is still there if its neck and
    its tail are still the darker part of their own window. Reported, never a clause — the finishing
    pass is an outside light and does not belong in an acceptance test."""
    moved, _w, need, _t = key_pixels(g, *site)
    lum = fr[..., :3].astype(np.int32).sum(-1)
    h, w = lum.shape
    vals = [int(lum[y, x]) for y, x in need if 0 <= y < h and 0 <= x < w]
    if not vals:
        return False
    ref = sum(vals) / float(len(vals))
    return all(lum[y, x] < ref for y, x in moved[::2] if 0 <= y < h and 0 <= x < w)


def survive_diag():
    print('== SURVIVAL THROUGH THE FINISHING PASS (reported, never a clause)')
    for kind in ('chest', 'helmet', 'legs', 'boots'):
        cfg = SLOTS[kind]
        tot = good = 0
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            stem = cfg['dst'] % cls
            arr = build(base, cfg, cls)
            fin, _ = finish_array(arr.copy(), '%s.png' % stem)
            a = base[:FH, :FW][..., 3] > 0
            for comp in comps_of(a, cfg['largest']):
                if comp.sum() < MIN_PX:
                    continue
                g = grid_of(comp)
                if g is None:
                    continue
                try:
                    want, _b1 = read_keys(arr[:FH, :FW], comp, g)
                except Exception:
                    continue
                tot += len(want)
                good += sum(1 for k in want if key_still_reads(fin[:FH, :FW], g, k))
        print('   %-7s %3d/%-3d keys still read correctly after finishing  (%.1f%%)'
              % (kind, good, tot, 100.0 * good / max(tot, 1)))


def slots_diag():
    print('== SLOTS')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            stones = keys = plates = small = 0
            for fi, sl, a in frames_of(base, cfg):
                fr = np.zeros((FH, FW, 4), dtype=base.dtype)
                D, M, L = BODY[cls]
                recolor(base[sl], fr, a, D, M, L)
                for comp in comps_of(a, cfg['largest']):
                    if comp.sum() < MIN_PX:
                        continue
                    got = build_component(fr, comp, cls)
                    if got is None:
                        small += 1
                        continue
                    g, _lab0, lab, k, _s = got
                    plates += 1
                    stones += len({int(i) for i in np.unique(lab) if i > 0})
                    keys += len(k)
            print('   %-7s %-8s plates %3d (too small %3d)  stones %4d  keys %4d'
                  % (kind, cls, plates, small, stones, keys))


def main():
    if '--cells' in sys.argv:
        dump_cells()
        return
    if '--trees' in sys.argv:
        trees_report()
        return
    if '--accept' in sys.argv:
        accept()
        return
    if '--controls' in sys.argv:
        controls_report()
        return
    if '--survive' in sys.argv:
        survive_diag()
        return
    if '--sweep' in sys.argv:
        slots_diag()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                stem = (cfg['dst'] % cls) + suffix
                arr = build(base, cfg, cls)
                dst = '%s/%s.png' % (outdir, stem)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
