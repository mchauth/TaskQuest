#!/usr/bin/env python3
"""SEVENTEENTH net-new-geometry axis for ALL FOUR SLOTS — the ASHLAR / MASONRY
BRICK-BOND family: a tessellated field of OFFSET RECTANGULAR CELLS laid in a running
bond, i.e. dressed-stone / brickwork. Horizontal mortar courses run the full width and
short vertical joints connect them, but the joints of each course are STAGGERED half a
brick against the course above — the defining feature of masonry bond. This is the
repeated offset-rectangular-cell surface axis that none of the sixteen existing
legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands) — NO verticals
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid CONTINUOUS CROSSING DIAGONAL lines -> diamond/lozenge mesh
  * 15th axis laid OVERLAPPING CURVED ARCS -> an imbricated scale field
  * 16th axis laid SHORT alternating-slope diagonal DASHES -> herringbone / twill
  * 17th (this) lays a STAGGERED grid of closed RECTANGULAR CELLS -> ashlar masonry.
Distinct from the 12th (pure horizontal, no vertical joints, no offset), from the 14th
(diagonal diamond net, not axis-aligned rectangles), and from the 13th point grid
(closed line cells, not discrete dots). The half-brick OFFSET between courses is what
separates it from a plain rectangular grid.

Per slot it lands as the 17th distinct axis:
  * CHEST  — ashlar cuirass: dressed-stone brick bond over the whole cuirass.
  * LEGS   — ashlar chausses: brick bond over the thighs.
  * BOOTS  — ashlar sabatons: brick bond over the boot.
  * HELMET — ashlar dome / bastion helm: brick bond over the whole crown.

Authoring philosophy is identical to gen_twill_axis16.py / gen_scale_axis15.py:
mortar pixels are painted ONLY onto pixels that are ALREADY opaque body pixels.
Because it never adds a pixel outside the existing silhouette it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — QA-safe
purely by construction. Sleep frames (fi>=60, lying down) get the recolor only — no
masonry. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 16th (twill, cool frost-steel) and 15th
(scale, antique-bronze/verdigris), the ashlar family is a WARM SANDSTONE / BRASS tint
per class:
  * warrior — warm iron-brown body + BRASS-SANDSTONE mortar, umber shadow
  * mage    — arcane-violet body + PALE-GOLD mortar, indigo shadow
  * ranger  — forest body + COPPER mortar, bark shadow

Run from repo root:
  python3 scripts/gen_ashlar_axis17.py
Then QA (examples):
  python3 scripts/sprite_qa.py _ashlar_legendary_preview/shirt_warrior_legendary17.png
  python3 scripts/sprite_qa.py _ashlardome_helmet_preview/helmet_mage_legendary17.png --y-min 2
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Per-class ashlar palettes: (MORTAR bright joint, SHADOW dark bevel pixel).
MORTAR = {
    'warrior': ((214, 190, 140), (70, 54, 34)),      # brass / sandstone, umber
    'mage':    ((222, 200, 150), (46, 30, 70)),      # pale gold, indigo
    'ranger':  ((198, 150, 96), (44, 40, 22)),       # copper, bark
}

# Per-class body tones: deep shadow / base / highlight. Warm variants so the set reads
# apart from the cool frost-steel twill 16th axis.
BODY = {
    'warrior': ((36, 30, 24), (86, 74, 58), (140, 124, 100)),   # warm iron-brown
    'mage':    ((26, 18, 48), (60, 44, 112), (124, 100, 190)),  # arcane violet
    'ranger':  ((22, 38, 18), (52, 84, 40), (104, 148, 80)),    # forest green
}

# One config block per slot. `largest` restricts the masonry to the biggest connected
# component (torso / dome) so raised arms are not bricked; boots/legs brick all opaque
# pixels (both limbs). `period` = brick-course height in px (brick width = 2*period).
SLOTS = {
    'chest': dict(
        outdir='_ashlar_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary17', period=4, largest=True,
    ),
    'legs': dict(
        outdir='_ashlar_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary17', period=3, largest=False,
    ),
    'boots': dict(
        outdir='_ashlar_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_ashlar', period=3, largest=False,
    ),
    'helmet': dict(
        outdir='_ashlardome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary17', period=3, largest=True,
    ),
}


def load_any(fname):
    """Load a source sheet; if the female (_f) variant is absent (warrior boots are a
    single gender-shared sheet), fall back to the base sheet."""
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_ashlar(fr, comp, mortar, shadow, period):
    """Paint an ashlar / brick-bond field onto one component. The component's bounding
    box is divided into horizontal COURSES of height `period`. A full-width horizontal
    mortar line is drawn at the top of each course, and short vertical joints are drawn
    within each course every `2*period` columns; the joint columns are OFFSET by
    `period` on every other course, producing the staggered running bond that defines
    masonry. A dark bevel SHADOW pixel is painted one row under each horizontal mortar
    pixel where that pixel is opaque and not itself mortar, giving carved-stone relief.
    Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    opaque = set(zip(ys.tolist(), xs.tolist()))

    p = max(2, period)
    brick_w = 2 * p
    mort = set()
    for y in range(y0, y1 + 1):
        course = (y - y0) // p
        row_in_course = (y - y0) % p
        # horizontal mortar line at the top row of each course
        if row_in_course == 0:
            for x in range(x0, x1 + 1):
                if (y, x) in opaque:
                    mort.add((y, x))
        # vertical joints inside the course body, staggered half a brick per course
        offset = p if (course % 2) else 0
        for x in range(x0, x1 + 1):
            if ((x - x0 - offset) % brick_w) == 0 and (y, x) in opaque:
                mort.add((y, x))

    for (y, x) in mort:
        put(fr, y, x, mortar)
    for (y, x) in mort:
        if (y + 1, x) in opaque and (y + 1, x) not in mort:
            put(fr, y + 1, x, shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    mortar, shadow = MORTAR[cls]
    period, largest = cfg['period'], cfg['largest']
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
        if largest:
            lbl, n = ndimage.label(a)
            if n >= 1:
                sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
                comp = (lbl == (int(np.argmax(sizes)) + 1))
            else:
                comp = a
        else:
            comp = a
        draw_ashlar(fr, comp, mortar, shadow, period)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                arr = shade(arr, adj_min=-0.20, adj_max=0.25)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                Image.fromarray(arr).save(dst)
                print('wrote %-52s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
