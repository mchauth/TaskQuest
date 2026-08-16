#!/usr/bin/env python3
"""FORTY-SIXTH net-new-geometry axis for ALL FOUR SLOTS — the CRAQUELURE / KINTSUGI family
(crackle-glaze shard field): an all-over field of IRREGULAR CONVEX GLAZE SHARDS separated by a
branching network of hairline FRACTURES filled with bright metal, in the manner of a crackled
ceramic glaze mended with kintsugi lacquer.

    the cell is  SHARD    (an irregular convex polygon, no two alike, each a slightly domed
                           plate of glaze carrying its OWN kiln-depth tone)
               + FISSURE  (the hairline crack between two shards, filled with bright metal)
               + JUNCTION (where THREE fissures meet at ~120 degrees — never a 4-way crossing)

*** This is the FIRST APERIODIC AXIS IN FORTY-SIX. ***  Every one of the forty-five prior axes is
strictly PERIODIC: one congruent cell stamped on a lattice, so every cell in the field is the same
shape, the same size, and its edges run in the same two or three fixed directions. Craquelure has
NO repeating cell at all — the field is a Voronoi partition of a JITTERED point set, so every shard
is a different polygon with a different area, a different edge count and edges at arbitrary angles,
and its vertices are 3-way Y-junctions rather than the 4-way crossings of a woven or ruled net.
That irregularity IS the ornament: a crackle glaze is legible precisely because it is not regular.

Geometry. Seed points sit on a grid of pitch P=4.5 in component-local coordinates, each displaced by
a deterministic per-cell jitter of up to JIT=1.55 px (hashed from the integer cell index, so a sheet
always regenerates identically and the male and female sheets of an item always match). For an
opaque body pixel at component-local (lx, ly) the nine candidate seeds in the 3x3 block of grid
cells around it are measured, giving the nearest distance d1, the runner-up d2, and the id of the
owning shard. The Voronoi EDGE FIELD is

    e = d2 - d1            # 0 exactly on the boundary between two shards, growing inward

    e <= 0.13              -> FISSURE CORE, metal pooling at the 3-way junctions    -> RIM
    e <= 0.64              -> FISSURE, the crack wall                               -> HILIT
    otherwise              -> SHARD INTERIOR, toned as below                        -> MID/SHADOW/GROUND

Using d2 - d1 rather than a distance-to-line test is what keeps the fissure one pixel wide of its
own accord all the way around every polygon and closes it exactly at the Y-junctions; there is no
edge list to walk and no seam to mis-join.

Shard interior. Each shard is a shallow dome of glaze lit from the upper left (matching every
sibling axis and the LEFT-facing character). With (ox, oy) the offset from the owning seed,
lit = (-ox - oy)/2.3: the up-left half of a shard catches the light, the down-right half falls away.
On top of that each shard is given its OWN kiln depth — a level nudged up or down from the hash of
its cell id — so neighbouring plates sit at visibly different glaze densities, exactly as a real
crackle glaze pools thicker in some cells than others. Finally, a pixel lying within 2.1 of a
fissure on the shaded side is dropped to the deepest tone: the plate edge tips down into the crack,
which is what makes the shards read as separate raised pieces rather than a flat printed net.

    lit > 0.55  -> MID (lit crown of the shard)   |   lit < -0.35 -> GROUND   |   else SHADOW
    hash nudge:  one shard in six is one level lighter, one in six one level darker
    e <= 1.0 and lit < 0  -> GROUND (the plate lip tipping into the fissure)

The repeated motif is AN IRREGULAR FIELD OF CONVEX GLAZE SHARDS DIVIDED BY A BRANCHING HAIRLINE
FRACTURE NET; none of the forty-five existing legendary axes per slot occupy it. The other ruled
"outline net" axes are the ones to separate it from, and the separation is categorical:
  * 14th lattice   — identical congruent DIAMONDS, two fixed edge directions, 4-way crossings
  * 17th ashlar    — identical congruent RECTANGLES, two fixed edge directions, T-joints on a bond
  * 19th honeycomb — identical congruent regular HEXAGONS on one lattice
  * 20th trellis   — identical congruent TRIANGLES, three fixed edge directions
  * 21st chainmail — closed CIRCLES that overlap and interlink; not a partition of the surface
  * 33rd octagram / 32nd quatrefoil — a single stamped star / rosette repeated on a lattice
    ... in every one of those the cell is the SAME cell everywhere and the edges run in two or three
    fixed directions. In craquelure no two shards are congruent, the edge directions are continuous,
    and the vertices are 3-way. It is also NOT any of:
  * 29th houndstooth (a jagged but strictly periodic woven check)
  * 35th facet / 36th quilt (raised regular pyramids / regular diamond cushions)
  * 37th coffer (sunken congruent rectangles with flat bevel walls)
  * 39th guilloche (two ribbons braided over-under — an interlace, not a partition)
  * 45th arcade (a colonnade of identical round-headed niches on piers — architecture, and the most
    rigidly periodic axis in the set)
  * 24th spiral / 28th concentric (curves winding around tiled centres, not cell walls)
  * 46th (this) AN IRREGULAR APERIODIC SHARD PARTITION WITH A METAL-FILLED FRACTURE NET.

Per slot it lands as the 46th distinct axis:
  * CHEST  — craquelure cuirass: the breastplate crazed and mended across the chest.
  * LEGS   — craquelure chausses: the crackle runs down the thighs.
  * BOOTS  — craquelure sabatons: shards wrap the boot.
  * HELMET — craquelure dome: a crazed glaze skull with gold veins over the crown.

Authoring philosophy identical to gen_arcade_axis45.py / gen_zigzag_axis44.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside the
existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a plain body recolor
only — no craquelure.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` — the canonical chain (no-smooth shading with protect=False,
shirt pauldron/gorget/chest-plate separation, helmet black eye+mouth visor with NO full-silhouette
rim, hat brim/crease folds for open headgear). See CONTEXT.md "MANDATORY — the finishing pass".

Palette. The 45th axis broke the metal streak with carved MASONRY; the 46th is the first FIRED
CERAMIC — a dark glaze body veined with a bright precious metal (kintsugi), which is also the first
time the LINE is the bright element and the FIELD is the dark one on an all-over axis, so it cannot
be confused at a glance with the 45th's pale stone or the 43rd's gilt reeds. Each class gets its
own glaze/metal pairing:
  * warrior — tenmoku (iron-black/persimmon glaze) mended in GOLD
  * mage    — aubergine (iron-purple glaze) mended in PLATINUM
  * ranger  — celadon (ash-green glaze) mended in COPPER

Run from repo root:
  python3 scripts/gen_craquelure_axis46.py
  python3 scripts/gen_craquelure_axis46.py --swatch        # motif only, no sheets written
Then QA (examples):
  python3 scripts/sprite_qa.py _craquelure_legendary_preview/shirt_warrior_legendary46.png
  python3 scripts/sprite_qa.py _craqueluredome_helmet_preview/helmet_mage_legendary46.png --y-min 2
  python3 scripts/sprite_qa.py _craquelure_boots_preview/boots_warrior_legendary_craquelure.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# --- Craquelure constants -------------------------------------------------------------------
# P is the mean shard pitch, and it is the ONE constant this axis lives or dies by. TUNING NOTE:
# the sibling axes sit at a cell pitch of 6-9 px (39th guilloche PX8/PY7, 45th arcade PX7/PY9) and
# the first cut here copied that at P=6 — which was wrong for this motif, and wrong for a reason
# worth writing down. A periodic axis only has to show ONE cell for the eye to infer the rest of
# the field; an APERIODIC one has to show SEVERAL, because the whole subject is that no two cells
# are alike. At P=6 a ~13 px torso holds barely two shards, so a single crack ran across an
# otherwise flat plate and it read as a scratch, not a crackle. A sweep at P=6/5/4.5/4/3.5 settled
# on 4.5: three to four shards across the torso, enough that CLOSED irregular cells of visibly
# different size and shape are on screen at once. Below 4 the shards drop under ~4 interior px, the
# per-shard dome shading has nowhere to land, and the field turns to noise.
P = 4.5          # mean shard pitch (component-local px)
JIT = 1.55       # max seed displacement from the grid node — 34% of the pitch. Swept at
#                  1.35/1.55/1.75/1.95: at 1.35 too many bisectors still line up with the base grid
#                  and long dead-straight vein columns show through, which is exactly the periodic
#                  look this axis exists to avoid; past ~1.75 shards start collapsing into slivers
#                  with no interior left to shade. 1.55 breaks the grid without losing cell
#                  coherence.
# d2-d1 grows at up to 2 per pixel stepped perpendicular to a shard boundary, so a threshold of t
# draws a line about t px wide, independent of P. E_VEIN=0.64 is therefore a HAIRLINE — one pixel —
# which is the whole point: a first cut at 1.20 gave a 2-3 px vein that ate more of the field than
# the shards did. The crack must be thinner than the plates it divides.
E_CORE = 0.13    # d2-d1 below this = the bright core of the metal-filled fissure. Because d2-d1
#                  goes to zero over a WIDER area at a 3-way junction than along a straight run,
#                  this tone lands mostly on the Y-junctions — the metal reads as POOLING where
#                  three cracks meet, which is exactly what kintsugi does. Not a second full-width
#                  line down the middle of every vein.
E_VEIN = 0.64    # d2-d1 below this = the fissure (one pixel wide all round)
E_LIP = 1.00     # within this of a fissure, on the shaded side, the plate tips into the crack
LIT_DIV = 2.3    # scales the shard-dome gradient to the mean shard radius
LIT_HI = 0.55    # lit crown of a shard
LIT_LO = -0.35   # shard face turned away from the upper-left light

# Per-class quintet, light from upper-left:
#   (GROUND deepest glaze pool + shaded plate lip, SHADOW glaze body,
#    MID lit crown of the shard, HILIT metal fissure fill, RIM fissure core catch)
# Unlike the sibling axes the two brightest tones belong to the LINE (the kintsugi metal) and the
# three darkest to the FIELD (the glaze) — the inverse of the usual raised-relief reading, which is
# what a mended crackle glaze actually looks like.
CRAQ = {
    # tenmoku iron-black & persimmon glaze, mended in gold
    'warrior': ((26, 14, 12), (66, 34, 24), (116, 62, 40), (214, 164, 62), (255, 232, 158)),
    # aubergine iron-purple glaze, mended in platinum. Held DOWN off pure white on purpose — a
    # first cut at (196,198,216)/(250,252,255) put the vein so close to white that the shards read
    # as light noise instead of a metal net on a dark glaze.
    'mage':    ((22, 14, 34), (58, 36, 82), (104, 70, 138), (170, 174, 200), (228, 232, 246)),
    # celadon ash-green glaze, mended in copper
    'ranger':  ((14, 28, 24), (36, 66, 54), (66, 106, 84), (206, 122, 66), (250, 206, 154)),
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only):
# (deep shadow / base / highlight).
BODY = {
    'warrior': ((26, 14, 12), (72, 38, 26), (124, 70, 44)),   # dark tenmoku
    'mage':    ((22, 14, 34), (60, 36, 82), (100, 66, 130)),  # dark aubergine
    'ranger':  ((14, 28, 24), (38, 68, 56), (70, 110, 88)),   # dark celadon
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_craquelure_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary46', largest=True,
    ),
    'legs': dict(
        outdir='_craquelure_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary46', largest=False,
    ),
    'boots': dict(
        outdir='_craquelure_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_craquelure', largest=False,
    ),
    'helmet': dict(
        outdir='_craqueluredome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary46', largest=True,
    ),
}


# --- the aperiodic seed field ---------------------------------------------------------------
def _hash32(i, j):
    """Deterministic 32-bit integer hash of a grid node. Pure integer arithmetic so the field is
    bit-identical on every machine and every run — a sheet regenerates the same, and the male and
    female sheets of an item crack along the same lines."""
    x = (i * 374761393 + j * 668265263) & 0xFFFFFFFF
    x = ((x ^ (x >> 13)) * 1274126177) & 0xFFFFFFFF
    return (x ^ (x >> 16)) & 0xFFFFFFFF


_SEED_CACHE = {}


def seed(i, j):
    """Jittered seed point of grid node (i, j), plus its hash. Cached — every pixel queries the
    same nine nodes as its neighbours."""
    key = (i, j)
    s = _SEED_CACHE.get(key)
    if s is None:
        h = _hash32(i, j)
        jx = ((h & 0xFF) / 255.0 - 0.5) * 2.0 * JIT
        jy = (((h >> 8) & 0xFF) / 255.0 - 0.5) * 2.0 * JIT
        s = (i * P + jx, j * P + jy, h)
        _SEED_CACHE[key] = s
    return s


def shard_at(lx, ly):
    """Return (d1, d2, ox, oy, h) for the point: distance to the owning seed, distance to the
    runner-up, the offset from the owning seed, and the owning shard's hash. d2 - d1 is the Voronoi
    edge field — zero on a shard boundary — which is what draws the fissure net."""
    gi, gj = int(math.floor(lx / P)), int(math.floor(ly / P))
    d1 = d2 = 1e9
    ox = oy = 0.0
    hh = 0
    for j in range(gj - 1, gj + 2):
        for i in range(gi - 1, gi + 2):
            sx, sy, h = seed(i, j)
            dx, dy = lx - sx, ly - sy
            d = math.hypot(dx, dy)
            if d < d1:
                d2 = d1
                d1, ox, oy, hh = d, dx, dy, h
            elif d < d2:
                d2 = d
    return d1, d2, ox, oy, hh


def tone_at(lx, ly, ground, shadow, mid, hilit, rim):
    """Classify one pixel of the craquelure field. See the module docstring."""
    d1, d2, ox, oy, h = shard_at(lx, ly)
    e = d2 - d1
    if e <= E_CORE:
        return rim                                   # metal fill, brightest catch
    if e <= E_VEIN:
        return hilit                                 # the hairline fissure itself
    lit = (-ox - oy) / LIT_DIV
    if lit > LIT_HI:
        lvl = 2                                      # lit crown of the shard
    elif lit < LIT_LO:
        lvl = 0                                      # face turned from the light
    else:
        lvl = 1
    nudge = h % 6                                    # this shard's own kiln depth
    if nudge == 0:
        lvl = min(2, lvl + 1)
    elif nudge == 1:
        lvl = max(0, lvl - 1)
    if e <= E_LIP and lit < 0.0:
        lvl = 0                                      # plate lip tipping into the crack
    return (ground, shadow, mid)[lvl]


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


def draw_craquelure(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the crackle-glaze shard field onto one component. Component-local coords (lx, ly) are
    anchored at the component bbox top-left. Only opaque body pixels are ever painted, so this
    cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        put(fr, yy, xx, tone_at(xx - x0, yy - y0, ground, shadow, mid, hilit, rim))


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = CRAQ[cls]
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
        draw_craquelure(fr, comp, ground, shadow, mid, hilit, rim)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def swatch(path='_diag_craquelure_swatch.png', w=42, h=28, zoom=12):
    """Render the bare motif on a flat field for all three classes, so the shard partition and the
    fissure net can be judged before any sheet is written. Writes one diagnostic PNG; touches
    nothing else."""
    pad = 3
    tile_w, tile_h = w * zoom, h * zoom
    img = Image.new('RGBA', (tile_w * 3 + pad * 4, tile_h + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        g, s, m, hi, ri = CRAQ[cls]
        a = np.zeros((h, w, 4), dtype=np.uint8)
        for ly in range(h):
            for lx in range(w):
                a[ly, lx, :3] = tone_at(lx, ly, g, s, m, hi, ri)
                a[ly, lx, 3] = 255
        t = Image.fromarray(a).resize((tile_w, tile_h), Image.NEAREST)
        img.paste(t, (pad + k * (tile_w + pad), pad))
    img.save(path)
    print('wrote %s (motif only — no sheets written)' % path)


def main():
    if '--swatch' in sys.argv:
        swatch()
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
