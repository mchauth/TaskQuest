#!/usr/bin/env python3
"""Generate a NINTH net-new-geometry chest showcase per class — a bold symmetric
HERALDIC CHEVRON (downward-pointing V) blazoned across the chest. This is a NEW
read AXIS distinct from all eight existing chest geometries:

  * "winged"   (legendary1) chests flare UP at the BACK.
  * "pauldron" (legendary2) chests spike UP at the two top SHOULDER CORNERS.
  * "cape"     (legendary3) chests drape down and flare OUTWARD at the SIDES.
  * "tabard"   (legendary4) chests hang a single centred panel straight DOWN.
  * "gorget"   (legendary5) chests rise UP at the CENTRE-NECK.
  * "baldric"  (legendary6) chests lay a SINGLE DIAGONAL band across the torso.
  * "girdle"   (legendary7) chests wrap a HORIZONTAL band across the waist.
  * "roundel"  (legendary8) chests plant a filled CIRCULAR boss at chest centre.
  * this CHEVRON lays TWO mirrored diagonal arms meeting at a low central apex —
    a symmetric down-pointing V. It is neither a single diagonal (baldric), a
    horizontal band (girdle), nor a radial disc (roundel); the paired-diagonal V
    reads completely apart from every prior chest silhouette.

Authoring philosophy is identical to gen_roundel_legendary.py, including the same
key robustness win: the chevron is painted ONLY onto pixels that are ALREADY
opaque body pixels (`a`). Because it never adds a pixel outside the existing
silhouette, it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — the chevron is QA-safe purely by construction. It still
reads as a distinct V because the metal tones contrast sharply with the recolored
body and the arms track a fixed apex/slope down the torso in every pose.

  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = a symmetric chevron. Per frame we find the body mass, set a central
    apex at APEX_FRAC down the torso and let two arms rise up-and-outward at SLOPE.
    Body pixels within CHEV_W of either arm are repainted: dark selvage at the band
    edge, lit metal on the crown, periodic bright STUDS marching up each arm, and a
    bright rivet at the apex. Everything is clamped to `a`, so the chevron tracks
    the torso through every pose/animation exactly.

Sleep frames (fi>=60, lying down) get the recolor only — no chevron — matching the
winged / pauldron / cape / tabard / gorget / baldric / girdle / roundel convention.
Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (chevron metal picked to read apart on the recolored body; the paired-V
silhouette is the headline):
  * warrior "Sovereign's Chevron" — obsidian/steel body + SILVER-WHITE chevron, crimson selvage
  * mage    "Astral Chevron"      — arcane-violet body + MAGENTA chevron, starlight studs
  * ranger  "Warden's Chevron"    — forest body + AMBER-GOLD chevron, pale studs

Run from repo root:
  python3 scripts/gen_chevron_legendary.py
Then QA:
  python3 scripts/sprite_qa.py _chevron_legendary_preview/shirt_warrior_legendary9.png
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

# Chevron geometry. The apex (bottom point of the V) sits APEX_FRAC of the way down
# the torso, centred horizontally on the body mass. Two arms rise up-and-outward
# from the apex to ARM_TOP_FRAC; SLOPE is the horizontal px gained per vertical px.
# CHEV_W is the half-thickness of each arm band; a bright stud is painted on the
# crown every STUD_STEP rows up each arm.
APEX_FRAC = 0.60      # 0 = top of torso, 1 = bottom -> apex sits lower-mid chest
ARM_TOP_FRAC = 0.20   # arms rise to near the shoulders
SLOPE = 0.85          # horizontal px per vertical px (arm diagonal)
CHEV_W = 1.4          # half-thickness of each arm band (px) -> ~3px band
STUD_STEP = 3         # bright stud every N rows up each arm

# ── Per-class palettes: body ramp (D/M/L) + chevron ramp (EDGE, CROWN, STUD) ────
# body:    deep shadow / base / highlight
# chevron: EDGE (dark selvage at band edge) / CROWN (lit metal) / STUD (bright
#          rivets up the arms + apex)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary9',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian -> steel
        chevron=((92, 14, 18), (206, 210, 222), (255, 250, 240)),    # silver-white, crimson selvage
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary9',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        chevron=((92, 18, 88), (208, 60, 178), (255, 224, 250)),     # magenta, starlight studs
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary9',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        chevron=((78, 50, 12), (214, 158, 46), (250, 236, 176)),     # amber-gold, pale studs
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


def draw_chevron(fr, a, pal):
    """Repaint a symmetric down-pointing V across the chest. Only body pixels are
    touched, so the chevron adds zero new silhouette pixels (QA-safe)."""
    EDGE, CROWN, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    ytop, ybot = int(ys.min()), int(ys.max())
    ext = max(ybot - ytop, 1)
    cx = float(xs.mean())
    y_apex = ytop + APEX_FRAC * ext            # apex row (fractional)
    y_arm_top = ytop + ARM_TOP_FRAC * ext      # top of the arms
    for y, x in zip(ys, xs):
        if y > y_apex or y < y_arm_top:
            continue
        arm = SLOPE * (y_apex - y)             # horizontal offset of each arm here
        dl = abs(x - (cx - arm))
        dr = abs(x - (cx + arm))
        d = min(dl, dr)
        if d > CHEV_W:
            continue
        stud = (int(round(arm)) % STUD_STEP == 0) and d <= 0.7
        if stud:
            tone = STUD
        elif d >= CHEV_W - 0.6:
            tone = EDGE                         # dark selvage at band edge
        else:
            tone = CROWN                        # lit metal crown
        put(fr, y, x, tone)
    # Bright rivet at the apex (clamped to a body pixel only).
    ay, ax = int(round(y_apex)), int(round(cx))
    if 0 <= ay < FH and 0 <= ax < FW and a[ay, ax]:
        put(fr, ay, ax, STUD)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['chevron']
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
        draw_chevron(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the chevron only repaints body
        # pixels so no stray is possible — a no-op here by construction, kept for
        # uniformity with the other generators.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        strays = da & ~keep
        for y, x in np.argwhere(strays):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_chevron_legendary_preview'
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
