#!/usr/bin/env python3
"""FORTY-SECOND net-new-geometry axis for ALL FOUR SLOTS — the STRIGIL / STRIGILATION family:
an all-over field of densely-packed CURVED vertical FLUTES that sweep down the plate in a shallow
S — the classical strigil ornament carved across Roman sarcophagi and bath-house walls. Where the
11th axis fluting runs its grooves DEAD-STRAIGHT and vertical, the strigil BENDS each flute into a
gentle S-curve (a running-comma sweep), so the surface reads as a raked field of curved gouged
channels rather than parallel straight lines. Each flute is a rounded concave GROOVE: under an
upper-left light the deepest incision falls to SHADOW, the rising right wall catches the HILIT, and
the shared convex RIDGE crest between flutes takes a bright RIM catch. The repeated motif is a DENSE
FIELD OF PARALLEL CURVED S-FLUTES; none of the forty-one existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel grooves (fluting)   <- strigil is the CURVED cousin:
        every flute BOWS into a shallow S as it runs down; fluting flutes are perfectly straight
  * 12th CONTINUOUS STRAIGHT HORIZONTAL bands, no gaps (lamellar)
  * 13th a field of DISCRETE RAISED ROUND POINTS on a 2-D grid (rivet-stud)
  * 14th crossing STRAIGHT DIAGONALS -> lozenge outline (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS (imbricated scale)   <- scale is short one-way arcs stacked
        in rows; strigil is a set of FULL-HEIGHT continuous curved channels running top-to-bottom
  * 16th SHORT alternating-slope diagonal dashes (herringbone / twill)
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells (ashlar)
  * 18th CHECKER of perpendicular short-thread bundles (basketweave)
  * 19th six-sided OUTLINE cells (honeycomb)   * 20th three-sided cells (trellis)
  * 21st single-radius CIRCLE OUTLINES (chainmail)   * 22nd ONE sine ripple as a band (wave)   <-
        wave is a SINGLE horizontal ripple line; strigil is MANY parallel vertical curved grooves
  * 23rd right-angle key-fret (meander)   * 24th curved coils around a centre (spiral)   <- spiral
        winds a closed coil about a point; a strigil flute is an OPEN sweeping channel, not a coil
  * 25th FLAT solid diagonal diamonds (argyle)   * 26th crossed bold bands + node (tartan)
  * 27th straight rays from a centre (sunburst)   * 28th NESTED closed RINGS (concentric)
  * 29th jagged broken-check color-and-weave (houndstooth)
  * 30th two strands twist down a column into a rope (cable)   <- cable BRAIDS two strands
        over-under into a twist; strigil flutes never cross or braid, they run parallel
  * 31st counter-phase ribs -> pointed ovals (ogee)   * 32nd four circular lobes per node (quatrefoil)
  * 33rd eight-pointed star outline (octagram)   * 34th nested-arc fans, half-drop (seigaiha)
  * 35th raised four-facet pyramids (facet)   * 36th convex diamond cushions + buttons (quilt)
  * 37th sunken rectangular panels (coffer)   * 38th alternating raised OVOIDS + pointed DARTS (egg-and-dart)
  * 39th two braided counter-phase ribbons enclosing eyes (guilloche)
  * 40th a BROKEN ROW OF RAISED RECTANGULAR TEETH hung from a fillet (dentil)
  * 41st a THREADED STRING OF ALTERNATING ROUND SPHERES + THIN DISK REELS (bead-and-reel)
  * 42nd (this) a DENSE FIELD OF PARALLEL CURVED S-FLUTES -> strigil / strigillation.

Critically distinct from every prior axis. Most important separations:
  - NOT the 11th fluting: fluting grooves run DEAD-STRAIGHT and vertical; every strigil flute BOWS
    into a shallow S-curve as it descends (phase warped by a sine of the row) — the whole surface
    rakes and sweeps, which is exactly how art historians tell strigils from plain flutes.
  - NOT the 22nd wave: wave is a SINGLE horizontal sine ribbon band; strigil is a WHOLE FIELD of
    many parallel vertical curved grooves filling the plate edge-to-edge.
  - NOT the 15th scale: scale is short one-way overlapping arcs stacked in horizontal rows; a
    strigil flute is one continuous full-height curved channel, not a stack of little arcs.
  - NOT the 30th cable: cable braids two strands over-under into a rope; strigil flutes run parallel
    and never cross or interlace.
The dense field of parallel curved S-flutes is the defining, previously-unused geometry.

Per slot it lands as the 42nd distinct axis:
  * CHEST  — strigil cuirass: curved S-flutes raked down the whole breastplate.
  * LEGS   — strigil chausses: curved S-flutes raked down the thighs.
  * BOOTS  — strigil sabatons: curved S-flutes over the boot.
  * HELMET — strigil dome: curved S-flutes swept over the whole crown.

Authoring philosophy identical to gen_beadreel_axis41.py / gen_dentil_axis40.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside the
existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no net. Shading applied here via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set the strigil family is POLISHED-METAL GOUGED RELIEF with its own
metal quintet (NOT the cast-bronze cornice metals of 37-41):
  * warrior — burnished copper (dark-umber ground / copper shadow / rose-copper mid / bright-copper hilit / pale-gold rim)
  * mage    — burnished steel-blue (slate ground / steel-blue shadow / pale-steel mid / ice-blue hilit / white rim)
  * ranger  — burnished jade-bronze (deep-pine ground / bottle shadow / jade mid / bright-jade hilit / pale-mint rim)

Run from repo root:
  python3 scripts/gen_strigil_axis42.py
Then QA (examples):
  python3 scripts/sprite_qa.py _strigil_legendary_preview/shirt_warrior_legendary42.png
  python3 scripts/sprite_qa.py _strigildome_helmet_preview/helmet_mage_legendary42.png --y-min 2
  python3 scripts/sprite_qa.py _strigil_boots_preview/boots_warrior_legendary_strigil.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# Strigil geometry. Tuned so the raked curved flutes read on a ~14px torso: a dense flute pitch PX
# across, each flute bowed into a shallow S by warping its horizontal phase with a sine of the row
# (amplitude AMP, wavelength LAM down). The signature is a FIELD OF PARALLEL CURVED S-FLUTES.
PX = 4.0         # flute pitch across (local px) -> dense enough to read several flutes on a torso
AMP = 1.7        # S-curve sway of each flute (local px)
LAM = 19.0       # vertical wavelength of the S sway (local px) -> ~one S over a torso/dome


# Per-class strigil tone quintet, light from upper-left:
#   (GROUND unused off-net fallback = deepest incision floor, SHADOW groove bottom, MID left wall +
#    side, HILIT lit right rising wall, RIM bright convex ridge crest between flutes).
STRIGIL = {
    'warrior': ((34, 18, 8), (92, 48, 22), (150, 92, 52), (226, 150, 92), (255, 216, 150)),  # burnished copper
    'mage':    ((18, 24, 40), (52, 70, 104), (104, 132, 172), (166, 202, 240), (232, 244, 255)),  # burnished steel-blue
    'ranger':  ((12, 32, 22), (36, 78, 54), (72, 134, 92), (128, 200, 138), (214, 248, 214)),  # burnished jade-bronze
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only): (deep shadow /
# base / highlight).
BODY = {
    'warrior': ((46, 26, 12), (86, 52, 26), (134, 88, 50)),   # dark copper cloth
    'mage':    ((22, 28, 50), (46, 58, 96), (86, 104, 152)),  # dark steel-blue cloth
    'ranger':  ((14, 38, 26), (36, 74, 52), (68, 122, 86)),   # dark jade cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_strigil_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary42', largest=True,
    ),
    'legs': dict(
        outdir='_strigil_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary42', largest=False,
    ),
    'boots': dict(
        outdir='_strigil_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_strigil', largest=False,
    ),
    'helmet': dict(
        outdir='_strigildome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary42', largest=True,
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


def draw_strigil(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the strigil curved-flute field onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, the flute phase is
    warped by a sine of the row so each flute bows into a shallow S:
        phase = lx + AMP * sin(2*pi*ly / LAM)
        u     = frac(phase / PX)          # 0..1 across one flute; groove bottom at u=0.5
    With c = u - 0.5 (groove bottom at c=0, shared ridge crest at c=+/-0.5) under an upper-left
    light a pixel is:
      * RIDGE crest (|c| >= 0.40)          -> convex crest, bright RIM catch between flutes
      * left wall (-0.40 < c <= -0.12)     -> MID (side away from the light)
      * groove bottom (-0.12 < c < 0.12)   -> SHADOW (the deep gouged incision)
      * right rising wall (0.12 <= c<0.40) -> HILIT (wall that faces up-left into the light)
    Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        phase = lx + AMP * math.sin(2.0 * math.pi * ly / LAM)
        u = phase / PX
        u = u - math.floor(u)            # frac -> [0,1)
        c = u - 0.5
        ac = abs(c)
        if ac >= 0.40:
            put(fr, yy, xx, rim)         # convex ridge crest between flutes
        elif c < -0.12:
            put(fr, yy, xx, mid)         # left wall (shadow-ward side)
        elif c < 0.12:
            put(fr, yy, xx, shadow)      # deep gouged incision (groove bottom)
        else:
            put(fr, yy, xx, hilit)       # right rising wall catches the light
    # `ground` reserved for parity of signature with sibling generators; strigil fills every
    # body pixel with a wall/crest/incision tone, so ground is not separately emitted.
    _ = ground


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = STRIGIL[cls]
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
        draw_strigil(fr, comp, ground, shadow, mid, hilit, rim)
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
