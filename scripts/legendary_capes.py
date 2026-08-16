#!/usr/bin/env python3
"""Generate legendary cape/hood chest options (male) — 6 preview sheets.

  shirt_warrior_legendary_cape         gold plate + crimson cape
  shirt_warrior_legendary_winged_cape  gold plate + seraph wings + crimson cape
  shirt_mage_legendary_cape            midnight robe + blue cape, tall collar, rune
  shirt_mage_legendary_hooded          midnight robe + pushed-back hood
  shirt_ranger_legendary_hooded        forest armor + green cloak + rugged hood
  shirt_ranger_legendary_cape          forest armor + green cloak

Built the legendary_armor_t1.py way:

  Body    : class T1 silhouette (shirt_rare1 / shirt_mage1 / shirt_ranger1)
            luminance-QUANTILE mapped onto a 6-step class ramp (gold /
            midnight blue around (20,15,60) / forest green around (40,80,30)).
            Source-black silhouette-edge px stay pure black outline.
  Cape    : trapezoid drawn BEHIND everything (first in draw order), anchored
            per frame on the skull-dome cx + garment neck_top (min top alpha
            over cx±3). Rows neck_top..~55, half-width 5 -> 7 (widest ~15px at
            the hem), hem drapes: center 3 columns ride 3..1 px higher so the
            outer corners hang lowest. Row min/max + per-column bottom px get
            the trim color; center columns get a dim highlight streak every
            5th row. Cape px are HIDDEN wherever the skin sheet is visible
            and not covered by the garment (skin & ~garment) — that carve-out
            is what makes the cape read as behind the body/legs instead of a
            robe over them. 1px exterior outline in a dark cape tone on truly
            empty neighbors grounds the edge (same trick as the wing OL).
  Wings   : (winged_cape only) wing_pixels imported from legendary_armor_t1,
            drawn OVER the cape, UNDER the plate; pauldron caps over the
            shoulders, identical to shirt_warrior_legendary1.
  Collar  : (mage cape) two raised triangular points per side, rows
            neck_top-5..neck_top-1. Spec anchor is cx±3, but the skull spans
            x=cx-4..cx+4 on idle frames, so cx±3 is entirely hidden behind
            the head by the skin carve-out; the points are widened to span
            cx±3..cx±5 with the tip column at cx±5 so the collar visibly
            frames the head from behind. Outer column = silver edge, tip px =
            accent-frozen glint (235,235,250).
  Hood    : rounded dome ring, y = head_top-2 .. neck_top+2, x = cx±7.
            Elliptic top half, straight sides below, drawn AFTER the body so
            the bottom rows drape onto the garment shoulders — but skin-
            carved like the cape, so it never covers the face: it shows as a
            2-3px ring around/above the head (pushed-back hood). Bottom px of
            every hood column = 1px rim highlight. Mage: fabric (30,22,80),
            silver rim (170,170,210), face-adjacent px lightened. Ranger:
            darker green fabric, brown leather rim (100,65,30), jagged
            notches on the outer edge + leather stitch px = rugged look.
  Cowl    : (hooded variants) hood + cape as ONE continuous garment — a
            monk's-robe cowl. Single silhouette from head_top-2 down to
            y=55, drawn in the cape slot (behind the body, skin-carved):
            rounded crown above the head (half 4 -> 6), straight fabric
            walls framing the head at |dx| 5..7 (face opening |dx|<=4 stays
            transparent, inner edge px lightened as lining), a 1px flare to
            half 8 at the neck, then a solid half-8 cape from the shoulders
            to the draped hem. Trim color traces the row min/max of every
            row, so one unbroken edge line runs crown -> hood side -> cape
            side -> hem: no seam. Same fill color top to bottom.
  Rune    : (mage cape) dim silver cross on the cape's lower-right lobe
            (cx+4..cx+6 ~ y=neck_top+17) — the only lower cape region not
            carved away by the legs on idle frames.
  Sleep   : frames fi >= 60 get the recolored body only (character lies
            down — no cape/wings/hood/collar, house convention).
  Shading : shade(adj_min=-0.20, adj_max=0.25) — the shirt override. Trim /
            rim colors take the cosine light (grounds them); deliberate
            glints pass sprite_shade's accent test (r>=230 & g>=190) and
            stay frozen. Do NOT run sprite_shade.py again on top.

Run from repo root:
  python3 scripts/legendary_capes.py
Writes sheets to sprites/preview_assets/char/ (DO NOT push — review first)
and _PREVIEW_<name>.png strips (frame 0 + idle/walk/run/jump/cheer/slash at
3x, composited over skin_m1 on a dark backdrop) to the repo root.
"""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR, ROOT
from rebuild_class_hats import make_head_dome_fn
from legendary_armor_t1 import (RAMP as GOLD_RAMP, wing_pixels, edge_mask,
                                OL as WING_OL, L as GOLD_L, M as GOLD_M,
                                FE as WING_FE)

FW, FH, COLS, NFR = 80, 64, 10, 70
CAPE_BOTTOM = 55                     # lowest cape row (outer corners)

# 6-step body ramps, dark -> light (GOLD_RAMP imported for warrior)
MID_RAMP = np.array([                # midnight blue around (20,15,60)
    (6, 4, 22), (12, 9, 40), (20, 15, 60),
    (32, 26, 88), (48, 40, 120), (70, 60, 158),
], dtype=np.uint8)
GRN_RAMP = np.array([                # forest green around (40,80,30)
    (10, 20, 8), (22, 44, 16), (40, 80, 30),
    (58, 106, 44), (80, 136, 60), (106, 168, 82),
], dtype=np.uint8)

# cape palettes
WAR_CAPE = dict(base=(160, 20, 20), hi=(200, 50, 50),
                trim=(200, 160, 40), outline=(60, 8, 8))
MAGE_CAPE = dict(base=(24, 18, 70), hi=(40, 32, 100),
                 trim=(180, 180, 220), outline=(8, 6, 26))
RGR_CAPE = dict(base=(30, 60, 22), hi=(42, 82, 32),
                trim=(100, 65, 30), outline=(10, 20, 8))

# hood palettes
MAGE_HOOD = dict(fill=(30, 22, 80), face=(44, 34, 104),
                 rim=(170, 170, 210), outline=(8, 6, 26),
                 rugged=False, peak=True)
RGR_HOOD = dict(fill=(34, 66, 26), face=(52, 92, 40),
                rim=(100, 65, 30), outline=(10, 20, 8),
                rugged=True, peak=True)

# one-piece cowl palettes (hood + cape = same cloth)
MAGE_COWL = dict(fill=(24, 18, 70), face=(44, 34, 104), hi=(40, 32, 100),
                 rim=(180, 180, 220), outline=(8, 6, 26),
                 rugged=False, peak=True)
RGR_COWL = dict(fill=(30, 60, 22), face=(52, 92, 40), hi=(42, 82, 32),
                rim=(100, 65, 30), outline=(10, 20, 8),
                rugged=True, peak=True)

COLLAR_BLUE = (24, 18, 70)           # tall collar body (matches cape)
COLLAR_EDGE = (180, 180, 220)        # silver edge column
COLLAR_TIP = (235, 235, 250)         # accent-frozen tip glint
RUNE = (150, 150, 190)               # dim silver arcane rune


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor_body(fr, src, a, ramp):
    """Quantile-map the source garment onto a 6-step ramp (edges stay black)."""
    src_black = a & (src[..., :3].astype(np.int32).sum(-1) < 90)
    edges = edge_mask(a) & src_black
    interior = a & ~edges
    if interior.any():
        rgbf = src[..., :3].astype(np.float64)
        lu = (3 * rgbf[..., 0] + 6 * rgbf[..., 1] + rgbf[..., 2]) / 10.0
        src_l = lu[interior]
        ref = np.sort(src_l)
        q = np.searchsorted(ref, src_l, side='left') / max(1, len(ref) - 1)
        idx = np.clip((q * (len(ramp) - 1)).round().astype(int),
                      0, len(ramp) - 1)
        fr[interior, :3] = ramp[idx]
        fr[interior, 3] = 255
    fr[edges, :3] = 0
    fr[edges, 3] = 255


def cape_cells(cx, nt, pal, rune=False):
    """{(x, y): rgb} for the cape trapezoid (before the skin carve-out)."""
    span = max(1, CAPE_BOTTOM - nt)
    cells = {}
    for y in range(nt, CAPE_BOTTOM + 1):
        t = (y - nt) / span
        half = int(round(5 + 2 * t))            # 5 at shoulders -> 7 at hem
        for dx in range(-half, half + 1):
            ybot = CAPE_BOTTOM - max(0, 3 - abs(dx))   # draped hem
            if y <= ybot:
                cells[(cx + dx, y)] = pal['base']
    # trim: row min/max x + per-column bottom px
    rows, colbot = {}, {}
    for (x, y) in cells:
        rows.setdefault(y, []).append(x)
        colbot[x] = max(colbot.get(x, -1), y)
    for y, xs in rows.items():
        cells[(min(xs), y)] = pal['trim']
        cells[(max(xs), y)] = pal['trim']
    for x, y in colbot.items():
        cells[(x, y)] = pal['trim']
    # subtle center highlight streaks
    for (x, y) in list(cells):
        if abs(x - cx) <= 1 and y > nt + 2 and (y - nt) % 5 == 2 \
                and cells[(x, y)] == pal['base']:
            cells[(x, y)] = pal['hi']
    if rune:                                    # cross on the lower-right lobe
        yc = nt + 17
        for (dx, dy) in ((5, -1), (4, 0), (5, 0), (6, 0), (5, 1)):
            p = (cx + dx, yc + dy)
            if p in cells:
                cells[p] = RUNE
    return cells


def hood_cells(cx, ht, nt, pal):
    """{(x, y): rgb} for the pushed-back hood dome (before carve-out)."""
    y_top, y_bot = ht - 2, nt + 2
    rx = 6                                      # apex/side width
    yc = y_top + max(4, (y_bot - y_top) // 2)   # dome apex band
    cells = {}
    for y in range(y_top, y_bot + 1):
        if y < yc:                              # elliptic top
            f = (yc - y) / max(1.0, (yc - y_top) + 0.5)
            half = int(round(rx * math.sqrt(max(0.0, 1.0 - f * f))))
            half = max(2, half)
        else:                                   # cowl flare toward shoulders
            t = (y - yc) / max(1.0, y_bot - yc)
            half = rx + int(round(2 * t))       # 6 -> 8 draped silhouette
        for dx in range(-half, half + 1):
            cells[(cx + dx, y)] = pal['fill']
    if pal.get('peak'):                         # small wizardly point on top
        for x, y in ((cx - 1, y_top - 1), (cx, y_top - 1), (cx + 1, y_top - 1),
                     (cx, y_top - 2)):
            cells[(x, y)] = pal['fill']
    if pal['rugged']:                           # jagged outer edge (lower half
        rows = {}                               # only — jags at head height
        for (x, y) in cells:                    # read as hair strands)
            rows.setdefault(y, []).append(x)
        for y, xs in rows.items():
            if yc <= y < nt and y % 3 == 0:
                cells.pop((min(xs), y), None)
            elif yc <= y < nt and y % 3 == 1:
                cells.pop((max(xs), y), None)
        # leather stitch px above the brow
        for p in ((cx - 3, y_top + 1), (cx + 2, y_top + 2)):
            if p in cells:
                cells[p] = pal['rim']
    # 1px rim highlight along the bottom curve (per-column bottom px)
    colbot = {}
    for (x, y) in cells:
        colbot[x] = max(colbot.get(x, -1), y)
    for x, y in colbot.items():
        cells[(x, y)] = pal['rim']
    return cells


def cowl_cells(cx, ht, nt, pal):
    """{(x, y): rgb} for the one-piece cowl: hood + cape, one silhouette.

    Rows head_top-2 .. CAPE_BOTTOM. Head region is an open ring (face at
    |dx|<=4 left transparent); at the neck the sides flare 7 -> 8 and the
    row goes solid, so the hood fabric flows straight into the cape with
    no seam. Same fill everywhere — it is all one piece of cloth.
    """
    y_top = ht - 2
    cells = {}
    for y in range(y_top, CAPE_BOTTOM + 1):
        if y < nt:                              # hood region (face open)
            if y == y_top:
                outer, inner = 4, 0             # rounded crown
            elif y == y_top + 1:
                outer, inner = 6, 0
            elif y >= nt - 2:
                outer, inner = 8, 5             # neck flare into the cape
            else:
                outer, inner = 7, 5             # fabric walls framing head
        else:                                   # cape region: solid width
            outer, inner = 8, 0
        for dx in range(-outer, outer + 1):
            if inner and abs(dx) < inner:
                continue                        # face opening stays open
            ybot = CAPE_BOTTOM - max(0, 3 - abs(dx))   # draped hem
            if y <= ybot:
                cells[(cx + dx, y)] = pal['fill']
    if pal.get('peak'):                         # small point on the crown
        for x, y in ((cx - 1, y_top - 1), (cx, y_top - 1), (cx + 1, y_top - 1),
                     (cx, y_top - 2)):
            cells[(x, y)] = pal['fill']
    # inner lining around the face opening (lighter fill)
    for y in range(y_top + 2, nt):
        for sgn in (1, -1):
            if (cx + sgn * 5, y) in cells and (cx + sgn * 4, y) not in cells:
                cells[(cx + sgn * 5, y)] = pal['face']
    if pal['rugged']:                           # jagged outer edge + stitches
        rows = {}
        for (x, y) in cells:
            rows.setdefault(y, []).append(x)
        for y in range(y_top + 2, nt - 2):
            xs = rows.get(y)
            if not xs:
                continue
            if y % 3 == 0:
                cells.pop((min(xs), y), None)
            elif y % 3 == 1:
                cells.pop((max(xs), y), None)
        for p in ((cx - 3, y_top + 1), (cx + 2, y_top + 2)):
            if p in cells:
                cells[p] = pal['rim']
    # continuous trim: row min/max x (crown -> hood side -> cape side, one
    # unbroken line) + per-column bottom px along the draped hem
    rows, colbot = {}, {}
    for (x, y) in cells:
        rows.setdefault(y, []).append(x)
        colbot[x] = max(colbot.get(x, -1), y)
    for y, xs in rows.items():
        cells[(min(xs), y)] = pal['rim']
        cells[(max(xs), y)] = pal['rim']
    for x, y in colbot.items():
        cells[(x, y)] = pal['rim']
    # subtle center highlight streaks on the cape body
    for (x, y) in list(cells):
        if abs(x - cx) <= 1 and y > nt + 2 and (y - nt) % 5 == 2 \
                and cells[(x, y)] == pal['fill']:
            cells[(x, y)] = pal['hi']
    return cells


def collar_cells(cx, nt):
    """Tall mage collar: two raised triangular points framing the head."""
    cells = {}
    for sgn in (1, -1):
        pts = [(3, -1), (4, -1), (5, -1),       # base row
               (4, -2), (5, -2),
               (4, -3), (5, -3),
               (5, -4),
               (5, -5)]                          # tip
        for dx, dy in pts:
            x, y = cx + sgn * dx, nt + dy
            if dx == 5:
                cells[(x, y)] = COLLAR_TIP if dy == -5 else COLLAR_EDGE
            else:
                cells[(x, y)] = COLLAR_BLUE
    return cells


def stamp(fr, cells, hide, a, outline):
    """Draw cells (skipping visible-skin px), then a 1px exterior outline."""
    drawn = set()
    for (x, y), rgb in cells.items():
        if 0 <= x < FW and 0 <= y < FH and not hide[y, x]:
            put(fr, y, x, rgb)
            drawn.add((x, y))
    if outline is None:
        return drawn
    for (x, y) in drawn:
        for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + ddx, y + ddy
            if (nx, ny) in cells or not (0 <= nx < FW and 0 <= ny < FH):
                continue
            if fr[ny, nx, 3] == 0 and not hide[ny, nx] and not a[ny, nx]:
                put(fr, ny, nx, outline)
    return drawn


def build(base, skin_sheet, dome, ramp, cape=None, wings=False,
          hood=None, collar=False, rune=False, cowl=None):
    out = np.zeros_like(base)
    skin_alpha = skin_sheet[..., 3] > 0
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        sleeping = fi >= 60

        # frame geometry
        ys, xs = np.where(a)
        hp = dome(fi)                            # (head_top, cx) or None
        cx = hp[1] if hp else (int(xs.min()) + int(xs.max())) // 2
        ht = hp[0] if hp else int(ys.min()) - 11
        cols = np.unique(xs)
        top = {int(x): int(ys[xs == x].min()) for x in cols}
        tops = [top[x] for x in range(cx - 3, cx + 4) if x in top]
        nt = min(tops) if tops else int(ys.min())
        hide = skin_alpha[sl] & ~a               # visible skin carves deco out

        # 1. cape (bottom-most layer)
        if cape is not None and not sleeping:
            stamp(fr, cape_cells(cx, nt, cape, rune=rune),
                  hide, a, cape['outline'])

        # 1b. one-piece cowl (hood + cape, same layer & cloth)
        if cowl is not None and not sleeping:
            stamp(fr, cowl_cells(cx, ht, nt, cowl),
                  hide, a, cowl['outline'])

        # 2. wings over the cape, under the plate
        if wings and not sleeping:
            wpx = wing_pixels(cx, nt - 8)
            for (x, y), rgb in wpx.items():
                put(fr, y, x, rgb)
            for (x, y) in wpx:
                for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    n = (x + ddx, y + ddy)
                    if n not in wpx and 0 <= n[0] < FW and 0 <= n[1] < FH \
                            and fr[n[1], n[0], 3] == 0:
                        put(fr, n[1], n[0], WING_OL)

        # 3. body recolor over everything so far
        recolor_body(fr, src, a, ramp)

        # 4. pauldron wing-root caps (winged variant)
        if wings and not sleeping:
            for sgn in (1, -1):
                for dx, dy, col in ((3, 0, GOLD_L), (4, 0, GOLD_L),
                                    (5, 0, WING_FE), (3, 1, GOLD_M),
                                    (4, 1, GOLD_L), (5, 1, GOLD_M)):
                    x, y = cx + sgn * dx, nt + dy
                    if 0 <= x < FW and 0 <= y < FH and a[y, x]:
                        put(fr, y, x, col)

        # 5. hood ring around the head (over the body, skin-carved)
        if hood is not None and not sleeping and hp:
            hc = hood_cells(cx, ht, nt, hood)
            drawn = stamp(fr, hc, hide, a, hood['outline'])
            # lighten the face-opening edge (hood px touching visible skin)
            for (x, y) in drawn:
                if hc[(x, y)] != hood['fill']:
                    continue
                for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + ddx, y + ddy
                    if 0 <= nx < FW and 0 <= ny < FH and hide[ny, nx]:
                        put(fr, y, x, hood['face'])
                        break

        # 6. tall collar points (over the body, skin-carved)
        if collar and not sleeping and hp:
            stamp(fr, collar_cells(cx, nt), hide, a, None)
    return out


def preview(sheet, skin_sheet, base, path, zoom=3, gap=4):
    """Frame-0 + first active frame of each animation row, 3x, over skin."""
    frames = []
    for row in range(6):                         # idle..slash (no sleep)
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
        for layer in (skin_sheet[sl], sheet[sl]):
            m = layer[..., 3] > 0
            tile[m] = layer[m]
    big = np.kron(bg, np.ones((zoom, zoom, 1), dtype=np.uint8))
    Image.fromarray(big).save(path)
    return frames


JOBS = [
    ('shirt_warrior_legendary_cape', 'shirt_rare1.png', GOLD_RAMP,
     dict(cape=WAR_CAPE)),
    ('shirt_warrior_legendary_winged_cape', 'shirt_rare1.png', GOLD_RAMP,
     dict(cape=WAR_CAPE, wings=True)),
    ('shirt_mage_legendary_cape', 'shirt_mage1.png', MID_RAMP,
     dict(cape=MAGE_CAPE, collar=True, rune=True)),
    ('shirt_mage_legendary_hooded', 'shirt_mage1.png', MID_RAMP,
     dict(cowl=MAGE_COWL)),
    ('shirt_ranger_legendary_hooded', 'shirt_ranger1.png', GRN_RAMP,
     dict(cowl=RGR_COWL)),
    ('shirt_ranger_legendary_cape', 'shirt_ranger1.png', GRN_RAMP,
     dict(cape=RGR_CAPE)),
]


def main():
    only = set(sys.argv[1:])                     # optional: item names to run
    skin_sheet = load('skin_m1.png')
    dome = make_head_dome_fn(skin_sheet)
    for name, src_name, ramp, kw in JOBS:
        if only and name not in only:
            continue
        base = load(src_name)
        arr = build(base, skin_sheet, dome, ramp, **kw)
        arr = shade(arr, adj_min=-0.20, adj_max=0.25)
        Image.fromarray(arr).save(CHAR + name + '.png')
        n = sum(1 for fi in range(NFR)
                if (arr[(fi // COLS) * FH:(fi // COLS + 1) * FH,
                        (fi % COLS) * FW:(fi % COLS + 1) * FW, 3] > 0).any())
        pv = os.path.join(ROOT, '_PREVIEW_%s.png' % name)
        frames = preview(arr, skin_sheet, base, pv)
        print('wrote %s (%d active frames), preview frames %s' %
              (name + '.png', n, frames))


if __name__ == '__main__':
    main()
