#!/usr/bin/env python3
"""FORTY-EIGHTH net-new-geometry axis for ALL FOUR SLOTS — the COSMATESQUE / OPUS SECTILE family
(hierarchical stone inlay): a field of square marble PANELS, each one framed by a pale fillet band
and filled with a large central ROUNDEL of porphyry surrounded by four small square TESSERAE of a
second stone — the quincunx panel of a Cosmati pavement, the inlaid floors of the Roman basilicas.

    the ornament is  PANEL    (the 1px pale fillet frame that squares off one bay, and the brighter
                               NODE stone where four fillets cross)
                   + ROUNDEL  (one large disc of porphyry filling the middle of the bay)
                   + TESSERA  (four small square stones of a contrasting marble in the corners)
                   + GROUND   (the dark bedding the three stones are set into)

*** THIS IS THE FIRST HIERARCHICAL, MULTI-SCALE AXIS IN FORTY-EIGHT. ***  Every one of the
forty-seven prior axes has exactly ONE characteristic element size. The ruled lattices (11th-45th)
stamp a single congruent cell on a lattice, so every element on the plate is the same size by
construction. The 46th craquelure broke periodicity, but its shards still all belong to one size
band — they vary by a jitter, not by a scale factor, and a field of slightly-different shards still
reads as "one size of shard". The 47th mokume broke positionality, but every lamina in the nest is
the same PB thick. Cosmatesque puts THREE DELIBERATELY DIFFERENT SIZES on the plate at once, in a
fixed ratio — an 8px panel, a 5px roundel, a 2px tessera, 8 : 5 : 2 — so the eye reads a large form,
a medium form and a small form simultaneously and infers a composition rather than a texture. That
is the whole subject of the axis: not a motif but a HIERARCHY of motifs.

The palette is built on the same idea and is the second half of the argument: MATERIAL IS A FUNCTION
OF SCALE. The big element is porphyry, the small element is a contrasting marble, the frame is white
marble, the bedding is dark. Three stones, one per rank in the hierarchy — which is exactly how a
real Cosmati panel is cut, and it means the scale hierarchy survives even where the silhouette is
too narrow to show a whole panel: a 4px limb still shows the pale frame, a slice of coloured roundel
and a corner tessera in three distinguishable stones. (Contrast the 47th, whose two ramps alternate
band-to-band with no regard to size, because its subject was two metals forge-welded, not a
composition.)

Geometry, per opaque body pixel, in component-local coordinates (lx, ly) measured from the
component's bounding box:

    ax, ay = lx % P, ly % P                    P = PANEL = 8 px, the bay pitch
    ax == 0 or ay == 0   -> FILLET             the 1px pale marble band framing the bay
        ax == 0 and ay == 0  -> NODE           the brighter crossing stone (a 4th, 1px rank)
    otherwise the bay interior, ix = ax-1, iy = ay-1, over 0 .. S-1 with S = P-1:
        |ix-c| + |iy-c| <= RR  -> ROUNDEL      c = (S-1)/2, RR = 2.0  (a 5px-wide disc)
        ix, iy both within TS of an interior corner -> TESSERA        (a 2x2 square stone)
        else                 -> GROUND         the dark bedding, i.e. the spandrel

Relief. Opus sectile is flush inlay, so this axis does NOT emboss its cells the way the ridge and
boss axes do; instead each stone is POLISHED and takes a specular read appropriate to its own size.
The roundel is a shallow polished disc lit from the upper left, `lit = (-dx - dy) / (2*RR)`, giving
it a bright upper-left crescent and a dark lower-right one — the only element large enough to carry
a gradient. A tessera is 2x2 and can carry exactly one highlight, so its upper-left pixel takes the
bright stone and the other three the base: one pip, which is what a small polished square does at
this scale. The fillet is flat pale marble and the node one step brighter. Rendering a 5px element
with a three-tone gradient and a 2px element with a single pip is not a shortcut — it is the reason
the two ranks stay distinguishable at 1x.

Distinctness, against the axes it could be mistaken for:
  * 17th ashlar — rectangular OUTLINE cells on a bond. The nearest neighbour by silhouette, and the
    separation is the axis itself: an ashlar cell is EMPTY, one scale, a plain outline. A Cosmati
    bay is a frame with a composition inside it in two further sizes and two further stones.
  * 14th lattice / 19th honeycomb / 20th trellis / 21st chainmail — congruent one-scale nets.
  * 37th coffer — sunken congruent rectangular panels with a bevel. A coffer is one recessed cell
    and nothing is set into it; the Cosmati bay is flush and carries a roundel and four tesserae.
  * 13th studwork — a point-grid of rivets, i.e. only the small rank, on no frame.
  * 25th argyle — a SOLID-FILLED diagonal-diamond field. Worth naming explicitly because at 8px the
    roundel resolves to a diamond, so the two share a shape: but argyle's diamonds are one size,
    tile edge-to-edge with nothing between them, and have no frame and no subordinate stones. Here
    the diamond is one of four ranks and is isolated in its bay by bedding on every side.
  * 28th concentric / 32nd quatrefoil / 33rd octagram — a single stamped rosette repeated on a
    lattice: one motif, one size, no frame and no subordinate stones.
  * 26th tartan — crossing bold bands with a brighter overlap node, which is the nearest thing in
    the set to the fillet-and-node grid, but the field between tartan's bands is plain woven cloth;
    there is nothing set into it and no second or third element size.
  * 46th craquelure — irregular, but single-scale, and a partition rather than a composition.
  * 47th mokume — shape-conformal, but every lamina is the same thickness.

Per slot it lands as the 48th distinct axis:
  * CHEST  — cosmati cuirass: quincunx bays across the breast, fillets squaring the torso.
  * LEGS   — cosmati chausses: a column of bays down each thigh.
  * BOOTS  — cosmati sabatons: inlaid stone over the foot.
  * HELMET — cosmati dome: the pale fillet grid runs over the skull, roundels on the temples.

Authoring philosophy identical to gen_mokume_axis47.py / gen_craquelure_axis46.py /
gen_arcade_axis45.py: every pattern pixel is painted ONLY onto pixels ALREADY opaque in the body.
Because it never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction. Sleep frames
(fi >= 60) get a plain body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` — the canonical chain (no-smooth shading with protect=False,
shirt pauldron/gorget/chest-plate separation, helmet black eye+mouth visor with NO full-silhouette
rim, hat brim/crease folds for open headgear). See CONTEXT.md "MANDATORY — the finishing pass".

Run from repo root:
  python3 scripts/gen_cosmati_axis48.py
  python3 scripts/gen_cosmati_axis48.py --swatch     # bare motif on a test plate, no sheets written
  python3 scripts/gen_cosmati_axis48.py --sweep      # panel-pitch sweep on a real torso AND a real leg
Then QA (examples):
  python3 scripts/sprite_qa.py _cosmati_legendary_preview/shirt_warrior_legendary48.png
  python3 scripts/sprite_qa.py _cosmatidome_helmet_preview/helmet_mage_legendary48.png --y-min 2
  python3 scripts/sprite_qa.py _cosmati_boots_preview/boots_warrior_legendary_cosmati.png --y-max 63
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

# --- Cosmatesque constants ------------------------------------------------------------------
# PANEL is the bay pitch and the constant that sets whether the HIERARCHY reads at all, which is a
# different failure mode from either of the last two axes. The 46th needed a SMALL pitch (an
# aperiodic field must show several cells before the eye accepts they differ); the 47th needed a
# pitch set by the THINNEST part (a contour nest's band count is the piece's half-thickness). This
# axis needs a pitch large enough to hold THREE RANKS AT ONCE — a frame, a disc and a corner stone
# have to be simultaneously visible inside one bay or the composition collapses into whichever rank
# survives, and that rank is then indistinguishable from an older single-scale axis. Swept at
# 10/9/8/7/6 (--sweep) on a real torso and a real leg:
#   10   one bay is wider than the 13px torso, so the torso shows ONE roundel adrift in a field of
#        bedding with the frame reduced to a stray line down the edge — no composition at all, and
#        at a glance just a coloured boss, i.e. an impoverished 28th concentric.
#   9    better, but still only one bay across the chest: the frame reads on two sides, the four
#        tesserae come in unpaired, and both legs go a whole bay without a roundel — the hierarchy
#        is present in principle and invisible in practice.
#   8    the torso holds ~1.7 bays across and 2 down — frame, roundel and all four tesserae legible
#        together — and a 4-5px limb still shows fillet + roundel edge + a corner stone, i.e. three
#        stones and three sizes even on the thinnest part. Chosen.
#   7    the interior drops to 6px and the roundel's outer pixels become ORTHOGONALLY ADJACENT to
#        the corner tesserae (interior (1,2) is roundel and (1,1) is tessera): the quincunx fuses
#        into one blob per bay, and a fused blob is a single element — the hierarchy collapses to
#        one rank plus a frame, which is the 17th ashlar with a filling.
#   6    worse than fused — at S=5 the roundel mathematically SWALLOWS the tessera cells outright
#        (|1-2|+|1-2| = 2 <= RR), so the small rank does not render at all. The hierarchy is gone.
PANEL = 8         # bay pitch (px) — see sweep above
ROUND_R = 2.0     # roundel radius in the L1 (diamond) metric -> a 5px-wide polished disc
TESS = 2          # side of the small corner tesserae (px)
LIT_HI = 0.34     # roundel arc facing the upper-left light
LIT_LO = -0.34    # roundel arc turned away from it

# Three stones per class, one per rank in the hierarchy, plus the dark bedding.
#   PORPHYRY (LO, MID, HI) -> the ROUNDEL, the only element big enough to hold a gradient
#   MARBLE   (BASE, NODE)  -> the FILLET frame and its brighter crossing node
#   STONE    (BASE, PIP)   -> the small corner TESSERAE, base plus a single highlight pixel
#   BED                    -> the dark bedding the stones are set into (the spandrel)
# Every pale value here is deliberately clear of the skin palette: on a narrow female chest the
# fillet grid is most of what is visible, and a warm off-white would read as bare skin at 1x — the
# lesson the 47th's rose gold cost a whole cut to learn.
PORPHYRY = {
    'warrior': ((78, 26, 38), (132, 48, 62), (190, 96, 110)),      # imperial porphyry
    'mage':    ((28, 42, 104), (52, 76, 166), (104, 138, 226)),    # lapis lazuli
    'ranger':  ((26, 66, 50), (46, 110, 80), (96, 168, 126)),      # verde antico serpentine
}
MARBLE = {
    'warrior': ((198, 196, 190), (248, 248, 244)),                 # carrara
    'mage':    ((186, 192, 214), (242, 246, 255)),                 # moonstone
    'ranger':  ((206, 202, 182), (248, 246, 230)),                 # ivory
}
STONE = {
    # The small rank has to differ from its own roundel AND from the other classes' small rank, or
    # three classes of the same axis read as one item in three tints. A first cut gave all three a
    # warm gold (giallo / gold / copper) and warrior and mage came out indistinguishable at 1x —
    # the tesserae are the busiest element on the plate, so they are what the eye colour-matches on.
    # Warrior therefore takes VERDE ANTICO against its porphyry, which is also the canonical Roman
    # pairing (the two stones a Cosmati panel is actually cut from); mage keeps gold against lapis;
    # ranger keeps copper, which is warm-brown enough not to be read as mage's gold.
    'warrior': ((72, 116, 80), (128, 180, 132)),                   # verde antico
    'mage':    ((156, 118, 44), (230, 186, 96)),                   # gold
    'ranger':  ((140, 88, 44), (206, 140, 78)),                    # copper
}
BED = {
    'warrior': (30, 26, 32),                                       # basalt
    'mage':    (14, 14, 34),                                       # indigo slate
    'ranger':  (18, 26, 20),                                       # bog oak
}

# Per-class body (ground) tones for the recolor, visible on sleep frames only:
# (deep shadow / base / highlight), taken off the bedding so the piece reads as one object.
BODY = {
    'warrior': ((22, 18, 24), (48, 42, 52), (86, 76, 92)),
    'mage':    ((10, 10, 26), (30, 30, 66), (62, 66, 122)),
    'ranger':  ((12, 18, 14), (36, 48, 38), (70, 92, 74)),
}

# One config block per slot. `largest` restricts the field to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_cosmati_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary48', largest=True,
    ),
    'legs': dict(
        outdir='_cosmati_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary48', largest=False,
    ),
    'boots': dict(
        outdir='_cosmati_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_cosmati', largest=False,
    ),
    'helmet': dict(
        outdir='_cosmatidome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary48', largest=True,
    ),
}


# --- the hierarchical field -----------------------------------------------------------------
def cosmati_tone(lx, ly, porph, marble, stone, bed):
    """Tone for one body pixel at component-local (lx, ly).

    This function IS the axis: it dispatches on which RANK of the hierarchy the pixel belongs to —
    frame, node, roundel, tessera or bedding — and each rank is a different size AND a different
    stone. Forty-seven prior axes answer 'which part of the one cell am I in'; this one answers
    'which of three nested elements am I part of'."""
    P = PANEL
    ax, ay = lx % P, ly % P
    if ax == 0 or ay == 0:
        # the pale fillet band framing the bay; brighter where four fillets cross
        return marble[1] if (ax == 0 and ay == 0) else marble[0]
    S = P - 1
    ix, iy = ax - 1, ay - 1
    c = (S - 1) / 2.0
    dx, dy = ix - c, iy - c
    if abs(dx) + abs(dy) <= ROUND_R:
        # the porphyry roundel — the one element wide enough to carry a real gradient
        lit = (-dx - dy) / (2.0 * ROUND_R)
        return porph[2] if lit > LIT_HI else (porph[0] if lit < LIT_LO else porph[1])
    inx = ix < TESS or ix >= S - TESS
    iny = iy < TESS or iy >= S - TESS
    if inx and iny:
        # a 2x2 corner tessera: one highlight pip on its upper-left pixel, base elsewhere
        px = ix if ix < TESS else (ix - (S - TESS))
        py = iy if iy < TESS else (iy - (S - TESS))
        return stone[1] if (px == 0 and py == 0) else stone[0]
    return bed


def paint_cosmati(fr, comp, porph, marble, stone, bed):
    """Paint the quincunx panel field onto one component. Only opaque body pixels are ever painted,
    so this cannot create strays."""
    if comp.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp)
    y0, x0 = int(ys.min()), int(xs.min())
    for y, x in zip(ys, xs):
        rgb = cosmati_tone(int(x) - x0, int(y) - y0, porph, marble, stone, bed)
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
    porph, marble, stone, bed = PORPHYRY[cls], MARBLE[cls], STONE[cls], BED[cls]
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
        paint_cosmati(fr, comp, porph, marble, stone, bed)
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
    panel field can be judged on a shape that has the features real slots have."""
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


def swatch(path='_diag_cosmati_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the three ranks of the
    hierarchy and their three stones can be judged before any sheet is written."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_cosmati(a, m, PORPHYRY[cls], MARBLE[cls], STONE[cls], BED[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only — no sheets written)' % path)


def sweep(path='_diag_cosmati_sweep.png', zoom=11):
    """Render the warrior chest idle frame at a range of bay pitches, plus a leg frame, so the
    pitch can be judged on whether ALL THREE RANKS survive — including on the thin parts."""
    global PANEL
    keep = PANEL
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    for p in (10, 9, 8, 7, 6):
        PANEL = p
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comp = (lbl == int(counts.argmax())) if n else a
            fr = np.zeros_like(src)
            paint_cosmati(fr, comp, PORPHYRY['warrior'], MARBLE['warrior'],
                          STONE['warrior'], BED['warrior'])
            col.append(Image.fromarray(fr).crop(crop))
        cells.append(('PANEL=%d' % p, col))
    PANEL = keep
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


def main():
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
