#!/usr/bin/env python3
"""THIRTY-FIRST net-new-geometry axis for ALL FOUR SLOTS — the OGEE / ONION / DAMASK family:
an all-over net of POINTED-OVAL (ogee) cells, the unmistakable damask / onion-dome / brocade
lattice. Parallel vertical ribs run down the whole body, but adjacent ribs undulate in OPPOSITE
phase so they alternately PINCH together (forming a cusp) and BULGE apart (forming the belly of
an oval); every pair of neighbouring ribs therefore encloses a vertical column of POINTED-OVAL
ogee cells that touch at their cusps, and a small bright BOSS/pip sits at each cell centre. The
repeated motif is the OGEE CELL — a closed cell whose boundary is a cyma / S-shaped double curve
meeting at top and bottom cusps; none of the thirty existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting) — ribs NEVER pinch, enclose nothing
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> straight-edged lozenge OUTLINE (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS -> imbricated scale field (open arcs, no closed cell)
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes -> herringbone / twill
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells -> ashlar brick-bond
  * 18th CHECKER of perpendicular SHORT-THREAD bundles -> basketweave
  * 19th tessellation of SIX-sided straight OUTLINE cells -> honeycomb
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells -> trellis
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE outlines -> chainmail rings
  * 22nd ONE CONTINUOUS UNDULATING SINE line -> watered-steel ripple (open, one ribbon)
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES -> meander key-fret
  * 24th CONTINUOUS CURVED COILS winding around a CENTRE point -> spiral / volute whorl
  * 25th FILLED ALTERNATE DIAGONAL DIAMONDS SOLID -> argyle / harlequin
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter OVERLAP NODE -> tartan / sett
  * 27th SHOOTS STRAIGHT RAYS OUTWARD from a shared CENTRE -> sunburst / compass
  * 28th STACKS NESTED CLOSED RINGS at growing radius around a CENTRE -> concentric target
  * 29th INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill -> houndstooth
  * 30th TWO INTERTWINING STRANDS braiding OVER-UNDER down a column -> cable / rope
  * 31st (this) COUNTER-PHASE RIBS PINCH-AND-BULGE to enclose POINTED-OVAL cells -> ogee / damask.

Critically distinct from the 11th fluting: fluting ribs are dead-straight parallels that never
touch and enclose no cell — ogee ribs undulate in OPPOSITE phase, pinching to cusps and enclosing
pointed-oval cells. Distinct from the 22nd wave: wave is ONE open undulating ribbon; ogee is a
field of CLOSED pointed-oval CELLS. Distinct from the 30th cable: cable's two strands cross
OVER-UNDER into a solid rope down a single column; ogee's ribs never cross — they only pinch and
bulge, leaving an OPEN pointed-oval cell between them. Distinct from every straight-edged /
circular / hexagonal cell net (14th lattice diamond, 19th honeycomb hex, 21st chainmail circle):
the ogee cell boundary is a CYMA (S-curve) meeting at CUSPS — a pointed oval, the signature
damask silhouette none of those produce. The counter-phase pinch-and-bulge rib pair enclosing a
cusped pointed oval is the defining, previously-unused geometry.

Per slot it lands as the 31st distinct axis:
  * CHEST  — ogee/damask cuirass: pointed-oval brocade net down the whole cuirass.
  * LEGS   — ogee/damask chausses: pointed-oval brocade net down the thighs.
  * BOOTS  — ogee/damask sabatons: pointed-oval brocade net over the boot.
  * HELMET — ogee/damask dome: pointed-oval brocade net over the whole crown.

Construction, per opaque body pixel in component-local coords (lx, ly) anchored at the component
bbox top-left. Vertical ribs sit at pitch PX. Rib index k has centreline
    xc_k(ly) = k*PX + AMP*sin(2*pi*ly/PY) * (-1)**k
so even and odd ribs swing in OPPOSITE directions; the gap between neighbours breathes between
PX-2*AMP (pinch/cusp) and PX+2*AMP (bulge/belly), enclosing a stacked column of pointed ovals.
The three ribs nearest the pixel are tested; the minimum signed distance d to a rib centreline
decides the tone:
    d <= RIB*CROWN        -> bright rib crest (RIB_HI)
    d <= RIB              -> rib flank        (RIB_MID)
    d <= RIB+GROOVE       -> recessed groove  (GROOVE)         (dark shadow hugging the rib)
    else                  -> body ground
A small bright BOSS (PIP) is stamped at each ogee cell centre, on a half-pitch-offset brick
lattice (xnode=(m+0.5)*PX, ynode=n*PY + PY/2 for odd m), so each pointed oval carries a
damask flower-pip.  Anchoring to the component bbox keeps the net stable frame-to-frame.

Authoring philosophy is identical to gen_cable_axis30.py / gen_houndstooth_axis29.py: every
pattern pixel is painted ONLY onto pixels that are ALREADY opaque body pixels. Because it never
adds a pixel outside the existing silhouette it CANNOT create isolated pixels, background bleed,
or accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60, lying
down) get a plain body recolor only — no net. Shading applied in this script via shade(); do NOT
run sprite_shade.py again.

To read as a clearly DIFFERENT set from the 30th cable (braided metal rope), 29th houndstooth
(flat two-tone cloth) and 28th concentric (engraved burnished metal) the ogee family is a rich
WOVEN DAMASK BROCADE — a deep saturated cloth ground with a bright metallic-thread ogee rib and a
pale boss, cloth-of-gold / cloth-of-silver. The brocade distinguishes class:
  * warrior — crimson-and-gold damask (garnet groove / bronze flank / bright-gold crest / pale pip)
  * mage    — royal-violet-and-silver damask (indigo groove / silver flank / moonsilver crest / pip)
  * ranger  — forest-and-antique-gold damask (bottle groove / antique-gold flank / gold crest / pip)

Run from repo root:
  python3 scripts/gen_ogee_axis31.py
Then QA (examples):
  python3 scripts/sprite_qa.py _ogee_legendary_preview/shirt_warrior_legendary31.png
  python3 scripts/sprite_qa.py _ogeedome_helmet_preview/helmet_mage_legendary31.png --y-min 2
  python3 scripts/sprite_qa.py _ogee_boots_preview/boots_warrior_legendary_ogee.png --y-max 63
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

# Ogee / onion / damask geometry constants. Tuned high-frequency so the pointed-oval net reads
# on a ~14px torso: narrow rib pitch (two cells across the torso), swing amplitude large enough
# that adjacent ribs nearly pinch shut to a cusp, thin ribs so the pointed oval stays open.
PX = 6            # horizontal rib pitch (px between rib columns)
PY = 8            # vertical ogee pitch (px per full pinch->bulge->pinch)
AMP = 1.6         # rib swing amplitude (gap breathes PX-2AMP .. PX+2AMP = 2.8 .. 9.2 px)
RIB = 0.9         # rib half-width (thin -> pointed-oval cell stays open)
CROWN = 0.5       # within this fraction of RIB -> bright rib crest
GROOVE = 0.75     # dark groove band width hugging the rib beyond RIB
PIP = 0.85        # boss radius at each cell centre

# Per-class ogee tone quad: (GROOVE dark recess, RIB_MID flank, RIB_HI crest, PIP boss).
OGEE = {
    'warrior': ((40, 8, 10), (150, 110, 40), (250, 214, 110), (255, 240, 180)),   # garnet / bronze / gold / pale-gold
    'mage':    ((26, 18, 44), (150, 150, 180), (244, 242, 255), (210, 220, 255)), # indigo / silver / moonsilver / pale
    'ranger':  ((14, 28, 18), (150, 120, 56), (236, 206, 120), (250, 232, 170)),  # bottle / antique-gold / gold / pale
}

# Per-class body (cloth ground) tones for the recolor: (deep shadow / base / highlight).
BODY = {
    'warrior': ((74, 20, 24), (120, 34, 38), (170, 60, 60)),     # crimson cloth
    'mage':    ((48, 36, 84), (86, 68, 138), (132, 112, 186)),   # royal violet cloth
    'ranger':  ((28, 50, 32), (52, 86, 54), (86, 124, 84)),      # deep forest cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_ogee_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary31', largest=True,
    ),
    'legs': dict(
        outdir='_ogee_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary31', largest=False,
    ),
    'boots': dict(
        outdir='_ogee_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_ogee', largest=False,
    ),
    'helmet': dict(
        outdir='_ogeedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary31', largest=True,
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


def draw_ogee(fr, comp, groove, rib_mid, rib_hi, pip):
    """Paint the ogee / onion / damask net onto one component. For each opaque body pixel, in
    component-local coords (lx, ly) anchored at the component bbox top-left, vertical ribs at
    pitch PX undulate in OPPOSITE phase for neighbouring ribs so adjacent ribs pinch to a cusp
    and bulge to a belly, enclosing a stacked column of pointed-oval cells. The pixel takes the
    rib crest / rib flank / groove / body tone by its distance to the nearest rib centreline, and
    a bright boss is stamped at each ogee cell centre. Only opaque body pixels are ever painted,
    so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        s = math.sin(2.0 * math.pi * ly / PY)
        # nearest three rib indices around this pixel
        k0 = int(round(lx / PX))
        dmin = 1e9
        for k in (k0 - 1, k0, k0 + 1):
            xc = k * PX + AMP * s * (1 if (k % 2 == 0) else -1)
            d = abs(lx - xc)
            if d < dmin:
                dmin = d
        # boss / pip at each ogee cell centre (half-pitch-offset brick lattice)
        m = int(round(lx / PX - 0.5))
        xnode = (m + 0.5) * PX
        ynode_off = (PY * 0.5) if (m % 2) else 0.0
        n = round((ly - ynode_off) / PY)
        ynode = n * PY + ynode_off
        dpip = math.hypot(lx - xnode, ly - ynode)
        if dpip <= PIP:
            put(fr, yy, xx, pip)
            continue
        if dmin <= RIB * CROWN:
            put(fr, yy, xx, rib_hi)
        elif dmin <= RIB:
            put(fr, yy, xx, rib_mid)
        elif dmin <= RIB + GROOVE:
            put(fr, yy, xx, groove)
        # else: leave the recolored body ground untouched


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    groove, rib_mid, rib_hi, pip = OGEE[cls]
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
        draw_ogee(fr, comp, groove, rib_mid, rib_hi, pip)
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
                print('wrote %-56s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
