#!/usr/bin/env python3
"""FOURTEENTH net-new-geometry axis for ALL FOUR SLOTS — the LATTICE / DIAPER family:
a crossing DIAGONAL net of raised bright lines forming a lozenge (diamond) mesh tiled
across the piece. This is the repeated-DIAGONAL-LATTICE surface axis that none of the
thirteen existing legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th (this) lays CROSSING DIAGONAL lines -> a continuous diamond/lozenge mesh.
Orientation (diagonal) + topology (crossing net of lozenges) make it a distinct
geometric primitive from all three, and from every one-boss / single-line axis.

Per slot it lands as the 14th distinct axis:
  * CHEST  — lattice cuirass: gilt diamond diaper across the whole cuirass.
  * LEGS   — diamond chausses: lozenge net over the thighs.
  * BOOTS  — latticed warboots: diamond mesh over the boot.
  * HELMET — latticed dome: diamond net over the whole crown.

Authoring philosophy is identical to gen_stud_axis13.py / gen_lamellar_legendary.py:
lattice pixels are painted ONLY onto pixels that are ALREADY opaque body pixels.
Because it never adds a pixel outside the existing silhouette it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — QA-safe
purely by construction. Sleep frames (fi>=60, lying down) get the recolor only — no
lattice. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 13th (studwork, gold/cyan/copper caps),
the lattice cap family is a PLATINUM/MITHRIL tint per class:
  * warrior — obsidian/steel body + PLATINUM lattice, dark-steel bevel shadow
  * mage    — arcane-violet body + LIGHT-AMETHYST lattice, deep-indigo shadow
  * ranger  — forest body + PALE-SAGE lattice, dark-bark shadow

Run from repo root:
  python3 scripts/gen_lattice_axis14.py
Then QA (examples):
  python3 scripts/sprite_qa.py _lattice_legendary_preview/shirt_warrior_legendary14.png
  python3 scripts/sprite_qa.py _latticedome_helmet_preview/helmet_mage_legendary14.png --y-min 2
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

# Per-class lattice palettes: (CAP bright line, SHADOW dark bevel pixel).
LATT = {
    'warrior': ((214, 222, 236), (58, 64, 80)),     # platinum, dark-steel shadow
    'mage':    ((196, 150, 240), (30, 24, 78)),      # light-amethyst, deep-indigo
    'ranger':  ((178, 208, 150), (34, 46, 24)),      # pale-sage, dark-bark
}

# Per-class body tones: deep shadow / base / highlight (same legendary base tones
# shared across the net-new-geometry axes).
BODY = {
    'warrior': ((28, 30, 36), (74, 78, 90), (128, 134, 150)),   # obsidian -> steel
    'mage':    ((20, 16, 54), (54, 42, 122), (120, 96, 200)),   # arcane violet
    'ranger':  ((20, 40, 18), (48, 88, 42), (98, 150, 82)),     # forest green
}

# One config block per slot. `largest` restricts the lattice to the biggest connected
# component (torso / dome) so raised arms are not netted; boots/legs net all opaque
# pixels (both limbs). `period` = diagonal spacing of the lattice lines in px.
SLOTS = {
    'chest': dict(
        outdir='_lattice_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary14', period=5, largest=True,
    ),
    'legs': dict(
        outdir='_diamond_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary14', period=5, largest=False,
    ),
    'boots': dict(
        outdir='_lattice_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_lattice', period=4, largest=False,
    ),
    'helmet': dict(
        outdir='_latticedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary14', period=4, largest=True,
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


def draw_lattice(fr, comp, cap, shadow, period):
    """Paint a crossing diagonal lattice (diamond diaper) onto one component. A pixel
    lies on the mesh when it sits on either diagonal family:
        (dx + dy) % period == 0   (one diagonal direction)
        (dx - dy) % period == 0   (the other)
    Cap pixels are painted on the mesh lines; a dark bevel SHADOW pixel is painted one
    row below each cap where that pixel is itself opaque and NOT itself a mesh line,
    giving the net a raised look. Never paints outside the component, so it cannot
    create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    opaque = set(zip(ys.tolist(), xs.tolist()))

    def on_mesh(y, x):
        dy, dx = y - y0, x - x0
        return ((dx + dy) % period == 0) or ((dx - dy) % period == 0)

    caps = [(y, x) for (y, x) in opaque if on_mesh(y, x)]
    for (y, x) in caps:
        put(fr, y, x, cap)
    for (y, x) in caps:
        if (y + 1, x) in opaque and not on_mesh(y + 1, x):
            put(fr, y + 1, x, shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    cap, shadow = LATT[cls]
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
        draw_lattice(fr, comp, cap, shadow, period)
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
