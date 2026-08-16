#!/usr/bin/env python3
"""
fix_combat_strays.py — Detect (and optionally remove) stray pixels in the
combat (Slash, row 5) frames of rare shirt sprite sheets.

Detection rules within each combat frame (50-55):
  1. Isolated pixels: opaque pixel with zero opaque 4-neighbors.
  2. Tiny clusters: connected components (8-conn) of <= MAX_CLUSTER px that are
     detached from the main silhouette (main component = largest in frame).
  3. Frame-edge bleed: opaque pixels in the outer 2px margin of a frame that
     are disconnected from the frame's main component (diffusion bleed from a
     neighboring frame).
  4. Palette outliers: pixels whose hue is far from every color in the frame's
     dominant palette (built from frame 0, the canonical idle frame).

Usage:
  python3 fix_combat_strays.py <sheet.png> [--fix]
"""
import sys
import numpy as np
from PIL import Image
from collections import deque

FRAME_W, FRAME_H = 80, 64
COLS, ROWS = 10, 7
COMBAT_FRAMES = [50, 51, 52, 53, 54, 55]   # row 5 = Slash (HANDOFF.md)
MAX_CLUSTER = 3
ALPHA_MIN = 10


def frame_slice(fi):
    col, row = fi % 10, fi // 10
    x0, y0 = col * FRAME_W, row * FRAME_H
    return x0, y0


def components(mask):
    """8-connected components of a boolean mask. Returns label array + sizes."""
    lab = np.zeros(mask.shape, dtype=np.int32)
    sizes = {}
    nxt = 0
    H, W = mask.shape
    for sy in range(H):
        for sx in range(W):
            if mask[sy, sx] and lab[sy, sx] == 0:
                nxt += 1
                q = deque([(sy, sx)])
                lab[sy, sx] = nxt
                n = 0
                while q:
                    y, x = q.popleft()
                    n += 1
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx_ = y + dy, x + dx
                            if 0 <= ny < H and 0 <= nx_ < W and mask[ny, nx_] and lab[ny, nx_] == 0:
                                lab[ny, nx_] = nxt
                                q.append((ny, nx_))
                sizes[nxt] = n
    return lab, sizes


def build_palette(img):
    """Palette from frame 0 (canonical idle frame): unique RGB of opaque px."""
    x0, y0 = frame_slice(0)
    fr = img[y0:y0 + FRAME_H, x0:x0 + FRAME_W]
    op = fr[:, :, 3] > ALPHA_MIN
    cols = fr[op][:, :3].astype(np.int32)
    if len(cols) == 0:
        return np.zeros((0, 3), dtype=np.int32)
    return np.unique(cols, axis=0)


def palette_dist(rgb, palette):
    if len(palette) == 0:
        return 0
    d = np.abs(palette - np.array(rgb, dtype=np.int32)).sum(axis=1)
    return int(d.min())


def analyze(path, fix=False):
    im = Image.open(path).convert('RGBA')
    img = np.array(im)
    assert img.shape == (448, 800, 4), f"unexpected size {img.shape}"
    palette = build_palette(img)
    findings = []  # (frame, sheet_x, sheet_y, rgba, reason)

    for fi in COMBAT_FRAMES:
        x0, y0 = frame_slice(fi)
        fr = img[y0:y0 + FRAME_H, x0:x0 + FRAME_W]
        op = fr[:, :, 3] > ALPHA_MIN
        if not op.any():
            continue
        lab, sizes = components(op)
        main = max(sizes, key=sizes.get)

        for fy in range(FRAME_H):
            for fx in range(FRAME_W):
                if not op[fy, fx]:
                    continue
                r, g, b, a = (int(v) for v in fr[fy, fx])
                reasons = []
                # rule 1: isolated (no 4-neighbors)
                n4 = 0
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx_ = fy + dy, fx + dx
                    if 0 <= ny < FRAME_H and 0 <= nx_ < FRAME_W and op[ny, nx_]:
                        n4 += 1
                if n4 == 0:
                    reasons.append("isolated")
                # rule 2/3: small detached cluster / edge bleed
                if lab[fy, fx] != main:
                    if sizes[lab[fy, fx]] <= MAX_CLUSTER:
                        reasons.append(f"detached-cluster({sizes[lab[fy, fx]]}px)")
                    if fx < 2 or fx >= FRAME_W - 2 or fy < 2 or fy >= FRAME_H - 2:
                        reasons.append("frame-edge-bleed")
                # rule 4: palette outlier
                pd = palette_dist((r, g, b), palette)
                if pd > 120:
                    reasons.append(f"palette-outlier(d={pd})")
                if reasons:
                    findings.append((fi, x0 + fx, y0 + fy, (r, g, b, a), "+".join(reasons)))

    name = path.split('/')[-1]
    print(f"\n=== {name} ===  ({len(findings)} stray pixel(s))")
    for fi, sx, sy, rgba, why in findings:
        print(f"  frame {fi}  sheet({sx:3d},{sy:3d})  rgba{rgba}  [{why}]")

    if fix and findings:
        for fi, sx, sy, rgba, why in findings:
            img[sy, sx] = (0, 0, 0, 0)
        Image.fromarray(img).save(path)
        print(f"  -> fixed {len(findings)} pixel(s), saved {path}")
    return findings


if __name__ == '__main__':
    fix = '--fix' in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith('--')]
    total = 0
    for p in paths:
        total += len(analyze(p, fix=fix))
    print(f"\nTotal: {total} stray pixel(s) {'fixed' if fix else 'found (dry run)'}")
