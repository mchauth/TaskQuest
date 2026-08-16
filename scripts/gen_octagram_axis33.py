#!/usr/bin/env python3
"""THIRTY-THIRD net-new-geometry axis for ALL FOUR SLOTS — the OCTAGRAM / EIGHT-POINT
STAR-AND-CROSS / GIRIH family: an all-over tessellation of straight-edged EIGHT-POINTED STARS
whose points nearly touch tip-to-tip, leaving a small rotated-square "cross" interstice between
every block of four. Each star is the classic octagram {8/2} — the compound outline of an
axis-aligned SQUARE overlaid with a 45deg-rotated SQUARE (diamond) of equal circumradius, giving
eight straight-edged points meeting at eight re-entrant notches. A bright CORE dot sits at each
star centre. The repeated motif is the EIGHT-POINTED STAR OUTLINE; none of the thirty-two existing
legendary axes per slot occupy it:
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
  * 32nd FOUR CIRCULAR LOBES around each node meeting at four cusps -> quatrefoil / tracery
  * 33rd (this) an axis-square + a 45deg-square overlaid into an EIGHT-POINTED STAR OUTLINE that
        tessellates with a rotated-square cross interstice -> octagram / girih star-and-cross.

Critically distinct from the 32nd quatrefoil: the quatrefoil is a CURVED four-lobe rosette (four
circular arcs meeting at four cusps); the octagram is a STRAIGHT-EDGED eight-pointed star (two
overlaid squares). Distinct from the 14th lattice and 25th argyle: those give a single diamond /
lozenge; the octagram is an EIGHT-point star (a diamond AND a square superimposed) and it is drawn
as an OUTLINE, not a solid fill. Distinct from the 27th sunburst: sunburst shoots open rays that
never close; the octagram is a CLOSED star polygon outline. Distinct from the 20th trellis /
19th honeycomb / 17th ashlar: those tessellate 3-, 6- and 4-sided convex OUTLINE cells; the
octagram's repeat unit is a re-entrant EIGHT-pointed STAR, non-convex, meeting at points. The
eight-pointed straight-edged star outline is the defining, previously-unused geometry.

Per slot it lands as the 33rd distinct axis:
  * CHEST  — star cuirass: octagram star net down the whole cuirass.
  * LEGS   — star chausses: octagram star net down the thighs.
  * BOOTS  — star sabatons: octagram star net over the boot.
  * HELMET — star dome: octagram star net over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the component
bbox top-left. Star centres sit on an orthogonal lattice of pitch P. For the nearest 3x3 block of
nodes, each node (i,j) at (i*P, j*P) with local offset (dx, dy) defines two overlaid squares:
    fA = max(|dx|, |dy|) - W          (axis-aligned square, <0 inside)
    fB = (|dx| + |dy|) - W*sqrt(2)    (45deg square / diamond of equal circumradius, <0 inside)
The union boundary (the octagram outline) is the axis-square edge where OUTSIDE the diamond, or the
diamond edge where OUTSIDE the axis-square, so the outline distance at that node is
    dnode = min( |fA| if fB >= -TOL,  |fB| if fA >= -TOL )
and dmin over all candidate nodes decides the stroke tone:
    dmin <= RIB*CROWN     -> bright star crest (RIB_HI)
    dmin <= RIB           -> star flank        (RIB_MID)
    dmin <= RIB+GROOVE    -> recessed groove   (GROOVE)   (dark shadow hugging the star)
    else                  -> body ground   (the rotated-square cross interstice reads here)
A bright CORE (PIP) is stamped within PIP px of each node centre. Pitch P and half-width W tuned so
neighbouring stars nearly touch tip-to-tip on a ~14px torso, leaving the cross interstice open.
Anchoring to the component bbox keeps the net stable frame-to-frame.

Authoring philosophy identical to gen_quatrefoil_axis32.py / gen_ogee_axis31.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a pixel outside
the existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no net. Shading applied here via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 32nd quatrefoil (pierced gothic TRACERY: dark enamel +
filigree rosette) and the 31st ogee (woven damask brocade) the octagram family is DAMASCENED
STAR-INLAY on polished plate — a mid-tone burnished metal ground with a bright inlaid metal star
outline and a jewelled core, like a gold-and-steel damascene star boss. The inlay distinguishes
class:
  * warrior — gilt star on gunmetal plate (dark-steel groove / brass flank / bright-gold crest / pale-gold pip)
  * mage    — silver star on violet-steel plate (indigo groove / steel-blue flank / white-silver crest / pale pip)
  * ranger  — copper star on bronzed-forest plate (bottle groove / bronze flank / bright-copper crest / pale pip)

Run from repo root:
  python3 scripts/gen_octagram_axis33.py
Then QA (examples):
  python3 scripts/sprite_qa.py _octagram_legendary_preview/shirt_warrior_legendary33.png
  python3 scripts/sprite_qa.py _octadome_helmet_preview/helmet_mage_legendary33.png --y-min 2
  python3 scripts/sprite_qa.py _octagram_boots_preview/boots_warrior_legendary_octagram.png --y-max 63
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

# Octagram / eight-point star-and-cross geometry. Tuned high-frequency so the star reads on a
# ~14px torso: node pitch gives ~two stars across, half-width chosen so points of adjacent stars
# nearly touch tip-to-tip, thin ring so the star reads as an outline and the cross interstice stays
# open.
P = 7            # star lattice pitch (px between star centres, both axes)
W = 2.35         # axis-square half-width; diamond circumradius = W*sqrt(2) ~= 3.3 -> tips nearly touch
RIB = 0.9        # ring half-width (thin -> star reads as outline)
CROWN = 0.5      # within this fraction of RIB -> bright ring crest
GROOVE = 0.6     # dark groove band width hugging the ring beyond RIB
PIP = 0.8        # jewelled core radius at each star centre
TOL = 0.55       # union-outline tolerance so the eight star points join cleanly at the notches
S2 = math.sqrt(2.0)

# Per-class inlay tone quad: (GROOVE dark recess, RIB_MID flank, RIB_HI crest, PIP core).
OCTA = {
    'warrior': ((26, 22, 12), (150, 116, 44), (252, 216, 112), (255, 242, 186)),  # dark-steel / brass / gold / pale
    'mage':    ((20, 22, 46), (132, 148, 178), (240, 244, 255), (208, 222, 255)), # indigo / steel-blue / silver / pale
    'ranger':  ((16, 26, 18), (156, 104, 58), (248, 178, 108), (252, 224, 176)),  # bottle / bronze / copper / pale
}

# Per-class body (ground) tones for the recolor: (deep shadow / base / highlight).
BODY = {
    'warrior': ((44, 46, 52), (74, 78, 88), (112, 118, 130)),   # gunmetal plate
    'mage':    ((34, 32, 62), (58, 56, 100), (94, 92, 150)),    # violet-steel plate
    'ranger':  ((28, 44, 32), (50, 76, 54), (84, 116, 84)),     # bronzed-forest plate
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_octagram_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary33', largest=True,
    ),
    'legs': dict(
        outdir='_octagram_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary33', largest=False,
    ),
    'boots': dict(
        outdir='_octagram_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_octagram', largest=False,
    ),
    'helmet': dict(
        outdir='_octadome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary33', largest=True,
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


def draw_octagram(fr, comp, groove, rib_mid, rib_hi, pip):
    """Paint the octagram / eight-point star net onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, star centres sit on an
    orthogonal lattice of pitch P; the nearest 3x3 block of nodes each define an axis-square (fA)
    and a 45deg-square (fB) whose union outline is the eight-pointed star, and the pixel takes
    star-crest / star-flank / groove / body tone by its minimum distance to any candidate star
    outline, with a bright core stamped at each node centre. Only opaque body pixels are ever
    painted, so it cannot create strays."""
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
                dx = lx - cx
                dy = ly - cy
                dc = math.hypot(dx, dy)
                if dc < dcore:
                    dcore = dc
                adx = abs(dx)
                ady = abs(dy)
                fA = max(adx, ady) - W              # axis-aligned square edge
                fB = (adx + ady) - W * S2           # 45deg square (diamond) edge
                # union outline: square edge where outside/near the diamond, and vice-versa
                if fB >= -TOL:
                    d = abs(fA)
                    if d < dmin:
                        dmin = d
                if fA >= -TOL:
                    d = abs(fB)
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
        # else: leave the recolored body ground untouched (the cross interstice reads here)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    groove, rib_mid, rib_hi, pip = OCTA[cls]
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
        draw_octagram(fr, comp, groove, rib_mid, rib_hi, pip)
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
