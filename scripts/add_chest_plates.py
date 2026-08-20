#!/usr/bin/env python3
"""add_chest_plates.py — Sculptural plate treatment for legendary chest sheets.

Per Matt's 7/27 sculptural-armor direction: legendary chests should read as
3D-volumed plate, not flat printed shirts. This post-pass adds, per frame:

  1. ROUNDED PAULDRON CAPS — silhouette extension outward at each shoulder
     over 4 rows in a rounded profile, colors sampled from the adjacent shirt
     pixel so the axis pattern/palette carries onto the cap, then lit as a
     plate: rim highlight on top, base mid, deep under-shadow at the bottom.
     Each cap row is closed by a near-black OUTLINE pixel on its outer edge.
     This matters: the shirt sheets carry no outline of their own (silhouette
     definition comes from the skin layer underneath), so an unoutlined
     extension overhangs the body and reads as a soft shelf rather than a
     plate. The outline restores the hard edge.
  2. UNDER-PAULDRON SHADOW — existing sleeve/torso pixels in the 2 rows
     below each cap edge darkened (plate casts a shadow on the arm).
  3. SHOULDER RIM LIGHT — top torso row brightened (light catches the
     plate's top edge).
  4. CHEST PLATE LIP — at ~55% of torso height: bright bevel row over a
     dark seam row over a mid shadow row. Reads as a thick breastplate
     lower edge overhanging the fauld/cloth below.

All tone work is multiplicative on RGB (hue-preserving), so the authored
pattern colors are retained. New pixels are placed ONLY on currently
transparent cells inside the QA box (x in [30,55], y >= 16) and always
adjacent to existing body — cannot create strays, and cannot eat the raised
arms on the cheer row or the extended arm on slash. Sleep row (frames 60-69)
is skipped (lying pose).

Torso detection is column-based: torso columns are those whose opaque pixel
count >= 50% of the max column count, which excludes thin extended arms
(slash) and raised arms (cheer).

Profiles (--profile): narrow | medium | wide  — silhouette extension per row.

Usage:
  python3 scripts/add_chest_plates.py FILE [FILE ...]   # in place
  python3 scripts/add_chest_plates.py --dry-run FILE    # stats only
"""
import sys
import numpy as np
from PIL import Image

FW, FH, COLS, NFR = 80, 64, 10, 70
QA_X0, QA_X1, QA_Y0 = 30, 55, 16

# Plate-color extension per cap row (an outline pixel is added just beyond).
# ASYMMETRIC by design: in 3/4 view the LEFT shoulder is the character's back
# side and must read as less prominent than the front-facing right one. A
# symmetric profile also spiked on the left, because the body's own left edge
# already slopes outward as it descends — a constant extension follows that
# slope out to a point, then drops 3px back when the profile ends. The back
# profile is therefore both shallower and 5 rows long, tapering 2-2-1-1-0 so
# the cap returns to the silhouette gradually instead of stepping off it.
# A back entry of 0 means "outline rim only, no plate extension" — 1px proud
# instead of 3px. That is what finally killed the spike: at 2px the cap
# overshot the body's own widest point and left a triangular tip.
PROFILES = {
    'narrow': ((0, 0, 0, 0),    (0, 0, 0, 0)),
    'medium': ((0, 0, 0, 0),    (0, 0, 0, 0)),
    'wide':   ((0, 0, 0, 0),    (0, 0, 0, 0)),
}   #          front (right)     back (left)
# Cap extension disabled: adding pixels outside the shirt silhouette caused
# frame-by-frame position shift (arm moves → cap moves → morphing artifact).
# All shading below operates on EXISTING pixels only, which is stable.
SHADE = (1.30, 1.05, 0.95, 0.70)    # RIM / BASE / MID / UNDER per cap row
OUTLINE_RGB = (12, 12, 16)          # near-black cap outline (matches the
                                    # face-outline family, not pure #000 —
                                    # sprite_qa flags lone pure-black)
# Under-pauldron cast shadow disabled (was tied to cap position, also moved).
SHADOW_RAMP = (0.88, 0.93, 0.97)
SHADOW_COLS = 0
TOP_RIM = 1.18                      # shoulder-row rim light
LIP_HI, LIP_DARK = 1.14, 0.62       # plate bottom bevel / hard seam
LIP_UNDER = (0.72, 0.86, 0.94)      # cast shadow ramp below the lip

# Metallic sheen on the breastplate (the region ABOVE the lip): a broad
# specular column at SPEC_X (light upper-right, matching sprite_shade's
# PEAK=0.55) plus a top catch, falling off into the seam so the plate reads
# as a curved metal surface.
#
# Applied as a BASE-LEVEL shift, not a multiply. A plain multiply blows out
# these already-bright sheets (V 180-230 * 1.4 all clips to 255) and the axis
# pattern disappears. Instead each pixel's deviation from the plate's mean V
# — which IS the pattern — is held constant while only the mean is moved, and
# the mean is clamped so every deviation still fits in 0..255. Pattern
# amplitude is therefore preserved exactly at any sheen strength.
SHEEN = 0.34                        # specular gain at the highlight column
SPEC_X, SPEC_SIG = 0.62, 0.20       # centre / width across torso, 0..1
SHEEN_DROP = 0.13                   # darkening toward the bottom of the plate
TOP_CATCH = 0.10                    # extra brightness on the top plate rows
EDGE_DARK = 0.07                    # barrel curvature: quadratic darkening
                                    # toward BOTH plate edges, so the
                                    # breastplate reads as a solid curved
                                    # volume rather than a flat lit panel

# Gorget shadow: the plate sits below the neck, so the rows directly under the
# neck opening are in shadow. The neck opening is found per frame as the
# transparent columns on the collar row (the V-neck gap), widened one column
# each side — geometry-driven, so it tracks every pose and neckline shape.
# Kept fairly light: this multiplies on top of the sheen result, so a deeper
# value compounds into a grey blob on the pale palettes.
NECK_SHADOW = (0.70, 0.85, 0.94)

# Plate SEPARATION (Matt 8/1, ref images): armor reads as distinct plates with
# dark seams between them, not one continuous lit surface. Added as
# multiplicative seams so the axis pattern still shows through:
#   STERNUM  — vertical seam down the breastplate centre, splitting it into
#              two pectoral plates (the single clearest cue in the refs).
#   PECT_*   — each pectoral is then modelled on its own: lit toward its outer
#              top, shaded toward the sternum and its lower edge, so the two
#              halves read as separate rounded volumes rather than one panel.
#   SHOULDER_SEAM — dark line on the body edge under each cap, detaching the
#              pauldron from the torso.
#   ABDOMEN  — banded lame line below the lip.
STERNUM_MUL = 0.52
STERNUM_OFF = 2            # px LEFT of torso centre (Matt 8/1). Enlarges the
                           # right-hand pectoral, which is the plate that
                           # should dominate.
PECT_INNER = 0.91          # shading approaching the sternum seam
PECT_LOWER = 0.88          # shading at the pectoral's lower edge
PECT_LIFT = 1.06           # lift at the pectoral's outer top
SHOULDER_SEAM = 0.68
SEAM_INSET = 0             # DISABLED: inset pixels shift with arm position each
                           # frame → morphing artifact. Set to 0 so seam only
                           # touches the silhouette edge itself (stable).
PAULDRON_LIFT = 1.09       # the enlarged pauldron face reads as raised plate
SEAM_TAIL = 0              # DISABLED: tail rows below cap also anchor to moving
                           # shoulder edge → frame-by-frame shift artifact.
# Dome shading inside the pauldron: bright toward the crown (upper, inboard),
# falling to shadow at the lower/outer rim, so the pad reads round rather than
# a flat lifted patch.
PAULDRON_CROWN = 1.16
PAULDRON_RIM = 0.74
# Horizontal lame seam across the breastplate. Matched to STERNUM_MUL so the
# two seams read as the same cut, and placed at CHEST_BAND_AT of the way down
# the pectoral — i.e. sitting just above where the lip shading begins, rather
# than up under the gorget where it crowded the collar (Matt 8/1).
CHEST_BAND = STERNUM_MUL
CHEST_BAND_AT = 1.0        # 1.0 puts the band on lip-1, one row lower
# SEPARATION VARIANTS (Matt 8/1: "future generated sprites can have varying
# separation looks so they aren't all the same"). Chosen deterministically per
# sheet from a hash of its filename, so a given sheet always regenerates
# identically but different axes get different plate breakups.
#   frac  — how far down the pectoral the sternum runs (0 = none, 1 = full)
#   band  — draw the horizontal lame seam
#   round_top — shift the sternum's top pixel 1px right for a rounded taper
# 'band_only' exists because Matt noted the rows WITHOUT a visible vertical
# line read well on their own.
# `start` is where the sternum BEGINS, as a fraction of the way down the
# pectoral. It always RUNS DOWN TO THE BAND ROW and includes it, so the
# vertical and horizontal seams always meet in a T (Matt 8/1: a short sternum
# left "2 pixels at the top" floating, not connected to the horizontal). Every
# variant keeps the band; they differ in how far up the vertical reaches.
# Matt 8/1 kept 'full' and 'band_only' and scrapped the rest (square / half /
# short — the partial-length verticals). Keeping the list structure so more can
# be added later, but only these two ship.
SEPARATION_VARIANTS = [
    ('full',      dict(start=0.0,  band=True, round_top=True)),
    ('band_only', dict(start=None, band=True, round_top=False)),
]
PLATE_EDGE = 0.72          # (unused — see note in plate_frame) dark edge on
                           # the outer 1px of each pectoral, bounding it (outer
                           # edge + sternum + gorget above + lip below)
ABDOMEN_MUL = 0.62
MAX_TORSO_W = 17                    # frame-0 bbox wider than this = winged/
                                    # cape geometry sheet -> skip whole sheet


def variant_for(path):
    """Deterministic separation variant for a sheet, from its filename.

    Same sheet always regenerates identically; different axes get different
    plate breakups so the set does not all read the same.
    """
    import hashlib, os
    base = os.path.basename(path)
    # strip the gender suffix so m/f of the same item stay consistent
    if base.endswith('_f.png'):
        base = base[:-6] + '.png'
    h = int(hashlib.md5(base.encode()).hexdigest()[:8], 16)
    return SEPARATION_VARIANTS[h % len(SEPARATION_VARIANTS)]


def _scale(px, f):
    return np.clip(px[:3].astype(np.float32) * f, 0, 255).astype(np.uint8)


def _outline_col(fr, y, x):
    """Outline color for a new cap pixel at (y,x).

    Normally OUTLINE_RGB. But if the cell abuts an existing PURE #000 outline
    pixel, use pure #000 instead. Filling a transparent cell next to a black
    pixel promotes that pixel from 'edge' to 'interior', and sprite_qa flags
    interior #000 that has no pure-black 4-neighbour — so an off-black rim
    here orphans the sheet's own outline and fails QA.
    """
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if (0 <= ny < FH and 0 <= nx < FW and fr[ny, nx, 3] > 0
                and not fr[ny, nx, :3].any()):
            return (0, 0, 0)
    return OUTLINE_RGB


def _put(fr, y, x, rgb):
    """Place a new pixel only on a transparent cell inside the QA box."""
    if not (QA_Y0 <= y < FH and QA_X0 <= x <= QA_X1):
        return 0
    if fr[y, x, 3] > 0:               # never overwrite existing body/arm
        return 0
    fr[y, x, :3] = rgb
    fr[y, x, 3] = 255
    return 1


def plate_frame(fr, profile=PROFILES['medium'], sep=None):
    """Add pauldrons + plate shading to one 64x80 RGBA frame, in place."""
    if sep is None:
        sep = SEPARATION_VARIANTS[0][1]
    op = fr[..., 3] > 0
    if not op.any():
        return 0
    added = 0
    colcnt = op.sum(axis=0)
    torso_cols = np.flatnonzero(colcnt >= 0.5 * colcnt.max())
    xl, xr = int(torso_cols.min()), int(torso_cols.max())
    if xr - xl < 6:                       # degenerate frame
        return 0

    tops = {}
    for x in (xl, xl + 1, xr - 1, xr):
        ys = np.flatnonzero(op[:, x])
        tops[x] = int(ys.min())
    sh_l = min(tops[xl], tops[xl + 1])
    sh_r = min(tops[xr - 1], tops[xr])

    torso_rows = np.flatnonzero(op[:, xl:xr + 1].any(axis=1))
    bot = int(torso_rows.max())

    # 1) pauldron caps — DISABLED: adding pixels outside the silhouette caused
    #    frame-by-frame shift (arm moves → cap anchors move → morphing artifact).
    #    All remaining shading operates on EXISTING pixels only.
    front, back = profile
    for side, edge, sh in ((-1, xl, sh_l), (1, xr, sh_r)):
        prof = back if side < 0 else front
        for dy, ext in enumerate(prof):
            if ext == 0:
                continue   # no extension → no outline pixel added
            y = sh + dy
            if y >= FH:
                continue
            row = np.flatnonzero(op[y, xl - 2:xr + 3]) + xl - 2
            if len(row) == 0:
                continue
            ax = int(row.min()) if side < 0 else int(row.max())
            src = fr[y, ax].copy()
            if src[3] == 0:
                continue
            f = SHADE[min(dy, len(SHADE) - 1)]
            for o in range(1, ext + 1):
                col = _scale(src, f * (1.0 - 0.06 * (o - 1)))
                added += _put(fr, y, ax + side * o, col)
            added += _put(fr, y, ax + side * (ext + 1),
                          _outline_col(fr, y, ax + side * (ext + 1)))
        # rounded top corner: skip entirely when caps are disabled
        # 2) under-pauldron cast shadow on existing pixels (ramped)
        for i, f in enumerate(SHADOW_RAMP):
            y = sh + len(prof) + i
            if y >= FH:
                continue
            for o in range(0, SHADOW_COLS):
                x = edge + side * o
                if 0 <= x < FW and fr[y, x, 3] > 0:
                    fr[y, x, :3] = _scale(fr[y, x], f)

    # 3) shoulder rim light on existing top torso row
    for sh, cols in ((sh_l, range(xl, xl + (xr - xl) // 2)),
                     (sh_r, range(xl + (xr - xl) // 2, xr + 1))):
        for x in cols:
            if fr[sh, x, 3] > 0:
                fr[sh, x, :3] = _scale(fr[sh, x], TOP_RIM)

    # 4) metallic sheen on the breastplate — everything above the lip.
    #    Applied BEFORE the lip rows so the seam stays the darkest line.
    sh_top = min(sh_l, sh_r)
    lip = sh_top + max(4, int(round(0.55 * (bot - sh_top))))
    y0, y1 = sh_top, lip - 1
    x0, x1 = max(0, xl), min(FW, xr + 1)
    if y1 > y0 and x1 > x0:
        reg = fr[y0:y1, x0:x1]
        m = reg[..., 3] > 0
        if m.sum() >= 4:
            rgbf = reg[..., :3].astype(np.float32)
            v = rgbf.max(axis=-1)
            mean_v = float(v[m].mean())
            dev = v - mean_v                    # the pattern, held constant

            ny = ((np.arange(y0, y1) - sh_top) /
                  max(1, y1 - y0))[:, None]     # 0 top of plate, 1 at seam
            nx = ((np.arange(x0, x1) - xl) /
                  max(1, xr - xl))[None, :]
            spec = np.exp(-((nx - SPEC_X) ** 2) / (2 * SPEC_SIG ** 2))
            f = ((1.0 - SHEEN_DROP * ny) *
                 (1.0 + SHEEN * spec * (1.0 - 0.5 * ny)))
            f = f + np.where(ny < 0.25, TOP_CATCH, 0.0)
            # barrel curvature: quadratic falloff toward both plate edges
            f = f - EDGE_DARK * (2.0 * np.abs(nx - 0.5)) ** 2

            # Fit the base into the headroom left by the pattern deviations.
            # Clipping here would flatten the sheen on already-pale sheets
            # (every value pinned to the cap = no gradient), so instead the
            # base's swing around the mean is COMPRESSED by a single factor.
            # The specular gradient keeps its shape, just at lower contrast.
            lo = max(0.0, -float(dev[m].min()))
            hi = max(lo, 255.0 - float(dev[m].max()))
            base = mean_v * f
            k = 1.0
            top = float(base.max()) - mean_v
            bot = mean_v - float(base.min())
            if top > 1e-6:
                k = min(k, max(0.0, hi - mean_v) / top)
            if bot > 1e-6:
                k = min(k, max(0.0, mean_v - lo) / bot)
            base = mean_v + (base - mean_v) * k
            v_new = np.clip(base + dev, 0.0, 255.0)

            scale = np.where(v > 0, v_new / np.maximum(v, 1e-9), 1.0)
            out = np.clip(rgbf * scale[..., None], 0, 255).astype(np.uint8)
            reg[..., :3] = np.where(m[..., None], out, reg[..., :3])

    # 5) gorget shadow — the plate sits below the neck, so the rows under the
    #    neck opening are shaded. The opening is the run of transparent
    #    columns on the collar row (the V-neck gap); if the collar row is
    #    solid, fall back to the middle third of the torso.
    #    Only the run NEAREST THE TORSO CENTRE counts: the collar row is also
    #    transparent out at the sloping shoulder edges, and taking min/max of
    #    all gaps spanned the whole torso and greyed out the entire chest.
    gap = [x for x in range(xl, xr + 1) if fr[sh_top, x, 3] == 0]
    runs = []
    for x in gap:
        if runs and x == runs[-1][-1] + 1:
            runs[-1].append(x)
        else:
            runs.append([x])
    mid = (xl + xr) / 2.0
    runs = [r for r in runs if r[0] > xl and r[-1] < xr]     # not an edge slope
    if runs:
        r = min(runs, key=lambda r: abs((r[0] + r[-1]) / 2.0 - mid))
        nx0, nx1 = r[0] - 1, r[-1] + 1
    else:
        w = xr - xl
        nx0, nx1 = xl + w // 3, xr - w // 3
    for i, f in enumerate(NECK_SHADOW):
        y = sh_top + 1 + i
        if not (0 <= y < FH) or y >= lip - 1:
            break
        for x in range(nx0, nx1 + 1):
            if 0 <= x < FW and fr[y, x, 3] > 0:
                fr[y, x, :3] = _scale(fr[y, x], f)

    # Snapshot the plate AFTER sheen + gorget but BEFORE any plate toning.
    # Both seams are derived from this in step 7 so they match each other.
    snap = fr[:, :, :3].copy()

    # 5b) PLATE SEPARATION — pectorals, sternum, shoulder seam, abdomen band
    pect_top = sh_top + len(NECK_SHADOW)        # below the gorget
    cx = max(xl + 1, (xl + xr) // 2 - STERNUM_OFF)

    def torso_run(y):
        """(x0, x1) of the contiguous opaque run containing the torso centre.

        Everything here must be clipped to this run, NOT to xl..xr. At the
        lower chest rows the torso and the arm are separate runs with a
        transparent gap between them, so a blind xl..xr sweep jumped the gap
        and drew the seam straight across the arm.
        """
        if not (0 <= y < FH) or not op[y, cx]:
            return None
        x0 = cx
        while x0 - 1 >= 0 and op[y, x0 - 1]:
            x0 -= 1
        x1 = cx
        while x1 + 1 < FW and op[y, x1 + 1]:
            x1 += 1
        return x0, x1

    if lip - 1 > pect_top:
        # per-pectoral modelling: lit outer-top, shaded toward sternum + base
        for y in range(pect_top, lip - 1):
            run = torso_run(y)
            if run is None:
                continue
            ty = (y - pect_top) / max(1, (lip - 2) - pect_top)   # 0 top, 1 base
            for x in range(run[0], run[1] + 1):
                if fr[y, x, 3] == 0 or x == cx:
                    continue
                inner = 1.0 - abs(x - cx) / max(1, (xr - xl) / 2.0)   # 1 at seam
                f = (1.0 + PECT_LIFT * (1.0 - inner) * (1.0 - ty) * 0.5)
                f *= (1.0 - (1.0 - PECT_INNER) * inner)
                f *= (1.0 - (1.0 - PECT_LOWER) * ty ** 2)
                fr[y, x, :3] = _scale(fr[y, x], f)

        # (No outer plate edge. Darkening the outermost column of every chest
        # row drew a long dark streak down the sleeve on sheets where torso
        # and sleeve are one contiguous run — the mage "arm line". It was also
        # redundant: the plate's outer boundary is already the body
        # silhouette, which the skin layer outlines. Plates stay bounded by
        # sternum inboard, gorget above and band/lip below.)

    # shoulder seam: detach each pauldron from the torso.
    # SKIP entirely when caps are disabled — the seam anchors to the
    # arm-silhouette edge which moves per frame, causing the same artifact.
    _caps_enabled = any(e > 0 for e in front) or any(e > 0 for e in back)
    for side, sh in ((-1, sh_l), (1, sh_r)) if _caps_enabled else ():
        prof = back if side < 0 else front
        inset = SEAM_INSET if side > 0 else 0
        nrows = len(prof) + SEAM_TAIL          # tail closes the pad's bottom
        for dy in range(nrows):
            y = sh + dy
            if not (0 <= y < FH):
                continue
            row = np.flatnonzero(op[y, xl - 2:xr + 3]) + xl - 2
            if len(row) == 0:
                continue
            ax = int(row.min()) if side < 0 else int(row.max())
            sx = ax - side * inset
            # dome the pad interior: bright at the crown (upper rows, inboard),
            # shading to the lower/outer rim so it reads round, not flat
            ty = dy / max(1, nrows - 1)
            for o in range(1, inset + 1):
                px = sx + side * o
                if not (0 <= px < FW and fr[y, px, 3] > 0):
                    continue
                tx = o / max(1, inset)          # 0 inboard, 1 at outer rim
                d = max(ty, tx * 0.8)
                f = PAULDRON_CROWN + (PAULDRON_RIM - PAULDRON_CROWN) * d ** 1.4
                fr[y, px, :3] = _scale(fr[y, px], f)
            if 0 <= sx < FW and fr[y, sx, 3] > 0:
                fr[y, sx, :3] = _scale(fr[y, sx], SHOULDER_SEAM)

    # abdomen: one banded lame line below the lip's cast shadow
    ab = lip + 1 + len(LIP_UNDER)
    if ab < bot:
        run = torso_run(ab)
        if run:
            for x in range(run[0], run[1] + 1):
                if fr[ab, x, 3] > 0:
                    fr[ab, x, :3] = _scale(fr[ab, x], ABDOMEN_MUL)

    # 6) chest plate lip: bevel / hard seam / ramped cast shadow below
    rows = [(lip - 1, LIP_HI), (lip, LIP_DARK)]
    rows += [(lip + 1 + i, f) for i, f in enumerate(LIP_UNDER)]
    for y, f in rows:
        if not (0 <= y < FH):
            continue
        run = torso_run(y)                  # clip: never jump the gap onto
        if run is None:                     # a detached arm (same bug class
            continue                        # as the chest band did)
        for x in range(run[0], run[1] + 1):
            if fr[y, x, 3] > 0:
                fr[y, x, :3] = _scale(fr[y, x], f)

    # 7) SEAMS LAST, from a common snapshot.
    #
    # The sternum and the horizontal band must read as the same cut. Drawing
    # them inline did not achieve that even with an identical multiplier,
    # because each was multiplying a different accumulated base: the sternum
    # column is skipped by the pectoral pass (so it was raw x MUL), while the
    # band row had already been darkened by PECT_LOWER and then by LIP_HI.
    # Same constant, visibly different result — and their intersection got
    # squared. Both are now taken from `snap`, the plate state before any
    # seam or lip toning, so they are guaranteed to match and the crossing
    # pixel is written once.
    if lip - 1 > pect_top:
        bandy = min(lip - 1,
                    pect_top + max(1, int(round(CHEST_BAND_AT *
                                                ((lip - 1) - pect_top)))))
        # Sternum: starts where the variant says, always runs DOWN TO AND
        # INCLUDING bandy so it meets the horizontal seam. Its TOP pixel steps
        # 1px right so the seam tapers instead of butting square (Matt).
        if sep['start'] is not None:
            top_y = pect_top + int(round(sep['start'] * (bandy - pect_top)))
            for y in range(top_y, bandy + 1):
                sx = cx + 1 if (sep['round_top'] and y == top_y) else cx
                if 0 <= sx < FW and fr[y, sx, 3] > 0:
                    fr[y, sx, :3] = _scale(snap[y, sx], STERNUM_MUL)
        if sep['band']:
            run = torso_run(bandy)
            if run and pect_top < bandy <= lip - 1:
                for x in range(run[0], run[1] + 1):
                    if fr[bandy, x, 3] > 0:
                        fr[bandy, x, :3] = _scale(snap[bandy, x], CHEST_BAND)
    return added


def plate_sheet(arr, profile=PROFILES['medium'], sep=None):
    """Apply to all frames except sleep row 6. Returns total pixels added."""
    fr0 = arr[:FH, :FW]
    xs = np.argwhere(fr0[..., 3] > 0)
    if len(xs) and (xs[:, 1].max() - xs[:, 1].min() + 1) > MAX_TORSO_W:
        return -1                       # winged/cape geometry — do not plate
    total = 0
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        if r == 6:                      # sleep row: lying pose, skip
            continue
        total += plate_frame(arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW],
                             profile, sep)
    return total


def main(argv):
    dry = '--dry-run' in argv
    prof = PROFILES['medium']
    for a in argv:
        if a.startswith('--profile='):
            prof = PROFILES[a.split('=', 1)[1]]
    files = [a for a in argv if not a.startswith('--')]
    for f in files:
        arr = np.array(Image.open(f).convert('RGBA'))
        vname, sep = variant_for(f)
        n = plate_sheet(arr, prof, sep)
        if n < 0:
            print(f"{f}: SKIP (wide geometry sheet — wings/cape)")
            continue
        print(f"{f}: +{n} pauldron px  [{vname}]")
        if not dry:
            Image.fromarray(arr).save(f)


if __name__ == '__main__':
    main(sys.argv[1:])
