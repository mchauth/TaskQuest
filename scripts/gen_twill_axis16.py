#!/usr/bin/env python3
"""SIXTEENTH net-new-geometry axis for ALL FOUR SLOTS — the HERRINGBONE / TWILL family:
a tessellated field of SHORT diagonal dashes whose slope ALTERNATES column-to-column,
i.e. forged twill / herringbone weave (\\/\\/\\/). This is the repeated
alternating-diagonal-DASH surface axis that none of the fifteen existing legendary
axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid CONTINUOUS CROSSING DIAGONAL lines -> diamond/lozenge mesh
  * 15th axis laid OVERLAPPING CURVED ARCS -> an imbricated scale field
  * 16th (this) lays SHORT diagonal dashes that FLIP slope every column -> herringbone.
The dashes are SHORT (never crossing, never continuous) and MIRROR direction between
neighbouring columns, so it is geometrically distinct from the continuous crossing
diagonals of the 14th (which form a closed diamond net) and from every straight/curved
continuous-line or point-grid axis.

Per slot it lands as the 16th distinct axis:
  * CHEST  — twill cuirass: herringbone weave over the whole cuirass.
  * LEGS   — twill chausses: herringbone over the thighs.
  * BOOTS  — twill sabatons: herringbone over the boot.
  * HELMET — twill coif/dome: herringbone over the whole crown.

Authoring philosophy is identical to gen_scale_axis15.py / gen_lattice_axis14.py:
twill pixels are painted ONLY onto pixels that are ALREADY opaque body pixels.
Because it never adds a pixel outside the existing silhouette it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — QA-safe
purely by construction. Sleep frames (fi>=60, lying down) get the recolor only — no
weave. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 15th (scale, antique-bronze/verdigris)
and 14th (lattice, platinum/amethyst/sage), the twill family is a COOL FROST-STEEL
tint per class:
  * warrior — obsidian/steel body + FROST-SILVER twill, slate shadow
  * mage    — arcane-violet body + ICE-CYAN twill, indigo shadow
  * ranger  — forest body + PEWTER twill, moss shadow

Run from repo root:
  python3 scripts/gen_twill_axis16.py
Then QA (examples):
  python3 scripts/sprite_qa.py _twill_legendary_preview/shirt_warrior_legendary16.png
  python3 scripts/sprite_qa.py _twilldome_helmet_preview/helmet_mage_legendary16.png --y-min 2
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

# Per-class twill palettes: (DASH bright weave, SHADOW dark bevel pixel).
TWILL = {
    'warrior': ((202, 214, 230), (58, 70, 88)),      # frost silver, slate shadow
    'mage':    ((150, 208, 226), (28, 32, 84)),      # ice cyan, indigo
    'ranger':  ((176, 186, 190), (40, 56, 34)),      # pewter, moss
}

# Per-class body tones: deep shadow / base / highlight (same legendary base tones
# shared across the net-new-geometry axes).
BODY = {
    'warrior': ((28, 30, 36), (74, 78, 90), (128, 134, 150)),   # obsidian -> steel
    'mage':    ((20, 16, 54), (54, 42, 122), (120, 96, 200)),   # arcane violet
    'ranger':  ((20, 40, 18), (48, 88, 42), (98, 150, 82)),     # forest green
}

# One config block per slot. `largest` restricts the weave to the biggest connected
# component (torso / dome) so raised arms are not woven; boots/legs weave all opaque
# pixels (both limbs). `period` = herringbone cell size in px.
SLOTS = {
    'chest': dict(
        outdir='_twill_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary16', period=4, largest=True,
    ),
    'legs': dict(
        outdir='_twill_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary16', period=3, largest=False,
    ),
    'boots': dict(
        outdir='_twill_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_twill', period=3, largest=False,
    ),
    'helmet': dict(
        outdir='_twilldome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary16', period=3, largest=True,
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


def draw_twill(fr, comp, dash, shadow, period):
    """Paint a herringbone / twill field onto one component. The component's bounding
    box is tiled into cells of size `period`x`period`. In each cell a SHORT diagonal
    dash is drawn corner-to-corner; the dash slope FLIPS every cell-column so adjacent
    columns mirror, forming the classic \\/\\/ herringbone. A dark bevel SHADOW pixel is
    painted one row under each dash where that pixel is opaque and not itself a dash,
    giving woven relief. Only opaque body pixels are ever painted, so it cannot create
    strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    opaque = set(zip(ys.tolist(), xs.tolist()))

    p = max(2, period)
    dashes = set()
    col = 0
    cx = x0
    while cx <= x1:
        down = (col % 2 == 0)          # alternate slope per cell-column
        cy = y0
        while cy <= y1:
            for t in range(p):
                x = cx + t
                y = cy + (t if down else (p - 1 - t))
                if (y, x) in opaque:
                    dashes.add((y, x))
            cy += p
        cx += p
        col += 1

    for (y, x) in dashes:
        put(fr, y, x, dash)
    for (y, x) in dashes:
        if (y + 1, x) in opaque and (y + 1, x) not in dashes:
            put(fr, y + 1, x, shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    dash, shadow = TWILL[cls]
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
        draw_twill(fr, comp, dash, shadow, period)
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
