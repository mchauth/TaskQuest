#!/usr/bin/env python3
"""THIRTY-NINTH net-new-geometry axis for ALL FOUR SLOTS — the GUILLOCHE / INTERLACED-RIBBON
family: an all-over field of horizontal bands, each band woven from TWO counter-phase SINE
RIBBONS that braid OVER-UNDER as they run and, between every pair of crossings, bulge apart to
enclose a near-CIRCULAR EYE holding a bezel-set central BOSS/pip — the classical running
guilloche (Tuscan border / banded interlace) carved on cornices, coins and column bases. Two
ribbon centre-lines share a period PX along a band centred at yb (band pitch PY down):
    s   = sin(2*pi*lx/PX)
    r1  = yb + AMP*s        (ribbon A)
    r2  = yb - AMP*s        (ribbon B, the mirror / counter-phase strand)
The ribbons CROSS wherever s=0 (every half period) and pull farthest apart where |s|=1, so a
row of round EYES sits on the band centre-line, one per half period. At each crossing ONE ribbon
passes OVER the other, the over-strand alternating crossing-to-crossing to weave a true
interlace. Each ribbon is shaded as a rounded metal TUBE (upper edge HILIT under an upper-left
light, lower edge SHADOW, crown MID) with a bright RIM at the extreme edge; inside every enclosed
eye a recessed GROUND floor carries a RIM boss catch-light at its centre. The repeated motif is
the pair of BRAIDED COUNTER-PHASE RIBBONS ENCLOSING A CHAIN OF EYES; none of the thirty-eight
existing legendary axes per slot occupy it:
  * 11th CONTINUOUS STRAIGHT VERTICAL parallel lines (fluting)
  * 12th CONTINUOUS STRAIGHT HORIZONTAL parallel lines (lamellar bands)
  * 13th a field of DISCRETE RAISED ROUND POINTS (rivet-stud grid)
  * 14th TWO crossing STRAIGHT DIAGONAL families -> straight-edged lozenge OUTLINE (lattice)
  * 15th OVERLAPPING SHORT CURVED ARCS, one arc per scale (imbricated scale field)
  * 16th SHORT alternating-slope STRAIGHT DIAGONAL dashes (herringbone / twill)
  * 17th STAGGERED grid of closed RECTANGULAR OUTLINE cells (ashlar brick-bond)
  * 18th CHECKER of perpendicular SHORT-THREAD bundles (basketweave)
  * 19th tessellation of SIX-sided straight OUTLINE cells (honeycomb)
  * 20th THREE STRAIGHT line families -> THREE-sided OUTLINE cells (trellis)
  * 21st STAGGERED grid of closed SINGLE-RADIUS CIRCLE outlines (chainmail)
  * 22nd ONE CONTINUOUS UNDULATING SINE line (watered-steel ripple)
  * 23rd a CONTINUOUS line turning only at RIGHT ANGLES (meander key-fret)
  * 24th CONTINUOUS CURVED COILS winding around a CENTRE point (spiral / volute)
  * 25th FLAT SOLID ALTERNATE DIAGONAL DIAMONDS (argyle / harlequin)
  * 26th CROSSED BOLD ORTHOGONAL BANDS with a brighter overlap node (tartan / sett)
  * 27th STRAIGHT RAYS radiating OUTWARD from a shared centre (sunburst / compass)
  * 28th NESTED CLOSED RINGS at growing radius around one centre (concentric target)
  * 29th INTERLOCKING JAGGED BROKEN-CHECK from a color-and-weave twill (houndstooth)
  * 30th TWO INTERTWINING STRANDS braiding OVER-UNDER down a COLUMN (cable / rope)
  * 31st COUNTER-PHASE RIBS PINCH-AND-BULGE enclosing POINTED-OVAL cells (ogee / damask)
  * 32nd FOUR CIRCULAR LOBES around each node meeting at four cusps (quatrefoil / tracery)
  * 33rd axis-square + 45deg-square overlaid into an EIGHT-POINTED STAR OUTLINE (octagram)
  * 34th OVERLAPPING FANS of NESTED CONCENTRIC ARCS on a half-drop lattice (seigaiha wave)
  * 35th a TESSELLATION OF RAISED FOUR-FACET PYRAMIDS with directional facet shading (facet)
  * 36th a field of CONVEX ROUNDED DIAMOND CUSHIONS pinned by sunken button tufts (quilt)
  * 37th a field of SUNKEN RECTANGULAR PANELS with a REVERSED bevel and a proud grid (coffer)
  * 38th an ALTERNATING BAND of RAISED CONVEX OVOIDS + POINTED DARTS (egg-and-dart / ovolo)
  * 39th (this) TWO BRAIDED COUNTER-PHASE SINE RIBBONS enclosing a CHAIN OF EYES -> guilloche.

Critically distinct from every prior axis. Most important separations:
  - NOT the 30th cable (torsade): the cable is two strands twisting OVER-UNDER down a single
    VERTICAL COLUMN and encloses NO shapes — the guilloche is two ribbons running HORIZONTALLY
    that braid AND bulge apart to enclose a chain of round EYES each holding a boss.
  - NOT the 22nd wave: the wave is ONE continuous sine ribbon — the guilloche is TWO
    counter-phase ribbons that interlace and enclose eyes.
  - NOT the 31st ogee: ogee cells are POINTED OVALS woven from a continuous rib NET with cusps —
    the guilloche eyes are ROUND, formed by two braided ribbons that pass OVER-UNDER at crossings.
  - NOT the 21st chainmail / 28th concentric / 32nd quatrefoil: those are static rings or lobes;
    the guilloche's defining feature is the OVER-UNDER BRAID of the two ribbons BETWEEN the eyes.
The braided counter-phase ribbon pair enclosing a chain of eyes is the defining, previously-unused
geometry.

Per slot it lands as the 39th distinct axis:
  * CHEST  — guilloche cuirass: braided eye-chain banded down the whole breastplate.
  * LEGS   — guilloche chausses: braided eye-chain banded down the thighs.
  * BOOTS  — guilloche sabatons: braided eye-chain over the boot.
  * HELMET — guilloche dome: braided eye-chain over the whole crown.

Authoring philosophy identical to gen_eggdart_axis38.py / gen_coffer_axis37.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel
outside the existing silhouette it CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe by construction. Sleep frames (fi>=60) get a
plain body recolor only — no net. Shading applied here via shade(); do NOT run sprite_shade.py
again.

To read as a clearly DIFFERENT set the guilloche family is DAMASCENED METAL INTERLACE — a plate
chased with the classical braided-ribbon guilloche, a white catch-light on each ribbon crown and
eye boss. Class differs by metal/gem (same metals as the cast-bronze family):
  * warrior — gilt-bronze guilloche (dark-bronze ground / bronze shadow / brass mid / bright-gold hilit / white-gold rim)
  * mage    — silvered violet guilloche (midnight ground / indigo shadow / steel-violet mid / bright-silver hilit / pale-white rim)
  * ranger  — bronzed forest guilloche (deep-forest ground / bottle shadow / bronze-green mid / bright-emerald hilit / pale-green rim)

Run from repo root:
  python3 scripts/gen_guilloche_axis39.py
Then QA (examples):
  python3 scripts/sprite_qa.py _guilloche_legendary_preview/shirt_warrior_legendary39.png
  python3 scripts/sprite_qa.py _guillochedome_helmet_preview/helmet_mage_legendary39.png --y-min 2
  python3 scripts/sprite_qa.py _guilloche_boots_preview/boots_warrior_legendary_guilloche.png --y-max 63
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

# Guilloche geometry. Tuned so the braided eye-chain reads on a ~14px torso: a horizontal band
# pitch PY, two counter-phase sine ribbons of period PX and amplitude AMP that braid over-under
# and enclose a chain of round eyes (one per half period) each holding a bezel boss.
PX = 8.0         # ribbon period across (local px) -> eye spacing = PX/2
PY = 7.0         # band pitch down (local px)
AMP = 2.0        # ribbon sine amplitude (eye half-height ~ AMP)
HW = 1.25        # ribbon half-width (tube radius)
EDGE = 0.45      # tube-edge fraction for hilit/shadow split (of HW)
PIP = 1.05       # eye-boss catch-light radius (local px)


# Per-class guilloche tone quintet: (GROUND recessed eye floor / band channel, SHADOW ribbon
# lower edge, MID ribbon crown, HILIT ribbon lit upper edge + boss body, RIM ribbon extreme edge
# + eye-boss catch-light). Light comes from the upper-left.
GUILLOCHE = {
    'warrior': ((40, 26, 10), (96, 64, 24), (168, 126, 52), (236, 190, 86), (255, 238, 168)),  # gilt-bronze
    'mage':    ((18, 16, 46), (66, 54, 114), (116, 100, 182), (176, 158, 240), (236, 228, 255)),  # silvered violet
    'ranger':  ((12, 30, 18), (38, 78, 48), (72, 132, 84), (124, 200, 128), (216, 248, 206)),  # bronzed forest
}

# Per-class body (ground) tones for the recolor (visible on sleep frames only, since the
# guilloche field otherwise tiles every opaque pixel): (deep shadow / base / highlight).
BODY = {
    'warrior': ((44, 30, 14), (82, 58, 26), (128, 96, 46)),   # dark bronze cloth
    'mage':    ((26, 24, 58), (52, 48, 104), (92, 86, 166)),   # dark violet cloth
    'ranger':  ((16, 40, 24), (38, 76, 50), (70, 122, 82)),    # dark forest cloth
}

# One config block per slot. `largest` restricts the net to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_guilloche_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary39', largest=True,
    ),
    'legs': dict(
        outdir='_guilloche_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary39', largest=False,
    ),
    'boots': dict(
        outdir='_guilloche_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_guilloche', largest=False,
    ),
    'helmet': dict(
        outdir='_guillochedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary39', largest=True,
    ),
}


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free).
    Returns (labels int32 array, n). Background (False) is label 0."""
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


def draw_guilloche(fr, comp, ground, shadow, mid, hilit, rim):
    """Paint the guilloche braided-ribbon eye-chain onto one component. For each opaque body
    pixel, in component-local coords (lx, ly) anchored at the component bbox top-left, a
    horizontal band pitch PY places two counter-phase sine ribbons (period PX, amplitude AMP)
    that braid over-under and bulge apart to enclose a chain of round eyes. A pixel is a RIBBON
    pixel when it lies within HW of either ribbon centre-line (at crossings the over-strand,
    chosen by crossing parity, wins); it is shaded as a rounded tube (upper edge hilit / lower
    edge shadow / crown mid / extreme edge rim). Otherwise it is inside an eye / channel: a
    recessed GROUND floor with a bright RIM boss catch-light at the eye centre. Only opaque body
    pixels are ever painted, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    two_pi = 2.0 * math.pi
    half = PX * 0.5
    for yy, xx in zip(ys.tolist(), xs.tolist()):
        lx = xx - x0
        ly = yy - y0
        # nearest band centre-line
        jb = round(ly / PY)
        yb = jb * PY
        s = math.sin(two_pi * lx / PX)
        r1 = yb + AMP * s
        r2 = yb - AMP * s
        o1 = ly - r1
        o2 = ly - r2
        d1 = abs(o1)
        d2 = abs(o2)
        on1 = d1 <= HW
        on2 = d2 <= HW
        if on1 or on2:
            if on1 and on2:
                # overlap near a crossing: the over-strand (alternating per crossing) wins
                k = int(math.floor(lx / half))
                chosen1 = (k % 2 == 0)
            elif on1:
                chosen1 = True
            else:
                chosen1 = False
            off = o1 if chosen1 else o2
            if abs(off) >= HW * (1.0 - 0.35):
                put(fr, yy, xx, rim)                 # bright extreme edge of the tube
            elif off < -HW * EDGE:
                put(fr, yy, xx, hilit)               # lit upper edge
            elif off > HW * EDGE:
                put(fr, yy, xx, shadow)              # lower edge in shadow
            else:
                put(fr, yy, xx, mid)                 # tube crown
            continue
        # not on a ribbon -> eye interior or band channel. Eye centres sit on the band
        # centre-line at the |s|=1 quarter phases (lx = PX/4 + m*PX/2).
        ecx = (math.floor(lx / half) + 0.5) * half
        de = math.hypot(lx - ecx, ly - yb)
        if de <= PIP:
            put(fr, yy, xx, rim)                     # eye-boss catch-light
        elif de <= PIP + 1.0:
            put(fr, yy, xx, hilit)                   # boss body
        else:
            put(fr, yy, xx, ground)                  # recessed eye floor / channel


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    ground, shadow, mid, hilit, rim = GUILLOCHE[cls]
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
        draw_guilloche(fr, comp, ground, shadow, mid, hilit, rim)
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
