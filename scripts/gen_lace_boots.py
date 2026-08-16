#!/usr/bin/env python3
"""Generate a SEVENTH net-new-geometry BOOTS showcase per class — a diagonal
CROSS-LACING / strapped-up boot: an X-pattern of criss-crossing laces repainted up
the boot shaft, with bright side EYELETS. This is a NEW boots AXIS distinct from
all six existing boots geometries, every one of which is a SILHOUETTE EXTENSION
adding mass around the foot:

  * legendary_greave   adds mass ABOVE (tall-narrow shin plate to a knee-cop).
  * legendary_cuff     flares mass to the SIDE at the ankle (wide cavalier fold).
  * legendary_sabaton  adds mass FORWARD at the toe (a poulaine point).
  * legendary_spur     projects mass at the HEEL (a rowel arm).
  * legendary_wing     fans diagonal ankle-WINGS up-and-out.
  * legendary_claw     drops beast-claw TALONS below the sole.
  * this LACING adds NO silhouette pixels at all — it is a woven X of laces
    repainted ACROSS the boot surface, the surface-pattern axis none of the six
    touch (parallel to how the girdle became the chest 7th, the leg-baldric the
    legs 7th, and the diadem the helmet 7th — all repaint patterns rather than new
    silhouette).

Authoring philosophy mirrors gen_girdle_legendary.py: the laces are painted ONLY
onto pixels that are ALREADY opaque boot pixels (`a`). Because it never adds a
pixel outside the existing silhouette, it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — the lacing is QA-safe purely by
construction.

  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = the cross-lacing. We label each frame's boot mass into CONNECTED
    COMPONENTS (so a walk/run pose with two separated feet gets its own X per
    foot, never one giant X spanning both). For each component we take its bbox and
    repaint any body pixel lying within LACE_HALF columns of EITHER bbox diagonal
    as a lace strand (the down-right strand lit, the down-left strand shadowed, so
    they read as WOVEN over/under), plus bright EYELETS on the outer edge at a few
    rows. Everything clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no lacing — matching the
convention of the other boots accents. Shading applied in-script via shade(); do
NOT run sprite_shade.py again.

Per class (lace/eyelet hue distinct so the seventh reads apart from the six):
  * warrior "Ironlace Warboots"    — dark-steel boot, pale-iron laces, gold eyelets
  * mage    "Astral Laced Striders"— deep-violet boot, silver laces, cyan eyelets
  * ranger  "Wildlace Striders"    — bark-brown boot, tan rawhide laces, bone eyelets

Run from repo root:
  python3 scripts/gen_lace_boots.py
Then QA:
  python3 scripts/sprite_qa.py _lace_boots_preview/boots_warrior_legendary_lace.png --y-max 63
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

# Lacing geometry. Per foot-component of bbox (h x w) we repaint body pixels whose
# horizontal distance to either bbox diagonal is <= LACE_HALF columns. The band is
# limited to the vertical middle of the component (V_LO..V_HI) so the laces sit on
# the shaft/instep, not the very toe/heel tips. EYELET_VS = the row fractions at
# which the outer-edge pixels are lit as eyelets. MIN_PX = ignore tiny components.
LACE_HALF = 0.9
V_LO, V_HI = 0.10, 0.92
EYELET_VS = (0.28, 0.52, 0.76)
MIN_PX = 8

# -- Per-class palettes: body ramp (D/M/L) + lace ramp (SHADOW, LIT, EYELET) ------
# body : deep shadow / base / highlight
# lace : SHADOW (under-strand, down-left diagonal) / LIT (over-strand, down-right
#        diagonal) / EYELET (bright metal eyelets on the outer edge)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_lace',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),          # dark steel
        lace=((96, 100, 112), (206, 212, 226), (222, 176, 56)),      # pale-iron laces, gold eyelets
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_lace',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),          # deep violet
        lace=((92, 96, 116), (208, 214, 232), (80, 200, 244)),       # silver laces, cyan eyelets
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_lace',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),            # bark brown
        lace=((96, 70, 40), (196, 156, 100), (236, 230, 210)),       # tan rawhide laces, bone eyelets
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


def lace_component(fr, comp, pal):
    """Repaint an X of laces + eyelets onto one boot-foot component. comp is a
    boolean mask (frame-sized) of the single component. Body pixels only."""
    SHADOW, LIT, EYELET = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    w = max(x1 - x0, 1)
    for y, x in zip(ys, xs):
        v = (y - y0) / h
        if not (V_LO <= v <= V_HI):
            continue
        u = (x - x0) / w
        # down-right strand: u == v  ; down-left strand: u == 1 - v
        d_dr = abs(u - v) * w          # horizontal dist (cols) to down-right diag
        d_dl = abs(u - (1.0 - v)) * w  # horizontal dist (cols) to down-left diag
        if min(d_dr, d_dl) <= LACE_HALF:
            put(fr, y, x, LIT if d_dr <= d_dl else SHADOW)
    # eyelets: light the outer-edge body pixel on both sides at a few rows
    for vf in EYELET_VS:
        ry = int(round(y0 + vf * h))
        row = np.where(comp[ry])[0] if 0 <= ry < FH else np.array([], dtype=int)
        if row.size:
            put(fr, ry, int(row.min()), EYELET)
            put(fr, ry, int(row.max()), EYELET)


def draw_lacing(fr, a, pal):
    lbl, n = ndimage.label(a)
    for i in range(1, n + 1):
        lace_component(fr, lbl == i, pal)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['lace']
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
        draw_lacing(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): laces only repaint body pixels
        # so no stray is possible; the guard is a no-op here by construction.
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
    outdir = '_lace_boots_preview'
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
