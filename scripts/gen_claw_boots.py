#!/usr/bin/env python3
"""Generate a SIXTH net-new-geometry BOOTS silhouette per class — BEAST-CLAW
TALONS that splay DOWNWARD from the sole, projecting a set of curved claw-points
below and slightly outward from the foot.

Why this is a NEW boots treatment (distinct from ALL FIVE existing ones):
  * legendary_greave adds mass ABOVE (tall-narrow shin plate to a knee-cop).
  * legendary_cuff flares mass to the SIDE at the ankle (low-wide cavalier fold).
  * legendary_sabaton adds mass FORWARD at the toe (a poulaine point raked along
    the GROUND row).
  * legendary_spur projects mass at the HEEL (a rowel arm out at ankle height).
  * legendary_wing fans diagonal ankle-WINGS up-and-out.
  * This one occupies the DOWNWARD axis none of them touch: talons drop BELOW the
    sole. Where the sabaton rakes its point sideways ALONG the ground, these
    claws hang DOWN past it — the foot reads as a raptor/beast claw gripping the
    earth, mass under the boot, not around it.

Authoring philosophy is identical to gen_sabaton_boots.py:
  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the talons. For each contiguous foot-run on the boot's bottom row we
    drop CLAW_N claws (at the run's left / middle / right). Each claw is a
    contiguous DOWNWARD staircase rooted directly below an opaque sole pixel (so
    the top claw pixel is 4-connected UP to the foot and the whole claw is one
    component fused to the body). Outer claws stair down-AND-out so the set
    splays; the middle claw drops straight. Drawn ONLY in transparent space below
    the sole — never overpaints the boot body.

Connectivity is further guaranteed with the same per-frame guard as the sabaton /
spur / cuff: any claw pixel not 4-connected to the body mass is cleared, so
accent strays are 0 by construction. Sleep frames (fi>=60) get the recolor only.
Because the claws hang below the sole (into the y~60-63 ground band) the female
warrior/other WIDE sheets may trip the expected 1px BACKGROUND-BLEED flag past
the x30-55 body box exactly like the sabaton toe — the rigorous verify is clean.

Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (claw hue distinct so all three read apart):
  * warrior "Ironrend Talons" — dark-steel boot, pale iron claws
  * mage    "Voidrend Talons" — deep-violet boot, amethyst/lilac claws
  * ranger  "Wildclaw Talons" — bark-brown boot, bone-white claws

Run from repo root:
  python3 scripts/gen_claw_boots.py
Then QA:
  python3 scripts/sprite_qa.py _claw_boots_preview/boots_warrior_legendary_claw.png --y-max 63
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

# Talon geometry. Per foot-run on the bottom row we drop up to CLAW_N claws; each
# is a downward staircase CLAW_LEN long. The middle claw drops straight; the two
# outer claws stair down-and-out by OUT_STEP so the foot splays.
CLAW_LEN = 3          # rows each claw hangs below the sole
OUT_STEP = 1          # outward drift per row for the outer claws
MIN_RUN = 3           # ignore foot-runs narrower than this (stray/thin px)

# ── Per-class palettes: body ramp (D/M/L) + claw ramp (TIP, D, M, L) ───────────
# body: deep shadow / base / highlight
# claw: TIP (dark claw-point at the bottom) / D (shadow where claw meets sole) /
#       M (mid) / L (lit)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_claw',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),                    # dark steel
        claw=((26, 28, 36), (70, 76, 88), (168, 176, 192), (222, 228, 240)),   # pale iron claws
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_claw',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),                    # deep violet
        claw=((28, 14, 44), (72, 44, 112), (158, 116, 210), (214, 186, 246)),  # amethyst/lilac claws
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_claw',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),                      # bark brown
        claw=((28, 24, 18), (88, 80, 64), (176, 166, 138), (236, 230, 210)),   # bone-white claws
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


def claw_tone(k, run, pal):
    """pal = (TIP, D, M, L). k = rows down from the sole (1..run). Dark TIP at the
    very bottom point; shadow crease where the claw meets the sole; lit/mid between."""
    TIP, D, M, L = pal
    if k == run:
        return TIP
    if k == 1:
        return D
    return L if (k % 2 == 0) else M


def runs_on_row(a, y):
    """Contiguous opaque runs (xstart, xend) on row y."""
    xs = np.where(a[y])[0]
    if xs.size == 0:
        return []
    out, start, prev = [], int(xs[0]), int(xs[0])
    for x in xs[1:]:
        x = int(x)
        if x == prev + 1:
            prev = x
            continue
        out.append((start, prev))
        start = prev = x
    out.append((start, prev))
    return out


def drop_claw(fr, a, y0, x0, sign, pal):
    """Downward staircase claw from directly below (y0,x0). sign 0 = straight,
    -1/+1 = drift out per row. Only fills transparent space below the sole."""
    cx = x0
    for k in range(1, CLAW_LEN + 1):
        y = y0 + k
        cx = x0 + sign * OUT_STEP * (k - 1)
        if not (0 <= cx < FW) or y >= FH:
            break
        if a[y, cx] or fr[y, cx, 3] > 0:   # never overpaint body/existing
            continue
        put(fr, y, cx, claw_tone(k, CLAW_LEN, pal))


def draw_talons(fr, a, pal):
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return
    y1 = int(rows.max())                   # boot overall bottom row
    for xstart, xend in runs_on_row(a, y1):
        if xend - xstart + 1 < MIN_RUN:
            continue
        xmid = (xstart + xend) // 2
        # left claw drifts out (-), middle straight (0), right claw drifts out (+)
        for x0, sign in ((xstart, -1), (xmid, 0), (xend, +1)):
            drop_claw(fr, a, y1, x0, sign, pal)


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
        if fi >= 60:                       # sleep: body only
            continue
        draw_talons(fr, a, pal)
        # Connectivity guard: drop any claw pixel not 4-connected to the body.
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
    outdir = '_claw_boots_preview'
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
