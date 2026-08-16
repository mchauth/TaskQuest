#!/usr/bin/env python3
"""SIXTY-SEVENTH net-new-geometry axis for ALL FOUR SLOTS — the COLOPHON family: the plate is ruled
into registers, each register carries a count of raised bosses, and WHAT THE PLATE COUNTS IS ITSELF.

    the ornament is  a REGISTER   a band of the plate, opened by a 1px sunken groove that runs the
                                  whole width of the piece at that station
                     a BOSS       a raised pip, two pixels of crest on the mid field of a register
    the law is       the number of bosses in register i is the number of registers that hold
                     exactly i bosses

*** THIS IS THE FIRST AXIS WHOSE INVARIANT THE PLATE ITSELF ASSERTS. ***
Sixty-six axes have been sentences said ABOUT a plate by somebody standing in front of it. The
sentence lived in the spec and the pixels were its evidence: a statistic holds among the shards
(46th), a wire is connected (54th), three hoops stand in 3:2:1 (61st), the raised studs
exclusive-or to zero (64th), each row is the image of the row above it (65th), no part can be
carried away (66th). In every one of them the claim is OURS and the plate is only the world the
claim is about. Here the claim is ON THE PLATE. The registers are a statement — "one register holds
no bosses, two registers hold one, one register holds two" — and the acceptance test does not bring
a claim to the pixels, it READS THE CLAIM OFF THE PIXELS and then checks the pixels against it.
The plate is both the assertion and the evidence, and it is the first plate in sixty-seven that
could be FALSE.

*** THE PAIR WITH THE 64th, AND WHY IT IS NOT THE SAME AXIS. ***
    the 64th TALLY     the studs carry a Hamming codeword: the plate CAN BE WRONG AND KNOW IT. Its
                       invariant is REDUNDANCY — the same fact stated twice so that a wound has an
                       address. What is checked is a relation between the plate and a CODE that
                       lives outside it.
    the 67th COLOPHON  the registers carry a census of themselves: the plate CAN SAY SOMETHING
                       FALSE. Its invariant is SELF-REFERENCE — a sentence whose subject is the
                       sentence. Nothing outside the plate is consulted anywhere in the test.
The 64th needs a codebook. This one needs nothing at all, and that is the whole of the difference:
its truth is not conformity to an external table, it is CONSISTENCY WITH ITSELF.

*** THE ACCEPTANCE TEST IS A NEW KIND: A SELF-AUDIT. ***
The reader is handed the pixels and the mask and told nothing — not the class, not the word, not
even the number of registers or which way they run. It discovers the ruling (the grooves are the
only lines that cross the whole piece, so the direction in which they run is recovered and not
given), counts the registers, counts the bosses in each, and then asks the plate's own question of
the plate's own answer.

    (1) RECOVERY     the registers and the boss counts read back off the pixels are exactly what was
                     driven into them, and the number of registers is the length of the word. The
                     orientation is recovered rather than given: EXACTLY ONE of the two readings of
                     the piece may be a ruling, and the number of plates that admitted two is
                     reported (0 of 630).
    (2) DESCRIPTIVE  for every i, count(register i) == #{ j : count(register j) == i }. Computed
                     from the recovered counts alone. THERE IS NO TOLERANCE CONSTANT IN THIS FILE.
    (3) EXHAUSTION   the complete set of self-descriptive words is computed by brute force for every
                     length the body can hold, and the recovered word must be a member of it. The
                     set is an OUTPUT: k=4 has exactly two members, k=5 exactly one, k=6 NONE, k=7
                     exactly one. Every axis before this one chose its three class identities; this
                     one ENUMERATED them, and there are exactly three that a plate this size can
                     hold.
    (4) INDIFFERENCE every boss is slid to a different lawful station inside its own register, the
                     plate is repainted from scratch, and the word read back must be IDENTICAL.
                     THE ONLY THING THIS ORNAMENT MEANS IS HOW MANY. It is the first axis in
                     sixty-seven that is invariant under moving its own elements: pitch, phase,
                     order, spacing, symmetry — every quantity the first sixty-six were made of —
                     are all free here, and the ornament survives their destruction.
    (5) FRAGILE      strike any one boss out of the pixels and DESCRIPTIVE must fail; add one boss
                     to any register and DESCRIPTIVE must fail. NOTHING IN THIS ORNAMENT IS
                     ORNAMENT — the 66th's LOAD-BEARING clause, said in arithmetic.
    (6) LEGIBLE      every boss states itself on two pixels and the reader requires both (a crest
                     cluster of any size but two is illegible, not a boss); and every groove must be
                     COMPLETE across the piece, because an unruled empty band is not a register
                     holding zero bosses, it is no register at all — and a plate that cannot show
                     its empty registers cannot say how long its own word is.

*** THE EIGHT CONTROLS, AND THE TWO THAT DO NOT FAIL. ***
Five of them are FALSE plates: same ruling, same relief, same palette, same pixel budget, different
arithmetic. Two are plates that cannot be READ — they say nothing at all rather than something false,
which is a different way of being useless and had to be shown separately. One is LAWFUL and cannot be
AFFORDED. Measured over the same 630 plates the axis is measured on:

    BLANK      ruled, and no boss driven anywhere — the word 0000. Its digits sum to zero where a
               self-descriptive word of length k must sum to k. 630 plates, 630 violations. The lower
               collapse boundary, and it is plain banding: the 11th FLUTING with grooves.
    UNIFORM    one boss in every register, 1111. THE HONEST NEAR MISS: the same ruling, the same
               relief, the same busyness, one more pixel moved than the axis itself, and a lie — four
               registers hold one boss each, so a true plate would read 0400. It IS the 13th STUDWORK
               and the 40th DENTIL, and it is THE CONTROL THAT PROVES THIS AXIS IS ARITHMETIC AND NOT
               DECORATION. 630 violations.
    SUMONLY    a word whose digits sum to k and which is not self-descriptive, FOUND by search rather
               than hand-written so it cannot be accused of being chosen to fail (0022, 00122). It
               passes the check every reader writes first — a census must account for k registers, so
               surely summing to k is the law — and it is FALSE. SUM = k IS NECESSARY AND NOT
               SUFFICIENT. THE BUG THIS AXIS WOULD HAVE SHIPPED WITH, and at 13px it is invisible.
               525 violations.
    PERMUTED   the true word's digits, reordered (0202 for 2020, 2101 for 1210, 12002 for 21200).
               Every register holds a count that genuinely occurs in the piece and the MULTISET of
               counts is exactly the axis's, so the plate's histogram is right and the plate is wrong.
               THE CONTROL THAT SEPARATES THE AXIS'S TWO BLINDNESSES: where a boss sits inside its
               register is nothing (clause INDIFFERENCE), and where a REGISTER sits is the whole law.
               595 violations.
    OFFBYONE   one boss struck from the true word (1020, 1110, 11200). Invisible at this scale, and
               false — and the only control that also fails FRAGILE from the other side, since 630 of
               its plates become lawful again if a boss is put BACK. 1890 violations, the worst score
               in the set.
    SINGLE     the axis's own arithmetic, said with a boss ONE pixel wide instead of two. NOT ONE
               PLATE IN TWENTY-FOUR SHEETS CAN BE READ: a lone crest pixel is not a boss to a reader
               that requires two witnesses, so every sheet goes silent and there is nothing left to be
               right or wrong about. This is what clause LEGIBLE is FOR, and it is why a boss is a
               domino.
    UNRULED    the axis's own arithmetic, with the groove left off the registers that hold no bosses —
               the obvious economy, and it is fatal. AN EMPTY BAND THAT IS NOT RULED IS NOT A REGISTER
               HOLDING ZERO, IT IS NO REGISTER AT ALL: the word comes out short, its length is wrong,
               and every sheet goes silent. 2020 would be read as a two-register plate. THE PLATE HAS
               TO BE ABLE TO SHOW WHAT IT DOES NOT HAVE.
    LONG       the k=7 word 3211000, which is perfectly lawful — it is the only self-descriptive word
               of its length and clause EXHAUSTION finds it. THE ONE CONTROL THAT DOES NOT FAIL, AND
               THAT IS ITS FINDING: eighteen of twenty-four sheets cannot hold seven registers at all
               and go silent, and the six that speak are torsos. The axis's maximum word length is not
               an arithmetic limit but a BODILY one.

*** CLASS IDENTITY IS A NUMBER THAT DESCRIBES ITSELF. ***
    warrior   2020     four registers: two hold none, none holds one, two hold two
    mage      21200    five registers: two hold none, one holds one, two hold two
    ranger    1210     four registers: one holds none, two hold one, one holds two
Not a colour (the 64th put its identity in the mid tone), not a rule (the 65th's was an automaton),
not a graph (the 66th's was a spanning tree), not a ratio (the 61st's was 3:2:1). And it is the first
class identity in sixty-seven that was not CHOSEN: clause EXHAUSTION proves that these three are ALL
THERE ARE at any length a sprite can carry, so the assignment is a bijection onto a complete set and
there was never a fourth to pick from. WHICH class gets which is the one free decision, and it was
made by the bodies: the mage's word is the long one because the mage's helmet is a tall hat with seven
registers in it, and the ranger's is 1210 because the ranger's helmet is a six-row hood with three.
Read across the brow it holds four, and 2020 — two registers of two bosses — does not fit in it.

*** THE AXIS HAS A MINIMUM, AND THE MINIMUM IS A THEOREM: FOUR REGISTERS. ***
    THERE IS NO SELF-DESCRIPTIVE WORD OF LENGTH ONE, TWO OR THREE. Clause EXHAUSTION does not
    estimate this, it enumerates all 1 + 4 + 27 candidates and finds nothing.
A sabaton is six rows of ragged diagonal; the pair of them, ruled as one piece, holds three registers
and — read across the toes instead, where a groove would have to cross the gap between the feet and
has no pixels there to be dark in — none that can be recovered. So THE BOOTS OF ALL THREE CLASSES ARE
RULED AND LEFT EMPTY, and they are reported rather than faked: six sheets of banded sabatons that
carry the ornament and say nothing with it, which is this axis's own BLANK control worn as an item,
exactly as the 66th wore its GLUE there. This is the first limit in the project that is not about
pixels: the 66th's joint did not fit a boot because a dovetail is four pixels across, and one could
imagine a smaller dovetail. NO ARITHMETIC CLOSES THIS GAP. The boot misses by one register and the
set of words that would fit it is provably EMPTY.

*** A SHEET IS RULED IN ALL FORTY-TWO POSES OR IN NONE. ***
An ornament that appears in some frames of a walk cycle and not others does not read as an item with
a hard case; it reads as a BUG. So the fit is decided per SHEET and not per plate, and the test of fit
is not "can it be driven" but "can it be driven AND READ BACK EXACTLY" — a ruling that cannot be
recovered is a plate that says nothing, and a plate that says nothing does not ship as a plate that
speaks. Two frames of a slashing female torso (fi 55) and two of a walking mage's chausses very nearly
took four whole sheets down with them for want of a three-pixel-wide register, which is what
`bands_search` exists for.

*** ONE PIECE, ONE RULING, ONE WORD — and the reader recovers which way it runs. ***
A pair of chausses is two shapes on the sheet and one garment, and the census is of the GARMENT: a
register runs across BOTH legs, so a boss on the left leg and a boss on the right are two bosses in
one register. Ruling the two shapes separately was the first draft and it was wrong twice over — it
gave the reader a CHOICE (two legs ruled alike are also a lawful ruling of the pair, so the same
pixels carried two different words and nothing in them said which was meant), and it made the sabaton
hopeless. Which WAY the ruling runs is left to the body — a helmet is eleven pixels wide and six tall,
and ruled the short way it holds three registers where four are needed — and the reader is told
nothing about it: it tries both readings of the piece and takes the one that is a ruling, and clause
RECOVERY reports how many plates admitted two. Measured: 0 of 630. THE ORIENTATION IS AN OUTPUT.

*** DISTINCTNESS. ***
  * 50th RUNIC — ruled inscription registers and a sixteen-letter alphabet, and it is this axis's
    NOTATION and its explicit predecessor. The 50th asserts NO LAW: any string of runes is a lawful
    plate, which is exactly what a vocabulary is. Here the registers are the same furniture and
    there is a law in them, and the law's subject is the registers themselves.
  * 64th TALLY — a message with a check. External codebook, error LOCATION. See the pair above.
  * 40th DENTIL / 13th STUDWORK — the UNIFORM control. Both are rows of raised marks at a fixed
    pitch, and PITCH IS WHAT THIS AXIS DOES NOT HAVE. Slide every boss anywhere in its band and the
    plate is unchanged (clause INDIFFERENCE); slide one dentil and the dentil course is broken.
  * 60th CADENCE — the ORDER of two widths is the ornament, a formal language. There the arrangement
    is everything; here the arrangement inside a register is nothing and only the CARDINALITY counts.
  * 53rd GRANULATION — the first axis whose element size is an output. This is the first whose
    element COUNT is the output, and the count is a count OF THE PLATE'S OWN PARTS.
  * 61st CANON — 3:2:1, a ratio among three hoops: a relation between parts. Still a sentence said
    from outside. Nothing in the 61st refers to the 61st.
  * 11th FLUTING — the BLANK control, i.e. this axis with nothing said.

Authoring philosophy identical to gen_canon_axis61.py ... gen_dovetail_axis66.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing added, nothing removed,
silhouette untouched — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Twenty-third generator to call it in-line, after axes 45-66.

Run from repo root:
  python3 scripts/gen_colophon_axis67.py
  python3 scripts/gen_colophon_axis67.py --words      # the complete self-descriptive sets, k=1..8
  python3 scripts/gen_colophon_axis67.py --cells      # ASCII of one real component, registers marked
  python3 scripts/gen_colophon_axis67.py --accept     # the six clauses over all 24 sheets
  python3 scripts/gen_colophon_axis67.py --controls   # the six controls through the same reader
  python3 scripts/gen_colophon_axis67.py --survive    # legibility through the finishing pass
  python3 scripts/gen_colophon_axis67.py --sweep      # slots + ruling diagnostics
Then QA (examples):
  python3 scripts/sprite_qa.py _colophon_legendary_preview/shirt_warrior_legendary67.png
  python3 scripts/sprite_qa.py _colophondome_helmet_preview/helmet_mage_legendary67.png --y-min 2
  python3 scripts/sprite_qa.py _colophon_boots_preview/boots_warrior_legendary_colophon.png --y-max 63
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

# A register cannot be shorter than TWO rows. One row is the groove, which must cross the whole
# piece, and one row is the field the bosses stand on. At one row the groove eats the field and the
# LONG control is what that looks like.
BAND_MIN = 2
# A boss is TWO pixels of crest, side by side along the register. Not one: a single crest pixel is
# indistinguishable from the noise the finishing pass leaves behind, and clause LEGIBLE is the
# statement that no single pixel decides how many bosses a register holds.
BOSS_W = 2
# Two bosses must not be 4-ADJACENT, or their crest runs into one cluster and two bosses become one.
# Diagonal contact is allowed and is not a concession: a 4-connected reader keeps diagonal clusters
# apart, and the 64th TALLY paid for this lesson the other way round — two-symbol relief belongs on a
# DIAGONAL, because in rows it fuses into fluting bars. It is also what makes the axis affordable: a
# sabaton is four pixels wide, so two bosses side by side need five columns and will never fit,
# while two bosses cornerwise need three columns and two rows and fit exactly.
BOSS_ADJ = 1        # forbidden Manhattan distance between the pixels of two different bosses
# How many pixels a row must have before it can be a groove. ONE, and that is not laziness: in the
# right reading of a ruled piece a fully dark row can only BE a groove, because the field is mid and
# the bosses are crest, so there is nothing for a wider threshold to protect against. It was three
# for an afternoon and it cost the axis every helmet in the batch — the crown of a dome is two pixels
# wide, so the first groove of every helmet was invisible and no helmet had a ruling at all. What a
# threshold here would really be doing is discriminating the WRONG reading, and that job belongs to
# the structural test below, which is exact, and to clause RECOVERY, which measures it.
GROOVE_MIN = 1

# CLASS IDENTITY IS A NUMBER THAT DESCRIBES ITSELF. Clause EXHAUSTION proves these are the only
# three at any length a sprite can carry.
WORDS = {'warrior': (2, 0, 2, 0), 'mage': (2, 1, 2, 0, 0), 'ranger': (1, 2, 1, 0)}

# Three metals, three temperatures, no stop anywhere near black (the visor's eye and mouth pixels
# are black and a near-black darkest stop swallows them — the 49th's lesson).
#   warrior  GARNET      deep red iron
#   mage     CELADON     cold green-grey glaze
#   ranger   OLIVE BRASS warm dark brass
# Darkest channel-sums 206 / 224 / 194. Deliberately unrelated to the 64th (bronze/ice/bone), the
# 65th (argent/gold/rose) and the 66th (basalt/porphyry/sandstone) so that the four most recent
# axes cannot be mistaken for a recolor set.
PAL = {
    'warrior':  ((212, 152, 156), (150, 78, 86), (96, 52, 58)),
    'mage':     ((176, 214, 196), (96, 142, 126), (56, 88, 80)),
    'ranger':   ((196, 190, 132), (128, 120, 64), (78, 74, 42)),
}
DARK, MID, CREST = 0, 1, 2       # the reader's three stops, darkest first

BODY = {cls: (p[2], p[1], p[0]) for cls, p in PAL.items()}

SLOTS = {
    'chest': dict(
        outdir='_colophon_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary67', largest=True,
    ),
    'legs': dict(
        outdir='_colophon_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary67', largest=False,
    ),
    'boots': dict(
        outdir='_colophon_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_colophon', largest=False,
    ),
    'helmet': dict(
        outdir='_colophondome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary67', largest=True,
    ),
}


# --- the arithmetic ----------------------------------------------------------------------------
def is_descriptive(word):
    """The law, and the whole of the law: digit i counts the registers holding exactly i bosses."""
    k = len(word)
    for i in range(k):
        if word[i] != sum(1 for c in word if c == i):
            return False
    return True


def all_descriptive(k):
    """Every self-descriptive word of length k, by brute force over all k**k digit strings.

    Nothing is assumed — not that the digits sum to k (they must, and that is a THEOREM here and not
    an input), not that digit k-1 is zero, not that a solution exists. k=6 has none, and the empty
    answer is as much an output as the others."""
    out = []
    for w in itertools.product(range(k), repeat=k):
        if is_descriptive(w):
            out.append(w)
    return out


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


# --- the piece: components in reading order, cropped, and turned the long way -------------------
class Part(object):
    """One component of the piece, cropped to its own box and turned so its rows are its registers.

    `flip` records whether the crop was transposed. It is not a secret: the reader recovers it by
    trying both readings and finding the one in which the grooves cross the piece.

    WHICH WAY A PIECE IS RULED IS NOT A TASTE AND IT IS NOT THE LONG AXIS EITHER — that was the
    first draft, and it cost the axis its boots. Stacking the registers along the long way maximises
    how MANY registers a part can hold and minimises how WIDE they are, and a register two pixels
    wide has nowhere to put two bosses. A sabaton is wide and flat: ruled the long way it holds
    seven registers and not one boss. So the ornament tries both readings and keeps whichever one
    will actually carry the word, and the reader, which is told nothing, does exactly the same."""

    def __init__(self, comp):
        ys, xs = np.nonzero(comp)
        self.y0, self.x0 = int(ys.min()), int(xs.min())
        self.y1, self.x1 = int(ys.max()), int(xs.max())
        self.box = comp[self.y0:self.y1 + 1, self.x0:self.x1 + 1].copy()
        self.orient(False)

    def orient(self, flip):
        self.flip = flip
        self.mask = self.box.T.copy() if flip else self.box.copy()
        self.h, self.w = self.mask.shape
        return self

    def to_frame(self, r, c):
        """A working-coordinate pixel, back in the frame."""
        if self.flip:
            return self.y0 + c, self.x0 + r
        return self.y0 + r, self.x0 + c

    def cap(self):
        return self.h // BAND_MIN


def piece_mask(a, largest):
    """THE CENSUS IS OF THE PIECE, AND THE PIECE IS ONE THING however many pieces of it a pose leaves
    visible. A pair of chausses is two shapes on the sheet and one garment; a register runs across
    BOTH legs, and a boss on the left leg and a boss on the right leg are two bosses in one register.

    This was not the first draft either, and the first draft was wrong twice over. Ruling each shape
    separately gave the ornament more places to put things — and it gave the READER a choice: two legs
    ruled alike are also a lawful ruling of the pair, so the same pixels carried two different words
    and there was nothing in them to say which was meant. It also made the sabaton impossible, since a
    single boot is four pixels wide and six tall and holds three registers at the outside. Ruled as
    one piece, the pair is fourteen pixels across, and read across the toes it holds seven. ONE PIECE,
    ONE RULING, ONE WORD, AND NOTHING FOR THE READER TO CHOOSE."""
    live = [c for c in comps_of(a, largest) if c.sum() >= MIN_PX]
    if not live:
        return None
    m = live[0].copy()
    for c in live[1:]:
        m |= c
    return m


def parts_of(a, largest):
    """The piece, as the one part it is. Kept plural because every diagnostic in the file speaks of
    parts, and because a piece with nothing big enough on it is no parts at all."""
    m = piece_mask(a, largest)
    return [] if m is None else [Part(m)]


def allotments(caps, k):
    """Every way of sharing k registers among the parts, at least one each, none over its capacity.

    Every part carries at least one register: a part of the piece with no ruling on it is a part of
    the piece that is not talking, and the reader — which cannot know it was meant to be silent —
    would count the registers of a shorter word. The plans come out biggest-part-first, which is the
    order that gives the widest registers the most work."""
    n = len(caps)
    if n == 0 or k < n or sum(caps) < k:
        return
    def rec(i, left, acc):
        if i == n - 1:
            if 1 <= left <= caps[i]:
                yield acc + [left]
            return
        room = sum(caps[i + 1:])
        lo = max(1, left - room)
        hi = min(caps[i], left - (n - 1 - i))
        for v in range(hi, lo - 1, -1):
            for r in rec(i + 1, left - v, acc + [v]):
                yield r
    for plan in rec(0, k, []):
        yield plan


def bands_of(part, nb, priority=None):
    """Split a part's rows into exactly nb bands, none shorter than BAND_MIN. Row r0 of each band is
    its groove; the rest is the field the bosses stand on.

    A part's rows rarely divide evenly, and the leftover rows have to go somewhere. `priority` is the
    order in which bands are offered them; the ornament tries the busiest registers first, because a
    register that must hold two bosses needs field and a register that holds none does not. Which
    band got the slack is not part of the law — the reader recovers the ruling from the grooves
    themselves, and clause RECOVERY requires only that the registers come out within one row of each
    other, which even division guarantees however the slack is shared."""
    h = part.h
    base, extra = h // nb, h % nb
    if base < BAND_MIN:
        return None
    order = list(priority) if priority is not None else list(range(nb))
    fat = set(order[:extra])
    out, r = [], 0
    for b in range(nb):
        hb = base + (1 if b in fat else 0)
        out.append((r, r + hb - 1))
        r += hb
    return out


# --- driving the bosses ------------------------------------------------------------------------
def boss_sites(part, band, taken, reverse=False):
    """Every station in this band where a boss could be driven, given the ones already driven.

    A station is BOSS_W neighbouring body pixels in one row of the band's field, no station pixel
    within BOSS_GAP of a pixel already spoken for. `reverse` walks the band the other way and is
    what clause INDIFFERENCE uses to prove the stations do not matter."""
    r0, r1 = band
    rows = list(range(r0 + 1, r1 + 1))
    if reverse:
        rows = rows[::-1]
    sites = []
    for r in rows:
        cols = list(range(part.w - BOSS_W + 1))
        if reverse:
            cols = cols[::-1]
        for c in cols:
            px = [(r, c + i) for i in range(BOSS_W)]
            if not all(part.mask[y, x] for y, x in px):
                continue
            bad = False
            for y, x in px:
                for dy, dx in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (y + dy, x + dx) in taken:
                        bad = True
                        break
                if bad:
                    break
            if not bad:
                sites.append(px)
    return sites


def drive_band(part, band, need, taken, reverse):
    """Drive `need` bosses into one register, BACKTRACKING.

    First-fit is not good enough and the reason is worth writing down: a register three rows tall on
    a slashing torso has room for two bosses cornerwise and only if the FIRST one is put in the right
    place. Greedy takes the leftmost station, which blocks its own neighbour, and the plate is then
    declared impossible — a whole sheet of chests was going out ruled and empty for exactly this,
    with nothing wrong with the bodies at all. The station a boss ends up in means nothing (clause
    INDIFFERENCE), so the search may hunt for any arrangement that fits."""
    if need == 0:
        return []
    for px in boss_sites(part, band, taken, reverse):
        taken2 = set(taken)
        taken2.update(px)
        rest = drive_band(part, band, need - 1, taken2, reverse)
        if rest is not None:
            return [px] + rest
    return None


def drive(part, bands, counts, reverse=False):
    """Drive the counts into the bands. Returns a list of boss pixel-pairs per band, or None if the
    body has no room for what the word asks — in which case the plate is REPORTED, never shipped as
    a plate that quietly says something false."""
    taken = set()
    out = []
    for band, need in zip(bands, counts):
        got = drive_band(part, band, need, taken, reverse)
        if got is None:
            return None
        for px in got:
            taken.update(px)
        out.append(got)
    return out


def tones_for(part, bands, bosses, counts=None, mode=None):
    """The tone map of one part: DARK on the groove rows, CREST on the bosses, MID everywhere else.

    Every register is ruled whether or not it holds a boss. An empty band that is not ruled is not a
    register holding zero, it is no register at all, and the plate would be unable to say how long
    its own word is — clause LEGIBLE."""
    t = np.full(part.mask.shape, MID, dtype=np.int8)
    t[~part.mask] = -1
    for bi, (r0, _r1) in enumerate(bands):
        if mode == 'unruled' and counts is not None and counts[bi] == 0:
            continue        # the control: an empty register left unopened
        row = t[r0]
        row[part.mask[r0]] = DARK
    for band_bosses in bosses:
        for px in band_bosses:
            keep = px[:1] if mode == 'single' else px
            for r, c in keep:
                t[r, c] = CREST
    return t


def paint_tones(fr, part, t, pal):
    crest, mid, dark = pal
    stops = {DARK: dark, MID: mid, CREST: crest}
    for r in range(part.h):
        for c in range(part.w):
            v = int(t[r, c])
            if v < 0:
                continue
            y, x = part.to_frame(r, c)
            put(fr, y, x, stops[v])


def paint_plain(fr, part, pal):
    """A part the word will not fit: ruled at the top and otherwise plain, and REPORTED."""
    crest, mid, dark = pal
    for r in range(part.h):
        for c in range(part.w):
            if not part.mask[r, c]:
                continue
            y, x = part.to_frame(r, c)
            put(fr, y, x, dark if r == 0 else mid)


# --- the reader --------------------------------------------------------------------------------
def read_part(fr, comp, flip):
    """Registers and boss counts, off the pixels, under one of the two readings of a component.

    Returns (grooves, counts, illegible) or None when this reading yields no ruling at all. The
    three stops are discovered from the plate, never told: they are the darkest, middle and
    lightest luminances present in the component."""
    ys, xs = np.nonzero(comp)
    y0, x0, y1, x1 = int(ys.min()), int(xs.min()), int(ys.max()), int(xs.max())
    box = comp[y0:y1 + 1, x0:x1 + 1]
    lum = fr[..., :3].astype(np.int32).sum(-1)[y0:y1 + 1, x0:x1 + 1]
    if flip:
        box, lum = box.T.copy(), lum.T.copy()
    vals = sorted({int(lum[r, c]) for r, c in np.argwhere(box)})
    if len(vals) < 2:
        return None
    stops = (vals[0], vals[len(vals) // 2], vals[-1])

    def stop_of(r, c):
        v = int(lum[r, c])
        return int(np.argmin([abs(v - s) for s in stops]))

    h, w = box.shape
    grooves, illegible = [], 0
    for r in range(h):
        cols = [c for c in range(w) if box[r, c]]
        if len(cols) < GROOVE_MIN:
            continue
        if all(stop_of(r, c) == DARK for c in cols):
            grooves.append(r)
    # A RULING, and not merely some dark rows. Three exact facts, no tolerance anywhere: the ruling
    # opens at the part's very first row, there are at least two registers, and no register is
    # shorter than BAND_MIN — a groove and a field. This is what tells the two readings of a part
    # apart: a column of a ruled part is dark only where it crosses the grooves, so the wrong
    # reading of a part almost never opens on its own first row with two clear registers under it.
    # ALMOST never is not a proof, so it is MEASURED instead of assumed — clause RECOVERY requires
    # that exactly ONE reading of every component is a ruling, and it is reported as a count.
    if len(grooves) < 2 or grooves[0] != 0:
        return None
    spans = [grooves[i + 1] - grooves[i] for i in range(len(grooves) - 1)] + [h - grooves[-1]]
    if min(spans) < BAND_MIN:
        return None
    counts = []
    for gi, r0 in enumerate(grooves):
        r1 = grooves[gi + 1] - 1 if gi + 1 < len(grooves) else h - 1
        sub = np.zeros((r1 - r0, w), dtype=bool)
        for r in range(r0 + 1, r1 + 1):
            for c in range(w):
                if box[r, c] and stop_of(r, c) == CREST:
                    sub[r - r0 - 1, c] = True
        lbl, n = label4(sub)
        good = 0
        for i in range(1, n + 1):
            if int((lbl == i).sum()) == BOSS_W:
                good += 1
            else:
                illegible += 1
        counts.append(good)
    return grooves, counts, illegible


def read_component(fr, comp):
    """Recover the reading as well as the registers. EXACTLY ONE of the two readings of a component
    may produce a ruling; if both do, the plate is ambiguous and says nothing."""
    got = [(flip, read_part(fr, comp, flip)) for flip in (False, True)]
    live = [(flip, g) for flip, g in got if g is not None]
    if len(live) != 1:
        return None
    return live[0]


def read_piece(fr, a, largest):
    """The piece's word, and its illegibilities. One piece, one ruling, one word."""
    m = piece_mask(a, largest)
    if m is None:
        return None
    got = read_component(fr, m)
    if got is None:
        return None
    flip, (_grooves, counts, illegible) = got
    if not counts:
        return None
    return tuple(counts), illegible, [flip]


# --- building ---------------------------------------------------------------------------------
CONTROLS = ('blank', 'uniform', 'sumonly', 'permuted', 'offbyone', 'single',
            'unruled', 'long')


def word_for(cls, mode):
    """The word this plate will carry. The controls are all words too — that is the point of them:
    the ornament, the relief, the palette and the pixel budget are held fixed and only the
    ARITHMETIC is changed."""
    w = WORDS[cls]
    k = len(w)
    if mode is None:
        return w
    if mode == 'blank':
        return tuple([0] * k)
    if mode == 'uniform':
        return tuple([1] * k)
    if mode == 'sumonly':
        return _sumonly(k)
    if mode == 'permuted':
        return tuple(list(w[1:]) + [w[0]])
    if mode == 'offbyone':
        i = max(range(k), key=lambda j: w[j])
        return tuple(w[j] - (1 if j == i else 0) for j in range(k))
    if mode == 'long':
        return (3, 2, 1, 1, 0, 0, 0)
    if mode in ('single', 'unruled'):
        return w        # the arithmetic is the axis's own; what is broken is how it is SAID
    raise ValueError(mode)


def _sumonly(k):
    """Any word of length k whose digits sum to k and which is not self-descriptive. Found, not
    hand-written, so the control cannot be accused of being chosen to fail."""
    for w in itertools.product(range(k), repeat=k):
        if sum(w) == k and not is_descriptive(w) and max(w) <= 2:
            return w
    for w in itertools.product(range(k), repeat=k):
        if sum(w) == k and not is_descriptive(w):
            return w
    raise RuntimeError('no sumonly word for k=%d' % k)


def bands_greedy(part, nb, counts):
    """Every register gets BAND_MIN rows, and every row left over goes to the registers that have
    something to hold, busiest first.

    Even division is the first thing tried and it is right nearly always. It is not always right: a
    slashing torso read the long way gives a three-row register three pixels wide, and two bosses
    cornerwise need three columns AND three rows. Two frames of a walk cycle failed on that and took
    three whole sheets down with them (a sheet is ruled in all forty-two poses or in none). The
    registers of a plate therefore need not be the same height — nothing in the law says they are,
    only the reader's grip on which way the plate is ruled, and that grip is a groove on the first
    row and two clear registers under it, not a measurement."""
    h = part.h
    if h < nb * BAND_MIN:
        return None
    hs = [BAND_MIN] * nb
    left = h - nb * BAND_MIN
    order = [b for b in sorted(range(nb), key=lambda b: -counts[b]) if counts[b] > 0]
    order = order or list(range(nb))
    i = 0
    while left > 0:
        b = order[i % len(order)]
        if hs[b] < BAND_MIN + 2 or i >= 4 * nb:
            hs[b] += 1
            left -= 1
        i += 1
        if i > 8 * nb:
            hs[-1] += left
            left = 0
    out, r = [], 0
    for hb in hs:
        out.append((r, r + hb - 1))
        r += hb
    return out


def bands_search(part, nb, limit=400):
    """Every way of cutting the part into nb registers of at least BAND_MIN rows, most even first.

    The last resort, and it earns its keep on exactly the plates that have no room to spare: two
    slashing female torsos are ruled by nothing else in this file."""
    h = part.h
    if h < nb * BAND_MIN:
        return
    extra = h - nb * BAND_MIN
    cands = []
    for add in itertools.product(range(extra + 1), repeat=nb):
        if sum(add) != extra:
            continue
        hs = [BAND_MIN + a for a in add]
        cands.append((max(hs) - min(hs), hs))
        if len(cands) > 20000:
            break
    cands.sort(key=lambda t: t[0])
    for _spread, hs in cands[:limit]:
        out, r = [], 0
        for hb in hs:
            out.append((r, r + hb - 1))
            r += hb
        yield out


def drive_part(p, nb, counts, reverse):
    """Rule one part into nb registers holding these counts. Even ruling first, always."""
    plans = [bands_of(p, nb, sorted(range(nb), key=lambda b: -counts[b])),
             bands_of(p, nb, list(range(nb))),
             bands_greedy(p, nb, counts)]
    seen = set()
    for bands in plans:
        if bands is None or tuple(bands) in seen:
            continue
        seen.add(tuple(bands))
        bosses = drive(p, bands, counts, reverse)
        if bosses is not None:
            return bands, bosses
    for bands in bands_search(p, nb):
        if tuple(bands) in seen:
            continue
        seen.add(tuple(bands))
        bosses = drive(p, bands, counts, reverse)
        if bosses is not None:
            return bands, bosses
    return None


def try_plan(parts, word, flips, reverse):
    """One reading of every part and one sharing of the registers, driven or refused."""
    for p, f in zip(parts, flips):
        p.orient(f)
    caps = [p.cap() for p in parts]
    for have in allotments(caps, len(word)):
        painted, i, ok = [], 0, True
        for p, nb in zip(parts, have):
            counts = tuple(word[i:i + nb])
            i += nb
            got = drive_part(p, nb, counts, reverse)
            if got is None:
                ok = False
                break
            painted.append((p, got[0], counts, got[1]))
        if ok:
            return painted
    return None


def plan_piece(parts, word, reverse=False):
    """Ruling and bosses for the piece, or None if the body will not hold the word.

    Two things are searched: which way the piece is read (upright before turned, so a plate is
    turned only when it must be) and how its rows are shared among the registers. The first
    arrangement that carries the word wins, because which arrangement it is means nothing — clause
    INDIFFERENCE is the statement that the ornament has no geometry to get right.

    Returns (painted, silent) — `silent` for the caller's sake; a piece is now all or nothing."""
    if not parts:
        return None, []
    for flips in ((False,), (True,)):
        got = try_plan(parts, word, flips, reverse)
        if got is not None:
            return got, []
    return None, list(parts)


def build_piece(fr, a, cls, largest, mode=None, reverse=False):
    """Rule the piece and drive its word. Returns the plan actually painted, or None when the piece
    was ruled and left empty and must be REPORTED."""
    parts = parts_of(a, largest)
    if not parts:
        return None
    word = word_for(cls, mode)
    painted, silent = plan_piece(parts, word, reverse)
    for p in silent:
        p.orient(False)
        paint_plain(fr, p, PAL[cls])
    if painted is None:
        return None
    for (p, bands, counts, bosses) in painted:
        paint_tones(fr, p, tones_for(p, bands, bosses, counts, mode), PAL[cls])
    return painted


def sheet_carries(base, cfg, cls, mode=None):
    """Can EVERY active frame of this sheet carry the word?

    All or nothing, per sheet, and this is a rendering fact rather than an arithmetic one. An item
    whose ornament appears in some frames of a walk cycle and not others does not read as an item
    with a hard case, it reads as a BUG — the plate flickers. So a slot that cannot say the word in
    all forty-two poses does not say it in any of them: it ships ruled and EMPTY, which is this
    axis's own BLANK control worn as an item, and it is REPORTED rather than faked."""
    for fi, sl, a in frames_of(base, cfg):
        fr = np.zeros((FH, FW, 4), dtype=base.dtype)
        D, M, L = BODY[cls]
        recolor(base[sl], fr, a, D, M, L)
        painted = build_piece(fr, a, cls, cfg['largest'], mode)
        if painted is None:
            return False
        # DRIVING IT IS NOT ENOUGH — IT HAS TO BE READABLE. A ruling can be driven into a pair of
        # sabatons read across the toes and then be unrecoverable, because a register that lands on
        # the gap between the boots has no pixels to be dark in and the reader never sees the groove.
        # A plate that cannot be read is a plate that says nothing, and a plate that says nothing is
        # not shipped as a plate that speaks.
        driven = tuple(c for (_p, _b, counts, _bo) in painted for c in counts)
        got = read_piece(fr, a, cfg['largest'])
        if got is None or got[0] != driven or got[1]:
            return False
    return True


def build(base, cfg, cls, mode=None, reverse=False, force=None):
    D, M, L = BODY[cls]
    largest = cfg['largest']
    rule = sheet_carries(base, cfg, cls, mode) if force is None else force
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
        if rule:
            build_piece(fr, a, cls, largest, mode, reverse)
        else:
            for p in parts_of(a, largest):
                p.orient(False)
                paint_plain(fr, p, PAL[cls])
    return out, rule


# --- the acceptance test -----------------------------------------------------------------------
def frames_of(base, cfg):
    for fi in range(SLEEP_FROM):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        a = base[sl][..., 3] > 0
        if a.any():
            yield fi, sl, a


def one_plate(base, sl, a, cfg, cls, mode=None, reverse=False):
    """One frame's plate, built in isolation: the frame, the plan, and nothing else."""
    fr = np.zeros((FH, FW, 4), dtype=base.dtype)
    D, M, L = BODY[cls]
    recolor(base[sl], fr, a, D, M, L)
    painted = build_piece(fr, a, cls, cfg['largest'], mode, reverse)
    return fr, painted


def accept(mode=None, verbose=True, limit=None):
    res = dict(sheets=0, silent=0, plates=0, unruled=0, registers=0, bosses=0,
               recovery=0, ambiguous=0, descriptive=0, exhaustion=0, indifference=0,
               vacuous=0, moved=0, stations=0,
               fragile_strike=0, fragile_add=0, strikes=0, legible=0, words={}, flips={})
    sets = {k: all_descriptive(k) for k in range(2, 9)}
    for kind, cfg in SLOTS.items():
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                res['sheets'] += 1
                # A SHEET IS TESTED ONLY IF IT SHIPS SPEAKING. A slot that cannot say the word in all
                # forty-two poses ships ruled and EMPTY, and a plate that says nothing is not offered
                # to a test of what it says — it is REPORTED.
                if not sheet_carries(base, cfg, cls, mode):
                    res['silent'] += 1
                    continue
                n = 0
                for fi, sl, a in frames_of(base, cfg):
                    if limit is not None and n >= limit:
                        break
                    n += 1
                    fr, painted = one_plate(base, sl, a, cfg, cls, mode)
                    if painted is None:
                        res['unruled'] += 1
                        continue
                    res['plates'] += 1
                    driven = tuple(c for (_p, _b, counts, _bo) in painted for c in counts)
                    res['registers'] += len(driven)
                    res['bosses'] += sum(driven)
                    # (1) RECOVERY — and, first, that the piece admits exactly ONE reading
                    m = piece_mask(a, cfg['largest'])
                    readings = [read_part(fr, m, f) for f in (False, True)]
                    if sum(1 for r in readings if r is not None) != 1:
                        res['ambiguous'] += 1
                    got = read_piece(fr, a, cfg['largest'])
                    if got is None:
                        res['recovery'] += 1
                        continue
                    word, ill, flips = got
                    if word != driven:
                        res['recovery'] += 1
                    # (6) LEGIBLE
                    res['legible'] += ill
                    # (2) DESCRIPTIVE
                    if not is_descriptive(word):
                        res['descriptive'] += 1
                    # (3) EXHAUSTION
                    k = len(word)
                    if k not in sets:
                        sets[k] = all_descriptive(k)
                    if word not in sets[k]:
                        res['exhaustion'] += 1
                    res['words'][word] = res['words'].get(word, 0) + 1
                    for f in flips:
                        res['flips'][f] = res['flips'].get(f, 0) + 1
                    # (4) INDIFFERENCE — the same word with every boss driven somewhere else
                    fr2, p2 = one_plate(base, sl, a, cfg, cls, mode, reverse=True)
                    got2 = read_piece(fr2, a, cfg['largest']) if p2 is not None else None
                    if got2 is None or got2[0] != word:
                        res['indifference'] += 1
                    else:
                        sa = {tuple(px) for (_p, _b, _c, bo) in painted for band in bo for px in
                              [tuple(band_px) for band_px in band]}
                        sb = {tuple(px) for (_p, _b, _c, bo) in p2 for band in bo for px in
                              [tuple(band_px) for band_px in band]}
                        res['stations'] += len(sa)
                        res['moved'] += len(sa - sb)
                        if sa and sa == sb:
                            # nothing actually moved, so the clause proved nothing on this plate
                            res['vacuous'] += 1
                    # (5) FRAGILE — strike one boss out of the PIXELS, one at a time
                    for f2, _grp in _strikes(fr, a, cfg['largest']):
                        res['strikes'] += 1
                        g3 = read_piece(f2, a, cfg['largest'])
                        if g3 is not None and is_descriptive(g3[0]):
                            res['fragile_strike'] += 1
                    # (5) FRAGILE — add one boss to any register, in the arithmetic
                    for i in range(k):
                        w2 = list(word)
                        w2[i] += 1
                        if is_descriptive(tuple(w2)):
                            res['fragile_add'] += 1
    if verbose:
        _report(mode, res, sets)
    return res


def _strikes(fr, a, largest):
    """Every plate that is this plate with exactly one boss struck out of the pixels."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    out = []
    for comp in comps_of(a, largest):
        if comp.sum() < MIN_PX:
            continue
        vals = sorted({int(lum[y, x]) for y, x in np.argwhere(comp)})
        if len(vals) < 3:
            continue
        crest, mid = vals[-1], vals[len(vals) // 2]
        midrgb = None
        for y, x in np.argwhere(comp):
            if int(lum[y, x]) == mid:
                midrgb = fr[y, x, :3].copy()
                break
        if midrgb is None:
            continue
        pts = {(int(y), int(x)) for y, x in np.argwhere(comp) if int(lum[y, x]) == crest}
        seen = set()
        for (y, x) in sorted(pts):
            if (y, x) in seen:
                continue
            grp = [(y, x)]
            if (y, x + 1) in pts:
                grp.append((y, x + 1))
            seen.update(grp)
            f2 = fr.copy()
            for (gy, gx) in grp:
                f2[gy, gx, :3] = midrgb
            out.append((f2, grp))
    return out


def _report(mode, res, sets):
    name = 'AXIS' if mode is None else ('CONTROL ' + mode.upper())
    print('== %s' % name)
    print('   sheets speaking %2d of %2d   (ruled and EMPTY, reported, never tested: %d)'
          % (res['sheets'] - res['silent'], res['sheets'], res['silent']))
    print('   plates %4d   registers %5d   bosses %5d'
          % (res['plates'], res['registers'], res['bosses']))
    print('   (1) RECOVERY      %4d violations   (%d plates admitted two readings)'
          % (res['recovery'], res['ambiguous']))
    print('   (2) DESCRIPTIVE   %4d violations' % res['descriptive'])
    print('   (3) EXHAUSTION    %4d violations' % res['exhaustion'])
    print('   (4) INDIFFERENCE  %4d violations   (%d of %d stations re-driven; %d plates where '
          'nothing moved)'
          % (res['indifference'], res['moved'], res['stations'], res['vacuous']))
    print('   (5) FRAGILE       %4d of %d struck plates still lawful, %4d added bosses still lawful'
          % (res['fragile_strike'], res['strikes'], res['fragile_add']))
    print('   (6) LEGIBLE       %4d illegible crest clusters' % res['legible'])
    bad = (res['recovery'] + res['ambiguous'] + res['descriptive'] + res['exhaustion']
           + res['indifference'] + res['fragile_strike'] + res['fragile_add'] + res['legible'])
    print('   words read: %s' % (', '.join('%s x%d' % (''.join(map(str, w)), n)
                                           for w, n in sorted(res['words'].items())) or '(none)'))
    print('   readings recovered: %s' % (', '.join(
        '%s x%d' % ('transposed' if f else 'upright', n)
        for f, n in sorted(res['flips'].items())) or '(none)'))
    if bad:
        verdict = 'FAIL (%d clause violations)' % bad
    elif res['plates'] == 0:
        verdict = ('DEAD - not one plate in twenty-four sheets can be READ at all, so there is '
                   'nothing to be right or wrong about')
    elif res['silent'] and mode is not None:
        verdict = ('LAWFUL BUT UNPAYABLE - %d of %d sheets go silent'
                   % (res['silent'], res['sheets']))
    else:
        verdict = 'ALL PASS'
    print('   >>> %s' % verdict)
    return bad


def controls_report():
    print('The axis, then the six controls, through the same reader.\n')
    accept(None)
    for m in CONTROLS:
        print()
        accept(m)


# --- diagnostics -------------------------------------------------------------------------------
def words_report():
    print('== EXHAUSTION: every self-descriptive word, by brute force over all k**k digit strings')
    for k in range(2, 9):
        sol = all_descriptive(k)
        print('   k=%d  %6d candidates  %d solution%s  %s'
              % (k, k ** k, len(sol), '' if len(sol) == 1 else 's',
                 ', '.join(''.join(map(str, w)) for w in sol) or '(none)'))
    print('\n   the three class words, and there are no others a sprite can hold:')
    for cls, w in WORDS.items():
        print('     %-8s %-6s k=%d  self-descriptive %s'
              % (cls, ''.join(map(str, w)), len(w), is_descriptive(w)))
    print('\n   THEOREM, not an input: a self-descriptive word\'s digits sum to its length.')
    for k in range(2, 9):
        for w in all_descriptive(k):
            assert sum(w) == k
    print('     verified for every solution found above.')


CH = 'sprites/preview_assets/char'


def dump_cells():
    kind, cls = 'chest', 'warrior'
    cfg = SLOTS[kind]
    base = load_any('%s.png' % cfg['srcs'][cls])
    for fi, sl, a in frames_of(base, cfg):
        fr, painted = one_plate(base, sl, a, cfg, cls)
        if painted is None:
            continue
        print('== %s %s frame %d, word %s' % (kind, cls, fi, ''.join(map(str, WORDS[cls]))))
        p, bands, counts, bosses = painted[0]
        t = tones_for(p, bands, bosses, counts)
        glyph = {-1: '.', DARK: '=', MID: '-', CREST: 'O'}
        for r in range(p.h):
            tag = ''
            for bi, (r0, r1) in enumerate(bands):
                if r == r0:
                    tag = '  <- register %d opens (holds %d)' % (bi, counts[bi])
            print('   ' + ''.join(glyph[int(t[r, c])] for c in range(p.w)) + tag)
        print('   reading: %s ("=" groove, "O" boss, "-" field)'
              % ('transposed' if p.flip else 'upright'))
        got = read_piece(fr, a, cfg['largest'])
        print('   read back off the pixels: %s' % (''.join(map(str, got[0])) if got else 'NOTHING'))
        return


def slots_diag():
    print('== SLOTS  (registers a piece can hold, and whether its class word fits)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (cfg['srcs'][cls], suffix))
                fit = unfit = 0
                caps = []
                for fi, sl, a in frames_of(base, cfg):
                    parts = parts_of(a, cfg['largest'])
                    caps.append(sum(p.cap() for p in parts))
                    fr, painted = one_plate(base, sl, a, cfg, cls)
                    ok = painted is not None
                    if ok:
                        driven = tuple(c for (_p, _b, cs, _bo) in painted for c in cs)
                        got = read_piece(fr, a, cfg['largest'])
                        ok = got is not None and got[0] == driven and not got[1]
                    if ok:
                        fit += 1
                    else:
                        unfit += 1
                print('   %-7s %-8s %-2s  word %-6s  capacity %2d-%2d  frames fit %2d/%2d  '
                      'SHEET %s'
                      % (kind, cls, suffix or 'm', ''.join(map(str, WORDS[cls])),
                         min(caps), max(caps), fit, fit + unfit,
                         'ruled + spoken' if unfit == 0 else 'RULED AND EMPTY (reported)'))


def survive_diag():
    """Does the RELIEF still read after the finishing pass? Reported, never a clause.

    It is measured RELATIVELY and it has to be. The finishing pass lays a cosine ramp across the
    whole sheet, so a groove on the lit shoulder ends up brighter than a field pixel in the shadow
    under the arm and the strict three-stop reader — which is the right reader for the acceptance
    test, where nothing has been shaded yet — decodes 0% of finished chests. That number says
    nothing about whether a player can see the ornament. What a player can see is LOCAL CONTRAST, so
    what is measured here is local contrast: is each groove still darker than the field of its own
    register, and is each boss still lighter than the field of its own row."""
    print('== SURVIVAL through the finishing pass (reported, not a clause; local contrast)')
    print('   grooves darker than their own register, bosses lighter than their own row')
    for kind, cfg in SLOTS.items():
        gt = gok = bt = bok = 0
        for cls in cfg['srcs']:
            base = load_any('%s.png' % cfg['srcs'][cls])
            if not sheet_carries(base, cfg, cls):
                continue
            arr, _ruled = build(base, cfg, cls)
            dst = '_tmp/%s_%s.png' % (cfg['dst'] % cls, kind)
            fin, _info = finish_array(arr.copy(), dst)
            for fi, sl, a in frames_of(base, cfg):
                fr0 = np.zeros((FH, FW, 4), dtype=base.dtype)
                D, M, L = BODY[cls]
                recolor(base[sl], fr0, a, D, M, L)
                painted = build_piece(fr0, a, cls, cfg['largest'])
                if painted is None:
                    continue
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for (p, bands, counts, bosses) in painted:
                    bosspx = {q for band in bosses for px in band for q in px}
                    for bi, (r0, r1) in enumerate(bands):
                        gr = [p.to_frame(r0, c) for c in range(p.w) if p.mask[r0, c]]
                        fld = [p.to_frame(r, c) for r in range(r0 + 1, r1 + 1)
                               for c in range(p.w) if p.mask[r, c] and (r, c) not in bosspx]
                        if gr and fld:
                            gt += 1
                            if (np.mean([lum[y, x] for y, x in gr])
                                    < np.mean([lum[y, x] for y, x in fld])):
                                gok += 1
                        for px in bosses[bi]:
                            r = px[0][0]
                            row = [p.to_frame(r, c) for c in range(p.w)
                                   if p.mask[r, c] and (r, c) not in bosspx]
                            if not row:
                                continue
                            bt += 1
                            here = np.mean([lum[y, x] for y, x in
                                            [p.to_frame(rr, cc) for rr, cc in px]])
                            if here > np.mean([lum[y, x] for y, x in row]):
                                bok += 1
        print('   %-7s grooves %4d/%-4d (%3d%%)   bosses %4d/%-4d (%3d%%)'
              % (kind, gok, gt, (100 * gok // gt) if gt else 0,
                 bok, bt, (100 * bok // bt) if bt else 0))


def main():
    if '--words' in sys.argv:
        words_report()
        return
    if '--cells' in sys.argv:
        dump_cells()
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
                arr, ruled = build(base, cfg, cls)
                dst = '%s/%s.png' % (outdir, stem)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-62s opaque_px=%-6d finish=%s/%s  %s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant'],
                         'word %s' % ''.join(map(str, WORDS[cls])) if ruled
                         else 'RULED AND EMPTY (reported)'))


if __name__ == '__main__':
    main()
