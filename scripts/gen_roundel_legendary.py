#!/usr/bin/env python3
"""Generate an EIGHTH net-new-geometry chest showcase per class — a bold CENTRAL
CIRCULAR ROUNDEL / BOSS MEDALLION ("Aegis") planted on the chest. This is a NEW
read AXIS distinct from all seven existing chest geometries, EVERY one of which is
linear/band-based:

  * "winged"   (legendary1) chests flare UP at the BACK.
  * "pauldron" (legendary2) chests spike UP at the two top SHOULDER CORNERS.
  * "cape"     (legendary3) chests drape down and flare OUTWARD at the SIDES.
  * "tabard"   (legendary4) chests hang a single centred panel straight DOWN.
  * "gorget"   (legendary5) chests rise UP at the CENTRE-NECK.
  * "baldric"  (legendary6) chests lay a single DIAGONAL band across the torso.
  * "girdle"   (legendary7) chests wrap a HORIZONTAL band across the waist.
  * this AEGIS plants a filled CIRCULAR BOSS at the chest centre — the first
    NON-linear chest axis. A disc reads completely apart from any band: it is
    radial, not directional, so it contrasts with all seven prior silhouettes.

Authoring philosophy is identical to gen_girdle_legendary.py (its direct
predecessor), including the same key robustness win: the roundel is painted ONLY
onto pixels that are ALREADY opaque body pixels (`a`). Because it never adds a
pixel outside the existing silhouette, it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — the boss is QA-safe
purely by construction. It still reads as a distinct radial medallion because the
metal tones contrast sharply with the recolored body and it lands at a fixed
fraction down the torso, centred horizontally, in every pose.

  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a circular boss. For each frame we find the body mass, place the
    disc centre at (mean-x, BOSS_FRAC down the vertical extent), radius BOSS_R.
    Body pixels within the disc are repainted as concentric shells: dark rim on
    the outer ring, lit metal on the ring inside it, and a bright domed STUD at
    the very centre, plus four cardinal rivets on the rim for a bossed-shield
    look. Everything is clamped to `a`, so the boss tracks the torso through
    every pose/animation exactly.

Sleep frames (fi>=60, lying down) get the recolor only — no boss — matching the
winged / pauldron / cape / tabard / gorget / baldric / girdle convention. Shading
applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (boss metal distinct from EVERY prior legendary chest accent so all
eight read apart; the radial silhouette is the headline):
  * warrior "Sovereign's Aegis" — obsidian/steel body + GOLD boss, white-hot stud
  * mage    "Astral Aegis"      — arcane-violet body + CYAN-silver boss, starlight stud
  * ranger  "Warden's Aegis"    — forest body + BRONZE boss, gold stud

Run from repo root:
  python3 scripts/gen_roundel_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _roundel_legendary_preview/shirt_warrior_legendary8.png
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

# Boss geometry. The disc is centred horizontally on the body mass and BOSS_FRAC
# of the way down its vertical extent (upper-mid chest). BOSS_R is the outer
# radius; RIM_W is the thickness of the dark outer ring; the centre <= STUD_R is
# painted as the bright domed stud. Cardinal rivets are placed on the rim.
BOSS_FRAC = 0.46      # 0 = top of torso, 1 = bottom -> sits high-centre chest
BOSS_R = 3.3          # outer radius of the medallion (px)
RIM_W = 1.0           # dark selvage ring thickness (px)
STUD_R = 0.9          # central domed boss-stud radius (px)

# ── Per-class palettes: body ramp (D/M/L) + boss ramp (RIM, MID, FACE, STUD) ───
# body:  deep shadow / base / highlight
# boss:  RIM (dark outer ring) / MID / FACE (lit metal ring) / STUD (bright dome
#        + cardinal rivets)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary8',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),                    # obsidian -> steel
        boss=((70, 48, 8), (140, 100, 20), (208, 158, 44), (255, 246, 210)),   # gold medallion, white-hot stud
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary8',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),                    # arcane violet
        boss=((26, 60, 80), (52, 118, 150), (110, 196, 226), (240, 252, 255)), # cyan-silver, starlight stud
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary8',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                      # forest green
        boss=((58, 32, 12), (112, 68, 28), (168, 108, 48), (238, 206, 110)),   # bronze medallion, gold stud
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


def draw_roundel(fr, a, pal):
    """Repaint a circular boss medallion at the chest centre. Only body pixels
    are touched, so the boss adds zero new silhouette pixels (QA-safe)."""
    RIM, MID, FACE, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    ytop, ybot = int(ys.min()), int(ys.max())
    cy = ytop + BOSS_FRAC * (ybot - ytop)      # disc centre-row (fractional)
    cx = float(xs.mean())                      # disc centre-col
    r_in = BOSS_R - RIM_W                       # inner edge of the dark rim
    for y, x in zip(ys, xs):
        d = ((y - cy) ** 2 + (x - cx) ** 2) ** 0.5
        if d > BOSS_R:
            continue
        if d <= STUD_R:
            tone = STUD                         # bright domed centre stud
        elif d >= r_in:
            tone = RIM                          # dark outer ring
        elif d >= r_in - 1.0:
            tone = FACE                         # lit metal ring just inside rim
        else:
            tone = MID                          # inner field
        put(fr, y, x, tone)
    # Four cardinal rivets on the rim (N/E/S/W), clamped to body pixels only.
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        yy = int(round(cy + dy * (BOSS_R - 0.4)))
        xx = int(round(cx + dx * (BOSS_R - 0.4)))
        if 0 <= yy < FH and 0 <= xx < FW and a[yy, xx]:
            put(fr, yy, xx, STUD)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['boss']
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
        draw_roundel(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the boss only repaints body
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
    outdir = '_roundel_legendary_preview'
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
