#!/usr/bin/env python3
"""Generate a FOURTH net-new-geometry chest showcase per class — a heraldic
TABARD/BANNER that hangs straight DOWN the FRONT-CENTER of the torso and ends in
a swallowtail hem, completing the chest showcase to FOUR distinct silhouettes
(matching helmets, which already have four axes, and legs, which have four).

Why this is a NEW silhouette (distinct from ALL THREE existing chest geometries):
  * The "winged" chests flare UP at the BACK (a pair of wings rising behind the
    shoulders).
  * The "pauldron" chests spike UP at the SHOULDERS (mass added at the two top
    corners of the torso).
  * The "cape" chests drape down and flare OUTWARD at the two SIDE edges (a pair
    of side panels widening toward the hem).
  * This tabard adds a SINGLE CENTERED panel hanging straight DOWN below the
    tunic hem along the body's centre line, ending in a forked swallowtail. It is
    the only chest piece whose net-new silhouette is a central bottom tongue
    rather than side/shoulder/back mass — up-back / up-shoulder / out-sides /
    down-centre is the same four-way contrast the helmets draw.

Authoring philosophy is identical to gen_cape_legendary.py:
  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose/animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = a single centered tabard panel drawn ONLY in the transparent space
    directly BELOW the tunic hem (never overpaints the body). The panel's top row
    sits immediately under the hem's centre columns, so it is 4-connected to the
    body by construction. It hangs HANG rows, tapering slightly, and the bottom
    SWALLOW rows are split by a central notch into two heraldic prongs (each prong
    stays connected up through the solid panel above the notch — QA-safe: no
    isolated pixels, no accent-caused multi-component frames). A per-frame
    connectivity guard clears any panel pixel not 4-connected to the body mass, so
    accent strays are 0 by construction. The hem is clamped to y<=52 so it stays
    inside the QA character zone for BOTH genders (no background-bleed flag).

Per class (field hue distinct from EVERY prior legendary chest so all four read
apart; the silhouette is the headline):
  * warrior "Sovereign's Tabard" — obsidian/steel body + royal-blue field, gold trim/emblem
  * mage    "Runeweave Tabard"   — arcane-violet body + emerald field, pale-gold rune trim
  * ranger  "Warden's Tabard"     — forest body + burgundy/wine field, cream-bone trim

Sleep frames (fi>=60, lying down) get the recolor only — no tabard — matching the
winged / pauldron / cape convention. Shading applied in-script via shade(); do
NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_tabard_legendary.py
Then QA (the hanging tabard intentionally extends below the tunic hem):
  python3 scripts/sprite_qa.py _tabard_legendary_preview/shirt_warrior_legendary4.png
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

# Tabard geometry.
HALF = 3          # half-width of the panel at the top (full width ~2*HALF+1 = 7)
HANG = 9          # rows the tabard hangs below the tunic hem
TAPER_AT = 6      # rows down at which the panel begins narrowing by 1px/row
SWALLOW = 3       # bottom rows split by the central notch into two prongs
NOTCH = 1         # half-width of the central notch (|x-cx|<=NOTCH cleared)
Y_HEM_MAX = 52    # clamp hem inside QA character zone for both genders

# ── Per-class palettes: body ramp (D/M/L) + tabard ramp (TRIM, D, M, L) ────────
# body:   deep shadow / base / highlight
# tabard: TRIM (bright edge + centre emblem stripe) / D (fold shadow) /
#         M (mid fabric) / L (lit fold)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary4',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),              # obsidian->steel
        tabard=((255, 214, 96), (18, 30, 78), (34, 58, 140), (70, 104, 208)),  # royal blue, gold trim
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary4',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),              # arcane violet
        tabard=((236, 226, 150), (10, 44, 30), (22, 84, 54), (58, 150, 96)),   # emerald, pale-gold runes
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary4',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                # forest green
        tabard=((232, 220, 188), (56, 12, 22), (104, 24, 38), (158, 52, 66)),  # burgundy/wine, cream trim
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


def tab_tone(x, cx, half, pal):
    """Pick a tabard tone. pal = (TRIM, D, M, L). x is the column, cx the centre,
    half the current half-width. Outer edge columns + the central emblem stripe
    read as bright TRIM; a shadow crease sits just inside the left edge; the rest
    alternate lit/mid fabric."""
    TRIM, D, M, L = pal
    off = x - cx
    if abs(off) >= half:                 # outer selvage / trim edge
        return TRIM
    if off == 0:                          # central emblem stripe
        return TRIM
    if off == -(half - 1) and half >= 2:  # fold shadow just inside the left edge
        return D
    return L if (off % 2 == 0) else M


def torso_center(a):
    """Centre column of the torso, measured over its lower rows (where the hem
    hangs) so the tabard tracks the body's true midline in every pose."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return None, None
    y1 = int(rows.max())
    lo = max(int(rows.min()), y1 - 8)
    xs = np.where(a[lo:y1 + 1].any(axis=0))[0]
    if xs.size == 0:
        xs = np.where(a[y1])[0]
    cx = int(round((int(xs.min()) + int(xs.max())) / 2.0))
    return cx, y1


def draw_tabard(fr, a, pal):
    cx, y1 = torso_center(a)
    if cx is None:
        return
    for j in range(1, HANG + 1):
        y = y1 + j
        if y > Y_HEM_MAX or y >= FH:
            break
        half = HALF - max(0, j - TAPER_AT)   # narrow as it descends
        if half < 1:
            break
        in_swallow = j > HANG - SWALLOW
        for x in range(cx - half, cx + half + 1):
            if in_swallow and abs(x - cx) <= NOTCH:
                continue                      # central swallowtail notch
            if not (0 <= x < FW):
                continue
            if a[y, x] or fr[y, x, 3] > 0:    # never overpaint body/existing
                continue
            put(fr, y, x, tab_tone(x, cx, half, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['tabard']
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
        draw_tabard(fr, a, pal)
        # Connectivity guard: drop any tabard pixel not 4-connected to the body
        # mass (only touches stranded accent px, never body px).
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_tabard_legendary_preview'
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
