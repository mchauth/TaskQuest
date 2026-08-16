#!/usr/bin/env python3
"""Generate a NINTH net-new-geometry BOOTS showcase per class — a reinforced steel
TOE-CAP: the forward toe of each boot repainted as a bright metal cap with a raised
rim line behind it. This brings boots to 9-axis parity with the chest slot and is a
NEW boots AXIS distinct from all eight existing boots geometries:

  * legendary_greave   adds mass ABOVE (tall-narrow shin plate to a knee-cop).
  * legendary_cuff     flares mass to the SIDE at the ankle (wide cavalier fold).
  * legendary_sabaton  adds mass FORWARD at the toe (a poulaine POINT — silhouette).
  * legendary_spur     projects mass at the HEEL (a rowel arm).
  * legendary_wing     fans diagonal ankle-WINGS up-and-out.
  * legendary_claw     drops beast-claw TALONS below the sole.
  * legendary_lace     weaves a DIAGONAL X of laces across the shaft.
  * legendary_strap    lays a HORIZONTAL buckle band across the instep.
  * this TOE-CAP repaints the frontmost toe columns of the foot as a bright metal
    cap with a raised rim — a forward-surface axis. The sabaton also lives at the
    toe but as ADDED silhouette (a long poulaine point); the toe-cap adds no
    silhouette pixels, it is a flat repaint of the toe that already exists.

Authoring philosophy mirrors gen_strap_boots.py: the cap is painted ONLY onto
pixels that are ALREADY opaque boot pixels (`a`). Because it never adds a pixel
outside the existing silhouette, it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — the cap is QA-safe purely by
construction.

  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto a
    class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = the toe-cap. We label each frame's boot mass into CONNECTED COMPONENTS
    (so a walk/run pose with two separated feet gets its own cap per foot). The
    character faces LEFT, so the toe is the FRONT (left-most) columns of the foot.
    For each component we take its lower sole rows (bottom SOLE_FRAC of the bbox),
    find the left-most opaque column of each such row, and repaint the CAP_W columns
    from there inward as a bright metal cap (lit crown at the toe tip, mid metal
    behind), then draw a one-column raised RIM just behind the cap in dark tone.
    Everything clamped to `a`.

Sleep frames (fi>=60, lying down) get the recolor only — no cap — matching the
convention of the other boots accents. Shading applied in-script via shade(); do
NOT run sprite_shade.py again.

Per class (cap hue distinct so the ninth reads apart from the eight):
  * warrior "Ironshod Warboots"     — dark-steel boot, STEEL cap, gold rim
  * mage    "Astral Toecap Striders"— deep-violet boot, SILVER cap, cyan rim
  * ranger  "Wildshod Striders"     — bark-brown boot, BRONZE cap, copper rim

Run from repo root:
  python3 scripts/gen_toecap_boots.py
Then QA:
  python3 scripts/sprite_qa.py _toecap_boots_preview/boots_warrior_legendary_toecap.png --y-max 63
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

# Toe-cap geometry. SOLE_FRAC = we cap only the lower sole rows (bottom fraction of
# each foot component's bbox), so the cap wraps the toe not the shaft. CAP_W = width
# in px of the metal cap from the front (left) edge inward. MIN_PX ignores specks.
SOLE_FRAC = 0.42
CAP_W = 2
MIN_PX = 8

# -- Per-class palettes: body ramp (D/M/L) + cap ramp (CROWN, METAL, RIM) ---------
# body : deep shadow / base / highlight
# cap  : CROWN (lit toe tip) / METAL (cap body behind the tip) / RIM (dark raised
#        rim line just behind the cap)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_toecap',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),      # dark steel
        cap=((208, 214, 228), (128, 134, 150), (222, 176, 56)),  # steel cap, gold rim
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_toecap',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),      # deep violet
        cap=((214, 222, 240), (120, 124, 150), (80, 200, 244)),  # silver cap, cyan rim
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_toecap',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),        # bark brown
        cap=((198, 138, 58), (150, 100, 44), (206, 132, 66)),    # bronze cap, copper rim
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


def cap_component(fr, comp, pal):
    """Repaint a toe-cap onto one boot-foot component. comp is a boolean mask
    (frame-sized) of the single component. Body pixels only; front = left edge."""
    CROWN, METAL, RIM = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    h = max(y1 - y0, 1)
    sole_top = y0 + (1.0 - SOLE_FRAC) * h        # only rows below this are the sole
    for y in range(int(round(sole_top)), y1 + 1):
        row = np.where(comp[y])[0]
        if row.size == 0:
            continue
        xl = int(row.min())                      # front (toe) column, char faces left
        # metal cap: CAP_W columns from the toe tip inward
        for k in range(CAP_W):
            x = xl + k
            if 0 <= x < FW and comp[y, x]:
                put(fr, y, x, CROWN if k == 0 else METAL)
        # raised rim: one column just behind the cap, dark tone
        rx = xl + CAP_W
        if 0 <= rx < FW and comp[y, rx]:
            put(fr, y, rx, RIM)


def draw_caps(fr, a, pal):
    lbl, n = ndimage.label(a)
    for i in range(1, n + 1):
        cap_component(fr, lbl == i, pal)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['cap']
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
        draw_caps(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the cap only repaints body
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
    outdir = '_toecap_boots_preview'
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
