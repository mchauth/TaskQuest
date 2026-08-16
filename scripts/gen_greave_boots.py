#!/usr/bin/env python3
"""Generate a NET-NEW-GEOMETRY BOOTS silhouette per class — tall plated GREAVES
that rise up the SHIN from the top of the boot and flare into a knee-cop cuff.

Why this is a NEW silhouette (not a recolor, not a repeat):
  * Every existing boot (tier boots + the staged legendary "Sabatons /
    comet-striders / talon-striders" from the legs sets) is an ANKLE-LEVEL
    footprint occupying only y~56-63: a low shoe with, at most, a couple of tiny
    ankle-wing tabs beside the heel (~2 rows).
  * The greave is a CONTINUOUS armored shin plate that grows UPWARD out of the
    boot top for ~9 rows to about mid-shin and flares outward into a knee-cop at
    the very top — a tall vertical profile clearly distinct from the low ankle
    shoe, and (unlike the war-kilt) it is anchored to the FOOT and climbs the
    leg rather than draping from the hip.

Authoring philosophy is identical to gen_warkilt_legs.py / gen_cape_legendary.py:
  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose/animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = a shin plate rising above each SHIN column of the boot. "Shin
    columns" are the columns whose own topmost boot pixel sits at (or 1 below)
    the boot's overall top row — i.e. the back-of-leg columns, NOT the forward
    toe. Each plate column stacks directly above that column's top boot pixel and
    grows contiguously upward, so every accent pixel is 4-connected to the body
    mass by construction (QA-safe: no isolated pixels, no accent-caused
    multi-component frames). Drawn ONLY in transparent space — never overpaints
    the body. A flared knee-cop widens the plate outward by 1px on each side for
    the top two rows; those cuff pixels are adjacent to the plate below them, so
    they stay connected.

Connectivity is further guaranteed with the same per-frame guard as the war-kilt:
any greave pixel not 4-connected to the body mass is cleared, so accent strays
are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no greave — matching the
tasset / kilt / cape / hat convention. Shading applied in-script via shade(); do
NOT run sprite_shade.py again.

Per class (metal/leather distinct in HUE, silhouette is the headline):
  * warrior "Ironwrought Greaves" — obsidian/steel boot + steel plate, gold-rivet cuff
  * mage    "Voidstep Greaves"    — arcane-violet boot + midnight plate, silver-star cuff
  * ranger  "Thornstride Greaves" — forest boot + umber leather plate, tan-bronze cuff

Run from repo root:
  python3 scripts/gen_greave_boots.py
Then QA (accents intentionally rise above the normal boot zone -> bleed OK):
  python3 scripts/sprite_qa.py _greave_boots_preview/boots_warrior_legendary_greave.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Greave geometry. The plate rises RISE rows above each shin column's top boot
# pixel. Y_TOP_MIN clamps the highest row so the plate stops at mid-shin and
# never intrudes into the torso/chest zone. CUFF_ROWS at the very top flare
# outward by 1px per side (the knee-cop).
RISE = 9              # rows the shin plate climbs above the boot top
Y_TOP_MIN = 46        # never draw a greave pixel above this row (mid-shin cap)
CUFF_ROWS = 2         # topmost plate rows that flare outward into a knee-cop
SHIN_TOP_BAND = 1     # a column is a "shin" column if its top boot pixel is
                      # within this many rows of the boot's overall top row

# ── Per-class palettes: body ramp (D/M/L) + greave ramp (TRIM, D, M, L) ────────
# body:   deep shadow / base / highlight
# greave: TRIM (bright rivet/cuff edge) / D (plate shadow) / M (mid plate) / L (lit plate)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_greave',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),              # obsidian->steel
        greave=((255, 205, 90), (58, 62, 74), (110, 116, 132), (176, 184, 204)),  # steel plate, gold-rivet cuff
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_greave',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),              # arcane violet
        greave=((222, 232, 255), (14, 16, 46), (34, 40, 100), (78, 92, 184)),     # midnight plate, silver-star cuff
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_greave',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                # forest green
        greave=((214, 196, 150), (44, 30, 18), (86, 60, 34), (128, 96, 52)),      # umber leather, tan-bronze cuff
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    """Quantized 3-tone recolor of the legendary silhouette (per-frame)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def greave_tone(k, rise, is_edge, pal):
    """Pick a plate tone. pal = (TRIM, D, M, L). k = rows above the boot top
    (1..rise). The top CUFF_ROWS read as the bright knee-cop TRIM; edge columns
    take the plate shadow D so the plate reads as rounded metal."""
    TRIM, D, M, L = pal
    if k > rise - CUFF_ROWS:
        return TRIM                       # bright knee-cop at the top
    if is_edge:
        return D                          # rounded plate shadow on the sides
    # a soft vertical highlight stripe up the plate centre
    return L if (k % 3 == 0) else M


def draw_greave(fr, a, pal):
    """Tall shin plate rising out of each shin column of the boot, flared cuff."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return
    y0 = int(rows.min())                  # boot overall top row
    # per-column top boot pixel
    top_y = {}
    for x in range(FW):
        ys = np.where(a[:, x])[0]
        if ys.size:
            top_y[x] = int(ys.min())
    # shin columns = those whose top boot pixel sits in the top band (back of leg)
    shin = sorted(x for x, ty in top_y.items() if ty <= y0 + SHIN_TOP_BAND)
    if not shin:
        return
    xmin, xmax = shin[0], shin[-1]
    for x in shin:
        ty = top_y[x]
        for k in range(1, RISE + 1):
            y = ty - k
            if y < Y_TOP_MIN:
                break
            if not (0 <= y < FH and 0 <= x < FW):
                continue
            if a[y, x]:                   # never overpaint the body
                continue
            is_edge = (x == xmin or x == xmax)
            put(fr, y, x, greave_tone(k, RISE, is_edge, pal))
    # Flared knee-cop: for the top CUFF_ROWS, extend the plate 1px outward on
    # each side. Anchor each cuff pixel to the plate pixel it sits beside so it
    # stays 4-connected.
    TRIM = pal[0]
    ty_shin = top_y[xmin]                 # representative shin top
    for k in range(RISE - CUFF_ROWS + 1, RISE + 1):
        y = ty_shin - k
        if y < Y_TOP_MIN or not (0 <= y < FH):
            continue
        for x, sgn in ((xmin, -1), (xmax, +1)):
            xx = x + sgn
            if not (0 <= xx < FW):
                continue
            if a[y, xx] or (fr[y, xx, 3] > 0):
                continue
            if fr[y, x, 3] > 0:           # only if the plate pixel beside it exists
                put(fr, y, xx, TRIM)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['greave']
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
        if fi >= 60:                      # sleep: body only
            continue
        draw_greave(fr, a, pal)
        # Connectivity guard: drop any greave pixel not 4-connected to the body
        # mass (only touches stranded accent px, never body px).
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


CHAR = 'sprites/preview_assets/char'
# Some source sheets (e.g. female warrior armor boots) are still staged in a
# preview folder rather than the char dir; search those as a fallback.
FALLBACK_DIRS = ['_fem_warrior_boots_preview']


def load_src(fname):
    p = os.path.join(CHAR, fname)
    if os.path.exists(p):
        return np.array(Image.open(p).convert('RGBA'))
    for d in FALLBACK_DIRS:
        p = os.path.join(d, fname)
        if os.path.exists(p):
            return np.array(Image.open(p).convert('RGBA'))
    raise FileNotFoundError(fname)


def main():
    outdir = '_greave_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_src('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-46s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
