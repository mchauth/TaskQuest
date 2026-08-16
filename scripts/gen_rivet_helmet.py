#!/usr/bin/env python3
"""TENTH net-new-geometry HELMET showcase per class — a RIVETED RIM: a reinforcing
band wrapped around the lower edge of the helm, studded with a regular row of round
rivets (the riveted construction of a banded war-helm). This brings the helmet slot
to TEN distinct axes. It is the studded-construction axis none of the nine existing
legendary helmets occupy:

  * legendary1 (base)      — plain dome.
  * legendary2 (crest)     — a tall vertical crest (silhouette).
  * legendary3 (winghelm)  — wide side wings (silhouette).
  * legendary4 (aventail)  — a mail drape hanging below.
  * legendary5 (visor)     — a forward faceplate + eye-slit.
  * legendary6 (antler)    — a branching antler rack (silhouette).
  * legendary7 (diadem)    — a JEWELLED brow-band (coloured gems, high on the brow).
  * legendary8 (comb)      — a vertical median comb down the centre.
  * legendary9 (cheek)     — paired lateral cheek-plates framing the face.
  * this RIVET-RIM lays a horizontal reinforcing band low on the helm rim, studded
    with evenly-spaced METAL rivets — mechanical construction, not gems — distinct
    from the jewelled diadem (higher, coloured, no studs) and every crest/wing/plate
    motif. A flat repaint that adds no silhouette pixels and never touches the face
    slit (rivets sit on the dome rim above it).

Authoring philosophy is identical to gen_comb_helmet.py / gen_kneeband_legs.py:
rivet pixels are painted ONLY onto pixels that are ALREADY opaque body pixels
(`a`). Because it never adds a pixel outside the existing silhouette it CANNOT
create isolated pixels, background bleed, or accent-caused multi-component frames
— QA-safe purely by construction.

  * Body  = the class helmet silhouette (helmet_rare1 for warrior — full m+f
    coverage; helmet_mage4 / helmet_ranger4 for mage/ranger, + _f) recolored
    per-frame via luminance-quantile mapping onto a class-distinct 3-tone ramp.
  * Accent = the riveted rim. For the largest helm component per frame we take its
    bbox, place the band centre-row RIM_FRAC of the way down, repaint body pixels
    within BAND_HALF rows as a metal band (lit top edge), then stamp a bright rivet
    stud every STUD_STEP columns along the band. All clamped to `a`.

Sleep frames (fi>=60) get the recolor only — no rim. Shading applied in-script via
shade(); do NOT run sprite_shade.py again.

Per class the rim/rivet hue is distinct from EVERY prior legendary helmet accent:
  * warrior "Warlord's Riveted Helm" — dark-iron body + STEEL band, gold rivets
  * mage    "Astral Riveted Circlet" — cosmic-indigo body + SILVER band, cyan rivets
  * ranger  "Warden's Studded Hood"  — forest body + BRONZE band, copper rivets

Run from repo root:
  python3 scripts/gen_rivet_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _rivet_helmet_preview/helmet_warrior_legendary10.png --y-min 2
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

# Riveted-rim geometry. Band centre-row RIM_FRAC down the helm bbox, BAND_HALF rows
# thick. Rivets are bright studs stamped every STUD_STEP columns along the band.
RIM_FRAC = 0.74
BAND_HALF = 0.9
STUD_STEP = 2
MIN_PX = 12

# body : deep shadow / base / highlight
# rim  : BAND (metal band) / EDGE (lit top edge) / RIVET (bright stud)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary10',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),      # dark iron -> steel
        rim=((70, 74, 86), (140, 146, 162), (232, 190, 70)),      # steel band, lit, gold rivets
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary10',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),       # cosmic indigo -> violet
        rim=((70, 76, 92), (150, 158, 180), (72, 200, 244)),      # silver band, lit, cyan rivets
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary10',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),         # forest green
        rim=((84, 58, 26), (150, 108, 52), (206, 132, 66)),       # bronze band, lit, copper rivets
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


def rivet_rim(fr, comp, pal):
    BAND, EDGE, RIVET = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    cy = y0 + RIM_FRAC * h
    band_cols = {}
    for y, x in zip(ys, xs):
        if abs(y - cy) <= BAND_HALF:
            put(fr, y, x, EDGE if (y - cy) <= -0.2 else BAND)
            band_cols.setdefault(x, []).append(y)
    if not band_cols:
        return
    # stamp a bright rivet stud every STUD_STEP columns, phased to the band's left
    xs_sorted = sorted(band_cols)
    x_left = xs_sorted[0]
    for x in xs_sorted:
        if (x - x_left) % STUD_STEP != 0:
            continue
        yy = band_cols[x]
        ry = int(round(np.median(yy)))     # rivet on the band's centre row for this col
        if comp[ry, x]:
            put(fr, ry, x, RIVET)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['rim']
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
        if n >= 1:
            sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
            dome = (lbl == (int(np.argmax(sizes)) + 1))
            rivet_rim(fr, dome, pal)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_rivet_helmet_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-50s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
