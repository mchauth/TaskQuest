#!/usr/bin/env python3
"""Generate a NINTH net-new-geometry HELMET showcase per class — paired lateral
CHEEK-PLATES: two vertical guard panels repainted down the OUTER edges of the lower
face zone, framing the face on both sides. This brings the helmet slot to NINE
distinct axes, at parity with the chest slot, and is the paired-lateral-vertical
axis that none of the eight existing legendary helmets occupy:

  * legendary1 (horns / crown-fans / crest) sweep UP-and-OUT above the skull.
  * legendary2 (crest)                       rises straight UP as one tall fin.
  * legendary3 (winged helm)                 fans WIDE and near-horizontal OUT.
  * legendary4 (aventail)                    hangs mail DOWN the sides (full drape).
  * legendary5 (visor)                       fills the CENTRE forward columns.
  * legendary6 (antler)                      BRANCHES into a multi-pronged rack.
  * legendary7 (diadem)                      a HORIZONTAL jewelled brow BAND.
  * legendary8 (comb)                        a single VERTICAL median ridge, centre.
  * these CHEEK-PLATES add NO silhouette pixels — two short PAIRED vertical panels
    repainted at the outer edges of the LOWER FACE only (not the full-height side
    drape of the aventail). comb (single centre vertical) vs cheek-plates (paired
    outer verticals) is the same central-vs-lateral contrast the legs slot draws
    between the loin-guard and the side-stripes.

Authoring philosophy is identical to gen_comb_helmet.py (its direct model),
including the key robustness win: the plates are painted ONLY onto pixels that are
ALREADY opaque helmet pixels (`a`). Because they never add a pixel outside the
existing silhouette, they CANNOT create isolated pixels, background bleed, or
accent-caused multi-component frames — QA-safe purely by construction. They read as
distinct guards because the metal tones contrast with the recolored helm and they
hug the two outer edges of the face zone in every pose.

  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp (0 px dropped by construction).
  * Accent = paired cheek plates. Per frame we take the helmet mass, restrict to the
    LOWER FACE_FRAC of its height (the cheek/jaw zone), and for each row there
    repaint the outer PLATE_W columns on each side: lit crown at the outer rim, dark
    selvage at the inner rim, plus periodic bright RIVETS marching down each plate.
    Everything is clamped to `a`, so the plates track the head through every pose.

Helmet sheets are empty on the sleep frames, so those are skipped. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class (plate hue distinct so the ninth reads apart from the eight):
  * warrior "Sovereign's Cheek-Guard" — dark-iron helm + GOLD plates, ruby rivets
  * mage    "Astral Face-Wards"        — cosmic-indigo helm + SILVER plates, sapphire rivets
  * ranger  "Warden's Jaw-Guards"      — forest helm + BRONZE plates, emerald rivets

Run from repo root:
  python3 scripts/gen_cheek_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _cheek_helmet_preview/helmet_warrior_legendary9.png --y-min 2
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

# Cheek-plate geometry. FACE_FRAC = bottom fraction of the helm mass height that
# counts as the face/cheek zone (the plates live only here, not on the dome).
# PLATE_W = width in px of each outer plate. RIVET_STEP = a bright rivet every N
# rows down each plate. GAP_MIN = a row must be at least this wide to carry two
# separate plates (narrow rows get a single outer hint per side instead of overlap).
FACE_FRAC = 0.5
PLATE_W = 2
RIVET_STEP = 3
GAP_MIN = 6

# -- Per-class palettes: body ramp (D/M/L) + plate ramp (EDGE, CROWN, RIVET) ------
# body  : deep shadow / base / highlight
# plate : EDGE (dark selvage at inner rim) / CROWN (lit plate body at outer rim) /
#         RIVET (bright rivets down each plate)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary9',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),                   # dark iron -> steel
        plate=((70, 48, 8), (214, 168, 52), (232, 40, 52)),                    # gold plates, ruby rivets
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary9',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                    # cosmic indigo -> violet
        plate=((70, 76, 92), (212, 220, 236), (56, 120, 240)),                 # silver plates, sapphire rivets
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary9',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                      # forest green
        plate=((52, 34, 12), (166, 116, 48), (46, 200, 108)),                  # bronze plates, emerald rivets
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    """Quantized 3-tone recolor of the helmet silhouette (per-frame)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_cheeks(fr, a, pal):
    """Repaint paired cheek plates down the outer edges of the lower face zone. Only
    helm pixels are touched, so the plates add zero new silhouette pixels (QA-safe)."""
    EDGE, CROWN, RIVET = pal
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    h = max(y1 - y0, 1)
    face_top = y0 + (1.0 - FACE_FRAC) * h        # only rows below this are the face
    for y in range(int(round(face_top)), y1 + 1):
        row_x = np.where(a[y])[0]
        if row_x.size == 0:
            continue
        xl, xr = int(row_x.min()), int(row_x.max())
        span = xr - xl
        rivet = ((y - int(round(face_top))) % RIVET_STEP == 0)
        if span >= GAP_MIN:
            for k in range(PLATE_W):
                lx, rx = xl + k, xr - k
                # inner rim (k == PLATE_W-1) is the dark selvage, outer is lit crown
                tone = EDGE if k == PLATE_W - 1 else CROWN
                if a[y, lx]:
                    put(fr, y, lx, RIVET if (rivet and k == 0) else tone)
                if a[y, rx]:
                    put(fr, y, rx, RIVET if (rivet and k == 0) else tone)
        else:
            # narrow row (jaw/overlap): a single lit hint at each outer px
            if a[y, xl]:
                put(fr, y, xl, RIVET if rivet else CROWN)
            if a[y, xr]:
                put(fr, y, xr, RIVET if rivet else CROWN)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['plate']
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
        draw_cheeks(fr, a, pal)
        # Connectivity guard (belt-and-suspenders): the plates only repaint helm
        # pixels so no stray is possible; the guard is a no-op here by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        strays = da & ~keep
        for y, x in np.argwhere(strays):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_cheek_helmet_preview'
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
