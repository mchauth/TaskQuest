#!/usr/bin/env python3
"""THIRTY-SEVENTH net-new-geometry axis for ALL FOUR SLOTS — the COFFER / CAISSON /
SUNKEN-PANEL family: an all-over field of RECESSED RECTANGULAR PANELS on an orthogonal
lattice, each panel a flat SUNKEN FLOOR ringed by a REVERSED bevel and pinned by a small
jewel boss at its centre (coffered ceiling / caisson panelling / debossed strapwork). The
body is tiled by a square lattice (pitch P); the SHARED GRID between panels stands proud as a
bright LAND, and each cell dives DOWN into a flat recessed FLOOR through four bevelled REVEAL
walls whose shading is the INVERSE of a raised boss — under an upper-left light the TOP and
LEFT reveals fall into SHADOW while the BOTTOM and RIGHT reveals catch the HIGHLIGHT, proving
the panel is cut INTO the surface, not raised out of it. A small bright jewel PIP is bezel-set
at the bottom of each sunken floor. The repeated motif is the SUNKEN RECTANGULAR PANEL with a
reversed bevel and a proud grid; none of the thirty-six existing legendary axes per slot occupy
it:
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
  * 37th (this) a field of SUNKEN RECTANGULAR PANELS with a REVERSED bevel and a proud grid,
    each floor holding a small jewel boss -> coffered / caisson panelling.

Critically distinct from every prior axis, and DELIBERATELY the INVERSE RELIEF of the two
existing relief axes. Against the 35th FACET — its closest structural relative — the facet
cell is a RAISED four-sided PYRAMID that rises to a BRIGHT WHITE-HOT APEX PIP at the cell
centre, with the seam recessed at the shared edges (matter pushed OUT of the surface toward
the light); the coffer cell is the exact opposite — a FLAT SUNKEN FLOOR pushed IN, its four
straight bevelled walls shaded in REVERSE (top/left dark, bottom/right light) so the centre is
the LOW point and the shared GRID between cells is the proud high LAND. Against the 36th QUILT,
the quilt cell is a ROUNDED CONVEX cushion on a DIAMOND (45deg) lattice pinned by a SUNKEN
ROUND button at the nodes; the coffer cell is an ANGULAR FLAT-FLOORED rectangular recess on an
ORTHOGONAL lattice with straight bevelled reveals and a proud grid (no rounding, no diamonds,
no round buttons). It is NOT the 17th ashlar (that draws only the flat mortar OUTLINE of
rectangular cells with no relief — the coffer is a fully modelled 3-D recess with bevelled
walls and a floor, exactly the relationship the 35th facet has to the 14th lattice), NOT the
13th studwork (isolated RAISED round rivets on a plain ground — coffer is edge-to-edge SUNKEN
rectangular panels meeting at a shared proud grid), NOT the 26th tartan (flat crossed colour
bands, no relief). The sunken flat-floored rectangular panel with a reversed bevel and a proud
grid is the defining, previously-unused geometry.

Per slot it lands as the 37th distinct axis:
  * CHEST  — coffered cuirass: sunken-panel field down the whole breastplate.
  * LEGS   — coffered chausses: sunken-panel field down the thighs.
  * BOOTS  — coffered sabatons: sunken-panel field over the boot.
  * HELMET — coffered dome: sunken-panel field over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the
component bbox top-left. Square lattice pitch P: u = frac(lx/P), v = frac(ly/P) in [0,1) are
the in-cell coords; du = min(u, 1-u), dv = min(v, 1-v), de = min(du, dv) = distance to the
nearest cell edge; dc = hypot(u-0.5, v-0.5) = distance to the cell centre. Under an upper-left
light:
    de <= LAND                      -> proud shared GRID land between panels (bright)
    de <= LAND+BEV : bevelled REVEAL wall, tone by nearest edge (REVERSED for a recess) —
        nearest edge is left/right if du<dv else top/bottom;
        LEFT (u<0.5) or TOP (v<0.5)   -> SHADOW wall (falls away from the light)
        RIGHT (u>=0.5) or BOTTOM      -> HILIT wall (catches the light)
    dc <= PIPR                      -> jewel PIP bezel-set in the sunken floor centre
    else                            -> flat recessed FLOOR (darkest field)
P/LAND/BEV tuned so ~2 panels span a ~14px torso and the proud grid + reversed bevel read.
Anchoring to the bbox keeps the net stable frame-to-frame.

Authoring philosophy identical to gen_facet_axis35.py / gen_quilt_axis36.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a pixel
outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run
sprite_shade.py again.

To read as a clearly DIFFERENT set the coffer family is CAST-BRONZE CAISSON PANELLING — a
plate stamped with recessed strapwork coffers, a jewel bezel-set at the bottom of each panel.
Class differs by metal/gem:
  * warrior — gilt-bronze coffer (dark-bronze floor / bronze shadow-reveal / brass grid / bright-gold hilit-reveal / white-gold pip)
  * mage    — silvered violet coffer (midnight floor / indigo shadow-reveal / steel-violet grid / bright-silver hilit-reveal / pale-white pip)
  * ranger  — bronzed forest coffer (deep-forest floor / bottle shadow-reveal / bronze-green grid / bright-emerald hilit-reveal / pale-green pip)

Run from repo root:
  python3 scripts/gen_coffer_axis37.py
Then QA (examples):
  python3 scripts/sprite_qa.py _coffer_legendary_preview/shirt_warrior_legendary37.png
  python3 scripts/sprite_qa.py _cofferdome_helmet_preview/helmet_mage_legendary37.png --y-min 2
  python3 scripts/sprite_qa.py _coffer_boots_preview/boots_warrior_legendary_coffer.png --y-max 63
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

# Coffer panel geometry. Tuned so the recessed panel reads on a ~14px torso: a square pitch
# giving ~two panels across, a 1px proud grid land, a bevelled reveal ring, a small jewel pip
# at the bottom of the flat recessed floor.
P = 7.0          # square-lattice pitch (in local px)
LAND = 0.12      # proud grid half-width in cell-fraction units (shared land between panels)
BEV = 0.17       # bevelled reveal-wall thickness beyond the land
PIPR = 0.13      # jewel-pip radius from cell centre

# Per-class coffer tone quintet: (FLOOR recessed field, SHADOW reveal wall, LAND proud grid,
# HILIT reveal wall, PIP jewel boss). Light comes from the upper-left; for a SUNKEN panel the
# TOP/LEFT reveal walls fall into SHADOW and the BOTTOM/RIGHT walls catch the HILIT (reversed
# vs a raised boss), the shared grid stands proud as the bright LAND, the floor is the low
# dark field, and a jewel PIP is bezel-set at the floor centre.
COFFER = {
    'warrior': ((40, 26, 10), (96, 64, 24), (168, 126, 52), (236, 190, 86), (255, 238, 168)),  # gilt-bronze
    'mage':    ((18, 16, 46), (66, 54, 114), (116, 100, 182), (176, 158, 240), (236, 228, 255)),  # silvered violet
    'ranger':  ((12, 30, 18), (38, 78, 48), (72, 132, 84), (124, 200, 128), (216, 248, 206)),  # bronzed forest
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only, since the
# coffer field otherwise tiles every opaque pixel): (deep shadow / base / highlight).
BODY = {
    'warrior': ((44, 30, 14), (82, 58, 26), (128, 96, 46)),   # dark bronze cloth
    'mage':    ((26, 24, 58), (52, 48, 104), (92, 86, 166)),   # dark violet cloth
    'ranger':  ((16, 40, 24), (38, 76, 50), (70, 122, 82)),    # dark forest cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_coffer_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary37', largest=True,
    ),
    'legs': dict(
        outdir='_coffer_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary37', largest=False,
    ),
    'boots': dict(
        outdir='_coffer_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_coffer', largest=False,
    ),
    'helmet': dict(
        outdir='_cofferdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary37', largest=True,
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


def draw_coffer(fr, comp, floor, shadow, land, hilit, pip):
    """Paint the sunken rectangular-panel field onto one component. For each opaque body pixel,
    in component-local coords (lx, ly) anchored at the component bbox top-left, a square lattice
    (pitch P) defines cells whose SHARED GRID stands proud (land) and whose interior dives into
    a flat recessed FLOOR through four bevelled REVEAL walls. de = distance to nearest cell edge
    selects land / reveal ring; within the reveal the nearest edge picks the wall, shaded in
    REVERSE for a recess (top/left shadow, bottom/right hilit); dc = distance to cell centre
    picks the jewel pip; otherwise the recessed floor. Only opaque body pixels are ever painted,
    so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        u = (lx / P) % 1.0
        v = (ly / P) % 1.0
        du = min(u, 1.0 - u)
        dv = min(v, 1.0 - v)
        de = du if du < dv else dv
        if de <= LAND:
            put(fr, yy, xx, land)                       # proud shared grid between panels
            continue
        if de <= LAND + BEV:
            # bevelled reveal wall — REVERSED shading for a recess
            if du < dv:                                  # nearest edge is left / right
                put(fr, yy, xx, shadow if u < 0.5 else hilit)
            else:                                        # nearest edge is top / bottom
                put(fr, yy, xx, shadow if v < 0.5 else hilit)
            continue
        dc = math.hypot(u - 0.5, v - 0.5)
        if dc <= PIPR:
            put(fr, yy, xx, pip)                         # jewel bezel-set in the sunken floor
            continue
        put(fr, yy, xx, floor)                           # flat recessed floor


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    floor, shadow, land, hilit, pip = COFFER[cls]
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
        draw_coffer(fr, comp, floor, shadow, land, hilit, pip)
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
