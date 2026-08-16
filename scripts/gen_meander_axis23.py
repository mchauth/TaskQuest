#!/usr/bin/env python3
"""TWENTY-THIRD net-new-geometry axis for ALL FOUR SLOTS — the MEANDER / GREEK-KEY
(FRET) family: an all-over field of a CONTINUOUS RECTILINEAR line that turns only at
RIGHT ANGLES and repeatedly hooks inward into small SQUARE SPIRALS, then runs on to the
next hook along a shared horizontal rail. The repeated motif is the interlocking square
spiral of the classical Greek key border. This is the RECTILINEAR-RIGHT-ANGLE-SPIRAL axis
that none of the twenty-two existing legendary axes per slot occupy:
  * 11th laid CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th laid CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th laid TWO crossing STRAIGHT diagonal families -> lozenge/diamond mesh
  * 15th laid OVERLAPPING SHORT CURVED ARCS -> imbricated scale field
  * 16th laid SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone/twill
  * 17th laid a STAGGERED grid of closed RECTANGULAR cells -> ashlar brick-bond
  * 18th laid a CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th laid a tessellation of SIX-sided cells -> honeycomb
  * 20th laid THREE STRAIGHT line families -> THREE-sided cells -> trellis
  * 21st laid a staggered grid of closed CIRCLES -> chainmail rings
  * 22nd laid CONTINUOUS UNDULATING SINE lines -> watered-steel ripple
  * 23rd (this) lays a CONTINUOUS line that turns only at RIGHT ANGLES and coils into
    repeated SQUARE SPIRAL HOOKS -> Greek-key / meander fret.
Distinct from the 22nd wave axis because every turn is a hard 90-degree corner, never a
curve. Distinct from the straight-line axes (flute / lamellar / twill / lattice / trellis)
because the line does not run straight edge to edge — it coils inward into a hook and back
out. Distinct from the closed-cell axes (ashlar / basketweave / honeycomb / chainmail)
because nothing closes into a cell; it is one OPEN spiralling line. The RIGHT-ANGLE INWARD
SPIRAL is the motif that separates it from every prior axis.

Per slot it lands as the 23rd distinct axis:
  * CHEST  — key-fret cuirass: meander band field over the whole cuirass.
  * LEGS   — key-fret chausses: meander field over the thighs.
  * BOOTS  — key-fret sabatons: meander field over the boot.
  * HELMET — key-fret dome: meander field over the whole crown.

Authoring philosophy is identical to gen_wave_axis22.py / gen_chainmail_axis21.py: fret
pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never
adds a pixel outside the existing silhouette it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — QA-safe by construction. Sleep frames
(fi>=60, lying down) get the recolor only — no fret. Shading applied in this script via
shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 22nd (wave, warm watered body + pale pearl
ripple) the meander family is an ANTIQUE / classical look: a dark OXIDIZED-metal body per
class with a bright ANTIQUE-GOLD key line and a dark under-shadow giving the fret raised
relief. The shared bright gold fret reads instantly as "gilded Greek key" while the dark
body tint distinguishes the class:
  * warrior — dark oxidized bronze body + antique-gold key, umber shadow
  * mage    — dark indigo body + pale-gold key, blue-black shadow
  * ranger  — dark forest-bronze body + antique-gold key, deep-green shadow

Run from repo root:
  python3 scripts/gen_meander_axis23.py
Then QA (examples):
  python3 scripts/sprite_qa.py _meander_legendary_preview/shirt_warrior_legendary23.png
  python3 scripts/sprite_qa.py _meanderdome_helmet_preview/helmet_mage_legendary23.png --y-min 2
  python3 scripts/sprite_qa.py _meander_boots_preview/boots_warrior_legendary_meander.png --y-max 63
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

# One square-spiral Greek-key hook. Row 0 is the shared horizontal rail that connects
# every hook in a band left-to-right (the meander is one continuous line). PW columns wide,
# PH rows tall; tiled horizontally with no gap so the rail is unbroken, and stacked
# vertically with GAP blank rows between bands so adjacent bands never touch.
PATTERN = [
    "1111111",   # rail — continuous across the whole band
    "0000010",   # drop into the hook at the right
    "0111010",   # inner top of the spiral
    "0101010",   # spiral walls
    "0100010",
    "0111110",   # bottom of the spiral
]
PH = len(PATTERN)
PW = len(PATTERN[0])
GAP = 2                      # blank rows between stacked meander bands
VPERIOD = PH + GAP
_STAMP = np.array([[c == '1' for c in row] for row in PATTERN], dtype=bool)

# Per-class fret palettes: (KEY bright gold line pixel, SHADOW dark under-key pixel).
SEAM = {
    'warrior': ((224, 188, 96), (44, 30, 12)),        # antique gold key, umber shadow
    'mage':    ((232, 214, 150), (20, 20, 44)),        # pale gold key, blue-black shadow
    'ranger':  ((214, 190, 110), (14, 30, 18)),        # antique gold key, deep-green shadow
}

# Per-class body tones: deep shadow / base / highlight. DARK OXIDIZED-metal variants so the
# set reads apart from wave's warm watered body: here the body is a dark antique metal and
# the seam is a bright gilded key, not a pale ripple.
BODY = {
    'warrior': ((26, 20, 12), (66, 50, 28), (108, 84, 48)),   # oxidized bronze
    'mage':    ((20, 18, 38), (48, 44, 88), (86, 80, 140)),   # dark indigo
    'ranger':  ((16, 26, 16), (44, 62, 40), (78, 106, 70)),   # forest bronze
}

# One config block per slot. `largest` restricts the fret to the biggest connected
# component (torso / dome) so raised arms are not fretted; boots/legs fret all opaque
# pixels (both limbs).
SLOTS = {
    'chest': dict(
        outdir='_meander_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary23', largest=True,
    ),
    'legs': dict(
        outdir='_meander_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary23', largest=False,
    ),
    'boots': dict(
        outdir='_meander_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_meander', largest=False,
    ),
    'helmet': dict(
        outdir='_meanderdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary23', largest=True,
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


def draw_meander(fr, comp, seam, shadow):
    """Paint a field of interlocking Greek-key SQUARE-SPIRAL hooks onto one component. The
    hook stamp is tiled across the component's bounding box (anchored to its top-left so the
    fret is stable across frames): horizontally with no gap so the top rail is continuous,
    vertically with GAP blank rows between bands. A pixel is a KEY (seam) pixel when the
    tiled stamp is on there AND the pixel is opaque body. A dark under-key SHADOW pixel below
    each key pixel (where opaque and not itself a key) gives the fret its raised relief. Only
    opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())

    opaque = set(zip(ys.tolist(), xs.tolist()))
    key_px = set()
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        ry = (yy - y0) % VPERIOD
        if ry >= PH:                       # in the vertical gap between bands
            continue
        rx = (xx - x0) % PW
        if _STAMP[ry, rx]:
            key_px.add((yy, xx))
            put(fr, yy, xx, seam)
    # under-key relief: one pixel below each key pixel, if opaque and not a key
    for (yy, xx) in key_px:
        nb = (yy + 1, xx)
        if nb in opaque and nb not in key_px:
            put(fr, nb[0], nb[1], shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    seam, shadow = SEAM[cls]
    largest = cfg['largest']
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
        draw_meander(fr, comp, seam, shadow)
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
