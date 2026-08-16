#!/usr/bin/env python3
"""Generate a SECOND NET-NEW-GEOMETRY BOOTS silhouette per class — a low, WIDE
folded-cuff CAVALIER BOOT: a turned-down cuff that flares HORIZONTALLY OUTWARD
at the top of the boot (the ankle/lower-shin), well beyond the leg's own width.

Why this is a NEW silhouette (distinct from BOTH existing boots geometries):
  * Tier boots + the staged legendary Sabatons/comet-striders/talon-striders are
    a low ANKLE shoe (y~56-63) with, at most, tiny ankle-wing tabs.
  * The already-staged "greave boots" are a TALL, NARROW shin plate that climbs
    UPWARD ~9 rows to a knee-cop — a vertical profile.
  * This cuff boot is the deliberate OPPOSITE read: SHORT and WIDE. It does not
    climb the leg; instead a folded cuff band juts OUTWARD sideways by up to
    CUFF_OUT px on each side across the top CUFF_H rows of the boot, giving a
    low, bell-mouthed cavalier/musketeer flare. Tall-narrow (greave) vs
    low-wide (cuff) is the same silhouette contrast the legs showcase draws
    between stiff-plate faulds and soft war-kilt, and the helmets draw between
    the straight-up crest and the wide-out wing-helm.

Authoring philosophy is identical to gen_greave_boots.py / gen_warkilt_legs.py:
  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the folded cuff. For each of the top CUFF_H rows of the boot we take
    that row's own leftmost/rightmost boot pixel and extend OUTWARD 1..CUFF_OUT
    px. Every cuff pixel is laid down as a contiguous run starting from the boot
    pixel in ITS OWN row, so each is 4-connected to the body mass by construction
    (QA-safe: no isolated pixels, no accent-caused multi-component frames). Drawn
    ONLY in transparent space — never overpaints the body. The topmost cuff row
    reads as the bright folded lip (TRIM); a thin dark fold line sits beneath it.

Connectivity is further guaranteed with the same per-frame guard as the greave:
any cuff pixel not 4-connected to the body mass is cleared, so accent strays are
0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no cuff — matching the
greave / tasset / kilt / cape convention. Shading applied in-script via shade();
do NOT run sprite_shade.py again.

Per class (hue-distinct from the greave set so the two boots read apart):
  * warrior "Bulwark Warboots"   — gunmetal boot + gold folded cuff
  * mage    "Nightveil Striders" — deep indigo boot + pale-cyan folded cuff
  * ranger  "Pathwarden Boots"   — bark-brown boot + olive/tan folded cuff

Run from repo root:
  python3 scripts/gen_cuff_boots.py
Then QA (the cuff intentionally flares beyond the normal boot footprint):
  python3 scripts/sprite_qa.py _cuff_boots_preview/boots_warrior_legendary_cuff.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import shade               # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Cuff geometry. The folded cuff occupies the top CUFF_H rows of the boot and
# juts OUTWARD by up to CUFF_OUT px on each side of that row's own boot extent.
CUFF_H = 3            # number of boot rows the folded cuff spans (from the top)
CUFF_OUT = 3          # max px the cuff flares outward on EACH side

# ── Per-class palettes: body ramp (D/M/L) + cuff ramp (TRIM, D, M, L) ──────────
# body: deep shadow / base / highlight
# cuff: TRIM (bright folded lip) / D (fold-line shadow) / M (mid) / L (lit fold)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_cuff',
        body=((40, 44, 52), (86, 92, 104), (140, 148, 164)),               # gunmetal
        cuff=((255, 208, 96), (60, 46, 16), (150, 118, 44), (206, 168, 70)),  # gold cuff
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_cuff',
        body=((18, 18, 60), (46, 46, 128), (96, 100, 206)),                # deep indigo
        cuff=((214, 244, 255), (24, 42, 66), (60, 110, 150), (120, 180, 214)),  # pale-cyan cuff
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_cuff',
        body=((36, 26, 16), (78, 56, 32), (128, 96, 56)),                  # bark brown
        cuff=((222, 214, 150), (40, 44, 18), (86, 92, 42), (140, 150, 74)),   # olive/tan cuff
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


def cuff_tone(j, k, is_outer, pal):
    """Pick a folded-cuff tone. pal = (TRIM, D, M, L). j = cuff row index from
    the top (0 = topmost/folded lip). k = px out from the leg (1..CUFF_OUT).
    Top row = bright folded lip; the row beneath it reads as the dark fold line;
    outermost px darker for a rounded bell edge."""
    TRIM, D, M, L = pal
    if j == 0:
        return TRIM                       # bright folded lip along the very top
    if j == 1:
        return D                          # dark fold-line crease under the lip
    if is_outer:
        return D                          # rounded shadow at the outer edge
    return L if (k % 2 == 0) else M


def draw_cuff(fr, a, pal):
    """Low, wide folded cuff flaring outward across the top CUFF_H boot rows."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return
    y0 = int(rows.min())                  # boot overall top row
    for j in range(CUFF_H):
        y = y0 + j
        xs = np.where(a[y])[0]
        if xs.size == 0:
            continue
        xmin, xmax = int(xs.min()), int(xs.max())
        # flare a contiguous run outward from each side of THIS row's boot extent
        for base_x, sgn in ((xmin, -1), (xmax, +1)):
            for k in range(1, CUFF_OUT + 1):
                x = base_x + sgn * k
                if not (0 <= x < FW):
                    break
                if a[y, x] or fr[y, x, 3] > 0:   # never overpaint body/existing
                    continue
                is_outer = (k == CUFF_OUT)
                put(fr, y, x, cuff_tone(j, k, is_outer, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['cuff']
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
        draw_cuff(fr, a, pal)
        # Connectivity guard: drop any cuff pixel not 4-connected to the body
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
    outdir = '_cuff_boots_preview'
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
