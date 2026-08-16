#!/usr/bin/env python3
"""carve_face_openings.py — Carve a horizontal eye SLIT into helmet sheets.

Supersedes apply_helmet_eye_slit.py for general use. That script copied
helmet_2's authored face GRILLE — a fixed pattern of vertical bars that does
not correspond to where the eyes actually sit. This script instead anchors the
slit to the SKIN sheet's own head geometry, which is already drawn correctly
for the 3/4 angle in every pose.

Slit style (Matt, 8/1): a single horizontal slit, matching the currently
deployed closed helms. No eyebrows, no mouth opening. Reference rows, frame 0:

  helmet_2  y=26  ....#####ooo#.....
  helmet_3  y=26  ....########......
  helmet_4  y=26  .........ooo#.....   (slit clipped by its own visor shape)

How the slit is placed
----------------------
Per frame, on the gender-matched skin sheet:

  head_top  = topmost opaque row of the head column span
  slit row  = head_top + EYE_ROW (5)
      frame 0 male: head_top=21 -> row 26; female head_top=22 -> row 27, per
      SPRITE_SPEC §2. Verified to hold on run row 2 (head_top=20 -> row 25)
      and slash row 5, so the relative anchor tracks the head through every
      pose and x-shift with no per-pose table.

  The slit spans the head's INTERIOR pixels on that row — opaque and not
  touching transparency. Excluding boundary pixels stops the slit one pixel
  inside the silhouette rather than eating the head's outline.

The resulting per-frame mask is repainted near-black on the helmet, ONLY
where the helmet is already opaque. No pixel is added outside the helmet
silhouette, so the operation is QA-safe by construction: it cannot create
strays or bleed — and each helmet's own visor shape clips the slit naturally.

Self-limiting on open headgear: wizard hats, hoods and circlets have no
opaque pixels over the eyes, so nothing is carved on them.

Usage:
  python3 scripts/carve_face_openings.py FILE [FILE ...]
  python3 scripts/carve_face_openings.py --dry-run FILE
  python3 scripts/carve_face_openings.py --preview OUT.png FILE   # zoom check
"""
import sys
import numpy as np
from PIL import Image

CH = "sprites/preview_assets/char"
FW, FH, COLS, NFR = 80, 64, 10, 70
SLIT_RGB = (16, 14, 18)      # near-black opening interior
EYE_ROW = 5                  # slit row, relative to head_top (frame 0 male:
                             # head_top=21 -> eye row 26, per SPRITE_SPEC §2;
                             # female head_top=22 -> 27. Same +5 offset.)
SLIT_ROWS = 1                # slit height; deployed helms (helmet_2/3/4) all
                             # use a single row — see module docstring
SLIT_EXTEND_L = 1            # px the slit reaches further left (face side)
SLIT_INSET = 1               # px of helmet left standing each side of the
                             # slit, so it is framed rather than cutting the
                             # dome clean in half
HEAD_X0, HEAD_X1 = 30, 56    # head can shift within this span across poses

# Visor relief. The generated dome helmets carry NO outline of their own —
# unlike the deployed helms (helmet_2/3/4), every one of which rims the whole
# silhouette in near-black. Without that frame a dark slit floats in a solid
# bright dome and reads as a mail slot. So the rework adds:
#   OUTLINE_MUL — darken the helmet's boundary ring (opaque pixels touching
#     transparency). Multiplicative, so it is a very dark version of the
#     armor's own hue rather than flat black, and the silhouette is unchanged
#     because existing pixels are re-toned, not added.
#   BROW_MUL / CHEEK_MUL — shade the row above the slit and light the row
#     below it, so the opening reads as recessed under a brow ridge.
OUTLINE_MUL = 0.26
# ...but a pure multiply gives an UNEVEN rim: a bright edge pixel (RGB sum 450)
# lands at ~117, which reads as mid-grey rather than outline, while an already
# dark one goes properly black. That grey fringe is what Matt saw as "extra
# grey pixels on the left side of the outline". Clamp every rim pixel to at
# most OUTLINE_MAX_SUM so the ring is uniformly dark regardless of what it
# started from (still hue-preserving — RGB is scaled, not replaced).
OUTLINE_MAX_SUM = 95
BROW_MUL = 0.55
CHEEK_MUL = 1.16

# Full visor relief (dark rim + brow/cheek) only suits helmets that already
# carry authored dark structure — an actual visor/outline in the source art.
# On smooth, densely patterned domes the near-black rim eats the design and the
# result reads as mud (Matt 8/1: "several sprites got mangled ... blending with
# the legendary colored rare sets"). Measured on his own examples:
#     usable   legendary14 .231  legendary9 .242  legendary6 .295  legendary7 .363
#     mangled  legendary30 .077  legendary25 .154  legendary36 .165  l18 .176
# so the threshold sits in the gap. Below it a sheet gets a PLAIN slit and no
# rim/brow/cheek, which preserves the pattern and still opens the eyes.
RELIEF_MIN_DARKFRAC = 0.20
_DF_Y0, _DF_Y1, _DF_X0, _DF_X1 = 18, 32, 32, 50


def dark_structure(arr):
    """Fraction of the frame-0 head area that is authored dark structure."""
    reg = arr[_DF_Y0:_DF_Y1, _DF_X0:_DF_X1]
    op = reg[..., 3] > 0
    if op.sum() < 40:
        return 0.0
    lum = reg[..., :3].astype(int).sum(-1)
    return float(((lum < 210) & op).sum()) / float(op.sum())

# VISOR VARIANTS (Matt 8/1) — the same idea as the chest SEPARATION_VARIANTS:
# helmets should not all carry an identical opening. Chosen deterministically
# per sheet from a hash of its filename.
#   breath  — horizontal breath slit BREATH_ROW below the eye row (mouth slit)
#   nasal   — a 1px nasal bar of helmet left standing at the face centre,
#             splitting the eye slit into two openings
#   grille  — breath row cut as short vertical vents instead of one slit
BREATH_ROW = 2               # rows below the eye slit; +2 leaves a solid cheek
                             # row between, which reads as a helm rather than
                             # merging into one tall hole
BREATH_INSET = 1             # breath slit is narrower than the eye slit
VISOR_VARIANTS = [
    ('slit',   dict(breath=False, nasal=False, grille=False)),
    ('breath', dict(breath=True,  nasal=False, grille=False)),
    ('nasal',  dict(breath=False, nasal=True,  grille=False)),
    ('grille', dict(breath=True,  nasal=False, grille=True)),
    ('great',  dict(breath=True,  nasal=True,  grille=False)),
]


def variant_for(path):
    """Deterministic visor variant for a helmet sheet, from its filename.

    Mirrors add_chest_plates.variant_for: same sheet always regenerates
    identically, and the `_f` suffix is stripped so male/female of the same
    helmet get the same visor.
    """
    import hashlib
    import os
    base = os.path.basename(path)
    if base.endswith('_f.png'):
        base = base[:-6] + '.png'
    h = int(hashlib.md5(base.encode()).hexdigest()[:8], 16)
    return VISOR_VARIANTS[h % len(VISOR_VARIANTS)]


_CACHE = {}


def _load(p):
    return np.array(Image.open(p).convert("RGBA"))


def face_mask(gender='m', var=None):
    """Per-frame boolean mask of the visor opening, from the skin sheet."""
    if var is None:
        var = VISOR_VARIANTS[0][1]
    key = (('f' if gender == 'f' else 'm'),
           var['breath'], var['nasal'], var['grille'])
    if key in _CACHE:
        return _CACHE[key]
    skin = _load(f"{CH}/skin_{'f' if gender == 'f' else 'm'}1.png")
    m = np.zeros(skin.shape[:2], bool)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        fr = skin[sl]
        op = fr[..., 3] > 0
        if not op.any():
            continue
        # head_top: topmost opaque row anywhere in the head x-span
        band = op[:, HEAD_X0:HEAD_X1]
        rows = np.flatnonzero(band.any(axis=1))
        if len(rows) == 0:
            continue
        head_top = int(rows.min())

        # Interior = opaque and not touching transparency (4-neighborhood).
        # This excludes the head OUTLINE, so the slit stops cleanly one pixel
        # inside the silhouette instead of eating the head's edge.
        pad = np.pad(op, 1, constant_values=False)
        touches_bg = ~(pad[:-2, 1:-1] & pad[2:, 1:-1] &
                       pad[1:-1, :-2] & pad[1:-1, 2:])
        interior = op & ~touches_bg

        win = np.zeros_like(op)
        y0 = head_top + EYE_ROW
        win[y0:min(y0 + SLIT_ROWS, FH), HEAD_X0:HEAD_X1] = True
        # Span the slit across the actual FACIAL FEATURES, not the whole head
        # interior. The head is drawn in 3/4 facing LEFT: the face occupies the
        # left of the skull and the right side is the receding back of the head
        # (frame 0, eye row: features at x=37..41, plain skull at x=42..43).
        # Taking the full interior therefore ran the slit around the side of
        # the head — the "wrong direction" read. Using the feature extent makes
        # the slit sit on the face and lean correctly in every pose for free.
        dark = op & (fr[..., :3].astype(int).sum(-1) < 200)
        feat = dark & interior & win
        band = np.zeros_like(op)
        for yy in range(y0, min(y0 + SLIT_ROWS, FH)):
            xs = np.flatnonzero(feat[yy])
            if len(xs) == 0:
                xs = np.flatnonzero(interior[yy] & win[yy])
                if len(xs) == 0:
                    continue
                xs = xs[SLIT_INSET:len(xs) - SLIT_INSET] if len(xs) > 2 * SLIT_INSET else xs
                if len(xs) == 0:
                    continue
            # extend 1px further LEFT (Matt 8/1) — the face side, so the slit
            # reaches the far edge of the visor rather than stopping short of it
            lo = max(0, xs.min() - SLIT_EXTEND_L)
            hi = xs.max()
            band[yy, lo:hi + 1] = True
            # nasal bar: leave 1px of helmet standing at the eye slit's centre,
            # splitting it into two openings
            if var['nasal'] and hi - lo >= 4:
                band[yy, (lo + hi) // 2] = False
            # breath / mouth slit, BREATH_ROW below and inset each side
            if var['breath']:
                by = yy + BREATH_ROW
                b0, b1 = lo + BREATH_INSET, hi - BREATH_INSET
                if by < FH and b1 > b0:
                    if var['grille']:
                        # short vertical vents instead of one continuous slit
                        for bx in range(b0, b1 + 1, 2):
                            band[by, bx] = True
                    else:
                        band[by, b0:b1 + 1] = True
        # Masked by `op` (head opaque), not `interior`: the extension pixel is
        # the head's own boundary, which `interior` excludes — that is why a
        # naive +1 did nothing. Carving it is safe because the mask is applied
        # only where the HELMET is opaque, and the helmet's outline ring sits
        # a further pixel out at its own silhouette.
        m[sl] = band & op
    _CACHE[key] = m
    return m


def _mul(out, m, f):
    """Multiply RGB of the masked pixels by f (hue-preserving)."""
    if not m.any():
        return
    v = out[m][:, :3].astype(np.float32) * f
    out[m, 0], out[m, 1], out[m, 2] = (np.clip(v, 0, 255).astype(np.uint8).T)


def _rim(out, m):
    """Darken the outline ring to a UNIFORM dark value (hue-preserving).

    Uses min(OUTLINE_MUL, OUTLINE_MAX_SUM/lum) per pixel, so bright edge
    pixels are pulled down as far as dark ones instead of stopping at grey.
    """
    if not m.any():
        return
    px = out[m][:, :3].astype(np.float32)
    lum = np.maximum(px.sum(1, keepdims=True), 1.0)
    f = np.minimum(OUTLINE_MUL, OUTLINE_MAX_SUM / lum)
    out[m, 0], out[m, 1], out[m, 2] = np.clip(px * f, 0, 255).astype(np.uint8).T


def _boundary(op):
    """Opaque pixels touching transparency (4-neighborhood) — the outline ring."""
    pad = np.pad(op, 1, constant_values=False)
    return op & ~(pad[:-2, 1:-1] & pad[2:, 1:-1] &
                  pad[1:-1, :-2] & pad[1:-1, 2:])


def carve(arr, gender='m', relief=True, var=None, rim=False):
    """Return (new_arr, n_px): visor slit carved where the helmet is opaque.

    With relief=True also rims the helmet in a dark outline and shades a brow
    above / catches light below the slit, so the opening reads as a recessed
    visor instead of a bar floating in a solid dome.
    """
    out = arr.copy()
    if var is None:
        var = VISOR_VARIANTS[0][1]
    mask = face_mask(gender, var)
    if mask.shape != out.shape[:2]:
        raise ValueError("sheet size mismatch with skin reference")
    op = out[..., 3] > 0
    apply = mask & op

    if relief and apply.any():
        # dark outline ring — only on frames whose helmet actually covers the
        # eye row, so open headgear (hats, hoods) is left untouched
        active = np.zeros(out.shape[:2], bool)
        for fi in range(NFR):
            r, c = fi // COLS, fi % COLS
            sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
            if apply[sl].any():
                active[sl] = True
        # The full-silhouette dark rim is OFF by default (rim=False). It was
        # the destructive step: darkening the entire helmet boundary swamped
        # coloured and patterned domes (Matt 8/1 "jumbled messes"). The visor
        # proper is just the black eye/mouth pixels plus their LOCAL brow and
        # cheek shading, which is safe on any design.
        if rim:
            _rim(out, _boundary(op) & active)
        # brow above / cheek catch below, inside the helmet only
        up = np.zeros_like(mask)
        up[:-1, :] = mask[1:, :]
        dn = np.zeros_like(mask)
        dn[1:, :] = mask[:-1, :]
        _mul(out, up & op & ~mask, BROW_MUL)
        _mul(out, dn & op & ~mask, CHEEK_MUL)

    out[apply, 0], out[apply, 1], out[apply, 2] = SLIT_RGB
    out[apply, 3] = 255
    return out, int(apply.sum())


def main(argv):
    dry = '--dry-run' in argv
    prev = None
    if '--preview' in argv:
        prev = argv[argv.index('--preview') + 1]
        argv = [a for i, a in enumerate(argv)
                if i not in (argv.index('--preview'), argv.index('--preview') + 1)]
    files = [a for a in argv if not a.startswith('--')]
    tot = 0
    for f in files:
        gender = 'f' if f[:-4].endswith('_f') else 'm'
        vname, var = variant_for(f)
        arr = _load(f)
        fixed, n = carve(arr, gender, var=var)
        tot += n
        print(f"{'[dry] ' if dry else ''}carved {n:4d} px  ({gender})  [{vname}]  {f}")
        if prev:
            skin = Image.open(f"{CH}/skin_{gender}1.png").convert("RGBA")
            tiles = []
            for fi in (0, 22, 52):
                r, c = fi // COLS, fi % COLS
                for src in (arr, fixed):
                    b = skin.crop((c * FW, r * FH, (c + 1) * FW, (r + 1) * FH)).copy()
                    b.alpha_composite(Image.fromarray(
                        src[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]))
                    tiles.append(b.crop((30, 14, 56, 40)))
            Z = 10
            out = Image.new('RGBA', (len(tiles) * (26 * Z + 6) + 6, 26 * Z + 12),
                            (28, 28, 32, 255))
            for i, t in enumerate(tiles):
                out.paste(t.resize((26 * Z, 26 * Z), Image.NEAREST),
                          (6 + i * (26 * Z + 6), 6))
            out.save(prev)
            print(f"  preview: {prev}  (idle/run/slash, before|after pairs)")
        if not dry:
            Image.fromarray(fixed).save(f)
    print(f"total {tot} px across {len(files)} sheets")


if __name__ == '__main__':
    main(sys.argv[1:])
