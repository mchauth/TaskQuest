#!/usr/bin/env python3
"""FORTY-SEVENTH net-new-geometry axis for ALL FOUR SLOTS — the MOKUME / CONTOUR-LAMINATION family
(wood-grain metal): a forged billet of alternating metal LAMINAE, ground back until the layers
surface as a nest of closed CONTOUR BANDS that run PARALLEL TO THE EDGE OF THE PIECE — the ring
figure of Japanese mokume-gane, and the same figure a topographic map draws around a hill.

    the ornament is  LAMINA  (a closed band of one metal, everywhere the same depth below the
                              surface, so its outline is an inward offset of the silhouette)
                   + SEAM    (the 1px step down where the next lamina inward laps under this one)
                   + FIGURE  (the whole nest: bands pinching at a waist, swelling over a pauldron,
                              closing into an island at the thickest part of the piece)

*** THIS IS THE FIRST SHAPE-CONFORMAL AXIS IN FORTY-SEVEN. ***  Every one of the forty-six prior
axes — including the 46th, which broke periodicity — computes its tone from a function of ABSOLUTE
POSITION: `tone = f(lx, ly)`, the pixel's coordinates inside the component bounding box. Whether the
field is a ruled lattice (11th-45th) or a jittered Voronoi partition (46th), the pattern is stamped
onto the piece from outside and the silhouette merely crops it; slide the body one pixel left and a
different part of the wallpaper shows through. Mokume computes its tone from a function of the
DISTANCE TO THE SILHOUETTE: `tone = f(d(x, y))`, where d is the chamfer distance transform of the
component's own opaque mask. The pattern is therefore a property OF THE PIECE, not of the canvas:
every band is an inward offset of the outline, so the figure wraps a boot differently from a
breastplate, flows around the arm gap instead of being cut by it, pinches where the plate necks and
closes into an island at its thickest point. Nothing in the set does that. It is also the reason
the axis cannot be confused with any ring-like predecessor at a glance: a mokume band is not a
circle and not a repeat, it is the shape of the armour piece drawn smaller.

Geometry. For each component, d = chamfer distance from the background (orthogonal step 1.0,
diagonal step sqrt(2), computed by min-plus relaxation — self-contained NumPy, no scipy), so the
outermost body pixel sits at d=1. Band coordinate u = (d - 0.5) / PB with PB = 1.7 px; band index
b = floor(u) counts inward from the rim, t = u - b is the position across the band.

    b % 2 == 0   ->  PALE lamina ramp        (band 0, the rim band, is PALE by design)
    b % 2 == 1   ->  DARK lamina ramp

    (1 - t) * PB <= SEAM_PX   ->  SEAM: the step down to the next lamina inward -> that ramp's LO
    otherwise                 ->  lit by the band's own surface normal, below

The rim band is deliberately the PALE metal. A contour axis puts its outermost band exactly on the
silhouette, and CONTEXT.md's standing rule is that a dark full-silhouette rim swamps a coloured or
patterned dome; running the outer lamina bright turns that unavoidable edge band into a chased
bright outline instead of the failure mode.

Lighting. Because the bands follow the outline, the surface they model is a mound: the outward
normal of the lamina at a pixel is -grad(d), which points out of the silhouette perpendicular to the
band. Under the standard upper-left light,

    lit = (gx + gy) / (sqrt(2) * |grad d|)        lit > 0.30 -> HI | lit < -0.30 -> LO | else MID

so each band is bright along its upper-left arc and falls away along its lower-right arc, all the
way around the nest — the round, hand-ground look of a real mokume billet. Where |grad d| collapses
(the medial axis, the ridge of the mound) the normal is undefined and the pixel takes MID, which is
correct: that is the flat top of the piece.

Palette. First axis built on TWO independent three-tone metal ramps rather than one five-tone
quintet, because the subject is literally two metals forge-welded together; alternating whole ramps
band to band is what makes the laminae read as different MATERIALS rather than as different
brightnesses of one material.
  * warrior — shakudo (blue-black patinated alloy) laminated with FINE SILVER
  * mage    — niello (violet-black) laminated with ROSE GOLD
  * ranger  — kuromido (chocolate-black) laminated with WHITE BRONZE

Distinctness, against the axes it could be mistaken for:
  * 28th concentric — nested closed rings, but they are CIRCLES of fixed radius step stamped around
    tiled centres on a lattice: many identical ring families repeated across the plate, positional.
    Mokume has exactly ONE nest per component, its bands are not circles, and no two are similar.
  * 24th spiral — a single continuous curve winding into tiled centres; mokume bands are closed,
    disjoint, never connected to one another.
  * 21st chainmail — closed circles that overlap and interlink, a lattice of them.
  * 15th scale / 34th seigaiha — arcs and nested fans stamped on a lattice, all identical.
  * 11th fluting / 42nd strigil / 43rd gadroon / 44th zigzag — linear ridges running in a FIXED
    direction (straight, sine-bowed, or triangle-folded); a mokume band changes direction
    continuously and returns to where it started.
  * 46th craquelure — aperiodic, but a PARTITION into cells meeting at 3-way junctions; mokume has
    no cells and no junctions, only disjoint nested loops.
  * 14th lattice / 17th ashlar / 19th honeycomb / 20th trellis / 32nd / 33rd — congruent cells on a
    lattice; the antithesis of a shape-conformal figure.
  * plain "outline + inner outline" — the reason this is an axis and not a rim: the nest is
    3-5 bands deep with alternating METALS and a normal-lit round, and the finishing pass's own
    edge treatment is unaffected.

Per slot it lands as the 47th distinct axis:
  * CHEST  — mokume cuirass: the ring figure closes around the sternum.
  * LEGS   — mokume chausses: bands run down each thigh and pinch at the knee.
  * BOOTS  — mokume sabatons: the figure wraps the foot.
  * HELMET — mokume dome: contour rings crown the skull, bright lamina at the rim.

Authoring philosophy identical to gen_craquelure_axis46.py / gen_arcade_axis45.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside
the existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi >= 60) get a plain body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` — the canonical chain (no-smooth shading with protect=False,
shirt pauldron/gorget/chest-plate separation, helmet black eye+mouth visor with NO full-silhouette
rim, hat brim/crease folds for open headgear). See CONTEXT.md "MANDATORY — the finishing pass".

Run from repo root:
  python3 scripts/gen_mokume_axis47.py
  python3 scripts/gen_mokume_axis47.py --swatch      # bare motif on a test plate, no sheets written
  python3 scripts/gen_mokume_axis47.py --sweep       # PB sweep on a real torso, no sheets written
Then QA (examples):
  python3 scripts/sprite_qa.py _mokume_legendary_preview/shirt_warrior_legendary47.png
  python3 scripts/sprite_qa.py _mokumedome_helmet_preview/helmet_mage_legendary47.png --y-min 2
  python3 scripts/sprite_qa.py _mokume_boots_preview/boots_warrior_legendary_mokume.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# --- Mokume constants -----------------------------------------------------------------------
# PB is the lamina thickness and it is the constant this axis lives or dies by, for a reason that is
# the mirror image of the 46th's tuning note. Craquelure needed a SMALL pitch because an aperiodic
# field has to show SEVERAL cells before the eye accepts that no two are alike. A contour nest has
# the opposite problem: the number of bands is not set by the pitch alone but by the HALF-THICKNESS
# of the piece, because the nest runs from the rim to the medial axis and stops. A ~13px torso is
# ~7px to its medial axis and a 4-5px limb is barely 2, so the pitch has to be chosen against the
# THINNEST part that still has to read, not the widest. Swept at 2.6/2.3/2.0/1.7/1.4 (--sweep):
#   2.6 / 2.3  a 4px limb holds ONE band and the whole leg goes a single flat metal — no lamination
#              anywhere below the torso, and the torso itself gets two bands, i.e. a rim and a fill.
#   2.0        limbs alternate at last, but the torso stops at three bands and the figure still
#              reads as concentric rather than laminated.
#   1.7        limbs show rim + core (2 bands), torso shows 4-5, and the pinch at the waist and the
#              island over the sternum are both legible. Chosen.
#   1.4        the seam eats the band: at 1.4 the SEAM_PX=0.85 step is 60% of the lamina, so every
#              band is mostly its own shadow line and the two metals stop alternating cleanly.
PB = 1.7          # lamina thickness (px) — see sweep above
RIM_D = 1.5       # the RIM band (band 0) is given its own thinner allotment — just the single
#                   outermost ring of body pixels — instead of a full lamina's worth. First cut gave
#                   band 0 the full PB like every other band, and because a contour nest counts
#                   inward from the rim, that put the widest, palest band on the outside of every
#                   piece and the alternation only began two pixels in: thin limbs came out a flat
#                   sheet of one metal and the torso read as "silver plate with a dark inlay" rather
#                   than as a laminate. Pinning the rim to one pixel makes it a chased bright
#                   outline and lets the dark lamina start immediately behind it, so even a 4px limb
#                   shows rim + core in two different metals.
SEAM_PX = 0.85    # a pixel within this of the band's INNER boundary is the step down to the next
#                   lamina. Deliberately on the INNER edge: putting it on the outer edge would lay a
#                   dark line directly along the silhouette, which is the exact failure mode
#                   CONTEXT.md warns about for helmets.
LIT_HI = 0.30     # band arc facing the upper-left light
LIT_LO = -0.30    # band arc turned away from it
GRAD_EPS = 0.12   # below this |grad d| the surface normal is undefined (medial axis) -> MID
EDT_ITERS = 24    # min-plus relaxation passes; propagates distance well past any body half-width
WD = 1.4142135623730951

# Two three-tone metal ramps per class, each (LO, MID, HI). Band 0 (the rim band) takes PALE.
PALE = {
    'warrior': ((118, 124, 134), (184, 190, 200), (244, 247, 252)),   # fine silver
    # Rose gold, pushed PINK rather than peach on purpose. A first cut at
    # (146,84,68)/(214,140,116)/(252,208,188) was a warm tan and, because the female chest is narrow
    # enough that the rim band is most of what you see of it, the whole robe read as BARE SKIN at
    # 1x. Any pale ramp on this axis has to clear the skin palette, because the rim band is the one
    # part of a contour nest that is guaranteed to be visible on every piece however thin.
    'mage':    ((132, 70, 84), (198, 116, 128), (246, 178, 190)),     # rose gold
    'ranger':  ((132, 130, 106), (190, 186, 152), (246, 244, 214)),   # white bronze
}
DARK = {
    'warrior': ((16, 18, 30), (40, 46, 72), (74, 84, 118)),           # shakudo
    'mage':    ((20, 14, 28), (48, 32, 64), (84, 58, 104)),           # niello
    'ranger':  ((22, 16, 12), (54, 38, 26), (92, 66, 44)),            # kuromido
}

# Per-class body (ground) tones for the recolor, visible on sleep frames only:
# (deep shadow / base / highlight), taken off the dark lamina so the billet reads as one object.
BODY = {
    'warrior': ((16, 18, 30), (44, 50, 76), (80, 90, 124)),
    'mage':    ((20, 14, 28), (52, 34, 68), (90, 62, 110)),
    'ranger':  ((22, 16, 12), (58, 40, 28), (98, 70, 48)),
}

# One config block per slot. `largest` restricts the nest to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_mokume_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary47', largest=True,
    ),
    'legs': dict(
        outdir='_mokume_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary47', largest=False,
    ),
    'boots': dict(
        outdir='_mokume_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_mokume', largest=False,
    ),
    'helmet': dict(
        outdir='_mokumedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary47', largest=True,
    ),
}


# --- the shape-conformal field --------------------------------------------------------------
def chamfer(mask, iters=EDT_ITERS):
    """Chamfer distance transform of `mask` (True = inside), measured from the background.
    Orthogonal step 1, diagonal step sqrt(2). Computed by min-plus relaxation so it is a handful of
    whole-array NumPy ops and needs no scipy; `iters` passes resolve every distance up to `iters`
    px, far past any half-width in a 64px sprite. The outermost body pixel comes out at d=1.

    This function is the axis: it is the only place in forty-seven generators where the ornament's
    coordinate is derived from the SHAPE of the piece instead of from the canvas."""
    INF = 1e6
    d = np.where(mask, INF, 0.0)
    for _ in range(iters):
        prev = d
        m = d
        c = np.full_like(d, INF)
        c[1:, :] = np.minimum(c[1:, :], m[:-1, :] + 1.0)          # from above
        c[:-1, :] = np.minimum(c[:-1, :], m[1:, :] + 1.0)         # from below
        c[:, 1:] = np.minimum(c[:, 1:], m[:, :-1] + 1.0)          # from left
        c[:, :-1] = np.minimum(c[:, :-1], m[:, 1:] + 1.0)         # from right
        c[1:, 1:] = np.minimum(c[1:, 1:], m[:-1, :-1] + WD)       # diagonals
        c[1:, :-1] = np.minimum(c[1:, :-1], m[:-1, 1:] + WD)
        c[:-1, 1:] = np.minimum(c[:-1, 1:], m[1:, :-1] + WD)
        c[:-1, :-1] = np.minimum(c[:-1, :-1], m[1:, 1:] + WD)
        d = np.minimum(d, c)
        if np.array_equal(d, prev):
            break
    return d


def band_field(d, mask):
    """From the distance field, the per-pixel (band index, across-band position t, lit) triple.
    `lit` is the dot of the lamina's outward normal -grad(d) with the upper-left light."""
    gy, gx = np.gradient(d)
    mag = np.hypot(gx, gy)
    lit = np.where(mag > GRAD_EPS, (gx + gy) / (WD * np.maximum(mag, 1e-6)), 0.0)
    # Band 0 is the single outermost ring (d <= RIM_D); the laminae proper start behind it.
    u = (d - RIM_D) / PB
    b = np.where(d <= RIM_D, 0, 1 + np.floor(u)).astype(np.int32)
    t = np.where(d <= RIM_D, 0.5, u - np.floor(u))
    b = np.where(mask, np.maximum(b, 0), 0)
    return b, t, lit


def paint_mokume(fr, comp, pale, dark):
    """Paint the contour-lamination nest onto one component. Only opaque body pixels are ever
    painted, so this cannot create strays."""
    if comp.sum() < MIN_PX:
        return
    d = chamfer(comp)
    b, t, lit = band_field(d, comp)
    for y, x in np.argwhere(comp):
        bi = int(b[y, x])
        ramp = pale if (bi % 2 == 0) else dark
        # band 0 is the 1px chased rim: it is never given a seam, or the outline would go dark.
        if bi > 0 and (1.0 - float(t[y, x])) * PB <= SEAM_PX:
            rgb = ramp[0]                          # seam: step down to the next lamina inward
        else:
            lv = float(lit[y, x])
            rgb = ramp[2] if lv > LIT_HI else (ramp[0] if lv < LIT_LO else ramp[1])
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


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


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    pale, dark = PALE[cls], DARK[cls]
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
        paint_mokume(fr, comp, pale, dark)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ----------------------------------------------------------------------------
def _test_plate(w=44, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the
    contour nest can be judged on a shape that has the features real slots have."""
    m = np.zeros((h, w), dtype=bool)
    yy, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    half = 9.0 - 3.2 * np.abs(np.sin((yy[:, 0] / (h - 1.0)) * np.pi * 1.0)) * 0.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False          # neck notch
    return m


def swatch(path='_diag_mokume_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the contour nest and the
    two alternating metals can be judged before any sheet is written."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_mokume(a, m, PALE[cls], DARK[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only — no sheets written)' % path)


def sweep(path='_diag_mokume_sweep.png', zoom=11):
    """Render the warrior chest idle frame at a range of lamina thicknesses, plus a leg frame, so
    the pitch can be judged on the THINNEST part that has to read, not just the torso."""
    global PB
    keep = PB
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    for pb in (2.6, 2.3, 2.0, 1.7, 1.4):
        PB = pb
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comp = (lbl == int(counts.argmax())) if n else a
            fr = np.zeros_like(src)
            paint_mokume(fr, comp, PALE['warrior'], DARK['warrior'])
            col.append(Image.fromarray(fr).crop(crop))
        cells.append(('PB=%.1f' % pb, col))
    PB = keep
    cw, ch = 28 * zoom, 26 * zoom
    pad, lab = 8, 18
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + 2 * (ch + lab)), (24, 24, 28, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
    except Exception:
        f = ImageFont.load_default()
    x = pad
    for name, col in cells:
        y = pad
        for im in col:
            img.alpha_composite(im.resize((cw, ch), Image.NEAREST), (x, y))
            d.text((x + 2, y + ch), name, font=f, fill=(210, 210, 220, 255))
            y += ch + lab
        x += cw + pad
    img.convert('RGB').save(path)
    print('wrote %s (pitch sweep — no sheets written)' % path)


def main():
    if '--swatch' in sys.argv:
        swatch()
        return
    if '--sweep' in sys.argv:
        sweep()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass — never a bespoke shade() in a generator.
                # save_finished() rather than a bare .save(): it writes the TaskQuestFinish
                # version stamp, without which a later bulk `sprite_finish.py <dir>` backfill
                # would run the whole chain over these sheets a SECOND time.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-62s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
