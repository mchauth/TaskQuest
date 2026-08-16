#!/usr/bin/env python3
"""ELEVENTH net-new-geometry BOOTS showcase per class — a RIVETED SHAFT SEAM: a
vertical seam running up the outside of the boot shaft, studded with a column of
round rivets (the riveted back-seam of a tall war-boot). This brings the boots slot
to ELEVEN distinct axes. It is the vertical-seam-of-studs axis none of the ten
existing legendary boots occupy:

  * legendary1 (greave)    — a tall shin plate + knee-cop.
  * legendary2 (cuff)      — one wide folded cavalier cuff at the top.
  * legendary3 (sabaton)   — a forward-raked poulaine toe (silhouette).
  * legendary4 (spur)      — a heel rowel-spur wheel.
  * legendary5 (winged)    — diagonal ankle wings.
  * legendary6 (claw)      — downward beast-claw talons.
  * legendary7 (lace)      — a diagonal cross-lacing X on the instep.
  * legendary8 (strap)     — ONE horizontal buckle-strap across the instep.
  * legendary9 (toecap)    — a reinforced steel toe-cap + rim.
  * legendary10 (tristrap) — three stacked HORIZONTAL straps up the shaft.
  * this RIVET-SHAFT runs a single VERTICAL seam of rivets up the shaft — the
    vertical-stud axis, distinct from the horizontal tristrap/instep straps and
    every toe/heel/wing/claw motif. A flat repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_tristrap_boots.py: seam pixels are painted
ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — QA-safe by construction. Each
frame's boot mass is labelled into CONNECTED COMPONENTS so a stride with both feet
gets its own seam per foot.

Sleep frames (fi>=60, lying down) get the recolor only — no seam. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class the seam/rivet hue is the class accent family:
  * warrior "Warlord's Riveted Warboots" — dark-steel body + steel seam, gold rivets
  * mage    "Astral Seam-Striders"        — deep-violet body + silver seam, cyan rivets
  * ranger  "Warden's Studded Field-Boots"— bark-brown body + bronze seam, copper rivets

Run from repo root:
  python3 scripts/gen_rivetshaft_boots.py
Then QA:
  python3 scripts/sprite_qa.py _rivetshaft_boots_preview/boots_warrior_legendary_rivetshaft.png --y-max 63
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

# Seam runs up the upper SEAM_SPAN fraction of each boot component's bbox height,
# placed SEAM_FRAC of the way across (outer side). Rivets every STUD_STEP rows.
SEAM_FRAC = 0.62
SEAM_SPAN = 0.62
STUD_STEP = 2
MIN_PX = 8

# body : deep shadow / base / highlight
# seam : SEAM (lit seam line) / SHADOW (dark seam edge) / RIVET (bright stud)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_rivetshaft',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),     # dark steel
        seam=((168, 174, 190), (60, 64, 76), (232, 190, 70)),   # steel seam, dark edge, gold rivet
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_rivetshaft',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),     # deep violet
        seam=((196, 202, 224), (40, 34, 96), (80, 200, 244)),   # silver seam, dark edge, cyan rivet
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_rivetshaft',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),       # bark brown
        seam=((160, 120, 68), (44, 32, 18), (206, 132, 66)),    # bronze seam, dark edge, copper rivet
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


def draw_seam(fr, comp, pal):
    """Paint a vertical riveted seam up one boot component."""
    SEAM, SHADOW, RIVET = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    w = max(x1 - x0, 1)
    seam_x = x0 + SEAM_FRAC * w
    ytop = y0
    ybot = y0 + SEAM_SPAN * h
    for y, x in zip(ys, xs):
        if not (ytop <= y <= ybot):
            continue
        if abs(x - seam_x) < 0.5:
            put(fr, y, x, SEAM)
        elif abs(x - (seam_x + 1.0)) < 0.5:     # dark edge to the right of the seam
            put(fr, y, x, SHADOW)
    # rivet studs every STUD_STEP rows along the seam
    sx = int(round(seam_x))
    for y in range(int(round(ytop)), int(round(ybot)) + 1, STUD_STEP):
        if comp[y, sx] if (0 <= y < FH and 0 <= sx < FW) else False:
            put(fr, y, sx, RIVET)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['seam']
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
        lbl, n = ndimage.label(a)
        for k in range(1, n + 1):
            draw_seam(fr, lbl == k, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_rivetshaft_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_src('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.20, adj_max=0.25)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-52s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
