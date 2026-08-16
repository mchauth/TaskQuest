#!/usr/bin/env python3
"""TWENTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS — the ARGYLE / HARLEQUIN family:
an all-over field of SOLID-FILLED DIAMONDS laid on the diagonal, alternating body-tone and
a contrast "diamond" tone in a rotated checkerboard, overlaid with a fine cross-stitch line
along the two diagonals. The repeated motif is the SOLID FILLED LOZENGE CELL. This is the
first SOLID-FILL tessellation axis; none of the twenty-four existing legendary axes per slot
occupy it:
  * 11th laid CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th laid CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th laid TWO crossing STRAIGHT diagonal families -> lozenge OUTLINE / diamond MESH
  * 15th laid OVERLAPPING SHORT CURVED ARCS -> imbricated scale field
  * 16th laid SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone/twill
  * 17th laid a STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th laid a CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th laid a tessellation of SIX-sided OUTLINE cells -> honeycomb
  * 20th laid THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st laid a staggered grid of closed CIRCLE OUTLINES -> chainmail rings
  * 22nd laid CONTINUOUS UNDULATING SINE lines -> watered-steel ripple
  * 23rd laid a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th laid CONTINUOUS CURVED COILS winding around centres -> spiral / volute whorl
  * 25th (this) FILLS ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin.
Critically distinct from the 14th LATTICE: the lattice draws the diamond OUTLINE net (thin
crossing diagonal lines with EMPTY diamond interiors); argyle FILLS alternate diamonds SOLID
so the motif is a two-tone AREA tessellation, not a line net. Distinct from every other prior
axis, all of which are line, point, arc, coil, ring or open-cell-OUTLINE fields — this is the
only axis whose cells are FILLED. The fine cross-stitch diagonal line is a minor classic
accent, not the motif.

Per slot it lands as the 25th distinct axis:
  * CHEST  — harlequin cuirass: diamond field over the whole cuirass.
  * LEGS   — harlequin chausses: diamond field over the thighs.
  * BOOTS  — harlequin sabatons: diamond field over the boot.
  * HELMET — harlequin dome: diamond field over the whole crown.

Authoring philosophy is identical to gen_spiral_axis24.py / gen_meander_axis23.py: every
argyle pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction. Sleep
frames (fi>=60, lying down) get the recolor only — no diamonds. Shading applied in this
script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 24th (spiral, verdigris teal body + copper coil)
the harlequin family is a REGAL JEWEL look: a rich saturated body per class with a bright
warm GOLD diamond fill and a pale CREAM cross-stitch line. The shared gold diamond over a
jewel body reads instantly as "court harlequin regalia" while the body tint distinguishes
class:
  * warrior — deep crimson-wine body + bright gold diamond, cream cross-line
  * mage    — royal violet body + pale-gold diamond, silver-cream cross-line
  * ranger  — deep bottle-green body + antique-brass diamond, tan-cream cross-line

Run from repo root:
  python3 scripts/gen_argyle_axis25.py
Then QA (examples):
  python3 scripts/sprite_qa.py _argyle_legendary_preview/shirt_warrior_legendary25.png
  python3 scripts/sprite_qa.py _argyledome_helmet_preview/helmet_mage_legendary25.png --y-min 2
  python3 scripts/sprite_qa.py _argyle_boots_preview/boots_warrior_legendary_argyle.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Argyle geometry. Work in rotated coordinates u = dx + dy, v = dx - dy (a 45-degree rotation
# of the component-local pixel offset). A CELL x CELL checker in (u, v) space becomes a field
# of diagonal DIAMONDS in screen space. Alternate diamonds (where the cell parity cu+cv is
# even) are FILLED with the diamond tone; the others keep the recolored body. A thin
# cross-stitch LINE is painted where u or v sits within LINE_W of a cell boundary, giving the
# classic argyle over-stitch. The field is anchored to the component bbox top-left so it is
# stable frame-to-frame.
CELL = 9                # diamond cell pitch in rotated (u/v) units
LINE_W = 0.9            # half-width of the cross-stitch line in rotated units


# Per-class accent palettes: (DIAMOND solid-fill tone, LINE cross-stitch tone).
SEAM = {
    'warrior': ((214, 170, 74), (238, 226, 190)),     # gold diamond, cream line
    'mage':    ((206, 182, 120), (224, 224, 236)),     # pale-gold diamond, silver-cream line
    'ranger':  ((186, 158, 92), (226, 216, 184)),      # antique-brass diamond, tan-cream line
}

# Per-class body tones: deep shadow / base / highlight. REGAL JEWEL variants so the set reads
# apart from spiral's teal verdigris: here the body is a rich saturated jewel tone and the
# diamond is a warm bright gold.
BODY = {
    'warrior': ((54, 12, 22), (104, 26, 40), (150, 48, 62)),   # crimson-wine
    'mage':    ((36, 18, 58), (66, 36, 100), (100, 66, 142)),  # royal violet
    'ranger':  ((14, 40, 28), (30, 70, 48), (54, 104, 74)),    # bottle-green
}

# One config block per slot. `largest` restricts the diamond field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs field all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_argyle_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary25', largest=True,
    ),
    'legs': dict(
        outdir='_argyle_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary25', largest=False,
    ),
    'boots': dict(
        outdir='_argyle_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_argyle', largest=False,
    ),
    'helmet': dict(
        outdir='_argyledome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary25', largest=True,
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


def draw_argyle(fr, comp, diamond, line):
    """Paint a field of solid diagonal diamonds onto one component. For each opaque pixel,
    compute rotated coords u = dx + dy, v = dx - dy relative to the component bbox top-left.
    The (u, v) plane is tiled into CELL x CELL cells; cells with even parity (cu+cv even) are
    FILLED with the diamond tone, the rest keep the body. A cross-stitch LINE tone is painted
    where u or v is within LINE_W of a cell edge. Only opaque body pixels are ever painted, so
    it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())

    for yy, xx in zip(ys.tolist(), xs.tolist()):
        dx = xx - x0
        dy = yy - y0
        u = dx + dy
        v = dx - dy
        cu = u // CELL
        cv = v // CELL
        # cross-stitch line: near a cell boundary in either rotated axis
        fu = u - cu * CELL
        fv = v - cv * CELL
        on_line = (min(fu, CELL - fu) <= LINE_W) or (min(fv, CELL - fv) <= LINE_W)
        if on_line:
            put(fr, yy, xx, line)
        elif ((cu + cv) & 1) == 0:
            put(fr, yy, xx, diamond)
        # else: leave the recolored body tone (the alternate diamond)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    diamond, line = SEAM[cls]
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
        draw_argyle(fr, comp, diamond, line)
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
                print('wrote %-54s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
