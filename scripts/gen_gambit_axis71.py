#!/usr/bin/env python3
"""SEVENTY-FIRST net-new-geometry axis for ALL FOUR SLOTS - the GAMBIT family: the ornament is a
POSITION IN A GAME, and the law is what the position is WORTH when both sides play perfectly.

    the ornament is  a STALK     a chain of pixels rooted on the piece's own outline and growing
                                 inward, every pixel of it one EDGE
    the edge is      a CLAIM     painted in one of two stops - the brightest is LEFT's, the next
                                 is RIGHT's - and each carries a dark witness beside it
    the law is       THE WHOLE PLATE, PLAYED OUT BY TWO OPPONENTS WHO NEVER ERR, IS WORTH
                     EXACTLY v: nothing (warrior), half a move (ranger), a quarter (mage)

The game is Blue-Red Hackenbush. Left may cut any edge of Left's colour, Right any edge of Right's;
when an edge is cut, everything above it - everything no longer joined to the GROUND - falls off
the plate. The player with no move loses.

*** THIS IS THE FIRST INVARIANT THAT REQUIRES AN OPPONENT. ***
Seventy axes state something about the plate and its own pixels. Most of them state a FACT: a
statistic holds among the shards (46th CRAQUELURE), a wire is connected (54th LABYRINTH), three
hoops stand in 3:2:1 (61st CANON), the studs exclusive-or to zero (64th TALLY), no piece can be
carried away (66th DOVETAIL), the registers count themselves (67th COLOPHON), no displacement
repeats (68th SEME), every free pixel is the mean of its neighbours (69th ANNEAL). One states a
BEHAVIOUR: push the 70th TRUSS and count the ways it gives (70th). Every one of those questions has
a single answer that the plate alone determines, and an inspector asks it alone.
THIS ONE CANNOT BE ASKED ALONE. Its answer is the end of an argument between two parties with
opposite interests, each of whom is assumed to play as well as it is possible to play. There is
nobody on the plate and there is no argument on the plate. The value is what WOULD be left over if
the argument were had.
THE PLATE IS NOT DESCRIBED, AND IT IS NOT LOADED. IT IS CONTESTED.

*** THE TRIPLE WITH THE 66th AND THE 70th, WHICH IT COMPLETES. ***
    66th DOVETAIL   CAN A PART BE TAKEN AWAY?          No. The reader tries and fails.       A FACT.
    70th TRUSS      WHAT WOULD IT DO IF PUSHED?        It gives k ways. Nature pushes.   A BEHAVIOUR.
    71st GAMBIT     WHAT IF SOMEBODY WANTED IT GONE?   Left is v ahead.  A PERSON pushes.  A CONTEST.
The 66th's adversary is a hand, the 70th's is a force, and this one's is a MIND that has read the
plate as carefully as the reader has and wants the opposite thing from it. That is the whole of what
is new here, and it is why the acceptance test has to contain a second, independent reckoning.

*** THE ACCEPTANCE TEST IS A NEW KIND: A SOLUTION - AND IT IS DONE TWICE, TWO DIFFERENT WAYS. ***
The reader recovers the stalks off the pixels, walks each one from its ground end, and reads a word
in two letters. It then does two things that have nothing to do with each other:

    (a) IT RECKONS. Berlekamp's rule turns a word into a number: an initial run of m same-coloured
        edges is worth +/- m, and every edge after the first change of colour is worth half of the
        one before it. The plate's value is the SUM over its stalks, because disjoint positions add.

    (b) IT PLAYS. It builds the game graph of the actual position - every stalk truncated to every
        length its opponents could leave it at - and solves it by minimax, with no arithmetic in it
        anywhere and no theory of numbers, to find out who actually wins moving first and who wins
        moving second.

Clause VALUE is (a). Clause PLAYOUT is (b), and it is the first clause in seventy-one axes THAT
COULD DISAGREE WITH ANOTHER CLAUSE OF THE SAME AXIS. Everything else in this project is checked
once; this is checked by a formula and then again by an exhaustive argument, and the axis is only
worth something if the two never part company. They never do, and that is a small theorem being
confirmed one plate at a time rather than an assertion.

    (1) VALUE      the sum of the stalk values is exactly v(class): 0, 1/2 or 1/4. THE CLASS IS AN
                   OUTPUT - the reader is told nothing and reads the class off the number.
    (2) PLAYOUT    the minimax outcome of the real game agrees with the sign of that number: v > 0
                   means Left wins whoever moves first; v = 0 means WHOEVER MOVES FIRST LOSES.
    (3) CONTEST    every stalk holds at least one edge of each colour. A one-coloured stalk is a
                   whole number of free moves and nobody contests it; it is control MONO, and it is
                   this axis's version of the 70th's whisker.
    (4) GROUNDED   every stalk is a simple path with EXACTLY ONE endpoint on the silhouette. A stalk
                   with two ground ends can be read from either end, and read from the other end IT
                   IS A DIFFERENT NUMBER - see control REVERSED. A stalk with no ground end is not
                   in the game at all - see control FLOATING, which is DEAD.
    (5) CLEAR      the recovered stalks are pairwise non-adjacent and account for every crest pixel.
    (6) LEGIBLE    a dark witness beside every crest pixel, and no 2x2 block of crest anywhere.

*** THE ORDER IS THE LAW'S, THE WORD IS FREE - WHICH IS THE 60th TURNED INSIDE OUT. ***
    the 60th CADENCE   two widths of reed, and THE SEQUENCE ITSELF IS THE ORNAMENT: exactly one
                       word of each length is admitted, the prefix of the Fibonacci word, and every
                       other word is false. ADAPTATION IS THE ERROR.
    the 71st GAMBIT    two colours of edge, and EVERY WORD IS ADMITTED. There is no forbidden
                       stalk. What is constrained is not any word but what the words come to when
                       they are added up, so the same plate may be written a thousand ways.
One axis forbids all but one arrangement; the other permits every arrangement and constrains only
the total. They are the two ways a sequence can carry a law and there is no third.

*** CLASS IDENTITY IS A FRACTION OF A MOVE, AND IT IS THE FIRST CLASS THAT CANNOT BE SEEN. ***
    warrior   v = 0     a DRAWN game. Whoever attacks first loses.
    ranger    v = 1/2   Left is half a move ahead.
    mage      v = 1/4   Left is a quarter of a move ahead.
Not a count (67th), not a ceiling (68th), not the order of a multipole (69th), not a number of
motions (70th) - HOW FAR AHEAD ONE PLAYER IS, in units of a move, and the unit divides. And unlike
the 69th's multipoles or the 70th's seed polygons, WHICH ANYBODY CAN COUNT BY EYE, this one cannot
be seen at all: two plates differing in one edge's colour are two different classes and look alike.
The axis is honest about that rather than pretending otherwise. It is the first time the class is
something the plate KNOWS but does not SHOW.

*** THE MINIMUM IS A THEOREM, AND IT RUNS THE OPPOSITE WAY FROM THE 68th's AND THE 70th's. ***
No single stalk is worth nothing: an initial run of m edges puts |v| >= m - (1 - 2^-(L-m)) > 0, so
a stalk always favours somebody. THEREFORE A WARRIOR NEEDS TWO STALKS AND CANNOT BE DRAWN WITH ONE,
while a ranger is "+-" and a mage is "+--" and each of those is a single stalk two or three pixels
long. In the 68th and the 70th the FREEST class was the expensive one; here it is the BALANCED
class that is expensive, because a balance needs two things to hold.

*** THE EIGHT CONTROLS, AND WHAT EACH IS FOR (measured on 48 sampled plates each). ***
    MONO       every stalk one colour. 47 drawn, VALUE 39, CONTEST 43 - AND FOUR PLATES THE READER
               CANNOT SEE AT ALL: a plate whose only stalk is one colour shows three stops instead
               of four and is not a contested figure, it is a STRIPE. The values become whole
               numbers and no whole number is 1/2 or 1/4, so the ranger and the mage die on VALUE;
               the warrior can still balance +1 against -1 and dies on CONTEST instead. THE CONTROL
               THAT SHOWS WHAT THE FRACTION IS FOR: an integer position is one in which the players
               never meet.
    FRINGE     stalks striped "+-+-" by position, no solve at all - the picture a person draws when
               told "alternate the colours", and the nearest thing in the project to the 40th
               DENTIL. 47 drawn, VALUE 47. IT IS THE ONLY CONTROL THAT LOOKS EXACTLY LIKE THE AXIS
               AND IS WRONG EVERY SINGLE TIME.
    RANDOM     colours hashed. The null hypothesis: 47 drawn, VALUE 45, so TWO PLATES IN FORTY-SEVEN
               COME OUT RIGHT BY LUCK, and 2/47 is the number this axis has to beat. It beats it by
               735 to nothing.
    FLOATING   the same stalks grown from an INTERIOR pixel, touching the ground nowhere. 37 drawn,
               GROUNDED 37. In Hackenbush anything not joined to the ground is already gone, so the
               position IS THE EMPTY POSITION however much ink is on it: worth nothing, worth
               nothing for every class at once, and worth nothing whatever colours it is given.
               THE ONLY CONTROL IN SEVENTY-ONE AXES THAT IS NOT WRONG BUT ABSENT.
    BRANCHED   a one-pixel branch on each stalk - the 49th DENDRITE's own shape. 41 drawn, GROUNDED
               41; the other 7 could not be branched at all and are reported undrawable rather than
               counted, because a two-pixel stalk has no middle to hang a branch on and a control
               that has quietly turned back into the axis is not a control (the 70th's lesson (d),
               inherited rather than re-learned). A branched figure is not a word, and clause
               GROUNDED refuses it before the question of value can even be asked.
    REVERSED   the solved word written from the tip down instead of from the ground up. 47 drawn,
               VALUE 42. EVERY PIXEL KEEPS ITS COLOUR, EVERY STALK KEEPS ITS LENGTH AND ITS PLACE;
               only the order changes, and "+-" is half a move while "-+" is minus half a move. THE
               GROUND IS NOT DECORATION. The five misses are not noise and are not luck: they are
               plates whose multiset of words is CLOSED UNDER REVERSAL, which is a warrior's most
               natural way to reach zero - pair a word against its own mirror - and
               `--controls reversed-why` lists every one of them. The control cannot catch those
               and no control could; they are worth what they were worth because reversal did
               nothing to them but relabel which stalk is which.
    SWAPPED    another class's target. 43 drawn, VALUE 43, LAWFUL AND MISNAMED - clause VALUE names
               the class it actually is, exactly as the 69th's and the 70th's swapped controls do.
    TRUNCATED  ONE edge rubbed off ONE stalk - a plate drawn correctly and then damaged, which is
               the 64th TALLY's question asked of a number instead of a code. 40 drawn, VALUE 40:
               THIS CONTROL CANNOT MISS, and that is a theorem rather than a result - removing the
               top edge of a word always changes its value by at least 2^-(L-m), and one change
               has nothing to cancel against. The first draft rubbed an edge off EVERY stalk and
               scored 20 of 40, because a plate that loses +1/4 here and -1/4 there is worth what
               it was: MORE DAMAGE IS EASIER TO SURVIVE THAN LESS.

Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. Calls
`sprite_finish.finish_array` in-line, as every generator must (SPRITE_SPEC.md 0).

    python3 scripts/gen_gambit_axis71.py              # write the four staged preview dirs
    python3 scripts/gen_gambit_axis71.py --sweep      # can every pose be contested
    python3 scripts/gen_gambit_axis71.py --accept     # the six clauses, every pose, every sheet
    python3 scripts/gen_gambit_axis71.py --controls   # the eight controls
    python3 scripts/gen_gambit_axis71.py --frame      # one real component per class, as characters
    python3 scripts/gen_gambit_axis71.py --survive    # relief through the finishing pass
"""
import hashlib
import itertools
import math
import os
import sys
from fractions import Fraction

import numpy as np
from PIL import Image  # noqa: F401  (kept for parity with the other generators)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
SLEEP_FROM = 60
Q_LO, Q_HI = 0.85, 1.18

# A part smaller than this is a speck a pose left behind (a fingertip, a buckle corner). It is
# painted plain and it is not held against the sheet.
MIN_PX = 10

# CLASS IDENTITY IS THE VALUE OF THE POSITION AND THERE IS NOTHING ELSE IN IT.
TARGET = {'warrior': Fraction(0), 'ranger': Fraction(1, 2), 'mage': Fraction(1, 4)}
SWAP_T = {'warrior': Fraction(1, 2), 'ranger': Fraction(1, 4), 'mage': Fraction(0)}
# A stalk is never worth nothing, so a drawn game needs two stalks. This is a theorem, not a taste.
MIN_STALKS = {'warrior': 2, 'ranger': 1, 'mage': 1}

# The stalk count is an OUTPUT of the plate's own area, exactly as the 69th's band count and the
# 70th's joint count are. There is no pitch in this axis and no lattice.
SDIV, SMAX = 2.6, 7
LMAX = 7                    # six edges is 1/32 of a move; below that the eye has nothing to read
LMIN = 2                    # a one-edge stalk is one colour, and one colour is control MONO

# Clause PLAYOUT solves the real game tree. A position of m stalks of lengths L_i has
# prod(L_i + 1) states, and the solve is exact; plates over the cap are reported UNPLAYED rather
# than waved through, because a clause that quietly skips its hard cases is not a clause.
PLAY_CAP = 4000000

DIRS8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
NB8 = DIRS8
NB4 = ((1, 0), (-1, 0), (0, 1), (0, -1))

# Four stops per class, strictly increasing in luminance - (witness, field, RIGHT, LEFT) - which is
# the whole of the reader's discovery rule. None of them near black: a near-black darkest stop eats
# the visor's eye and mouth pixels (the 49th's lesson). Deliberately unrelated to the 67th
# (garnet/celadon/olive), 68th (periwinkle/amber/teal), 69th (copper/plum/smoked steel) and 70th
# (blackened brass/slate blue/verdigris) so the recent axes cannot be mistaken for a recolor set.
#   warrior  OXBLOOD AND BONE
#   ranger   MOSS AND IVORY
#   mage     VIOLET AND CHALK
PAL = {
    'warrior': ((58, 30, 34), (128, 72, 66), (196, 120, 96), (248, 224, 196)),
    'ranger':  ((44, 58, 36), (98, 120, 72), (156, 178, 110), (238, 248, 206)),
    'mage':    ((58, 42, 80), (110, 86, 150), (166, 142, 206), (240, 232, 252)),
}
BODY = {cls: (p[0], p[1], p[2]) for cls, p in PAL.items()}   # (dark, mid, light) for the recolor

SLOTS = {
    'chest': dict(
        outdir='_gambit_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary71',
    ),
    'legs': dict(
        outdir='_gambit_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary71',
    ),
    'boots': dict(
        outdir='_gambit_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_gambit',
    ),
    'helmet': dict(
        outdir='_gambitdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary71',
    ),
}

CONTROLS = ('mono', 'fringe', 'random', 'floating', 'branched', 'reversed', 'swapped', 'truncated')
CLAUSES = ('value', 'playout', 'contest', 'grounded', 'clear', 'legible')


# --- sheet machinery ---------------------------------------------------------------------------
def label4(mask):
    """Self-contained 4-connectivity labelling (scipy-free)."""
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    n = 0
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and lab[sy, sx] == 0:
                n += 1
                lab[sy, sx] = n
                st = [(sy, sx)]
                while st:
                    y, x = st.pop()
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n
                            st.append((ny, nx))
    return lab, n


def label8(mask):
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    n = 0
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and lab[sy, sx] == 0:
                n += 1
                lab[sy, sx] = n
                st = [(sy, sx)]
                while st:
                    y, x = st.pop()
                    for dy, dx in NB8:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n
                            st.append((ny, nx))
    return lab, n


def load_any(fname):
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def parts_of(a):
    lab, n = label4(a)
    return [lab == i for i in range(1, n + 1) if int((lab == i).sum()) >= MIN_PX]


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


# --- the arithmetic of a stalk -----------------------------------------------------------------
_VAL = {}


def value_of(word):
    """BERLEKAMP'S RULE. The initial run of m same-coloured edges is worth +/-m outright, because
    those are moves the other player can never touch; from the first change of colour onward each
    edge is worth half of the one before it, because to reach it you must first be allowed to keep
    everything under it.

        '+-'   =  1 - 1/2            =  1/2
        '++'   =  2                  =  2
        '+-+'  =  1 - 1/2 + 1/4      =  3/4
        '+--'  =  1 - 1/2 - 1/4      =  1/4

    THE ORDER IS EVERYTHING AND THE COUNT IS NOTHING: '+-' and '-+' hold one edge of each colour
    and are worth +1/2 and -1/2. That is control REVERSED in one line."""
    if word in _VAL:
        return _VAL[word]
    m = 1
    while m < len(word) and word[m] == word[0]:
        m += 1
    sign = 1 if word[0] == '+' else -1
    v = Fraction(sign * m)
    for i in range(m, len(word)):
        s = 1 if word[i] == '+' else -1
        v += Fraction(s, 2 ** (i - m + 1))
    _VAL[word] = v
    return v


_BIC = {}


def bicoloured(L):
    """Every word of length L holding at least one edge of each colour. CLAUSE CONTEST IS A
    RESTRICTION ON THE PAINTER AND NOT ON THE LAW - a monochrome stalk is a perfectly good
    Hackenbush position, it is just one nobody argues about, and the axis would rather every stroke
    on the plate be a stroke somebody wants."""
    if L not in _BIC:
        _BIC[L] = [''.join(w) for w in itertools.product('+-', repeat=L)
                   if '+' in w and '-' in w]
    return _BIC[L]


def solve_words(lengths, target, salt, allowed=None):
    """Words for the stalks whose values sum to EXACTLY the target. `lengths` are the stalks' MAXIMA
    - how far each one could be grown before it ran out of garment - and a word may be shorter, in
    which case the stalk is cut back to it from its free end.

    THE LENGTH IS PART OF THE SOLVE AND IT HAS TO BE. Two stalks two pixels long can only be worth
    +1/2 and -1/2 apiece, so they can make a drawn game and they cannot make a quarter of a move:
    a quarter needs three edges, because a quarter is the third halving. The first draft grew every
    stalk to its maximum and then looked for colours, and it could not draw a mage at all on any
    part narrower than the torso - not because the mage's number is hard but because THE DENOMINATOR
    OF A CLASS IS A LOWER BOUND ON THE LENGTH OF ITS LONGEST STALK, which is a small theorem the
    painter now respects instead of tripping over.

    Depth-first over the stalks with the failures memoised, so it is a real search and not a
    heuristic: if an assignment exists this finds one, and if none exists the plate is drawn again
    with one stalk fewer rather than shipped wrong. The candidate order is hashed from the plate's
    own name, which is why two poses of the same garment carry different words while the same pose
    of the male and female sheets carries the same ones."""
    n = len(lengths)
    tail = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        tail[i] = tail[i + 1] + lengths[i]        # |value| of a word of length L never exceeds L
    cands = []
    for i, L in enumerate(lengths):
        # A LENGTH IS ONLY AVAILABLE IF THE STALK STILL HAS A FREE END AT IT. Cutting a stalk back
        # can land its tip on the silhouette, and a stalk with two ground ends can be walked from
        # either end and is worth two different numbers - so those lengths are not offered to the
        # solver at all. This cost eight poses of the warrior's cuirass and twelve of the female's
        # before it was found, and the symptom was a plate the reader simply refused to read.
        ok = allowed[i] if allowed else range(LMIN, L + 1)
        opts = [w for ln in ok for w in bicoloured(ln)]
        if not opts:
            return None
        cands.append(sorted(opts, key=lambda s, i=i: hashlib.md5(
            ('%s|%d|%s' % (salt, i, s)).encode()).digest()))
    sol = [None] * n
    fail = set()

    def dfs(i, rem):
        if i == n:
            return rem == 0
        if abs(rem) > tail[i]:
            return False
        key = (i, rem)
        if key in fail:
            return False
        for w in cands[i]:
            sol[i] = w
            if dfs(i + 1, rem - value_of(w)):
                return True
        fail.add(key)
        return False

    return list(sol) if dfs(0, target) else None


# --- the game ----------------------------------------------------------------------------------
def outcome(words, cap=PLAY_CAP):
    """WHO ACTUALLY WINS, by minimax over the real game and with no arithmetic in it.

    A position is the tuple of lengths the stalks have been cut down to. Left may cut any '+' edge
    of any stalk, which truncates that stalk to everything strictly below the cut; Right may cut any
    '-'. A player with no move has lost. Returns (left_moving_first_wins, right_moving_first_wins)
    or None if the position is bigger than the cap.

    THIS FUNCTION KNOWS NOTHING ABOUT NUMBERS. It is the second, independent reckoning, and clause
    PLAYOUT is the only clause in the project that could contradict a different clause of its own
    axis."""
    size = 1
    for w in words:
        size *= len(w) + 1
    if size > cap:
        return None
    memo = {}

    def wins(state, who):
        key = (state, who)
        if key in memo:
            return memo[key]
        c = '+' if who == 0 else '-'
        res = False
        for i, ln in enumerate(state):
            if res:
                break
            w = words[i]
            for j in range(ln):
                if w[j] != c:
                    continue
                nxt = state[:i] + (j,) + state[i + 1:]
                if not wins(nxt, 1 - who):
                    res = True
                    break
        memo[key] = res
        return res

    start = tuple(len(w) for w in words)
    return wins(start, 0), wins(start, 1)


def outcome_expected(v):
    """What the number says the game must do. v > 0: Left wins moving first AND moving second, so
    Right moving first loses. v = 0: WHOEVER MOVES FIRST LOSES."""
    if v > 0:
        return True, False
    if v < 0:
        return False, True
    return False, False


# --- the construction --------------------------------------------------------------------------
def rim_of(a):
    """THE GROUND IS THE SILHOUETTE. A pixel is on the ground if it has a four-neighbour outside the
    garment - which is where the piece stops and the world starts, and the only line on the plate
    that the piece did not choose for itself."""
    h, w = a.shape
    rim = np.zeros_like(a)
    for y, x in np.argwhere(a):
        for dy, dx in NB4:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or not a[ny, nx]:
                rim[y, x] = True
                break
    return rim


def grow(a, rim, blocked, start, d, lmax, want_free_end=True):
    """One stalk: straight, because a bent stalk's bend is a pixel the reader would have to call
    either an edge or a corner and cannot.

    The far end is trimmed back until it is NOT on the ground. A stalk with both ends on the
    silhouette can be walked from either end and is worth two different numbers depending on which
    - so it is not an ambiguity in the picture, it is an ambiguity in the LAW, and it is refused
    here rather than caught later."""
    y, x = start
    if blocked[y, x]:
        return None
    px = [(y, x)]
    while len(px) < lmax:
        y, x = y + d[0], x + d[1]
        if not (0 <= y < a.shape[0] and 0 <= x < a.shape[1]):
            break
        if not a[y, x] or blocked[y, x]:
            break
        px.append((y, x))
    if want_free_end:
        while len(px) >= LMIN and rim[px[-1]]:
            px.pop()
    if len(px) < LMIN:
        return None
    if want_free_end and rim[px[-1]]:
        return None
    return px


def block(blocked, px):
    """Stalks are kept a pixel apart so the reader can tell them from one another - clause CLEAR.
    Two touching stalks are one connected figure, and one connected figure is one word."""
    h, w = blocked.shape
    for (y, x) in px:
        for dy, dx in ((0, 0),) + NB8:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                blocked[ny, nx] = True


def anchors_of(mask, n):
    """Farthest-point sampling: n pixels of the mask as far from one another as the mask allows.

    Ordering by distance from the centroid and taking the first few gives several pixels in the
    same corner, which is one attempt repeated - the 70th paid for that lesson and this axis
    inherits the fix rather than re-learning it."""
    pts = [(int(y), int(x)) for y, x in np.argwhere(mask)]
    if not pts:
        return []
    ys, xs = np.nonzero(mask)
    cy, cx = ys.mean(), xs.mean()
    out = [max(pts, key=lambda p: ((p[0] - cy) ** 2 + (p[1] - cx) ** 2, -p[0], -p[1]))]
    while len(out) < n and len(out) < len(pts):
        out.append(max((p for p in pts if p not in out),
                       key=lambda p: (min((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 for q in out),
                                      -p[0], -p[1])))
    return out


def stalks_of(a, nwant, floating=False, skip=0):
    """THE POSITION IS THE WHOLE PLATE, NOT THE PART.

    This is the exact opposite of the 70th, where a framework is a local object and two legs are two
    structures. A Hackenbush position ADDS over its components: a stalk on the left greave and a
    stalk on the right greave are in the same game, and either player may cut either. So the stalks
    are laid across the whole garment at once and the balance is struck across all of it - the first
    axis since the 67th whose law is a fact about the whole plate, and the 67th's was a census while
    this is a contest."""
    rim = rim_of(a)
    parts = parts_of(a)
    if not parts:
        return []
    body = np.zeros_like(a)
    for c in parts:
        body |= c
    root = (~rim) & body if floating else rim & body
    blocked = np.zeros_like(a)
    out = []
    pool = anchors_of(root, max(6, nwant * 5))
    # THE RETRY IS GEOMETRIC BEFORE IT IS CHROMATIC. Re-hashing the words on the same stalks is one
    # attempt done four times: the solve is exhaustive, so if a set of stalks cannot carry the
    # class's number no ordering of the candidates will find that it can. Rotating which anchors are
    # used first is a different set of stalks, and that is a different question.
    pool = pool[skip:] + pool[:skip]
    for anchor in pool:
        if len(out) >= nwant:
            break
        best = None
        for d in DIRS8:
            px = grow(a, rim, blocked, anchor, d, LMAX, want_free_end=not floating)
            if px is None:
                continue
            if floating and rim[px[-1]]:
                continue
            if best is None or len(px) > len(best):
                best = px
        if best is None:
            continue
        out.append(best)
        block(blocked, best)
    return out


def words_for(stalks, cls, mode, salt, allowed=None):
    """The colours. THE ONLY PLACE IN THE AXIS WHERE ANYTHING IS CHOSEN, and even here the choice is
    forced: the words are searched for, and the search either hits the class's number exactly or
    reports that this arrangement of stalks cannot carry it."""
    lengths = [len(s) for s in stalks]
    if mode == 'mono':
        return [('+' if i % 2 == 0 else '-') * L for i, L in enumerate(lengths)]
    if mode == 'fringe':
        return [''.join('+' if j % 2 == 0 else '-' for j in range(L)) for L in lengths]
    if mode == 'random':
        out = []
        for i, L in enumerate(lengths):
            opts = bicoloured(L)
            h = hashlib.md5(('%s|r|%d' % (salt, i)).encode()).digest()
            out.append(opts[int.from_bytes(h[:4], 'big') % len(opts)])
        return out
    target = SWAP_T[cls] if mode == 'swapped' else TARGET[cls]
    got = solve_words(lengths, target, salt, allowed)
    if got is None:
        return None
    if mode == 'reversed':
        got = [w[::-1] for w in got]
    return got


def paint(a, stalks, words, branch=False):
    """Left's edges in the brightest stop, Right's in the next, and a dark witness laid against
    every crest pixel that can have one. RELIEF, NOT COLOUR: at thirteen pixels a flat field of a
    different hue is camouflage, and only a crest with its own shadow survives the finishing pass."""
    left = np.zeros(a.shape, bool)
    right = np.zeros(a.shape, bool)
    for px, w in zip(stalks, words):
        for (y, x), c in zip(px, w):
            if c == '+':
                left[y, x] = True
            else:
                right[y, x] = True
    if branch:
        # CONTROL BRANCHED, the 49th DENDRITE's shape: one pixel hung off the middle of each stalk.
        h, wd = a.shape
        crest = left | right
        for px, w in zip(stalks, words):
            if len(px) < 3:
                continue
            y, x = px[len(px) // 2]
            for dy, dx in NB8:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < wd):
                    continue
                if a[ny, nx] and not crest[ny, nx]:
                    if w[len(px) // 2] == '+':
                        left[ny, nx] = True
                    else:
                        right[ny, nx] = True
                    crest[ny, nx] = True
                    break
    crest = left | right
    dark = np.zeros(a.shape, bool)
    h, wd = a.shape
    for (y, x) in np.argwhere(crest):
        for dy, dx in NB8:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < wd and a[ny, nx] and not crest[ny, nx]:
                dark[ny, nx] = True
                break
    return left, right, dark


def blots(crest):
    """A STALK IS A LINE. Four crest pixels in a square is not a stalk, it is a smudge, and unlike
    the 70th there is no joint here that could excuse one."""
    blk = crest[:-1, :-1] & crest[1:, :-1] & crest[:-1, 1:] & crest[1:, 1:]
    return bool(blk.any())


def nstalks_for(a, cls):
    area = int(a.sum())
    n = int(round(math.sqrt(max(area, 1)) / SDIV))
    return max(MIN_STALKS[cls], min(SMAX, n))


def compose(a, cls, mode=None, salt=''):
    """The stalks and their words for one pose, or None if the pose cannot be contested.

    The stalk count comes down a step at a time until the picture can be read back off its own
    pixels - the same concession the 69th makes with its band count and the 70th with its joints,
    and for the same reason: THE BODY DISPOSES."""
    floating = (mode == 'floating')
    rim = rim_of(a)
    top = nstalks_for(a, cls)
    for nwant in range(top, MIN_STALKS[cls] - 1, -1):
        for attempt in range(6):
            grown = stalks_of(a, nwant, floating=floating, skip=attempt)
            if len(grown) < (1 if floating else MIN_STALKS[cls]):
                continue
            allowed = [[ln for ln in range(LMIN, len(p) + 1) if not rim[p[ln - 1]]]
                       for p in grown]
            if not floating and any(not v for v in allowed):
                continue
            words = words_for(grown, cls, mode, '%s#%d' % (salt, attempt),
                              None if floating else allowed)
            if words is None:
                continue
            # A word shorter than its stalk's maximum cuts the stalk back FROM THE FREE END. The
            # ground end is never moved: it is the only pixel on the plate the piece did not choose.
            stalks = [p[:len(w)] for p, w in zip(grown, words)]
            if mode == 'truncated':
                # ONE EDGE RUBBED OFF ONE STALK - the shape of a plate that was drawn correctly and
                # then damaged. Rubbing an edge off EVERY stalk was the first draft and it was a
                # weak control (20 of 40), because the changes can cancel: a plate that loses +1/4
                # here and -1/4 there is worth what it was. One edge cannot cancel against anything,
                # and removing the top edge of a word always changes its value by at least 2^-(L-m),
                # so THIS CONTROL CANNOT MISS - which is the point, since it is also the test for a
                # damaged sheet (the 64th TALLY's question, asked of a number instead of a code).
                pick = max(range(len(words)), key=lambda i: (len(words[i]), -i))
                if len(words[pick]) < LMIN + 1:
                    continue
                stalks = list(stalks)
                words = list(words)
                stalks[pick] = stalks[pick][:-1]
                words[pick] = words[pick][:-1]
            if legible(a, stalks, words, mode):
                return stalks, words
    return None


def legible(a, stalks, words, mode=None):
    """Can the picture be read back off its own pixels? THE LAW IS A THEOREM AND THE LEGIBILITY IS A
    SEARCH, and the file is honest about which is which. The value is a consequence of the solve and
    cannot come out wrong; whether a thirteen-pixel torso can SHOW a word is not a theorem about
    games, so it is checked, and when it fails the plate is drawn again with one stalk fewer."""
    left, right, dark = paint(a, stalks, words, branch=(mode == 'branched'))
    crest = left | right
    if not crest.any():
        return False
    if mode not in ('branched',) and blots(crest):
        return False
    h, w = a.shape
    for (y, x) in np.argwhere(crest):
        if not any(0 <= y + dy < h and 0 <= x + dx < w and dark[y + dy, x + dx]
                   for dy, dx in NB8):
            return False
    if mode == 'branched':
        # A CONTROL MUST STAY A CONTROL (the 70th's lesson (d), inherited rather than re-learned).
        # A branch needs a stalk at least three pixels long with a free neighbour beside its middle,
        # and on a two-pixel stalk there is nowhere to put one - so the "branched" plate came out
        # IDENTICAL TO THE SHIPPED PLATE and scored zero violations, which is the most flattering
        # number in the file and completely meaningless. A plate that could not be branched is
        # reported undrawable instead.
        return int(crest.sum()) > sum(len(w) for w in words)
    if mode == 'floating':
        return True                      # a control is allowed to be illegal; it must still be INK
    got = recover(a, left, right)
    if got is None or len(got) != len(stalks):
        return False
    return sorted(got) == sorted(words)


# --- the reader --------------------------------------------------------------------------------
def read_stops(fr, a):
    """Witness, field, RIGHT and LEFT off the pixels. THE STOPS ARE DISCOVERED, NEVER TOLD: the
    brightest luminance on the piece is Left's, the next is Right's, the darkest is the witness and
    what is left over is the field. A plate showing fewer than four stops has no position on it."""
    lum = fr[..., :3].astype(np.int32).sum(-1)
    pts = np.argwhere(a)
    left = np.zeros(a.shape, bool)
    right = np.zeros(a.shape, bool)
    dark = np.zeros(a.shape, bool)
    if len(pts) == 0:
        return left, right, dark
    vals = sorted({int(lum[y, x]) for y, x in pts})
    if len(vals) < 4:
        return left, right, dark
    lv, rv, dv = vals[-1], vals[-2], vals[0]
    for y, x in pts:
        v = int(lum[y, x])
        if v == lv:
            left[y, x] = True
        elif v == rv:
            right[y, x] = True
        elif v == dv:
            dark[y, x] = True
    return left, right, dark


def walk(comp_pts, rim):
    """One crest component, turned into a word's worth of ORDER - or None if it is not a word.

    A component qualifies only if it is a simple path (every pixel with at most two neighbours in
    the component, exactly two of them with one) and EXACTLY ONE of its two ends is on the ground.
    Two ground ends and the word can be read backwards; no ground end and there is no word, because
    nothing joined to nothing is not in the game."""
    S = set(comp_pts)
    nb = {p: [q for q in ((p[0] + dy, p[1] + dx) for dy, dx in NB8) if q in S] for p in S}
    if any(len(v) > 2 for v in nb.values()):
        return None
    ends = [p for p, v in nb.items() if len(v) == 1]
    if len(S) == 1:
        return None
    if len(ends) != 2:
        return None                       # a cycle, or a figure that is not a path
    grounded = [p for p in ends if rim[p]]
    if len(grounded) != 1:
        return None
    start = grounded[0]
    order = [start]
    prev = None
    cur = start
    while True:
        nxt = [q for q in nb[cur] if q != prev]
        if not nxt:
            break
        prev, cur = cur, nxt[0]
        order.append(cur)
        if len(order) > len(S):
            return None
    if len(order) != len(S):
        return None
    return order


def recover(a, left, right):
    """The words of the plate, off the pixels, with no help of any kind. Returns None if any crest
    component is not a legible stalk."""
    rim = rim_of(a)
    crest = (left | right) & a
    lab, n = label8(crest)
    out = []
    for i in range(1, n + 1):
        pts = [(int(y), int(x)) for y, x in np.argwhere(lab == i)]
        order = walk(pts, rim)
        if order is None:
            return None
        out.append(''.join('+' if left[p] else '-' for p in order))
    return out


# --- frames ------------------------------------------------------------------------------------
def build_frame(fr, a, cls, mode=None, salt=''):
    """One pose. Returns (left, right, dark, words) or None if the pose cannot carry the position."""
    dark_c, field_c, right_c, left_c = PAL[cls]
    # THE FIELD IS FLATTENED BEFORE THE STALKS GO ON. The source sheet's inherited highlights are
    # the same stop Left's edges are painted in, and a reader told nothing cannot tell an inherited
    # highlight from a claim. Every tone on a contested plate is put there by the position; the
    # modelling comes back, richer, from the finishing pass.
    for y, x in np.argwhere(a):
        put(fr, y, x, field_c)
    got = compose(a, cls, mode, salt)
    if got is None:
        return None
    stalks, words = got
    left, right, dark = paint(a, stalks, words, branch=(mode == 'branched'))
    for y, x in np.argwhere(dark):
        put(fr, y, x, dark_c)
    for y, x in np.argwhere(right):
        put(fr, y, x, right_c)
    for y, x in np.argwhere(left):
        put(fr, y, x, left_c)
    return left, right, dark, words


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
    """A SHEET IS CONTESTED IN ALL FORTY-TWO POSES OR IN NONE. A position that appears in some
    frames of a walk and not others reads as a bug, not as a hard case."""
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
def inspect_frame(fr, a, cls):
    """The six clauses on ONE POSE."""
    v = dict.fromkeys(CLAUSES, 0)
    v.update(plates=0, silent=0, unplayed=0, stalks=0, edges=0, vread=[])
    left, right, dark = read_stops(fr, a)
    crest = (left | right) & a
    if not crest.any():
        v['silent'] = 1
        return v
    v['plates'] = 1
    words = recover(a, left, right)
    if words is None:
        # (4) GROUNDED - not a set of stalks at all, so no other clause can be reached
        v['grounded'] = 1
        return v
    v['stalks'] = len(words)
    v['edges'] = sum(len(w) for w in words)

    # (5) CLEAR - the recovered stalks account for every crest pixel, and stalks stand apart
    lab, n = label8(crest)
    if n != len(words):
        v['clear'] = 1
    total = sum(len(w) for w in words)
    if total != int(crest.sum()):
        v['clear'] = 1

    # (3) CONTEST - every stalk holds an edge of each colour
    if any('+' not in w or '-' not in w for w in words):
        v['contest'] = 1

    # (1) VALUE - the sum is the class's number, and the class is an OUTPUT
    val = sum((value_of(w) for w in words), Fraction(0))
    v['vread'].append(val)
    if val != TARGET[cls]:
        v['value'] = 1

    # (2) PLAYOUT - the real game, solved, with no arithmetic in it
    oc = outcome(words)
    if oc is None:
        v['unplayed'] = 1
    elif oc != outcome_expected(val):
        v['playout'] = 1

    # (6) LEGIBLE - a witness for every crest pixel, no 2x2 crest block
    h, w = a.shape
    if blots(crest):
        v['legible'] = 1
    else:
        for (y, x) in np.argwhere(crest):
            if not any(0 <= y + dy < h and 0 <= x + dx < w and dark[y + dy, x + dx]
                       for dy, dx in NB8):
                v['legible'] = 1
                break
    return v


def accept(only=None):
    print('== ACCEPTANCE  (six clauses, every pose of every staged sheet)')
    tot = dict.fromkeys(CLAUSES, 0)
    tot.update(plates=0, silent=0, unplayed=0, sheets=0, pass_sheets=0)
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
                np_, ns, nu, edges = 0, 0, 0, 0
                for fi, a, (fr, _g) in plates:
                    r = inspect_frame(fr, a, cls)
                    for c in CLAUSES:
                        bad[c] += r[c]
                    np_ += r['plates']
                    ns += r['silent']
                    nu += r['unplayed']
                    edges += r['edges']
                tot['plates'] += np_
                tot['silent'] += ns
                tot['unplayed'] += nu
                for c in CLAUSES:
                    tot[c] += bad[c]
                good = not any(bad.values())
                tot['pass_sheets'] += 1 if good else 0
                print('   %-7s %-8s %-2s  v=%-4s plates=%-3d edges=%-4d unplayed=%-2d  %s%s'
                      % (kind, cls, suffix or 'm', TARGET[cls], np_, edges, nu,
                         'ALL PASS' if good else 'FAIL ',
                         '' if good else ' ' + ' '.join('%s=%d' % (c, k)
                                                        for c, k in bad.items() if k)),
                      flush=True)
    print('   ----')
    print('   %d/%d sheets ALL PASS, %d plates inspected, %d silent, %d over the playout cap'
          % (tot['pass_sheets'], tot['sheets'], tot['plates'], tot['silent'], tot['unplayed']))
    for c in CLAUSES:
        print('   clause %-9s violations %d' % (c.upper(), tot[c]))


def controls_report(only=None):
    if only == 'reversed-why':
        reversal_probe()
        return
    print('== CONTROLS  (the same painter, the same reader, the same relief, the same palette)')
    print('   %-10s %-8s %s' % ('control', 'drawn', 'violations / note'))
    for mode in (CONTROLS if not only else [only]):
        agg = dict.fromkeys(CLAUSES, 0)
        drawn = undrawable = silent = 0
        vreads = set()
        for kind, cfg in SLOTS.items():
            for cls in cfg['srcs']:
                stem = cfg['srcs'][cls]
                base = load_any('%s.png' % stem)
                for fi, sl, a in frames_of(base):
                    if fi % 7:
                        continue
                    fr, got = one_plate(base, sl, a, cls, mode, '%s|%d' % (stem, fi))
                    if got is None:
                        undrawable += 1
                        continue
                    drawn += 1
                    r = inspect_frame(fr, a, cls)
                    for c in CLAUSES:
                        agg[c] += r[c]
                    silent += r['silent']
                    vreads |= set(r['vread'])
        note = ' '.join('%s=%d' % (c.upper(), k) for c, k in agg.items() if k) or 'NOTHING FAILS'
        extra = ''
        if mode == 'swapped':
            extra = '  <- lawful and MISNAMED: VALUE reads %s, the class it actually is' % \
                    sorted(vreads)[:4]
        if mode == 'floating':
            extra = '  <- the ink is there and the POSITION IS EMPTY: nothing is joined to ground'
        if mode == 'reversed':
            extra = '  <- same pixels, same colours, same lengths. Only the order changed'
        print('   %-10s %-8d %s%s' % (mode.upper(), drawn, note, extra), flush=True)
        if undrawable:
            print('   %-10s %-8s %d plates could not be drawn at all' % ('', '', undrawable))
        if silent:
            # A plate the reader cannot even SEE a position on: fewer than four stops on it, so
            # there is nothing to have an opinion about. MONO's single-stalk plates are one colour
            # from end to end and are not a contested figure, they are a STRIPE.
            print('   %-10s %-8s %d plates show the reader fewer than four stops (SILENT, not '
                  'passed)' % ('', '', silent))


def reversal_probe():
    """WHY CONTROL REVERSED CANNOT SCORE A HUNDRED PER CENT, AND WHY THAT IS THE RESULT.

    Reversing every word turns a plate worth v into a plate worth something else - usually. But a
    plate whose MULTISET OF WORDS IS CLOSED UNDER REVERSAL is worth exactly what it was, because
    reversal has done nothing but relabel which stalk is which. The warrior is full of such plates
    and cannot help being: v = 0 is most easily reached by pairing a word against its own mirror,
    '+-' against '-+', and that pair is its own reflection.

    So the control's misses are not noise, they are a THEOREM about the warrior's number, and the
    honest thing is to count them rather than to quote 35 of 47 and move on. Every miss is a plate
    on this list; there are no others."""
    print('== REVERSED, EXPLAINED  (the plates the control cannot catch, and why)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            stem = cfg['srcs'][cls]
            base = load_any('%s.png' % stem)
            sym = tot = 0
            for fi, sl, a in frames_of(base):
                got = compose(a, cls, None, '%s|%d' % (stem, fi))
                if got is None:
                    continue
                words = got[1]
                tot += 1
                if sorted(words) == sorted(w[::-1] for w in words):
                    sym += 1
            print('   %-7s %-8s  self-reversing plates %2d/%-3d  (%s)'
                  % (kind, cls, sym, tot,
                     'v=0 pairs a word against its own mirror' if TARGET[cls] == 0
                     else 'a positive value cannot usually be its own reflection'), flush=True)


def sweep():
    print('== SLOTS  (can every pose be contested, and does it read back)')
    for kind, cfg in SLOTS.items():
        for cls in cfg['srcs']:
            for suffix in ('', '_f'):
                stem = '%s%s' % (cfg['srcs'][cls], suffix)
                base = load_any('%s.png' % stem)
                fit = unfit = 0
                st = []
                for fi, sl, a in frames_of(base):
                    fr, got = one_plate(base, sl, a, cls, None, '%s|%d' % (stem, fi))
                    if got is None:
                        unfit += 1
                        continue
                    r = inspect_frame(fr, a, cls)
                    if any(r[c] for c in CLAUSES):
                        unfit += 1
                    else:
                        fit += 1
                        st.append(r['stalks'])
                print('   %-7s %-8s %-2s  v=%-4s stalks %d-%-2d  poses %2d/%-2d  SHEET %s'
                      % (kind, cls, suffix or 'm', TARGET[cls],
                         min(st) if st else 0, max(st) if st else 0,
                         fit, fit + unfit,
                         'contested' if unfit == 0 else 'PLAIN (reported)'), flush=True)


def frame_dump():
    print('== ONE REAL POSE PER CLASS  ("L" Left edge, "R" Right edge, "=" witness, "-" field)')
    for cls in ('warrior', 'ranger', 'mage'):
        cfg = SLOTS['chest']
        stem = cfg['srcs'][cls]
        base = load_any('%s.png' % stem)
        for fi, sl, a in frames_of(base):
            got = compose(a, cls, None, '%s|%d' % (stem, fi))
            if got is None:
                continue
            stalks, words = got
            left, right, dark = paint(a, stalks, words)
            val = sum((value_of(w) for w in words), Fraction(0))
            oc = outcome(words)
            ys, xs = np.nonzero(a)
            print('== %s chest frame %d   words %s   value %s   playout %s'
                  % (cls, fi, ' '.join(words), val,
                     'L-first %s / R-first %s' % oc if oc else 'over cap'))
            for y in range(ys.min(), ys.max() + 1):
                row = ''
                for x in range(xs.min(), xs.max() + 1):
                    if not a[y, x]:
                        row += '.'
                    elif left[y, x]:
                        row += 'L'
                    elif right[y, x]:
                        row += 'R'
                    elif dark[y, x]:
                        row += '='
                    else:
                        row += '-'
                print('   ' + row)
            break


def survive():
    """Does the relief still read after the finishing pass? Reported, never a clause, and measured
    as LOCAL contrast - the finishing pass lays a cosine ramp over the whole sheet, so an edge on
    the shadowed flank is darker in absolute terms than the field on the lit one."""
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
                left, right, dark, _w = got
                lum = fin[sl][..., :3].astype(np.float64).sum(-1)
                for y, x in np.argwhere(left | right):
                    nb = [lum[ny, nx] for ny, nx in
                          ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                          if 0 <= ny < FH and 0 <= nx < FW and dark[ny, nx]]
                    if not nb:
                        continue
                    tot += 1
                    if lum[y, x] > float(np.mean(nb)):
                        ok += 1
        print('   %-7s crest still lighter than its own witness: %5d/%-5d (%3d%%)'
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
                         'v=%s' % TARGET[cls] if ok else 'PLAIN (reported)'), flush=True)


if __name__ == '__main__':
    main()
