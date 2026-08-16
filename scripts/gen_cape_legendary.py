#!/usr/bin/env python3
"""Generate a THIRD net-new-geometry chest showcase per class — a heavy draped
"warcape" legendary that changes the silhouette with a cape DRAPING DOWN and
FLARING OUTWARD at the hem (distinct from the winged chests, which flare UP at
the back, and the pauldron chests, which spike UP at the shoulders).

Same QA-safe authoring philosophy as gen_pauldron_legendary.py / gen_seraph_legs.py:
  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose / animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = a pair of draped CAPE sheets that hug each side edge of the torso
    and flare outward toward the hem (widening down the body, hanging a few rows
    below the tunic). For every body row the cape's off=1 column is edge-adjacent
    to that row's own outer edge, and the off ranges are contiguous 1..width with
    width changing <=1 per row, so each side's cape is one connected component
    fused to the torso (QA-safe: no isolated pixels, no accent-caused
    multi-component frames). Drawn ONLY in transparent out-of-silhouette space —
    never overpaints the body.

Per class (fabric distinct in HUE from every prior legendary, silhouette is the
headline):
  * warrior "Warlord's Warcape"   — obsidian/steel body + crimson->ember cape, gold trim
  * mage    "Astral Shroud"        — arcane-violet body + midnight->starfield cape, silver trim
  * ranger  "Wildwood Cloak"       — forest body + umber->moss leather cape, tan-fur trim

Sleep frames (fi>=60, lying down) get the recolor only — no cape — matching the
winged-chest / pauldron / hat convention. Shading applied in-script via shade();
do NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_cape_legendary.py
Then QA (accents intentionally extend outside the normal x30-55 zone -> bleed OK):
  python3 scripts/sprite_qa.py _cape_legendary_preview/shirt_warrior_legendary3.png
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

# Cape geometry: how far the hem hangs below the tunic bottom, and max fabric width.
# Y_HEM_MAX keeps the hem inside the QA character zone (y<=52) for BOTH genders so
# the cape passes sprite_qa clean with no background-bleed flag (like the seraph legs).
HEM_DROP = 4
MAXW = 5
Y_HEM_MAX = 52

# ── Per-class palettes: body ramp (D/M/L) + cape ramp (TRIM, D, M, L) ──────────
# body:  deep shadow / base / highlight
# cape:  TRIM (bright hem/edge) / D (fold shadow) / M (mid fabric) / L (lit fold)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary3',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),          # obsidian->steel
        cape=((255, 205, 90), (74, 12, 14), (150, 28, 26), (214, 70, 40)),  # crimson->ember, gold trim
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary3',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),          # arcane violet
        cape=((222, 232, 255), (12, 14, 44), (30, 36, 96), (70, 84, 176)),  # midnight->starfield, silver trim
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary3',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),            # forest green
        cape=((214, 196, 150), (44, 30, 18), (86, 60, 34), (120, 108, 60)),  # umber->moss leather, tan trim
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


def cape_tone(off, width, pal):
    """Pick a cape tone. pal = (TRIM, D, M, L)."""
    TRIM, D, M, L = pal
    if off >= width and width >= 2:
        return TRIM                       # bright outer hem/edge trim
    if off >= width - 1 and width >= 3:
        return D                          # fold shadow just inside the trim
    if off <= 1:
        return L                          # lit inner fold against the body
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


def draw_cape(fr, a, sign, pal):
    edges, y0, y1 = side_edges(a, sign)
    if not edges:
        return
    last_edge = edges[y1]
    total = (y1 - y0) + HEM_DROP
    for y in range(y0, min(y1 + HEM_DROP, Y_HEM_MAX, FH - 1) + 1):
        edge_x = edges.get(y, last_edge)
        p = (y - y0) / max(total, 1)
        width = 1 + round(p * (MAXW - 1))
        for off in range(1, width + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                   # never overpaint the body
                continue
            put(fr, y, x, cape_tone(off, width, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['cape']
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
            draw_cape(fr, a, sign, pal)
        # Connectivity guard: drop any cape pixel not 4-connected to the body
        # mass. A few contorted poses (e.g. female slash, fi=55) split the torso
        # edge and can strand a hem fragment; this removes ONLY such floaters
        # (never touches body px), so accent strays are 0 by construction.
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)         # 4-connectivity (default structure)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0                # clear stranded accent pixel
    return out


def main():
    outdir = '_cape_legendary_preview'
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
