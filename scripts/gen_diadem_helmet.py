#!/usr/bin/env python3
"""Generate a SEVENTH net-new-geometry HELMET showcase per class — a jewelled
BROW-BAND / DIADEM CIRCLET wrapping horizontally around the helmet brow. This is a
NEW helmet AXIS distinct from all six existing helmet geometries, every one of
which is a SILHOUETTE EXTENSION reaching out past the head:

  * legendary1 (horns / crown-fans / crest)  sweep UP-and-OUT above the skull.
  * legendary2 (crest)                        rises straight UP as one tall fin.
  * legendary3 (winged helm)                  fans WIDE and near-horizontal OUT.
  * legendary4 (aventail)                     hangs mail DOWN the sides.
  * legendary5 (visor)                        fills the CENTRE forward columns.
  * legendary6 (antler)                       BRANCHES into a multi-pronged rack.
  * this DIADEM adds NO silhouette pixels at all — it is a bold HORIZONTAL jewelled
    band repainted ACROSS the brow, the surface-band axis none of the six touch
    (parallel to how the girdle became the chest 7th and the leg-baldric the legs
    7th — both repaint bands rather than new silhouette).

Authoring philosophy is identical to gen_girdle_legendary.py (its direct model),
including the key robustness win: the diadem is painted ONLY onto pixels that are
ALREADY opaque helmet pixels (`a`). Because it never adds a pixel outside the
existing silhouette, it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — the diadem is QA-safe purely by
construction. The band still reads as a distinct circlet because the jewel tones
contrast sharply with the recolored helm and it lands at a fixed fraction down the
helmet in every pose.

  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a horizontal circlet band. For each frame we take the helmet mass's
    vertical extent and place the band at BAND_FRAC of the way down it, BAND_HALF
    px thick. Helmet pixels inside the band are repainted as the circlet: lit metal
    crown along the centre row, dark rim on the top/bottom edges, periodic bright
    GEMS marching across, and a larger central CENTRE-GEM. Everything is clamped to
    `a`, so the diadem tracks the head through every pose/animation exactly.

Helmet sheets are empty on the sleep frames, so those are skipped. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class (jewel hue distinct so the seventh reads apart from the six):
  * warrior "Sovereign's Diadem" — dark-iron helm + GOLD circlet, ruby gems
  * mage    "Astral Circlet"     — cosmic-indigo helm + SILVER circlet, sapphire gems
  * ranger  "Warden's Circlet"   — forest helm + BRONZE circlet, emerald gems

Run from repo root:
  python3 scripts/gen_diadem_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _diadem_helmet_preview/helmet_warrior_legendary7.png --y-min 2
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

# Circlet geometry. The band is a horizontal strip across the helmet mass, placed
# at BAND_FRAC down the vertical extent of the frame's helm pixels (a low fraction
# so it lands on the brow, not the crown), with a half-thickness of BAND_HALF.
# GEM_STEP = paint a bright gem every N columns across the crown row. CGEM_R =
# half-size of the larger centre-gem at the horizontal centre.
BAND_FRAC = 0.42      # 0 = helm top, 1 = helm bottom -> lands on the brow
BAND_HALF = 1.4
GEM_STEP = 3
CGEM_R = 1

# -- Per-class palettes: body ramp (D/M/L) + circlet ramp (EDGE, MID, CROWN, GEM) -
# body   : deep shadow / base / highlight
# circlet: EDGE (dark rim on both edges) / MID / CROWN (lit metal centre-row) /
#          GEM (bright jewels + centre-gem)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary7',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),                   # dark iron -> steel
        circlet=((70, 48, 8), (140, 100, 20), (214, 168, 52), (232, 40, 52)),  # gold band, ruby gems
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary7',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                    # cosmic indigo -> violet
        circlet=((70, 76, 92), (140, 148, 168), (212, 220, 236), (56, 120, 240)),  # silver band, sapphire gems
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary7',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                      # forest green
        circlet=((52, 34, 12), (104, 70, 26), (166, 116, 48), (46, 200, 108)), # bronze band, emerald gems
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    """Quantized 3-tone recolor of the helmet silhouette (per-frame)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_diadem(fr, a, pal):
    """Repaint a horizontal circlet band across the helmet brow. Only helm pixels
    are touched, so the band adds zero new silhouette pixels (QA-safe)."""
    EDGE, MID, CROWN, GEM = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    ytop, ybot = int(ys.min()), int(ys.max())
    cy = ytop + BAND_FRAC * (ybot - ytop)     # band centre-row (fractional)
    xleft = int(xs.min())
    for y, x in zip(ys, xs):
        ad = abs(y - cy)                       # vertical dist from centre-row
        if ad > BAND_HALF:
            continue
        # tone by vertical position within the band: lit metal crown centre-row,
        # dark rim on top/bottom edges
        if ad <= 0.55:
            tone = CROWN
        elif ad <= 1.0:
            tone = MID
        else:
            tone = EDGE
        # periodic bright gems marching across the crown row
        if ad <= 0.55 and ((x - xleft) % GEM_STEP == 0):
            tone = GEM
        put(fr, y, x, tone)
    # larger centre-gem: bright square where the band crosses the helm centre,
    # clamped to helm pixels only.
    bx = int(round(float(xs.mean())))
    by = int(round(cy))
    for dy in range(-CGEM_R, CGEM_R + 1):
        for dx in range(-CGEM_R, CGEM_R + 1):
            yy, xx = by + dy, bx + dx
            if 0 <= yy < FH and 0 <= xx < FW and a[yy, xx]:
                put(fr, yy, xx, GEM)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['circlet']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():                        # empty (incl. sleep) frames skipped
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        draw_diadem(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the band only repaints helm
        # pixels so no stray is possible; the guard is a no-op here by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        strays = da & ~keep
        for y, x in np.argwhere(strays):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_diadem_helmet_preview'
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
