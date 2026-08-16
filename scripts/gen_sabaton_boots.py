#!/usr/bin/env python3
"""Generate a THIRD NET-NEW-GEOMETRY BOOTS silhouette per class — a pointed
WAR-SABATON whose toe rakes FORWARD into a long tapering poulaine point at the
GROUND, completing the boots showcase to three distinct silhouettes (matching
chest / helmet / legs, which each already have three).

Why this is a NEW silhouette (distinct from BOTH existing boots geometries):
  * The staged "greave boots" add mass ABOVE the boot — a tall, narrow shin plate
    that climbs UPWARD ~9 rows to a knee-cop (a vertical profile, top-anchored).
  * The staged "cuff boots" add mass to the SIDE at the ankle — a folded cavalier
    cuff that flares HORIZONTALLY OUTWARD across the top rows (a low-wide profile,
    ankle/top-anchored).
  * This sabaton adds mass at the BOTTOM — a raked, pointed toe that sweeps
    FORWARD past the foot along the ground, LONGEST at the very bottom row and
    tapering to nothing a few rows up. Up (greave) / out-at-ankle (cuff) /
    forward-at-toe (sabaton) is the same three-way silhouette contrast the legs
    showcase draws (short-flaps / soft-drape / stiff-plate) and the helmets draw
    (up-out horns / straight-up crest / wide-out wing-helm).

Authoring philosophy is identical to gen_cuff_boots.py / gen_greave_boots.py:
  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the raked poulaine toe. For each of the bottom TOE_H rows of the
    boot we take that row's own leftmost/rightmost boot pixel and extend a
    contiguous run OUTWARD along the ground; the run is longest on the very
    bottom row (TOE_MAX) and shortens by TOE_TAPER px per row going up, so the
    toe sweeps to a point at the ground and pulls back in above it. Every toe
    pixel is laid down as a contiguous run starting from the boot pixel in ITS
    OWN row, so each is 4-connected to the body mass by construction (QA-safe:
    no isolated pixels, no accent-caused multi-component frames). Drawn ONLY in
    transparent space — never overpaints the body. The outermost pixel of each
    run is the dark claw-point; the row's inner run alternates lit/mid metal.

Connectivity is further guaranteed with the same per-frame guard as the cuff/
greave: any toe pixel not 4-connected to the body mass is cleared, so accent
strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no toe — matching the
greave / cuff / tasset / kilt / cape convention. Shading applied in-script via
shade(); do NOT run sprite_shade.py again.

Per class (hue-distinct from BOTH the greave and cuff sets so all three boots
read apart):
  * warrior "Dreadclaw Sabatons" — dark-steel boot + pale iron claw-points
  * mage    "Hexbite Striders"   — deep violet boot + amethyst/lilac claw-points
  * ranger  "Beastfang Treads"   — bark-brown boot + bone-white claw-points

Run from repo root:
  python3 scripts/gen_sabaton_boots.py
Then QA (the raked toe intentionally sweeps beyond the normal boot footprint):
  python3 scripts/sprite_qa.py _sabaton_boots_preview/boots_warrior_legendary_sabaton.png --y-max 63
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

# Poulaine-toe geometry. The raked toe occupies the bottom TOE_H rows of the boot
# and sweeps OUTWARD along the ground: longest on the bottom-most row (TOE_MAX px
# per side) and TOE_TAPER px shorter for each row above, so it comes to a point.
TOE_H = 3             # number of boot rows the raked toe spans (from the bottom)
TOE_MAX = 5           # max px the toe rakes forward on EACH side (bottom row)
TOE_TAPER = 2         # px shorter per row going up from the bottom

# ── Per-class palettes: body ramp (D/M/L) + claw ramp (TIP, D, M, L) ───────────
# body: deep shadow / base / highlight
# claw: TIP (dark claw-point) / D (fold/shadow) / M (mid metal) / L (lit metal)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_sabaton',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),                # dark steel
        claw=((28, 30, 38), (86, 92, 104), (170, 178, 194), (222, 228, 240)),  # pale iron claws
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_sabaton',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),                # deep violet
        claw=((30, 16, 46), (78, 46, 118), (158, 116, 210), (214, 186, 246)),  # amethyst/lilac claws
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_sabaton',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),                  # bark brown
        claw=((30, 26, 20), (96, 88, 72), (176, 166, 138), (236, 230, 210)),  # bone-white claws
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


def claw_tone(k, run_len, pal):
    """Pick a raked-toe tone. pal = (TIP, D, M, L). k = px out from the boot
    (1..run_len). The outermost px is the dark claw TIP; the innermost px reads
    as a shadow crease under the boot; the rest alternate lit/mid metal."""
    TIP, D, M, L = pal
    if k == run_len:
        return TIP                        # dark claw-point at the very tip
    if k == 1:
        return D                          # shadow crease where toe meets boot
    return L if (k % 2 == 0) else M


def draw_toe(fr, a, pal):
    """Long forward-raked poulaine toe sweeping outward across the bottom rows."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return
    y1 = int(rows.max())                  # boot overall bottom row (ground)
    for j in range(TOE_H):
        y = y1 - j
        run_len = TOE_MAX - j * TOE_TAPER
        if run_len < 1:
            continue
        xs = np.where(a[y])[0]
        if xs.size == 0:
            continue
        xmin, xmax = int(xs.min()), int(xs.max())
        # rake a contiguous run outward from each side of THIS row's boot extent
        for base_x, sgn in ((xmin, -1), (xmax, +1)):
            for k in range(1, run_len + 1):
                x = base_x + sgn * k
                if not (0 <= x < FW):
                    break
                if a[y, x] or fr[y, x, 3] > 0:   # never overpaint body/existing
                    continue
                put(fr, y, x, claw_tone(k, run_len, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['claw']
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
        draw_toe(fr, a, pal)
        # Connectivity guard: drop any toe pixel not 4-connected to the body
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
    outdir = '_sabaton_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_src('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-50s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
