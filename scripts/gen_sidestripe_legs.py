#!/usr/bin/env python3
"""Generate an EIGHTH net-new-geometry LEGS showcase per class — PAIRED OUTER
SIDE-STRIPES: two bold vertical bands repainted down the OUTER edge of each leg
(the dress-trouser / racing-stripe axis). This brings the legs slot to EIGHT
distinct axes, at parity with the chest and boots slots, and is the paired-lateral-
vertical axis that none of the seven existing legendary legs occupy:

  * legendary1 (tassets)     — SHORT paired hip flaps hanging at the outer sides.
  * legendary2 (war-kilt)    — a long smooth cloth drape to a flared HEM.
  * legendary3 (faulds)      — a STIFF full-width tiered plate skirt.
  * legendary4 (poleyns)     — round disc bulging OUTWARD at the KNEE.
  * legendary5 (cuisses)     — a broad fin flaring OUTWARD at the HIP.
  * legendary6 (loin-guard)  — a NARROW vertical strap on the CENTRELINE.
  * legendary7 (sword-belt)  — a bold DIAGONAL band across the thighs.
  * these SIDE-STRIPES lay two full-height vertical bands at the OUTER edge of
    each leg — the paired-lateral-vertical axis (mirror of the single centre
    loin-guard and orthogonal to the diagonal sword-belt).

Authoring philosophy is identical to gen_legbaldric_legs.py and
gen_loinguard_legs.py, including the key robustness win: the stripes are painted
ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because they never add
a pixel outside the existing silhouette, they CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — the stripes are QA-safe
purely by construction. They read as distinct bands because the stripe tones
contrast with the recolored body and they hug the outer leg edge in every pose.

  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = paired outer stripes. Per frame, per pixel-row of the leg mass we find
    the leftmost and rightmost opaque columns and repaint a STRIPE_W-wide band just
    inside each outer edge: lit crown down the stripe centre, dark selvage at the
    inner rim, plus periodic bright STUDS marching down each stripe. Everything is
    clamped to `a`, so the stripes track the legs through every pose exactly.

Sleep frames (fi>=60, lying down) get the recolor only — no stripes — matching the
apron / cuisse / kilt / baldric convention. Shading applied in-script via shade();
do NOT run sprite_shade.py again.

Per class (stripe hue distinct from EVERY prior legendary legs accent so all eight
read apart):
  * warrior "Warlord's Field-Stripes" — obsidian/steel body + CRIMSON stripes, gold studs
  * mage    "Astral Piping"           — arcane-violet body + CYAN stripes, starlight studs
  * ranger  "Warden's Trail-Stripes"  — forest body + TAN-leather stripes, copper studs

Run from repo root:
  python3 scripts/gen_sidestripe_legs.py
Then QA:
  python3 scripts/sprite_qa.py _sidestripe_legs_preview/pants_warrior_legendary8.png --y-max 62
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

# Side-stripe geometry. STRIPE_W = width in px of each outer stripe (from the outer
# edge inward). GAP_MIN = a row's leg span must be at least this wide to carry two
# separate stripes (narrow rows get a single centred hint instead of overlap).
# STUD_STEP = paint a bright stud every N rows down each stripe.
STRIPE_W = 2
GAP_MIN = 6
STUD_STEP = 3

# ── Per-class palettes: body ramp (D/M/L) + stripe ramp (EDGE, CROWN, STUD) ──────
# body  : deep shadow / base / highlight
# stripe: EDGE (dark selvage at inner rim) / CROWN (lit stripe body) /
#         STUD (bright rivets down the stripe)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary8',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian -> steel
        stripe=((96, 12, 16), (206, 44, 52), (255, 214, 96)),        # crimson stripes, gold studs
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary8',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        stripe=((18, 78, 96), (52, 176, 214), (255, 246, 200)),      # cyan piping, starlight studs
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary8',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        stripe=((60, 46, 26), (150, 116, 70), (206, 132, 66)),       # tan leather, copper studs
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


def draw_side_stripes(fr, a, pal):
    """Repaint paired vertical stripes at the outer edge of each leg row. Only body
    pixels are touched, so the stripes add zero new silhouette pixels (QA-safe)."""
    EDGE, CROWN, STUD = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    ytop = int(ys.min())
    # Work row by row so the stripes hug the true outer edge in every pose.
    for y in range(int(ys.min()), int(ys.max()) + 1):
        row_x = np.where(a[y])[0]
        if row_x.size == 0:
            continue
        xl, xr = int(row_x.min()), int(row_x.max())
        span = xr - xl
        stud = ((y - ytop) % STUD_STEP == 0)
        if span >= GAP_MIN:
            # two stripes: left band [xl .. xl+W-1], right band [xr-W+1 .. xr]
            for k in range(STRIPE_W):
                lx, rx = xl + k, xr - k
                # inner rim (k == STRIPE_W-1) is the dark selvage, outer is lit crown
                tone = EDGE if k == STRIPE_W - 1 else CROWN
                if a[y, lx]:
                    put(fr, y, lx, STUD if (stud and k == 0) else tone)
                if a[y, rx]:
                    put(fr, y, rx, STUD if (stud and k == 0) else tone)
        else:
            # narrow row (ankle/overlap): a single lit hint at each outer px
            if a[y, xl]:
                put(fr, y, xl, STUD if stud else CROWN)
            if a[y, xr]:
                put(fr, y, xr, STUD if stud else CROWN)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['stripe']
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
        draw_side_stripes(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the stripes only repaint body
        # pixels so no stray is possible — no-op here by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        strays = da & ~keep
        for y, x in np.argwhere(strays):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_sidestripe_legs_preview'
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
