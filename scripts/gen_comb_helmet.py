#!/usr/bin/env python3
"""Generate an EIGHTH net-new-geometry HELMET showcase per class — a VERTICAL
median COMB / CREST-RIDGE repainted straight down the centre of the dome, front to
crown. This is a NEW helmet AXIS distinct from all seven existing helmet
geometries:

  * legendary1 (horns / crown-fans / crest) sweep UP-and-OUT above the skull.
  * legendary2 (crest)                       rises straight UP as one tall fin.
  * legendary3 (winged helm)                 fans WIDE and near-horizontal OUT.
  * legendary4 (aventail)                    hangs mail DOWN the sides.
  * legendary5 (visor)                       fills the CENTRE forward columns.
  * legendary6 (antler)                      BRANCHES into a multi-pronged rack.
  * legendary7 (diadem)                      a HORIZONTAL jewelled brow BAND.
  * this COMB adds NO silhouette pixels at all — it is a bold VERTICAL median
    ridge repainted DOWN the centre column of the dome, the orthogonal complement
    to the diadem's horizontal band. horns / crest-fin / wings / aventail / visor /
    antler / horizontal-band / VERTICAL-ridge is the eight-way contrast.

Authoring philosophy is identical to gen_diadem_helmet.py (its direct model),
including the key robustness win: the comb is painted ONLY onto pixels that are
ALREADY opaque helmet pixels (`a`). Because it never adds a pixel outside the
existing silhouette, it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — the comb is QA-safe purely by construction.
The ridge still reads as a distinct crest because the metal tones contrast with the
recolored helm and it lands at the head's centre column in every pose.

  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a vertical median ridge. For each frame we take the helmet mass's
    horizontal centroid and repaint helm pixels within COMB_HALF px of that centre
    column: bright lit crest along the exact centre line, mid metal one px either
    side, dark rim at the ridge edges, plus periodic bright STUDS marching down the
    crest and a square FINIAL boss at the very top. Everything is clamped to `a`,
    so the comb tracks the head through every pose/animation exactly.

Helmet sheets are empty on the sleep frames, so those are skipped. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class (crest hue distinct so the eighth reads apart from the seven):
  * warrior "Sovereign's Comb"  — dark-iron helm + GOLD crest, ruby finial
  * mage    "Astral Ridge"      — cosmic-indigo helm + SILVER crest, sapphire finial
  * ranger  "Warden's Crest"    — forest helm + BRONZE crest, emerald finial

Run from repo root:
  python3 scripts/gen_comb_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _comb_helmet_preview/helmet_warrior_legendary8.png --y-min 2
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

# Comb geometry. The ridge is a vertical strip at the helmet's horizontal centroid,
# COMB_HALF px half-thickness (so a ~3px-wide crest). STUD_STEP = paint a bright
# stud every N rows down the crest. FINIAL_R = half-size of the boss at the top.
COMB_HALF = 1.4
STUD_STEP = 3
FINIAL_R = 1

# -- Per-class palettes: body ramp (D/M/L) + crest ramp (EDGE, MID, CROWN, STUD) --
# body : deep shadow / base / highlight
# crest: EDGE (dark rim on both sides) / MID / CROWN (lit centre-line) /
#        STUD (bright rivets + finial boss)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary8',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),                   # dark iron -> steel
        crest=((70, 48, 8), (140, 100, 20), (214, 168, 52), (232, 40, 52)),    # gold crest, ruby finial
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary8',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                    # cosmic indigo -> violet
        crest=((70, 76, 92), (140, 148, 168), (212, 220, 236), (56, 120, 240)),# silver crest, sapphire finial
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary8',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                      # forest green
        crest=((52, 34, 12), (104, 70, 26), (166, 116, 48), (46, 200, 108)),   # bronze crest, emerald finial
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


def draw_comb(fr, a, pal):
    """Repaint a vertical median ridge down the helmet centre column. Only helm
    pixels are touched, so the comb adds zero new silhouette pixels (QA-safe)."""
    EDGE, MID, CROWN, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    cx = float(xs.mean())                      # centre column (fractional)
    ytop = int(ys.min())
    for y, x in zip(ys, xs):
        ad = abs(x - cx)                       # horizontal dist from centre column
        if ad > COMB_HALF:
            continue
        # tone by horizontal position within the ridge: lit crest centre-line,
        # dark rim on the two sides
        if ad <= 0.55:
            tone = CROWN
        elif ad <= 1.0:
            tone = MID
        else:
            tone = EDGE
        # periodic bright studs marching down the crest crown line
        if ad <= 0.55 and ((y - ytop) % STUD_STEP == 0):
            tone = STUD
        put(fr, y, x, tone)
    # finial boss: bright square at the very top of the ridge, clamped to helm px.
    bx = int(round(cx))
    by = ytop + 1
    for dy in range(-FINIAL_R, FINIAL_R + 1):
        for dx in range(-FINIAL_R, FINIAL_R + 1):
            yy, xx = by + dy, bx + dx
            if 0 <= yy < FH and 0 <= xx < FW and a[yy, xx]:
                put(fr, yy, xx, STUD)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['crest']
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
        draw_comb(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the comb only repaints helm
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
    outdir = '_comb_helmet_preview'
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
