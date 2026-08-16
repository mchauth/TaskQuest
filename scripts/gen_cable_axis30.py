#!/usr/bin/env python3
"""THIRTIETH net-new-geometry axis for ALL FOUR SLOTS — the CABLE / ROPE-TWIST / TORSADE
family: an all-over field of TWO intertwining strands that spiral around each other and cross
OVER-UNDER at a regular pitch, the unmistakable twisted-rope / cable-knit / barley-sugar column.
Several parallel cable columns run down the whole body; within each column two rounded strands
travel vertically, each swinging side-to-side in opposite phase so they braid past one another,
with the strand that is momentarily "in front" drawn on top and a dark recessed groove between
and beside the strands. Each strand is tube-shaded (bright crown, mid flank) so it reads as a
raised 3-D rope. The repeated motif is the TWO-STRAND TRAVELLING BRAID (a torsade); none of the
twenty-nine existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> lozenge OUTLINE / diamond MESH (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS -> imbricated scale field
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone / twill
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th tessellation of SIX-sided OUTLINE cells -> honeycomb
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE OUTLINES -> chainmail rings
  * 22nd ONE CONTINUOUS UNDULATING SINE line -> watered-steel ripple
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th CONTINUOUS CURVED COILS winding around a CENTRE point -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE -> sunburst / compass
  * 28th STACKS NESTED CLOSED RINGS at growing radius around a CENTRE -> concentric target
  * 29th INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill -> houndstooth
  * 30th (this) TWO INTERTWINING STRANDS braiding OVER-UNDER down a column -> cable / rope.
Critically distinct from the 22nd wave (a SINGLE sine ribbon that only undulates — a cable is
TWO strands that actually cross over and under one another). Distinct from the 24th spiral (one
coil winding AROUND a fixed centre point — a cable is a pair of strands TRAVELLING down a
column, twisting about EACH OTHER, not orbiting a point). Distinct from the 21st chainmail
(closed separate rings — cable strands are continuous, never closing). Distinct from the 11th
fluting (straight parallel ribs that never cross — cable ribs braid across one another). The
over-under crossing of two continuous strands is the defining, previously-unused geometry.

Per slot it lands as the 30th distinct axis:
  * CHEST  — cable cuirass: braided rope columns down the whole cuirass.
  * LEGS   — cable chausses: braided rope columns down the thighs.
  * BOOTS  — cable sabatons: braided rope columns over the boot.
  * HELMET — cable dome: braided rope columns over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the
component bbox top-left:
    col_x   = ((lx mod COLW) - (COLW-1)/2)      # signed x within the cable column
    phase   = 2*pi*ly / PITCH                   # position along the twist
    xa      =  AMP*sin(phase)                    # strand A centre (swings +/-)
    xb      = -AMP*sin(phase)                    # strand B centre (opposite phase)
    a_front = cos(phase) >= 0                    # which strand is momentarily in front
    da,db   = |col_x-xa|, |col_x-xb|             # distance to each strand centre
  If the pixel is within strand radius R of a strand it is painted with that strand's tube tone
  (bright crown when very near the centreline, mid flank otherwise); when it is within R of BOTH
  strands the a_front flag decides which is drawn on top; pixels near no strand get the dark
  groove tone.  Anchoring to the component bbox keeps the twist stable frame-to-frame.

Authoring philosophy is identical to gen_houndstooth_axis29.py / gen_concentric_axis28.py: every
rope pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never
adds a pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed,
or accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60, lying
down) get a plain body recolor only — no rope. Shading applied in this script via shade(); do
NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 24th spiral (verdigris volute) and the 29th
houndstooth (flat two-tone cloth) the cable family is a lustrous braided METAL rope — a twisted
torc / barley-sugar column of precious metal.  The metal distinguishes class:
  * warrior — molten-gold rope (umber groove / bronze flank / bright-gold crown)
  * mage    — moonsilver-violet rope (deep-violet groove / silver flank / white-silver crown)
  * ranger  — verdigris-copper rope (forest groove / copper flank / pale-gold crown)

Run from repo root:
  python3 scripts/gen_cable_axis30.py
Then QA (examples):
  python3 scripts/sprite_qa.py _cable_legendary_preview/shirt_warrior_legendary30.png
  python3 scripts/sprite_qa.py _cabledome_helmet_preview/helmet_mage_legendary30.png --y-min 2
  python3 scripts/sprite_qa.py _cable_boots_preview/boots_warrior_legendary_cable.png --y-max 63
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

# Cable / rope-twist geometry constants.  Tuned high-frequency so the two-strand braid reads
# on a ~14px torso: narrow columns (more repeats), thin strands so the dark groove between and
# around them stays visible, short pitch so a full over-under twist fits in a few rows.
COLW = 5          # width of one cable column (px)
PITCH = 6         # vertical twist pitch (px per full swing)
AMP = 1.15        # strand swing amplitude within the column
R = 1.25          # strand tube radius (thin -> groove stays open)
CROWN = 0.55      # within this fraction of R -> bright crown tone

# Per-class rope tone triple: (GROOVE dark recess, FLANK strand mid, CROWN strand highlight).
ROPE = {
    'warrior': ((30, 22, 8), (156, 112, 40), (252, 216, 104)),    # deep umber / bronze / bright gold
    'mage':    ((32, 24, 58), (146, 146, 178), (246, 244, 255)),  # deep violet / silver / white-silver
    'ranger':  ((18, 34, 22), (156, 98, 52), (240, 214, 132)),    # deep forest / copper / pale gold
}

# Per-class body tones for pixels OUTSIDE the roped component (e.g. raised arms) — a plain
# mid recolor so those pixels still read as the same garment. (deep shadow / base / highlight)
BODY = {
    'warrior': ((78, 60, 26), (128, 100, 46), (182, 150, 78)),
    'mage':    ((70, 66, 96), (116, 114, 140), (170, 168, 194)),
    'ranger':  ((52, 66, 44), (100, 116, 84), (150, 168, 132)),
}

# One config block per slot. `largest` restricts the roped field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs rope all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_cable_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary30', largest=True,
    ),
    'legs': dict(
        outdir='_cable_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary30', largest=False,
    ),
    'boots': dict(
        outdir='_cable_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_cable', largest=False,
    ),
    'helmet': dict(
        outdir='_cabledome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary30', largest=True,
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


def draw_cable(fr, comp, groove, flank, crown):
    """Paint the two-strand cable / rope-twist onto one component. For each opaque body pixel,
    in component-local coords (lx, ly) anchored at the component bbox top-left, two strands
    swing in opposite phase down each COLW-wide column and cross over-under at PITCH; the pixel
    takes the tube tone of whichever strand it lies within (bright crown near the centreline,
    mid flank otherwise), the front strand winning overlaps, else the dark groove tone. Only
    opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    half = (COLW - 1) / 2.0
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        col_x = (lx % COLW) - half
        phase = 2.0 * math.pi * ly / PITCH
        s = math.sin(phase)
        xa = AMP * s
        xb = -AMP * s
        a_front = math.cos(phase) >= 0.0
        da = abs(col_x - xa)
        db = abs(col_x - xb)
        in_a = da <= R
        in_b = db <= R
        if in_a and in_b:
            d = da if a_front else db
        elif in_a:
            d = da
        elif in_b:
            d = db
        else:
            put(fr, yy, xx, groove)
            continue
        put(fr, yy, xx, crown if d <= R * CROWN else flank)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    groove, flank, crown = ROPE[cls]
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
        draw_cable(fr, comp, groove, flank, crown)
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
                print('wrote %-56s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
