#!/usr/bin/env python3
"""Generate a FOURTH net-new-geometry LEGS silhouette per class — articulated
KNEE-COP POLEYNS: rounded plate discs that bulge OUTWARD at the KNEES (a lateral
mid-leg mass), distinct from ALL three prior legendary legs which hang from the
hips and read top-to-hem.

Why this is a NEW silhouette (not a recolor, not a repeat of an existing axis):
  * legendary1 (Seraph Greaves / Starweaver Robe-Tassets / Skyhunter Pelt-Tassets)
    are SHORT PAIRED hip-flaps — small tabs at the very top of the legs.
  * legendary2 (Warlord's Battle-Kilt / Astral Ritual-Skirt / Wildwood War-Kilt)
    is a long SMOOTH cloth drape widening to a soft flared HEM at the bottom.
  * legendary3 (Bronze/Rune/Scale Faulds) is a STIFF tiered plate skirt hanging
    from the hips to knee-length.
  * ALL three above put their mass at the HIP and/or HEM and run vertically.
    These POLEYNS instead put a compact ROUND plate disc at the KNEE that bulges
    OUTWARD then tapers back in above and below — a mid-leg LATERAL bulge, an
    axis none of the prior legs use. The disc has a lit central boss + a rivet
    trim rim so it reads as a domed articulated knee-cop, not cloth or a skirt.

Authoring philosophy is identical to gen_faulds_legs.py / gen_cape_legendary.py:
  * Body  = the class t4 pants silhouette (armor_pants_4 / pants_mage4 /
    pants_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, 0 src px dropped.
  * Accent = a knee-cop disc hugging each OUTER leg edge, confined to a KNEE
    Y-BAND. For every band row the disc's off=1 column is edge-adjacent to that
    row's own outer edge, and off-ranges are a contiguous 1..width whose width
    changes <=1 per row (round profile: peaks at the knee centre, tapers to 1 at
    the band top/bottom), so each side's poleyn is one connected component fused
    to the body (QA-safe: no isolated pixels, no accent-caused multi-component
    frames). Drawn ONLY in transparent out-of-silhouette space — never overpaints
    the body.

Connectivity is further guaranteed with the same per-frame guard as the kilt /
faulds: any poleyn pixel not 4-connected to the body mass (rare contorted poses
that split a leg edge) is cleared, so accent strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no poleyns. Shading is
applied in-script via shade(); do NOT run sprite_shade.py again.

Per class (knee-cop metal distinct in HUE from that class's prior legendary legs
so the four legs read as four different sets):
  * warrior "Warlord's Aegis Poleyns" — obsidian body + STEEL-BLUE knee-cops, gold rivets
  * mage    "Astral Rose-Poleyns"      — arcane-violet body + ROSE/magenta knee-cops, silver rivets
  * ranger  "Wildwood Bone-Poleyns"    — forest body + BONE/ivory knee-cops, tan rivets

Run from repo root:
  python3 scripts/gen_poleyn_legs.py
Then QA (accents intentionally extend outside the normal leg zone -> bleed OK):
  python3 scripts/sprite_qa.py _poleyn_legs_preview/pants_warrior_legendary4.png --y-max 62
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

# Knee-cop geometry. The disc is centred a fraction KNEE_FRAC down each frame's
# own leg silhouette and spans BAND_HALF rows above/below that centre. Width
# follows a rounded profile peaking at MAXW at the centre and tapering to 1 at
# the band edges, so the outer profile domes OUTWARD at the knee then pulls back
# in — a compact lateral bulge, not a hip-to-hem drape.
KNEE_FRAC = 0.55      # knee sits ~55% down the leg silhouette
BAND_HALF = 3         # rows above/below knee centre (7-row disc)
MAXW = 4              # widest outward reach at the knee centre
Y_DISC_MAX = 59       # never draw disc below this row (keeps it off the foot/bg
                      # zone at y>=60 for both genders)

# ── Per-class palettes: body ramp (D/M/L) + knee-cop ramp (RIVET, D, M, L) ─────
# body:    deep shadow / base / highlight
# poleyn:  RIVET (bright rim/stud) / D (rim shadow) / M (mid plate) / L (lit boss)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary4',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),            # obsidian->steel
        cop=((255, 214, 96), (28, 42, 74), (66, 96, 150), (150, 184, 232)),  # steel-blue, gold rivet
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary4',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),            # arcane violet
        cop=((232, 232, 244), (72, 14, 46), (150, 40, 98), (222, 112, 172)),  # rose/magenta, silver rivet
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary4',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),              # forest green
        cop=((214, 184, 122), (70, 62, 48), (150, 138, 108), (226, 218, 190)),  # bone/ivory, tan rivet
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


def cop_tone(off, width, pal):
    """Pick a knee-cop tone. pal = (RIVET, D, M, L)."""
    RIVET, D, M, L = pal
    if off >= width and width >= 2:
        return RIVET                      # bright outer rivet/rim stud
    if off >= width - 1 and width >= 3:
        return D                          # rim shadow just inside the stud
    if off <= 1:
        return L                          # lit central boss against the leg
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


def draw_poleyn(fr, a, sign, pal):
    edges, y0, y1 = side_edges(a, sign)
    if not edges:
        return
    span = y1 - y0
    knee = y0 + int(round(KNEE_FRAC * span))
    yb0, yb1 = knee - BAND_HALF, knee + BAND_HALF
    last_edge = edges[y1]
    for y in range(yb0, yb1 + 1):
        if not (0 <= y <= Y_DISC_MAX and y < FH):
            continue
        edge_x = edges.get(y, last_edge)
        # rounded profile: full width at the knee centre, taper to 1 at band ends
        dy = abs(y - knee)
        width = 1 + int(round((1.0 - dy / max(BAND_HALF, 1)) * (MAXW - 1)))
        width = max(width, 1)
        for off in range(1, width + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                   # never overpaint the body
                continue
            put(fr, y, x, cop_tone(off, width, pal))


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['cop']
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
            draw_poleyn(fr, a, sign, pal)
        # Connectivity guard: drop any knee-cop pixel not 4-connected to the body
        # mass (contorted poses can split a leg edge and strand a disc fragment);
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
    outdir = '_poleyn_legs_preview'
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
