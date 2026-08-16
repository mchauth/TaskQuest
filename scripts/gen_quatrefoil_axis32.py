#!/usr/bin/env python3
"""THIRTY-SECOND net-new-geometry axis for ALL FOUR SLOTS — the QUATREFOIL / GOTHIC-TRACERY /
CLOVERLEAF family: an all-over net of FOUR-LOBED cusped rosettes, the unmistakable pierced
cathedral-tracery / quatrefoil silhouette. At every lattice node four equal circular LOBES are
arranged around the node centre (one offset up, down, left, right); the four lobe arcs meet at
CUSPS to enclose a four-petalled clover, and adjacent quatrefoils touch at cusps too, leaving a
small concave-square PIERCE between every block of four. A bright CORE dot sits at each rosette
centre. The repeated motif is the QUATREFOIL — a compound outline of FOUR circular lobes meeting
at four inward cusps, radially four-fold symmetric; none of the thirty-one existing legendary axes
per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> straight-edged lozenge OUTLINE (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS all facing ONE way -> imbricated scale field
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone / twill
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th tessellation of SIX-sided straight OUTLINE cells -> honeycomb
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE outlines, ONE ring per centre -> chainmail
  * 22nd ONE CONTINUOUS UNDULATING SINE line -> watered-steel ripple
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th CONTINUOUS CURVED COILS winding around a CENTRE point -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE -> sunburst / compass
  * 28th STACKS NESTED CLOSED RINGS at growing radius around a CENTRE -> concentric target
  * 29th INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill -> houndstooth
  * 30th TWO INTERTWINING STRANDS braiding OVER-UNDER down a column -> cable / rope
  * 31st COUNTER-PHASE RIBS PINCH-AND-BULGE to enclose POINTED-OVAL cells -> ogee / damask
  * 32nd (this) FOUR CIRCULAR LOBES around each node meeting at four cusps -> quatrefoil / tracery.

Critically distinct from the 21st chainmail: chainmail stamps ONE single-radius circle per centre;
the quatrefoil stamps FOUR circles arranged as a four-fold rosette that meet at cusps. Distinct
from the 28th concentric: concentric stacks several rings at growing radius around a SINGLE point;
the quatrefoil is FOUR equal lobes offset in four directions, never nested. Distinct from the 31st
ogee: the ogee cell is a TWO-cusp pointed oval formed by counter-phase vertical ribs; the
quatrefoil is a FOUR-cusp four-lobe rosette on an orthogonal lattice with no vertical rib system.
Distinct from the 15th scale: scale arcs all face ONE way and stay open (never close into a cell);
quatrefoil lobes face FOUR directions and close into a four-petal rosette. The four-lobe rosette
meeting at four inward cusps is the defining, previously-unused geometry.

Per slot it lands as the 32nd distinct axis:
  * CHEST  — tracery cuirass: quatrefoil rosette net down the whole cuirass.
  * LEGS   — tracery chausses: quatrefoil rosette net down the thighs.
  * BOOTS  — tracery sabatons: quatrefoil rosette net over the boot.
  * HELMET — tracery dome: quatrefoil rosette net over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the component
bbox top-left. Rosette centres sit on an orthogonal lattice of pitch P. For the nearest 3x3 block
of nodes, each node (i,j) at (i*P, j*P) contributes four LOBE centres offset by +/-LOBE along x and
y; for every lobe the RING distance |dist_to_lobe_centre - LR| is measured, and the minimum ring
distance dmin over all candidate lobes decides the stroke tone:
    dmin <= RIB*CROWN     -> bright lobe crest (RIB_HI)
    dmin <= RIB           -> lobe flank        (RIB_MID)
    dmin <= RIB+GROOVE    -> recessed groove   (GROOVE)   (dark shadow hugging the tracery)
    else                  -> body ground
A bright CORE (PIP) is stamped within PIP px of each node centre. With LOBE==LR each lobe circle
passes through its node centre, so the four lobes form a true clover meeting at the centre; pitch
P tuned so neighbouring rosettes just touch at cusps on a ~14px torso. Anchoring to the component
bbox keeps the net stable frame-to-frame.

Authoring philosophy identical to gen_ogee_axis31.py / gen_cable_axis30.py: every pattern pixel is
painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a pixel outside the
existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no net. Shading applied here via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 31st ogee (woven damask brocade), 28th concentric
(engraved target-work) and 21st chainmail (blued rings) the quatrefoil family is PIERCED GOTHIC
TRACERY — a dark stone/enamel ground with a bright metal filigree rosette and a jewelled core,
cathedral rose-window stonework. The tracery distinguishes class:
  * warrior — bronze tracery on oxblood enamel (garnet groove / bronze flank / bright-gold crest / pip)
  * mage    — silver tracery on midnight-blue enamel (indigo groove / steel flank / moonsilver crest / pip)
  * ranger  — antique-gold tracery on mossy-green enamel (bottle groove / antique-gold flank / gold crest / pip)

Run from repo root:
  python3 scripts/gen_quatrefoil_axis32.py
Then QA (examples):
  python3 scripts/sprite_qa.py _quatrefoil_legendary_preview/shirt_warrior_legendary32.png
  python3 scripts/sprite_qa.py _quatredome_helmet_preview/helmet_mage_legendary32.png --y-min 2
  python3 scripts/sprite_qa.py _quatrefoil_boots_preview/boots_warrior_legendary_quatrefoil.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Quatrefoil / gothic-tracery geometry. Tuned high-frequency so the four-lobe rosette reads on a
# ~14px torso: node pitch gives two rosettes across, lobe offset == lobe radius so each lobe passes
# through the rosette centre (true clover), thin ring so the pierce between rosettes stays open.
P = 7            # rosette lattice pitch (px between rosette centres, both axes)
LOBE = 1.7       # lobe-centre offset from node along x and y
LR = 1.7         # lobe circle radius (== LOBE -> lobes meet at the node centre)
RIB = 0.9        # ring half-width (thin -> pierce stays open)
CROWN = 0.5      # within this fraction of RIB -> bright ring crest
GROOVE = 0.6     # dark groove band width hugging the ring beyond RIB
PIP = 0.8        # jewelled core radius at each rosette centre

# Per-class tracery tone quad: (GROOVE dark recess, RIB_MID flank, RIB_HI crest, PIP core).
QUAT = {
    'warrior': ((40, 8, 10), (150, 110, 40), (250, 214, 110), (255, 240, 180)),   # garnet / bronze / gold / pale
    'mage':    ((22, 20, 48), (140, 150, 175), (242, 244, 255), (205, 220, 255)), # indigo / steel / moonsilver / pale
    'ranger':  ((14, 28, 18), (150, 120, 56), (236, 206, 120), (250, 232, 170)),  # bottle / antique-gold / gold / pale
}

# Per-class body (ground) tones for the recolor: (deep shadow / base / highlight).
BODY = {
    'warrior': ((70, 18, 22), (112, 30, 34), (158, 54, 54)),     # oxblood enamel
    'mage':    ((30, 34, 74), (54, 60, 118), (92, 100, 168)),    # midnight-blue enamel
    'ranger':  ((26, 48, 30), (48, 82, 50), (82, 120, 80)),      # mossy-green enamel
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_quatrefoil_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary32', largest=True,
    ),
    'legs': dict(
        outdir='_quatrefoil_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary32', largest=False,
    ),
    'boots': dict(
        outdir='_quatrefoil_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_quatrefoil', largest=False,
    ),
    'helmet': dict(
        outdir='_quatredome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary32', largest=True,
    ),
}


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


# lobe-centre offsets (up / down / left / right) around each rosette node
LOBES = ((LOBE, 0.0), (-LOBE, 0.0), (0.0, LOBE), (0.0, -LOBE))


def draw_quatrefoil(fr, comp, groove, rib_mid, rib_hi, pip):
    """Paint the quatrefoil / gothic-tracery net onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, rosette centres sit on
    an orthogonal lattice of pitch P; the nearest 3x3 block of nodes each contribute four lobe
    circles, and the pixel takes ring-crest / ring-flank / groove / body tone by its minimum ring
    distance to any candidate lobe, with a bright core stamped at each node centre. Only opaque
    body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        i0 = int(round(lx / P))
        j0 = int(round(ly / P))
        dmin = 1e9
        dcore = 1e9
        for i in (i0 - 1, i0, i0 + 1):
            for j in (j0 - 1, j0, j0 + 1):
                cx = i * P
                cy = j * P
                dc = math.hypot(lx - cx, ly - cy)
                if dc < dcore:
                    dcore = dc
                for ox, oy in LOBES:
                    d = abs(math.hypot(lx - (cx + ox), ly - (cy + oy)) - LR)
                    if d < dmin:
                        dmin = d
        if dcore <= PIP:
            put(fr, yy, xx, pip)
            continue
        if dmin <= RIB * CROWN:
            put(fr, yy, xx, rib_hi)
        elif dmin <= RIB:
            put(fr, yy, xx, rib_mid)
        elif dmin <= RIB + GROOVE:
            put(fr, yy, xx, groove)
        # else: leave the recolored body ground untouched


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    groove, rib_mid, rib_hi, pip = QUAT[cls]
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
            lbl, n = ndimage.label(a)
            if n >= 1:
                sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
                comp = (lbl == (int(np.argmax(sizes)) + 1))
            else:
                comp = a
        else:
            comp = a
        draw_quatrefoil(fr, comp, groove, rib_mid, rib_hi, pip)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
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
