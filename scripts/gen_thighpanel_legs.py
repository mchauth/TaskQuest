#!/usr/bin/env python3
"""ELEVENTH net-new-geometry LEGS showcase per class — a THIGH-PLATE PANEL: a
rectangular reinforcing plate riveted onto the front of each thigh (a flat
cuisse-plate patch). This brings the legs slot to ELEVEN distinct axes. It is the
rectangular-panel surface axis none of the ten existing legendary legs occupy:

  * legendary1 (tassets)     — short paired hip flaps.
  * legendary2 (war-kilt)    — a long cloth drape to a flared hem.
  * legendary3 (faulds)      — a stiff tiered plate skirt at the hip (silhouette).
  * legendary4 (poleyns)     — round knee discs (silhouette).
  * legendary5 (cuisses)     — a hip fin (silhouette).
  * legendary6 (loin-guard)  — a narrow vertical centre strap.
  * legendary7 (sword-belt)  — ONE diagonal band across the thighs.
  * legendary8 (side-stripe) — paired vertical bands, outer edge.
  * legendary9 (knee-band)   — one horizontal band at the knee.
  * legendary10 (cross-garter)— an X of crossed straps on the shin.
  * this THIGH-PLATE lays a solid RECTANGULAR plate panel (lit rim + corner rivets)
    on the upper front of each thigh — the enclosed-panel axis, distinct from every
    strip/band/stripe/X. A flat repaint that adds no silhouette pixels.

Authoring philosophy is identical to gen_crossgarter_legs.py: panel pixels are
painted ONLY onto pixels that are ALREADY opaque body pixels (`a`). Because it
never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe by construction.
Each frame's leg mass is labelled into CONNECTED COMPONENTS so a walk/run pose with
two separated legs gets its own panel per leg.

Sleep frames (fi>=60, lying down) get the recolor only — no panel. Shading applied
in-script via shade(); do NOT run sprite_shade.py again.

Per class the plate hue is the class accent family:
  * warrior "Warlord's Plated Cuisses" — obsidian/steel body + steel plate, gold rivets
  * mage    "Astral Sigil-Panels"      — arcane-violet body + silver plate, cyan rivets
  * ranger  "Warden's Bracer-Chausses" — forest body + tan-leather plate, copper rivets

Run from repo root:
  python3 scripts/gen_thighpanel_legs.py
Then QA:
  python3 scripts/sprite_qa.py _thighpanel_legs_preview/pants_warrior_legendary11.png --y-max 62
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

# Panel occupies the vertical span [PANEL_TOP, PANEL_BOT] of each leg component's
# bbox height, inset INSET cols from each side edge.
PANEL_TOP = 0.14
PANEL_BOT = 0.46
INSET = 1
MIN_PX = 10

# body : deep shadow / base / highlight
# panel: FIELD (plate body) / EDGE (lit top rim) / RIVET (bright corner rivet)
CLASSES = {
    'warrior': dict(
        src='armor_pants_4', dst='pants_warrior_legendary11',
        body=((28, 30, 36), (74, 78, 90), (128, 134, 150)),      # obsidian -> steel
        panel=((92, 98, 112), (168, 174, 190), (232, 190, 70)),  # steel plate, lit rim, gold rivets
    ),
    'mage': dict(
        src='pants_mage4', dst='pants_mage_legendary11',
        body=((20, 16, 54), (54, 42, 122), (120, 96, 200)),      # arcane violet
        panel=((120, 126, 150), (196, 202, 224), (72, 200, 244)),# silver plate, lit rim, cyan rivets
    ),
    'ranger': dict(
        src='pants_ranger4', dst='pants_ranger_legendary11',
        body=((20, 40, 18), (48, 88, 42), (98, 150, 82)),        # forest green
        panel=((110, 78, 42), (160, 120, 68), (206, 132, 66)),   # tan plate, lit rim, copper rivets
    ),
}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_panel(fr, comp, pal):
    """Paint a rectangular plate panel onto one leg component."""
    FIELD, EDGE, RIVET = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    h = max(y1 - y0, 1)
    ytop = y0 + PANEL_TOP * h
    ybot = y0 + PANEL_BOT * h
    xlo, xhi = x0 + INSET, x1 - INSET
    painted = []                             # actual panel pixels (all opaque)
    for y, x in zip(ys, xs):
        if ytop <= y <= ybot and xlo <= x <= xhi:
            put(fr, y, x, EDGE if abs(y - ytop) < 0.9 else FIELD)
            painted.append((y, x))
    # corner rivets: leftmost & rightmost pixel of the panel's top row (opaque)
    if painted:
        top_row = min(p[0] for p in painted)
        row_xs = [x for (y, x) in painted if y == top_row]
        put(fr, top_row, min(row_xs), RIVET)
        put(fr, top_row, max(row_xs), RIVET)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['panel']
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
        lbl, n = ndimage.label(a)
        for k in range(1, n + 1):
            draw_panel(fr, lbl == k, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_thighpanel_legs_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.20, adj_max=0.25)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-48s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
