#!/usr/bin/env python3
"""FORTY-FOURTH net-new-geometry axis for ALL FOUR SLOTS — the ZIGZAG / DANCETTE family
(the Norman "chevron molding"): an all-over field of nested, raised convex V-ridges that fold the
surface into a stack of chevrons — the classic zigzag/dancette running across Romanesque arch
voussoirs, doorway orders and font rims. This is the ANGULAR member of the linear-ridge family and
sits naturally beside its straight and curved siblings:

    11th FLUTING   — straight vertical CONCAVE grooves (incised, dead-straight)
    43rd GADROON   — straight vertical CONVEX reeds   (raised, dead-straight)
    42nd STRIGIL   — curved vertical CONCAVE S-flutes  (incised, sine-bowed)
    44th ZIGZAG    — folded horizontal CONVEX V-ridges (raised, triangle-folded)  <-- this

Where gadroon raises DEAD-STRAIGHT vertical rods and strigil BOWS its flutes into a smooth sine S,
the zigzag FOLDS its raised ridge into a hard triangular chevron: each ridge runs as a horizontal
band whose centre-line is deflected up and down by a TRIANGLE wave of the column, so the band bends
into a crisp V and — stacked band over band — reads as a field of nested chevrons. Triangle (not
sine) is the whole point: the arms are DEAD-STRAIGHT diagonals meeting at a sharp point, an angular
zigzag, never a smooth curve.

Geometry: ridge-band pitch PY down, chevron horizontal period PX across, fold amplitude AMP. Per
opaque body pixel in component-local (lx, ly):
    t   = frac(lx / PX)                 # 0..1 across one chevron
    zig = AMP * (2*abs(t - 0.5))        # triangle: 0 at chevron centre, AMP at the shared point
    phase = (ly + zig) / PY             # ridge phase, warped up/down into a V by zig
    u = frac(phase);  c = u - 0.5       # ridge crest at c=0, quirk valley between ridges at c=+/-0.5
The ridge is a folded half-round rod lit from the upper-left, shaded ACROSS the band thickness:
    |c| >= 0.42                 -> QUIRK valley between chevron ridges -> SHADOW (thin sunken line)
    -0.42 <  c <= -0.12         -> upper shoulder facing the light     -> RIM   (brightest catch)
    -0.12 <  c <   0.12         -> folded ridge crest                  -> HILIT (bright top of V)
     0.12 <= c <   0.42         -> lower shoulder falling away         -> MID   (shaded flank)
The repeated motif is a DENSE FIELD OF NESTED RAISED V-CHEVRON RIDGES; none of the forty-three
existing legendary axes per slot occupy it:
  * 11th straight vertical CONCAVE grooves (fluting)   <- zigzag is FOLDED, CONVEX and RAISED
  * 12th continuous straight HORIZONTAL bands (lamellar) <- lamellar bands are STRAIGHT & flat;
        zigzag bands FOLD into sharp V's and carry convex relief
  * 13th round rivet points (studwork)   * 14th diamond outline mesh (lattice)
  * 15th overlapping curved arcs (scale)
  * 16th short alternating-slope diagonal DASHES (twill/herringbone)  <- twill is a broken texture
        of tiny disconnected dashes; zigzag is CONTINUOUS full-length V-ridges with convex relief
  * 17th rectangular outline cells (ashlar)   * 18th woven checker (basketweave)
  * 19th hex cells (honeycomb)   * 20th triangular cells (trellis)
  * 21st circle outlines (chainmail)   * 22nd ONE smooth horizontal SINE ribbon (wave)  <- wave is
        a single smooth curve; zigzag is a whole FIELD of hard ANGULAR triangle-folded ridges
  * 23rd right-angle key-fret (meander)  <- meander turns only 90 degrees into a rectilinear key;
        zigzag turns at an ACUTE point into a diagonal V — angular but not rectilinear
  * 24th coils around a centre (spiral)   * 25th flat solid diamonds (argyle)
  * 26th crossed bands + node (tartan)   * 27th straight rays from a centre (sunburst)
  * 28th nested closed rings (concentric)   * 29th jagged broken-check color-weave (houndstooth)
  * 30th two strands braided into a rope (cable)   * 31st counter-phase ribs -> pointed ovals (ogee)
  * 32nd four circular lobes (quatrefoil)   * 33rd eight-point star outline (octagram)
  * 34th nested-arc fans (seigaiha)   * 35th raised four-facet pyramids (facet)
  * 36th convex diamond cushions + buttons (quilt)   * 37th sunken rectangular panels (coffer)
  * 38th raised ovoids + pointed darts (egg-and-dart)   * 39th braided ribbons + eyes (guilloche)
  * 40th raised rectangular teeth from a fillet (dentil)
  * 41st threaded spheres + disk reels (bead-and-reel)
  * 42nd curved CONCAVE S-flutes (strigil)   <- strigil bows with a SINE and INCISES concave
        channels; zigzag folds with a TRIANGLE and RAISES convex ridges (curve-vs-fold AND cut-vs-
        proud both separate them)
  * 43rd straight CONVEX vertical reeds (gadroon)   <- gadroon reeds are DEAD-STRAIGHT and vertical;
        zigzag ridges FOLD into V's and run horizontally (straight-vs-folded separates them, exactly
        as straight fluting vs curved strigil are separated only by their path)
  * 44th (this) a DENSE FIELD OF NESTED RAISED V-CHEVRON RIDGES -> zigzag / dancette.

NOTE this is NOT the old 9th-axis "chevron" chest accent: that was a single FLAT printed V-stripe
across one slot (flagged for 3/4 rework). This axis 44 is a full-field RAISED convex CHEVRON RELIEF
covering all four slots — a different thing entirely (flat stripe vs modelled zigzag relief field).
Its stem is `zigzag` precisely to avoid the old chevron files.

Per slot it lands as the 44th distinct axis:
  * CHEST  — zigzag cuirass: nested convex V-ridges folded down the whole breastplate.
  * LEGS   — zigzag chausses: nested convex V-ridges folded down the thighs.
  * BOOTS  — zigzag sabatons: nested convex V-ridges folded over the boot.
  * HELMET — zigzag dome: nested convex V-ridges folded over the whole crown.

Authoring philosophy identical to gen_gadroon_axis43.py / gen_strigil_axis42.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside
the existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no net. Shading applied here via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set the zigzag family is STORM-FORGED steel with its OWN quintet
(NOT the gilt-gold of 43 gadroon, nor the burnished copper/steel-blue/jade of 42 strigil, nor the
cast-bronze cornice of 37-41):
  * warrior — storm-forged gunmetal & silver (dark-gunmetal / slate / steel / bright-steel / white)
  * mage    — arcane cobalt (deep-navy / indigo / cobalt / sky-blue / white)
  * ranger  — storm verdigris (dark-iron-green / pine / verdigris / pale-jade / pale-mint)

Run from repo root:
  python3 scripts/gen_zigzag_axis44.py
Then QA (examples):
  python3 scripts/sprite_qa.py _zigzag_legendary_preview/shirt_warrior_legendary44.png
  python3 scripts/sprite_qa.py _zigzagdome_helmet_preview/helmet_mage_legendary44.png --y-min 2
  python3 scripts/sprite_qa.py _zigzag_boots_preview/boots_warrior_legendary_zigzag.png --y-max 63
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

# Zigzag geometry. Tuned so the nested V-chevrons read on a ~14px torso: a chevron horizontal
# period PX across (about two V's on a torso), ridge-band pitch PY down (several nested bands),
# and a fold amplitude AMP giving a clean ~33deg diagonal arm. The signature is a FIELD OF NESTED
# RAISED V-CHEVRON RIDGES.
PX = 6.0         # chevron horizontal period across (local px) -> ~two V's across a torso
PY = 4.0         # ridge-band pitch down (local px) -> several nested bands
AMP = 2.0        # triangle fold amplitude -> diagonal arms of the V


# Per-class zigzag tone quintet, light from upper-left:
#   (GROUND unused off-net fallback, SHADOW quirk valley between ridges, MID lower falling shoulder,
#    HILIT folded ridge crest, RIM bright upper shoulder catch).
ZIGZAG = {
    'warrior': ((26, 28, 34), (70, 74, 86), (126, 132, 150), (196, 202, 220), (246, 248, 255)),  # storm-forged steel
    'mage':    ((18, 20, 50), (48, 54, 116), (92, 106, 190), (160, 180, 240), (236, 242, 255)),  # arcane cobalt
    'ranger':  ((14, 32, 28), (40, 72, 58), (84, 130, 106), (152, 204, 176), (230, 250, 240)),   # storm verdigris
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only): (deep shadow /
# base / highlight).
BODY = {
    'warrior': ((30, 32, 40), (64, 68, 82), (104, 110, 130)),   # dark storm steel
    'mage':    ((20, 22, 50), (46, 52, 104), (84, 96, 160)),    # dark cobalt cloth
    'ranger':  ((14, 32, 28), (38, 70, 56), (72, 116, 94)),     # dark verdigris cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_zigzag_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary44', largest=True,
    ),
    'legs': dict(
        outdir='_zigzag_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary44', largest=False,
    ),
    'boots': dict(
        outdir='_zigzag_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_zigzag', largest=False,
    ),
    'helmet': dict(
        outdir='_zigzagdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary44', largest=True,
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


def draw_zigzag(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the nested V-chevron ridge field onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left:
        t     = frac(lx / PX)              # 0..1 across one chevron
        zig   = AMP * (2*|t - 0.5|)        # triangle fold: 0 at centre, AMP at the shared point
        phase = (ly + zig) / PY            # ridge phase warped up/down into a V
        u = frac(phase);  c = u - 0.5      # crest at c=0, quirk valley at c=+/-0.5
    Under an upper-left light, shaded ACROSS the band thickness:
      * QUIRK valley (|c| >= 0.42)          -> thin sunken line between chevron ridges -> SHADOW
      * upper shoulder (-0.42 < c <= -0.12) -> faces the light                         -> RIM
      * ridge crest (-0.12 < c < 0.12)      -> folded top of the V                     -> HILIT
      * lower shoulder (0.12 <= c < 0.42)   -> falls away from the light               -> MID
    Only opaque body pixels are ever painted, so it cannot create strays. Triangle (not sine) makes
    the arms dead-straight diagonals meeting at a sharp point — a hard angular zigzag."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        t = lx / PX
        t = t - math.floor(t)                 # frac -> [0,1)
        zig = AMP * (2.0 * abs(t - 0.5))       # triangle fold
        phase = (ly + zig) / PY
        u = phase - math.floor(phase)          # frac -> [0,1)
        c = u - 0.5
        ac = abs(c)
        if ac >= 0.42:
            put(fr, yy, xx, shadow)            # thin sunken quirk valley between chevron ridges
        elif c <= -0.12:
            put(fr, yy, xx, rim)               # upper shoulder catches the upper-left light
        elif c < 0.12:
            put(fr, yy, xx, hilit)             # folded ridge crest (top of the V)
        else:
            put(fr, yy, xx, mid)               # lower shoulder falls away from the light
    # `ground` reserved for parity of signature with sibling generators; zigzag fills every
    # body pixel with a ridge/quirk tone, so ground is not separately emitted.
    _ = ground


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = ZIGZAG[cls]
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
        draw_zigzag(fr, comp, ground, shadow, mid, hilit, rim)
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
