#!/usr/bin/env python3
"""add_helmet_back_outline.py — Consistent perimeter outline for generated helmet sheets.

Problem
-------
Generated legendary helmet sheets are produced from procedural dome art with
no authored outline ring. `carve_face_openings` adds a visor slit (eye/mouth
pixels) but rim=False is used to avoid flattening patterned designs. The
result: every frame has a fully unoutlined silhouette except for a few interior
visor pixels. Visually the helmet floats with no edge definition.

Back/side frames (fr62-66) compound this — carve_face_openings places visor
pixels based on the skin sheet face position, but in those frames the character
is turning away so the visor lands on the back of the head. Those frames end up
with even fewer coherent black pixels.

Fix
---
For every frame on every helmet sheet, check what fraction of its perimeter
pixels are already dark (RGB sum < 90). If fewer than OUTLINE_THRESHOLD of the
perimeter ring is dark, darken the entire ring with a hue-preserving multiply
(same formula as carve_face_openings OUTLINE_MUL). This:

  - Adds a consistent dark edge to generated legendaries on ALL frames
  - Skips frames that are already well-outlined (authored helmets: ranger/mage
    base sets already have 50-90% dark perimeter, so they are untouched)
  - Is idempotent: a frame outlined by a previous run of this script has 100%
    dark perimeter, so it is skipped on re-runs

Open-headgear guard: if frame 0 has fewer than MIN_IDLE_ALPHA opaque pixels,
the sheet is a hat/hood/circlet and is skipped entirely.

Usage
-----
  python3 scripts/add_helmet_back_outline.py sprites/preview_assets/char/
  python3 scripts/add_helmet_back_outline.py --dry-run sprites/preview_assets/char/
  python3 scripts/add_helmet_back_outline.py --force sprites/preview_assets/char/
"""
import os
import sys
import glob
import argparse
import numpy as np
from PIL import Image, PngImagePlugin

FW, FH, COLS, NFR = 80, 64, 10, 70

OUTLINE_MUL      = 0.28   # multiplicative darken factor for perimeter ring
OUTLINE_MAX_SUM  = 90     # clamp so bright pixels go as dark as already-dark ones

# Fraction of perimeter pixels that must be dark (RGB sum < OUTLINE_MAX_SUM)
# before we consider the frame already outlined and skip it.
# Authored helmets (mage/ranger base) sit at 50-90% → safely above this.
# Generated legendaries before fix sit at 0-10% → safely below.
OUTLINE_THRESHOLD = 0.30

# Minimum opaque pixels on idle frame 0 to be treated as a closed helmet.
# Below this it is a hat/hood/circlet whose silhouette reads fine without rim.
MIN_IDLE_ALPHA = 40

STAMP_KEY = "HelmOutlineV2"
VERSION   = "1"


def _boundary(op):
    """Opaque pixels touching transparency (4-neighborhood)."""
    pad = np.pad(op, 1, constant_values=False)
    return op & ~(pad[:-2, 1:-1] & pad[2:, 1:-1] &
                  pad[1:-1, :-2] & pad[1:-1, 2:])


def _dark_frac(sl, ring):
    """Fraction of ring pixels whose RGB sum is below OUTLINE_MAX_SUM."""
    if not ring.any():
        return 1.0
    dark = (sl[ring, :3].astype(int).sum(1) < OUTLINE_MAX_SUM)
    return float(dark.sum()) / float(ring.sum())


def _darken_rim(frame_out, ring):
    """Hue-preserving darken of ring pixels. Modifies frame_out in place."""
    px = frame_out[ring, :3].astype(np.float32)
    lum = np.maximum(px.sum(1, keepdims=True), 1.0)
    f = np.minimum(OUTLINE_MUL, OUTLINE_MAX_SUM / lum)
    darkened = np.clip(px * f, 0, 255).astype(np.uint8)
    frame_out[ring, 0] = darkened[:, 0]
    frame_out[ring, 1] = darkened[:, 1]
    frame_out[ring, 2] = darkened[:, 2]


def process(path, dry_run=False, force=False):
    """Outline frames that need it. Returns (frames_changed, px_changed) or None."""
    try:
        img = Image.open(path)
        if img.size != (800, 448):
            return None
        if not force and img.info.get(STAMP_KEY) == VERSION:
            return (0, 0)
        arr = np.array(img.convert('RGBA'))
    except Exception as e:
        print(f"  ERR {os.path.basename(path)}: {e}", file=sys.stderr)
        return None

    # Open-headgear guard
    sl0 = arr[0:FH, 0:FW]
    if int((sl0[..., 3] > 0).sum()) < MIN_IDLE_ALPHA:
        return None

    out = arr.copy()
    frames_changed = 0
    px_changed = 0

    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = out[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
        op = sl[..., 3] > 0
        if not op.any():
            continue
        ring = _boundary(op)
        if not ring.any():
            continue
        if _dark_frac(sl, ring) >= OUTLINE_THRESHOLD:
            continue   # already well-outlined — skip
        _darken_rim(sl, ring)
        frames_changed += 1
        px_changed += int(ring.sum())

    if frames_changed == 0:
        return (0, 0)

    if not dry_run:
        meta = PngImagePlugin.PngInfo()
        meta.add_text(STAMP_KEY, VERSION)
        for k, v in img.info.items():
            if k not in (STAMP_KEY, 'dpi') and isinstance(v, str):
                try:
                    meta.add_text(k, v)
                except Exception:
                    pass
        Image.fromarray(out).save(path, pnginfo=meta)

    return (frames_changed, px_changed)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('paths', nargs='+', help='PNG files or directories')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true',
                    help='re-process already-stamped files')
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            files += glob.glob(os.path.join(p, 'helmet_*.png'))
        elif os.path.isfile(p):
            files.append(p)
        else:
            print(f"WARN: not found: {p}", file=sys.stderr)

    files = sorted(set(files))
    if not files:
        print("No helmet PNG files found.")
        return

    total_files = 0
    total_frames = 0
    total_px = 0
    skipped = 0

    tag = '[dry] ' if args.dry_run else ''
    for path in files:
        result = process(path, dry_run=args.dry_run, force=args.force)
        if result is None:
            skipped += 1
            continue
        fc, px = result
        if fc > 0:
            print(f"{tag}{os.path.basename(path)}: {fc} frames, {px} px")
            total_files += 1
            total_frames += fc
            total_px += px

    print(f"\n{tag}Done — {total_files} files updated "
          f"({total_frames} frames, {total_px} px), {skipped} skipped")


if __name__ == '__main__':
    main()
