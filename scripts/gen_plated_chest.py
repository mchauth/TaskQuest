#!/usr/bin/env python3
"""Plated-chest showcase v2 — steel body + a DEFINED, OUTLINED plate breastplate
and distinct pauldron discs (in the style of the pauldron/girdle/chainmail
legendaries, which sit crisp METAL pieces on top of a recolored body).

v1 was wrong: it recolored the whole body to leather and smeared a borderless gray
region that read as splotches. The leather was only Matt's *layering* reference
(like chainmail's silver over the body). This version:

  * BODY  = the class chest silhouette recolored to a steel ramp (the "shirt").
  * PLATE = a breastplate drawn as an explicit SHAPE with a hard dark OUTLINE, a
    scooped neckline, straight sides, a fauld bottom edge, gold collar+belt trim,
    and interior bevel (lit top, shadowed bottom). The outline is what makes it
    read as a separate raised object instead of a splotch.
  * PAULDRONS = distinct rounded steel DISCS at each shoulder, each with its own
    dark outline ring + gold rim + lit dome, drawn edge-connected to the body
    (one component -> QA-safe). Near (right) pauldron larger for the 3/4 view.

Painted onto opaque body pixels + edge-adjacent shoulder space only; no isolated
pixels. Plate/pauldrons located per-frame from the body bbox so they track poses.

Three plate VARIANTS for rarer-set variety:
  * v1 "Ironheart Cuirass"       — smooth plate + central domed boss
  * v2 "Warden's Muscled Cuirass" — anatomical sternum groove + pec ridges
  * v3 "Lamellar Warplate"       — three stacked, beveled lames

Sleep frames (fi>=60) get the steel recolor only. shade() applied in-script.

Run:  python3 scripts/gen_plated_chest.py
QA:   python3 scripts/sprite_qa.py _plated_chest_preview/shirt_warrior_plated1.png
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

# Steel body ramp (the shirt under the plate) — same obsidian->steel as the
# pauldron/girdle legendaries so the plate reads as metal-on-metal, not on cloth.
BODY = ((28, 30, 36), (74, 78, 90), (128, 134, 150))
# Plate palette.
OUTLINE = (10, 12, 16)
P_SHADOW = (58, 64, 78)
P_MID = (118, 126, 144)
P_LIT = (186, 196, 214)
P_HI = (230, 236, 248)
GOLD = (206, 158, 44)
GOLD_HI = (248, 222, 128)

# Plate vertical span (fraction of torso extent) and side insets from body edges.
PL_TOP, PL_BOT = 0.14, 0.66
INSET_L, INSET_R = 2, 1        # right (facing) inset smaller -> 3/4 asymmetry

VARIANTS = {
    1: dict(dst='shirt_warrior_plated1', kind='boss'),
    2: dict(dst='shirt_warrior_plated2', kind='muscle'),
    3: dict(dst='shirt_warrior_plated3', kind='lamellar'),
}
SRC = 'armor_chest_4'
# Rounded pauldron disc: dy (rows from shoulder top) -> outward reach in px.
PAULD_NEAR = {0: 2, 1: 3, 2: 3, 3: 2, 4: 1}
PAULD_FAR = {0: 1, 1: 2, 2: 2, 3: 1}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, ramp):
    D, M, L = ramp
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        put(fr, y, x, D if q < Q_LO else (L if q > Q_HI else M))


def plate_mask(a, ytop, ybot):
    """Boolean plate shape over the torso: scooped neckline at top, straight sides,
    fauld point at the bottom. Returns (mask, y0, y1, per-row [xl,xr])."""
    y0 = int(round(ytop + PL_TOP * (ybot - ytop)))
    y1 = int(round(ytop + PL_BOT * (ybot - ytop)))
    mask = np.zeros_like(a)
    rows = {}
    for y in range(y0, y1 + 1):
        rx = np.where(a[y])[0]
        if rx.size < 6:
            continue
        xl, xr = int(rx.min()) + INSET_L, int(rx.max()) - INSET_R
        rel = (y - y0) / max(1, (y1 - y0))
        # neckline scoop: top two rows pull in from the centre
        if y - y0 <= 1:
            cx = (xl + xr) // 2
            xl, xr = xl + 1, xr - 1
            if xr - xl < 3:
                continue
        # fauld: last row narrows to a central point
        if y == y1:
            cx = int(round(xl + (xr - xl) * 0.55))
            xl, xr = cx - 2, cx + 2
        if xr - xl < 2:
            continue
        for x in range(xl, xr + 1):
            if a[y, x]:
                mask[y, x] = True
        rows[y] = (xl, xr)
    return mask, y0, y1, rows


def draw_plate(fr, a, kind):
    ys, xs = np.where(a)
    if ys.size == 0:
        return
    ytop, ybot = int(ys.min()), int(ys.max())
    mask, y0, y1, rows = plate_mask(a, ytop, ybot)
    if not rows:
        return
    # 1) fill interior bevel — a breastplate lit FROM ABOVE: bright top ridge,
    #    mid upper body, progressively darker toward the bottom, dark side edges.
    for y, (xl, xr) in rows.items():
        ridge = int(round(xl + (xr - xl) * 0.58))
        rel = (y - y0) / max(1, (y1 - y0))
        for x in range(xl, xr + 1):
            if not mask[y, x]:
                continue
            if x == xl or x == xr:
                tone = P_SHADOW                # dark side edges define the curve
            elif rel < 0.16:
                tone = P_HI                    # bright top ridge (catches light)
            elif rel < 0.42:
                tone = P_LIT                   # lit upper chest
            elif rel > 0.82:
                tone = P_SHADOW                # shadowed lower plate
            elif rel > 0.62:
                tone = P_MID
            elif x == ridge and kind != 'muscle':
                tone = P_LIT                   # central ridge
            else:
                tone = P_MID
            put(fr, y, x, tone)
        # variant detailing
        if kind == 'muscle':
            if mask[y, ridge]:
                put(fr, y, ridge, P_SHADOW)               # sternum groove
            if rel < 0.55:
                sp = 2 + int(round(rel * 3))
                for xx in (ridge - sp, ridge + sp):
                    if xl < xx < xr and mask[y, xx]:
                        put(fr, y, xx, P_HI if rel < 0.3 else P_LIT)
        elif kind == 'lamellar':
            if abs(rel - 0.34) < 0.05 or abs(rel - 0.67) < 0.05:
                for x in range(xl, xr + 1):
                    if mask[y, x]:
                        put(fr, y, x, OUTLINE)             # groove between lames
            elif abs(rel - 0.44) < 0.05 or abs(rel - 0.77) < 0.05:
                for x in range(xl + 1, xr):
                    if mask[y, x]:
                        put(fr, y, x, P_LIT)               # lit lip of next lame
    # 2) central domed boss for Ironheart
    if kind == 'boss' and rows:
        ymid = (y0 + y1) // 2
        if ymid in rows:
            xl, xr = rows[ymid]
            cxr = int(round(xl + (xr - xl) * 0.58))
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    yy, xx = ymid + dy, cxr + dx
                    dist = (dy * dy + dx * dx) ** 0.5
                    if dist > 2.1 or not mask[yy, xx]:
                        continue
                    put(fr, yy, xx, P_HI if dist <= 0.8 else (OUTLINE if dist >= 1.6 else P_LIT))
    # 3) gold trim: collar line along the top edge, belt line along the fauld
    top_y = min(rows)
    xl, xr = rows[top_y]
    for x in range(xl, xr + 1):
        if mask[top_y, x]:
            put(fr, top_y, x, GOLD_HI if x in (xl, xr) else GOLD)
    belt_y = max(rows)
    xl, xr = rows[belt_y]
    for x in range(xl, xr + 1):
        if mask[belt_y, x]:
            put(fr, belt_y, x, GOLD)
    # 4) hard OUTLINE around the whole plate shape (this is what makes it read as a
    #    distinct raised object rather than a splotch)
    for y, (xl, xr) in rows.items():
        for x in range(xl, xr + 1):
            if not mask[y, x]:
                continue
            edge = False
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < FH and 0 <= nx < FW) or not mask[ny, nx]:
                    edge = True
                    break
            if edge and a[y, x]:
                # keep gold trim visible; only outline non-gold edge pixels
                cur = tuple(fr[y, x, :3])
                if cur not in (GOLD, GOLD_HI):
                    put(fr, y, x, OUTLINE)
    # 5) pauldrons — anchored to the true SHOULDER row (widest row of the upper
    #    torso), never the arms. NEAR (right/front) is a bold protruding disc; FAR
    #    (left/back) is flat — shading on the silhouette edge, no bulge — so the
    #    3/4 perspective reads correctly.
    sy = _shoulder_row(a, ytop, ybot)
    cx = int(np.median(xs))                 # stable torso centre (arm-independent)
    _pauldron_near(fr, a, sy, cx)
    _pauldron_far(fr, a, sy, cx)


def _shoulder_row(a, ytop, ybot):
    """Row of maximum torso width in the upper ~half — the shoulder line. Ignores a
    raised arm (thin) so the pauldron never lands on the arm."""
    ext = max(ybot - ytop, 1)
    best_y, best_w = ytop, -1
    for y in range(ytop, ytop + int(0.5 * ext) + 1):
        rx = np.where(a[y])[0]
        if rx.size:
            w = int(rx.max() - rx.min())
            if w > best_w:
                best_w, best_y = w, y
    return best_y


SHW = 6                                          # shoulder half-width from torso centre


def _pauldron_near(fr, a, sy, cx):
    """Bold domed disc on the near (right/front) shoulder: protrudes ~2px, outlined
    ring + gold rim + lit dome. The base column is clamped near the shoulder point
    (cx+SHW) so an extended/raised arm can't drag it out onto the arm."""
    for dy, reach in ((-1, 2), (0, 3), (1, 2)):
        y = sy + dy
        rx = np.where(a[y])[0]
        if rx.size == 0:
            continue
        # sit at the silhouette edge, but never further out than the shoulder point
        base_x = min(int(rx.max()), cx + SHW)
        for off in range(0, reach + 1):
            x = base_x + off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if off == reach:
                tone = OUTLINE                   # outer ring
            elif off == reach - 1:
                tone = GOLD                       # gold rim
            elif dy == -1 and off <= 1:
                tone = P_HI                       # lit dome crown
            else:
                tone = P_LIT if off <= 1 else P_MID
            put(fr, y, x, tone)


def _pauldron_far(fr, a, sy, cx):
    """Flat far (left/back) shoulder: a thin dark outline + a lit lip on the
    silhouette edge, clamped near the shoulder point (cx-SHW), protruding at most
    1px — reads as a smaller, receding pauldron in perspective."""
    for dy in (-1, 0, 1):
        y = sy + dy
        rx = np.where(a[y])[0]
        if rx.size == 0:
            continue
        xe = max(int(rx.min()), cx - SHW)
        if not (0 <= xe < FW):
            continue
        put(fr, y, xe, OUTLINE)
        if xe + 1 < FW and a[y, xe + 1]:
            put(fr, y, xe + 1, P_HI if dy == -1 else P_SHADOW)
        if dy == 0 and 0 <= xe - 1 < FW and a[y, xe - 1]:
            put(fr, y, xe - 1, OUTLINE)          # 1px hint only, and only on body


def build(base, kind):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a, BODY)
        if fi >= 60:
            continue
        draw_plate(fr, a, kind)
        # keep only components connected to the body (pauldrons are edge-connected)
        da = fr[..., 3] > 0
        lbl, _ = ndimage.label(da)
        body_labels = set(np.unique(lbl[a])) - {0}
        keep = np.isin(lbl, list(body_labels)) if body_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_plated_chest_preview'
    os.makedirs(outdir, exist_ok=True)
    for v, cfg in VARIANTS.items():
        for suffix in ('', '_f'):
            base = load('%s%s.png' % (SRC, suffix))
            arr = build(base, cfg['kind'])
            arr = shade(arr, adj_min=-0.14, adj_max=0.22)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-42s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
