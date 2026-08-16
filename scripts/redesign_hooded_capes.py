#!/usr/bin/env python3
"""Legendary hooded capes — v6 COMBINED: hood cap + cape in ONE shirt item.

Earlier versions split the design across two slots (cape in the shirt
PNG, deep-hood cap in a separate helmet PNG) so the cap could draw over
the hair. v6 folds the cap back into the shirt sprite as a single
combined item: the game stacks layers skin -> pants -> boots -> SHIRT ->
sword -> hair -> helmet (see index.html getCharLayers /
applyLegLayerOrder), so the hood cap pixels — drawn in the HEAD ZONE of
the shirt sheet (rows head_top-1 .. brim_row+8) — sit over the head/face
skin but UNDER the hair layer: the hair shows naturally on top of the
hood, which reads as a pushed-around-the-hair deep hood. One LOOT_TABLE
entry per class (shirt slot only); the helmet_*_legendary_cowl entries
are gone.

Draw order per frame (all into the one shirt frame):
  1. Cape back panel + trapezoid (hooded_cape_cells) — behind the body,
     skin-carved, brim_row down to y=55. No cape on sleep frames.
  2. Hood cap (cap_cells) — crown dome + asymmetric side drape at head
     height. NOT skin-carved (the hood covers the head skin); drawn on
     every frame the reference helmet_mage1.png is active (incl. sleep).
  3. Body recolor (recolor_body) — the dark robe/armor base, quantile-
     mapped T1 silhouette; overwrites any cap px that strays onto the
     garment so the chest edge stays crisp.

  Combined sheets (shirt slot), one per class:
    shirt_mage_legendary_hooded.png    hood + midnight robe + blue cape
    shirt_ranger_legendary_hooded.png  hood + forest armor + green cape

  Cape geometry (hooded_cape_cells): back panel cx+/-3 from brim_row
  (head_top+2) down behind the head/neck, flares to +/-4 at the
  shoulders, then the normal cape trapezoid half 5 -> 7 to the draped
  hem at y=55. Trim traces row min/max + hem; center highlight streaks.

  Hood geometry (cap_cells) — unchanged from v5:
    Crown: dome rows head_top-1..head_top+1 (half 4/4/4, exact skull
    width). Side panel rows brim_row..brim_row+8, dx spans per
    PANEL_SPAN — asymmetric for the 3/4 view (face on the RIGHT): only
    the right panel gets the deep oval drape + lining trim; the left is
    a 1px trailing lining edge. The oval face opening stays TRANSPARENT
    so the face (and hair, which draws above this layer anyway) shows
    through. Ranger: crown jags + leather stitch px. Black exterior
    outline everywhere except into the face opening.

  Sleep frames: body + hood only (house convention: no cape).

  Shading: ONE pass over the combined sheet — shade(adj_min=-0.20,
  adj_max=0.25), the shirt override. The hood fills are authored flat
  dark (midnight blue / forest green) and take their left-shadow /
  right-light modelling from that same pass; no separate
  sprite_shade.py run.

Run from repo root:
  python3 scripts/redesign_hooded_capes.py
Writes sheets to sprites/preview_assets/char/ (DO NOT push — review first)
and _PREVIEW_hooded_<cls>.png strips (skin + hair + combined shirt, frame 0
+ first frame of each anim at 4x) to the repo root.
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR, ROOT
from rebuild_class_hats import make_head_dome_fn
from legendary_capes import (FW, FH, COLS, NFR, CAPE_BOTTOM,
                             MID_RAMP, GRN_RAMP, MAGE_CAPE, RGR_CAPE,
                             put, recolor_body, stamp)

BLACK = (0, 0, 0)

# Hood palettes — DARK cloth, authored flat; the shirt shade() pass
# does the light modelling on the combined sheet.
#   crown  : cap/dome fill        panel : side-panel fill
#   lining : 1px trim tracing the inner edge of the face opening
#            (mage: silver thread; ranger: warm tan leather binding)
#   rim    : ranger leather stitch px
CAP_PAL = {
    'mage':   dict(crown=(40, 30, 100), panel=(35, 25, 85),
                   lining=(190, 185, 230), rim=(80, 60, 160)),
    'ranger': dict(crown=(45, 80, 35), panel=(38, 68, 28),
                   lining=(180, 140, 80), rim=(140, 105, 60)),
}


def hooded_cape_cells(cx, ht, nt, pal):
    """{(x, y): rgb} back panel + cape, one continuous silhouette.

    brim_row (ht+2) .. nt-3 : panel half 3 (behind the skull, +/-4 wide, so
                              invisible from the front — fabric down the back)
    nt-2 .. nt-1            : half 4 shoulder flare
    nt .. CAPE_BOTTOM       : cape trapezoid half 5 -> 7, draped hem
    """
    brim = ht + 2
    span = max(1, CAPE_BOTTOM - nt)
    cells = {}
    for y in range(brim, CAPE_BOTTOM + 1):
        if y < nt - 2:
            half = 3
        elif y < nt:
            half = 4
        else:
            t = (y - nt) / span
            half = int(round(5 + 2 * t))
        for dx in range(-half, half + 1):
            ybot = CAPE_BOTTOM - max(0, 3 - abs(dx))   # draped hem
            if y <= ybot:
                cells[(cx + dx, y)] = pal['base']
    # trim: row min/max x (one unbroken edge panel -> cape -> hem) + col bottoms
    rows, colbot = {}, {}
    for (x, y) in cells:
        rows.setdefault(y, []).append(x)
        colbot[x] = max(colbot.get(x, -1), y)
    for y, xs in rows.items():
        cells[(min(xs), y)] = pal['trim']
        cells[(max(xs), y)] = pal['trim']
    for x, y in colbot.items():
        cells[(x, y)] = pal['trim']
    # subtle center highlight streaks on the cape body
    for (x, y) in list(cells):
        if abs(x - cx) <= 1 and y > nt + 2 and (y - nt) % 5 == 2 \
                and cells[(x, y)] == pal['base']:
            cells[(x, y)] = pal['hi']
    return cells


# RIGHT-side panel (inner, outer) dx extents per row below brim_row.
# The character is drawn at a 3/4 angle facing RIGHT (the face sits on
# the right half of the head silhouette). So only the RIGHT panel
# (positive dx = front of the face) gets the deep drape: outer edge
# tapers 6 -> 7 -> 8 (fabric drapes wider as it falls) then pulls back
# in 7 -> 6 toward the chin. The inner edge is 5 through the mid-face
# rows (widest part of the oval) but pulls IN at both ends — 4 on the
# top (brim) row and 1 on the chin row — so the opening's corners
# round into an oval/arch instead of a rectangle. The LEFT side
# (negative dx = back/side of the head) is just a thin trailing edge:
# 1px of lining at dx=-5 for LEFT_EDGE_ROWS rows, then nothing.
PANEL_SPAN = ((4, 6), (5, 7), (5, 8), (5, 8),
              (5, 7), (5, 7), (5, 6), (5, 6), (1, 6))
LEFT_EDGE_ROWS = 1           # rows of the 1px back-edge below the brim


def cap_cells(cx, ht, pal, rugged=False, back_mask=False):
    """{(x, y): rgb} deep hood, drawn into the shirt sheet's head zone.

    Crown rows (offsets from head_top=ht) — filled full-width, covers the
    head skin (hair draws on a HIGHER layer and shows on top):
      ht-1 : half 4   flat crown top at skull width (slim: no dome row
                      above the head, no side overhang)
      ht   : half 4   skull width
      ht+1 : half 4   (|dx| <= 4 of this row is the trim's top edge)
    Side panels (brim = ht+2, the first full-width skull row) — the
    hood is ASYMMETRIC to match the 3/4 view (face on the RIGHT):
      RIGHT (front of the face), brim+i, i=0..8: dx = +PANEL_SPAN[i]
      spans. Deep drape: the panel runs all the way to chin level,
      outer edge 6->8->6, inner edge 5 through the mid-face rows but
      pulled in to 4 on the brim row and 1 on the chin row, curving
      around the face in a deep oval with rounded corners.
      LEFT (back/side of the head): only a 1px lining edge at dx=-5
      for the first LEFT_EDGE_ROWS rows — the thin trailing edge of
      the hood seen from behind — plus a corner px at dx=-4 on the
      brim row so the opening's top-left corner rounds in too.
    Face-opening trim: a 1px 'lining' border traces the inner edge of
    the opening — the |dx| <= 4 span of crown row ht+1 (top edge) plus
    the innermost column of every right panel row (front curve, down
    to the chin corner px) plus the 1px left back-edge column.
    Face opening: everything left of the right panel's inner edge
    (x - cx < PANEL_SPAN[i][0]) from brim down is NEVER touched
    except that 1px back edge — transparent, so the face shows through.
    Fills are FLAT dark cloth (crown / panel / lining); the shirt
    shade() pass on the combined sheet does the light modelling.
    """
    crown, panel = pal['crown'], pal['panel']
    rim, lining = pal['rim'], pal['lining']
    brim = ht + 2
    fill, over = {}, {}
    # ── crown dome: covers the head skin, full width ──
    crown_rows = [(ht - 1, 4), (ht, 4), (ht + 1, 4)]
    if back_mask:
        # helmet variant: 1 extra crown row catches ponytail root px
        crown_rows.insert(0, (ht - 2, 4))
    for y, half in crown_rows:
        for dx in range(-half, half + 1):
            fill[(cx + dx, y)] = crown
    # trim, top edge: the crown pixels directly above the face opening
    for dx in range(-4, 5):
        fill[(cx + dx, ht + 1)] = lining
    # ── RIGHT panel: fabric framing the front of the face, to the chin ──
    for i, (inner, outer) in enumerate(PANEL_SPAN):
        y = brim + i
        for adx in range(inner, outer + 1):
            if adx == inner:                       # trim: inner opening edge
                fill[(cx + adx, y)] = lining
            else:                                  # panel fill (flat)
                fill[(cx + adx, y)] = panel
    # ── LEFT: back/side of the head ──
    if back_mask:
        # HELMET variant: opaque back-of-hood panel, dx -7..-3, from
        # head_top-1 down to brim+6. In-game the hair layer is masked
        # by the helmet's opaque px (hatType 'partial'), so this zone
        # blocks ponytail/long/medium hair flowing behind the head —
        # it reads as the back of the hood fabric. setdefault keeps
        # the crown/lining px where the zone overlaps the crown rows.
        for y in range(ht - 1, brim + 7):
            for dx in range(-7, -2):
                fill.setdefault((cx + dx, y), panel)
    else:
        # shirt variant (hair draws on top anyway): just the hood's
        # thin trailing edge, 1px of lining, then nothing
        for i in range(LEFT_EDGE_ROWS):
            fill[(cx - 5, brim + i)] = lining
        # top-left corner of the opening curves in: 1px at dx=-4 on
        # the brim row (mirrors the right panel's inner=4 top row)
        fill[(cx - 4, brim)] = lining
    if rugged:                                     # ranger: jags + stitches
        fill.pop((cx + 4, ht - 1), None)           # torn crown edge
        fill.pop((cx + 8, brim + 3), None)         # torn outer edge, right
        over[(cx + 2, ht)] = rim
        over[(cx - 3, ht - 1)] = rim
        over[(cx + 7, brim + 4)] = rim             # leather stitch px
    # exterior black outline — everywhere EXCEPT into the face opening
    # and the open left/back side (everything left of the right
    # panel's inner edge on panel rows stays transparent: the 1px back
    # edge floats there un-outlined)
    def in_opening(x, y):
        i = y - brim
        if 0 <= i < len(PANEL_SPAN):
            if back_mask and x - cx <= -3:
                return False               # back-mask zone: outline it
            return x - cx < PANEL_SPAN[i][0]
        return False
    px = {}
    for (x, y) in set(fill):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if n in fill:
                continue
            if in_opening(*n):
                continue                           # face opening: keep open
            px[n] = BLACK
    px.update(fill)
    px.update(over)
    return px


def build_shirt(base, skin_sheet, dome, ramp, pal, cap_pal, rugged,
                hat_frames):
    """Combined sheet: cape (1st) + hood cap (2nd) + body recolor (3rd)."""
    out = np.zeros_like(base)
    skin_alpha = skin_sheet[..., 3] > 0
    hat_frames = set(hat_frames)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        ys, xs = np.where(a)
        hp = dome(fi)
        cx = hp[1] if hp else (int(xs.min()) + int(xs.max())) // 2
        ht = hp[0] if hp else int(ys.min()) - 11
        top = {int(x): int(ys[xs == x].min()) for x in np.unique(xs)}
        tops = [top[x] for x in range(cx - 3, cx + 4) if x in top]
        nt = min(tops) if tops else int(ys.min())
        hide = skin_alpha[sl] & ~a                 # visible skin carves fabric
        # 1. cape back panel + trapezoid (behind everything; not on sleep)
        if fi < 60:
            stamp(fr, hooded_cape_cells(cx, ht, nt, pal),
                  hide, a, pal['outline'])
        # 2. hood cap in the head zone — over the cape and the head skin
        #    (no skin carve: the hood covers the head), all hat frames
        if fi in hat_frames and hp is not None:
            for (x, y), rgb in cap_cells(cx, ht, cap_pal, rugged).items():
                put(fr, y, x, rgb)
        # 3. body recolor on top: crisp chest edge over any stray cap px
        recolor_body(fr, src, a, ramp)
    return out


def get_active_frames(path):
    a = np.array(Image.open(path).convert('RGBA'))
    return [fi for fi in range(NFR)
            if (a[(fi // COLS) * FH:(fi // COLS + 1) * FH,
                  (fi % COLS) * FW:(fi % COLS + 1) * FW, 3] > 0).any()]


def preview(layer_sheets, base, path, zoom=3, gap=4):
    """Frame-0 + first active frame of each anim row, layers bottom->top."""
    frames = []
    for row in range(6):                           # idle..slash (no sleep)
        for fi in range(row * COLS, (row + 1) * COLS):
            r, c = fi // COLS, fi % COLS
            sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
            if (base[sl][..., 3] > 0).any():
                frames.append(fi)
                break
    bg = np.zeros((FH, len(frames) * (FW + gap) - gap, 4), dtype=np.uint8)
    bg[..., :3] = (40, 40, 48)
    bg[..., 3] = 255
    for i, fi in enumerate(frames):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        tile = bg[:, i * (FW + gap):i * (FW + gap) + FW]
        for sheet in layer_sheets:
            m = sheet[sl][..., 3] > 0
            tile[m] = sheet[sl][m]
    big = np.kron(bg, np.ones((zoom, zoom, 1), dtype=np.uint8))
    Image.fromarray(big).save(path)
    return frames


JOBS = [
    ('mage', 'shirt_mage1.png', MID_RAMP, MAGE_CAPE, False),
    ('ranger', 'shirt_ranger1.png', GRN_RAMP, RGR_CAPE, True),
]


def main():
    skin_sheet = load('skin_m1.png')
    hair_sheet = load('hair_m1.png')
    dome = make_head_dome_fn(skin_sheet)
    hat_frames = get_active_frames(CHAR + 'helmet_mage1.png')
    for cls, src_name, ramp, pal, rugged in JOBS:
        base = load(src_name)
        shirt = build_shirt(base, skin_sheet, dome, ramp, pal,
                            CAP_PAL[cls], rugged, hat_frames)
        shirt = shade(shirt, adj_min=-0.20, adj_max=0.25)
        shirt_name = 'shirt_%s_legendary_hooded.png' % cls
        Image.fromarray(shirt).save(CHAR + shirt_name)

        # preview: skin + hair + combined shirt (hair over the hood crown,
        # exactly the in-game layer order — no helmet layer)
        pv = os.path.join(ROOT, '_PREVIEW_hooded_%s.png' % cls)
        frames = preview([skin_sheet, shirt, hair_sheet], base, pv, zoom=4)
        print('wrote %s, preview frames %s' % (shirt_name, frames))


if __name__ == '__main__':
    main()
