#!/usr/bin/env python3
"""Generate a NINTH net-new-geometry LEGS showcase per class — a HORIZONTAL
KNEE-BAND / articulation garter: a single bold band repainted straight across each
leg at knee height, with a bright central boss (the articulation cop). This brings
the legs slot to NINE distinct axes, at parity with the chest slot, and is the
horizontal cross-leg surface axis that none of the eight existing legendary legs
occupy:

  * legendary1 (tassets)     — SHORT paired hip flaps hanging at the outer sides.
  * legendary2 (war-kilt)    — a long smooth cloth drape to a flared HEM.
  * legendary3 (faulds)      — a STIFF full-width tiered plate skirt at the HIP.
  * legendary4 (poleyns)     — round disc bulging OUTWARD at the KNEE (silhouette).
  * legendary5 (cuisses)     — a broad fin flaring OUTWARD at the HIP.
  * legendary6 (loin-guard)  — a NARROW vertical strap on the CENTRELINE.
  * legendary7 (sword-belt)  — a bold DIAGONAL band across the thighs.
  * legendary8 (side-stripe) — two full-height paired VERTICAL bands, outer edge.
  * this KNEE-BAND lays one HORIZONTAL band across each leg at knee height — the
    horizontal-surface axis (the legs analogue of the chest GIRDLE and the boots
    STRAP), orthogonal to the vertical side-stripe and distinct from the diagonal
    sword-belt. The poleyn already lives at the knee but as OUTWARD silhouette; the
    knee-band is a flat repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_strap_boots.py / gen_sidestripe_legs.py,
including the key robustness win: the band is painted ONLY onto pixels that are
ALREADY opaque body pixels (`a`). Because it never adds a pixel outside the
existing silhouette, it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — the band is QA-safe purely by construction.

  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = the knee band. We label each frame's leg mass into CONNECTED
    COMPONENTS (so a walk/run pose with two separated legs gets its own band per
    leg, never one band spanning both). For each component we take its bbox, place
    the band centre-row KNEE_FRAC of the way down, and repaint any body pixel
    within BAND_HALF rows of that line as a metal band (lit top edge / shadowed
    body), then stamp a bright square BOSS with a dark pin at the component
    centre-x. Everything clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no band — matching the
apron / cuisse / kilt / baldric / side-stripe convention. Shading applied in-script
via shade(); do NOT run sprite_shade.py again.

Per class (band hue distinct from EVERY prior legendary legs accent so all nine
read apart):
  * warrior "Warlord's Knee-Guard" — obsidian/steel body + STEEL band, gold boss
  * mage    "Astral Articulation"   — arcane-violet body + SILVER band, sapphire boss
  * ranger  "Warden's Knee-Wrap"    — forest body + TAN-leather band, copper boss

Run from repo root:
  python3 scripts/gen_kneeband_legs.py
Then QA:
  python3 scripts/sprite_qa.py _kneeband_legs_preview/pants_warrior_legendary9.png --y-max 62
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

# Knee-band geometry. Per leg-component of bbox height h we place the band centre-
# row KNEE_FRAC of the way down (0.5 = knee-ish on the standing pose) and repaint
# body pixels within BAND_HALF rows of it. The square BOSS spans BOSS_HALF cols
# either side of the component centre-x, over the band height, with a single dark
# pin pixel at its centre. MIN_PX ignores tiny toe/heel specks.
KNEE_FRAC = 0.52
BAND_HALF = 1.1
BOSS_HALF = 1.2
MIN_PX = 8

# -- Per-class palettes: body ramp (D/M/L) + band ramp (BAND, EDGE, BOSS) ---------
# body : deep shadow / base / highlight
# band : BAND (metal body of the band) / EDGE (lit top edge of the band) /
#        BOSS (bright central articulation cop; its centre pin reuses BAND)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary9',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),      # obsidian -> steel
        band=((30, 32, 40), (120, 126, 142), (232, 190, 70)),    # steel band, lit edge, gold boss
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary9',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),      # arcane violet
        band=((40, 44, 60), (150, 158, 180), (72, 132, 244)),    # silver band, lit edge, sapphire boss
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary9',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),        # forest green
        band=((60, 46, 26), (150, 116, 70), (206, 132, 66)),     # tan leather, lit edge, copper boss
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


def band_component(fr, comp, pal):
    """Repaint a horizontal knee band onto one leg component. comp is a boolean
    mask (frame-sized) of the single component. Body pixels only."""
    BAND, EDGE, BOSS = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cy = y0 + KNEE_FRAC * h          # band centre-row (fractional)
    cx = 0.5 * (x0 + x1)            # component centre-col
    band_rows = set()
    for y, x in zip(ys, xs):
        if abs(y - cy) <= BAND_HALF:
            # lit top edge of the band, shadowed metal below
            put(fr, y, x, EDGE if (y - cy) <= -0.2 else BAND)
            band_rows.add(y)
    # square boss plate at the component centre, over the band height
    for y in sorted(band_rows):
        for x in range(int(round(cx - BOSS_HALF)), int(round(cx + BOSS_HALF)) + 1):
            if 0 <= y < FH and 0 <= x < FW and comp[y, x]:
                put(fr, y, x, BOSS)
    # single dark pin pixel at the boss centre
    py = int(round(cy))
    px = int(round(cx))
    if 0 <= py < FH and 0 <= px < FW and comp[py, px]:
        put(fr, py, px, BAND)


def draw_bands(fr, a, pal):
    lbl, n = ndimage.label(a)
    for i in range(1, n + 1):
        band_component(fr, lbl == i, pal)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['band']
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
        if fi >= 60:                       # sleep: body only
            continue
        draw_bands(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the band only repaints body
        # pixels so no stray is possible; the guard is a no-op here by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_kneeband_legs_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-46s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
