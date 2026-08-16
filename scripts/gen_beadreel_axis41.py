#!/usr/bin/env python3
"""FORTY-FIRST net-new-geometry axis for ALL FOUR SLOTS — the BEAD-AND-REEL / ASTRAGAL family:
an all-over field of horizontal COURSES, each course a string threaded with an alternating rhythm
of round convex spherical BEADS and thin lens-shaped REEL disk-spacers seen edge-on — the
classical astragal bead molding that runs beneath egg-and-dart on cornices, coins and
picture-frames. One course per band pitch PY down; along each course the beads repeat at pitch PX,
each a raised SPHERE of radius RB shaded round under an upper-left light (white-hot crown catch on
the upper-left, lit flank, mid body, dark lower-right terminator), and BETWEEN every pair of beads
a slender REEL — a thin vertical lens/disk spacer (half-width RW, half-height RH) shaded as a small
convex disk (bright top, mid middle, dark bottom). Everything off the string drops to a recessed
GROUND channel. The repeated motif is a STRING OF ALTERNATING ROUND SPHERES + THIN DISK REELS;
none of the forty existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel bands, no gaps (lamellar)
  * 13th a field of DISCRETE RAISED ROUND POINTS on a 2-D grid (rivet-stud)   <- bead-and-reel is a
        CONTINUOUS 1-D STRING of round beads with lens REEL spacers strung between them, not a
        scatter of isolated rivets on an area grid, and each bead is a full relief SPHERE
  * 14th crossing STRAIGHT DIAGONALS -> lozenge outline (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS (imbricated scale)
  * 16th SHORT alternating-slope diagonal dashes (herringbone / twill)
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells, flat (ashlar)
  * 18th CHECKER of perpendicular short-thread bundles (basketweave)
  * 19th six-sided OUTLINE cells (honeycomb)   * 20th three-sided cells (trellis)
  * 21st single-radius CIRCLE OUTLINES (chainmail)   <- bead is a SOLID convex SPHERE, not an open
        ring, and it is strung in a 1-D course with lens spacers, not an interlinked 2-D ring mesh
  * 22nd ONE sine ripple (wave)   * 23rd right-angle key-fret (meander)
  * 24th curved coils around a centre (spiral)   * 25th FLAT solid diagonal diamonds (argyle)
  * 26th crossed bold bands + node (tartan)   * 27th straight rays from a centre (sunburst)
  * 28th NESTED closed RINGS around a centre (concentric)   <- bead is one solid sphere, not a set
        of nested rings; the string alternates sphere/disk rather than growing concentric circles
  * 29th jagged broken-check color-and-weave (houndstooth)
  * 30th two strands twist down a column (cable)   * 31st counter-phase ribs -> pointed ovals (ogee)
  * 32nd four circular lobes per node (quatrefoil)   * 33rd eight-pointed star outline (octagram)
  * 34th nested-arc fans, half-drop (seigaiha)   * 35th raised four-facet pyramids (facet)
  * 36th convex diamond cushions + buttons (quilt)   * 37th sunken rectangular panels (coffer)
  * 38th alternating raised OVOIDS + pointed DARTS (egg-and-dart)   <- egg-and-dart alternates a
        tall OVOID with a POINTED arrowhead dart; bead-and-reel alternates a ROUND sphere with a
        thin ROUND-edged DISK reel — no ovoids, no points, spheres not eggs, disks not darts
  * 39th two braided counter-phase ribbons enclosing a chain of eyes (guilloche)
  * 40th a BROKEN ROW OF RAISED RECTANGULAR TEETH hung from a fillet (dentil)   <- dentil teeth are
        RECTANGULAR blocks; the bead is a ROUND sphere and the reel a ROUND disk — no straight
        block edges, no fillet, a threaded string rather than a hung course
  * 41st (this) a STRING OF ALTERNATING ROUND SPHERES + THIN DISK REELS -> bead-and-reel / astragal.

Critically distinct from every prior axis. Most important separations:
  - NOT the 38th egg-and-dart: egg-and-dart is a TWO-element band of a raised tall OVOID plus a
    slender POINTED DART lozenge — bead-and-reel is a TWO-element band of a raised ROUND SPHERE
    plus a thin ROUND-edged DISK reel; there are no ovoids, no pointed darts, only spheres and disks.
  - NOT the 13th studwork: studwork scatters isolated round rivets across a 2-D area grid — the
    bead-and-reel beads are strung in a CONTINUOUS 1-D course, each a full relief sphere, with lens
    reel spacers threaded between consecutive beads.
  - NOT the 21st chainmail / 28th concentric: those are OPEN rings (single or nested) — the bead is
    a SOLID convex sphere with round relief shading, not an outline ring.
  - NOT the 40th dentil: dentil is a broken row of RECTANGULAR teeth hung from a fillet; the
    bead-and-reel course is a threaded string of ROUND spheres and disks, no straight block edges.
The threaded string of alternating round spheres and thin disk reels is the defining,
previously-unused geometry.

Per slot it lands as the 41st distinct axis:
  * CHEST  — bead-and-reel cuirass: strings of beads + reels banded down the whole breastplate.
  * LEGS   — bead-and-reel chausses: strings of beads + reels banded down the thighs.
  * BOOTS  — bead-and-reel sabatons: strings of beads + reels over the boot.
  * HELMET — bead-and-reel dome: strings of beads + reels over the whole crown.

Authoring philosophy identical to gen_dentil_axis40.py / gen_guilloche_axis39.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel
outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain
body recolor only — no net. Shading applied here via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set the bead-and-reel family is CAST-BRONZE ASTRAGAL RELIEF — a
plate carved with the classical bead molding, a white catch-light on each bead crown. Class differs
by metal/gem (same metals as the cast-bronze cornice family 37/38/39/40):
  * warrior — gilt-bronze beads (dark-bronze ground / bronze shadow / brass mid / bright-gold hilit / white-gold rim)
  * mage    — silvered violet beads (midnight ground / indigo shadow / steel-violet mid / bright-silver hilit / pale-white rim)
  * ranger  — bronzed forest beads (deep-forest ground / bottle shadow / bronze-green mid / bright-emerald hilit / pale-green rim)

Run from repo root:
  python3 scripts/gen_beadreel_axis41.py
Then QA (examples):
  python3 scripts/sprite_qa.py _beadreel_legendary_preview/shirt_warrior_legendary41.png
  python3 scripts/sprite_qa.py _beadreeldome_helmet_preview/helmet_mage_legendary41.png --y-min 2
  python3 scripts/sprite_qa.py _beadreel_boots_preview/boots_warrior_legendary_beadreel.png --y-max 63
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

# Bead-and-reel geometry. Tuned so the astragal reads on a ~14px torso: courses at band pitch PY
# down, along each course round BEADS of radius RB at pitch PX, with a thin REEL disk-spacer
# (half-width RW, half-height RH) at every bead-to-bead boundary. The signature is a threaded
# STRING of alternating round spheres and thin disk reels.
PX = 6.0         # bead pitch across (local px)  -> bead + reel + bead ...
PY = 7.0         # course pitch down (local px)
RB = 2.3         # bead radius (sphere)
BH = 2.8         # course band half-height (|dy_c| beyond this -> ground channel)
RW = 1.0         # reel half-width (thin disk seen edge-on)
RH = 2.5         # reel half-height


# Per-class bead-and-reel tone quintet: (GROUND recessed channel off the string, SHADOW bead
# lower-right terminator + reel bottom, MID bead/reel body, HILIT bead lit upper-left flank + reel
# top, RIM white crown catch on the bead upper-left + reel top edge). Light comes from upper-left.
BEADREEL = {
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
        outdir='_beadreel_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary41', largest=True,
    ),
    'legs': dict(
        outdir='_beadreel_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary41', largest=False,
    ),
    'boots': dict(
        outdir='_beadreel_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_beadreel', largest=False,
    ),
    'helmet': dict(
        outdir='_beadreeldome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary41', largest=True,
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


def draw_beadreel(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the bead-and-reel astragal onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, a course pitch PY
    places a horizontal string centre-line; along it round BEADS of radius RB repeat at pitch PX,
    with a thin REEL disk (half-width RW, half-height RH) at each bead-to-bead boundary. A pixel is:
      * BEAD  (hypot(dx_b, dy_c) <= RB)                 -> raised sphere, round relief under UL light
      * REEL  (|dx_r| <= RW and |dy_c| <= RH)           -> thin convex disk spacer (top hi / bot lo)
      * GROUND (off the string / between courses)       -> recessed channel
    Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        # nearest course centre-line
        jc = round(ly / PY)
        dy_c = ly - jc * PY
        if abs(dy_c) > BH + 0.001:
            put(fr, yy, xx, ground)      # channel between courses
            continue
        # nearest bead centre along the string
        ib = round(lx / PX)
        dx_b = lx - ib * PX
        rr = math.hypot(dx_b, dy_c)
        if rr <= RB + 0.001:
            # raised sphere: round relief, upper-left light
            lit = (-dx_b - dy_c) / RB
            if lit > 0.85:
                put(fr, yy, xx, rim)      # white-hot crown catch (upper-left)
            elif lit > 0.15:
                put(fr, yy, xx, hilit)    # lit upper-left flank
            elif lit > -0.55:
                put(fr, yy, xx, mid)      # sphere body
            else:
                put(fr, yy, xx, shadow)   # lower-right terminator
            continue
        # nearest reel (disk) sits at the half-way boundary between beads
        ir = math.floor(lx / PX) + 0.5
        dx_r = lx - ir * PX
        if abs(dx_r) <= RW + 0.001 and abs(dy_c) <= RH + 0.001:
            # thin convex disk spacer seen edge-on: bright top, mid body, dark bottom
            litr = -dy_c / RH
            if litr > 0.55:
                put(fr, yy, xx, rim)      # top edge catch
            elif litr > -0.1:
                put(fr, yy, xx, hilit)    # upper body
            elif litr > -0.6:
                put(fr, yy, xx, mid)      # mid
            else:
                put(fr, yy, xx, shadow)   # bottom
            continue
        put(fr, yy, xx, ground)          # recessed channel off the string


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = BEADREEL[cls]
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
        draw_beadreel(fr, comp, ground, shadow, mid, hilit, rim)
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
