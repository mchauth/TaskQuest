#!/usr/bin/env python3
"""Generate a SECOND net-new-geometry chest showcase per class — a heavy
"great-pauldron" legendary that changes the silhouette at the SHOULDERS
(distinct from the already-staged winged chests, which flare at the back).

Same QA-safe authoring philosophy as gen_seraph_legs.py:
  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose / animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = a pair of large layered SPAULDERS (shoulder plates tapering to a
    spike) fanning UP-and-OUTWARD from each shoulder corner, mirrored L/R, drawn
    ONLY in transparent (out-of-silhouette) space and edge-adjacent to the body,
    so each spaulder is one connected component with the torso (QA-safe: no
    isolated pixels, no accent-caused multi-component frames).

Per class:
  * warrior "Colossus Pauldrons"  — obsidian/steel body + molten-copper spikes
  * mage    "Archon's Mantle"      — arcane-violet body + prismatic cyan crystal
  * ranger  "Wildwarden's Spaulders" — forest body + bone-white tusked plates

Sleep frames (fi>=60, lying down) get the recolor only — no spaulders — matching
the winged-chest / hat convention. Shading applied in-script via shade(); do NOT
run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_pauldron_legendary.py
Then QA (accents intentionally extend outside the normal x30-55 zone):
  python3 scripts/sprite_qa.py _pauldron_legendary_preview/shirt_warrior_legendary2.png
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# ── Per-class palettes: body ramp (D/M/L) + spaulder ramp (edge/D/M/L) ─────────
# body: deep shadow / base / highlight   spaulder: outline / shadow / mid / lit
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary2',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),      # obsidian->steel
        sp=((70, 30, 8), (150, 60, 15), (230, 120, 30), (255, 205, 120)),  # molten copper
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary2',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),      # arcane violet
        sp=((18, 58, 88), (30, 120, 160), (72, 200, 230), (206, 250, 255)),  # cyan crystal
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary2',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),        # forest green
        sp=((92, 80, 58), (150, 138, 108), (212, 202, 172), (246, 242, 224)),  # bone white
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


# ── Spaulder: layered shoulder plate rising up-and-out, tapering to a spike ────
# dy = rows ABOVE the shoulder anchor -> outward reach (off) from the edge column.
# Contiguous off ranges + <=1 change between rows => the whole fan is 4-connected
# and its dy=0 off=1 pixel is edge-adjacent to the body (roots the plate).
SPAULDER = {0: 3, 1: 4, 2: 4, 3: 3, 4: 2, 5: 1}


def sp_tone(dy, off, outer, pal):
    """Pick a spaulder tone. pal = (EDGE, D, M, L)."""
    EDGE, D, M, L = pal
    if off >= outer:
        return EDGE                      # outer outline
    if off >= outer - 1:
        return D                         # shadow just inside the edge
    if off <= 1 and dy <= 2:
        return L                         # lit top-inner face
    return M


def shoulder_anchor(a, sign, band=6):
    """Return (edge_x, anchor_y) for the given side's SHOULDER.

    Anchor at the TOP band of the torso silhouette (neck/shoulder area):
    anchor_y = the top row that actually carries a pixel at the outermost column
    within the top `band` rows on that side, so the off=1 accent pixel is
    edge-adjacent to the body for connectivity, and edge_x is the shoulder
    corner (never mid-torso)."""
    ys, xs = np.where(a)
    top_y = int(ys.min())
    band_mask = a[top_y:top_y + band, :]
    bxs = np.where(band_mask.any(axis=0))[0]
    edge_x = int(bxs.min()) if sign < 0 else int(bxs.max())
    col = np.flatnonzero(a[top_y:top_y + band, edge_x])
    anchor_y = top_y + int(col.min()) if col.size else top_y
    return edge_x, anchor_y


def draw_spaulder(fr, a, edge_x, anchor_y, sign, pal):
    for dy, outer in SPAULDER.items():
        y = anchor_y - dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                  # never overpaint the body
                continue
            put(fr, y, x, sp_tone(dy, off, outer, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['sp']
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
        if fi >= 60:                     # sleep: body only
            continue
        for sign in (-1, +1):
            edge_x, anchor_y = shoulder_anchor(a, sign)
            draw_spaulder(fr, a, edge_x, anchor_y, sign, pal)
    return out


def main():
    outdir = '_pauldron_legendary_preview'
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
