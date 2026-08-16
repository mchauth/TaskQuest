#!/usr/bin/env python3
"""Generate a FIFTH NET-NEW-GEOMETRY BOOTS silhouette per class — WINGED ANKLE
BOOTS ("talaria"): a compact feathered wing that sweeps DIAGONALLY UP-AND-OUT
from each ankle. This completes the boots showcase to FIVE distinct silhouettes,
bringing the boots slot to parity with helmet / legs (5 axes each) and chest (6).

Why this is a NEW silhouette (distinct from ALL FOUR existing boots geometries):
  * "greave boots"  add mass ABOVE the boot   — a tall narrow shin plate climbing
    STRAIGHT UP to a knee-cop (pure-vertical profile).
  * "cuff boots"    add mass to the SIDE      — a folded cavalier cuff flaring
    FLAT/HORIZONTALLY OUTWARD across the ankle-top rows (pure-horizontal).
  * "sabaton boots" add mass at the BOTTOM    — a raked poulaine toe sweeping
    FORWARD along the GROUND row (a forward point).
  * "spur boots"    add mass at the HEEL      — a thin arm + rowel wheel projecting
    BACKWARD/OUTWARD at heel height (a horizontal back-spike).
  * These WINGED boots add mass on the DIAGONAL — a short feathered wing rising
    UP-AND-OUT from each ankle at ~45 degrees. Up (greave) / flat-out (cuff) /
    forward (sabaton) / back (spur) / diagonal-up-out (wing) is the five-way
    silhouette contrast that reads unmistakably apart at a glance. The stepped
    feather barbs at the wing's leading edge make it read as a wing, not a fin.

Authoring philosophy is identical to gen_spur_boots.py / gen_sabaton_boots.py /
gen_cuff_boots.py / gen_greave_boots.py:
  * Body  = the class t4 boot silhouette (armor_boots_4 / boots_mage4 /
    boots_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — every pose/animation tracked, source
    silhouette preserved (0 px dropped by construction).
  * Accent = the ankle wing. On the ankle row (WY_DY above the boot's own bottom
    row, i.e. ABOVE the ground/toe zone) we take that row's leftmost/rightmost
    boot pixel and grow a small wing OUTWARD-AND-UP as a stack of horizontal runs
    whose column ranges OVERLAP row-to-row, so the whole wing is 4-CONNECTED to
    the boot by construction (the base run sits directly above a boot pixel; each
    higher run shares columns with the run below it). Feather tips get the lit
    tone, the attach edge the dark tone. Drawn ONLY in transparent space, never
    overpaints the body.

Connectivity is further guaranteed with the same per-frame guard as the
spur/sabaton/cuff/greave: any accent pixel not 4-connected to the body mass is
cleared, so accent strays are 0 by construction.

Sleep frames (fi>=60, lying down) get the recolor only — no wing — matching the
spur / sabaton / cuff / tasset / kilt / cape convention. Shading applied in-script
via shade(); do NOT run sprite_shade.py again.

Per class (feather hue chosen distinct from that class's greave / cuff / sabaton
/ spur accents so all five boots read apart):
  * warrior "Valkyr Warstriders"     — dark-steel boot + silver-white feathers
  * mage    "Zephyr Voidwing Striders"— deep-violet boot + pale-lilac feathers
  * ranger  "Skyrunner Treads"       — bark-brown boot + cream/tan hawk feathers

Run from repo root:
  python3 scripts/gen_winged_boots.py
Then QA (the wing intentionally projects beyond the normal boot footprint):
  python3 scripts/sprite_qa.py _winged_boots_preview/boots_warrior_legendary_wing.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import shade               # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# ── Wing geometry ─────────────────────────────────────────────────────────────
# The wing anchors at ANKLE height: WY_DY rows above the boot's own bottom row
# (clearly ABOVE the ground/toe zone). From the side's own edge pixel it grows a
# 3-row wing whose successive horizontal runs step OUTWARD-AND-UP. Adjacent runs
# overlap in columns, so the wing is 4-connected by construction.
# Keep every wing pixel inside sprite_qa's background box (x in [30,55]) so the
# wing never bleeds into the neighbouring-frame margin.
BG_X_MIN, BG_X_MAX = 30, 55
WY_DY = 3            # rows above the boot bottom where the wing anchors
# Each tuple = (dy above anchor row, inner-offset, outer-offset) from the edge px,
# measured in the OUTWARD direction (sgn applied). Ranges overlap row-to-row.
WING_RUNS = (
    (1, 0, 3),       # low, near feathers  (cols edge .. edge+3out)
    (2, 1, 5),       # mid feathers        (cols edge+1out .. edge+5out)
    (3, 3, 6),       # high tip feathers   (cols edge+3out .. edge+6out)
)

# ── Per-class palettes: body ramp (D/M/L) + wing ramp (TIP, D, M, L) ───────────
# body: deep shadow / base / highlight
# wing: TIP (dark barb outline) / D (attach shadow) / M (mid feather) / L (lit tip)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_wing',
        body=((40, 42, 48), (84, 88, 98), (150, 156, 168)),                 # dark steel
        wing=((70, 74, 88), (120, 126, 142), (182, 188, 200), (240, 244, 252)),  # silver-white
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_wing',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),                 # deep violet
        wing=((64, 40, 100), (118, 90, 172), (176, 150, 220), (242, 234, 255)),  # pale lilac
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_wing',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),                   # bark brown
        wing=((72, 54, 30), (132, 104, 60), (196, 168, 116), (248, 238, 206)),  # cream/tan hawk
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def free(fr, a, y, x):
    """True if (y,x) is paintable: in the QA background box, not body, empty."""
    return (BG_X_MIN <= x <= BG_X_MAX and 0 <= y < FH
            and not a[y, x] and fr[y, x, 3] == 0)


def recolor(src, fr, a, D, M, L):
    """Quantized 3-tone recolor of the legendary silhouette (per-frame)."""
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_wing(fr, a, pal):
    """Compact feathered wing rising DIAGONALLY UP-AND-OUT from each ankle side."""
    TIP, D, M, L = pal
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return
    y1 = int(rows.max())
    y_a = y1 - WY_DY                       # ankle row (above the ground toe)
    if y_a < 4 or not a[y_a].any():
        return
    xs = np.where(a[y_a])[0]
    xmin, xmax = int(xs.min()), int(xs.max())
    for edge_x, sgn in ((xmin, -1), (xmax, +1)):
        for (dy, off_in, off_out) in WING_RUNS:
            ry = y_a - dy
            # horizontal feather run, laid from inner offset outward to the tip
            inner = edge_x + sgn * off_in
            outer = edge_x + sgn * off_out
            step = sgn
            xr = inner
            painted_tip = None
            while (step > 0 and xr <= outer) or (step < 0 and xr >= outer):
                if free(fr, a, ry, xr):
                    # tone: attach edge dark, body mid, outermost lit
                    if xr == inner and dy == 1:
                        tone = D
                    elif xr == outer:
                        tone = L
                    else:
                        tone = M
                    put(fr, ry, xr, tone)
                    painted_tip = xr
                xr += step
            # dark barb outline just beyond the lit tip of the top run
            if dy == WING_RUNS[-1][0] and painted_tip is not None:
                bx = painted_tip + sgn
                if free(fr, a, ry, bx):
                    put(fr, ry, bx, TIP)


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
        if fi >= 60:                       # sleep: body only
            continue
        draw_wing(fr, a, pal)
        # Connectivity guard: drop any accent pixel not 4-connected to the body
        # mass (only touches stranded accent px, never body px).
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        drop = da & ~keep
        for y, x in np.argwhere(drop):
            fr[y, x, :] = 0
    return out


CHAR = 'sprites/preview_assets/char'
FALLBACK_DIRS = ['_fem_warrior_boots_preview']


def load_src(fname):
    p = os.path.join(CHAR, fname)
    if os.path.exists(p):
        return np.array(Image.open(p).convert('RGBA'))
    for d in FALLBACK_DIRS:
        p = os.path.join(d, fname)
        if os.path.exists(p):
            return np.array(Image.open(p).convert('RGBA'))
    raise FileNotFoundError(fname)


def main():
    outdir = '_winged_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_src('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.18, adj_max=0.26)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-52s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
