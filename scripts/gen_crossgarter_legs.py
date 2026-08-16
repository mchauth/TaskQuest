#!/usr/bin/env python3
"""TENTH net-new-geometry LEGS showcase per class — CROSS-GARTER wraps: a Roman/
Norse-style criss-cross lattice bound around each shin, an 'X' of two diagonal
straps over the lower leg. This brings the legs slot to TEN distinct axes. It is
the lattice/criss-cross surface axis none of the nine existing legendary legs
occupy:

  * legendary1 (tassets)     — short paired hip flaps.
  * legendary2 (war-kilt)    — a long cloth drape to a flared hem.
  * legendary3 (faulds)      — a stiff tiered plate skirt at the hip.
  * legendary4 (poleyns)     — round knee discs (silhouette).
  * legendary5 (cuisses)     — a hip fin (silhouette).
  * legendary6 (loin-guard)  — a narrow vertical centre strap.
  * legendary7 (sword-belt)  — ONE diagonal band across the thighs.
  * legendary8 (side-stripe) — paired vertical bands, outer edge.
  * legendary9 (knee-band)   — one horizontal band at the knee.
  * this CROSS-GARTER lays TWO crossed diagonals (an X) over each SHIN — a lattice
    on the lower leg, distinct from the single sword-belt diagonal (upper thigh,
    one direction) and from every horizontal/vertical band. A flat repaint that
    adds no silhouette pixels.

Authoring philosophy is identical to gen_kneeband_legs.py: strap pixels are painted
ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — QA-safe purely by construction.

  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = the cross-garter. Each frame's leg mass is labelled into CONNECTED
    COMPONENTS (a walk/run pose with two separated legs gets its own X per leg).
    For each component we take the LOWER portion (below GARTER_TOP of the bbox
    height) and repaint any body pixel whose perpendicular distance to either of
    the two crossing diagonals is within STRAP_HALF as a leather strap (lit where
    the two straps cross). All clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no garter — matching the
apron / cuisse / kilt / side-stripe / knee-band convention. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class the strap hue is distinct from EVERY prior legendary legs accent:
  * warrior "Warlord's Cross-Garter" — obsidian/steel body + OXBLOOD straps, gold knot
  * mage    "Astral Bindings"        — arcane-violet body + PALE-SILVER straps, cyan knot
  * ranger  "Warden's Leg-Wraps"     — forest body + TAN-leather straps, copper knot

Run from repo root:
  python3 scripts/gen_crossgarter_legs.py
Then QA:
  python3 scripts/sprite_qa.py _crossgarter_legs_preview/pants_warrior_legendary10.png --y-max 62
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

# Cross-garter geometry. The X occupies the lower (1-GARTER_TOP) fraction of each
# leg component's bbox. STRAP_HALF is the half-thickness (perpendicular distance)
# of each diagonal strap. MIN_PX ignores tiny toe/heel specks.
GARTER_TOP = 0.42      # straps start this far down the component
STRAP_HALF = 0.9
MIN_PX = 10

# body : deep shadow / base / highlight
# garter: STRAP (leather body) / EDGE (lit strap-cross highlight) / KNOT (bright knot)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary10',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),      # obsidian -> steel
        garter=((96, 40, 30), (150, 70, 50), (232, 190, 70)),    # oxblood strap, lit, gold knot
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary10',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),      # arcane violet
        garter=((150, 158, 180), (200, 206, 224), (72, 200, 244)),  # pale silver strap, lit, cyan knot
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary10',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),        # forest green
        garter=((96, 66, 34), (150, 110, 62), (206, 132, 66)),   # tan leather strap, lit, copper knot
    ),
}


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


def _dist_to_seg(x, y, x0, y0, x1, y1):
    """Perpendicular distance from (x,y) to segment (x0,y0)-(x1,y1)."""
    dx, dy = x1 - x0, y1 - y0
    L2 = dx * dx + dy * dy
    if L2 < 1e-6:
        return np.hypot(x - x0, y - y0)
    t = ((x - x0) * dx + (y - y0) * dy) / L2
    t = max(0.0, min(1.0, t))
    px, py = x0 + t * dx, y0 + t * dy
    return np.hypot(x - px, y - py)


def garter_component(fr, comp, pal):
    STRAP, EDGE, KNOT = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    yt = y0 + GARTER_TOP * h            # top of the garter zone
    # two crossing diagonals spanning the lower box [yt..y1] x [x0..x1]
    seg1 = (x0, yt, x1, y1)             # top-left -> bottom-right
    seg2 = (x1, yt, x0, y1)            # top-right -> bottom-left
    cross_pts = []
    for y, x in zip(ys, xs):
        if y < yt:
            continue
        d1 = _dist_to_seg(x, y, *seg1)
        d2 = _dist_to_seg(x, y, *seg2)
        if min(d1, d2) <= STRAP_HALF:
            # where the two straps overlap -> lit highlight
            put(fr, y, x, EDGE if (d1 <= STRAP_HALF and d2 <= STRAP_HALF) else STRAP)
            if d1 <= STRAP_HALF and d2 <= STRAP_HALF:
                cross_pts.append((y, x))
    # bright knot pip at the crossing (median of overlap pixels)
    if cross_pts:
        cy = int(round(np.median([p[0] for p in cross_pts])))
        cx = int(round(np.median([p[1] for p in cross_pts])))
        if comp[cy, cx]:
            put(fr, cy, cx, KNOT)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['garter']
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
            garter_component(fr, lbl == i, pal)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_crossgarter_legs_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-48s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
