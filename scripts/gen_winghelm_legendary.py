#!/usr/bin/env python3
"""Generate a THIRD net-new-geometry HELMET silhouette per class — a WINGED HELM
whose accent is a pair of feathered wings sweeping HORIZONTALLY OUTWARD from the
sides of the head.

Why this is a NEW helmet silhouette (not a recolor, not a repeat):
  * The first legendary helmets (warrior Wyrmhorn horns, mage Starweaver
    crown-fans, ranger Plumed-Hood crest-feathers) all spread UP-and-OUTWARD
    above the skull — a tall, upward profile.
  * The second legendary helmets (the Crest circlets) are a single NARROW,
    TALL vertical fin rising straight up from the crown.
  * BOTH prior helmet silhouettes therefore extend UPWARD. This one extends
    WIDE: a broad, low, near-horizontal wing fanning OUTWARD from each side of
    the head at roughly skull height — a horizontal span clearly distinct from
    both upward profiles, occupying the previously-unused sideways axis.

Authoring philosophy is identical to gen_crest_legendary.py / gen_cape_legendary.py:
  * Body  = the class helmet silhouette (helmet_rare1 / helmet_mage4 /
    helmet_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose/animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = for each side, a feathered wing centred on that side's WIDEST row
    (the brim / skull-full-width band). Each wing row draws a contiguous
    outward run off=1..span starting edge-adjacent to that row's own outer edge,
    so off=1 is always horizontally adjacent to a body pixel and the whole wing
    is one 4-connected component fused to the helm (QA-safe: no isolated pixels,
    no accent-caused multi-component frames). span tapers above/below the centre
    row into a wing/leaf profile. Drawn ONLY in transparent out-of-silhouette
    space — never overpaints the body.

Connectivity is further guaranteed with the same per-frame guard as the cape /
greave: any wing pixel not 4-connected to the body mass is cleared, so accent
strays are 0 by construction.

Wings sit at head height (y ~ 18..30) so they never intrude on the torso/floor.
Like the winged chest and horned helm, the wings legitimately extend past the
x30-55 character box, so sprite_qa reports BACKGROUND-BLEED at the wing columns
— that is the intended silhouette, not a stray.

Per class (wing plumage distinct in HUE, silhouette is the headline):
  * warrior "Valkyr War-Wings" — steel helm + white->gold seraph-plumage wings
  * mage    "Astral Aether-Wings" — cosmic hat + cyan->violet arcane wings
  * ranger  "Falcon Wing-Helm" — forest hood + cream->russet hawk wings

Helmets have no sleep-frame accent convention issue: helmet source sheets are
empty on the sleep frames, so those frames are simply skipped.

Run from repo root:
  python3 scripts/gen_winghelm_legendary.py
Then QA (accents intentionally extend outside the x30-55 zone -> bleed OK):
  python3 scripts/sprite_qa.py _winghelm_legendary_preview/helmet_warrior_legendary3.png --y-min 2
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

# Wing geometry. The wing is a horizontal fan centred on each side's widest row.
# SPAN_MAX = farthest the centre row reaches outward; the fan tapers TAPER px per
# row away from the centre. BAND_UP/BAND_DN = rows above/below the centre the wing
# spans. Y_MIN clamps every wing pixel into the QA head zone (y>=2).
SPAN_MAX = 10          # centre-row outward reach (px beyond the head edge)
TAPER = 2              # span lost per row of vertical distance from the centre
BAND_UP = 3            # wing rows above the centre row
BAND_DN = 2            # wing rows below the centre row
Y_MIN = 2              # never draw a wing pixel above this row (head zone)

# ── Per-class palettes: body ramp (D/M/L) + wing ramp (TIP, D, M, L) ───────────
# body: deep shadow / base / highlight
# wing: TIP (bright leading/tip feather) / D (trailing-edge shadow) /
#       M (mid vane) / L (lit inner vane against the head)
CLASSES = {
    'warrior': dict(
        src='helmet_rare1', dst='helmet_warrior_legendary3',
        body=((40, 42, 50), (92, 96, 110), (150, 156, 172)),               # dark iron -> steel
        wing=((255, 236, 150), (120, 96, 30), (206, 176, 92), (245, 232, 196)),  # white->gold seraph plumage
    ),
    'mage': dict(
        src='helmet_mage4', dst='helmet_mage_legendary3',
        body=((16, 16, 58), (44, 40, 120), (110, 96, 200)),                # cosmic indigo -> violet
        wing=((210, 240, 255), (40, 30, 96), (70, 70, 176), (150, 170, 240)),   # cyan->violet arcane
    ),
    'ranger': dict(
        src='helmet_ranger4', dst='helmet_ranger_legendary3',
        body=((18, 38, 16), (44, 84, 38), (92, 146, 78)),                  # forest green
        wing=((240, 228, 196), (52, 32, 18), (120, 78, 44), (188, 150, 104)),   # cream->russet hawk plumage
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


def wing_tone(off, span, dist, pal):
    """Pick a wing tone. pal = (TIP, D, M, L). off = px out from the head edge
    (1..span); dist = |row - centre|. The outer tip and every 3rd primary read
    as the bright TIP feather; the trailing (bottom) rows shade to D."""
    TIP, D, M, L = pal
    if off >= span and span >= 2:
        return TIP                          # bright outer tip feather
    if off % 3 == 0 and off < span:
        return TIP                          # separated primary highlight
    if dist >= BAND_DN and off > span - 2:
        return D                            # trailing-edge shadow
    if off <= 1:
        return L                            # lit inner vane against the head
    return M


def side_edges(a, sign):
    """Per-row outer edge on one side, plus the row with the max outward reach."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return {}, None
    edges = {}
    for y in range(int(rows.min()), int(rows.max()) + 1):
        xs = np.where(a[y])[0]
        if xs.size:
            edges[y] = int(xs.min()) if sign < 0 else int(xs.max())
    if not edges:
        return {}, None
    # widest row on this side = most outward edge (min x for left / max x for right)
    yc = (min(edges, key=lambda y: edges[y]) if sign < 0
          else max(edges, key=lambda y: edges[y]))
    return edges, yc


def draw_wing(fr, a, sign, pal):
    edges, yc = side_edges(a, sign)
    if yc is None:
        return
    last_edge = edges[yc]
    for y in range(yc - BAND_UP, yc + BAND_DN + 1):
        if y < Y_MIN or y >= FH:
            continue
        dist = abs(y - yc)
        span = SPAN_MAX - TAPER * dist
        if span < 2:
            continue
        edge_x = edges.get(y, last_edge)
        for off in range(1, span + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW):
                continue
            if a[y, x]:                      # never overpaint the body
                continue
            put(fr, y, x, wing_tone(off, span, dist, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['wing']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():                      # empty (incl. sleep) frames skipped
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        for sign in (-1, +1):
            draw_wing(fr, a, sign, pal)
        # Connectivity guard: drop any wing pixel not 4-connected to the body
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
    outdir = '_winghelm_legendary_preview'
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
