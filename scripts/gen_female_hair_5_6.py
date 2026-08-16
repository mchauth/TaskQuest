#!/usr/bin/env python3
"""Derive female hairstyles 5 (Bob) and 6 (Pixie) from Short (hair_f1-5).

Purely SUBTRACTIVE per-frame: isolate hair pixels (diff vs skin), then remove
the thin shoulder-fall below the main head mass. Pixie also tapers the lower
sides. Subtractive-only guarantees no pixels appear outside the original
silhouette, so no strays can be introduced. Colors carry over from source.

Style 5 (Bob)   files hair_f21-25  <- hair_f1-5
Style 6 (Pixie) files hair_f26-30  <- hair_f1-5
"""
import sys
from PIL import Image

CHAR = "sprites/preview_assets/char"
FW, FH = 80, 64
COLS, ROWS = 10, 7

def frame_box(idx):
    c, r = idx % COLS, idx // COLS
    return (c*FW, r*FH, c*FW+FW, r*FH+FH)

def load_frames(path):
    im = Image.open(path).convert("RGBA")
    return im

def is_hair(hp, sp):
    if hp[3] < 30:
        return False
    if sp[3] < 30:
        return True
    d = abs(hp[0]-sp[0]) + abs(hp[1]-sp[1]) + abs(hp[2]-sp[2])
    return d > 15

def process_frame(hair_px, skin_px, mode):
    """Return set of (x,y) pixels to CLEAR (make transparent)."""
    # per-row hair x-extents
    rows = {}
    for y in range(FH):
        xs = [x for x in range(FW) if is_hair(hair_px(x, y), skin_px(x, y))]
        if xs:
            rows[y] = xs
    if not rows:
        return set()
    ys = sorted(rows)
    top = ys[0]
    # Crown-relative cut: keep hair from the crown down to a fixed number of
    # rows below the topmost hair pixel. Robust across facing directions since
    # it tracks each frame's own head position.
    if mode == "bob":
        cut = top + 8    # jaw-length bob
    else:  # pixie
        cut = top + 6    # cropped pixie
    clear = set()
    # Clear ALL non-transparent pixels below the cut line. The hair sheet
    # contains only hair pixels, so anything below the hairline is hair —
    # this also catches dark outline pixels that sit within the skin-diff
    # threshold and would otherwise be left orphaned (QA isolated-pixel fail).
    for y in range(cut + 1, FH):
        for x in range(FW):
            if hair_px(x, y)[3] >= 30:
                clear.add((x, y))
    # taper lower sides on both styles: trim 1px off each edge of bottom 2 rows
    kept = [y for y in ys if y <= cut]
    for y in kept[-2:]:
        xs = sorted(rows[y])
        if len(xs) >= 4:
            clear.add((xs[0], y))
            clear.add((xs[-1], y))
    return clear

def build(src_path, out_path, mode):
    hair = load_frames(src_path)
    skin = load_frames(f"{CHAR}/skin.png")
    out = hair.copy()
    op = out.load()
    hp_full = hair.load()
    sp_full = skin.load()
    total_cleared = 0
    for idx in range(COLS*ROWS):
        bx, by, _, _ = frame_box(idx)
        # local pixel accessors
        hpx = lambda x, y: hp_full[bx+x, by+y]
        spx = lambda x, y: sp_full[bx+x, by+y]
        clear = process_frame(hpx, spx, mode)
        for (x, y) in clear:
            op[bx+x, by+y] = (0, 0, 0, 0)
        total_cleared += len(clear)
    out.save(out_path)
    return total_cleared

if __name__ == "__main__":
    import os
    OUT = sys.argv[1] if len(sys.argv) > 1 else CHAR
    os.makedirs(OUT, exist_ok=True)
    # style 5 Bob: f21-25 from f1-5 ; style 6 Pixie: f26-30 from f1-5
    for color in range(1, 6):
        src = f"{CHAR}/hair_f{color}.png"
        bob = f"{OUT}/hair_f{20+color}.png"
        pix = f"{OUT}/hair_f{25+color}.png"
        cb = build(src, bob, "bob")
        cp = build(src, pix, "pixie")
        print(f"color{color}: bob->{bob} cleared={cb}  pixie->{pix} cleared={cp}")
    print("done")
