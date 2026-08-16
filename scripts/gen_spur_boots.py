#!/usr/bin/env python3
"""Generate a FOURTH NET-NEW-GEOMETRY BOOTS silhouette per class — a KNIGHT'S
ROWEL-SPUR that projects BACKWARD/OUTWARD from the heel and is tipped by a small
spiked star-wheel (rowel). This completes the boots showcase to FOUR distinct
silhouettes, bringing the boots slot to parity with chest / helmet / legs (which
each already have four net-new-geometry silhouettes).

Why this is a NEW silhouette (distinct from ALL THREE existing boots geometries):
  * "greave boots"  add mass ABOVE the boot   — a tall narrow shin plate climbing
    UPWARD to a knee-cop (vertical profile, top-anchored).
  * "cuff boots"    add mass to the SIDE      — a folded cavalier cuff flaring
    HORIZONTALLY OUTWARD across the ankle-top rows (low-wide profile).
  * "sabaton boots" add mass at the BOTTOM    — a raked poulaine toe sweeping
    FORWARD along the GROUND row (a forward point).
  * These SPUR boots add mass at the HEEL     — a thin spur ARM projecting outward
    at ankle/heel height (ABOVE the ground toe zone, BELOW the shin), each tipped
    by a spiked ROWEL WHEEL. Up (greave) / out-at-ankle (cuff) / forward-at-toe
    (sabaton) / heel-spur-wheel (spur) is the four-way silhouette contrast the
    chest / helmet / legs showcases each already draw.
  The signature spiked ROWEL WHEEL at the arm tip is unique to this boot and
  reads unmistakably as a spur even though the arm itself is short.

Authoring philosophy is identical to gen_sabaton_boots.py / gen_cuff_boots.py /
gen_greave_boots.py:
  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the heel spur. On a single heel row (SP_DY above the boot's own
    bottom row, i.e. ABOVE the ground/toe zone the sabaton uses) we take that
    row's leftmost/rightmost boot pixel and lay a contiguous horizontal ARM of
    length ARM outward, then stamp a small rowel WHEEL at the tip: a lit hub with
    four dark spikes (out / up / down / and the outermost point). Every accent
    pixel is 4-connected to the body mass by construction — the arm is a
    contiguous run starting from the boot pixel in ITS OWN row, and each rowel
    spike touches the hub which touches the arm. Drawn ONLY in transparent space,
    never overpaints the body.

Connectivity is further guaranteed with the same per-frame guard as the sabaton/
cuff/greave: any accent pixel not 4-connected to the body mass is cleared, so
accent strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no spur — matching the
sabaton / cuff / tasset / kilt / cape convention. Shading applied in-script via
shade(); do NOT run sprite_shade.py again.

Per class (spur hue chosen distinct from that class's greave / cuff / sabaton
accents so all four boots read apart):
  * warrior "Ironclad Rowel-Spurs" — dark-steel boot + warm GOLD rowel wheels
  * mage    "Astral Rowel-Striders"— deep-violet boot + cyan-starlight rowels
  * ranger  "Wildspur Treads"      — bark-brown boot + burnished-COPPER rowels

Run from repo root:
  python3 scripts/gen_spur_boots.py
Then QA (the rowel intentionally projects beyond the normal boot footprint):
  python3 scripts/sprite_qa.py _spur_boots_preview/boots_warrior_legendary_spur.png --y-max 63
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

# ── Spur geometry ─────────────────────────────────────────────────────────────
# The spur sits at HEEL height: SP_DY rows above the boot's own bottom row (so it
# is clearly ABOVE the ground/toe zone the sabaton uses). A thin horizontal ARM
# of length ARM projects outward from each side, tipped by a rowel wheel.
SP_DY = 3             # rows above the boot bottom where the spur arm anchors
ARM = 3               # horizontal reach of the spur arm (px, per side)

# ── Per-class palettes: body ramp (D/M/L) + spur ramp (TIP, D, M, L) ───────────
# body: deep shadow / base / highlight
# spur: TIP (dark spike) / D (attach shadow) / M (mid metal) / L (lit hub)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_spur',
        body=((40, 42, 48), (84, 88, 98), (150, 156, 168)),                # dark steel
        spur=((70, 48, 12), (150, 110, 30), (210, 166, 60), (248, 224, 140)),  # warm gold rowel
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_spur',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),                # deep violet
        spur=((26, 58, 78), (60, 132, 168), (120, 206, 232), (224, 248, 255)),  # cyan-starlight rowel
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_spur',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),                  # bark brown
        spur=((56, 28, 12), (132, 74, 32), (196, 116, 58), (238, 176, 116)),  # burnished copper rowel
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def free(fr, a, y, x):
    """True if (y,x) is in-frame, not body, not already painted."""
    return 0 <= y < FH and 0 <= x < FW and not a[y, x] and fr[y, x, 3] == 0


def recolor(src, fr, a, D, M, L):
    """Quantized 3-tone recolor of the legendary silhouette (per-frame)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_spur(fr, a, pal):
    """Thin heel spur ARM + rowel WHEEL projecting outward from each side."""
    TIP, D, M, L = pal
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return
    y1 = int(rows.max())
    y_a = y1 - SP_DY                       # heel/ankle row (above the ground toe)
    if y_a < 2 or not a[y_a].any():
        return
    xs = np.where(a[y_a])[0]
    xmin, xmax = int(xs.min()), int(xs.max())
    for base_x, sgn in ((xmin, -1), (xmax, +1)):
        # horizontal arm outward from this side's own edge
        tip_x = None
        for k in range(1, ARM + 1):
            x = base_x + sgn * k
            if not free(fr, a, y_a, x):
                break
            put(fr, y_a, x, D if k == 1 else M)
            tip_x = x
        if tip_x is None:
            continue
        # rowel wheel at the arm tip: lit hub + dark spikes (out / up / down)
        put(fr, y_a, tip_x, L)                        # bright hub
        for (yy, xx) in ((y_a, tip_x + sgn), (y_a - 1, tip_x), (y_a + 1, tip_x)):
            if free(fr, a, yy, xx):
                put(fr, yy, xx, TIP)                  # spikes


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['spur']
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
        draw_spur(fr, a, pal)
        # Connectivity guard: drop any accent pixel not 4-connected to the body
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
    outdir = '_spur_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_src('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-52s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
