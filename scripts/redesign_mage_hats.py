#!/usr/bin/env python3
"""Redesign mage wizard hats (helmet_mage1-6 + helmet_mage1_f) — v5 "folded back".

Changes vs v4:
  Placement : brim now sits at brim_row = the first row where the skull spans
              its full 9px width (head_top + 2), NOT at head_top. The lower
              brim + full droop staircase closes the transparent notches that
              used to appear between hair and hat at the brim edges
              (e.g. frame 40 (46,21), frame 40 (34,24)).
  Silhouette: fixed 10px cone for every tier, tip folded/curled to the RIGHT.
              Left edge roughly straight, right edge bulges then narrows —
              reads as slouchy fabric, not a geometric cone. Tip is 2px wide
              (no sharp point), ending 1-2px right of the centerline.
  Shading   : left face V*0.75, right face V*1.15; crease shadow V*0.65 along
              the fold line (leftmost px of rows dy=6..8); sheen V+0.12 on the
              upper-right (cx+3..cx+4, dy=3..5). sprite_shade.py then applies
              the global cosine light (PEAK=0.55, BELL_WIDTH=0.7) on top.
  Symbols   : one per tier at the lower-center front face (cx, brim_row-4) —
              t1 star, t2 cross, t3 crescent, t4 gold diamond outline,
              t5 yellow lightning bolt (Z-shape), t6 gold 4-pointed star.
              Clamped to cone fill. t4 anchors at cx+1 (cone center of
              mass shifts right with the fold); t5 and t6 use FINAL
              offsets from (cx, brim_row) with the lean baked in, plus a
              dark-purple 1px outline on cone-fill 4-neighbors.
  Flair     : t4/t6 tip star, t5 sparkles (kept inside the fill so every
              frame stays 4-connected), t6 gold rim on the drooped brim px.

Cone silhouette (offsets from cx; dy=0 is brim_row, dy=10 is the tip):
  dy= 0: -6..+6   brim base, 13px
  dy= 1: -5..+6   right side stays wide (bulge)
  dy= 2: -4..+6
  dy= 3: -4..+5
  dy= 4: -3..+4   start folding right
  dy= 5: -2..+4
  dy= 6: -1..+4   fold crease starts
  dy= 7:  0..+4
  dy= 8: +1..+3
  dy= 9: +1..+2
  dy=10: +1..+2   tip, 2px wide

Run from repo root, then:
  python3 scripts/sprite_shade.py sprites/preview_assets/char/helmet_mageN.png
  python3 scripts/sprite_qa.py sprites/preview_assets/char/helmet_mageN.png --y-min 2
"""
import os
import colorsys
import numpy as np
from PIL import Image

CH = "sprites/preview_assets/char"
W, H, COLS, NFR = 80, 64, 10, 70
HW = 9   # constant skull width
HC = 10  # cone height above brim (all tiers)

MAGE_HAT = {
    1: dict(D=(50, 25, 80),  M=(105, 43, 186), L=(131, 64, 212), A=(192, 192, 192)),
    2: dict(D=(60, 16, 102), M=(90, 24, 154),  L=(123, 47, 196), A=(192, 192, 192)),
    3: dict(D=(29, 17, 69),  M=(45, 27, 105),  L=(70, 48, 155),  A=(192, 192, 192)),
    4: dict(D=(16, 16, 62),  M=(26, 26, 94),   L=(46, 46, 143),  A=(255, 215, 0),
            S=(255, 240, 160), tip_star=True),
    5: dict(D=(8, 8, 28),    M=(13, 13, 43),   L=(58, 40, 110),  A=(255, 215, 0),
            S=(226, 226, 255), sparkles=True),
    6: dict(D=(5, 5, 16),    M=(10, 10, 26),   L=(93, 58, 150),  A=(240, 230, 140),
            S=(255, 240, 160), gold_rim=True, tip_star=True),
}

SILVER = (220, 220, 235)

# (left_off, right_off) from cx, indexed by dy above brim_row
SILHOUETTE = {
    0: (-6, 6), 1: (-5, 6), 2: (-4, 6), 3: (-4, 5), 4: (-3, 4),
    5: (-2, 4), 6: (-1, 4), 7: (0, 4), 8: (1, 3), 9: (1, 2), 10: (1, 2),
}


def scale_v(rgb, factor):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    v = min(1.0, max(0.0, v * factor))
    r2, g2, b2 = colorsys.hsv_to_rgb(h, s, v)
    return (int(round(r2 * 255)), int(round(g2 * 255)), int(round(b2 * 255)))


def add_v(rgb, delta):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    v = min(1.0, max(0.0, v + delta))
    r2, g2, b2 = colorsys.hsv_to_rgb(h, s, v)
    return (int(round(r2 * 255)), int(round(g2 * 255)), int(round(b2 * 255)))


# ── Skull-dome head tracking (same clustering as rebuild_class_hats.py) ──────

def runs_of(xs):
    out = []
    if not xs:
        return out
    s = p = xs[0]
    for x in xs[1:]:
        if x == p + 1:
            p = x
        else:
            out.append((s, p)); s = p = x
    out.append((s, p))
    return out


def make_head_metrics_fn(skin_arr):
    """Return fn(frame_idx) -> (head_top, cx, brim_row) or None.

    brim_row = first row at/below head_top where the skull spans the full
    HW=9 width around cx (cx-4..cx+4 all opaque). This is y=23 for the male
    idle frame, y=24 for the female — per SPRITE_SPEC.
    """
    def metrics(fi):
        c, r = fi % COLS, fi // COLS
        frame = skin_arr[r*H:(r+1)*H, c*W:(c+1)*W]
        zone = frame[:32, :, 3] > 0
        op = np.argwhere(zone)
        if len(op) == 0:
            return None
        ymin = int(op[:, 0].min())
        top = op[op[:, 0] <= ymin + 2]
        clusters = runs_of(sorted(set(top[:, 1].tolist())))
        chosen = None
        for a, b in clusters:
            for y in range(ymin, min(ymin + 6, 32)):
                xs = [x for x in range(max(0, a-2), min(W, b+3)) if zone[y, x]]
                if xs and max(e - s + 1 for s, e in runs_of(xs)) >= 7:
                    chosen = (a, b); break
            if chosen:
                break
        if chosen is None:
            chosen = clusters[0]
        a, b = chosen
        hymin = min(y for y in range(32) for x in range(a, b+1) if zone[y, x])
        def rowpix(y):
            return [x for s2, e in runs_of([x for x in range(W) if zone[y, x]])
                    if e >= a and s2 <= b for x in range(s2, e+1)]
        xs2 = [x for y in range(hymin, min(hymin + 2, 32)) for x in rowpix(y)]
        cx = int(round(sum(xs2) / len(xs2)))
        brim_row = hymin + 2                      # fallback
        for y in range(hymin, min(hymin + 8, H)):
            if all(frame[y, x, 3] > 0 for x in range(cx - 4, cx + 5)
                   if 0 <= x < W):
                brim_row = y
                break
        return hymin, cx, brim_row
    return metrics


# ── Tier symbols: {(dx, dy): rgb} offsets from (cx, sym_cy) ──────────────────

def tier_symbol(tier, P):
    A = P.get('A', SILVER)
    if tier == 1:                                   # tiny 3px star (sparkle)
        return {(0, -1): (215, 205, 245), (0, 0): (252, 248, 255),
                (0, 1): (215, 205, 245)}
    if tier == 2:                                   # 5px plus/cross
        c = (240, 232, 255)
        return {(0, 0): (252, 248, 255), (-1, 0): c, (1, 0): c,
                (0, -1): c, (0, 1): c}
    if tier == 3:                                   # crescent, open right
        c = (232, 224, 252)
        return {(0, -2): c, (-1, -1): c, (-1, 0): c, (-1, 1): c, (0, 2): c}
    if tier == 4:                                   # gold diamond outline
        g = A
        return {(0, -2): g, (-1, -1): g, (1, -1): g, (-2, 0): g, (2, 0): g,
                (-1, 1): g, (1, 1): g, (0, 2): g}
    if tier == 5:
        # Lightning bolt, compact + chunky: two fat 2px-wide arms with a
        # clear leftward kick, 5 rows tall (brim_row-7 .. brim_row-3). The
        # top arm sits on the right (dx=+2), the bottom arm on the left
        # (dx=0..+1) — the 2px shift reads as the zigzag at game scale,
        # where the old 8px-tall 1px-wide bolt collapsed into a thin slash.
        # Offsets are FINAL positions from (cx, brim_row), like t6 — no
        # anchor shift, no tilt. Every px sits inside the cone SILHOUETTE at
        # its row (dy=7: 0..+4; dy=6: -1..+4; dy=5: -2..+4; dy=4: -3..+4;
        # dy=3: -4..+5).
        # All colors pass sprite_shade.py's accent test (r>=230, g>=190).
        BY = (255, 255, 80)                         # bright yellow
        WH = (255, 255, 200)                        # white-hot flash
        return {(2, -7): BY,                        # top arm (right)
                (2, -6): BY,
                (2, -5): BY,                        # kick row, right side
                (1, -5): WH,                        # flash at the bend
                (1, -4): BY,                        # bottom arm (left)
                (0, -4): BY,
                (0, -3): BY}                        # bottom tip
    # tier 6: gold 4-pointed star / sunburst — the archmage's seal. Compact
    # and blocky so it reads at 2x game scale (the old full-height 1px-wide
    # bolt collapsed into a faint diagonal stroke). Offsets are FINAL
    # positions from (cx, brim_row): star centered at (+1, -5) — vertical
    # arm dy=-7..-3 at dx=+1, horizontal arm dx=-1..+3 at dy=-5, dim-gold
    # sparkle px on the four diagonals so it reads as a star, not a plus.
    # Every offset sits inside the cone SILHOUETTE at its row (dy=7: 0..+4;
    # dy=6: -1..+4; dy=5: -2..+4; dy=4: -3..+4; dy=3: -4..+5) — no clipping.
    # CRITICAL: every color passes sprite_shade.py's accent-gold test
    # (r>=230 AND g>=190) so the shader freezes the whole star. Dimmer
    # tones stay above that floor — (200,185,60) would be crushed to mud
    # by the band-smoothing pass, like the old rune was.
    BG = (255, 240, 100)                            # bright gold core + arms
    G  = (240, 220, 80)                             # gold side arms
    DG = (230, 200, 70)                             # dim gold sparkles
    return {(1, -7): BG,                            # top arm
            (1, -6): BG,
            (-1, -5): G, (0, -5): G,                # left arm
            (1, -5): BG,                            # center
            (2, -5): G, (3, -5): G,                 # right arm
            (1, -4): BG,                            # bottom arm
            (1, -3): BG,
            (0, -6): DG, (2, -6): DG,               # diagonal sparkles
            (0, -4): DG, (2, -4): DG}


# ── Hat builder ──────────────────────────────────────────────────────────────

def _finish(fill, over, no_outline_below):
    px = {}
    for (x, y) in set(fill):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if n not in fill and n[1] <= no_outline_below:
                px[n] = (0, 0, 0)
    px.update(fill)
    px.update(over)
    return px


def mage_hat_v5(tier, brim_row, cx):
    P = MAGE_HAT[tier]
    M = P['M']
    left_c   = scale_v(M, 0.75)   # shadowed left face
    right_c  = scale_v(M, 1.15)   # lit right face
    crease_c = scale_v(M, 0.65)   # fabric fold shadow
    fill, over = {}, {}

    # ── Brim: 13 wide at brim_row, outer 2px droop 1 row, curl-under shadow ──
    bw = HW + 4
    bx0 = cx - bw // 2
    edge_c   = scale_v(M, 0.85)
    droop_c  = scale_v(M, 0.65)
    shadow_c = scale_v(M, 0.45)
    for k in range(2, bw - 2):                     # center 9px anchor row
        fill[(bx0 + k, brim_row)] = M
    for k in range(bw // 2 + 1, bw - 2):           # lit right half of brim
        fill[(bx0 + k, brim_row)] = scale_v(M, 1.10)
    for k in (0, 1, bw - 2, bw - 1):               # overhang, same row
        fill[(bx0 + k, brim_row)] = edge_c         #   (keeps brim 4-connected)
        fill[(bx0 + k, brim_row + 1)] = droop_c    # droop, one row lower
    for k in (0, bw - 1):                          # outermost: curl-under
        fill[(bx0 + k, brim_row + 2)] = shadow_c

    # ── Crown: folded-back cone, tip curled right ────────────────────────────
    for dy in range(1, HC + 1):
        lo, ro = SILHOUETTE[dy]
        y = brim_row - dy
        x0, x1 = cx + lo, cx + ro
        wdt = x1 - x0 + 1
        for x in range(x0, x1 + 1):
            rel = (x - x0) / max(1, wdt - 1)
            fill[(x, y)] = (left_c if rel < 0.35 else
                            right_c if rel > 0.65 else M)

    # crease shadow along the fold line: leftmost px of rows dy=6..8
    for dy in (6, 7, 8):
        lo, _ = SILHOUETTE[dy]
        fill[(cx + lo, brim_row - dy)] = crease_c

    # sheen on the upper-right of the fold (V+0.12)
    for dy in (3, 4, 5):
        _, ro = SILHOUETTE[dy]
        for x in (cx + 3, cx + 4):
            if x <= cx + ro:
                fill[(x, brim_row - dy)] = add_v(right_c, 0.12)

    tip_y = brim_row - HC
    tip_x = cx + 2                                 # right px of the 2px tip

    # ── Tier symbol on the lower-center front face ───────────────────────────
    # The cone folds right from dy=4 up, so its center of mass at symbol
    # height sits ~1px right of cx: t4 anchors at cx+1. t5's lightning
    # bolt and t6's star use FINAL offsets from (cx, brim_row) with the
    # fold lean baked into the shape (see tier_symbol), so they get no
    # anchor shift and no tilt here. Both get a dark outline pass below.
    sym_cy = brim_row if tier in (5, 6) else brim_row - 4
    sym_cx = cx + 1 if tier == 4 else cx
    placed = []
    for (dx, dy), col in tier_symbol(tier, P).items():
        p = (sym_cx + dx, sym_cy + dy)
        if p in fill and p[1] <= brim_row - 1:
            over[p] = col
            placed.append(p)
    if tier in (5, 6):
        # 1px dark-purple outline on every cone-fill 4-neighbor of the bolt
        # so the yellow pops off the near-black hat at any render scale.
        OUTL = (30, 20, 60)
        for (x, y) in placed:
            for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + ddx, y + ddy)
                if n in fill and n not in over and n[1] <= brim_row - 1:
                    over[n] = OUTL

    # ── Flair ────────────────────────────────────────────────────────────────
    if P.get('tip_star'):
        over[(tip_x, tip_y)] = P['S']
    if P.get('sparkles'):                          # inside the fill: connected
        over[(cx + 3, brim_row - 7)] = P['S']
        over[(cx - 2, brim_row - 5)] = P['S']
        # t5 rain drops: scattered light blue-grey px around the bolt so the
        # sparkles read as a storm, not strays. Offsets sit inside the cone
        # SILHOUETTE at their rows (dy=4: -3..+4; dy=3: -4..+5) — no clipping.
        RAIN = (160, 170, 200)
        over[(cx + 4, brim_row - 4)] = RAIN        # lower-right of the bolt
        over[(cx - 3, brim_row - 3)] = RAIN        # lower-left, below sparkle
    if P.get('gold_rim'):                          # t6: gold on drooped rim px
        for k in (0, 1, bw - 2, bw - 1):
            over[(bx0 + k, brim_row + 1)] = P['A']

    return _finish(fill, over, no_outline_below=brim_row - 1)


# ── Sheet composition ────────────────────────────────────────────────────────

def get_active_frames(hat_path):
    a = np.array(Image.open(hat_path).convert('RGBA'))
    return [fi for fi in range(NFR)
            if (a[(fi//COLS)*H:(fi//COLS+1)*H, (fi%COLS)*W:(fi%COLS+1)*W, 3] > 0).any()]


def build_sheet(tier, frames, metrics_fn, hair_arr=None):
    """hair_arr: reference hair sheet (tallest style). Used by the gap-fill
    pass — any transparent px directly BELOW a hat px that has hair directly
    beneath it gets the curl-under shadow tone. Closes the 1px notches that
    appear where a hair strand starts a row below the brim edge (e.g. female
    frame 0 at (47,24)). Only 4-adjacent extensions, so frames stay connected.
    """
    shadow_rgba = (*scale_v(MAGE_HAT[tier]['M'], 0.45), 255)
    sheet = np.zeros((H * 7, W * COLS, 4), np.uint8)
    for fi in frames:
        m = metrics_fn(fi)
        if m is None:
            continue
        _head_top, cx, brim_row = m
        gx, gy = (fi % COLS) * W, (fi // COLS) * H
        px = mage_hat_v5(tier, brim_row, cx)
        for (x, y), rgb in px.items():
            if 0 <= x < W and 0 <= y < H:
                sheet[gy + y, gx + x] = (*rgb, 255)
        if hair_arr is None:
            continue
        hair_f = hair_arr[gy:gy + H, gx:gx + W, 3]
        for y in range(brim_row, min(brim_row + 3, H - 1)):
            for x in range(max(1, cx - 8), min(W - 1, cx + 9)):
                if (sheet[gy + y, gx + x, 3] == 0        # transparent notch
                        and sheet[gy + y - 1, gx + x, 3] > 0   # hat above
                        and hair_f[y, x] == 0                  # no hair here
                        and hair_f[y + 1, x] > 0):             # hair below
                    sheet[gy + y, gx + x] = shadow_rgba
    return sheet


def main():
    skin_m = np.array(Image.open(f"{CH}/skin_m1.png").convert('RGBA'))
    skin_f = np.array(Image.open(f"{CH}/skin_f1.png").convert('RGBA'))
    hair_m = np.array(Image.open(f"{CH}/hair_m1.png").convert('RGBA'))
    hair_f = np.array(Image.open(f"{CH}/hair_f1.png").convert('RGBA'))
    metrics_m = make_head_metrics_fn(skin_m)
    metrics_f = make_head_metrics_fn(skin_f)

    frames_m = get_active_frames(f"{CH}/helmet_mage1.png")
    for tier in range(1, 7):
        sheet = build_sheet(tier, frames_m, metrics_m, hair_m)
        Image.fromarray(sheet).save(f"{CH}/helmet_mage{tier}.png")
        print(f"wrote helmet_mage{tier}.png ({len(frames_m)} frames)")

    t1f = f"{CH}/helmet_mage1_f.png"
    if os.path.exists(t1f):
        frames_f = get_active_frames(t1f)
        Image.fromarray(build_sheet(1, frames_f, metrics_f, hair_f)).save(t1f)
        print(f"wrote helmet_mage1_f.png ({len(frames_f)} frames)")


if __name__ == '__main__':
    main()
