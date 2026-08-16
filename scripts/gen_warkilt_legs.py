#!/usr/bin/env python3
"""Generate a SECOND net-new-geometry LEGS silhouette per class — a knee-length
draped WAR-KILT that hangs from the hips and flares OUTWARD toward its hem.

Why this is a NEW silhouette (not a recolor, not a repeat):
  * The already-staged legendary legs (Seraph Greaves / Starweaver's Robe-Tassets
    / Skyhunter's Pelt-Tassets) are SHORT PAIRED hip-flaps: a couple of small
    feathered tabs at the very top corners of the leg (~6 rows).
  * The war-kilt is a CONTINUOUS draped skirt that runs down the OUTER edge of
    each leg from the hip to about knee height and flares outward at the hem — a
    long, wide, pleated profile clearly distinct from the short tassets, and
    distinct from the torso-level cape (which drapes from the chest).

Authoring philosophy is identical to gen_cape_legendary.py / gen_seraph_legs.py:
  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose/animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = a draped kilt sheet hugging each OUTER side edge of the legs. For
    every leg row the kilt's off=1 column is edge-adjacent to that row's own
    outer edge, and off ranges are a contiguous 1..width with width changing <=1
    per row, so each side's kilt is one connected component fused to the body
    (QA-safe: no isolated pixels, no accent-caused multi-component frames). Drawn
    ONLY in transparent out-of-silhouette space — never overpaints the body.

Connectivity is further guaranteed with the same per-frame guard as the cape:
any kilt pixel not 4-connected to the body mass (rare contorted poses that split
a leg edge) is cleared, so accent strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no kilt — matching the
tasset / cape / hat convention. Shading applied in-script via shade(); do NOT run
sprite_shade.py again.

Per class (fabric distinct in HUE, silhouette is the headline):
  * warrior "Warlord's Battle-Kilt" — obsidian/steel body + crimson->ember kilt, gold-stud hem
  * mage    "Astral Ritual-Skirt"   — arcane-violet body + midnight->starfield kilt, silver hem
  * ranger  "Wildwood War-Kilt"      — forest body + umber->moss leather kilt, tan-fur hem

Run from repo root:
  python3 scripts/gen_warkilt_legs.py
Then QA (accents intentionally extend outside the normal leg zone -> bleed OK):
  python3 scripts/sprite_qa.py _warkilt_legs_preview/pants_warrior_legendary2.png --y-max 62
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

# Kilt geometry. The kilt starts at the hip (silhouette top) and runs down for a
# limited number of rows (knee-length), widening toward the hem. KILT_ROWS caps
# the length so the hem lands about knee height, not at the feet. Y_HEM_MAX keeps
# the hem inside the QA character zone for both genders. MAXW is the widest the
# hem flares.
KILT_ROWS = 20        # rows below the hip that the kilt covers (knee-length)
MAXW = 5              # widest outward reach at the hem
Y_HEM_MAX = 58        # never draw kilt below this row (keeps hem out of the QA
                      # foot/background zone at y>=60 for both genders)

# ── Per-class palettes: body ramp (D/M/L) + kilt ramp (TRIM, D, M, L) ──────────
# body:  deep shadow / base / highlight
# kilt:  TRIM (bright hem/stud edge) / D (pleat shadow) / M (mid fabric) / L (lit pleat)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary2',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian->steel
        kilt=((255, 205, 90), (74, 12, 14), (150, 28, 26), (214, 70, 40)),  # crimson->ember, gold-stud hem
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary2',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        kilt=((222, 232, 255), (12, 14, 44), (30, 36, 96), (70, 84, 176)),  # midnight->starfield, silver hem
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary2',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        kilt=((214, 196, 150), (44, 30, 18), (86, 60, 34), (120, 108, 60)),  # umber->moss leather, tan hem
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


def kilt_tone(y, off, width, pal):
    """Pick a kilt tone. pal = (TRIM, D, M, L). A vertical pleat pattern (every
    other column steps darker) reads as fabric folds, distinguishing the kilt
    from the smoother cape."""
    TRIM, D, M, L = pal
    if off >= width and width >= 2:
        return TRIM                       # bright outer hem / stud edge
    if off >= width - 1 and width >= 3:
        return D                          # fold shadow just inside the hem
    if off <= 1:
        return L                          # lit inner pleat against the leg
    # mid fabric with an alternating vertical-pleat shadow
    return D if (off % 2 == 0) else M


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


def draw_kilt(fr, a, sign, pal):
    """One draped kilt down the OUTER edge on side `sign`, hip->knee, flaring out."""
    edges, y0, y1 = side_edges(a, sign)
    if not edges:
        return
    y_bottom = min(y0 + KILT_ROWS, y1, Y_HEM_MAX, FH - 1)
    total = max(y_bottom - y0, 1)
    last_edge = edges[y0]
    for y in range(y0, y_bottom + 1):
        edge_x = edges.get(y, last_edge)
        last_edge = edge_x
        p = (y - y0) / total
        width = 1 + round(p * (MAXW - 1))   # 1 at hip -> MAXW at hem, +/-1 per row
        for off in range(1, width + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                     # never overpaint the body
                continue
            put(fr, y, x, kilt_tone(y, off, width, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['kilt']
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
            draw_kilt(fr, a, sign, pal)
        # Connectivity guard: drop any kilt pixel not 4-connected to the body
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
    outdir = '_warkilt_legs_preview'
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
