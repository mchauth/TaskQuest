#!/usr/bin/env python3
"""FIFTEENTH net-new-geometry axis for ALL FOUR SLOTS — the SCALE / SQUAMATA family:
a field of imbricated (overlapping, half-drop offset) curved scales tiled across the
piece, i.e. dragon/fish scale-mail. This is the repeated-CURVED-ARC surface axis that
none of the fourteen existing legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid CROSSING DIAGONAL straight lines -> diamond/lozenge mesh
  * 15th (this) lays OVERLAPPING CURVED ARCS -> an imbricated scale field.
Curvature (arcs, not straight segments) + half-drop imbrication (each row offset by
half a scale and overlapping the row below) make it a distinct geometric primitive
from all four repeated axes, and from every one-boss / single-line axis.

Per slot it lands as the 15th distinct axis:
  * CHEST  — dragonscale cuirass: scaled skin over the whole cuirass.
  * LEGS   — scaled chausses: scale field over the thighs.
  * BOOTS  — scaled sabatons: scale field over the boot.
  * HELMET — scaled coif/dome: scale field over the whole crown.

Authoring philosophy is identical to gen_lattice_axis14.py / gen_stud_axis13.py:
scale pixels are painted ONLY onto pixels that are ALREADY opaque body pixels.
Because it never adds a pixel outside the existing silhouette it CANNOT create
isolated pixels, background bleed, or accent-caused multi-component frames — QA-safe
purely by construction. Sleep frames (fi>=60, lying down) get the recolor only — no
scales. Shading applied in-script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 14th (lattice, platinum/amethyst/sage),
the scale cap family is an ANTIQUE-BRONZE / VERDIGRIS tint per class:
  * warrior — obsidian/steel body + ANTIQUE-GOLD scale caps, verdigris shadow
  * mage    — arcane-violet body + JADE scale caps, deep-teal shadow
  * ranger  — forest body + BRASS scale caps, olive shadow

Run from repo root:
  python3 scripts/gen_scale_axis15.py
Then QA (examples):
  python3 scripts/sprite_qa.py _scale_legendary_preview/shirt_warrior_legendary15.png
  python3 scripts/sprite_qa.py _scaledome_helmet_preview/helmet_mage_legendary15.png --y-min 2
"""
import os
import sys
import math
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Per-class scale palettes: (CAP bright rim, SHADOW dark bevel pixel).
SCALE = {
    'warrior': ((196, 158, 86), (52, 66, 60)),      # antique gold, verdigris shadow
    'mage':    ((150, 205, 190), (22, 58, 54)),      # jade, deep-teal
    'ranger':  ((188, 166, 104), (46, 52, 30)),      # brass, olive
}

# Per-class body tones: deep shadow / base / highlight (same legendary base tones
# shared across the net-new-geometry axes).
BODY = {
    'warrior': ((28, 30, 36), (74, 78, 90), (128, 134, 150)),   # obsidian -> steel
    'mage':    ((20, 16, 54), (54, 42, 122), (120, 96, 200)),   # arcane violet
    'ranger':  ((20, 40, 18), (48, 88, 42), (98, 150, 82)),     # forest green
}

# One config block per slot. `largest` restricts scales to the biggest connected
# component (torso / dome) so raised arms are not scaled; boots/legs scale all opaque
# pixels (both limbs). `period` = scale WIDTH in px (row height derives from it).
SLOTS = {
    'chest': dict(
        outdir='_scale_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary15', period=5, largest=True,
    ),
    'legs': dict(
        outdir='_scaled_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary15', period=4, largest=False,
    ),
    'boots': dict(
        outdir='_scale_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_scale', period=4, largest=False,
    ),
    'helmet': dict(
        outdir='_scaledome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary15', period=4, largest=True,
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


def draw_scales(fr, comp, cap, shadow, period):
    """Paint an imbricated (overlapping, half-drop) field of curved scales onto one
    component. Scale centres sit on an offset grid: width `period`, row-height `ph`,
    every other row shifted half a period so scales interlock. For each scale we paint
    the lower rim ARC (a downward-bulging semicircle) — the visible edge of a scale
    lying over the one below. A dark bevel SHADOW pixel is painted one row under each
    rim where that pixel is opaque and not itself a rim, giving raised relief. Only
    opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    opaque = set(zip(ys.tolist(), xs.tolist()))

    pw = period
    ph = max(2, period - 1)          # scales wider than tall -> squat imbrication
    rx = pw / 2.0
    ry = float(ph)

    caps = set()
    j = 0
    y_base = y0
    while y_base <= y1 + ph:
        off = (pw // 2) if (j % 2) else 0
        cx = x0 + off - pw
        while cx <= x1 + pw:
            steps = max(8, pw * 2)
            for s in range(steps + 1):
                ang = math.pi * (s / steps)          # 0..pi -> lower semicircle
                px = int(round(cx + rx * math.cos(ang)))
                py = int(round(y_base + ry * math.sin(ang)))
                if (py, px) in opaque:
                    caps.add((py, px))
            cx += pw
        j += 1
        y_base += ph

    for (y, x) in caps:
        put(fr, y, x, cap)
    for (y, x) in caps:
        if (y + 1, x) in opaque and (y + 1, x) not in caps:
            put(fr, y + 1, x, shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    cap, shadow = SCALE[cls]
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
        draw_scales(fr, comp, cap, shadow, period)
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
