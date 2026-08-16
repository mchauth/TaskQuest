#!/usr/bin/env python3
"""TWENTY-FOURTH net-new-geometry axis for ALL FOUR SLOTS — the SPIRAL / VOLUTE / WHORL
family: an all-over field of tiled CURVED SPIRAL coils. Each tile carries one continuous
CURVED line that winds around a central point, its radius growing steadily with angle
(an Archimedean whorl — snail-shell / ionic-volute / fingerprint look). The repeated motif
is the CONTINUOUS CURVED COIL WINDING AROUND A CENTRE. This is the curved-spiral axis that
none of the twenty-three existing legendary axes per slot occupy:
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
  * 23rd laid a CONTINUOUS line turning only at RIGHT ANGLES into square-spiral hooks -> meander
  * 24th (this) lays CONTINUOUS CURVED COILS winding around centres -> spiral / volute whorl.
Distinct from the 23rd meander because the coil is a smooth CURVE, never a right-angle turn.
Distinct from the 22nd wave because the line does not translate along a rail — it WINDS
AROUND a fixed centre, radius growing with angle. Distinct from the 15th scale (short open
arcs that do not encircle a centre) and the 21st chainmail (closed same-radius rings that
never coil). The CURVED INWARD/OUTWARD COIL AROUND A CENTRE is the motif that separates it
from every prior axis.

Per slot it lands as the 24th distinct axis:
  * CHEST  — volute cuirass: whorl field over the whole cuirass.
  * LEGS   — volute chausses: whorl field over the thighs.
  * BOOTS  — volute sabatons: whorl field over the boot.
  * HELMET — volute dome: whorl field over the whole crown.

Authoring philosophy is identical to gen_meander_axis23.py / gen_wave_axis22.py: spiral
pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never
adds a pixel outside the existing silhouette it CANNOT create isolated pixels, background
bleed, or accent-caused multi-component frames — QA-safe by construction. Sleep frames
(fi>=60, lying down) get the recolor only — no spiral. Shading applied in this script via
shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 23rd (meander, dark oxidized-metal body +
antique-gold key) the volute family is a VERDIGRIS / patinated-copper look: a teal-green
oxidized-copper body per class with a bright warm COPPER-ROSE coil line and a dark
under-shadow giving the coil raised relief. The shared warm copper coil over a cool teal
body reads instantly as "patinated bronze whorl" while the body tint distinguishes class:
  * warrior — deep verdigris teal body + bright rose-copper coil, dark-teal shadow
  * mage    — dark teal-indigo body + pale aqua-copper coil, blue-black shadow
  * ranger  — dark moss-teal body + antique-copper coil, deep-green shadow

Run from repo root:
  python3 scripts/gen_spiral_axis24.py
Then QA (examples):
  python3 scripts/sprite_qa.py _spiral_legendary_preview/shirt_warrior_legendary24.png
  python3 scripts/sprite_qa.py _spiraldome_helmet_preview/helmet_mage_legendary24.png --y-min 2
  python3 scripts/sprite_qa.py _spiral_boots_preview/boots_warrior_legendary_spiral.png --y-max 63
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

# Whorl geometry. Each tile is TILE x TILE and holds one Archimedean spiral centred in it.
# A pixel is on the coil when its radius from the tile centre is close (within THICK) to
# PITCH * (angle / 2pi) plus an integer number of PITCH steps — i.e. r grows by PITCH per
# full turn. Tiles are laid on a fixed grid anchored to the component bbox top-left so the
# field is stable frame-to-frame. Adjacent tiles alternate spin direction (a chirality
# checker) so the field reads as an interlocked whorl weave, not a grid of identical dots.
TILE = 12               # tile pitch (px)
PITCH = 3.0             # radial growth per full turn (px) -> ~2 coils inside the tile
THICK = 0.9             # half-thickness of the coil line, in the r-vs-target metric (px)
RMAX = 5.2              # outer radius of each whorl (px); < TILE/2 so tiles do not merge


# Per-class coil palettes: (COIL bright warm-copper line pixel, SHADOW dark under-coil px).
SEAM = {
    'warrior': ((222, 138, 96), (18, 40, 40)),        # rose-copper coil, dark-teal shadow
    'mage':    ((176, 214, 210), (14, 22, 42)),        # pale aqua-copper coil, blue-black shadow
    'ranger':  ((206, 150, 104), (12, 32, 24)),        # antique-copper coil, deep-green shadow
}

# Per-class body tones: deep shadow / base / highlight. VERDIGRIS / patinated-copper teal
# variants so the set reads apart from meander's dark oxidized body: here the body is a cool
# teal-green oxidized copper and the coil is a warm bright copper, not a gilded key.
BODY = {
    'warrior': ((14, 40, 40), (34, 78, 74), (60, 118, 110)),   # verdigris teal
    'mage':    ((14, 30, 44), (36, 60, 86), (66, 100, 134)),   # teal-indigo
    'ranger':  ((14, 34, 30), (36, 66, 52), (64, 104, 82)),    # moss-teal
}

# One config block per slot. `largest` restricts the whorl field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs field all opaque
# pixels (both limbs).
SLOTS = {
    'chest': dict(
        outdir='_spiral_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary24', largest=True,
    ),
    'legs': dict(
        outdir='_spiral_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary24', largest=False,
    ),
    'boots': dict(
        outdir='_spiral_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_spiral', largest=False,
    ),
    'helmet': dict(
        outdir='_spiraldome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary24', largest=True,
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


def draw_spiral(fr, comp, seam, shadow):
    """Paint a field of tiled Archimedean whorls onto one component. The tile grid is
    anchored to the component's bounding-box top-left so the field is stable across frames.
    Within each tile a pixel is a COIL pixel when its radius r from the tile centre is within
    THICK of PITCH*(angle/2pi) + k*PITCH for some integer k and r <= RMAX; adjacent tiles
    alternate spin (angle sign) via a checker so the whorls interlock rather than repeat.
    A dark under-coil SHADOW pixel one row below each coil pixel (where opaque and not itself
    a coil) gives the whorl raised relief. Only opaque body pixels are ever painted, so it
    cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())

    opaque = set(zip(ys.tolist(), xs.tolist()))
    key_px = set()
    half = TILE / 2.0
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        # tile index + local offset to tile centre
        tx = (xx - x0) // TILE
        ty = (yy - y0) // TILE
        lx = (xx - x0) - tx * TILE - half + 0.5
        ly = (yy - y0) - ty * TILE - half + 0.5
        r = (lx * lx + ly * ly) ** 0.5
        if r > RMAX or r < 0.35:            # outside whorl / dead centre
            continue
        spin = 1.0 if ((tx + ty) & 1) == 0 else -1.0
        ang = np.arctan2(spin * ly, lx)     # [-pi, pi]
        frac = (ang / (2.0 * np.pi)) % 1.0  # [0,1) position within a turn
        target = frac * PITCH               # nearest coil radius below r, mod PITCH
        d = (r - target) % PITCH
        d = min(d, PITCH - d)               # signed distance to closest coil arm
        if d <= THICK:
            key_px.add((yy, xx))
            put(fr, yy, xx, seam)
    # under-coil relief: one pixel below each coil pixel, if opaque and not a coil
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
        draw_spiral(fr, comp, seam, shadow)
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
