#!/usr/bin/env python3
"""Generate a SIXTH net-new-geometry HELMET silhouette per class — a great
BRANCHING ANTLER CROWN: a pair of stag/beast antlers that sweep UP-and-OUTWARD
from the crown corners and BRANCH into forward tines, framing the head like a
horned nature-lord's rack.

Why this is a NEW helmet treatment (distinct from ALL FIVE existing ones):
  * legendary1 (Wyrmhorn horns / Starweaver crown-fans / Plumed-Hood crest)
    spread UP-and-OUTWARD above the skull as SMOOTH single sweeps.
  * legendary2 (Crest circlets) rise straight UP from the crown as one tall fin.
  * legendary3 (Winged helms) fan WIDE and near-horizontal OUTWARD at skull
    height.
  * legendary4 (Aventail camail) hangs mail DOWN the SIDES, framing an open face.
  * legendary5 (Visored faceplate) fills the CENTRE forward columns, sealing the
    face.
  * This one occupies the BRANCHING axis none of them touch: a tall antler BEAM
    per side that climbs up-and-out AND throws off multiple contiguous TINES —
    the silhouette reads as a multi-pronged rack, not a smooth horn (l1), not a
    single fin (l2), not a flat wing (l3). Where the first-tier horns are two
    clean curves, the antlers are two branching trees.

Authoring philosophy is identical to gen_visor_helmet.py / gen_winghelm_legendary.py:
  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the antler rack. For each side we find the crown corner near the
    helmet TOP, root the beam one row ABOVE that column's own topmost helm pixel
    (so the root is 4-connected DOWN to the helm), then grow the beam as a
    4-connected STAIRCASE (up one row, then out one column — both pixels laid, so
    the chain never relies on a diagonal-only link). TINES branch off the beam
    the same way, each a contiguous staircase run rooted on a beam pixel. Every
    antler pixel is clamped to y>=Y_MIN (QA head zone) and drawn ONLY in
    transparent space (never overpaints the helmet body).

Connectivity is further guaranteed with the same per-frame guard as the visor /
wing / cape: any antler pixel not 4-connected to the body mass is cleared, so
accent strays are 0 by construction. Because the beam is anchored RELATIVE to
each frame's own helmet-top contour, it tracks the animation bob exactly (no
absolute-Y drift). Helmet sheets are empty on the sleep frames, so those are
skipped.

Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (antler hue distinct so all three read apart):
  * warrior "Dreadhorn Warcrown" — dark-iron helm, pale iron-bone antlers
  * mage    "Astral Antler-Crown" — cosmic-indigo helm, cyan/violet crystal tines
  * ranger  "Wildhorn Stag-Crown" — forest helm, warm natural stag-bone antlers

Run from repo root:
  python3 scripts/gen_antler_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _antler_helmet_preview/helmet_warrior_legendary6.png --y-min 2
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

# Antler geometry. Per side a near-VERTICAL BEAM climbs from the crown corner
# (mostly up, gently out) as a 4-connected staircase; TINES FORK off it, running
# mostly OUTWARD so they splay clearly away from the beam (a branching rack, not a
# smooth horn). Everything clamps to y>=Y_MIN.
BEAM_UP = 9            # rows the beam rises
BEAM_OUT = 4          # cols the beam drifts outward over its rise (up-biased)
ROOT_INSET = 1        # columns in from the top-band edge to root the beam
TOP_BAND = 4          # rows below the helmet top used to find the crown corner
Y_MIN = 2             # never draw an antler pixel above this row (QA head zone)
# Tines fork off the beam at these fractions of its length; each (frac, up, out).
# Small up + larger out => the tine breaks OUTWARD, clearly separating from the
# near-vertical beam so the silhouette reads as a multi-pronged antler.
TINES = ((0.30, 2, 4), (0.55, 2, 4), (0.80, 1, 3))

# ── Per-class palettes: body ramp (D/M/L) + antler ramp (TIP, D, M, L) ─────────
# body : deep shadow / base / highlight
# antler: TIP (bright prong tip) / D (base/shadow side) / M (mid beam) /
#         L (lit front face)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary6',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),                 # dark iron -> steel
        antler=((245, 242, 230), (96, 88, 74), (170, 160, 140), (222, 214, 196)),  # pale iron-bone
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary6',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                  # cosmic indigo -> violet
        antler=((200, 240, 255), (40, 34, 110), (92, 82, 196), (156, 172, 240)),   # cyan/violet crystal
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary6',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                    # forest green
        antler=((238, 226, 196), (78, 58, 34), (140, 110, 68), (196, 168, 120)),   # natural stag-bone
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


def antler_tone(kind, k, run, pal):
    """kind: 'beam' or 'tine'. k = index along the run (1..run). Bright TIP at the
    prong end; dark base; beams read mid, tines read lit so branches pop."""
    TIP, D, M, L = pal
    if k == run:
        return TIP
    if k == 1:
        return D
    return M if kind == 'beam' else L


def crown_corner(a, sign):
    """Column of the crown corner on one side, measured on the helmet's TOP band
    (the first TOP_BAND rows of opaque helm), inset ROOT_INSET columns inward."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return None
    ytop = int(rows.min())
    band = a[ytop:ytop + TOP_BAND]
    xs = np.where(band.any(axis=0))[0]
    if xs.size == 0:
        return None
    x_edge = int(xs.min()) if sign < 0 else int(xs.max())
    return x_edge - sign * ROOT_INSET      # inset inward off the very edge


def walk(fr, a, y0, x0, up, out, sign, kind, pal, place_root=False):
    """Walk a 4-connected staircase from (y0,x0): `up` rows up and `out` cols out
    (toward `sign`), advancing one axis per step (Bresenham-style) so every pixel
    shares an edge with the previous one. Returns the ordered path of (y,x) points
    on the intended line (whether or not each was painted). The root (y0,x0) is
    only painted when place_root (used for the beam, which sits above the helm)."""
    path = [(y0, x0)]
    if place_root and y0 >= Y_MIN and 0 <= x0 < FW and not a[y0, x0] and fr[y0, x0, 3] == 0:
        put(fr, y0, x0, antler_tone(kind, 0, up + out, pal))
    cy, cx = y0, x0
    dy = dx = 0
    total = up + out
    for k in range(1, total + 1):
        # advance whichever axis is furthest behind its share of the diagonal
        if dx >= out or (dy < up and dy * out <= dx * up):
            cy -= 1
            dy += 1
        else:
            cx += sign
            dx += 1
        path.append((cy, cx))
        if Y_MIN <= cy < FH and 0 <= cx < FW and not a[cy, cx] and fr[cy, cx, 3] == 0:
            put(fr, cy, cx, antler_tone(kind, k, total, pal))
    return path


def draw_antler(fr, a, sign, pal):
    xr = crown_corner(a, sign)
    if xr is None or not (0 <= xr < FW):
        return
    col_ys = np.where(a[:, xr])[0]
    if col_ys.size == 0:
        return
    y0 = int(col_ys.min()) - 1             # one row above this column's top helm px
    if y0 < Y_MIN:
        return
    # near-vertical main beam; keep its path for tine roots
    beam = walk(fr, a, y0, xr, BEAM_UP, BEAM_OUT, sign, 'beam', pal, place_root=True)
    if len(beam) < 3:
        return
    # fork tines OUTWARD off beam points so they splay clear of the beam
    for frac, tup, tout in TINES:
        idx = max(1, min(int(frac * (len(beam) - 1)), len(beam) - 1))
        by, bx = beam[idx]
        walk(fr, a, by, bx, tup, tout, sign, 'tine', pal)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['antler']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():                    # empty (incl. sleep) frames skipped
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        for sign in (-1, +1):
            draw_antler(fr, a, sign, pal)
        # Connectivity guard: drop any antler pixel not 4-connected to the body.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_antler_helmet_preview'
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
