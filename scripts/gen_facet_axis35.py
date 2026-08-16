#!/usr/bin/env python3
"""THIRTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS — the FACET / DIAMOND-POINT /
PYRAMIDAL-BOSS family: an all-over tessellation of RAISED FOUR-FACET PYRAMIDS (diamond-point
rustication / faceted gemstone bosses). The body is tiled by a square lattice; every cell is
a little four-sided pyramid rising to a bright apex at the cell centre, its four TRIANGULAR
FACETS (left / top / right / bottom) each flat-shaded by the direction it faces under an
upper-left light, with a dark recessed VALLEY seam in the channels between neighbouring
pyramids and a white-hot apex PIP at each summit. The repeated motif is the SOLID-MODELLED
FOUR-FACET PYRAMID with directional facet shading; none of the thirty-four existing legendary
axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE ROUND POINTS (rivet-stud grid)
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
  * 35th (this) a TESSELLATION OF RAISED FOUR-FACET PYRAMIDS with directional facet
    shading -> diamond-point / faceted-gem rustication.

Critically distinct from every prior axis by being a SOLID-MODELLED RELIEF rather than a
line/arc/point/outline drawn on a flat ground: where the 25th argyle FILLS each lozenge with
ONE flat colour and the 14th lattice draws the diamond OUTLINE, the facet cell is a raised
pyramid whose FOUR triangular faces each take a DIFFERENT tone by which way the face is
tilted (left face lit brightest, bottom face darkest) — a directional bevel, not a fill. It
is not the 13th studwork (those are ISOLATED round rivet dots on a plain ground; the facet
field is edge-to-edge pyramids that tile the WHOLE surface, meeting along shared valley
seams), not the 17th ashlar (flat rectangular outline cells, no relief), and not the 27th
sunburst (open rays from a point). The four-facet raised pyramid with per-face directional
tone is the defining, previously-unused geometry.

Per slot it lands as the 35th distinct axis:
  * CHEST  — faceted cuirass: pyramid-boss field down the whole cuirass.
  * LEGS   — faceted chausses: pyramid-boss field down the thighs.
  * BOOTS  — faceted sabatons: pyramid-boss field over the boot.
  * HELMET — faceted dome: pyramid-boss field over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the
component bbox top-left. Pyramid apices sit on a square lattice of pitch P. Each pixel is
assigned to its nearest apex; let (u, v) be the offset from that apex (u right, v down), each
in [-P/2, P/2]. The distance to the nearest cell BOUNDARY, edge = min(P/2 - |u|, P/2 - |v|),
picks the recessed valley seam when small. Otherwise the dominant axis and its sign pick the
facet the pixel lies on:
    edge <= SEAM                         -> recessed valley seam (darkest channel)
    within PIP of the apex                -> white-hot apex pip (summit)
    |u| >= |v|, u < 0                     -> LEFT face   (lit brightest, RIB_HI)
    |u| >= |v|, u >= 0                    -> RIGHT face  (shadow, RIB_LO)
    |u| <  |v|, v < 0                     -> TOP face    (mid-lit, RIB_MID)
    |u| <  |v|, v >= 0                    -> BOTTOM face (deep shadow, RIB_LO)
P/PIP/SEAM tuned so ~2-3 pyramids span a ~14px torso and the facet split reads. Anchoring to
the bbox keeps the net stable frame-to-frame.

Authoring philosophy identical to gen_seigaiha_axis34.py / gen_octagram_axis33.py: every
pattern pixel is painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run
sprite_shade.py again.

To read as a clearly DIFFERENT set the facet family is a field of CUT GEMSTONES bezel-set in
metal — a faceted jewel whose facing faces catch light and shade. Class differs by gem/metal:
  * warrior — topaz-and-gold (bronze-shadow valley / shadow-gold face / brass face / bright-gold lit face / white-gold pip)
  * mage    — sapphire-and-silver (midnight valley / indigo face / blue face / bright-blue lit face / pale pip)
  * ranger  — emerald-and-bronze (deep-forest valley / bottle face / emerald face / bright-emerald lit face / pale-green pip)

Run from repo root:
  python3 scripts/gen_facet_axis35.py
Then QA (examples):
  python3 scripts/sprite_qa.py _facet_legendary_preview/shirt_warrior_legendary35.png
  python3 scripts/sprite_qa.py _facetdome_helmet_preview/helmet_mage_legendary35.png --y-min 2
  python3 scripts/sprite_qa.py _facet_boots_preview/boots_warrior_legendary_facet.png --y-max 63
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

# Facet pyramid geometry. Tuned so the boss reads on a ~14px torso: pitch gives ~two-three
# pyramids across, a crisp four-face split, a thin dark valley seam, a bright apex pip.
P = 5.0          # square-lattice pitch between pyramid apices
SEAM = 0.7       # distance-to-cell-edge under which the pixel is the recessed valley seam
PIP = 0.85       # apex pip radius (summit highlight)

# Per-class facet tone quintet: (SEAM valley, RIB_LO shadow face, RIB_MID face, RIB_HI lit
# face, PIP apex). Light comes from the upper-left: LEFT face = RIB_HI, TOP = RIB_MID,
# RIGHT & BOTTOM = RIB_LO, valley = SEAM, summit = PIP.
GEM = {
    'warrior': ((28, 20, 8), (120, 86, 28), (176, 132, 44), (240, 196, 86), (255, 240, 180)),  # topaz/gold
    'mage':    ((14, 14, 40), (56, 64, 132), (96, 116, 196), (150, 176, 246), (222, 232, 255)),  # sapphire/silver
    'ranger':  ((10, 26, 16), (36, 86, 52), (60, 132, 80), (110, 190, 120), (216, 246, 206)),  # emerald/bronze
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only, since the
# facet field otherwise tiles every opaque pixel): (deep shadow / base / highlight).
BODY = {
    'warrior': ((40, 34, 18), (76, 62, 30), (120, 98, 48)),   # dark topaz-gold metal
    'mage':    ((24, 26, 56), (48, 54, 104), (86, 100, 168)),  # dark sapphire metal
    'ranger':  ((18, 40, 26), (40, 78, 52), (72, 124, 84)),    # dark emerald metal
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_facet_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary35', largest=True,
    ),
    'legs': dict(
        outdir='_facet_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary35', largest=False,
    ),
    'boots': dict(
        outdir='_facet_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_facet', largest=False,
    ),
    'helmet': dict(
        outdir='_facetdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary35', largest=True,
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


def draw_facet(fr, comp, seam, rib_lo, rib_mid, rib_hi, pip):
    """Paint the faceted pyramid-boss field onto one component. For each opaque body pixel,
    in component-local coords (lx, ly) anchored at the component bbox top-left, the nearest
    pyramid apex sits on a square lattice of pitch P; the pixel's offset (u, v) from that apex
    picks the valley seam (near a cell edge), the apex pip (near the summit), or one of the
    four triangular faces (left lit / top mid / right & bottom shadow) by dominant axis and
    sign. Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        i = round(lx / P)
        j = round(ly / P)
        u = lx - i * P          # in [-P/2, P/2]
        v = ly - j * P
        if math.hypot(u, v) <= PIP:
            put(fr, yy, xx, pip)
            continue
        edge = min(P / 2.0 - abs(u), P / 2.0 - abs(v))
        if edge <= SEAM:
            put(fr, yy, xx, seam)
            continue
        if abs(u) >= abs(v):
            put(fr, yy, xx, rib_hi if u < 0 else rib_lo)   # left lit / right shadow
        else:
            put(fr, yy, xx, rib_mid if v < 0 else rib_lo)  # top mid / bottom shadow


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    seam, rib_lo, rib_mid, rib_hi, pip = GEM[cls]
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
        draw_facet(fr, comp, seam, rib_lo, rib_mid, rib_hi, pip)
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
