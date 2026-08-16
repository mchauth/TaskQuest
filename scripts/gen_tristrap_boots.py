#!/usr/bin/env python3
"""TENTH net-new-geometry BOOTS showcase per class — a TRIPLE-STRAP shaft: three
stacked horizontal buckle-straps climbing the boot, each with a small square
buckle. This brings the boots slot to TEN distinct axes. It is the multi-band
shaft axis none of the nine existing legendary boots occupy:

  * legendary1 (greave)    — a tall shin plate + knee-cop.
  * legendary2 (cuff)      — one wide folded cavalier cuff at the top.
  * legendary3 (sabaton)   — a forward-raked poulaine toe (silhouette).
  * legendary4 (spur)      — a heel rowel-spur wheel.
  * legendary5 (winged)    — diagonal ankle wings.
  * legendary6 (claw)      — downward beast-claw talons.
  * legendary7 (lace)      — a diagonal cross-lacing X on the instep.
  * legendary8 (strap)     — ONE horizontal buckle-strap across the instep.
  * legendary9 (toecap)    — a reinforced steel toe-cap + rim.
  * this TRIPLE-STRAP stacks THREE horizontal straps up the whole shaft — the
    repeated-band axis, distinct from the single instep strap (one band, low) and
    every toe/heel/wing motif. A flat repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_strap_boots.py / gen_kneeband_legs.py:
strap pixels are painted ONLY onto pixels that are ALREADY opaque body pixels
(`a`). Because it never adds a pixel outside the existing silhouette it CANNOT
create isolated pixels, background bleed, or accent-caused multi-component frames
— QA-safe purely by construction.

  * Body  = the class t4 boots silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction). Female warrior boots
    source lives in the staged _fem_warrior_boots_preview/ dir (load_src fallback).
  * Accent = three straps. Each frame's boot mass is labelled into CONNECTED
    COMPONENTS (a stride with both feet gets three straps per foot). For each
    component we place strap centre-rows at STRAP_FRACS of the bbox height and
    repaint body pixels within BAND_HALF rows of each as a leather band (lit top
    edge), then stamp a small bright BUCKLE square at the component centre-x on
    each strap. All clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no straps — matching the
convention. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class the strap hue is distinct from EVERY prior legendary boots accent:
  * warrior "Warlord's Triple-Strap" — dark-steel body + OXBLOOD straps, gold buckles
  * mage    "Astral Buckles"         — deep-violet body + SILVER straps, cyan buckles
  * ranger  "Warden's Field-Boots"   — bark-brown body + TAN straps, copper buckles

Run from repo root:
  python3 scripts/gen_tristrap_boots.py
Then QA:
  python3 scripts/sprite_qa.py _tristrap_boots_preview/boots_warrior_legendary_tristrap.png --y-max 63
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

CHAR = 'sprites/preview_assets/char'
FALLBACK_DIRS = ['_fem_warrior_boots_preview']

# Three strap centre-rows as fractions of each boot component's bbox height.
STRAP_FRACS = (0.30, 0.55, 0.80)
BAND_HALF = 0.9
BUCKLE_HALF = 1.0
MIN_PX = 8

# body : deep shadow / base / highlight
# strap: STRAP (leather body) / EDGE (lit top edge) / BUCKLE (bright buckle)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_tristrap',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),     # dark steel
        strap=((96, 40, 30), (150, 70, 50), (222, 176, 56)),    # oxblood strap, lit, gold buckle
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_tristrap',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),     # deep violet
        strap=((150, 158, 180), (200, 206, 224), (80, 200, 244)),  # silver strap, lit, cyan buckle
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_tristrap',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),       # bark brown
        strap=((110, 78, 42), (160, 120, 68), (206, 132, 66)),  # tan strap, lit, copper buckle
    ),
}


def load_src(fname):
    p = os.path.join(CHAR, fname)
    if os.path.exists(p):
        return np.array(Image.open(p).convert('RGBA'))
    for d in FALLBACK_DIRS:
        p = os.path.join(d, fname)
        if os.path.exists(p):
            return np.array(Image.open(p).convert('RGBA'))
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


def strap_component(fr, comp, pal):
    STRAP, EDGE, BUCKLE = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cx = 0.5 * (x0 + x1)
    for frac in STRAP_FRACS:
        cy = y0 + frac * h
        band_rows = set()
        for y, x in zip(ys, xs):
            if abs(y - cy) <= BAND_HALF:
                put(fr, y, x, EDGE if (y - cy) <= -0.2 else STRAP)
                band_rows.add(y)
        # small buckle square at the strap centre
        for y in sorted(band_rows):
            for x in range(int(round(cx - BUCKLE_HALF)), int(round(cx + BUCKLE_HALF)) + 1):
                if 0 <= y < FH and 0 <= x < FW and comp[y, x]:
                    put(fr, y, x, BUCKLE)


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
        if fi >= 60:
            continue
        lbl, n = ndimage.label(a)
        for i in range(1, n + 1):
            strap_component(fr, lbl == i, pal)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_tristrap_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_src('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-54s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
