#!/usr/bin/env python3
"""Generate a SIXTH net-new-geometry chest showcase per class — a diagonal
BALDRIC (shoulder-to-hip sash/bandolier) crossing the torso. This is a NEW
silhouette AXIS distinct from all five existing chest geometries:

  * "winged"   (legendary1) chests flare UP at the BACK.
  * "pauldron" (legendary2) chests spike UP at the two top SHOULDER CORNERS.
  * "cape"     (legendary3) chests drape down and flare OUTWARD at the SIDES.
  * "tabard"   (legendary4) chests hang a single centred panel straight DOWN.
  * "gorget"   (legendary5) chests rise UP at the CENTRE-NECK.
  * this BALDRIC lays a bold DIAGONAL band ACROSS the front of the torso, from
    the right shoulder down to the left hip — the previously-unused diagonal
    axis. up-back / up-shoulder / out-sides / down-centre / up-neck / DIAGONAL
    is the six-way silhouette contrast.

Authoring philosophy is identical to gen_gorget_legendary.py, with ONE key
robustness win: the baldric accent is painted ONLY onto pixels that are ALREADY
opaque body pixels (`a`). Because it never adds a pixel outside the existing
silhouette, it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — the strap is QA-safe purely by construction. The
silhouette still reads as a distinct diagonal band because the strap tones
contrast sharply with the recolored body.

  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a diagonal strap. For each frame we take the centroid of the body
    mass and define an anti-diagonal line (top-right -> bottom-left) through it.
    Body pixels within perpendicular distance HALF of that line are repainted as
    the strap: lit crown down the centre-line, dark selvage at the two edges,
    plus periodic bright STUDS and a central BUCKLE. Everything is clamped to
    `a`, so the strap tracks the torso through every pose/animation exactly.

Sleep frames (fi>=60, lying down) get the recolor only — no strap — matching the
winged / pauldron / cape / tabard / gorget convention. Shading applied in-script
via shade(); do NOT run sprite_shade.py again.

Per class (strap hue distinct from EVERY prior legendary chest accent so all six
read apart; the DIAGONAL silhouette is the headline):
  * warrior "Sovereign's Baldric" — obsidian/steel body + OXBLOOD strap, GOLD studs
  * mage    "Astral Baldric"      — arcane-violet body + CYAN strap, starlight studs
  * ranger  "Warden's Baldric"    — forest body + TAN-leather strap, BRONZE studs

Run from repo root:
  python3 scripts/gen_baldric_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _baldric_legendary_preview/shirt_warrior_legendary6.png
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

# Baldric geometry. The strap is an anti-diagonal band (top-right -> bottom-left)
# through the body centroid. HALF = half-thickness of the strap in perpendicular
# pixels (so a ~3px-wide strap). STUD_STEP = paint a bright stud every N rows
# down the strap crown. BUCKLE_R = half-size of the square buckle at the centre.
HALF = 1.6
STUD_STEP = 3
BUCKLE_R = 1

# ── Per-class palettes: body ramp (D/M/L) + strap ramp (EDGE, MID, CROWN, STUD) ─
# body:  deep shadow / base / highlight
# strap: EDGE (dark selvage on both rims) / MID / CROWN (lit centre-line) /
#        STUD (bright rivets + buckle)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary6',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),                    # obsidian -> steel
        strap=((54, 12, 14), (110, 24, 26), (168, 44, 40), (255, 214, 96)),    # oxblood leather, gold studs
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary6',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),                    # arcane violet
        strap=((14, 60, 78), (26, 118, 150), (72, 196, 224), (224, 248, 255)), # cyan energy, starlight studs
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary6',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                      # forest green
        strap=((58, 40, 22), (104, 74, 40), (156, 118, 70), (198, 132, 58)),   # tan leather, bronze studs
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


def draw_baldric(fr, a, pal):
    """Repaint an anti-diagonal strap across the body mass. Only body pixels are
    touched, so the strap adds zero new silhouette pixels (QA-safe)."""
    EDGE, MID, CROWN, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    cy = float(ys.mean())
    cx = float(xs.mean())
    # Anti-diagonal line through centroid: normal n=(1,1)/sqrt2, so signed
    # perpendicular distance of a pixel is ((x-cx)+(y-cy))/sqrt2. |dist|<=HALF is
    # the strap band. `along` orders pixels down the strap for stud spacing.
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
    # central buckle: bright square where the strap crosses the torso centre,
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
        draw_baldric(fr, a, pal)
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
    outdir = '_baldric_legendary_preview'
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
