#!/usr/bin/env python3
"""Generate an EIGHTH net-new-geometry BOOTS showcase per class — a HORIZONTAL
BUCKLE-STRAP band clasped across the boot instep, with a bright central square
BUCKLE plate. This brings boots to 8-axis parity with the chest slot and is a NEW
boots AXIS distinct from all seven existing boots geometries:

  * legendary_greave   adds mass ABOVE (tall-narrow shin plate to a knee-cop).
  * legendary_cuff     flares mass to the SIDE at the ankle (wide cavalier fold).
  * legendary_sabaton  adds mass FORWARD at the toe (a poulaine point).
  * legendary_spur     projects mass at the HEEL (a rowel arm).
  * legendary_wing     fans diagonal ankle-WINGS up-and-out.
  * legendary_claw     drops beast-claw TALONS below the sole.
  * legendary_lace     weaves a DIAGONAL X of laces across the shaft.
  * this STRAP lays a single HORIZONTAL band across the instep with a centred
    square buckle — a horizontal surface axis none of the seven touch. It is the
    boots analogue of the chest GIRDLE (horizontal war-belt) and, like it, the
    leg-baldric and the diadem, is a repaint pattern rather than new silhouette.

Authoring philosophy mirrors gen_girdle_legendary.py / gen_lace_boots.py: the
strap is painted ONLY onto pixels that are ALREADY opaque boot pixels (`a`).
Because it never adds a pixel outside the existing silhouette, it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — the
strap is QA-safe purely by construction.

  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = the buckle strap. We label each frame's boot mass into CONNECTED
    COMPONENTS (so a walk/run pose with two separated feet gets its own strap per
    foot, never one band spanning both). For each component we take its bbox, place
    the strap centre-row STRAP_FRAC of the way down, and repaint any body pixel
    within STRAP_HALF rows of that line as a leather band (lit top edge / shadowed
    body), then stamp a bright square BUCKLE with a dark pin-hole at the component
    centre-x. Everything clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no strap — matching the
convention of the other boots accents. Shading applied in-script via shade(); do
NOT run sprite_shade.py again.

Per class (strap/buckle hue distinct so the eighth reads apart from the seven):
  * warrior "Ironclasp Warboots"   — dark-steel boot, black strap, gold buckle
  * mage    "Astral Clasp Striders"— deep-violet boot, slate strap, cyan buckle
  * ranger  "Wildclasp Striders"   — bark-brown boot, dark strap, bronze buckle

Run from repo root:
  python3 scripts/gen_strap_boots.py
Then QA:
  python3 scripts/sprite_qa.py _strap_boots_preview/boots_warrior_legendary_strap.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import shade                # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Strap geometry. Per foot-component of bbox (h x w) we place the strap centre-row
# STRAP_FRAC of the way down the component and repaint body pixels within
# STRAP_HALF rows of it as the leather band. The square BUCKLE spans BUCKLE_HALF
# cols either side of the component centre-x, over the full band height, with a
# single dark pin-hole pixel at its centre. MIN_PX ignores tiny toe/heel specks.
STRAP_FRAC = 0.48
STRAP_HALF = 1.1
BUCKLE_HALF = 1.2
MIN_PX = 8

# -- Per-class palettes: body ramp (D/M/L) + strap ramp (STRAP, EDGE, BUCKLE) -----
# body  : deep shadow / base / highlight
# strap : STRAP (leather body of the band) / EDGE (lit top edge of the band) /
#         BUCKLE (bright metal buckle plate; its centre pin-hole reuses STRAP)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_strap',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),      # dark steel
        strap=((20, 20, 24), (86, 88, 96), (222, 176, 56)),      # black strap, lit edge, gold buckle
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_strap',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),      # deep violet
        strap=((26, 24, 40), (96, 92, 120), (80, 200, 244)),     # slate strap, lit edge, cyan buckle
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_strap',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),        # bark brown
        strap=((28, 20, 12), (92, 70, 44), (198, 138, 58)),      # dark strap, lit edge, bronze buckle
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


def strap_component(fr, comp, pal):
    """Repaint a horizontal buckle strap onto one boot-foot component. comp is a
    boolean mask (frame-sized) of the single component. Body pixels only."""
    STRAP, EDGE, BUCKLE = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cy = y0 + STRAP_FRAC * h          # strap centre-row (fractional)
    cx = 0.5 * (x0 + x1)             # component centre-col
    band_rows = set()
    for y, x in zip(ys, xs):
        if abs(y - cy) <= STRAP_HALF:
            # lit top edge of the band, shadowed leather below
            put(fr, y, x, EDGE if (y - cy) <= -0.2 else STRAP)
            band_rows.add(y)
    # square buckle plate at the component centre, over the band height
    for y in sorted(band_rows):
        for x in range(int(round(cx - BUCKLE_HALF)), int(round(cx + BUCKLE_HALF)) + 1):
            if 0 <= y < FH and 0 <= x < FW and comp[y, x]:
                put(fr, y, x, BUCKLE)
    # single dark pin-hole pixel at the buckle centre
    py = int(round(cy))
    px = int(round(cx))
    if 0 <= py < FH and 0 <= px < FW and comp[py, px]:
        put(fr, py, px, STRAP)


def draw_straps(fr, a, pal):
    lbl, n = ndimage.label(a)
    for i in range(1, n + 1):
        strap_component(fr, lbl == i, pal)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['strap']
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
        draw_straps(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the strap only repaints body
        # pixels so no stray is possible; the guard is a no-op here by construction.
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
    outdir = '_strap_boots_preview'
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
