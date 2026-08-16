#!/usr/bin/env python3
"""FORTY-FIFTH net-new-geometry axis for ALL FOUR SLOTS — the ARCADE / BLIND ARCADING family
(Romanesque wall arcade): an all-over field of ROUND-HEADED RECESSED NICHES, each a semicircular
ARCH ROLL springing from a pair of slender vertical PIER SHAFTS, the whole run tied together by a
continuous IMPOST string-course at the springing line. This is the ARCHITECTURAL FRAME family — the
first axis whose repeating cell is a *structure* (arch + supporting pier + impost) rather than a
ridge, a tile, a boss or a woven band:

    the cell is  ARCH ROLL  (raised semicircular torus, upper half of the bay)
               + PIER SHAFT (raised vertical rod, lower half, at the bay boundaries)
               + IMPOST     (one continuous bright course at the springing line)
               + BAY        (the sunken niche the arch and piers enclose)

Geometry: bay pitch PX=7 across, arcade course pitch PY=9 down. Rather than solve an arc equation
(which degenerates at this scale — see the note on constants below), the NICHE OPENING is authored
as an explicit stepped round-arch profile and everything else is derived from it, so the arch is
guaranteed to close cleanly in whole pixels:

    yy = ly % PY;   dx = (lx % PX) - 3            # yy = row in the course, dx = -3..+3 in the bay
    OPEN(lx, ly)  = False                if yy == 0        # solid wall band between courses
                    |dx| <= 0            if yy == 1        # arch crown        1 px
                    |dx| <= 1            if yy == 2        # arch shoulders    3 px
                    |dx| <= 2            otherwise         # niche / bay       5 px

    open pixel                                   -> sunken NICHE               -> GROUND (deepest)
    closed pixel with an open 4-neighbour = the ARCH RING / JAMB / PIER frame:
        open below AND open to the right -> upper-left corner of the ring      -> RIM
        open below                       -> top of the ring (arch crown/haunch)-> HILIT
        open to the right                -> LEFT jamb, lit face                -> RIM
        open to the left                 -> RIGHT jamb, falling away           -> MID
        open above                       -> SILL under the niche               -> SHADOW
    closed, no open neighbour:
        yy == SPRING and |dx| >= 2       -> IMPOST block on top of the pier    -> HILIT
        otherwise                        -> flat SPANDREL / wall band behind   -> SHADOW

Because the profile steps 1 -> 3 -> 5 px over three rows, the derived frame walks in from the pier
at |dx|=3 to a 3px cap over the crown: a stepped ROUND-HEADED ARCH, unmistakably an arcade rather
than a grid of rectangles. Each pier is SHARED — the |dx|=3 column of one bay abuts the |dx|=-3
column of the next, so a pier is 2px wide, lit on its left column and shaded on its right, and the
arch feet land exactly on it.

Light is upper-left throughout, matching every sibling axis (and the LEFT-facing character). Unlike
most sibling axes this one uses all FIVE tones with distinct jobs — the deepest (GROUND) for the
sunken niche, SHADOW for the flat wall plane behind — so the recess never merges with the wall it
is cut into.

The repeated motif is A COLONNADE OF ROUND-HEADED RECESSED NICHES ON PIERS; none of the
forty-four existing legendary axes per slot occupy it:
  * 11th straight vertical CONCAVE grooves (fluting)   * 43rd straight vertical CONVEX reeds
        (gadroon)  <- both are bare parallel rods/channels running the full height with no arch,
        no impost and no enclosed cell; the arcade shaft is a SHORT pier that STOPS at an impost
        and CARRIES an arch
  * 12th continuous straight horizontal bands (lamellar)   * 40th rectangular teeth hung from a
        fillet (dentil)  <- dentil's fillet is the closest thing here to an impost, but a dentil
        tooth is a plain rectangular block and nothing springs from it; the arcade hangs a
        SEMICIRCULAR ARCH off its course and encloses a niche
  * 13th round rivet points (studwork)   * 14th diamond outline mesh (lattice)
  * 15th overlapping curved ARCS (scale)  <- a scale is a bare one-way arc, imbricated, with no
        pier, no impost and no recessed field; the arcade arch is a MODELLED ROLL standing on
        SHAFTS over a SUNKEN bay
  * 16th short alternating diagonal dashes (twill)   * 17th rectangular outline cells (ashlar)
  * 18th woven checker (basketweave)   * 19th hex cells (honeycomb)
  * 20th triangular cells (trellis)   * 21st circle outlines (chainmail)
  * 22nd one smooth sine ribbon (wave)   * 23rd right-angle key fret (meander)
  * 24th coils around a centre (spiral)   * 25th flat solid diamonds (argyle)
  * 26th crossed bands + node (tartan)   * 27th straight rays from a centre (sunburst)
  * 28th nested closed rings (concentric)   * 29th jagged broken check (houndstooth)
  * 30th two strands braided into a rope (cable)
  * 31st counter-phase ribs pinching into POINTED ovals (ogee)  <- the ogee cell is a lens with a
        CUSPED POINT at top and bottom formed by two identical curved ribs; the arcade cell is a
        SEMICIRCULAR head on STRAIGHT VERTICAL legs, flat-bottomed, with an impost at the join —
        round-vs-pointed and continuous-rib-vs-arch-on-post both separate them
  * 32nd four circular lobes (quatrefoil)   * 33rd eight-point star outline (octagram)
  * 34th nested-arc FANS (seigaiha)  <- seigaiha's arcs open DOWNWARD in nested threes and overlap;
        the arcade arch opens DOWNWARD once, is not nested, and stands on piers
  * 35th raised four-facet pyramids (facet)   * 36th convex diamond cushions (quilt)
  * 37th sunken rectangular panels (coffer)  <- a coffer is a sunken RECTANGLE with four flat bevel
        walls; the arcade niche is a sunken ROUND-HEADED cell framed by a modelled roll and shafts
  * 38th raised ovoids + pointed darts (egg-and-dart)   * 39th braided ribbons + eyes (guilloche)
  * 41st threaded spheres + disk reels (bead-and-reel)   * 42nd curved concave S-flutes (strigil)
  * 44th nested raised V-chevron ridges (zigzag)
  * 45th (this) A COLONNADE OF ROUND-HEADED RECESSED NICHES ON PIERS -> arcade / blind arcading.

Per slot it lands as the 45th distinct axis:
  * CHEST  — arcade cuirass: a wall arcade of niches run across the breastplate.
  * LEGS   — arcade chausses: niches run down the thighs.
  * BOOTS  — arcade sabatons: niches run around the boot.
  * HELMET — arcade dome: a blind arcade run around the crown like a cathedral lantern.

Authoring philosophy identical to gen_zigzag_axis44.py / gen_gadroon_axis43.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside
the existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no arcade.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` — the canonical chain (no-smooth shading with protect=False,
shirt pauldron/gorget/chest-plate separation, helmet black eye+mouth visor with NO full-silhouette
rim, hat brim/crease folds for open headgear). See CONTEXT.md "MANDATORY — the finishing pass".

Where every prior axis reached for a metal, the arcade family is CARVED STONE — it is architecture,
so it gets a MASONRY quintet all of its own (no metal in it anywhere):
  * warrior — rose porphyry & ivory  (dark maroon-stone / oxblood / dusty rose / pale ivory-pink /
              white)
  * mage    — lapis & moonstone      (midnight blue / deep lapis / azure stone / pale moonstone /
              white)
  * ranger  — serpentine & ivory     (deep pine-stone / serpentine / sage stone / pale ivory-green /
              white)

Run from repo root:
  python3 scripts/gen_arcade_axis45.py
Then QA (examples):
  python3 scripts/sprite_qa.py _arcade_legendary_preview/shirt_warrior_legendary45.png
  python3 scripts/sprite_qa.py _arcadedome_helmet_preview/helmet_mage_legendary45.png --y-min 2
  python3 scripts/sprite_qa.py _arcade_boots_preview/boots_warrior_legendary_arcade.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array                       # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# Arcade geometry. Tuned so a whole bay (arch head + shared piers + sunken niche) still reads on a
# ~14px torso: two bays across, about one and a half courses down — the same cell density as the
# 39th guilloche (PX8/PY7) and 38th egg-and-dart (PX7/PY8).
#
# TUNING NOTE (two cuts were thrown away before this one): an arch drawn by thresholding a circle
# does not survive at this scale. PX=5/R=2.3 with a 2px-thick roll filled the entire head and the
# axis degenerated into a plain rectangular grid; PX=6/R=2.9 with a 1px ring gave a rectangle with
# clipped top corners. The opening is only 5px wide, and 5px is the MINIMUM that can show an arch
# at all (a 1-3-5 step). So the profile is authored explicitly and the ring is derived as the
# 4-neighbour boundary of the opening — which cannot half-close or alias.
PX = 7           # bay pitch across (local px): 5px niche + 2px shared pier
PY = 9           # arcade course pitch down (local px)
SPRING = 3       # row within the course where the arch springs (impost block sits here)
# Stepped round-arch profile: half-width of the opening, by row within the course.
# row 0 is a solid wall band; then the head steps 1 -> 3 -> 5 px wide.
PROFILE = {0: -1, 1: 0, 2: 1}       # any other row -> HALF_MAX
HALF_MAX = 2


# Per-class arcade tone quintet, light from upper-left. All five tones carry a distinct job:
#   (GROUND sunken bay + tympanum — deepest, SHADOW flat spandrel wall behind the arcade,
#    MID faces falling away from the light, HILIT arch-roll crown + impost course,
#    RIM up-left faces + lit left column of each shaft).
ARCADE = {
    # rose porphyry & ivory
    'warrior': ((40, 20, 24), (86, 42, 48), (150, 96, 100), (214, 168, 168), (250, 238, 236)),
    # lapis & moonstone
    'mage':    ((16, 20, 46), (40, 52, 108), (86, 108, 176), (162, 190, 234), (240, 246, 255)),
    # serpentine & ivory
    'ranger':  ((16, 32, 26), (44, 76, 60), (96, 138, 112), (168, 206, 180), (240, 250, 240)),
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only): (deep shadow /
# base / highlight).
BODY = {
    'warrior': ((44, 22, 26), (92, 50, 54), (140, 92, 94)),    # dark porphyry
    'mage':    ((18, 22, 48), (44, 56, 108), (82, 102, 160)),  # dark lapis
    'ranger':  ((16, 32, 26), (42, 74, 58), (78, 118, 96)),    # dark serpentine
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_arcade_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary45', largest=True,
    ),
    'legs': dict(
        outdir='_arcade_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary45', largest=False,
    ),
    'boots': dict(
        outdir='_arcade_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_arcade', largest=False,
    ),
    'helmet': dict(
        outdir='_arcadedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary45', largest=True,
    ),
}


def is_open(lx, ly):
    """True where the pixel falls inside a NICHE OPENING of the tiled arcade, in component-local
    coordinates. The stepped round-arch profile (see module docstring) is authored explicitly
    rather than thresholded from a circle, so the head closes in whole pixels: a solid wall band,
    then 1 px, 3 px, 5 px. Evaluated by formula rather than from an array so a neighbour just
    outside the body silhouette still answers correctly."""
    yy = ly % PY
    half = PROFILE.get(yy, HALF_MAX)
    return abs((lx % PX) - 3) <= half


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


def draw_arcade(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the blind-arcade colonnade onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, the pixel is
    classified into one member of the arcade cell — arch roll, sunken tympanum, spandrel wall,
    impost course, pier shaft, or sunken bay — and toned for an upper-left light. See the module
    docstring for the full classification. Only opaque body pixels are ever painted, so this
    cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy_, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy_ - y0
        if is_open(lx, ly):
            put(fr, yy_, xx, ground)                  # sunken niche behind the arcade
            continue
        below = is_open(lx, ly + 1)
        above = is_open(lx, ly - 1)
        right = is_open(lx + 1, ly)
        left = is_open(lx - 1, ly)
        if below or above or right or left:
            # --- the arch ring / jamb / pier: the frame around the opening -------------
            if below and right:
                put(fr, yy_, xx, rim)                 # upper-left corner of the ring
            elif below:
                put(fr, yy_, xx, hilit)               # top of the ring (crown / haunch)
            elif right:
                put(fr, yy_, xx, rim)                 # left jamb, lit face
            elif left:
                put(fr, yy_, xx, mid)                 # right jamb, falling away
            else:
                put(fr, yy_, xx, shadow)              # sill under the niche
        elif (ly % PY) == SPRING and abs((lx % PX) - 3) >= 2:
            put(fr, yy_, xx, hilit)                   # impost block on top of the pier
        else:
            put(fr, yy_, xx, shadow)                  # flat spandrel / wall band behind


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = ARCADE[cls]
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
        draw_arcade(fr, comp, ground, shadow, mid, hilit, rim)
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
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass — never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                Image.fromarray(arr).save(dst)
                print('wrote %-58s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
