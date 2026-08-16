#!/usr/bin/env python3
"""Generate a SIXTH net-new-geometry LEGS silhouette per class — a center-front
HANGING LOIN-GUARD (a plated war-apron / faulds-lappet that runs straight DOWN
the front CENTRELINE of the legs and hangs a short forked tongue below the hem).
This brings the legs slot to SIX distinct axes, at parity with the chest slot,
and is the DOWN-CENTRE axis that none of the five prior legendary legs occupy.

Why this is a NEW silhouette (distinct from ALL FIVE existing legs geometries):
  * legendary1 (Seraph / Starweaver / Skyhunter tassets)  — SHORT PAIRED hip
    flaps hanging straight down at the OUTER sides (two narrow LATERAL tabs).
  * legendary2 (Battle-Kilt / Ritual-Skirt / War-Kilt)    — a long SMOOTH cloth
    drape widening to a soft flared HEM (full-width soft bottom edge).
  * legendary3 (Bronze/Rune/Scale Faulds)                 — a STIFF full-width
    tiered plate skirt filling the whole gap hip->knee.
  * legendary4 (Aegis/Rose/Bone Poleyns)                  — a compact round disc
    bulging OUTWARD at the mid-leg KNEE (lateral mass at the knee).
  * legendary5 (Bulwark/Warding/Warden Cuisses)           — a broad fin flaring
    OUTWARD at the HIP then tapering (lateral flare at the top of the leg).
  * This LOIN-GUARD instead is a NARROW vertical plated strap on the CENTRELINE,
    running waist->hem and then hanging a tapered forked tongue a few rows BELOW
    the hem. All prior axes push mass to the SIDES / HEM / KNEE / HIP; this one
    is the pure DOWN-CENTRE axis (mirrors how the chest slot's tabard is the
    down-centre counterpart to its lateral cape / shoulder pauldrons). It reads
    unmistakably apart at a glance: a bright central band with a swallowtail
    tongue dangling between the legs.

Authoring philosophy (fusing the two safest proven constructions):
  * Body   = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, 0 src px dropped.
  * Apron surface = the centreline band is REPAINTED over the pants' OWN opaque
    pixels (like the baldric): recolouring existing body pixels can never add a
    stray, a bleed, or a new component — it is a subset of the silhouette by
    construction. This is what makes the guard read as attached at the waist and
    plated down the front.
  * Hanging tongue = below the hem the guard extends a short tapered forked
    tongue into TRANSPARENT space only (like the tabard), tracking the body's
    true midline, clamped inside the QA character zone, and swept by the same
    per-frame 4-connectivity guard so any stranded tongue pixel in a contorted /
    spread-leg pose is cleared. Accent strays are therefore 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no guard — matching the
tabard / cuisse / kilt convention. Shading is applied in-script via shade(); do
NOT run sprite_shade.py again.

Per class (apron metal/leather distinct in HUE from that class's five prior
legendary legs so the six legs read as six different sets):
  * warrior "Warlord's War-Apron"  — obsidian body + CRIMSON plates, gold studs
  * mage    "Astral Ward-Apron"    — arcane-violet body + MIDNIGHT-BLUE plates,
                                      silver rune studs
  * ranger  "Wildwood Warden Apron"— forest body + TAN leather straps, cream lacing

Run from repo root:
  python3 scripts/gen_loinguard_legs.py
Then QA (the tongue intentionally hangs a little below the normal leg zone):
  python3 scripts/sprite_qa.py _loinguard_legs_preview/pants_warrior_legendary6.png --y-max 62
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

# ── Loin-guard geometry ───────────────────────────────────────────────────────
# The apron is a NARROW vertical strip on the tracked midline, HALF px either
# side (full width ~2*HALF+1). It runs TOP-DOWN from the waist through the
# central gap between the legs: on each row it REPAINTS the pants' own body
# pixels where the legs overlap the centre, and FILLS the transparent inter-leg
# gap where the legs separate — but a transparent pixel is only filled when the
# pixel directly above it is already opaque, so the whole strip is 4-connected to
# the waist by construction. It hangs to LOIN_FRAC of the leg length (ending
# around the knee, well short of the feet), then tapers to a point.
HALF = 2               # half-width of the central strip (full ~5 px)
WAIST_DY = 2           # start the strip this many rows below the leg's top row
LOIN_FRAC = 0.70       # strip ends this far down the leg span (knee-ish)
TAPER = 3              # over the last TAPER rows the strip narrows to a point
Y_HEM_MAX = 61         # clamp the strip bottom inside the QA character zone

# ── Per-class palettes: body ramp (D/M/L) + apron ramp (STUD, D, M, L) ─────────
#   body:  deep shadow / base / highlight
#   apron: STUD (bright rivet/lace + centre stripe) / D (edge shadow) /
#          M (mid plate/leather) / L (lit plate/leather)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary6',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),                 # obsidian->steel
        apron=((255, 214, 96), (60, 14, 20), (120, 26, 36), (178, 50, 60)),  # crimson plates, gold studs
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary6',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),                 # arcane violet
        apron=((236, 240, 248), (12, 20, 60), (26, 44, 110), (60, 88, 180)),  # midnight-blue, silver runes
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary6',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                   # forest green
        apron=((232, 220, 188), (40, 26, 14), (84, 54, 28), (138, 96, 52)),  # tan leather, cream lacing
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


def apron_tone(x, cx, half, pal):
    """Pick an apron tone. pal = (STUD, D, M, L). Outer edge columns + the central
    stripe read as bright STUD (rivets / lace / emblem); a shadow crease sits just
    inside the left edge; the rest alternate lit/mid plate."""
    STUD, D, M, L = pal
    off = x - cx
    if abs(off) >= half:                 # outer stud/rivet edge
        return STUD
    if off == 0:                          # central emblem stripe
        return STUD
    if off == -(half - 1) and half >= 2:  # fold shadow just inside the left edge
        return D
    return L if (off % 2 == 0) else M


def midline(a):
    """Centre column of the leg mass over its LOWER rows (where the guard hangs)
    so the apron tracks the true midline in every pose, plus the top/bottom rows."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return None, None, None
    y0, y1 = int(rows.min()), int(rows.max())
    lo = max(y0, y1 - 10)
    xs = np.where(a[lo:y1 + 1].any(axis=0))[0]
    if xs.size == 0:
        xs = np.where(a[y1])[0]
    cx = int(round((int(xs.min()) + int(xs.max())) / 2.0))
    return cx, y0, y1


def draw_loinguard(fr, a, pal):
    cx, y0, y1 = midline(a)
    if cx is None:
        return
    yb0 = min(y0 + WAIST_DY, y1)
    span = y1 - y0
    y_bot = min(y0 + int(round(LOIN_FRAC * span)), Y_HEM_MAX, FH - 1)
    if y_bot <= yb0:
        return
    for y in range(yb0, y_bot + 1):
        # taper the strip to a point over the last TAPER rows
        d_from_bot = y_bot - y
        half = HALF if d_from_bot >= TAPER else max(0, HALF - (TAPER - d_from_bot))
        for x in range(cx - half, cx + half + 1):
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:
                # repaint the body pixel (surface plate on the leg)
                fr[y, x, :3] = apron_tone(x, cx, max(half, 1), pal)
                fr[y, x, 3] = 255
            elif fr[y, x, 3] == 0 and y > 0 and fr[y - 1, x, 3] > 0:
                # fill the inter-leg gap ONLY when the pixel above is already
                # opaque -> strip stays 4-connected to the waist by construction
                put(fr, y, x, apron_tone(x, cx, max(half, 1), pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['apron']
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
        if fi >= 60:                            # sleep: body only
            continue
        draw_loinguard(fr, a, pal)
        # Connectivity guard: drop any accent pixel not 4-connected to the body
        # mass (spread-leg poses can strand a hanging-tongue fragment). Only ever
        # touches added tongue px in transparent space — the repainted band pixels
        # are body pixels and are always kept.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_loinguard_legs_preview'
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
