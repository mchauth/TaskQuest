#!/usr/bin/env python3
"""TWENTY-SEVENTH net-new-geometry axis for ALL FOUR SLOTS — the SUNBURST / RADIANT / COMPASS
family: an all-over field of tiled RADIATING CENTRES, each emitting a set of STRAIGHT RAYS
that shoot OUTWARD from a shared origin point in every principal direction (a compass-rose /
solar-burst / asterisk star), with a brighter CORE dot at each centre. The repeated motif is
the RADIAL BURST: many straight lines sharing one origin and fanning out omnidirectionally,
bounded in length so discrete star-bursts read across the body. This radiating-from-a-point
geometry is occupied by none of the twenty-six existing legendary axes per slot:
  * 11th laid CONTINUOUS STRAIGHT VERTICAL parallel lines only (fluting)
  * 12th laid CONTINUOUS STRAIGHT HORIZONTAL parallel lines only (lamellar bands)
  * 13th laid a field of DISCRETE POINTS (rivet-stud grid)
  * 14th laid TWO crossing STRAIGHT DIAGONAL families -> lozenge OUTLINE / diamond MESH
  * 15th laid OVERLAPPING SHORT CURVED ARCS -> imbricated scale field
  * 16th laid SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone / twill
  * 17th laid a STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th laid a CHECKER of perpendicular SHORT-THREAD bundles alternating dir -> basketweave
  * 19th laid a tessellation of SIX-sided OUTLINE cells -> honeycomb
  * 20th laid THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st laid a staggered grid of closed CIRCLE OUTLINES -> chainmail rings
  * 22nd laid CONTINUOUS UNDULATING SINE lines -> watered-steel ripple
  * 23rd laid a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th laid CONTINUOUS CURVED COILS winding around centres -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th (this) SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE point -> sunburst / compass.
Critically distinct from the 11th fluting and 12th lamellar (single-direction parallel line
families that never share an origin) and from the 14th lattice / 20th trellis (2-3 fixed line
families that mesh into closed cells): sunburst rays all EMANATE FROM ONE POINT and fan out in
every principal direction, forming a discrete radiating star rather than a parallel field or a
cellular mesh. Distinct from the 24th spiral (one CONTINUOUS CURVED coil winding AROUND a
centre) — sunburst rays are STRAIGHT lines shooting straight OUT from the centre, no winding.
Distinct from the 3rd studwork (isolated POINTS, no rays) and the 8th aegis-roundel chest
(a single central emblem, not an all-over tiled burst field). The bright core dot is the
origin accent, not the motif; the motif is the radiating straight-ray burst.

Per slot it lands as the 27th distinct axis:
  * CHEST  — sunburst cuirass: radiant bursts over the whole cuirass.
  * LEGS   — sunburst chausses: radiant bursts over the thighs.
  * BOOTS  — radiant sabatons: radiant bursts over the boot.
  * HELMET — radiant dome: radiant bursts over the whole crown.

Authoring philosophy is identical to gen_tartan_axis26.py / gen_argyle_axis25.py: every ray
pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60, lying
down) get the recolor only — no rays. Shading applied in this script via shade(); do NOT run
sprite_shade.py again.

To read as a clearly DIFFERENT set from the 26th (tartan, woven highland clan-cloth) and the
25th (argyle, regal jewel body + gold diamond) the sunburst family is a RADIANT / SOLAR /
ASTRAL look: a deep near-void body with BRIGHT RADIATING RAYS and a white-hot core — light
bursting out of darkness, celestial not woven. The body tint distinguishes class:
  * warrior — obsidian-black body + molten-gold rays + white-hot core (solar aegis)
  * mage    — deep-void indigo body + astral-cyan rays + white star core (astral burst)
  * ranger  — dark bottle-green body + amber-dawn rays + pale-gold core (dawn burst)

Run from repo root:
  python3 scripts/gen_sunburst_axis27.py
Then QA (examples):
  python3 scripts/sprite_qa.py _sunburst_legendary_preview/shirt_warrior_legendary27.png
  python3 scripts/sprite_qa.py _sunburstdome_helmet_preview/helmet_mage_legendary27.png --y-min 2
  python3 scripts/sprite_qa.py _sunburst_boots_preview/boots_warrior_legendary_sunburst.png --y-max 63
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

# Sunburst geometry. Work in component-local coords relative to the component bbox top-left so
# the burst grid is stable frame-to-frame. Tile the plane at PITCH; a radiating CENTRE sits at
# every grid node. For each opaque pixel, take its offset (rx, ry) to the NEAREST centre. A
# pixel is on a RAY if it lies on one of the eight principal directions from that centre —
# horizontal (ry==0), vertical (rx==0), or the two diagonals (|rx|==|ry|) — AND within reach R
# of the centre (so the bursts stay discrete, separated by body ground). The centre dot and its
# immediate neighbours (|rx|<=CORE and |ry|<=CORE) are the brighter CORE. Priority per pixel:
#   core  >  ray  >  recolored body.
PITCH = 10              # burst spacing (px) — centre-to-centre
R = 4                   # ray reach from centre (px); < PITCH/2 keeps bursts discrete
CORE = 1                # core radius (px) around each centre


# Per-class accent palettes: (RAY tone, CORE tone).
SEAM = {
    'warrior': ((214, 150, 44), (255, 244, 214)),   # molten-gold rays, white-hot core
    'mage':    ((92, 190, 220), (232, 240, 255)),    # astral-cyan rays, white star core
    'ranger':  ((210, 168, 70), (244, 232, 190)),    # amber-dawn rays, pale-gold core
}

# Per-class body tones: deep shadow / base / highlight. NEAR-VOID variants so the set reads
# apart from tartan's muted highland ground and argyle's jewel body: here the body is a deep
# celestial dark out of which the rays burst.
BODY = {
    'warrior': ((10, 10, 14), (26, 26, 34), (48, 48, 60)),     # obsidian-black
    'mage':    ((10, 12, 40), (24, 28, 72), (46, 52, 112)),    # deep-void indigo
    'ranger':  ((8, 26, 18), (20, 52, 34), (40, 82, 56)),      # dark bottle-green
}

# One config block per slot. `largest` restricts the burst field to the biggest connected
# component (torso / dome) so raised arms are not covered; boots/legs field all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_sunburst_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary27', largest=True,
    ),
    'legs': dict(
        outdir='_sunburst_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary27', largest=False,
    ),
    'boots': dict(
        outdir='_sunburst_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_sunburst', largest=False,
    ),
    'helmet': dict(
        outdir='_sunburstdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary27', largest=True,
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


def draw_sunburst(fr, comp, ray, core):
    """Paint a field of radiating star-bursts onto one component. For each opaque pixel take
    its offset (rx, ry) to the NEAREST centre on a PITCH grid anchored at the component bbox
    top-left. The centre dot + immediate neighbours are CORE; the eight principal directions
    (horizontal, vertical, both diagonals) within reach R are RAY; everything else keeps the
    recolored body. Only opaque body pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    half = PITCH // 2

    for yy, xx in zip(ys.tolist(), xs.tolist()):
        dx = xx - x0
        dy = yy - y0
        # offset to nearest centre, in range [-half, half)
        rx = ((dx + half) % PITCH) - half
        ry = ((dy + half) % PITCH) - half
        if abs(rx) <= CORE and abs(ry) <= CORE:
            put(fr, yy, xx, core)
        elif max(abs(rx), abs(ry)) <= R and (rx == 0 or ry == 0 or abs(rx) == abs(ry)):
            put(fr, yy, xx, ray)
        # else: leave the recolored body tone


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ray, core = SEAM[cls]
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
        draw_sunburst(fr, comp, ray, core)
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
