#!/usr/bin/env python3
"""TWENTY-SECOND net-new-geometry axis for ALL FOUR SLOTS — the WAVE / WATERED-STEEL
(DAMASCUS) family: an all-over field of CONTINUOUS UNDULATING SINE lines running across
the body. The repeated motif of this axis is a single connected WAVY LINE — a smooth
sinusoid — with many parallel wavy lines stacked to give the rippling "watered steel"
(Damascus / pattern-welded) surface. This is the CONTINUOUS-SINUOUS-CURVE axis that none
of the twenty-one existing legendary axes per slot occupy:
  * 11th axis laid CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid TWO crossing STRAIGHT diagonal families -> lozenge/diamond mesh
  * 15th axis laid OVERLAPPING SHORT CURVED ARCS -> imbricated scale field (open arcs)
  * 16th axis laid SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone/twill
  * 17th axis laid a STAGGERED grid of closed RECTANGULAR cells -> ashlar
  * 18th axis laid a CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th axis laid a tessellation of SIX-sided cells -> honeycomb
  * 20th axis laid THREE STRAIGHT line families -> THREE-sided cells -> trellis
  * 21st axis laid a staggered grid of closed CIRCLES -> chainmail rings
  * 22nd (this) lays CONTINUOUS UNDULATING SINE lines -> watered-steel ripple.
Distinct from every straight-line axis (flute / lamellar / twill / lattice / trellis)
because each line CURVES continuously — it is neither straight nor broken into segments.
Distinct from the 15th scale axis, whose motifs are SHORT DISCRETE downward arcs that do
NOT connect end-to-end; a watered line is one UNBROKEN sinusoid spanning the whole width.
Distinct from the 21st chainmail axis because nothing here closes into a loop/cell — the
lines are OPEN and run edge to edge. The CONTINUOUS-WAVY-LINE motif is what separates it
from every prior axis.

Per slot it lands as the 22nd distinct axis:
  * CHEST  — watered-steel cuirass: ripple field over the whole cuirass.
  * LEGS   — watered chausses: ripple field over the thighs.
  * BOOTS  — watered sabatons: ripple field over the boot.
  * HELMET — watered dome: ripple field over the whole crown.

Authoring philosophy is identical to gen_chainmail_axis21.py / gen_trellis_axis20.py:
ripple pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction.
Sleep frames (fi>=60, lying down) get the recolor only — no net. Shading applied in this
script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 21st (chainmail, blued-steel body + bright
steel RING seam) the wave family is a WARM WATERED / DAMASCUS steel: a smoky warm-tinted
body per class with a pale PEARL ripple seam. The shared pale ripple reads instantly as
"watered/Damascus steel" while the warm body tint distinguishes the class:
  * warrior — warm brown-steel body + pale silver-pearl ripple, dark umber shadow
  * mage    — violet-steel body + pale ice ripple, blue-black shadow
  * ranger  — teal-steel body + pale jade ripple, deep-teal shadow

Run from repo root:
  python3 scripts/gen_wave_axis22.py
Then QA (examples):
  python3 scripts/sprite_qa.py _wave_legendary_preview/shirt_warrior_legendary22.png
  python3 scripts/sprite_qa.py _wavedome_helmet_preview/helmet_mage_legendary22.png --y-min 2
  python3 scripts/sprite_qa.py _wave_boots_preview/boots_warrior_legendary_wave.png --y-max 63
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

# Per-class seam palettes: (RIPPLE bright pearl pixel, SHADOW dark under-ripple pixel).
SEAM = {
    'warrior': ((226, 216, 194), (40, 32, 22)),      # pale silver-pearl ripple, umber shadow
    'mage':    ((208, 212, 238), (22, 22, 46)),       # pale ice ripple, blue-black shadow
    'ranger':  ((210, 230, 222), (16, 34, 30)),       # pale jade ripple, deep-teal shadow
}

# Per-class body tones: deep shadow / base / highlight. WARM WATERED steel variants so the
# set reads apart from chainmail's cold blued body + steel rings (21st): here the body is a
# warmer, smokier tinted steel, and the seam is a pale watered ripple, not a ring.
BODY = {
    'warrior': ((34, 30, 26), (82, 74, 62), (134, 122, 102)),   # warm brown-steel
    'mage':    ((34, 24, 46), (76, 56, 106), (130, 102, 172)),  # violet steel
    'ranger':  ((22, 34, 34), (52, 82, 78), (98, 142, 136)),    # teal steel
}

# One config block per slot. `largest` restricts the net to the biggest connected
# component (torso / dome) so raised arms are not rippled; boots/legs ripple all opaque
# pixels (both limbs). `sp` = vertical line spacing (px); `A` = wave amplitude (px);
# `lam` = wavelength (px). A stays < sp so adjacent wavy lines never touch.
SLOTS = {
    'chest': dict(
        outdir='_wave_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary22', sp=4.5, A=1.3, lam=6.0, largest=True,
    ),
    'legs': dict(
        outdir='_wave_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary22', sp=3.5, A=1.0, lam=5.0, largest=False,
    ),
    'boots': dict(
        outdir='_wave_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_wave', sp=3.5, A=1.0, lam=5.0, largest=False,
    ),
    'helmet': dict(
        outdir='_wavedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary22', sp=3.5, A=1.0, lam=5.0, largest=True,
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


def draw_wave(fr, comp, seam, shadow, sp, A, lam):
    """Paint a field of CONTINUOUS UNDULATING SINE lines onto one component. Each wavy line
    k follows y = k*sp + A*sin(2*pi*x/lam); a pixel is a RIPPLE (seam) pixel when its
    vertical distance to the nearest such wavy line is within half a pixel -> it lies on the
    crest curve. A dark under-ripple SHADOW pixel below each ripple pixel (where opaque and
    not itself a ripple) gives the watered steel its raised, rolling relief. Only opaque
    body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    # Anchor phase to the component's top-left so the ripple is stable across frames.
    y0, x0 = float(ys.min()), float(xs.min())
    py = ys.astype(np.float32) - y0
    px = xs.astype(np.float32) - x0

    # Vertical offset of the wavy lines at each pixel's x, then distance to nearest line.
    offset = A * np.sin(2.0 * math.pi * px / lam)
    r = (py - offset) / sp
    d = np.abs(r - np.round(r)) * sp
    on_wave = d < 0.55

    opaque = set(zip(ys.tolist(), xs.tolist()))
    ripple_px = set()
    for yy, xx, s in zip(ys.tolist(), xs.tolist(), on_wave.tolist()):
        if s:
            ripple_px.add((yy, xx))
            put(fr, yy, xx, seam)
    # under-ripple relief: one pixel below each ripple pixel, if opaque and not a ripple
    for (yy, xx) in ripple_px:
        nb = (yy + 1, xx)
        if nb in opaque and nb not in ripple_px:
            put(fr, nb[0], nb[1], shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    seam, shadow = SEAM[cls]
    sp, A, lam, largest = cfg['sp'], cfg['A'], cfg['lam'], cfg['largest']
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
        draw_wave(fr, comp, seam, shadow, sp, A, lam)
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
                print('wrote %-54s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
