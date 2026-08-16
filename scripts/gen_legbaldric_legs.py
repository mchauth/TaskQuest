#!/usr/bin/env python3
"""Generate a SEVENTH net-new-geometry LEGS showcase per class — a diagonal
SWORD-BELT / HIP-SASH (a bandolier-style strap) crossing the thighs from the
outer hip down to the opposite inner knee. This brings the legs slot to SEVEN
distinct silhouette axes, at parity with the chest slot, and is the DIAGONAL
axis that none of the six existing legendary legs occupy:

  * legendary1 (Seraph / Starweaver / Skyhunter tassets) — SHORT PAIRED hip flaps
    hanging straight down at the OUTER sides (two narrow LATERAL tabs).
  * legendary2 (Battle-Kilt / Ritual-Skirt / War-Kilt)   — a long SMOOTH cloth
    drape widening to a soft flared HEM (full-width soft bottom edge).
  * legendary3 (Bronze/Rune/Scale Faulds)                — a STIFF full-width
    tiered plate skirt filling the whole gap hip->knee.
  * legendary4 (Aegis/Rose/Bone Poleyns)                 — a compact round disc
    bulging OUTWARD at the mid-leg KNEE (lateral mass at the knee).
  * legendary5 (Bulwark/Warding/Warden Cuisses)          — a broad fin flaring
    OUTWARD at the HIP then tapering (lateral flare at the top of the leg).
  * legendary6 (War-Apron / Ward-Apron / Warden Apron)   — a NARROW vertical
    plated strap on the CENTRELINE (pure DOWN-CENTRE axis).
  * this SWORD-BELT lays a bold DIAGONAL band ACROSS the thighs, hip -> opposite
    knee — the previously-unused diagonal axis. lateral-tabs / hem / full-skirt /
    knee-disc / hip-flare / down-centre / DIAGONAL is the seven-way contrast, an
    exact mirror of how the chest slot's baldric is the diagonal counterpart to
    its own six axes.

Authoring philosophy is identical to gen_baldric_legendary.py (chest, its direct
predecessor) and gen_girdle_legendary.py, including the same key robustness win:
the belt accent is painted ONLY onto pixels that are ALREADY opaque body pixels
(`a`). Because it never adds a pixel outside the existing silhouette, it CANNOT
create isolated pixels, background bleed, or accent-caused multi-component frames
— the strap is QA-safe purely by construction. The silhouette still reads as a
distinct diagonal band because the strap tones contrast sharply with the
recolored body and it lands at a fixed diagonal through the thigh mass in every
pose.

  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a diagonal strap. For each frame we take the centroid of the leg
    mass and define an anti-diagonal line (top-right -> bottom-left) through it.
    Body pixels within perpendicular distance HALF of that line are repainted as
    the strap: lit crown down the centre-line, dark selvage at the two edges,
    plus periodic bright STUDS and a central square BUCKLE. Everything is clamped
    to `a`, so the strap tracks the thighs through every pose/animation exactly.

Sleep frames (fi>=60, lying down) get the recolor only — no strap — matching the
apron / cuisse / kilt / tabard / baldric convention. Shading applied in-script
via shade(); do NOT run sprite_shade.py again.

Per class (strap hue distinct from EVERY prior legendary legs accent so all seven
read apart; the DIAGONAL silhouette is the headline):
  * warrior "Warlord's Sword-Belt" — obsidian/steel body + STEEL-BLUE strap, gold studs
  * mage    "Astral Sash"          — arcane-violet body + AMBER strap, starlight studs
  * ranger  "Warden's Baldric-Belt"— forest body + BIRCH-leather strap, copper studs

Run from repo root:
  python3 scripts/gen_legbaldric_legs.py
Then QA:
  python3 scripts/sprite_qa.py _legbaldric_legs_preview/pants_warrior_legendary7.png --y-max 62
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

# Sword-belt geometry. The strap is an anti-diagonal band (top-right ->
# bottom-left) through the leg-mass centroid. HALF = half-thickness of the strap
# in perpendicular pixels (so a ~3px-wide strap). STUD_STEP = paint a bright stud
# every N rows down the strap crown. BUCKLE_R = half-size of the square buckle.
HALF = 1.6
STUD_STEP = 3
BUCKLE_R = 1

# ── Per-class palettes: body ramp (D/M/L) + strap ramp (EDGE, MID, CROWN, STUD) ─
# body:  deep shadow / base / highlight
# strap: EDGE (dark selvage on both rims) / MID / CROWN (lit centre-line) /
#        STUD (bright rivets + buckle)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary7',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),                    # obsidian -> steel
        strap=((22, 34, 54), (44, 68, 104), (78, 116, 168), (255, 214, 96)),   # steel-blue leather, gold studs
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary7',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),                    # arcane violet
        strap=((72, 44, 8), (140, 92, 18), (208, 148, 40), (255, 246, 200)),   # warm amber, starlight studs
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary7',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                      # forest green
        strap=((60, 46, 26), (110, 84, 48), (162, 128, 78), (206, 132, 66)),   # birch leather, copper studs
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


def draw_sword_belt(fr, a, pal):
    """Repaint an anti-diagonal strap across the leg mass. Only body pixels are
    touched, so the strap adds zero new silhouette pixels (QA-safe)."""
    EDGE, MID, CROWN, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    cy = float(ys.mean())
    cx = float(xs.mean())
    # Anti-diagonal line through centroid: normal n=(1,1)/sqrt2, so signed
    # perpendicular distance of a pixel is ((x-cx)+(y-cy))/sqrt2. |dist|<=HALF is
    # the strap band. `along` (y order) drives stud spacing down the strap.
    inv = 1.0 / np.sqrt(2.0)
    ytop = int(ys.min())
    for y, x in zip(ys, xs):
        dist = ((x - cx) + (y - cy)) * inv
        ad = abs(dist)
        if ad > HALF:
            continue
        # tone by perpendicular position: lit crown centre, dark selvage rims
        if ad <= 0.55:
            tone = CROWN
        elif ad <= 1.05:
            tone = MID
        else:
            tone = EDGE
        # periodic bright studs marching down the crown line
        if ad <= 0.55 and ((y - ytop) % STUD_STEP == 0):
            tone = STUD
        put(fr, y, x, tone)
    # central buckle: bright square where the strap crosses the leg centre,
    # clamped to body pixels only.
    bx, by = int(round(cx)), int(round(cy))
    for dy in range(-BUCKLE_R, BUCKLE_R + 1):
        for dx in range(-BUCKLE_R, BUCKLE_R + 1):
            yy, xx = by + dy, bx + dx
            if 0 <= yy < FH and 0 <= xx < FW and a[yy, xx]:
                put(fr, yy, xx, STUD)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['strap']
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
        if fi >= 60:                          # sleep: body only
            continue
        draw_sword_belt(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the strap only repaints body
        # pixels so no stray is possible, but we keep the same guard as the other
        # generators for uniformity — it is a no-op here by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        strays = da & ~keep
        for y, x in np.argwhere(strays):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_legbaldric_legs_preview'
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
