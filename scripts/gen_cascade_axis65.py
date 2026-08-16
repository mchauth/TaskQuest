#!/usr/bin/env python3
"""SIXTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS — the CASCADE family: the engraving is not
laid out, it is GROWN. Every row of the field is the image of the row above it under one fixed
nearest-neighbour rule, so the whole ornament is the ORBIT of a one-dimensional automaton.

    the ornament is  RISE   a 2x1 rib lit on its LEFT face
                     FALL   the same rib lit on its RIGHT face
    the law is       row r+1 = f(row r), f a fixed function of (left, centre, right)

*** THIS IS THE FIRST AXIS WHOSE INVARIANT IS A CAUSE. ***
Sixty-four axes have been RELATIONS: a statistic holds among the shards (46th), a wire is connected
(54th), three hoops stand in 3:2:1 (61st), the raised studs exclusive-or to zero (64th). Every one
of them is a sentence about pixels that are all equally present, and it can be checked by holding
the sheet still. This one is a sentence about pixels PRODUCING other pixels. The field has a seed
row and everything under it is consequence. **The vertical direction of the plate is not a
direction here. It is a HISTORY.** The 57th FESTOON gave the set an UP; the 55th STRATA gave it a
BEFORE in the sense of which lap was laid over which; this gives it an up that is a before, in which
each row is not merely later than the one above it but CAUSED by it.

*** THE ACCEPTANCE TEST IS A NEW KIND: AN INDUCTION. IT RECOVERS THE GENERATOR FROM THE ARTEFACT
    AND THEN RE-DERIVES THE ARTEFACT. ***
Every reader in this project so far has been an instrument brought to the sheet already knowing what
it wanted to measure — an area, a winding number, a syndrome. This reader is told nothing. It is
handed the pixels and the mask, it watches which triples of cells are followed by which cell, and if
that correspondence is a FUNCTION it has found the law, which it then prints by its Wolfram number.
It is not checking a rule against the sheet. **It is learning the rule off the sheet and then using
it to predict the parts of the sheet it has not looked at.** The rule number appears nowhere in the
test; it is an output.

    (1) DETERMINISM   over every (left, centre, right) triple visible anywhere on the plate, the
                      cell below the centre is single-valued. No triple is ever followed by two
                      different things. This is the whole axis in one line, and it needs no
                      knowledge of which rule was used. RANDOM fails. REPEAT fails, at its seams.
    (2) REPLAY        the rule is fitted on the TOP HALF of the rows only and made to predict the
                      BOTTOM half, cell by cell, exactly. Zero mismatches. This is a forward
                      prediction and not a restatement of (1): a table fitted on all the data and
                      then checked against all the data is a tautology, which is the trap this
                      clause exists to avoid. There is NO TOLERANCE CONSTANT anywhere in this file.
    (3) RADIUS        radius one is SUFFICIENT (that is clause 1) and radius zero is NOT: the map
                      from a cell to the cell below it, taken alone, must be contradictory. If it
                      is not, every column is independent and the plate is the 11th FLUTING with
                      extra steps. STATIC fails. WIDE fails clause 1 and passes at radius two,
                      which is what makes this clause about ECONOMY: eight bits of law, not
                      thirty-two.
    (4) DEPENDENCE    the recovered rule is not a projection: not the identity, not a shift either
                      way, not a complement of any of those, not a constant. Those eight rules are
                      the ones that make a picture out of nothing happening. SHIFT fails, and it
                      fails while looking exactly like the 16th TWILL, which is the point.
    (5) SENSITIVITY   turn over ONE cell of the seed row, re-run the RECOVERED rule, and three
                      things must hold for every perturbation with no exceptions: the disagreement
                      NEVER DIES; it SATURATES THE LIGHT CONE, meaning that at row k some cell
                      exactly k away from the flip differs, which is the fastest a radius-one rule
                      can possibly transmit; and it GROWS, meaning strictly more than one changed
                      cell per row. The third is measured against the exact value a translation
                      scores — twelve changed cells over twelve rows — and not against a threshold
                      anyone chose. STATIC dies at the first clause of the three, SHIFT at the
                      third, and both of them pass (1) and (2) perfectly.
    (6) LEGIBLE       every cell states its value TWICE, on two stacked pixel pairs, and the reader
                      takes each pair as an independent witness and requires them to agree. No
                      single pixel decides anything.

*** THE EXACT COMPLEMENT OF THE 64th. ***
The two axes ask the same question — WHAT DOES ONE WRONG PIXEL DO? — and give opposite answers, and
between them they close the question.
    the 64th TALLY    one flipped stud changes exactly one stud, and the plate says its NUMBER.
                      Damage is bounded, local and named. The invariant is REDUNDANCY.
    the 65th CASCADE  one flipped cell in the seed changes an ever-widening cone of everything
                      beneath it, and no plate can say which cell it was, because a thousand
                      different wounds produce a thousand equally lawful-looking plates. Damage is
                      unbounded, non-local and anonymous. The invariant is DETERMINISM.
Redundancy buys you the location of an error at the price of spending studs on nothing. Determinism
buys you the whole plate for eight bits and a seed at the price of never being able to repair it.
Measured, over this batch: **one flipped cell costs the 64th exactly 1 stud and costs this axis a
mean of many hundreds** (printed by --sensitivity). That number is the difference between the two
axes and it is the only number either of them needs.

*** THE SIX CONTROLS. ***
    STATIC     rule 204, c' = c. Every column constant: vertical ribs. It passes DETERMINISM and
               REPLAY perfectly and forever, because nothing ever happens. The lower collapse
               boundary, and it is the 11th FLUTING exactly. Fails RADIUS, DEPENDENCE, SENSITIVITY.
    SHIFT      rule 170, c' = r. Diagonal ribs — the 16th TWILL. THE HONEST NEAR MISS: it is a
               genuine cellular automaton, genuinely deterministic, genuinely radius one, and it
               carries no information at all; the seed just walks sideways. It is what "grown by a
               rule" degenerates into if the rule is allowed to be a translation, and it is the
               reason clause DEPENDENCE is written down. Fails DEPENDENCE and SENSITIVITY.
    RANDOM     every row drawn independently. Looks the busiest and the most "designed" of the six
               and is the only one that is not a cascade at all. Fails DETERMINISM immediately —
               which is worth saying plainly, because at 13px it is nearly indistinguishable from
               the axis by eye. The upper collapse boundary.
    REPEAT     the first four rows grown honestly by the rule, then that block tiled down the
               plate. THE BUG THIS AXIS WOULD HAVE SHIPPED WITH, and it is invisible: three rows in
               four are perfectly lawful and the seams are two pixels tall. It fails DETERMINISM at
               the seams and only at the seams, which is exactly why clause 2 has no tolerance —
               a reader willing to forgive one row in four forgives this control.
    WIDE       radius two, c' = l2 XOR r2. A real cascade with a richer field and a law four times
               the size. It fails at radius one and passes at radius two, so it is not wrong, it is
               EXPENSIVE — the control that makes clause RADIUS a statement about economy rather
               than about correctness.
    REVERSED   the same orbit generated bottom-up and printed the other way round. It is a lawful
               cascade read against its own arrow, and it fails DETERMINISM downward. The control
               that proves the plate's arrow of time is a fact about the pixels and not a labelling
               convention.

*** DISTINCTNESS. ***
  * 63rd CURRENT — the other axis with time in it, and the split is total. There time is the FRAME
    INDEX and the invariant is invisible in any single picture. Here time is the Y AXIS OF ONE
    PICTURE and the invariant is entirely present in a single still frame. The 63rd cannot be
    checked without putting frames in order; this cannot be checked without putting ROWS in order.
  * 64th TALLY — see above; same question, opposite answer, and the palettes are deliberately
    unrelated so that the pair does not read as a recolor.
  * 49th DENDRITE — branching growth, but the branch is a SHAPE authored recursively and its rule
    is spatial, not temporal. A dendrite grown twice with different seeds is the same motif; a
    cascade grown twice with different seeds is a different plate.
  * 48th COSMATI — self-similarity across scales. This axis deliberately avoids the additive rule
    from a single lit cell (which would draw a Sierpinski triangle and collide with the 48th head
    on) by seeding a FULL RANDOM ROW, from which even the additive rules produce a field of nested
    triangles with no distinguished centre and no scale hierarchy.
  * 11th FLUTING / 16th TWILL — this axis's two degenerate controls, named as such rather than
    avoided.
  * 46th CRAQUELURE — aperiodic, but by a random process whose only claim is a statistic. This
    field is also aperiodic and is COMPLETELY DETERMINED by eight bits and a seed row: the two are
    opposite explanations of the same appearance, and clause DETERMINISM is what tells them apart.

*** CLASS IDENTITY IS THE LAW, NOT THE PALETTE. ***
Every previous axis distinguishes the three classes by colour and keeps the geometry identical.
Here each class is also a DIFFERENT AUTOMATON — warrior rule 30, mage rule 90, ranger rule 150 —
and the acceptance test recovers all three from the pixels without being told. Two of the three are
additive and one is not, and the reader does not care, which is the argument that the test is
reading the sheet rather than reciting the design.

Geometry, per COMPONENT, self-anchored in its own bounding box (the 62nd DATUM owns the other
choice):
    lattice   ONE orbit per item: W=40 columns x H=32 rows, seeded from sha256(item stem) and grown
              by the class's rule with a fixed quiescent boundary. The orbit is computed ONCE and
              every component of every frame shows the window of it that starts at that component's
              own bounding-box top-left. The orbit does not depend on the frame, so THE ENGRAVING
              DOES NOT BOIL: it is a fixed piece of work that the moving silhouette reveals more or
              less of.
    cell      2 px wide, 2 px tall. RISE is lit on the left pair and shadowed on the right; FALL is
              the mirror. Reading is RELATIVE — left pair against right pair — so it survives any
              overall lightening or darkening, which is what the finishing pass does.
    live      a cell counts iff all four of its pixels are opaque body pixels. Decided on the mask,
              which the reader recomputes exactly, because this generator never changes a
              silhouette.
    visible   a cell is VERIFIABLE iff it is live and all three of its antecedents are live. The
              plate is a window onto the orbit and the test checks only what the window shows —
              stated rather than hidden, and the coverage figure is printed.

THE RENDER-PAID LESSON. The 64th learned that two-symbol relief in ROWS fuses into horizontal bars
and must go on a diagonal. This axis puts the split VERTICALLY, which is the one arrangement the
64th could not use — and it can only afford to because the automaton itself guarantees that no
column stays in one state for long. A vertical split under a STATIC rule is precisely the 11th
FLUTING; under a real cascade it is a rib field full of dislocations, and the dislocations are the
triangles. The ornament shows the DOMAIN WALLS, and in an automaton the walls are the content.

Authoring philosophy identical to gen_canon_axis61.py ... gen_tally_axis64.py: every pattern pixel is
painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed, silhouette
untouched — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Twenty-first generator to call it in-line, after axes 45-64.

Run from repo root:
  python3 scripts/gen_cascade_axis65.py
  python3 scripts/gen_cascade_axis65.py --law          # the three laws, recovered from the pixels
  python3 scripts/gen_cascade_axis65.py --cells        # ASCII of one real component
  python3 scripts/gen_cascade_axis65.py --controls     # the six controls through the same reader
  python3 scripts/gen_cascade_axis65.py --accept       # the six clauses over all 24 sheets
  python3 scripts/gen_cascade_axis65.py --sensitivity  # the 64th answered 1; this answers ...
  python3 scripts/gen_cascade_axis65.py --survive      # legibility through the finishing pass
  python3 scripts/gen_cascade_axis65.py --sweep        # slots + visor diagnostics
Then QA (examples):
  python3 scripts/sprite_qa.py _cascade_legendary_preview/shirt_warrior_legendary65.png
  python3 scripts/sprite_qa.py _cascadedome_helmet_preview/helmet_mage_legendary65.png --y-min 2
  python3 scripts/sprite_qa.py _cascade_boots_preview/boots_warrior_legendary_cascade.png --y-max 63
"""
import os
import sys
import hashlib
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18
SLEEP_FROM = 60

CELL_W, CELL_H = 2, 2
LAT_W, LAT_H = 40, 32          # one orbit covers the whole frame at 2px cells: 80/2, 64/2

RISE, FALL = 1, 0

# A component must show at least this many verifiable cells to be tested. Below it the window onto
# the orbit is too small for a triple to have three live antecedents anywhere, and the plate is
# painted plain and REPORTED, never failed.
MIN_VERIFIABLE = 6
MIN_CELLS = 8

# The eight rules that make a picture out of nothing happening — clause DEPENDENCE.
PROJECTIONS = {0, 255, 204, 51, 170, 85, 240, 15}

# CLASS IDENTITY IS THE LAW. warrior 30 (chaotic, not additive), mage 90 (l XOR r),
# ranger 150 (l XOR c XOR r). All three have a two-sided light cone at speed one, which is what
# clause SENSITIVITY needs; the reader is never told any of these numbers.
RULE = {'warrior': 30, 'mage': 90, 'ranger': 150}


# --- the automaton ------------------------------------------------------------------------------
def step(row, rule):
    """One application of an eight-bit nearest-neighbour rule, quiescent outside the lattice."""
    l = np.concatenate(([0], row[:-1]))
    r = np.concatenate((row[1:], [0]))
    idx = (l << 2) | (row << 1) | r
    return ((rule >> idx) & 1).astype(np.uint8)


def step_wide(row):
    """The WIDE control: radius two, c' = l2 XOR r2. A real cascade with a law four times the size."""
    z = np.zeros(2, dtype=np.uint8)
    p = np.concatenate((z, row, z))
    return (p[:-4] ^ p[4:]).astype(np.uint8)


def seed_row(stem, w=LAT_W, salt='seed'):
    """The seed. A FULL row, not a single lit cell — a single cell under an additive rule draws a
    Sierpinski triangle, and the 48th COSMATI already owns self-similarity across scales."""
    out = np.zeros(w, dtype=np.uint8)
    need = (w + 7) // 8
    buf = b''
    k = 0
    while len(buf) < need:
        buf += hashlib.sha256(('%s|%s|%d' % (stem, salt, k)).encode()).digest()
        k += 1
    for i in range(w):
        out[i] = (buf[i // 8] >> (i % 8)) & 1
    return out


def orbit(stem, cls, mode=None, h=LAT_H, w=LAT_W):
    """The whole engraving of one item, as an h x w array of RISE/FALL. Computed once."""
    rule = RULE[cls]
    rows = [seed_row(stem, w)]
    if mode == 'random':
        for k in range(1, h):
            rows.append(seed_row(stem, w, 'rnd%d' % k))
        return np.array(rows, dtype=np.uint8)
    if mode == 'static':
        rule = 204
    if mode == 'shift':
        rule = 170
    if mode == 'repeat':
        blk = [rows[0]]
        for _ in range(3):
            blk.append(step(blk[-1], rule))
        rows = []
        while len(rows) < h:
            rows.extend(blk)
        return np.array(rows[:h], dtype=np.uint8)
    if mode == 'wide':
        for _ in range(h - 1):
            rows.append(step_wide(rows[-1]))
        return np.array(rows, dtype=np.uint8)
    for _ in range(h - 1):
        rows.append(step(rows[-1], rule))
    a = np.array(rows, dtype=np.uint8)
    if mode == 'reversed':
        a = a[::-1].copy()
    return a


# --- palette -------------------------------------------------------------------------------------
# TWO engraving stops per class, not three: the cell is a rib with a lit face and a shaded face and
# there is no third tone in it anywhere. The 64th put half of every tessera in the MID and hung
# class identity there; this axis has no mid in the pattern at all, so identity lives in the PAIR —
# three different hue oppositions rather than three different temperatures of one tone.
#   warrior  ARGENT ON WINE     bright silver ribs cut into dark red
#   mage     GOLD ON ABYSS      warm gold on deep blue, the only warm-on-cold pair
#   ranger   ROSE ON OLIVE      pale rose on grey-green
# NO STOP NEAR PURE BLACK: the finishing pass carves the visor as black eye and mouth pixels and a
# near-black darkest stop swallows them (the 49th's lesson). Darkest channel-sums 200 / 218 / 194.
# The lit/dark ratio is held near 1.8 rather than at the 3.5 the first draw used: a rib two pixels
# wide with a white face and a near-black face is not relief, it is a printed stripe, and the first
# render came out as barber-pole. Relief at this scale wants the two faces of ONE material.
CASPAL = {
    'warrior': ((176, 186, 204), (112, 50, 64), (86, 46, 58)),
    'mage':    ((206, 180, 120), (72, 88, 148), (54, 66, 104)),
    'ranger':  ((206, 186, 164), (104, 114, 68), (68, 78, 54)),
}

# (dark, mid, light) for the plain recolor on sleep frames, dead cells and plates too small to grow.
BODY = {cls: (p[2], p[1], p[0]) for cls, p in CASPAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_cascade_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary65', largest=True,
    ),
    'legs': dict(
        outdir='_cascade_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary65', largest=False,
    ),
    'boots': dict(
        outdir='_cascade_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_cascade', largest=False,
    ),
    'helmet': dict(
        outdir='_cascadedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary65', largest=True,
    ),
}


# --- sheet machinery -------------------------------------------------------------------------
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


# --- the grid ---------------------------------------------------------------------------------
def grid_of(comp):
    """The lattice window this component shows.

    Returns (origin_y, origin_x, live) where `live[gr, gc]` is True when all four pixels of the cell
    are opaque body pixels. Anchored at the component's own bounding-box top-left, so the engraving
    travels with the body."""
    ys, xs = np.nonzero(comp)
    if len(ys) == 0:
        return None
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    nr = min((y1 - y0 + 1) // CELL_H, LAT_H)
    nc = min((x1 - x0 + 1) // CELL_W, LAT_W)
    if nr < 2 or nc < 2:
        return None
    live = np.zeros((nr, nc), dtype=bool)
    for gr in range(nr):
        for gc in range(nc):
            y, x = y0 + gr * CELL_H, x0 + gc * CELL_W
            live[gr, gc] = bool(comp[y, x] and comp[y, x + 1] and
                                comp[y + 1, x] and comp[y + 1, x + 1])
    return y0, x0, live


def verifiable_mask(live):
    """A cell is verifiable iff it is live and all three of its antecedents are live. The plate is a
    window onto the orbit; this is the part of the window in which the law can be seen at all."""
    nr, nc = live.shape
    v = np.zeros_like(live)
    if nr < 2:
        return v
    up = live[:-1]
    ul = np.concatenate((np.zeros((nr - 1, 1), bool), up[:, :-1]), axis=1)
    ur = np.concatenate((up[:, 1:], np.zeros((nr - 1, 1), bool)), axis=1)
    v[1:] = live[1:] & up & ul & ur
    return v


def paint_cells_pal(fr, g, orb, crest, shade):
    """Paint the window. Only opaque body pixels are ever touched, so this cannot create strays and
    cannot change the silhouette. RISE is lit on the left pair, FALL on the right."""
    y0, x0, live = g
    nr, nc = live.shape
    for gr in range(nr):
        for gc in range(nc):
            if not live[gr, gc]:
                continue
            hi, lo = (0, 1) if int(orb[gr, gc]) == RISE else (1, 0)
            y, x = y0 + gr * CELL_H, x0 + gc * CELL_W
            for dy in (0, 1):
                put(fr, y + dy, x + hi, crest)
                put(fr, y + dy, x + lo, shade)


def read_cells(fr, g):
    """Read the states back OFF THE PIXELS, relatively and with two independent witnesses.

    Each of the cell's two rows is asked on its own whether the left pixel is brighter than the
    right. Both rows must agree; a cell whose witnesses disagree is returned as -1 and is not
    trusted by anything. The reader is handed the frame and the mask and is told no colours."""
    y0, x0, live = g
    nr, nc = live.shape
    lum = fr[..., :3].astype(np.int32).sum(-1)
    out = np.full((nr, nc), -1, dtype=np.int8)
    for gr in range(nr):
        for gc in range(nc):
            if not live[gr, gc]:
                continue
            y, x = y0 + gr * CELL_H, x0 + gc * CELL_W
            w0 = lum[y, x] - lum[y, x + 1]
            w1 = lum[y + 1, x] - lum[y + 1, x + 1]
            if w0 > 0 and w1 > 0:
                out[gr, gc] = RISE
            elif w0 < 0 and w1 < 0:
                out[gr, gc] = FALL
    return out


# --- the reader: recovering the law -----------------------------------------------------------
def observe(states, ver, radius=1):
    """Every (neighbourhood -> successor) pair the plate shows. The reader's entire input."""
    nr, nc = states.shape
    obs = []
    for gr in range(1, nr):
        for gc in range(nc):
            if not ver[gr, gc]:
                continue
            key = []
            ok = True
            for d in range(-radius, radius + 1):
                c = gc + d
                if c < 0 or c >= nc or states[gr - 1, c] < 0:
                    ok = False
                    break
                key.append(int(states[gr - 1, c]))
            if not ok or states[gr, gc] < 0:
                continue
            obs.append((tuple(key), int(states[gr, gc])))
    return obs


def fit(obs):
    """(table, contradictions). A contradiction is one neighbourhood seen with two successors."""
    tab, bad = {}, 0
    for k, v in obs:
        if k in tab and tab[k] != v:
            bad += 1
        else:
            tab[k] = v
    return tab, bad


def wolfram(tab):
    """Name the recovered radius-one law by its Wolfram number, or None if partly unseen."""
    n = 0
    for l in (0, 1):
        for c in (0, 1):
            for r in (0, 1):
                k = (l, c, r)
                if k not in tab:
                    return None
                n |= tab[k] << ((l << 2) | (c << 1) | r)
    return n


def run_recovered(row, tab):
    """Apply a recovered (possibly partial) table. Unknown neighbourhoods hold their centre."""
    out = row.copy()
    n = len(row)
    for i in range(n):
        k = (int(row[i - 1]) if i > 0 else 0, int(row[i]),
             int(row[i + 1]) if i + 1 < n else 0)
        out[i] = tab.get(k, int(row[i]))
    return out


# --- building --------------------------------------------------------------------------------
def build_frame(fr, a, largest, cls, stem, mode=None, orb=None):
    """Grow and paint one whole frame. Returns a list of (grid, orbit_window) actually engraved."""
    if orb is None:
        orb = orbit(stem, cls, mode)
    crest, shade, _dark = CASPAL[cls]
    out = []
    for comp in comps_of(a, largest):
        if comp.sum() < MIN_PX:
            continue
        g = grid_of(comp)
        if g is None:
            continue
        y0, x0, live = g
        nr, nc = live.shape
        if int(live.sum()) < MIN_CELLS:
            continue
        win = orb[:nr, :nc]
        paint_cells_pal(fr, g, win, crest, shade)
        out.append((g, win))
    return out


def build(base, cfg, cls, stem, mode=None):
    D, M, L = BODY[cls]
    largest = cfg['largest']
    orb = orbit(stem, cls, mode)
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
            continue                              # sleep: plain plate, nothing grown
        build_frame(fr, a, largest, cls, stem, mode, orb)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


CONTROLS = ('static', 'shift', 'random', 'repeat', 'wide', 'reversed')


# --- the acceptance test ------------------------------------------------------------------------
def plate_report(fr, a, largest, cls, stem, mode=None):
    """Read one frame back off its pixels.

    Returns a dict of raw observations, or None when the frame shows too small a window for the law
    to be visible at all. NOTHING IS DECIDED HERE. A single 7x7 window onto the orbit does not
    contain all eight neighbourhoods, so a per-plate verdict would be a verdict about how big the
    component is; the clauses are applied to the observations POOLED OVER THE CLASS, which is the
    scope the law actually claims (one law per class, every plate of every sheet)."""
    res = dict(cells=0, ver=0, wit_bad=0, top=[], bot=[], plates=0)
    for comp in comps_of(a, largest):
        if comp.sum() < MIN_PX:
            continue
        g = grid_of(comp)
        if g is None:
            continue
        _y0, _x0, live = g
        if int(live.sum()) < MIN_CELLS:
            continue
        st = read_cells(fr, g)
        res['wit_bad'] += int(((st < 0) & live).sum())
        nr, nc = live.shape
        ver = verifiable_mask(live) & (st >= 0)
        for gr in range(nr):
            for gc in range(nc):
                if ver[gr, gc]:
                    for d in (-1, 0, 1):
                        c = gc + d
                        if c < 0 or c >= nc or st[gr - 1, c] < 0:
                            ver[gr, gc] = False
                            break
        nver = int(ver.sum())
        res['cells'] += int(live.sum())
        res['ver'] += nver
        if nver < MIN_VERIFIABLE:
            continue
        res['plates'] += 1
        # clause REPLAY needs the split to be made HERE, per plate, so that the training set is
        # genuinely the upper part of each piece of engraving and the test set genuinely the part
        # underneath it. Pooling first and splitting afterwards would leak.
        cut = max(nr // 2, 2)
        for gr in range(1, nr):
            for gc in range(nc):
                if not ver[gr, gc]:
                    continue
                key = (int(st[gr - 1, gc - 1]), int(st[gr - 1, gc]), int(st[gr - 1, gc + 1]))
                (res['top'] if gr < cut else res['bot']).append((key, int(st[gr, gc])))
    return res if res['plates'] else None


def sensitivity(rule_tab, w=LAT_W, h=12, trials=None):
    """Clause SENSITIVITY, run on the RECOVERED table: flip one seed cell, re-run, and watch.

    The flipped cell is taken from the INTERIOR — far enough from the lattice edge that the whole
    light cone stays inside it. That is not a convenience: outside the interior the cone runs into
    the fixed quiescent boundary and is absorbed by it, and a difference that dies against the edge
    of the world says something about the edge, not about the law. Stated rather than hidden.

    Returns (span_ok_by_row_2, ever_died, mean_cells_changed)."""
    base = seed_row('sensitivity-probe', w)
    rows = [base]
    for _ in range(h - 1):
        rows.append(run_recovered(rows[-1], rule_tab))
    sat, died, changed = True, False, []
    idxs = range(h, max(h + 1, w - h)) if trials is None else trials
    for i in idxs:
        p = base.copy()
        p[i] ^= 1
        prow = [p]
        for _ in range(h - 1):
            prow.append(run_recovered(prow[-1], rule_tab))
        tot = 0
        for k in range(h):
            d = np.nonzero(rows[k] ^ prow[k])[0]
            if len(d) == 0:
                died = True
                break
            tot += len(d)
            # SATURATION: information must travel at the fastest speed a radius-one rule permits —
            # one cell per row. At row k SOME cell exactly k away from the flip must differ.
            if not (((i - k) in d) or ((i + k) in d)):
                sat = False
        changed.append(tot)
    mean = float(np.mean(changed)) if changed else 0.0
    return (sat, died, mean)


def gather(mode=None):
    """Read every sheet of the batch back off its pixels. Observations pooled per class."""
    tot = dict(cells=0, ver=0, wit_bad=0, plates=0, skipped=0)
    per = {cls: dict(top=[], bot=[]) for cls in ('warrior', 'mage', 'ranger')}
    for kind, cfg in SLOTS.items():
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                stem = (cfg['dst'] % cls) + suffix
                arr = build(base, cfg, cls, stem, mode)
                for fi in range(SLEEP_FROM):
                    r, c = fi // COLS, fi % COLS
                    sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
                    a = base[sl][..., 3] > 0
                    if not a.any():
                        continue
                    rep = plate_report(arr[sl], a, cfg['largest'], cls, stem, mode)
                    if rep is None:
                        tot['skipped'] += 1
                        continue
                    for k in ('cells', 'ver', 'wit_bad', 'plates'):
                        tot[k] += rep[k]
                    per[cls]['top'].extend(rep['top'])
                    per[cls]['bot'].extend(rep['bot'])
    return tot, per


def accept_all(mode=None):
    label = (mode or 'CASCADE').upper()
    print('== ACCEPTANCE — the 65th axis, CASCADE   [%s]' % label)
    tot, per = gather(mode)

    det_bad = rep_tot = rep_bad = rep_unseen = 0
    r0_ok = 0
    found = {}
    for cls, d in per.items():
        obs = d['top'] + d['bot']
        if not obs:
            continue
        tab, bad = fit(obs)
        det_bad += bad
        found[cls] = wolfram(tab)
        _t0, bad0 = fit([((k[1],), v) for k, v in obs])
        r0_ok += 1 if bad0 > 0 else 0
        ttab, _ = fit(d['top'])
        for k, v in d['bot']:
            rep_tot += 1
            if k not in ttab:
                rep_unseen += 1
            elif ttab[k] != v:
                rep_bad += 1

    nclass = len(found)
    c1 = det_bad == 0 and nclass == 3
    c2 = rep_bad == 0 and rep_tot > 0
    c3 = r0_ok == nclass and nclass == 3
    c4 = all(v is not None and v not in PROJECTIONS for v in found.values()) and nclass == 3
    c6 = tot['wit_bad'] == 0

    print('  plates read %d   (skipped, window too small to show the law: %d)'
          % (tot['plates'], tot['skipped']))
    print('  cells engraved %d   verifiable %d   (%.1f%% of the window — a cell is verifiable '
          'only when all three of its antecedents are on the plate)'
          % (tot['cells'], tot['ver'], 100.0 * tot['ver'] / max(tot['cells'], 1)))
    print('  CLAUSE 1 — DETERMINISM : %d contradicted neighbourhoods of %d observed  -> %s'
          % (det_bad, tot['ver'], 'PASS' if c1 else 'FAIL'))
    print('  CLAUSE 2 — REPLAY      : fitted on the top half of every plate, %d/%d predictions '
          'wrong on the bottom halves (%d unseen, not counted) -> %s'
          % (rep_bad, rep_tot, rep_unseen, 'PASS' if c2 else 'FAIL'))
    print('  CLAUSE 3 — RADIUS      : radius-0 map contradictory for %d/%d classes -> %s'
          % (r0_ok, max(nclass, 1), 'PASS' if c3 else 'FAIL'))
    print('  CLAUSE 4 — DEPENDENCE  : laws recovered from the pixels, per class:')
    for cls in ('warrior', 'mage', 'ranger'):
        v = found.get(cls)
        if v is None:
            print('       %-8s not recoverable (neighbourhoods missing or contradictory)' % cls)
        else:
            print('       %-8s rule %-4d%s' % (cls, v, '  PROJECTION' if v in PROJECTIONS else ''))
    print('                          -> %s' % ('PASS' if c4 else 'FAIL'))

    c5 = bool(found) and nclass == 3
    print('  CLAUSE 5 — SENSITIVITY : one seed cell turned over, re-run on the RECOVERED law:')
    for cls in ('warrior', 'mage', 'ranger'):
        n = found.get(cls)
        if n is None:
            c5 = False
            continue
        tab = {(l, c, r): (n >> ((l << 2) | (c << 1) | r)) & 1
               for l in (0, 1) for c in (0, 1) for r in (0, 1)}
        sat, died, mean = sensitivity(tab)
        grow = mean > 12.0            # strictly more than ONE changed cell per row over 12 rows
        ok = sat and (not died) and grow
        c5 = c5 and ok
        print('       %-8s saturates the light cone: %-5s  never dies: %-5s  cells changed by ONE '
              'flip over 12 rows: %7.1f (a translation scores exactly 12.0)  %s'
              % (cls, sat, not died, mean, 'PASS' if ok else 'FAIL'))
    print('                          (the 64th TALLY answers 1, exactly, by construction)')
    print('                          -> %s' % ('PASS' if c5 else 'FAIL'))
    print('  CLAUSE 6 — LEGIBLE     : %d cells of %d whose two witnesses disagree -> %s'
          % (tot['wit_bad'], tot['cells'], 'PASS' if c6 else 'FAIL'))
    allpass = c1 and c2 and c3 and c4 and c5 and c6
    print('OVERALL [%s]: %s' % (label, 'ALL PASS' if allpass else 'FAIL'))
    return allpass


def controls_report():
    print('== THE SIX CONTROLS, through the same reader\n')
    rows = []
    for mode in (None,) + CONTROLS:
        ok = accept_all(mode)
        rows.append(((mode or 'CASCADE').upper(), ok))
        print()
    print('== SUMMARY')
    for name, ok in rows:
        print('   %-10s %s' % (name, 'ALL PASS' if ok else 'FAIL'))
    axis_ok = rows[0][1]
    ctl_ok = all(not ok for _n, ok in rows[1:])
    print('OVERALL: %s' % ('ALL PASS  (axis passes, all six controls fail)'
                           if (axis_ok and ctl_ok) else 'FAIL'))
    return axis_ok and ctl_ok


def law_report():
    """The three laws, recovered from the pixels of one real sheet each, and named."""
    print('== THE LAW, recovered from the pixels — the rule number is an OUTPUT, never an input')
    tot, per = gather(None)
    for cls in ('warrior', 'mage', 'ranger'):
        obs = per[cls]['top'] + per[cls]['bot']
        tab, bad = fit(obs)
        n = wolfram(tab)
        print('   %-8s recovered %-12s  authored rule %-5d  %s   '
              '(%d observations, %d contradictions)'
              % (cls, ('rule %d' % n) if n is not None else 'incomplete', RULE[cls],
                 'MATCH' if n == RULE[cls] else 'MISMATCH', len(obs), bad))
        if n is not None:
            print('            table  ' + '  '.join(
                '%d%d%d->%d' % (l, c, r, (n >> ((l << 2) | (c << 1) | r)) & 1)
                for l in (1, 0) for c in (1, 0) for r in (1, 0)))
    print('   (the reader is given the pixels and the mask. It is not given these numbers.)')


def dump_cells(cls='warrior', kind='chest', fi=0):
    """One real component, printed as the automaton the eye is looking at."""
    cfg = SLOTS[kind]
    base = load_any('%s.png' % cfg['srcs'][cls])
    stem = cfg['dst'] % cls
    arr = build(base, cfg, cls, stem)
    r, c = fi // COLS, fi % COLS
    sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
    a = base[sl][..., 3] > 0
    comp = comps_of(a, cfg['largest'])[0]
    g = grid_of(comp)
    y0, x0, live = g
    st = read_cells(arr[sl], g)
    ver = verifiable_mask(live)
    print('== %s %s frame %d — read back off the pixels' % (cls, kind, fi))
    print('   #=RISE  .=FALL  (space)=off the plate   lower case = not verifiable')
    for gr in range(live.shape[0]):
        line = ''
        for gc in range(live.shape[1]):
            if not live[gr, gc]:
                line += ' '
            elif st[gr, gc] < 0:
                line += '?'
            else:
                ch = '#' if st[gr, gc] == RISE else '.'
                line += ch if ver[gr, gc] else (ch.lower() if ch == '#' else ',')
        print('   |%s|' % line)
    print('   authored rule %d; the row above causes the row below.' % RULE[cls])


def sens_report():
    print('== SENSITIVITY — WHAT DOES ONE WRONG PIXEL DO?')
    print('   the 64th TALLY : exactly 1 stud changes, and the plate prints its NUMBER.')
    print('   the 65th CASCADE:')
    for cls in ('warrior', 'mage', 'ranger'):
        n = RULE[cls]
        tab = {(l, c, r): (n >> ((l << 2) | (c << 1) | r)) & 1
               for l in (0, 1) for c in (0, 1) for r in (0, 1)}
        for h in (6, 12, 24):
            span_ok, died, mean = sensitivity(tab, h=h)
            print('     %-8s rule %-4d over %2d rows:  mean cells changed %7.1f   '
                  'span>=3 %-5s  dies %s' % (cls, n, h, mean, span_ok, died))
    print('   Redundancy buys the location of an error. Determinism buys the plate for eight bits.')
    print('   Neither is free and this batch prices both.')


def slots_diag(path='_diag_cascade_slots.png', zoom=8):
    cells = []
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            arr = build(base, cfg, cls, cfg['dst'] % cls)
            cells.append(arr[:FH, :FW])
    pad = 6
    w = FW * zoom // 2
    h = FH * zoom // 2
    img = Image.new('RGBA', (pad + len(cells) * (w + pad), pad + h + pad), (24, 24, 28, 255))
    for i, c in enumerate(cells):
        img.paste(Image.fromarray(c).resize((w, h), Image.NEAREST), (pad + i * (w + pad), pad))
    img.save(path)
    print('wrote %s' % path)


def visor_diag(path='_diag_cascade_visor.png', zoom=12):
    cfg = SLOTS['helmet']
    outs = []
    for cls, stem in cfg['srcs'].items():
        base = load_any('%s.png' % stem)
        arr = build(base, cfg, cls, cfg['dst'] % cls)
        raw = arr[16:40, 28:56].copy()
        fin, _ = finish_array(arr.copy(), 'helmet_%s_legendary65.png' % cls)
        outs.append((raw, fin[16:40, 28:56]))
    pad = 6
    h, w = outs[0][0].shape[:2]
    img = Image.new('RGBA', (pad + 2 * len(outs) * (w * zoom + pad), pad + h * zoom + pad),
                    (24, 24, 28, 255))
    for i, (a, b) in enumerate(outs):
        for j, c in enumerate((a, b)):
            img.paste(Image.fromarray(c).resize((w * zoom, h * zoom), Image.NEAREST),
                      (pad + (2 * i + j) * (w * zoom + pad), pad))
    img.save(path)
    print('wrote %s   (raw, finished) x warrior/mage/ranger' % path)


def survive_diag():
    """Reported, never a clause (the 57th/60th/61st rule): how many cells still read correctly after
    the finishing pass, which is an outside light and does not belong in an acceptance test."""
    print('== SURVIVAL THROUGH THE FINISHING PASS (reported, never a clause)')
    for kind in ('chest', 'helmet', 'legs', 'boots'):
        cfg = SLOTS[kind]
        tot = good = 0
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            stem = cfg['dst'] % cls
            arr = build(base, cfg, cls, stem)
            fin, _ = finish_array(arr.copy(), '%s.png' % stem)
            a = base[:FH, :FW][..., 3] > 0
            for comp in comps_of(a, cfg['largest']):
                if comp.sum() < MIN_PX:
                    continue
                g = grid_of(comp)
                if g is None or int(g[2].sum()) < MIN_CELLS:
                    continue
                want = read_cells(arr[:FH, :FW], g)
                got = read_cells(fin[:FH, :FW], g)
                m = g[2] & (want >= 0)
                tot += int(m.sum())
                good += int(((want == got) & m).sum())
        print('   %-7s %4d/%-4d cells still read correctly after finishing  (%.1f%%)'
              % (kind, good, tot, 100.0 * good / max(tot, 1)))


def main():
    if '--law' in sys.argv:
        law_report()
        return
    if '--cells' in sys.argv:
        dump_cells()
        return
    if '--controls' in sys.argv:
        controls_report()
        return
    if '--accept' in sys.argv:
        accept_all()
        return
    if '--sensitivity' in sys.argv:
        sens_report()
        return
    if '--survive' in sys.argv:
        survive_diag()
        return
    if '--sweep' in sys.argv:
        slots_diag()
        visor_diag()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                stem = (cfg['dst'] % cls) + suffix
                arr = build(base, cfg, cls, stem)
                dst = '%s/%s.png' % (outdir, stem)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
