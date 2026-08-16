#!/usr/bin/env python3
"""THIRTY-SIXTH net-new-geometry axis for ALL FOUR SLOTS — the QUILTED / CAPITONNE / TUFTED
DIAMOND-CUSHION family: an all-over field of CONVEX PADDED DIAMOND CUSHIONS on a DIAGONAL
lattice, each cushion bulging up between four SUNKEN BUTTON TUFTS at the lattice nodes
(button-tufted upholstery / Chesterfield quilting / padded gambeson). The body is tiled by a
diamond (45deg) lattice; the CENTRE of every diamond cell is the high point of a rounded
cushion, softly graded bright->dark under an upper-left light, while the four CORNERS of the
cell (the lattice nodes, where four cushions meet) are pulled DOWN into a dark round BUTTON
DIMPLE, with the puckered SEAM running along the diamond edges between cushions. The repeated
motif is the CONVEX ROUNDED DIAMOND CUSHION with a SUNKEN BUTTON at each node; none of the
thirty-five existing legendary axes per slot occupy it:
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
  * 35th a TESSELLATION OF RAISED FOUR-FACET PYRAMIDS with directional facet shading (facet)
  * 36th (this) a field of CONVEX ROUNDED DIAMOND CUSHIONS on a diagonal lattice, each bulge
    smoothly shaded and pinned by a SUNKEN BUTTON TUFT at every node -> quilted / capitonne
    tufted upholstery.

Critically distinct from every prior axis. Against the 35th facet — its closest relative as
the other RELIEF axis — the facet cell is an ANGULAR four-sided PYRAMID on a SQUARE lattice
that rises to a BRIGHT WHITE-HOT APEX PIP at the cell centre with hard flat-shaded triangular
facets meeting at a crisp ridge; the quilt cell is a SMOOTH ROUNDED (convex) cushion on a
DIAMOND lattice whose HIGH POINT is a soft graded highlight (not a hard pip) and whose defining
feature is the DARK SUNKEN BUTTON DIMPLE at each NODE where cushions meet — an INVERSE relief
(facet: bright point up at cell centre, dark seam at edges; quilt: soft bulge at cell centre,
dark sunken button at the corners). It is not the 25th argyle (those diamonds are FILLED FLAT
with ONE solid colour on a diagonal lattice; the quilt diamond is a graded convex DOME with a
sunken button, a relief not a fill), not the 14th lattice (diamond OUTLINE only), and not the
13th studwork (isolated raised round rivets on a plain ground; here the whole surface is
edge-to-edge cushions and the round features are SUNKEN buttons at shared nodes). The convex
rounded diamond cushion pinned by a sunken node button is the defining, previously-unused
geometry.

Per slot it lands as the 36th distinct axis:
  * CHEST  — quilted gambeson: padded-cushion field down the whole cuirass.
  * LEGS   — quilted chausses: padded-cushion field down the thighs.
  * BOOTS  — quilted sabatons: padded-cushion field over the boot.
  * HELMET — quilted coif: padded-cushion field over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the
component bbox top-left. The diamond lattice is the rotated grid s = lx + ly, t = lx - ly with
pitch P; buttons (nodes) sit at integer (s/P, t/P), cushion centres at the half-integer cell
centres. For a pixel, let gs = frac(s/P), gt = frac(t/P) in [0,1); the four cell CORNERS
(0/1, 0/1) are buttons, the CELL CENTRE (0.5, 0.5) is the cushion crown. dn = distance to the
nearest corner (button), dc = distance to the cell centre. Under an upper-left light (which in
this rotated space runs along -gs), lit = gs - 0.5 (negative = lit side):
    dn <= BUT                                 -> sunken BUTTON dimple (darkest)
    dc <= PIPR and lit < 0                     -> soft crown HIGHLIGHT (specular, not hard pip)
    dc <= CUSH and lit < -EDGE                 -> lit upper cushion face (RIB_HI)
    dc <= CUSH and lit >  EDGE                 -> shadow lower cushion face (RIB_LO)
    dc <= CUSH                                 -> cushion side (RIB_MID)
    else (near cell edge)                      -> puckered SEAM between cushions (dark thread)
P/BUT/CUSH tuned so ~2 cushions span a ~14px torso and the tuft + bulge read. Anchoring to the
bbox keeps the net stable frame-to-frame.

Authoring philosophy identical to gen_facet_axis35.py / gen_seigaiha_axis34.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a pixel
outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run
sprite_shade.py again.

To read as a clearly DIFFERENT set the quilt family is TUFTED PADDED UPHOLSTERY — a quilted
gambeson of jewelled velvet stitched with metal buttons. Class differs by cloth/metal:
  * warrior — gilt-buttoned oxblood quilt (dark-bronze button / bronze seam / gold-brown mid / bright-gold hi / pale-gold crown)
  * mage    — silver-buttoned violet quilt (indigo button / deep-violet seam / violet mid / lilac hi / white crown)
  * ranger  — copper-buttoned forest quilt (bottle button / deep-green seam / green mid / bright-green hi / pale-green crown)

Run from repo root:
  python3 scripts/gen_quilt_axis36.py
Then QA (examples):
  python3 scripts/sprite_qa.py _quilt_legendary_preview/shirt_warrior_legendary36.png
  python3 scripts/sprite_qa.py _quiltdome_helmet_preview/helmet_mage_legendary36.png --y-min 2
  python3 scripts/sprite_qa.py _quilt_boots_preview/boots_warrior_legendary_quilt.png --y-max 63
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

# Quilt cushion geometry. Tuned so the cushion reads on a ~14px torso: a diamond pitch giving
# ~two cushions across, a soft graded bulge, a crisp sunken button tuft at each node, a thin
# puckered seam between cushions.
P = 7.0          # diamond-lattice pitch (in s = lx+ly / t = lx-ly units)
BUT = 0.16       # button-dimple radius in cell-fraction units (sunken tuft at each node)
CUSH = 0.42      # cushion radius from cell centre; beyond this = puckered seam
PIPR = 0.14      # soft crown-highlight radius from cell centre
EDGE = 0.10      # directional threshold splitting lit / mid / shadow cushion faces

# Per-class quilt tone quintet: (BUTTON dimple, SEAM pucker, RIB_MID side, RIB_HI lit face,
# CROWN highlight). Light comes from the upper-left: lit face = RIB_HI, shadow face = RIB_LO
# (reused = SEAM tone for a soft plunge into the button), crown = CROWN, node = BUTTON.
QUILT = {
    'warrior': ((30, 18, 8), (92, 60, 22), (150, 108, 40), (226, 178, 74), (255, 234, 158)),   # gilt oxblood
    'mage':    ((16, 14, 44), (62, 50, 108), (110, 92, 176), (168, 150, 236), (232, 224, 255)),  # silver violet
    'ranger':  ((10, 28, 16), (34, 74, 44), (64, 128, 78), (116, 194, 122), (214, 246, 202)),   # copper forest
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only, since the
# cushion field otherwise tiles every opaque pixel): (deep shadow / base / highlight).
BODY = {
    'warrior': ((44, 30, 14), (82, 58, 26), (128, 96, 46)),   # dark oxblood-gold cloth
    'mage':    ((26, 24, 58), (52, 48, 104), (92, 86, 166)),   # dark violet cloth
    'ranger':  ((16, 40, 24), (38, 76, 50), (70, 122, 82)),    # dark forest cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_quilt_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary36', largest=True,
    ),
    'legs': dict(
        outdir='_quilt_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary36', largest=False,
    ),
    'boots': dict(
        outdir='_quilt_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_quilt', largest=False,
    ),
    'helmet': dict(
        outdir='_quiltdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary36', largest=True,
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


def draw_quilt(fr, comp, button, seam, rib_mid, rib_hi, crown):
    """Paint the tufted diamond-cushion field onto one component. For each opaque body pixel,
    in component-local coords (lx, ly) anchored at the component bbox top-left, the diamond
    lattice s = lx+ly, t = lx-ly with pitch P defines cells whose CORNERS are buttons (nodes)
    and whose CENTRE is the cushion crown. dn = distance to nearest corner (button), dc =
    distance to cell centre. lit = gs-0.5 (upper-left light in the rotated frame) splits the
    convex cushion into lit / side / shadow faces; the node gets a sunken button dimple and
    the cell edge a puckered seam. Only opaque body pixels are ever painted, so it cannot
    create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        s = (lx + ly) / P
        t = (lx - ly) / P
        gs = s - math.floor(s)          # [0,1)
        gt = t - math.floor(t)
        # distance to nearest cell corner (button node) and to cell centre (cushion crown)
        cx = 0.0 if gs < 0.5 else 1.0
        cy = 0.0 if gt < 0.5 else 1.0
        dn = math.hypot(gs - cx, gt - cy)
        dc = math.hypot(gs - 0.5, gt - 0.5)
        lit = gs - 0.5                  # upper-left light runs along -gs in this rotated frame
        if dn <= BUT:
            put(fr, yy, xx, button)                 # sunken button tuft at node
            continue
        if dc <= PIPR and lit < 0:
            put(fr, yy, xx, crown)                  # soft crown highlight
            continue
        if dc <= CUSH:
            if lit < -EDGE:
                put(fr, yy, xx, rib_hi)             # lit upper cushion face
            elif lit > EDGE:
                put(fr, yy, xx, seam)               # shadow lower cushion face (plunge to button)
            else:
                put(fr, yy, xx, rib_mid)            # cushion side
            continue
        put(fr, yy, xx, seam)                       # puckered seam between cushions


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    button, seam, rib_mid, rib_hi, crown = QUILT[cls]
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
        draw_quilt(fr, comp, button, seam, rib_mid, rib_hi, crown)
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
