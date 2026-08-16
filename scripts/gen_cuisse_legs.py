#!/usr/bin/env python3
"""Generate a FIFTH net-new-geometry LEGS silhouette per class — flared
HIP-WING CUISSES: a bold armoured fin that juts OUTWARD at the HIP (the very top
of the leg) and tapers back in as it descends, an upper-leg LATERAL flare. This
is an axis none of the four prior legendary legs use.

Why this is a NEW silhouette (not a recolor, not a repeat of an existing axis):
  * legendary1 (Seraph Greaves / Starweaver Robe-Tassets / Skyhunter Pelt-Tassets)
    are SHORT PAIRED hip-flaps that hang straight DOWN — narrow vertical tabs.
  * legendary2 (Warlord's Battle-Kilt / Astral Ritual-Skirt / Wildwood War-Kilt)
    is a long SMOOTH cloth drape widening to a soft flared HEM at the bottom.
  * legendary3 (Bronze/Rune/Scale Faulds) is a STIFF full-width tiered plate
    skirt hanging hip->knee, filling the gap between the legs.
  * legendary4 (Aegis/Rose/Bone Poleyns) is a compact ROUND disc that bulges
    OUTWARD at the KNEE (a mid-leg lateral mass) then pulls back in.
  * These CUISSES instead flare a broad triangular plate OUTWARD at the HIP —
    widest at the very top of the leg, tapering to nothing partway down. The
    mass is a LATERAL flare at the TOP of the leg (vs poleyn's lateral mass at
    the mid-leg KNEE, vs faulds' full-width central skirt, vs the vertical
    hip-flaps of legendary1). A bright rivet studs the outer rim, a lit boss
    hugs the leg, so it reads as a hinged articulated hip-plate, not cloth.

Authoring philosophy is identical to gen_poleyn_legs.py / gen_faulds_legs.py:
  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, 0 src px dropped.
  * Accent = a hip-wing plate hugging each OUTER leg edge, confined to a HIP
    Y-BAND at the top of each frame's own leg silhouette. For every band row the
    plate's off=1 column is edge-adjacent to that row's own outer edge, and
    off-ranges are a contiguous 1..width whose width changes <=1 per row (the fin
    is widest at the band top and tapers to 1 at the band bottom), so each side's
    cuisse is one connected component fused to the body (QA-safe: no isolated
    pixels, no accent-caused multi-component frames). Drawn ONLY in transparent
    out-of-silhouette space — never overpaints the body, so it can never become a
    central drape.

Connectivity is further guaranteed with the same per-frame guard as the poleyn /
kilt: any cuisse pixel not 4-connected to the body mass (rare contorted poses
that split a leg edge) is cleared, so accent strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no hip-wings. Shading
is applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (hip-plate metal distinct in HUE from that class's prior legendary legs
so the five legs read as five different sets):
  * warrior "Warlord's Bulwark Cuisses" — obsidian body + STEEL hip-wings, gold rivets
  * mage    "Astral Warding Cuisses"    — arcane-violet body + CYAN hip-wings, silver rivets
  * ranger  "Wildwood Warden Cuisses"   — forest body + COPPER hip-wings, tan rivets

Run from repo root:
  python3 scripts/gen_cuisse_legs.py
Then QA (accents intentionally extend outside the normal leg zone -> bleed OK):
  python3 scripts/sprite_qa.py _cuisse_legs_preview/pants_warrior_legendary5.png --y-max 62
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

# Hip-wing geometry. The fin is anchored at the TOP of each frame's own leg
# silhouette and spans BAND_LEN rows downward (a fraction of the leg span, capped
# so it stays in the UPPER leg — clearly above the poleyn's knee band). Width is
# widest at the band TOP (MAXW) and tapers to 1 at the band bottom, so the outer
# profile flares OUTWARD sharply at the hip then pulls back in — a lateral flare
# at the TOP of the leg, not a hip-to-hem drape and not a mid-leg knee disc.
BAND_FRAC = 0.42      # fin spans the top ~42% of the leg silhouette
BAND_MIN, BAND_MAX = 6, 11   # clamp band length in rows
MAXW = 5              # widest outward reach at the hip (bold flare)
Y_HIP_MIN = 2         # never draw above this row (safety; hips sit far below it)

# Per-class palettes: body ramp (D/M/L) + hip-plate ramp (RIVET, D, M, L)
#   body:  deep shadow / base / highlight
#   wing:  RIVET (bright rim/stud) / D (rim shadow) / M (mid plate) / L (lit boss)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary5',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),                 # obsidian->steel
        wing=((255, 214, 96), (44, 48, 58), (108, 116, 132), (182, 192, 210)),  # steel plate, gold rivet
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary5',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),                 # arcane violet
        wing=((236, 240, 248), (16, 58, 74), (36, 118, 150), (108, 202, 226)),  # cyan plate, silver rivet
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary5',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                   # forest green
        wing=((222, 196, 140), (58, 34, 18), (128, 74, 36), (196, 128, 66)),    # copper plate, tan rivet
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


def wing_tone(off, width, pal):
    """Pick a hip-plate tone. pal = (RIVET, D, M, L)."""
    RIVET, D, M, L = pal
    if off >= width and width >= 2:
        return RIVET                      # bright outer rivet/rim stud
    if off >= width - 1 and width >= 3:
        return D                          # rim shadow just inside the stud
    if off <= 1:
        return L                          # lit boss against the leg
    return M


def side_edges(a, sign):
    """Return (edges: dict row->outer edge_x on this side, y0, y1)."""
    rows = np.where(a.any(axis=1))[0]
    y0, y1 = int(rows.min()), int(rows.max())
    edges = {}
    for y in range(y0, y1 + 1):
        xs = np.where(a[y])[0]
        if xs.size:
            edges[y] = int(xs.min()) if sign < 0 else int(xs.max())
    return edges, y0, y1


def draw_hipwing(fr, a, sign, pal):
    edges, y0, y1 = side_edges(a, sign)
    if not edges:
        return
    span = y1 - y0
    band = int(round(BAND_FRAC * span))
    band = max(BAND_MIN, min(BAND_MAX, band))
    yb0 = max(y0, Y_HIP_MIN)
    yb1 = yb0 + band - 1
    last_edge = edges[y0]
    for y in range(yb0, yb1 + 1):
        if not (0 <= y < FH):
            continue
        edge_x = edges.get(y, last_edge)
        last_edge = edge_x
        # inverted-triangle profile: widest at the band TOP, taper to 1 at bottom
        frac = 1.0 - (y - yb0) / max(band - 1, 1)     # 1.0 at top -> 0.0 at bottom
        width = 1 + int(round(frac * (MAXW - 1)))
        width = max(width, 1)
        for off in range(1, width + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                   # never overpaint the body
                continue
            put(fr, y, x, wing_tone(off, width, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['wing']
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
        if fi >= 60:                      # sleep: body only
            continue
        for sign in (-1, +1):
            draw_hipwing(fr, a, sign, pal)
        # Connectivity guard: drop any hip-wing pixel not 4-connected to the body
        # mass (contorted poses can split a leg edge and strand a fin fragment);
        # this removes ONLY such floaters (never touches body px), so accent
        # strays are 0 by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)         # 4-connectivity (default structure)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0                # clear stranded accent pixel
    return out


def main():
    outdir = '_cuisse_legs_preview'
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
