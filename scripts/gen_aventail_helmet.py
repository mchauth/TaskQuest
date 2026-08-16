#!/usr/bin/env python3
"""Generate a FOURTH net-new-geometry HELMET silhouette per class — an AVENTAIL
(camail): a mail/scale drape that hangs DOWNWARD from the helmet rim along both
sides of the face to the shoulders.

Why this is a NEW helmet silhouette (distinct from ALL three existing ones):
  * Legendary1 helmets (Wyrmhorn horns / Starweaver crown-fans / Plumed-Hood
    crest-feathers) spread UP-and-OUTWARD above the skull.
  * Legendary2 helmets (Crest circlets) are a single NARROW, TALL vertical fin
    rising straight UP from the crown.
  * Legendary3 helmets (Winged helms) fan WIDE and near-horizontal OUTWARD from
    the sides at skull height.
  * All three prior silhouettes add mass AT-or-ABOVE the head. This one adds mass
    BELOW it: a curtain that hangs DOWN each side of the face, framing it and
    ending at the shoulder line — the previously-unused downward axis, the same
    four-way contrast the other slots draw.

Authoring philosophy is identical to gen_winghelm_legendary.py /
gen_sabaton_boots.py:
  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the aventail. Only the OUTER SIDEW columns of each helmet's bottom
    contour spawn a drape (the centre columns are left open so the face stays
    visible). For each such column we hang a contiguous vertical run starting one
    row BELOW that column's own lowest helmet pixel, so the top drape pixel is
    always 4-connected upward to the helm and the whole curtain is one component
    fused to the body (QA-safe: no isolated pixels, no accent-caused
    multi-component frames). The run is longest at the outer edge and tapers
    inward (TAPER) so the curtain curves around the jaw. Drawn ONLY in transparent
    space below the helm — never overpaints the body.

Connectivity is further guaranteed with the same per-frame guard as the wing /
cape / sabaton: any drape pixel not 4-connected to the body mass is cleared, so
accent strays are 0 by construction.

Because the drape is anchored RELATIVE to each frame's own helmet-bottom contour,
it tracks the character's animation bob exactly (no absolute-Y drift). Sleep /
empty frames have no helmet pixels, so they are simply skipped.

Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (mail hue distinct from that class's other three helmet accents so all
four read apart; the DOWNWARD silhouette is the headline):
  * warrior "Ironmaw Camail"   — dark-steel helm + blackened-steel mail, silver rim
  * mage    "Nightweave Veil"  — cosmic hat  + deep-indigo mail, starlight-silver
  * ranger  "Thornmesh Aventail"— forest hood + bronze/verdigris scale-mail

Run from repo root:
  python3 scripts/gen_aventail_helmet.py
Then QA:
  python3 scripts/sprite_qa.py _aventail_helmet_preview/helmet_warrior_legendary4.png --y-min 2 --y-max 63
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

# Aventail geometry. Only the outer SIDEW columns of the helmet's bottom contour
# spawn a drape; centre columns stay open so the face shows. DROP = rows the
# outer-edge column hangs (class-tuned so every class reaches ~shoulder line
# regardless of how low its helm already sits). TAPER = rows lost per column
# stepping inward toward the face, so the curtain curves around the jaw.
SIDEW = 3              # #outer columns per side that spawn a drape
TAPER = 2             # drape rows lost per column stepping inward

# ── Per-class palettes: body ramp (D/M/L) + mail ramp (RIM, HEM, M, L) + DROP ──
# body: deep shadow / base / highlight
# mail: RIM (bright leading-edge glint) / HEM (dark scalloped bottom) /
#       M (mid scale) / L (lit scale)  — body checkerboards M/L for a mail read
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary4', drop=4,
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),                    # dark iron -> steel
        mail=((214, 220, 232), (26, 28, 36), (84, 90, 104), (150, 158, 176)),   # blackened steel, silver rim
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary4', drop=8,
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                     # cosmic indigo -> violet
        mail=((198, 212, 255), (18, 16, 54), (60, 54, 146), (120, 118, 208)),   # deep-indigo mail, starlight rim
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary4', drop=9,
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                       # forest green
        mail=((220, 206, 150), (28, 30, 20), (96, 90, 52), (150, 142, 96)),     # bronze/verdigris scale
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


def mail_tone(x, y, j, drop, outer, pal):
    """Pick an aventail tone. pal = (RIM, HEM, M, L). j = px down from the helm
    (1..drop). The outer leading column reads as the bright RIM; the bottom row is
    the dark scalloped HEM; the body checkerboards lit/mid scale."""
    RIM, HEM, M, L = pal
    if j == drop:
        return HEM                        # dark scalloped hem at the bottom
    if outer:
        return RIM                        # bright leading edge of the drape
    return L if ((x + y) % 2 == 0) else M  # scale-mail checkerboard


def draw_aventail(fr, a, drop, pal):
    """Hang a mail curtain down the outer columns of the helmet's bottom contour."""
    cols = np.where(a.any(axis=0))[0]
    if cols.size == 0:
        return
    xmin, xmax = int(cols.min()), int(cols.max())
    for x in cols:
        col_ys = np.where(a[:, x])[0]
        y_col = int(col_ys.max())          # this column's own lowest helm pixel
        d_left, d_right = x - xmin, xmax - x
        if d_left < SIDEW:                 # left band
            side_d, outer = d_left, (d_left == 0)
        elif d_right < SIDEW:              # right band
            side_d, outer = d_right, (d_right == 0)
        else:                              # centre columns: leave the face open
            continue
        n = drop - side_d * TAPER          # longest at the outer edge
        if n < 1:
            continue
        for j in range(1, n + 1):
            y = y_col + j
            if y >= FH:
                break
            if a[y, x] or fr[y, x, 3] > 0:  # never overpaint body/existing
                continue
            put(fr, y, x, mail_tone(x, y, j, n, outer, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['mail']
    drop = cfg['drop']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():                    # empty (incl. sleep) frames skipped
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        draw_aventail(fr, a, drop, pal)
        # Connectivity guard: drop any drape pixel not 4-connected to the body
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
    outdir = '_aventail_helmet_preview'
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
