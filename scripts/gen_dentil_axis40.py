#!/usr/bin/env python3
"""FORTIETH net-new-geometry axis for ALL FOUR SLOTS — the DENTIL / DENTILATED-CORNICE family:
an all-over field of horizontal COURSES, each course a continuous bright top FILLET from which
hangs a row of DISCRETE RAISED RECTANGULAR TEETH ("dentils") separated by square recessed GAPS
("interdentils") — the classical dentil molding run under a cornice on temples, coins and
picture-frames. One course per band pitch PY down; along each course the teeth repeat at pitch
PX, each tooth TW wide (gap = PX-TW), hanging TH deep below a 1px continuous FILLET that ties
the teeth together across the whole course. Each tooth is shaded as a small RAISED BLOCK under an
upper-left light (top/left = HILIT, a white RIM catch on the top-left cap, right/bottom = SHADOW,
interior = MID); the fillet reads as a bright continuous lip; the gaps and the channel below the
teeth drop to a recessed GROUND. The repeated motif is a BROKEN ROW OF RAISED RECTANGULAR TEETH
depending from a continuous FILLET; none of the thirty-nine existing legendary axes per slot
occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel bands, NO gaps (lamellar)  <- dentil BREAKS the
        band into discrete teeth with recessed gaps, and adds directional block relief
  * 13th a field of DISCRETE RAISED ROUND POINTS (rivet-stud grid)          <- teeth are RECT
        blocks hung from a fillet in a 1-D course, not isolated round dots on a 2-D grid
  * 14th crossing STRAIGHT DIAGONALS -> lozenge OUTLINE (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS (imbricated scale)
  * 16th SHORT alternating-slope diagonal dashes (herringbone / twill)
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells, FLAT (ashlar)  <- dentil is a SOLID
        RAISED block with 3-D relief, a single course hung from a fillet, not a flat 2-D outline
  * 18th CHECKER of perpendicular short-thread bundles (basketweave)
  * 19th six-sided OUTLINE cells (honeycomb)   * 20th three-sided cells (trellis)
  * 21st single-radius CIRCLE outlines (chainmail)   * 22nd ONE sine ripple (wave)
  * 23rd right-angle key-fret (meander)   * 24th curved coils around a centre (spiral)
  * 25th FLAT solid diagonal diamonds (argyle)   * 26th crossed bold bands + node (tartan)
  * 27th straight rays from a centre (sunburst)   * 28th nested rings (concentric)
  * 29th jagged broken-check color-and-weave (houndstooth)
  * 30th two strands twist down a column (cable)   * 31st counter-phase ribs -> pointed ovals (ogee)
  * 32nd four circular lobes per node (quatrefoil)   * 33rd eight-pointed star outline (octagram)
  * 34th nested-arc fans, half-drop (seigaiha)   * 35th raised four-facet pyramids (facet)
  * 36th convex diamond cushions + buttons (quilt)   * 37th SUNKEN rectangular panels, reversed
        bevel, on a 2-D grid (coffer)  <- dentil is the OPPOSITE: RAISED teeth in a 1-D course,
        normal relief, hung from a fillet, plain recessed gaps (no full grid, no reversed bevel)
  * 38th alternating raised OVOIDS + pointed DARTS, a TWO-element band (egg-and-dart)  <- dentil
        is a ONE-element band: a plain rhythm of identical rectangular teeth, no darts, no ovoids
  * 39th two braided counter-phase ribbons enclosing a chain of eyes (guilloche)
  * 40th (this) a BROKEN ROW OF RAISED RECTANGULAR TEETH hung from a continuous FILLET -> dentil.

Critically distinct from every prior axis. Most important separations:
  - NOT the 12th lamellar: lamellar is a stack of CONTINUOUS horizontal bands with no breaks —
    the dentil course is BROKEN into discrete rectangular teeth with recessed square gaps between
    them, each tooth carrying block relief.
  - NOT the 37th coffer: coffer is a 2-D grid of SUNKEN panels with a REVERSED bevel (dark
    centre, proud grid) — the dentil is a 1-D course of RAISED teeth with NORMAL relief (bright
    lit cap, recessed gaps), hung from a fillet, no enclosing grid.
  - NOT the 13th studwork: studwork is isolated ROUND rivets on a 2-D point grid — dentils are
    RECTANGULAR blocks in a continuous 1-D course, joined at top by a fillet.
  - NOT the 38th egg-and-dart: that band alternates TWO different raised elements (ovoid + dart);
    the dentil course repeats ONE identical rectangular tooth.
The broken row of raised rectangular teeth depending from a continuous fillet is the defining,
previously-unused geometry.

Per slot it lands as the 40th distinct axis:
  * CHEST  — dentil cuirass: courses of dentil teeth banded down the whole breastplate.
  * LEGS   — dentil chausses: courses of dentil teeth banded down the thighs.
  * BOOTS  — dentil sabatons: courses of dentil teeth over the boot.
  * HELMET — dentil dome: courses of dentil teeth over the whole crown.

Authoring philosophy identical to gen_guilloche_axis39.py / gen_eggdart_axis38.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel
outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run sprite_shade.py
again.

To read as a clearly DIFFERENT set the dentil family is CAST-BRONZE CORNICE RELIEF — a plate
carved with the classical dentil molding, a white catch-light on each tooth cap. Class differs by
metal/gem (same metals as the cast-bronze family):
  * warrior — gilt-bronze dentils (dark-bronze ground / bronze shadow / brass mid / bright-gold hilit / white-gold rim)
  * mage    — silvered violet dentils (midnight ground / indigo shadow / steel-violet mid / bright-silver hilit / pale-white rim)
  * ranger  — bronzed forest dentils (deep-forest ground / bottle shadow / bronze-green mid / bright-emerald hilit / pale-green rim)

Run from repo root:
  python3 scripts/gen_dentil_axis40.py
Then QA (examples):
  python3 scripts/sprite_qa.py _dentil_legendary_preview/shirt_warrior_legendary40.png
  python3 scripts/sprite_qa.py _dentildome_helmet_preview/helmet_mage_legendary40.png --y-min 2
  python3 scripts/sprite_qa.py _dentil_boots_preview/boots_warrior_legendary_dentil.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Dentil geometry. Tuned so the dentilated cornice reads on a ~14px torso: courses at band pitch
# PY, each course a 1px continuous FILLET with teeth of width TW hung TH deep at tooth pitch PX
# (gap = PX-TW).  The signature is a BROKEN row of raised rectangular teeth under a fillet.
PX = 5.0         # tooth pitch across (local px)  -> tooth + gap
TW = 3.0         # tooth width across (gap = PX-TW = 2)
PY = 7.0         # course pitch down (local px)
FILLET_H = 1.0   # continuous top fillet height (local px)
TH = 4.0         # tooth depth below the fillet (local px)


# Per-class dentil tone quintet: (GROUND recessed gap / channel below teeth, SHADOW tooth
# right+bottom edge, MID tooth crown + fillet body, HILIT tooth lit top/left + fillet lip,
# RIM tooth top-left cap catch-light). Light comes from the upper-left.
DENTIL = {
    'warrior': ((40, 26, 10), (96, 64, 24), (168, 126, 52), (236, 190, 86), (255, 238, 168)),  # gilt-bronze
    'mage':    ((18, 16, 46), (66, 54, 114), (116, 100, 182), (176, 158, 240), (236, 228, 255)),  # silvered violet
    'ranger':  ((12, 30, 18), (38, 78, 48), (72, 132, 84), (124, 200, 128), (216, 248, 206)),  # bronzed forest
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only): (deep shadow /
# base / highlight).
BODY = {
    'warrior': ((44, 30, 14), (82, 58, 26), (128, 96, 46)),   # dark bronze cloth
    'mage':    ((26, 24, 58), (52, 48, 104), (92, 86, 166)),   # dark violet cloth
    'ranger':  ((16, 40, 24), (38, 76, 50), (70, 122, 82)),    # dark forest cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_dentil_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary40', largest=True,
    ),
    'legs': dict(
        outdir='_dentil_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary40', largest=False,
    ),
    'boots': dict(
        outdir='_dentil_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_dentil', largest=False,
    ),
    'helmet': dict(
        outdir='_dentildome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary40', largest=True,
    ),
}


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


def draw_dentil(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the dentilated cornice onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, a course pitch PY
    places a continuous top FILLET (height FILLET_H) with a row of raised rectangular TEETH of
    width TW (pitch PX, gap PX-TW) hung TH deep below it. A pixel is:
      * FILLET  (0 <= v < FILLET_H)                 -> continuous lip: top row RIM, else HILIT
      * TOOTH   (FILLET_H <= v < FILLET_H+TH, u<TW) -> raised block, block relief under UL light
      * GAP / recessed channel                      -> GROUND
    Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    gap = PX - TW
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        v = ly % PY               # depth within the course [0, PY)
        u = lx % PX               # phase within the tooth pitch [0, PX)
        if v < FILLET_H:
            # continuous top fillet lip tying the whole course together
            if (ly % PY) < 0.5:
                put(fr, yy, xx, rim)     # bright top edge of the fillet
            else:
                put(fr, yy, xx, hilit)   # lit fillet body
            continue
        if v < FILLET_H + TH and u < TW:
            # raised rectangular tooth: block relief under an upper-left light
            top = (v - FILLET_H) < 1.0            # top row of the tooth
            left = u < 1.0                         # left column of the tooth
            right = (TW - u) <= 1.0                # right column of the tooth
            bottom = (FILLET_H + TH - v) <= 1.0    # bottom row of the tooth
            if top and left:
                put(fr, yy, xx, rim)     # white cap catch-light on the top-left corner
            elif top or left:
                put(fr, yy, xx, hilit)   # lit top / left flank
            elif right or bottom:
                put(fr, yy, xx, shadow)  # shaded right / bottom flank
            else:
                put(fr, yy, xx, mid)     # tooth crown
            continue
        # gap between teeth, or the recessed channel below the teeth
        put(fr, yy, xx, ground)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = DENTIL[cls]
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
        draw_dentil(fr, comp, ground, shadow, mid, hilit, rim)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                arr = shade(arr, adj_min=-0.20, adj_max=0.25)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                Image.fromarray(arr).save(dst)
                print('wrote %-58s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
