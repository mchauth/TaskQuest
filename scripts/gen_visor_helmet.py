#!/usr/bin/env python3
"""Generate a FIFTH net-new-geometry HELMET silhouette per class — a closed
VISORED FACEPLATE: a solid metal face-guard that hangs DOWN from the helmet brow
and CLOSES OVER the face, leaving only a horizontal eye-slit with two glowing
eyes.

Why this is a NEW helmet treatment (distinct from ALL FOUR existing ones):
  * legendary1 (Wyrmhorn horns / Starweaver crown-fans / Plumed-Hood crest) spread
    UP-and-OUTWARD above the skull.
  * legendary2 (Crest circlets) rise straight UP from the crown as one tall fin.
  * legendary3 (Winged helms) fan WIDE and near-horizontal OUTWARD at skull height.
  * legendary4 (Aventail camail) hangs mail DOWN the SIDES, framing an OPEN face.
  * Every one of those either adds silhouette mass around the head OR leaves the
    face open. This one does the opposite: it fills the CENTRE columns below the
    brow with a solid plate that COVERS the face — the previously-unused
    forward/closing axis. Where the aventail is two side curtains with the face
    open, the visor is one centre plate with the face sealed: visually the exact
    inverse.

Authoring philosophy is identical to gen_aventail_helmet.py:
  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the faceplate. For the CENTRE columns of each helmet's bottom contour
    we hang a contiguous vertical plate starting one row BELOW that column's own
    lowest helmet pixel, so the top plate pixel is always 4-connected upward to
    the helm and the whole plate is one component fused to the body (QA-safe: no
    isolated pixels, no accent-caused multi-component frames). The plate is
    tallest at the centre and tapers at the outer face columns (CHIN) so the
    bottom rounds into a chin-guard. A dark SLIT band with two glowing eyes sits
    a few rows down; a bright central RIDGE runs the plate's midline (the nasal
    bar). Drawn ONLY in transparent space below the helm — never overpaints the
    helmet body, so the plate can only ever cover the face that the topmost helmet
    layer already sits in front of.

Connectivity is further guaranteed with the same per-frame guard as the aventail /
wing / cape: any plate pixel not 4-connected to the body mass is cleared, so
accent strays are 0 by construction. Because the plate is anchored RELATIVE to
each frame's own helmet-bottom contour, it tracks the animation bob exactly (no
absolute-Y drift). Sleep / empty frames have no helmet pixels, so they are
skipped.

Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (glow hue distinct so all read apart; the CLOSED face is the headline):
  * warrior "Ironclad Visor"  — dark-steel plate, silver ridge, cold silver eyes
  * mage    "Voidgaze Visor"  — cosmic-indigo plate, violet ridge, cyan eyes
  * ranger  "Wildmaw Visor"   — bronze/verdigris beast-helm, amber eyes

Run from repo root:
  python3 scripts/gen_visor_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _visor_helmet_preview/helmet_warrior_legendary5.png --y-min 2 --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Faceplate geometry. Centre columns of the helmet contour carry the plate.
#   mode 'hang'  (mage/ranger): the class helm is a hat/hood whose brim sits at
#     the brow, leaving the face OPEN below it. We hang a solid plate DOWN from
#     each centre column's lowest helm pixel — sealing the open face. Eye-slit
#     lands SLIT_J rows below the brow = the real eye row.
#   mode 'carve' (warrior): the class helm ALREADY seals the whole face. Hanging
#     below it would drop the slit onto the throat, so instead we REPAINT the
#     helm's own face region (top+BROW .. bottom) into a visored plate with the
#     eye-slit on the eye row. Repaints opaque helm px only -> stray/bleed/
#     multicomp impossible by construction (baldric-style).
FACEW = 4          # half-width: plate covers centre-FACEW .. centre+FACEW (9 cols)
DROP = 10          # 'hang': rows the centre column hangs (reaches the jaw)
CHIN = 2           # 'hang': plate rows lost per column stepping OUTWARD -> chin
SLIT_J = 3         # 'hang': rows below the brow where the eye-slit band sits
BROW = 4           # 'carve': rows below the helm top where the visor face begins
EYE_OFF = 2        # eye glow at +/- this column offset from centre

# ── Per-class palettes: body ramp (D/M/L) + plate ramp ──
# body : deep shadow / base / highlight
# plate: PLATE_D (shadow face) / PLATE_M (mid) / PLATE_L (lit face) /
#        RIDGE (bright central nasal bar) / SLIT (dark eye recess) / EYE (glow)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary5', mode='carve',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),                       # dark iron -> steel
        plate=dict(D=(58, 62, 74), M=(104, 110, 126), L=(168, 176, 196),
                   RIDGE=(206, 214, 230), SLIT=(20, 22, 30), EYE=(224, 236, 255)),  # steel, cold silver eyes
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary5', mode='hang',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                        # cosmic indigo -> violet
        plate=dict(D=(26, 22, 74), M=(58, 50, 140), L=(112, 100, 210),
                   RIDGE=(150, 130, 236), SLIT=(10, 8, 34), EYE=(120, 240, 255)),   # indigo plate, cyan eyes
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary5', mode='hang',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                          # forest green
        plate=dict(D=(58, 48, 26), M=(104, 86, 44), L=(158, 134, 74),
                   RIDGE=(196, 168, 96), SLIT=(20, 16, 8), EYE=(255, 188, 70)),     # bronze/verdigris, amber eyes
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    """Quantized 3-tone recolor of the legendary silhouette (per-frame)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def plate_tone(o, j, n, pal):
    """Pick a faceplate tone. o = column offset from centre (-FACEW..+FACEW);
    j = rows below the brow (1..n); n = this column's plate length.
    Central nasal ridge is bright; a dark slit band with two glowing eyes sits at
    SLIT_J; the bottom row of each column is the dark chin edge; faces shade
    L(right)/M/D(left) so the plate reads rounded even before shade()."""
    if j == n:
        return pal['D']                       # dark chin/edge row
    if j == SLIT_J:                            # eye-slit band
        if abs(o) == EYE_OFF:
            return pal['EYE']                  # glowing eye
        return pal['SLIT']                     # dark recess across the slit
    if o == 0:
        return pal['RIDGE']                    # bright central nasal bar
    return pal['L'] if o > 0 else pal['D'] if o < 0 else pal['M']


def draw_visor_hang(fr, a, pal):
    """mage/ranger: hang a solid faceplate DOWN the CENTRE columns from the helm
    bottom contour, sealing the open face. Only fills transparent space."""
    cols = np.where(a.any(axis=0))[0]
    if cols.size == 0:
        return
    centre = int(round(0.5 * (int(cols.min()) + int(cols.max()))))
    for o in range(-FACEW, FACEW + 1):
        x = centre + o
        if not (0 <= x < FW):
            continue
        col_ys = np.where(a[:, x])[0]
        if col_ys.size == 0:                   # no helm pixel here to anchor to
            continue
        y_col = int(col_ys.max())              # this column's own lowest helm pixel
        n = DROP - abs(o) * CHIN               # tallest at centre, rounds at chin
        if n < 1:
            continue
        for j in range(1, n + 1):
            y = y_col + j
            if y >= FH:
                break
            if a[y, x] or fr[y, x, 3] > 0:     # never overpaint helm/existing
                continue
            put(fr, y, x, plate_tone(o, j, n, pal))


def draw_visor_carve(fr, a, pal):
    """warrior: the helm already seals the face, so REPAINT its own face region
    (per centre column: top+BROW .. bottom) into a visored plate with the eye-slit
    on the eye row. Repaints opaque helm px only."""
    cols = np.where(a.any(axis=0))[0]
    if cols.size == 0:
        return
    centre = int(round(0.5 * (int(cols.min()) + int(cols.max()))))
    for o in range(-FACEW, FACEW + 1):
        x = centre + o
        if not (0 <= x < FW):
            continue
        col_ys = np.where(a[:, x])[0]
        if col_ys.size == 0:
            continue
        top, bot = int(col_ys.min()), int(col_ys.max())
        y0 = top + BROW                        # visor face begins below the brow
        bot -= abs(o)                          # round the outer chin corners
        if y0 > bot:
            continue
        n = bot - y0 + 1                        # plate length in this column
        for j in range(1, n + 1):
            y = y0 + j - 1
            if not a[y, x]:                    # only repaint solid helm pixels
                continue
            put(fr, y, x, plate_tone(o, j, n, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['plate']
    mode = cfg['mode']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():                        # empty (incl. sleep) frames skipped
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        (draw_visor_carve if mode == 'carve' else draw_visor_hang)(fr, a, pal)
        # Connectivity guard: drop any plate pixel not 4-connected to the body
        # mass (only touches stranded accent px, never body px).
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop_mask = da & ~keep
        for y, x in np.argwhere(drop_mask):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_visor_helmet_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-46s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
