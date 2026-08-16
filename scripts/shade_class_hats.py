#!/usr/bin/env python3
"""shade_class_hats.py — Fold + volume shading for mage and ranger class hats.

Matt 8/1: the class hats read flat — one green (ranger) or one purple (mage)
mass with no structure. The ranger cap in particular should read as a Robin
Hood hat, which is defined by its FOLDS: a turned-up brim catching light, a
dark crease where the crown overhangs that brim, and a domed crown.

Measured starting point (helmet_ranger2, frame 0): the hat is only SIX rows
tall (y=18..23) and ~10 wide, and carries just two tones — a mid green crown
and a marginally darker bottom row. There is no room for a literal folded
brim, so the fold is implied tonally instead:

  BRIM      bottom rows, LIFTED — the turned-up cuff faces up into the light
  CREASE    the row directly above the brim, DARKENED — the crown's overhang
            casts onto the brim. This single dark row is what actually sells
            the fold; without it the lifted brim just looks like a lighter hat.
  CROWN     everything above, given a dome gradient (specular slightly right
            of centre, matching sprite_shade's light and the chest sheen) plus
            a vertical falloff so the crown turns away at its base.

Protected: the outline, and any pixel whose hue is far from the hat's dominant
hue — that keeps the gold/white feather and any trim untouched.

All tone work is multiplicative on RGB, so hue and any authored pattern
survive. No pixel is added or removed, so the silhouette is untouched and the
operation is QA-safe by construction.

Usage:
  python3 scripts/shade_class_hats.py FILE [FILE ...] [--out DIR]
"""
import os
import sys
import numpy as np
from PIL import Image

FW, FH, COLS, NFR = 80, 64, 10, 70
OUTLINE_SUM = 120          # below this = outline, never shaded
HUE_TOL = 46               # max hue distance (deg) from the hat's dominant
                           # hue before a pixel counts as trim (feather, band)

BRIM_LIFT = 1.30           # turned-up cuff catches the light
CREASE_MUL = 0.58          # crown's overhang shadow onto the brim
CROWN_SPEC = 0.26          # dome highlight gain
CROWN_X = 0.60             # highlight centre across the hat, 0..1
CROWN_SIG = 0.30
CROWN_DROP = 0.20          # crown darkens toward its base


def _hue(rgb):
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx = rgb.max(-1)
    mn = rgb.min(-1)
    d = np.maximum(mx - mn, 1e-6)
    h = np.zeros(mx.shape, np.float32)
    m = mx == r
    h[m] = ((g - b)[m] / d[m]) % 6
    m = mx == g
    h[m] = ((b - r)[m] / d[m]) + 2
    m = mx == b
    h[m] = ((r - g)[m] / d[m]) + 4
    return (h * 60.0) % 360.0


def _hue_dist(a, b):
    d = np.abs(a - b) % 360.0
    return np.minimum(d, 360.0 - d)


def shade_frame(fr, brim_h=2):
    """Shade one 64x80 RGBA hat frame in place. Returns pixels touched."""
    op = fr[..., 3] > 0
    if not op.any():
        return 0
    rgb = fr[..., :3].astype(np.float32)
    body = op & (rgb.sum(-1) >= OUTLINE_SUM)
    if body.sum() < 6:
        return 0

    # dominant hue = hue of the most common body color; trim is excluded
    cols, counts = np.unique(fr[body][:, :3], axis=0, return_counts=True)
    dom = _hue(cols[counts.argmax()].astype(np.float32)[None, None, :])[0, 0]
    body &= _hue_dist(_hue(rgb), dom) <= HUE_TOL
    if body.sum() < 6:
        return 0

    rows = np.flatnonzero(body.any(1))
    top, bot = int(rows.min()), int(rows.max())
    if bot - top < 2:
        return 0
    # The brim starts at the WIDEST body row, not simply the bottom rows.
    # On the ranger cap those coincide, but a wizard hat's bottom rows are the
    # narrow tips of its flare — anchoring on width lifts the actual brim on
    # both silhouettes instead of a couple of stray tip pixels.
    widths = body.sum(1)
    brim_top = int(np.argmax(widths))
    if brim_top <= top:
        brim_top = max(top + 1, bot - brim_h + 1)
    crease = brim_top - 1

    xs = np.flatnonzero(body.any(0))
    x0, x1 = int(xs.min()), int(xs.max())
    span = max(1, x1 - x0)

    n = 0
    for y in range(top, bot + 1):
        for x in range(x0, x1 + 1):
            if not body[y, x]:
                continue
            if y >= brim_top:
                f = BRIM_LIFT
            elif y == crease:
                f = CREASE_MUL
            else:
                nx = (x - x0) / span
                ny = ((y - top) / max(1, crease - top)) if crease > top else 0.0
                spec = np.exp(-((nx - CROWN_X) ** 2) / (2 * CROWN_SIG ** 2))
                f = (1.0 - CROWN_DROP * ny) * (1.0 + CROWN_SPEC * spec)
            fr[y, x, :3] = np.clip(rgb[y, x] * f, 0, 255).astype(np.uint8)
            n += 1
    return n


def shade_sheet(arr, brim_h=2):
    total = 0
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        total += shade_frame(arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW],
                             brim_h)
    return total


def main(argv):
    out_dir = None
    if '--out' in argv:
        i = argv.index('--out')
        out_dir = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    files = [a for a in argv if not a.startswith('--')]
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    for f in files:
        arr = np.array(Image.open(f).convert('RGBA'))
        n = shade_sheet(arr)
        dst = os.path.join(out_dir, os.path.basename(f)) if out_dir else f
        Image.fromarray(arr).save(dst)
        print(f"{os.path.basename(f)}: shaded {n} px -> {dst}")


if __name__ == '__main__':
    main(sys.argv[1:])
