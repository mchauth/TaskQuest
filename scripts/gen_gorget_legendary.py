#!/usr/bin/env python3
"""Generate a FIFTH net-new-geometry chest showcase per class — a standing
high-collar GORGET that rises UP-and-OUTWARD from the NECK, framing the throat
from either side. This is a NEW silhouette AXIS distinct from all four existing
chest geometries:

  * "winged"   chests flare UP at the BACK (wings rising behind the shoulders).
  * "pauldron" chests spike UP at the two top SHOULDER CORNERS (outer mass).
  * "cape"     chests drape down and flare OUTWARD at the two SIDE edges.
  * "tabard"   chests hang a single centred panel straight DOWN the front.
  * this GORGET adds mass rising UP at the CENTRE-NECK: a pair of standing collar
    plates that peak just either side of the throat (offset ~2-4px from centre)
    and taper down toward the outer shoulders, leaving the front-centre throat
    open. Where the pauldron peaks at the OUTER corners, the gorget peaks NEAR
    the neck — up-back / up-shoulder / out-sides / down-centre / up-neck is the
    five-way silhouette contrast.

Authoring philosophy is identical to gen_tabard_legendary.py:
  * Body  = the class t4 chest silhouette (armor_chest_4 / shirt_mage4 /
    shirt_ranger4, + _f) recolored per-frame via luminance-quantile mapping onto
    a class-distinct 3-tone ramp — so every pose/animation is tracked and the
    source silhouette is preserved (0 px dropped by construction).
  * Accent = a standing collar drawn ONLY in the transparent space ABOVE the
    torso's own top rows. Each collar column is stacked directly above THAT
    column's own topmost opaque body pixel, so every collar pixel is 4-connected
    to the body by construction (each column chains straight down to its own
    shoulder). A per-frame connectivity guard clears any collar pixel not
    4-connected to the body mass, so accent strays are 0 by construction. The
    collar is clamped to y>=Y_MIN so it stays inside the QA head zone.

Per class (collar hue distinct from EVERY prior legendary chest so all five read
apart; the silhouette is the headline):
  * warrior "Sovereign's Gorget" — obsidian/steel body + bright SILVER-plate collar
  * mage    "Runeguard Gorget"   — arcane-violet body + AMBER-GOLD rune collar
  * ranger  "Warden's Gorget"    — forest body + VERDIGRIS-copper patina collar

Sleep frames (fi>=60, lying down) get the recolor only — no collar — matching the
winged / pauldron / cape / tabard convention. Shading applied in-script via
shade(); do NOT run sprite_shade.py again.

Run from repo root:
  python3 scripts/gen_gorget_legendary.py
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

# Gorget collar geometry.
COLLAR_H = 5      # max rows the collar rises above the shoulder (at the neck sides)
SPAN = 6          # half-width of the shoulder band the collar is built over
BAND = 4          # a column counts as "shoulder/neck top" if its top is within
                  #   ytop..ytop+BAND (so the collar tracks the sloped shoulder)
Y_MIN = 2         # keep collar inside the QA head zone

# ── Per-class palettes: body ramp (D/M/L) + collar ramp (TRIM, D, M, L) ─────────
# body:   deep shadow / base / highlight
# collar: TRIM (bright top rim + outer selvage) / D (fold shadow) /
#         M (mid plate) / L (lit plate)
CLASSES = {
    'warrior': dict(
        src='armor_chest_4', dst='shirt_warrior_legendary5',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),              # obsidian->steel
        collar=((240, 244, 250), (70, 78, 92), (150, 158, 172), (200, 208, 220)),  # bright silver plate
    ),
    'mage': dict(
        src='shirt_mage4', dst='shirt_mage_legendary5',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),              # arcane violet
        collar=((255, 236, 150), (96, 60, 16), (176, 120, 36), (228, 176, 72)),    # amber-gold runes
    ),
    'ranger': dict(
        src='shirt_ranger4', dst='shirt_ranger_legendary5',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),                # forest green
        collar=((214, 232, 214), (20, 58, 52), (40, 110, 96), (96, 168, 148)),     # verdigris/patina copper
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


def collar_tone(o, dy, h, pal):
    """Pick a collar tone. pal = (TRIM, D, M, L). o = column offset from neck
    centre, dy = row height above the shoulder (1..h), h = this column's collar
    height. Top rim + outer plate edges read as bright TRIM; a fold shadow sits
    on the inner left plate; the rest alternate lit/mid plate."""
    TRIM, D, M, L = pal
    if dy == h:                 # bright top rim of the standing collar
        return TRIM
    if abs(o) >= 4:             # outer selvage edge
        return TRIM
    if o == -2:                 # fold shadow on the left neck plate
        return D
    return L if (dy % 2 == 0) else M


def neck_top_band(a):
    """Return (cx, ctop) where cx is the neck centre column and ctop maps each
    shoulder/neck-top column x -> its own topmost opaque body row. Columns whose
    top is well below the shoulder line (arms/hem) are excluded so the collar
    only grows from the neck/shoulder band."""
    rows = np.where(a.any(axis=1))[0]
    if rows.size == 0:
        return None, {}
    ytop = int(rows.min())
    txs = np.where(a[ytop])[0]
    if txs.size == 0:
        return None, {}
    cx = int(round((int(txs.min()) + int(txs.max())) / 2.0))
    ctop = {}
    for x in range(cx - SPAN, cx + SPAN + 1):
        if not (0 <= x < FW):
            continue
        col = np.where(a[:, x])[0]
        if col.size and int(col.min()) <= ytop + BAND:
            ctop[x] = int(col.min())
    return cx, ctop


def collar_height(o):
    """Standing-collar height profile: peaks just either side of the throat
    (|o|=2..3), open at the front-centre throat (|o|<=1 low), tapering down to
    the outer shoulders."""
    ao = abs(o)
    if ao <= 1:
        return 1                      # open throat at the front centre
    if ao <= 3:
        return COLLAR_H               # tall neck-side plates
    return max(1, COLLAR_H - (ao - 3))  # taper toward the outer shoulder


def draw_gorget(fr, a, pal):
    cx, ctop = neck_top_band(a)
    if cx is None or not ctop:
        return
    for x, cy in ctop.items():
        o = x - cx
        h = collar_height(o)
        for dy in range(1, h + 1):
            y = cy - dy
            if y < Y_MIN:
                break
            if a[y, x] or fr[y, x, 3] > 0:   # never overpaint body/existing
                continue
            put(fr, y, x, collar_tone(o, dy, h, pal))
        # outward curl on the tall neck-side plates: 1px beyond the edge at the
        # top rim, horizontally adjacent to this column's own top pixel so it
        # stays 4-connected.
        if 2 <= abs(o) <= 3:
            s = 1 if o > 0 else -1
            y = cy - h
            xf = x + s
            if Y_MIN <= y < FH and 0 <= xf < FW and not a[y, xf] and fr[y, xf, 3] == 0:
                put(fr, y, xf, pal[0])       # bright TRIM curl


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['collar']
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
        if fi >= 60:                          # sleep: body only
            continue
        draw_gorget(fr, a, pal)
        # Connectivity guard: drop any collar pixel not 4-connected to the body
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
    outdir = '_gorget_legendary_preview'
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
