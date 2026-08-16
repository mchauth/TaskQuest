#!/usr/bin/env python3
"""THIRTY-EIGHTH net-new-geometry axis for ALL FOUR SLOTS — the EGG-AND-DART / OVOLO /
EGG-AND-TONGUE family: an all-over field of horizontal bands, each band an alternating run of
a RAISED CONVEX OVOID (the "egg") ringed by a bright bezel SHELL and a slender downward-pointing
DART (the "tongue"/arrowhead) set in the gap between every pair of eggs (the classical ovolo
enrichment carved on cornices and picture-frames). The body is tiled by a rectangular lattice
(horizontal pitch PX for the egg spacing, vertical pitch PY for the band rows). At each lattice
node sits an EGG: a convex ellipse rising toward an upper-left light so its upper-left flank
takes the HILIT crown (with a white catch-light at the very summit), its lower-right flank falls
to SHADOW, and a bright bezel SHELL rings its rim. Centred in every horizontal gap between two
eggs, on the band's centre-line, sits a DART: a small raised pointed lozenge/tongue reading as
the arrowhead of the enrichment. The channels between bands and around the motifs are a dark
recessed GROUND. The repeated motif is the ALTERNATING RAISED OVOID + POINTED DART; none of the
thirty-seven existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE RAISED ROUND POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> straight-edged lozenge OUTLINE (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS, one arc per scale (imbricated scale field)
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes (herringbone / twill)
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells (ashlar brick-bond)
  * 18th CHECKER of perpendicular SHORT-THREAD bundles (basketweave)
  * 19th tessellation of SIX-sided straight OUTLINE cells (honeycomb)
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells (trellis)
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE outlines (chainmail)
  * 22nd ONE CONTINUOUS UNDULATING SINE line (watered-steel ripple)
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES (meander key-fret)
  * 24th CONTINUOUS CURVED COILS winding around a CENTRE point (spiral / volute)
  * 25th FLAT SOLID ALTERNATE DIAGONAL DIAMONDS (argyle / harlequin)
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter overlap node (tartan / sett)
  * 27th STRAIGHT RAYS radiating OUTWARD from a shared centre (sunburst / compass)
  * 28th NESTED CLOSED RINGS at growing radius around one centre (concentric target)
  * 29th INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill (houndstooth)
  * 30th TWO INTERTWINING STRANDS braiding OVER-UNDER down a column (cable / rope)
  * 31st COUNTER-PHASE RIBS PINCH-AND-BULGE enclosing POINTED-OVAL cells (ogee / damask)
  * 32nd FOUR CIRCULAR LOBES around each node meeting at four cusps (quatrefoil / tracery)
  * 33rd axis-square + 45deg-square overlaid into an EIGHT-POINTED STAR OUTLINE (octagram)
  * 34th OVERLAPPING FANS of NESTED CONCENTRIC ARCS on a half-drop lattice (seigaiha wave)
  * 35th a TESSELLATION OF RAISED FOUR-FACET PYRAMIDS with directional facet shading (facet)
  * 36th a field of CONVEX ROUNDED DIAMOND CUSHIONS pinned by sunken button tufts (quilt)
  * 37th a field of SUNKEN RECTANGULAR PANELS with a REVERSED bevel and a proud grid (coffer)
  * 38th (this) an ALTERNATING BAND of RAISED CONVEX OVOIDS + POINTED DARTS -> egg-and-dart.

Critically distinct from every prior axis. Against the relief axes it is neither a pyramid
(35th facet), a diamond cushion (36th quilt), nor a sunken rectangular panel (37th coffer):
the egg is a SMOOTH CONVEX OVOID (taller than wide, elliptical) ringed by a bezel SHELL and
ALTERNATED with a separate POINTED DART motif in every gap — a two-element repeat, not a single
tiled cell. It is NOT the 13th studwork (isolated round rivets — the egg is an elongated ovoid,
ringed by a shell, and interleaved with darts, not a bare round dot), NOT the 15th scale (open
arcs facing one way — the egg is a closed convex boss with a full bezel), NOT the 31st ogee
(pointed-oval CELLS formed by counter-phase ribs of a continuous net — the egg-and-dart is a row
of DISCRETE raised bosses with separate darts between them, not woven ribbon cells), NOT the 28th
concentric (nested rings — the egg is a single convex dome, not a bullseye). The alternating
raised-ovoid + pointed-dart enrichment on a banded lattice is the defining, previously-unused
geometry.

Per slot it lands as the 38th distinct axis:
  * CHEST  — ovolo cuirass: egg-and-dart enrichment banded down the whole breastplate.
  * LEGS   — ovolo chausses: egg-and-dart enrichment banded down the thighs.
  * BOOTS  — ovolo sabatons: egg-and-dart enrichment over the boot.
  * HELMET — ovolo dome: egg-and-dart enrichment over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the
component bbox top-left. Rectangular lattice PX (egg pitch across) x PY (band pitch down). Egg
centres at (i*PX, j*PY) with i=round(lx/PX), j=round(ly/PY); ey=j*PY, ex=i*PX. Dart centres in
the gaps at ((i2+0.5)*PX, ey) with i2=round(lx/PX-0.5). Let (dxe,dye)=(lx-ex,ly-ey) and the
elliptical metric ee=hypot(dxe/RX, dye/RY). Under an upper-left light lit=-(dxe/RX)-(dye/RY):
    ee <= 1.0                       -> EGG interior (convex ovoid):
        ee<=CATCH and lit>EDGE      ->   RIM white catch-light at the crown
        lit >  EDGE                 ->   HILIT lit upper-left flank
        lit < -EDGE                 ->   SHADOW lower-right flank
        else                        ->   MID side
    ee <= 1.0 + SHELL               -> bright bezel SHELL ring (RIM)
    dart lozenge |ddx|/DW+|ddy|/DH<=1 -> DART raised tongue (HILIT), tip catch (RIM) near point
    else                            -> recessed GROUND channel (darkest field)
PX/PY/RX/RY tuned so ~2 eggs span a ~14px torso and the ovoid + dart alternation reads.
Anchoring to the bbox keeps the net stable frame-to-frame.

Authoring philosophy identical to gen_coffer_axis37.py / gen_facet_axis35.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a pixel
outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run sprite_shade.py
again.

To read as a clearly DIFFERENT set the egg-and-dart family is CAST-BRONZE OVOLO ENRICHMENT — a
plate carved with the classical egg-and-tongue moulding, a white catch-light on each ovoid crown.
Class differs by metal/gem (same metals as the cast-bronze family):
  * warrior — gilt-bronze ovolo (dark-bronze ground / bronze shadow / brass mid / bright-gold hilit / white-gold rim)
  * mage    — silvered violet ovolo (midnight ground / indigo shadow / steel-violet mid / bright-silver hilit / pale-white rim)
  * ranger  — bronzed forest ovolo (deep-forest ground / bottle shadow / bronze-green mid / bright-emerald hilit / pale-green rim)

Run from repo root:
  python3 scripts/gen_eggdart_axis38.py
Then QA (examples):
  python3 scripts/sprite_qa.py _eggdart_legendary_preview/shirt_warrior_legendary38.png
  python3 scripts/sprite_qa.py _eggdartdome_helmet_preview/helmet_mage_legendary38.png --y-min 2
  python3 scripts/sprite_qa.py _eggdart_boots_preview/boots_warrior_legendary_eggdart.png --y-max 63
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

# Egg-and-dart geometry. Tuned so the enrichment reads on a ~14px torso: a rectangular lattice
# giving ~two eggs across, a convex ovoid (taller than wide) ringed by a bezel shell, and a
# slender pointed dart lozenge centred in every gap between eggs.
PX = 7.0         # egg pitch across (local px)
PY = 8.0         # band pitch down (local px)
RX = 2.4         # egg ellipse half-width
RY = 3.2         # egg ellipse half-height (taller than wide = ovoid)
SHELL = 0.34     # bezel shell ring thickness beyond the egg (in ee units)
CATCH = 0.42     # crown catch-light radius (in ee units)
EDGE = 0.34      # facet split for the convex ovoid shading
DW = 1.35        # dart lozenge half-width
DH = 3.0         # dart lozenge half-height (point downward)

# Per-class egg-and-dart tone quintet: (GROUND recessed field, SHADOW ovoid lower-right flank,
# MID ovoid side, HILIT ovoid lit flank + dart, RIM bezel shell + crown catch-light). Light
# comes from the upper-left; the ovoid's upper-left flank is HILIT and its lower-right flank is
# SHADOW, the bezel shell rings it in RIM, the dart is a raised HILIT tongue, and the field
# between motifs is the dark GROUND.
EGGDART = {
    'warrior': ((40, 26, 10), (96, 64, 24), (168, 126, 52), (236, 190, 86), (255, 238, 168)),  # gilt-bronze
    'mage':    ((18, 16, 46), (66, 54, 114), (116, 100, 182), (176, 158, 240), (236, 228, 255)),  # silvered violet
    'ranger':  ((12, 30, 18), (38, 78, 48), (72, 132, 84), (124, 200, 128), (216, 248, 206)),  # bronzed forest
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only, since the
# egg-and-dart field otherwise tiles every opaque pixel): (deep shadow / base / highlight).
BODY = {
    'warrior': ((44, 30, 14), (82, 58, 26), (128, 96, 46)),   # dark bronze cloth
    'mage':    ((26, 24, 58), (52, 48, 104), (92, 86, 166)),   # dark violet cloth
    'ranger':  ((16, 40, 24), (38, 76, 50), (70, 122, 82)),    # dark forest cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_eggdart_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary38', largest=True,
    ),
    'legs': dict(
        outdir='_eggdart_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary38', largest=False,
    ),
    'boots': dict(
        outdir='_eggdart_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_eggdart', largest=False,
    ),
    'helmet': dict(
        outdir='_eggdartdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary38', largest=True,
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


def draw_eggdart(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the egg-and-dart enrichment onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, a rectangular
    lattice (PX across, PY down) places a convex ovoid EGG at every node and a pointed DART in
    every horizontal gap between eggs. The elliptical metric ee selects egg interior / bezel
    shell; convex ovoid shading (upper-left light) splits the egg into hilit / mid / shadow with
    a crown catch-light; a lozenge test places the raised dart. Only opaque body pixels are ever
    painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        # nearest egg node
        i = round(lx / PX)
        j = round(ly / PY)
        ex = i * PX
        ey = j * PY
        dxe = lx - ex
        dye = ly - ey
        ee = math.hypot(dxe / RX, dye / RY)
        if ee <= 1.0:
            lit = -(dxe / RX) - (dye / RY)
            if ee <= CATCH and lit > EDGE:
                put(fr, yy, xx, rim)                 # crown catch-light
            elif lit > EDGE:
                put(fr, yy, xx, hilit)               # lit upper-left flank
            elif lit < -EDGE:
                put(fr, yy, xx, shadow)              # lower-right flank
            else:
                put(fr, yy, xx, mid)                 # side
            continue
        if ee <= 1.0 + SHELL:
            put(fr, yy, xx, rim)                     # bright bezel shell ring
            continue
        # nearest dart in the horizontal gap (band centre-line at ey)
        i2 = round(lx / PX - 0.5)
        dxd = (i2 + 0.5) * PX
        ddx = lx - dxd
        ddy = ly - ey
        if abs(ddx) / DW + abs(ddy) / DH <= 1.0:
            # raised pointed tongue: bright tip catch near the point, hilit body
            if ddy >= DH * 0.45:
                put(fr, yy, xx, rim)                 # dart tip catch-light
            else:
                put(fr, yy, xx, hilit)               # dart body
            continue
        put(fr, yy, xx, ground)                      # recessed ground channel


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = EGGDART[cls]
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
        draw_eggdart(fr, comp, ground, shadow, mid, hilit, rim)
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
