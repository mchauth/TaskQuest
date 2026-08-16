#!/usr/bin/env python3
"""TWENTY-FIRST net-new-geometry axis for ALL FOUR SLOTS — the CHAINMAIL / RING-MAIL
family: an all-over field of small interlinked CIRCULAR RINGS (annuli). The closed cell
of this axis is a CIRCLE — a repeated grid of tiny O-shaped rings, offset row-to-row like
real riveted mail, so the eye reads a sheet of interlocking metal loops. This is the
ANNULAR / closed-curve surface axis that none of the twenty existing legendary axes per
slot occupy:
  * 11th axis laid CONTINUOUS VERTICAL parallel lines (fluting)
  * 12th axis laid CONTINUOUS HORIZONTAL parallel lines (lamellar bands)
  * 13th axis laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th axis laid TWO crossing diagonal families -> FOUR-sided lozenge/diamond mesh
  * 15th axis laid OVERLAPPING CURVED ARCS -> an imbricated scale field (OPEN arcs)
  * 16th axis laid SHORT alternating-slope DIAGONAL dashes -> herringbone / twill
  * 17th axis laid a STAGGERED grid of closed RECTANGULAR (4-sided) CELLS -> ashlar
  * 18th axis laid a CHECKER of perpendicular SHORT-THREAD BUNDLES -> basketweave
  * 19th axis laid a tessellation of SIX-sided CELLS -> honeycomb
  * 20th axis laid THREE line families -> tessellation of THREE-sided CELLS -> trellis
  * 21st (this) laid a staggered grid of CLOSED CIRCLES -> chainmail rings.
Distinct from the 15th scale field, whose motifs are OPEN downward arcs (each scale is a
single curved segment, not a closed loop): a mail ring is a COMPLETE closed circle. And
distinct from every polygon axis (triangle/rectangle/hexagon/diamond) because a circle has
no straight sides or corners — it is a smooth closed curve. The CLOSED-CIRCLE cell is what
separates it from every prior axis.

Per slot it lands as the 21st distinct axis:
  * CHEST  — chainmail hauberk: ring field over the whole cuirass.
  * LEGS   — chainmail chausses: ring field over the thighs.
  * BOOTS  — mail sabatons: ring field over the boot.
  * HELMET — mail coif / ringmail dome: ring field over the whole crown.

Authoring philosophy is identical to gen_trellis_axis20.py / gen_honeycomb_axis19.py:
ring pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction.
Sleep frames (fi>=60, lying down) get the recolor only — no net. Shading applied in
this script via shade(); do NOT run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 20th (trellis, SILVER triangle net over a
metallic body) the chainmail family is a BLUED-STEEL ring mail: a dark blued-iron body per
class with a bright common polished-STEEL ring seam. The shared steel ring field reads
instantly as "mail" while the blued body tint distinguishes the class:
  * warrior — gunmetal / blued-steel body + bright steel rings, black-iron shadow
  * mage    — blue-steel body + steel rings, blue-black shadow
  * ranger  — green-steel body + steel rings, deep-forest shadow

Run from repo root:
  python3 scripts/gen_chainmail_axis21.py
Then QA (examples):
  python3 scripts/sprite_qa.py _chainmail_legendary_preview/shirt_warrior_legendary21.png
  python3 scripts/sprite_qa.py _chaincoif_helmet_preview/helmet_mage_legendary21.png --y-min 2
  python3 scripts/sprite_qa.py _chainmail_boots_preview/boots_warrior_legendary_chainmail.png --y-max 63
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

# Per-class seam palettes: (RING bright steel pixel, SHADOW dark under-ring pixel).
SEAM = {
    'warrior': ((200, 206, 214), (26, 22, 18)),      # steel ring, black-iron shadow
    'mage':    ((196, 204, 220), (20, 20, 44)),       # steel ring, blue-black shadow
    'ranger':  ((196, 208, 206), (16, 30, 24)),       # steel ring, deep-forest shadow
}

# Per-class body tones: deep shadow / base / highlight. Blued-steel variants so the set
# reads apart from trellis's warm/indigo/olive metallic body + silver seam (20th): here
# the body is a colder BLUED IRON, darker and more desaturated.
BODY = {
    'warrior': ((30, 32, 38), (74, 80, 92), (120, 128, 144)),   # gunmetal blued steel
    'mage':    ((22, 26, 50), (52, 60, 108), (98, 108, 178)),   # blue steel
    'ranger':  ((22, 32, 26), (54, 74, 58), (100, 128, 104)),   # green steel
}

# One config block per slot. `largest` restricts the net to the biggest connected
# component (torso / dome) so raised arms are not netted; boots/legs net all opaque
# pixels (both limbs). `sp` = ring center spacing in px; `R` = ring radius in px
# (R must be < sp/2 so adjacent rings do not merge).
SLOTS = {
    'chest': dict(
        outdir='_chainmail_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary21', sp=5.0, R=1.7, largest=True,
    ),
    'legs': dict(
        outdir='_chainmail_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary21', sp=4.0, R=1.4, largest=False,
    ),
    'boots': dict(
        outdir='_chainmail_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_chainmail', sp=4.0, R=1.4, largest=False,
    ),
    'helmet': dict(
        outdir='_chaincoif_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary21', sp=4.0, R=1.4, largest=True,
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


def draw_chainmail(fr, comp, seam, shadow, sp, R):
    """Paint a field of small interlinked RINGS onto one component. Ring centers sit on a
    staggered grid (every other row offset by half a spacing, like real riveted mail). A
    pixel is a RING (seam) pixel when its distance to the nearest ring center is within
    half a pixel of the ring radius R -> it lies on the circle's rim. A dark under-ring
    SHADOW pixel below each ring pixel (where opaque and not itself a ring) gives the mail
    its raised, interlocked relief. Only opaque body pixels are ever painted, so it cannot
    create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    # Anchor phase to the component's top-left so the net is stable across frames.
    y0, x0 = float(ys.min()), float(xs.min())
    py = ys.astype(np.float32) - y0
    px = xs.astype(np.float32) - x0

    # Nearest staggered ring center for each pixel.
    row = np.round(py / sp)
    cy = row * sp
    xoff = (row.astype(int) % 2) * (sp / 2.0)
    col = np.round((px - xoff) / sp)
    cx = col * sp + xoff
    d = np.hypot(px - cx, py - cy)
    on_ring = np.abs(d - R) < 0.55

    opaque = set(zip(ys.tolist(), xs.tolist()))
    ring_px = set()
    for yy, xx, s in zip(ys.tolist(), xs.tolist(), on_ring.tolist()):
        if s:
            ring_px.add((yy, xx))
            put(fr, yy, xx, seam)
    # under-ring relief: one pixel below each ring pixel, if opaque and not a ring
    for (yy, xx) in ring_px:
        nb = (yy + 1, xx)
        if nb in opaque and nb not in ring_px:
            put(fr, nb[0], nb[1], shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    seam, shadow = SEAM[cls]
    sp, R, largest = cfg['sp'], cfg['R'], cfg['largest']
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
        draw_chainmail(fr, comp, seam, shadow, sp, R)
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
