#!/usr/bin/env python3
"""THIRTY-FOURTH net-new-geometry axis for ALL FOUR SLOTS — the SEIGAIHA / OCEANIC
WAVE-SCALE family: an all-over field of overlapping FANS, where each fan is a set of
NESTED CONCENTRIC ARCS (multiple arcs per scale) bulging upward, laid on a HALF-DROP
lattice so the fans interlock into continuous concentric-wave rows — the classic
blue-ocean-wave / fish-scale pattern (青海波). A bright CORE dot sits at each fan apex.
The repeated motif is the MULTI-ARC NESTED FAN; none of the thirty-three existing
legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> straight-edged lozenge OUTLINE (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS, ONE arc per scale, all facing ONE way -> imbricated scale field
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone / twill
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th tessellation of SIX-sided straight OUTLINE cells -> honeycomb
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE outlines, ONE ring per centre -> chainmail
  * 22nd ONE CONTINUOUS UNDULATING SINE line -> watered-steel ripple
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th CONTINUOUS CURVED COILS winding around a CENTRE point -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE -> sunburst / compass
  * 28th STACKS NESTED CLOSED RINGS at growing radius around ONE CENTRE -> concentric target
  * 29th INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill -> houndstooth
  * 30th TWO INTERTWINING STRANDS braiding OVER-UNDER down a column -> cable / rope
  * 31st COUNTER-PHASE RIBS PINCH-AND-BULGE to enclose POINTED-OVAL cells -> ogee / damask
  * 32nd FOUR CIRCULAR LOBES around each node meeting at four cusps -> quatrefoil / tracery
  * 33rd axis-square + 45deg-square overlaid into an EIGHT-POINTED STAR OUTLINE -> octagram / girih
  * 34th (this) OVERLAPPING FANS of NESTED CONCENTRIC ARCS on a HALF-DROP lattice -> seigaiha wave-scale.

Critically distinct from the 15th scale: the scale field draws ONE convex arc per scale
(the leading tile edge); the seigaiha fan is a stack of THREE nested concentric arcs per
scale, and the fans overlap in a half-drop so the arcs interlock into continuous wave rows.
Distinct from the 28th concentric: concentric stacks CLOSED rings (full 360deg) around ONE
tiled centre; the seigaiha draws only the LOWER-fan arcs (scallops opening downward) on a
dense overlapping lattice, so the repeat is an interlocking half-circle wave, not a bullseye.
Distinct from the 21st chainmail (single non-overlapping ring per centre) and the 24th spiral
(one continuous coil of GROWING radius). The overlapping nested-arc wave-scale fan is the
defining, previously-unused geometry.

Per slot it lands as the 34th distinct axis:
  * CHEST  — wave cuirass: seigaiha fan net down the whole cuirass.
  * LEGS   — wave chausses: seigaiha fan net down the thighs.
  * BOOTS  — wave sabatons: seigaiha fan net over the boot.
  * HELMET — wave dome: seigaiha fan net over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the
component bbox top-left. Fan apex centres sit on a HALF-DROP lattice: pitch PX across, PY
down, odd rows shifted PX/2. Each pixel is assigned to the NEAREST apex that is at-or-above
it (cy <= ly) so every fan opens DOWNWARD (a scallop). Let d be the distance to that apex.
The nested arcs are the level sets d = k*RINGSTEP (k=1..3, outermost at R = 3*RINGSTEP = the
scallop rim); the distance to the nearest arc line dl = |d mod RINGSTEP centred| decides tone:
    dl <= RIB*CROWN     -> bright wave crest (RIB_HI)
    dl <= RIB           -> wave flank        (RIB_MID)
    dl <= RIB+GROOVE    -> recessed trough   (GROOVE)   (dark shadow hugging the arc)
    else                -> body ground   (the smooth scale face reads here)
A bright CORE (PIP) is stamped within PIP px of each apex. PX/PY/R tuned so ~2-3 fans span a
~14px torso and the rows overlap to interlock. Anchoring to the bbox keeps the net stable
frame-to-frame.

Authoring philosophy identical to gen_octagram_axis33.py / gen_quatrefoil_axis32.py: every
pattern pixel is painted ONLY onto pixels ALREADY opaque body pixels. Because it never adds a
pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run
sprite_shade.py again.

To read as a clearly DIFFERENT set the seigaiha family is DAMASCENED WAVE-INLAY on polished
plate — a mid-tone burnished metal ground with a bright inlaid metal arc and a jewelled apex
core, like a tidal wave-scale damascene. The inlay distinguishes class:
  * warrior — gilt wave on gunmetal plate (dark-steel trough / brass flank / bright-gold crest / pale-gold pip)
  * mage    — silver wave on violet-steel plate (indigo trough / steel-blue flank / white-silver crest / pale pip)
  * ranger  — copper wave on bronzed-forest plate (bottle trough / bronze flank / bright-copper crest / pale pip)

Run from repo root:
  python3 scripts/gen_seigaiha_axis34.py
Then QA (examples):
  python3 scripts/sprite_qa.py _seigaiha_legendary_preview/shirt_warrior_legendary34.png
  python3 scripts/sprite_qa.py _seidome_helmet_preview/helmet_mage_legendary34.png --y-min 2
  python3 scripts/sprite_qa.py _seigaiha_boots_preview/boots_warrior_legendary_seigaiha.png --y-max 63
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Seigaiha wave-scale geometry. Tuned so the fan reads on a ~14px torso: apex pitch gives
# ~two fans across, three nested arcs per fan, rows overlap (PY < R) so the fans interlock.
PX = 6.0         # horizontal pitch between fan apex centres
PY = 3.0         # vertical pitch between fan rows (< R so rows overlap and interlock)
RINGSTEP = 2.0   # spacing between the nested concentric arcs of one fan
R = 6.0          # fan (scallop) radius = 3 * RINGSTEP -> three arcs at 2,4,6
RIB = 0.62       # arc-line half-width
CROWN = 0.42     # within this fraction of RIB -> bright arc crest
GROOVE = 0.5     # dark trough band width hugging the arc beyond RIB
PIP = 0.9        # jewelled core radius at each fan apex

# Per-class inlay tone quad: (GROOVE dark trough, RIB_MID flank, RIB_HI crest, PIP core).
SEA = {
    'warrior': ((26, 22, 12), (150, 116, 44), (252, 216, 112), (255, 242, 186)),  # dark-steel / brass / gold / pale
    'mage':    ((20, 22, 46), (132, 148, 178), (240, 244, 255), (208, 222, 255)), # indigo / steel-blue / silver / pale
    'ranger':  ((16, 26, 18), (156, 104, 58), (248, 178, 108), (252, 224, 176)),  # bottle / bronze / copper / pale
}

# Per-class body (ground) tones for the recolor: (deep shadow / base / highlight).
BODY = {
    'warrior': ((40, 46, 56), (68, 78, 94), (104, 118, 138)),   # deep-sea gunmetal plate
    'mage':    ((32, 32, 64), (54, 56, 104), (90, 92, 156)),    # abyssal violet-steel plate
    'ranger':  ((26, 44, 36), (46, 76, 60), (80, 116, 92)),     # bronzed-forest tidal plate
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_seigaiha_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary34', largest=True,
    ),
    'legs': dict(
        outdir='_seigaiha_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary34', largest=False,
    ),
    'boots': dict(
        outdir='_seigaiha_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_seigaiha', largest=False,
    ),
    'helmet': dict(
        outdir='_seidome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary34', largest=True,
    ),
}


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free).
    Returns (labels int32 array, n). Background (False) is label 0. Matches
    scipy.ndimage.label's default cross structuring element on these small 80x64 masks."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    n = 0
    stack = []
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and labels[sy, sx] == 0:
                n += 1
                labels[sy, sx] = n
                stack.append((sy, sx))
                while stack:
                    y, x = stack.pop()
                    if y > 0 and mask[y - 1, x] and labels[y - 1, x] == 0:
                        labels[y - 1, x] = n
                        stack.append((y - 1, x))
                    if y < h - 1 and mask[y + 1, x] and labels[y + 1, x] == 0:
                        labels[y + 1, x] = n
                        stack.append((y + 1, x))
                    if x > 0 and mask[y, x - 1] and labels[y, x - 1] == 0:
                        labels[y, x - 1] = n
                        stack.append((y, x - 1))
                    if x < w - 1 and mask[y, x + 1] and labels[y, x + 1] == 0:
                        labels[y, x + 1] = n
                        stack.append((y, x + 1))
    return labels, n


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


def draw_seigaiha(fr, comp, trough, rib_mid, rib_hi, pip):
    """Paint the seigaiha wave-scale fan net onto one component. For each opaque body pixel,
    in component-local coords (lx, ly) anchored at the component bbox top-left, fan apex
    centres sit on a half-drop lattice (pitch PX across, PY down, odd rows shifted PX/2). The
    pixel is assigned to the nearest apex at-or-above it (fan opens downward); its distance d
    to that apex, folded into the nested-arc period RINGSTEP, gives crest / flank / trough /
    body tone, with a bright core stamped at each apex. Only opaque body pixels are ever
    painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        j0 = int(round(ly / PY))
        best_d = 1e9
        dcore = 1e9
        for j in (j0 - 2, j0 - 1, j0, j0 + 1):
            cy = j * PY
            if cy > ly + 0.5:          # apex must be at or above the pixel (fan opens down)
                continue
            xoff = (PX / 2.0) if (j & 1) else 0.0
            i0 = int(round((lx - xoff) / PX))
            for i in (i0 - 1, i0, i0 + 1):
                cx = i * PX + xoff
                dx = lx - cx
                dy = ly - cy
                d = math.hypot(dx, dy)
                if d < dcore:
                    dcore = d
                if d <= R + GROOVE and d < best_d:
                    best_d = d
        if dcore <= PIP:
            put(fr, yy, xx, pip)
            continue
        if best_d > 1e8:
            continue                    # above every apex: leave recolored body ground
        phase = best_d - RINGSTEP * math.floor(best_d / RINGSTEP)  # 0..RINGSTEP
        # arc lines sit at integer multiples of RINGSTEP, i.e. where phase ~ 0 (== RINGSTEP):
        dline = min(phase, RINGSTEP - phase)
        if dline <= RIB * CROWN:
            put(fr, yy, xx, rib_hi)
        elif dline <= RIB:
            put(fr, yy, xx, rib_mid)
        elif dline <= RIB + GROOVE:
            put(fr, yy, xx, trough)
        # else: leave the recolored body ground untouched (smooth scale face)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    trough, rib_mid, rib_hi, pip = SEA[cls]
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
            lbl, n = label4(a)
            if n >= 1:
                counts = np.bincount(lbl.ravel())
                counts[0] = 0
                comp = (lbl == int(counts.argmax()))
            else:
                comp = a
        else:
            comp = a
        draw_seigaiha(fr, comp, trough, rib_mid, rib_hi, pip)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
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
                print('wrote %-58s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
