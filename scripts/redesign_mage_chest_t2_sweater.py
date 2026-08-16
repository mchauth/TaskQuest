#!/usr/bin/env python3
"""Redesign mage chest T2 (shirt_mage2 + _f) — button-up sweater over collared shirt.

"Apprentice Robes II" (level 5) becomes an academic/casual mage look: a fitted
heathered-purple button-up sweater worn over a cream collared shirt. Built from
the shirt_mage1[.png/_f] silhouette (tracks every pose), same authoring
philosophy as redesign_mage_chest_t23.py:

  Tones   : T1's per-pixel V quantized against the frame median into a 3-tone
            ramp (shadow / base / highlight) so sprite_shade's diffusion makes
            smooth knit-fabric gradients.
            D=(40,20,90)  M=(60,30,120)  L=(86,50,158)
  Collar  : cream (240,240,235) shirt collar, two matching 3-px L-shapes
            (6 px total), one on each side of the neck opening. The V-neck
            opening is located per frame as the garment-transparent,
            skin-backed pixels near the head center. Anchored on the
            opening's ymid row: ly=ry = ymid+2 (the 6ec4132-approved collar
            sat at ymid+1; +1 more shifts it down so the sweater neckline
            rim above reads as body, not a stray purple pixel on the tips),
            lx = left opening edge at ymid minus 1, rx = right edge plus 1.
            Left L is (lx,ly)+(lx,ly+1)+(lx+1,ly+1), right L the mirror
            (rx,ry)+(rx,ry+1)+(rx-1,ry+1) — vertical tip + horizontal arm
            pointing INWARD toward the neck center (the 6ec4132 shape).
            Each side is drawn independently; tips always drawn, base
            pixels clamp one row lower if they fall outside the
            silhouette, else skipped. Passes sprite_shade's accent test
            (r>=230 & g>=190) so it stays crisp. Only on frames where the
            neck is visible: idle/walk/run/jump (fi < 40) and only when the
            opening is actually found — cheer and slash raise/shift the arms
            over the neckline, sleep lies down.
  Buttons : vertical line down the sweater center, dark (30,20,50) 1 px each
            with a (190,170,230) catch-light 1 px above. Button column is
            btn_x = bcx - 1 (decoupled from the collar center; 1 px lower x
            = 1 px to the character's right on screen). Male rows
            neck+4/+7/+10(+13), female neck+3/+6/+9. Idle + walk frames only
            (fi < 20).
  Cuffs   : darker purple (40,20,90), 2 px tall at the sleeve bottoms of the
            outer columns, idle/walk/run only (fi < 30) — same stray-diagonal
            guard as the T2/T3 robe script.
  Hem     : fitted — NO flare, no under-robe band. Bottom edge rows get the
            shadow tone as a ribbed hem band (upright frames only).
  Sleep   : frames fi >= 60 get tones only.

Run from repo root:
  python3 scripts/redesign_mage_chest_t2_sweater.py
Shading is applied in-script with the shirt override (ADJ_MIN=-0.20,
ADJ_MAX=+0.25, BELL_WIDTH=0.7) — do NOT run sprite_shade.py again on top.
Then QA:
  python3 scripts/sprite_qa.py sprites/preview_assets/char/shirt_mage2.png \
      sprites/preview_assets/char/shirt_mage2_f.png
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR
from rebuild_class_hats import make_head_dome_fn

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18            # v/vref quantization thresholds (house style)

D      = (40, 20, 90)              # shadow / cuffs / hem rib
M      = (60, 30, 120)             # sweater base (heathered purple)
L      = (86, 50, 158)             # highlight
COLLAR = (240, 240, 235)           # cream shirt collar (accent-frozen)
BTN    = (30, 20, 50)              # button
BTN_HI = (190, 170, 230)           # catch-light above each button


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def find_neck_opening(a, skin_a, cx, y0):
    """Locate the V-neck opening: garment-transparent, skin-backed pixels
    near the head center. Returns (ymid, runs) — the collar row and a dict
    mapping each opening row to its (lx, rx) edge columns — or None if no
    opening is visible this frame."""
    hole = (~a) & skin_a
    # Seed: deepest hole column close to the head center (the notch tip);
    # ties break toward cx so the deep side gaps beside the arms can't win.
    seed, best = None, 0
    for x in range(max(0, cx - 3), min(a.shape[1] - 1, cx + 3) + 1):
        ys_h = np.flatnonzero(hole[:, x])
        ys_h = ys_h[(ys_h >= y0) & (ys_h <= y0 + 8)]
        # the notch hangs from the neckline: must start near the garment
        # top, and only its contiguous-from-top span counts as depth (so a
        # detached lower hole in the same column can't inflate it).
        if len(ys_h) == 0 or ys_h[0] > y0 + 2:
            continue
        d = 1
        while d < len(ys_h) and ys_h[d] == ys_h[0] + d:
            d += 1
        if d > best or (d == best and abs(x - cx) < abs(seed - cx)):
            best, seed = d, int(x)
    if seed is None:
        return None
    # Walk the notch top-down: the first row's run must contain the seed,
    # every later row's run must horizontally overlap the previous row's.
    # Side gaps never overlap the notch, so they cannot leak in.
    runs, prev = {}, None
    for y in range(y0, min(y0 + 9, a.shape[0])):
        xs_h = np.flatnonzero(hole[y, :])
        xs_h = xs_h[(xs_h >= cx - 6) & (xs_h <= cx + 6)]
        if len(xs_h) == 0:
            if prev is not None:
                break
            continue
        groups = np.split(xs_h, np.where(np.diff(xs_h) > 1)[0] + 1)
        if prev is None:
            g = next((g for g in groups if g[0] <= seed <= g[-1]), None)
            if g is None:
                continue
        else:
            cand = [g for g in groups if g[0] <= prev[1] and g[-1] >= prev[0]]
            if not cand:
                break
            # widest overlap wins (ties: closest to the previous run's
            # center) — a wide neckline row can merge with a side gap, and
            # the notch continues from the middle, not the gap end.
            pc = (prev[0] + prev[1]) / 2.0
            g = max(cand, key=lambda g: (
                min(int(g[-1]), prev[1]) - max(int(g[0]), prev[0]),
                -abs((int(g[0]) + int(g[-1])) / 2.0 - pc)))
        runs[y] = prev = (int(g[0]), int(g[-1]))
    if not runs:
        return None
    # Collar row: middle of the NARROW (V-edge) rows. The top row of a scoop
    # neckline can span shoulder to shoulder — that is neckline, not collar.
    narrow = [y for y in runs if runs[y][1] - runs[y][0] + 1 <= 5]
    rows = sorted(narrow if narrow else runs)
    ymid = rows[len(rows) // 2]
    return ymid, runs


def build(base, skin_sheet, dome, female):
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

        # ── 1. quantized 3-tone recolor of the T1 silhouette ────────────────
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            put(fr, y, x, tone)

        # ── 2. frame geometry (garment bbox + skin-sheet skull tracking) ────
        ys, xs = np.where(a)
        y0, y1 = int(ys.min()), int(ys.max())
        x0, x1 = int(xs.min()), int(xs.max())
        w = max(1, x1 - x0)
        cols = np.unique(xs)
        top = {int(x): int(ys[xs == x].min()) for x in cols}
        bot = {int(x): int(ys[xs == x].max()) for x in cols}
        hp = dome(fi)                       # (head_top, cx) from skin sheet
        cx = hp[1] if hp else int(round(x0 + 0.5 * w))
        sleeping = fi >= 60
        # Collar anchor: deepest transparent row of the V-neck notch. The
        # notch columns have LARGER top[] values than the neckline shoulders,
        # so max(tops)-1 is the lowest open row inside the opening. Clamped
        # to min(tops) for frames with a flat neckline (no notch).
        tops = [top[x] for x in range(cx - 2, cx + 3) if x in top]
        neck = max(min(tops), max(tops) - 1)   # fallback anchor
        btn_x = cx - 2                         # fallback button column
        opening = find_neck_opening(a, skin_alpha[sl], cx, y0) \
            if not sleeping else None
        if opening:
            ymid, oruns = opening
            olx, orx = oruns[ymid]
            neck = max(oruns)                  # buttons hang from opening tip
            btn_x = (olx + orx) // 2           # centered under the opening

        def clip_col(x):
            # nearest column that actually has garment pixels
            return x if x in top else min(top, key=lambda k: abs(k - x))

        def clip_row(y, x):
            # snap to the nearest OPAQUE row of column x (columns can have
            # transparent holes mid-span)
            rows = np.flatnonzero(a[:, x])
            return min((int(ry) for ry in rows), key=lambda ry: abs(ry - y))

        # ── 3. button line down the sweater center (idle/walk only) ─────────
        if fi < 20:
            offs = (3, 6, 9) if female else (4, 7, 10, 13)
            xb = clip_col(btn_x)
            for off in offs:
                by = neck + off
                if by <= y1 - 2 and a[by, xb]:
                    put(fr, by, xb, BTN)
                    if by - 1 > neck + 1 and a[by - 1, xb]:
                        put(fr, by - 1, xb, BTN_HI)

        # ── 4. sleeve cuffs: bottom 2 px of short outer columns (fi < 30) ────
        if fi < 30:
            for x in cols:
                rel = (x - x0) / w
                if (rel <= 0.16 or rel >= 0.84) and bot[x] < y1 - 2:
                    put(fr, bot[x], x, D)
                    if a[bot[x] - 1, x]:
                        put(fr, bot[x] - 1, x, D)

        # ── 5. fitted ribbed hem: shadow the bottom edge (upright frames) ────
        if not sleeping:
            for x in cols:
                if bot[x] >= y1 - 1:
                    put(fr, bot[x], x, D)

        # ── 6. shirt collar points (neck-visible frames only) ───────────────
        # Two matching L-shapes, one on each side of the neck opening — the
        # exact 6ec4132-approved shape, shifted 1 px further down. Anchored
        # on the opening's ymid row: ly=ry = ymid+2, lx = left edge at ymid
        # minus 1, rx = right edge plus 1 (this reproduces the 6ec4132
        # frame-0 x positions on both sheets). Left L is (lx,ly) tip,
        # (lx,ly+1) corner, (lx+1,ly+1) arm pointing INWARD toward the
        # neck center; right L is the mirror: (rx,ry), (rx,ry+1),
        # (rx-1,ry+1). The arms stay separated (lx+1 < rx-1 whenever the
        # opening is >=1 px wide at ymid). Each side is drawn INDEPENDENTLY
        # (no pairwise/mirror gating — that dropped pixels). The tip at
        # ly/ry is ALWAYS drawn; each base pixel (row ly+1) is clamped
        # per-pixel against the silhouette — if transparent, try one row
        # lower (ly+2), and if still transparent, skip that pixel. Drawn
        # LAST so cuffs/hem can never overwrite a collar pixel.
        if fi < 40 and opening:
            ly = ry = ymid                     # collar row (was ymid+2; up 2px)
            olx, orx = oruns[ymid]             # opening edges at ymid
            lx, rx = olx - 1, orx + 1          # tips sit just outside them
            # a collar pixel may sit on the garment OR on the skin-backed
            # opening (the shirt peeking through the V-neck) — only truly
            # EMPTY space (no garment, no skin) counts as transparent.
            backed = a | skin_alpha[sl]

            def draw_L(tx, ty, dx):
                drawn = []
                put(fr, ty, tx, COLLAR)        # tip: always drawn
                drawn.append((tx, ty))
                for px in (tx, tx + dx):       # corner, then horizontal arm
                    py = ty + 1
                    if not (0 <= px < FW):
                        continue
                    if py < FH and backed[py, px]:
                        put(fr, py, px, COLLAR)
                        drawn.append((px, py))
                    elif py + 1 < FH and backed[py + 1, px]:
                        put(fr, py + 1, px, COLLAR)
                        drawn.append((px, py + 1))
                return drawn

            left_px = draw_L(lx, ly, +1)       # arm points RIGHT (inward)
            right_px = draw_L(rx, ry, -1)      # arm points LEFT (inward)
            if fi == 0:
                print('  frame 0 collar L pixels (x,y): %s' % left_px)
                print('  frame 0 collar R pixels (x,y): %s' % right_px)
    return out


def main():
    for suffix, skin, female in (('', 'skin_m1.png', False),
                                 ('_f', 'skin_f1.png', True)):
        base = load('shirt_mage1%s.png' % suffix)
        skin_sheet = load(skin)
        dome = make_head_dome_fn(skin_sheet)
        arr = build(base, skin_sheet, dome, female)
        arr = shade(arr, adj_min=-0.20, adj_max=0.25)
        dst = 'shirt_mage2%s.png' % suffix
        Image.fromarray(arr).save(CHAR + dst)
        print('wrote %s' % dst)


if __name__ == '__main__':
    main()
