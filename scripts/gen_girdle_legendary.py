#!/usr/bin/env python3
"""Generate a SEVENTH net-new-geometry chest showcase per class — a bold
HORIZONTAL WAR-BELT / GIRDLE band wrapping the midriff. This is a NEW silhouette
AXIS distinct from all six existing chest geometries:

  * "winged"   (legendary1) chests flare UP at the BACK.
  * "pauldron" (legendary2) chests spike UP at the two top SHOULDER CORNERS.
  * "cape"     (legendary3) chests drape down and flare OUTWARD at the SIDES.
  * "tabard"   (legendary4) chests hang a single centred panel straight DOWN.
  * "gorget"   (legendary5) chests rise UP at the CENTRE-NECK.
  * "baldric"  (legendary6) chests lay a single DIAGONAL band across the torso.
  * this GIRDLE wraps a bold HORIZONTAL band across the WAIST/midriff — the last
    unused primary axis. up-back / up-shoulder / out-sides / down-centre /
    up-neck / diagonal / HORIZONTAL is the seven-way silhouette contrast.

Authoring philosophy is identical to gen_baldric_legendary.py (its direct
predecessor), including the same key robustness win: the belt accent is painted
ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it never adds
a pixel outside the existing silhouette, it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — the belt is QA-safe
purely by construction. The silhouette still reads as a distinct horizontal band
because the belt tones contrast sharply with the recolored body and it lands at a
fixed fraction down the torso in every pose.

  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a horizontal belt. For each frame we take the body mass's vertical
    extent and place the band at BAND_FRAC of the way down it, BAND_HALF px thick.
    Body pixels inside the band are repainted as the belt: lit crown along the
    centre row, dark selvage on the top/bottom rims, plus periodic bright STUDS
    marching across and a central square BUCKLE. Everything is clamped to `a`, so
    the belt tracks the torso through every pose/animation exactly.

Sleep frames (fi>=60, lying down) get the recolor only — no belt — matching the
winged / pauldron / cape / tabard / gorget / baldric convention. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class (belt hue distinct from EVERY prior legendary chest accent so all seven
read apart; the HORIZONTAL silhouette is the headline):
  * warrior "Sovereign's War-Belt" — obsidian/steel body + BRONZE-leather belt, SILVER studs
  * mage    "Astral Girdle"        — arcane-violet body + GOLD belt, starlight studs
  * ranger  "Warden's War-Belt"    — forest body + OXBLOOD belt, GOLD studs

Run from repo root:
  python3 scripts/gen_girdle_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _girdle_legendary_preview/shirt_warrior_legendary7.png
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

# Belt geometry. The band is a horizontal strip across the body mass, placed at
# BAND_FRAC down the vertical extent of the frame's body pixels, with a
# half-thickness of BAND_HALF (so a ~3px-tall belt). STUD_STEP = paint a bright
# stud every N columns across the belt crown. BUCKLE_R = half-size of the square
# buckle at the horizontal centre.
BAND_FRAC = 0.64      # 0 = top of torso, 1 = bottom -> sits on the waist
BAND_HALF = 1.6
STUD_STEP = 3
BUCKLE_R = 1

# ── Per-class palettes: body ramp (D/M/L) + belt ramp (EDGE, MID, CROWN, STUD) ─
# body:  deep shadow / base / highlight
# belt:  EDGE (dark selvage on both rims) / MID / CROWN (lit centre-row) /
#        STUD (bright rivets + buckle)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary7',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),                    # obsidian -> steel
        belt=((46, 30, 14), (92, 60, 28), (150, 104, 52), (222, 226, 232)),    # bronze leather, silver studs
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary7',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),                    # arcane violet
        belt=((72, 48, 8), (140, 100, 20), (208, 158, 44), (255, 246, 200)),   # warm gold, starlight studs
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary7',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                      # forest green
        belt=((52, 12, 14), (104, 26, 26), (162, 44, 40), (238, 200, 96)),     # oxblood leather, gold studs
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


def draw_girdle(fr, a, pal):
    """Repaint a horizontal belt across the body mass. Only body pixels are
    touched, so the belt adds zero new silhouette pixels (QA-safe)."""
    EDGE, MID, CROWN, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    ytop, ybot = int(ys.min()), int(ys.max())
    cy = ytop + BAND_FRAC * (ybot - ytop)     # belt centre-row (fractional)
    xleft = int(xs.min())
    for y, x in zip(ys, xs):
        dist = y - cy                          # signed vertical dist from centre-row
        ad = abs(dist)
        if ad > BAND_HALF:
            continue
        # tone by vertical position within the band: lit crown centre-row, dark
        # selvage on top/bottom rims
        if ad <= 0.55:
            tone = CROWN
        elif ad <= 1.05:
            tone = MID
        else:
            tone = EDGE
        # periodic bright studs marching across the crown row
        if ad <= 0.55 and ((x - xleft) % STUD_STEP == 0):
            tone = STUD
        put(fr, y, x, tone)
    # central buckle: bright square where the belt crosses the torso centre,
    # clamped to body pixels only.
    bx = int(round(float(xs.mean())))
    by = int(round(cy))
    for dy in range(-BUCKLE_R, BUCKLE_R + 1):
        for dx in range(-BUCKLE_R, BUCKLE_R + 1):
            yy, xx = by + dy, bx + dx
            if 0 <= yy < FH and 0 <= xx < FW and a[yy, xx]:
                put(fr, yy, xx, STUD)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['belt']
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
        draw_girdle(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the belt only repaints body
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
    outdir = '_girdle_legendary_preview'
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
