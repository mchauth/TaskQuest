#!/usr/bin/env python3
"""FORTY-NINTH net-new-geometry axis for ALL FOUR SLOTS — the DENDRITE / FROST-FERN family
(recursive branching crystal): a network of raised STEMS from which FRONDS spring at 45 degrees in
alternating succession, each frond splitting at its tip into a FORK of two shorter members — the
branching habit of a native-metal dendrite in ore, and of frost on a cold window.

    the ornament is  TRUNK   (generation 0 — the continuous vertical stem, the root of the tree)
                   + FROND   (generation 1 — springing from the trunk at 45 deg, alternating left
                              and right up the stem)
                   + FORK    (generation 2 — the two shorter members a frond splits into at its
                              tip, bracketing their parent's heading)
                   + GROUND  (the dark matrix the crystal grew in, carrying the CAST SHADOW of the
                              branch that overhangs it)

*** THIS IS THE FIRST BRANCHING AXIS IN FORTY-NINE — the first whose motif is a TREE. ***
The subject of this axis is DESCENT: an element's identity comes from its distance from the root
ALONG THE STRUCTURE, not from its position on the plate and not from its size class. Nothing in the
prior forty-eight has that relation, and the three families it could be confused with each fail it
in a different way:

  * The ruled-cell axes (11th-45th) stamp a CLOSED FIGURE on a lattice — a diamond, a hexagon, a
    scale, an arch, a bay. A closed figure has an inside and an outside; a tree has neither. Every
    part of a stamped cell is coequal, so there is no parent and no child anywhere in the family.
  * The line axes — 11th fluting, 22nd wave, 24th spiral, 23rd meander, 30th cable, 39th guilloche,
    42nd strigil, 43rd gadroon, 44th zigzag — run UNBRANCHED members. A meander turns corners and a
    cable crosses its neighbour, but no line in any of them ever SPLITS: follow a strigil flute or a
    guilloche ribbon from end to end and it has exactly two ends and no forks. A dendrite frond has
    one parent end and many child ends.
  * The 46th craquelure is the only prior axis with genuine 3-way junctions, and it is precisely
    the instructive near miss. A craquelure net is a PARTITION: its junctions are unordered, every
    hairline is coequal with every other, there is no root, no growth direction, and cutting one
    member leaves a net rather than orphaning a subtree. A dendrite is ACYCLIC and DIRECTED — it
    has a stem, the fronds hang off it in one sense, and the forks hang off the fronds.
  * The 48th cosmati is the other near miss and is worth stating carefully, because it also puts
    several sizes on the plate. Its three ranks are DISJOINT STAMPED ELEMENTS whose rank is their
    size; they touch nothing and are related only by the bay they share. Here the ranks are
    CONNECTED and the rank IS the connection — a fork member is a fork member because of what it
    grows out of, and it would still be one if it were the same length as its parent.
  * The 47th mokume nests closed loops inside one another. Nesting is containment, not descent:
    no lamina grows out of another, and every lamina is the same thickness.

TAPER, and the one honest compromise at this scale. A real dendrite's members get THINNER with each
generation. At 13px across a torso the trunk is already 1px, so thickness cannot encode rank, and
the axis therefore spends its two remaining channels on it: LENGTH (trunk continuous, frond FROND_L
px, fork BARB_L px) and VALUE (the metal ramp steps down one stop per generation, and a frond dims
again along its own length as it runs away from the stem). Rank is legible in a 4px limb that only
has room for a stem and one fork member, because the stem is the brightest thing on the piece and
the fork the dimmest.

RELIEF. The crystal stands PROUD of its matrix and the matrix is flat, so the relief is carried by
a CAST SHADOW rather than by shading the ornament itself: a ground pixel whose upper-left neighbour
belongs to the tree takes the darker of the two bedding tones. This is the first axis to light
itself by what the ornament DOES TO THE GROUND instead of by a gradient across the ornament — which
is the only relief cue available to a figure that is 1px wide everywhere.

Geometry. The field is periodic with period (TRUNK_P, FROND_P) and the tile is not written as a
per-pixel membership test but GROWN, by a recursive `grow()` that paints a member and then spawns
its children — the code expresses descent because descent is the subject. Trunks stand at
lx % TRUNK_P == 0; a right frond springs at ly % FROND_P == 0 and a left frond at the half period,
so the fronds alternate up the stem as a fern's pinnae do.

Per slot it lands as the 49th distinct axis:
  * CHEST  — dendrite cuirass: stems up the breast, fronds interlocking across the ribs.
  * LEGS   — dendrite chausses: a crystal stem down each thigh.
  * BOOTS  — dendrite sabatons: frost fern over the instep.
  * HELMET — dendrite dome: stems over the skull, fronds spreading at the temples.

Authoring philosophy identical to gen_cosmati_axis48.py / gen_mokume_axis47.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside the
existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi >= 60) get a plain body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` — the canonical chain (no-smooth shading with protect=False,
shirt pauldron/gorget/chest-plate separation, helmet black eye+mouth visor with NO full-silhouette
rim, hat brim/crease folds for open headgear). See CONTEXT.md "MANDATORY — the finishing pass".

Run from repo root:
  python3 scripts/gen_dendrite_axis49.py
  python3 scripts/gen_dendrite_axis49.py --swatch   # bare motif on a test plate, no sheets written
  python3 scripts/gen_dendrite_axis49.py --sweep    # frond-pitch sweep on a real torso AND a real leg
Then QA (examples):
  python3 scripts/sprite_qa.py _dendrite_legendary_preview/shirt_warrior_legendary49.png
  python3 scripts/sprite_qa.py _dendritedome_helmet_preview/helmet_mage_legendary49.png --y-min 2
  python3 scripts/sprite_qa.py _dendrite_boots_preview/boots_warrior_legendary_dendrite.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# --- Dendrite constants ---------------------------------------------------------------------
# TRUNK_P is the horizontal stem pitch and FROND_P the vertical interval between fronds on one
# stem. The failure mode of a BRANCHING axis is unlike any of the three before it. The 46th needed
# a SMALL pitch (an aperiodic field must show several cells before the eye accepts they differ);
# the 47th needed a pitch set by the THINNEST part (a contour nest's band count is the half
# thickness); the 48th needed a pitch big enough to hold all three ranks in ONE bay. This axis
# needs a pitch at which A FROND STILL HAS ROOM TO CARRY A CHILD — because the moment a frond is
# reduced to bare primaries the tree has only two generations, and a stem with unbranched diagonal
# ticks is not a dendrite, it is a herringbone, i.e. the 16th twill with a spine. The constant that
# governs that is FROND_P (see --sweep); TRUNK_P is then set to 2*FROND_L + 1 so opposing fronds
# from adjacent stems interlock with a 1px matrix gap and never fuse into a lattice.
# Swept 12/10/8/6/4 (--sweep) on a real torso AND a real leg, and this axis is the first whose
# pitch is bounded on BOTH sides by a collapse into an OLDER AXIS rather than into mush:
#   12  the torso fits ONE frond per stem and the leg fits none — what is left is a field of bare
#       bright vertical lines on a dark ground, which is the 11th fluting. Too sparse and the tree
#       disappears into an axis from thirty-eight batches ago.
#   10  the leg still goes a whole stem without a frond; the torso reads as fluting with a defect.
#    8  the torso carries 2-3 fronds per stem with the tip fork intact and open matrix between
#       them, and the leg carries 2. Stem, frond and fork are simultaneously legible with dark
#       ground visible around each — chosen.
#    6  the fronds of one stem begin to run into the fronds of the next: the gaps close, the eye
#       joins neighbouring diagonals across the matrix, and the field reads as one continuous
#       diagonal weave — the 16th twill herringbone. Too dense and the tree collapses the OTHER
#       way, into a different old axis. (Judged on the wide --swatch plate, where the crowding
#       shows first: at 6 the plate is a diagonal hatch, at 8 it is unmistakably fronds.)
#    4  coverage passes 45% and the whole thing is a checker of 1px marks with no readable
#       structure at any generation.
FROND_P = 8       # rows between successive fronds on the same side of a stem — see sweep below
FROND_L = 3       # length of a generation-1 frond (px)
BARB_L = 1        # length of a generation-2 tip-fork member (px)
MAXGEN = 2        # trunk(0) -> frond(1) -> fork(2)
TRUNK_P = 2 * FROND_L + 1     # = 7: opposing fronds interlock with a 1px matrix gap

# Four-stop metal ramp per class (LO, MID, HI, TOP) plus two bedding tones (BASE, SHADOW).
# Rank is spent on VALUE because at 13px it cannot be spent on thickness:
#   TOP  -> TRUNK      (generation 0)
#   HI   -> FROND near the stem, MID -> FROND far from it   (generation 1, tapering)
#   LO   -> FORK       (generation 2)
# Every pale stop is deliberately clear of the skin palette: on a narrow female chest the stems and
# their fronds are most of what is visible, and a warm off-white would read as bare skin at 1x —
# the lesson the 47th's rose gold cost a whole cut to learn.
METAL = {
    # native silver dendrite in magnetite — cold white, unmistakably not skin
    'warrior': ((122, 130, 148), (170, 180, 198), (214, 222, 238), (250, 252, 255)),
    # hoarfrost fern on black ice — pale cyan, the coldest ramp in the set
    'mage':    ((72, 132, 156), (110, 182, 208), (162, 224, 240), (228, 252, 255)),
    # native gold dendrite in umber gossan — pushed to a saturated amber, well clear of tan skin
    'ranger':  ((132, 84, 20), (186, 128, 34), (232, 176, 62), (255, 224, 128)),
}
BEDDING = {
    # (BASE, SHADOW) — SHADOW is what a ground pixel takes when the tree overhangs it from the
    # upper left. This pair IS the relief of the axis; keep the two stops well separated.
    # The BASE must also stay clear of pure black, and that is a HELMET constraint rather than a
    # taste one: the finishing pass carves the visor as black eye and mouth pixels, so a matrix that
    # is itself near-black swallows the face slit and the dome reads as a featureless dark lump. A
    # first cut at (34,34,42) / (16,26,46) did exactly that on the warrior dome. Both stops are
    # lifted here so the black visor has something to be black against.
    'warrior': ((50, 50, 62), (28, 28, 36)),        # magnetite
    'mage':    ((36, 52, 82), (18, 28, 50)),        # black ice
    'ranger':  ((66, 48, 30), (36, 26, 16)),        # umber gossan
}

# Per-class body (ground) tones for the recolor, visible on sleep frames only:
# (deep shadow / base / highlight), taken off the bedding so the piece reads as one object.
BODY = {
    'warrior': ((20, 20, 26), (40, 40, 50), (78, 80, 94)),
    'mage':    ((10, 16, 30), (26, 40, 66), (58, 92, 124)),
    'ranger':  ((22, 16, 10), (52, 38, 24), (94, 70, 40)),
}

# One config block per slot. `largest` restricts the field to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_dendrite_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary49', largest=True,
    ),
    'legs': dict(
        outdir='_dendrite_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary49', largest=False,
    ),
    'boots': dict(
        outdir='_dendrite_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_dendrite', largest=False,
    ),
    'helmet': dict(
        outdir='_dendritedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary49', largest=True,
    ),
}


# --- the branching tile ---------------------------------------------------------------------
# The tile is GROWN rather than tested. `_tile()` returns two periodic arrays over
# (FROND_P, TRUNK_P): GEN (-1 = matrix, 0 = trunk, 1 = frond, 2 = barb) and DEPTH (how far along
# its own member the pixel sits, which is what produces the taper inside a frond). Writes wrap
# modulo the period, so a frond that runs off the right of the tile re-enters on the left and the
# stems interlock exactly as they do on an unbounded field.
_TILE_CACHE = {}


def _tile():
    key = (TRUNK_P, FROND_P, FROND_L, BARB_L, MAXGEN)
    if key in _TILE_CACHE:
        return _TILE_CACHE[key]
    H, W = FROND_P, TRUNK_P
    gen = np.full((H, W), -1, dtype=np.int8)
    dep = np.zeros((H, W), dtype=np.int8)

    def put(y, x, g, d):
        yy, xx = y % H, x % W
        if gen[yy, xx] == -1 or g < gen[yy, xx]:
            gen[yy, xx] = g
            dep[yy, xx] = d

    def grow(x, y, dx, dy, length, g):
        """Paint one member from (x,y) in direction (dx,dy), then FORK at its tip into two
        shorter children that bracket the parent's own direction.

        This recursion IS the axis: a child exists because its parent does, and it inherits its
        parent's heading. The rule is deliberately a TIP fork and not lateral barbs — the first cut
        sprouted children off the middle of each frond on the mirrored diagonal, and because a
        mirrored barb points back toward the stem it fell into the gap between one frond and the
        next, filling the matrix and collapsing the whole field into a 50%-coverage checker (see
        the swatch note in CONTEXT.md). Forking only at the tip keeps the matrix open, and an open
        matrix is what lets a 1px tree read as a tree at all."""
        tx, ty = x, y
        for i in range(1, length + 1):
            tx, ty = x + dx * i, y + dy * i
            put(ty, tx, g, i)
        if g < MAXGEN:
            for cdx, cdy in ((dx, 0), (0, dy)):           # the two axis directions bracketing (dx,dy)
                for j in range(1, max(1, length - 2) + 1):
                    put(ty + cdy * j, tx + cdx * j, g + 1, j)

    for y in range(H):
        put(y, 0, 0, 0)                                   # the stem, generation 0
    grow(0, 0, 1, 1, FROND_L, 1)                          # right frond
    grow(0, FROND_P // 2, -1, 1, FROND_L, 1)              # left frond, half a period up the stem

    tree = gen >= 0
    # cast shadow: a matrix pixel whose UPPER-LEFT neighbour belongs to the tree. Computed on the
    # periodic tile so the shadow tiles seamlessly with the ornament that casts it.
    up_left = np.roll(np.roll(tree, 1, axis=0), 1, axis=1)
    shadow = (~tree) & up_left
    _TILE_CACHE[key] = (gen, dep, shadow)
    return _TILE_CACHE[key]


def dendrite_tone(lx, ly, metal, bed, phase=0, thin=False):
    """Tone for one body pixel at component-local (lx, ly).

    This function dispatches on GENERATION — how far the pixel's member is from the root of the
    tree — where forty-eight prior axes dispatch on which part of a closed cell the pixel is in.

    `phase` shifts the stem lattice so that a stem runs down the CENTRE of the component instead of
    down its left bounding edge. This is not cosmetic. With no phase the lx==0 stem lands exactly on
    the leftmost column of the piece, and because the stem is the brightest stop in the ramp and
    runs unbroken from top to bottom, the result is a BRIGHT FULL-SILHOUETTE RIM BAR — the inverse
    of the standing 'no dark rim on helmets' rule and just as destructive: on the first cut the
    warrior dome read as two white bars framing the face and the mage hat grew a white bar hanging
    beside the cheek, with the ornament itself invisible behind them. A centred stem also happens to
    be the right composition for armour: one bright spine up the breastbone or over the crown of the
    skull, with fronds spreading to both sides of it."""
    gen, dep, shadow = _tile()
    yy, xx = ly % FROND_P, (lx - phase) % TRUNK_P
    g = gen[yy, xx]
    if g < 0:
        return bed[1] if shadow[yy, xx] else bed[0]
    if g == 0:
        # NO BRIGHT RIM. Centring the lattice stops a stem landing on the main bounding edge, but a
        # piece with narrow protrusions — a mage hat brim, a hood flap, a boot cuff — can still put
        # a stem on a part that is only 1-2px thick, and an unbroken top-stop line there reads as a
        # detached white bar hanging beside the face rather than as a stem on the piece. Where the
        # body is too thin to show the stem has anything growing out of it, the stem drops to the
        # frond stop. Same principle as the standing helmet rule, in the other direction: the
        # silhouette edge is never allowed to carry the extreme of the ramp.
        return metal[1] if thin else metal[3]             # trunk: the brightest thing on the piece
    if g == 1:
        # a frond dims as it runs away from its stem — taper, spent on value because 1px members
        # have no thickness left to spend it on
        return metal[2] if dep[yy, xx] <= 1 else metal[1]
    return metal[0]                                       # tip fork: the dimmest, generation 2


def paint_dendrite(fr, comp, metal, bed):
    """Paint the dendrite field onto one component. Only opaque body pixels are ever painted, so
    this cannot create strays."""
    if comp.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp)
    y0, x0 = int(ys.min()), int(xs.min())
    w = int(xs.max()) - x0 + 1
    phase = (w // 2) % TRUNK_P          # a stem down the centre of the piece, never on its edge
    # THIN = the body is not opaque on both sides of this pixel, i.e. the piece is 1px across here.
    # A stem on such a pixel is demoted (see dendrite_tone) so no protrusion carries a bright bar.
    left = np.zeros_like(comp)
    right = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    thin_m = comp & ~(left & right)
    for y, x in zip(ys, xs):
        rgb = dendrite_tone(int(x) - x0, int(y) - y0, metal, bed, phase, bool(thin_m[y, x]))
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free).
    Returns (labels int32 array, n). Background (False) is label 0."""
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
                    if y > 0 and mask[y - 1, x] and labels[y - 1, x] == 0:
                        labels[y - 1, x] = n
                        stack.append((y - 1, x))
                    if y < h - 1 and mask[y + 1, x] and labels[y + 1, x] == 0:
                        labels[y + 1, x] = n
                        stack.append((y + 1, x))
                    if x > 0 and mask[y, x - 1] and labels[y, x - 1] == 0:
                        labels[y, x - 1] = n
                        stack.append((y, x - 1))
                    if x < w - 1 and mask[y, x + 1] and labels[y, x + 1] == 0:
                        labels[y, x + 1] = n
                        stack.append((y, x + 1))
    return labels, n


def load_any(fname):
    """Load a source sheet; if the female (_f) variant is absent (warrior boots are a
    single gender-shared sheet), fall back to the base sheet."""
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
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


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    metal, bed = METAL[cls], BEDDING[cls]
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
        if fi >= 60:                            # sleep: body only
            continue
        if largest:
            lbl, n = label4(a)
            if n >= 1:
                counts = np.bincount(lbl.ravel())
                counts[0] = 0
                comp = (lbl == int(counts.argmax()))
            else:
                comp = a
        else:
            comp = a
        paint_dendrite(fr, comp, metal, bed)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ----------------------------------------------------------------------------
def _test_plate(w=44, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the
    dendrite field can be judged on a shape that has the features real slots have."""
    m = np.zeros((h, w), dtype=bool)
    yy, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False          # neck notch
    return m


def swatch(path='_diag_dendrite_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the three generations of
    the tree and the cast shadow can be judged before any sheet is written."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_dendrite(a, m, METAL[cls], BEDDING[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only — no sheets written)' % path)


def sweep(path='_diag_dendrite_sweep.png', zoom=11):
    """Render the warrior chest idle frame at a range of frond pitches, plus a leg frame, so the
    pitch can be judged on whether the THIRD GENERATION survives — including on the thin parts."""
    global FROND_P
    keep = FROND_P
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    for p in (12, 10, 8, 6, 4):
        FROND_P = p
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comp = (lbl == int(counts.argmax())) if n else a
            fr = np.zeros_like(src)
            paint_dendrite(fr, comp, METAL['warrior'], BEDDING['warrior'])
            col.append(Image.fromarray(fr).crop(crop))
        cells.append(('FROND_P=%d' % p, col))
    FROND_P = keep
    cw, ch = 28 * zoom, 26 * zoom
    pad, lab = 8, 18
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + 2 * (ch + lab)), (24, 24, 28, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
    except Exception:
        f = ImageFont.load_default()
    x = pad
    for name, col in cells:
        y = pad
        for im in col:
            img.alpha_composite(im.resize((cw, ch), Image.NEAREST), (x, y))
            d.text((x + 2, y + ch), name, font=f, fill=(210, 210, 220, 255))
            y += ch + lab
        x += cw + pad
    img.convert('RGB').save(path)
    print('wrote %s (pitch sweep — no sheets written)' % path)


def dump_tile():
    """ASCII dump of the grown tile — the fastest way to confirm the tree has three generations
    and that no child landed back on its own stem."""
    gen, dep, shadow = _tile()
    sym = {-1: '.', 0: 'T', 1: 'F', 2: 'b'}
    print('tile %dx%d  TRUNK_P=%d FROND_P=%d FROND_L=%d' %
          (gen.shape[0], gen.shape[1], TRUNK_P, FROND_P, FROND_L))
    for rep in range(3):
        for y in range(gen.shape[0]):
            print(''.join(sym[int(gen[y, x % gen.shape[1]])] for x in range(TRUNK_P * 3)))
    counts = {k: int((gen == k).sum()) for k in (-1, 0, 1, 2)}
    print('per-tile px  matrix=%d trunk=%d frond=%d barb=%d  shadow=%d'
          % (counts[-1], counts[0], counts[1], counts[2], int(shadow.sum())))


def main():
    if '--tile' in sys.argv:
        dump_tile()
        return
    if '--swatch' in sys.argv:
        swatch()
        return
    if '--sweep' in sys.argv:
        sweep()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass — never a bespoke shade() in a generator.
                # save_finished() rather than a bare .save(): it writes the TaskQuestFinish
                # version stamp, without which a later bulk `sprite_finish.py <dir>` backfill
                # would run the whole chain over these sheets a SECOND time.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-62s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
