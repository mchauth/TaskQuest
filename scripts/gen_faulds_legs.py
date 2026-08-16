#!/usr/bin/env python3
"""Generate a THIRD net-new-geometry LEGS silhouette per class — segmented
LAMELLAR PLATE FAULDS: a stiff, tiered plate skirt of stacked horizontal armor
bands hanging from the hips, distinct from BOTH prior legendary legs.

Why this is a NEW silhouette (not a recolor, not a repeat):
  * legendary1 (Seraph Greaves / Starweaver Robe-Tassets / Skyhunter Pelt-Tassets)
    are SHORT PAIRED hip-flaps (~6 rows) — small tabs at the leg-top corners.
  * legendary2 (Warlord's Battle-Kilt / Astral Ritual-Skirt / Wildwood War-Kilt)
    is a long SMOOTH cloth drape that widens MONOTONICALLY to a soft flared hem.
  * These faulds are STIFF METAL PLATE: the outer edge is TIERED/STEPPED (each
    lamellar band steps in 1px at its seam then holds), and every band carries a
    dark top-seam shadow + a lit plate-top highlight so the skirt reads as a
    stack of overlapping metal lames — clearly a plate silhouette, not cloth.

Authoring philosophy is identical to gen_warkilt_legs.py / gen_cape_legendary.py:
  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, 0 src px dropped.
  * Accent = a fauld sheet hugging each OUTER side edge of the legs. For every
    leg row the fauld's off=1 column is edge-adjacent to that row's own outer
    edge, and off-ranges are a contiguous 1..width, so each side's fauld is one
    connected component fused to the body (QA-safe: no isolated pixels, no
    accent-caused multi-component frames). Drawn ONLY in transparent
    out-of-silhouette space — never overpaints the body.

Connectivity is further guaranteed with the same per-frame guard as the kilt:
any fauld pixel not 4-connected to the body mass (rare contorted poses that split
a leg edge) is cleared, so accent strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no faulds. Shading is
applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (plate metal distinct in HUE from that class's cloth war-kilt):
  * warrior "Warlord's Bronze Faulds" — obsidian body + warm BRASS/BRONZE plates
  * mage    "Astral Rune-Faulds"      — arcane-violet body + CYAN/teal rune-plates
  * ranger  "Wildwood Scale-Faulds"   — forest body + burnished COPPER scale-plates

Run from repo root:
  python3 scripts/gen_faulds_legs.py
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

# Fauld geometry. The skirt starts at the hip (silhouette top) and runs down for
# a limited number of rows (knee-length). Unlike the smooth kilt it is built from
# discrete lamellar BANDS: BAND_H rows each, with a 1px step-in notch at every
# band seam so the outer profile is tiered rather than a smooth flare.
FAULD_ROWS = 20       # rows below the hip that the faulds cover (knee-length)
MAXW = 4              # widest outward reach (stiffer/narrower than the cloth kilt)
BAND_H = 4           # rows per lamellar band (segmentation period)
Y_HEM_MAX = 58        # never draw fauld below this row (keeps hem out of the QA
                      # foot/background zone at y>=60 for both genders)

# ── Per-class palettes: body ramp (D/M/L) + fauld ramp (TRIM, D, M, L) ─────────
# body:  deep shadow / base / highlight
# fauld: TRIM (bright rivet/hem) / D (seam shadow) / M (mid plate) / L (lit plate top)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary3',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian->steel
        fauld=((255, 224, 150), (70, 50, 20), (130, 96, 40), (196, 150, 70)),  # warm brass/bronze
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary3',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        fauld=((210, 255, 245), (10, 44, 50), (24, 92, 104), (70, 180, 190)),  # cyan/teal rune-plate
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary3',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        fauld=((240, 190, 120), (60, 28, 16), (128, 62, 32), (190, 110, 60)),  # burnished copper scale
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


def fauld_tone(rb, off, width, pal):
    """Pick a fauld tone. pal = (TRIM, D, M, L). rb = row index within the band.
    The band top row (rb==0) is a dark seam shadow; the row below (rb==1) is the
    lit plate top; the outer column is a bright rivet/hem; the rest is mid plate.
    This horizontal banding reads as stacked metal lames (vs the cloth kilt's
    vertical pleats)."""
    TRIM, D, M, L = pal
    if off >= width and width >= 2:
        return TRIM                       # bright outer rivet / plate edge
    if rb == 0:
        return D                          # dark seam shadow between lames
    if rb == 1:
        return L                          # lit top lip of the plate below the seam
    return M                              # plate body


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


def draw_fauld(fr, a, sign, pal):
    """One tiered lamellar fauld down the OUTER edge on side `sign`, hip->knee."""
    edges, y0, y1 = side_edges(a, sign)
    if not edges:
        return
    y_bottom = min(y0 + FAULD_ROWS, y1, Y_HEM_MAX, FH - 1)
    total = max(y_bottom - y0, 1)
    last_edge = edges[y0]
    for y in range(y0, y_bottom + 1):
        edge_x = edges.get(y, last_edge)
        last_edge = edge_x
        p = (y - y0) / total
        base = 1 + round(p * (MAXW - 1))     # 1 at hip -> MAXW near the hem
        rb = (y - y0) % BAND_H
        # 1px step-in notch at each band seam (except the very first row) -> the
        # outer profile is tiered rather than a smooth flare. Width change stays
        # small; each row is still a contiguous run anchored at off=1 (connected).
        width = base
        if rb == 0 and y != y0:
            width = max(1, base - 1)
        for off in range(1, width + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                     # never overpaint the body
                continue
            put(fr, y, x, fauld_tone(rb, off, width, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['fauld']
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
        if fi >= 60:                        # sleep: body only
            continue
        for sign in (-1, +1):
            draw_fauld(fr, a, sign, pal)
        # Connectivity guard: drop any fauld pixel not 4-connected to the body
        # mass (only touches stranded accent px, never body px).
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_faulds_legs_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-44s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
