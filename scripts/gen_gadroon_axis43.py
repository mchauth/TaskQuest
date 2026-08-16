#!/usr/bin/env python3
"""FORTY-THIRD net-new-geometry axis for ALL FOUR SLOTS — the GADROON / REEDING family:
an all-over field of parallel, DEAD-STRAIGHT vertical CONVEX ROUNDED REEDS — fat half-round rods
standing proud of the plate, separated by a thin sunken quirk line — the classical gadrooning /
reeding that runs down silver hollow-ware, column shafts and furniture legs. This is deliberately
the INVERSE RELIEF of the 11th axis fluting, exactly as the 37th coffer is the inverse relief of
the 35th facet: where fluting CUTS concave grooves INTO the surface (the groove bottom falls to
shadow, the sharp ridge crest between grooves takes the bright rim), gadrooning RAISES convex reeds
OUT of the surface (the rounded reed body is the lit crown; the thin quirk valley between reeds
falls to shadow). Reeds are bright bodies; flutes are dark channels — the surface reads
convex-proud, not incised.

Geometry: reed pitch PX across; per opaque body pixel in component-local (lx, ly),
    u = frac(lx / PX);  c = u - 0.5          # reed centre at c=0, quirk valley at c=+/-0.5
The reed is a half-round rod lit from the upper-left, so left-facing shoulders are brightest, the
crown is bright, the right-facing shoulder falls away, and the thin quirk between reeds is darkest:
    |c| >= 0.42                 -> QUIRK valley between reeds     -> SHADOW (thin sunken line)
    -0.42 <  c <= -0.12         -> left shoulder facing the light -> RIM   (brightest catch)
    -0.12 <  c <   0.12         -> rounded reed crown             -> HILIT (bright top of the rod)
     0.12 <= c <   0.42         -> right shoulder falling away    -> MID   (shaded convex side)
The repeated motif is a DENSE FIELD OF PARALLEL CONVEX VERTICAL REEDS; none of the forty-two
existing legendary axes per slot occupy it:
  * 11th CONCAVE STRAIGHT VERTICAL grooves (fluting)   <- gadroon is the CONVEX INVERSE: fluting
        incises dark channels with bright ridges between; gadroon raises bright rounded rods with
        thin dark quirks between (bodies and gaps swap relief, exactly like coffer<->facet)
  * 12th continuous straight HORIZONTAL bands (lamellar)
  * 13th discrete raised ROUND POINTS on a grid (rivet-stud)
  * 14th crossing straight diagonals -> lozenge outline (lattice)
  * 15th overlapping short curved ARCS (imbricated scale)
  * 16th short alternating-slope diagonal dashes (twill)
  * 17th staggered rectangular OUTLINE cells (ashlar)   * 18th checker of short-thread bundles (basketweave)
  * 19th hex outline cells (honeycomb)   * 20th triangular cells (trellis)
  * 21st circle outlines (chainmail)   * 22nd ONE horizontal sine ribbon (wave)
  * 23rd right-angle key-fret (meander)   * 24th curved coils around a centre (spiral)
  * 25th flat solid diamonds (argyle)   * 26th crossed bands + node (tartan)
  * 27th straight rays from a centre (sunburst)   * 28th nested closed rings (concentric)
  * 29th jagged broken-check color-and-weave (houndstooth)
  * 30th two strands braided over-under into a rope (cable)   <- cable BRAIDS and crosses two
        strands; gadroon reeds run parallel and NEVER cross
  * 31st counter-phase ribs -> pointed ovals (ogee)   * 32nd four circular lobes per node (quatrefoil)
  * 33rd eight-point star outline (octagram)   * 34th nested-arc fans (seigaiha)
  * 35th raised four-facet pyramids (facet)   * 36th convex diamond cushions + buttons (quilt)
  * 37th sunken rectangular panels (coffer)   * 38th raised ovoids + pointed darts (egg-and-dart)
  * 39th two braided ribbons enclosing eyes (guilloche)
  * 40th broken row of raised rectangular teeth from a fillet (dentil)
  * 41st threaded string of round spheres + thin disk reels (bead-and-reel)
  * 42nd dense field of parallel CURVED S-flutes (strigil)   <- strigil flutes are CURVED and
        CONCAVE (incised); gadroon reeds are STRAIGHT and CONVEX (raised) — curved-vs-straight AND
        cut-vs-proud both separate them
  * 43rd (this) a DENSE FIELD OF PARALLEL CONVEX VERTICAL REEDS -> gadroon / reeding.

Critically distinct from every prior axis. Most important separations:
  - NOT the 11th fluting: gadroon is its INVERSE RELIEF (raised convex rods with dark quirks
    between, vs incised concave channels with bright ridges between) — the same raised<->sunken
    inversion the 37th coffer applies to the 35th facet.
  - NOT the 42nd strigil: strigil flutes BOW into a curved S and are incised concave channels;
    gadroon reeds are dead-straight vertical and raised convex — both curvature and relief differ.
  - NOT the 41st bead-and-reel: bead-and-reel threads discrete spheres + disks along HORIZONTAL
    courses; gadroon reeds are continuous full-height vertical rods with no beads.
  - NOT the 30th cable: cable braids two strands over-under; gadroon reeds run parallel, never cross.
The dense field of parallel convex vertical reeds is the defining, previously-unused geometry.

Per slot it lands as the 43rd distinct axis:
  * CHEST  — gadroon cuirass: convex reeds raised down the whole breastplate.
  * LEGS   — gadroon chausses: convex reeds raised down the thighs.
  * BOOTS  — gadroon sabatons: convex reeds raised over the boot.
  * HELMET — gadroon dome: convex reeds raised over the whole crown.

Authoring philosophy identical to gen_strigil_axis42.py / gen_beadreel_axis41.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside
the existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no net. Shading applied here via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set the gadroon family is BRIGHT GADROONED PRECIOUS-METAL with its
own metal quintet (NOT the burnished polished-metal of 42, nor the cast-bronze cornice of 37-41):
  * warrior — gilt gold gadroon (dark-bronze ground / amber shadow / gold mid / bright-gold hilit / pale-gold-white rim)
  * mage    — silvered amethyst (deep-violet ground / plum shadow / lilac mid / pale-silver hilit / white rim)
  * ranger  — antique verdant-gold (deep-forest ground / bottle shadow / mossy-gold mid / pale-gold-green hilit / pale-mint rim)

Run from repo root:
  python3 scripts/gen_gadroon_axis43.py
Then QA (examples):
  python3 scripts/sprite_qa.py _gadroon_legendary_preview/shirt_warrior_legendary43.png
  python3 scripts/sprite_qa.py _gadroondome_helmet_preview/helmet_mage_legendary43.png --y-min 2
  python3 scripts/sprite_qa.py _gadroon_boots_preview/boots_warrior_legendary_gadroon.png --y-max 63
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

# Gadroon geometry. Tuned so the raised convex reeds read on a ~14px torso: a reed pitch PX across
# (a touch fatter than the 11th fluting so each rod reads as a plump convex body, not a thin line).
# The signature is a FIELD OF PARALLEL CONVEX VERTICAL REEDS.
PX = 4.5         # reed pitch across (local px) -> a few plump rods across a torso


# Per-class gadroon tone quintet, light from upper-left:
#   (GROUND unused off-net fallback, SHADOW thin quirk valley between reeds, MID right falling
#    shoulder, HILIT rounded reed crown, RIM bright left shoulder catch).
GADROON = {
    'warrior': ((36, 24, 6), (104, 70, 20), (168, 122, 44), (232, 184, 84), (255, 236, 168)),  # gilt gold
    'mage':    ((30, 16, 46), (78, 46, 108), (132, 96, 168), (196, 168, 226), (244, 238, 255)),  # silvered amethyst
    'ranger':  ((12, 34, 20), (40, 78, 44), (94, 138, 66), (168, 206, 108), (226, 248, 200)),  # antique verdant-gold
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only): (deep shadow /
# base / highlight).
BODY = {
    'warrior': ((44, 30, 10), (92, 64, 24), (140, 100, 44)),   # dark gilt cloth
    'mage':    ((28, 16, 42), (60, 40, 88), (104, 76, 140)),   # dark amethyst cloth
    'ranger':  ((14, 36, 20), (40, 74, 42), (76, 118, 66)),    # dark verdant cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_gadroon_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary43', largest=True,
    ),
    'legs': dict(
        outdir='_gadroon_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary43', largest=False,
    ),
    'boots': dict(
        outdir='_gadroon_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_gadroon', largest=False,
    ),
    'helmet': dict(
        outdir='_gadroondome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary43', largest=True,
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


def draw_gadroon(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the gadroon convex-reed field onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left:
        u = frac(lx / PX)            # 0..1 across one reed; reed centre at u=0.5
        c = u - 0.5                  # reed crown at c=0, quirk valley at c=+/-0.5
    Under an upper-left light a pixel is:
      * QUIRK valley (|c| >= 0.42)          -> thin sunken line between reeds -> SHADOW
      * left shoulder (-0.42 < c <= -0.12)  -> faces the light               -> RIM (brightest)
      * reed crown (-0.12 < c < 0.12)       -> rounded top of the rod        -> HILIT
      * right shoulder (0.12 <= c < 0.42)   -> falls away from the light     -> MID
    Only opaque body pixels are ever painted, so it cannot create strays. This is the raised
    convex inverse of the 11th fluting's incised concave channels."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        u = lx / PX
        u = u - math.floor(u)            # frac -> [0,1)
        c = u - 0.5
        ac = abs(c)
        if ac >= 0.42:
            put(fr, yy, xx, shadow)      # thin sunken quirk valley between reeds
        elif c <= -0.12:
            put(fr, yy, xx, rim)         # left shoulder catches the upper-left light
        elif c < 0.12:
            put(fr, yy, xx, hilit)       # rounded reed crown
        else:
            put(fr, yy, xx, mid)         # right shoulder falls away from the light
    # `ground` reserved for parity of signature with sibling generators; gadroon fills every
    # body pixel with a reed/quirk tone, so ground is not separately emitted.
    _ = ground


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = GADROON[cls]
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
        draw_gadroon(fr, comp, ground, shadow, mid, hilit, rim)
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
