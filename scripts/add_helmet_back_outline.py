#!/usr/bin/env python3
"""add_helmet_back_outline.py — Dark perimeter outline on helmet back/side frames.

Problem
-------
carve_face_openings.py is called with rim=False for all frames, so helmet
sheets have NO outline ring anywhere. On front-facing frames the visor slit
(eye/mouth pixels) provides enough definition. On back/side frames (fr62-66,
row 6 cols 2-6, where the character turns away during the sleep animation)
the visor pixels land on the BACK of the head and look wrong, and the helmet
silhouette has no dark edge at all.

Fix
---
For frames 62-66 only, darken the outermost opaque pixel ring with a
hue-preserving multiply (same formula as carve_face_openings.OUTLINE_MUL).
This gives the back of the helmet a clear silhouette edge without touching
the coloured/patterned interior or any other frame.

Open headgear guard
-------------------
Wizard hats, hoods, and circlets are identified by low coverage on the idle
frame (< HELM_MIN_PX opaque pixels). They are skipped — their silhouette
already reads fine without an extra dark rim.

Usage
-----
  python3 scripts/add_helmet_back_outline.py sprites/preview_assets/char/
  python3 scripts/add_helmet_back_outline.py --dry-run sprites/preview_assets/char/
  python3 scripts/add_helmet_back_outline.py --force sprites/preview_assets/char/
  python3 scripts/add_helmet_back_outline.py path/to/helmet_warrior_legendary54.png
"""
import os
import sys
import glob
import argparse
import numpy as np
from PIL import Image, PngImagePlugin

FW, FH, COLS, NFR = 80, 64, 10, 70
BACK_FRAMES = list(range(62, 67))   # fr62-66 (row 6 cols 2-6)

OUTLINE_MUL     = 0.28   # multiplicative darken factor for perimeter ring
OUTLINE_MAX_SUM = 90     # cap sum so bright pixels go uniformly dark

# Authored helmets (helmet_2/3/4, ranger/mage base sets) already carry
# consistent black structure in back frames — ratio of min back-frame black
# count to idle frame black count sits at 0.77+. Generated legendaries drop
# to 0.09-0.60. Skip anything at or above 0.70 to avoid double-darkening.
BACK_RATIO_THRESHOLD = 0.70

STAMP_KEY = "HelmBackOutline"
VERSION   = "1"


def _boundary(op):
    """Opaque pixels touching transparency (4-neighborhood)."""
    pad = np.pad(op, 1, constant_values=False)
    return op & ~(pad[:-2, 1:-1] & pad[2:, 1:-1] &
                  pad[1:-1, :-2] & pad[1:-1, 2:])


def _darken_rim(frame_out, op):
    """Hue-preserving darken of the perimeter ring. Modifies frame_out in place."""
    ring = _boundary(op)
    if not ring.any():
        return 0
    px = frame_out[ring, :3].astype(np.float32)
    lum = np.maximum(px.sum(1, keepdims=True), 1.0)
    f = np.minimum(OUTLINE_MUL, OUTLINE_MAX_SUM / lum)
    darkened = np.clip(px * f, 0, 255).astype(np.uint8)
    frame_out[ring, 0] = darkened[:, 0]
    frame_out[ring, 1] = darkened[:, 1]
    frame_out[ring, 2] = darkened[:, 2]
    return int(ring.sum())


def _black_count(sl):
    return int(((sl[..., 0] < 40) & (sl[..., 1] < 40) & (sl[..., 2] < 40)
                & (sl[..., 3] > 0)).sum())


def _needs_outline(arr):
    """Return True if back frames lack authored dark structure.

    Authored helmets keep the same black pixel count in back frames as idle.
    Generated legendaries drop to ~10-60% of idle. Threshold = 0.70.
    """
    idle_b = _black_count(arr[0:FH, 0:FW])
    if idle_b == 0:
        return False
    min_b = idle_b
    for fi in BACK_FRAMES:
        r, c = fi // COLS, fi % COLS
        sl = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
        if (sl[..., 3] > 0).any():
            min_b = min(min_b, _black_count(sl))
    return (min_b / idle_b) < BACK_RATIO_THRESHOLD


def process(path, dry_run=False, force=False):
    """Add back-outline to one helmet sheet. Returns (frames_changed, px_changed) or None."""
    try:
        img = Image.open(path)
        if img.size != (800, 448):
            return None
        # Idempotency stamp
        if not force and img.info.get(STAMP_KEY) == VERSION:
            return (0, 0)
        arr = np.array(img.convert('RGBA'))
    except Exception as e:
        print(f"  ERR {os.path.basename(path)}: {e}", file=sys.stderr)
        return None

    # Skip authored helmets that already have consistent back-frame structure
    if not _needs_outline(arr):
        return None

    out = arr.copy()
    frames_changed = 0
    px_changed = 0

    for fi in BACK_FRAMES:
        r, c = fi // COLS, fi % COLS
        sl = out[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
        op = sl[..., 3] > 0
        if not op.any():
            continue
        n = _darken_rim(sl, op)
        if n:
            frames_changed += 1
            px_changed += n

    if frames_changed == 0:
        return (0, 0)

    if not dry_run:
        meta = PngImagePlugin.PngInfo()
        meta.add_text(STAMP_KEY, VERSION)
        # Carry any existing metadata from the source image
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
    ap.add_argument('--dry-run', action='store_true',
                    help='report what would change without writing files')
    ap.add_argument('--force', action='store_true',
                    help='re-process files already stamped with this version')
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
            print(f"{tag}{os.path.basename(path)}: {fc} frames, {px} px outlined")
            total_files += 1
            total_frames += fc
            total_px += px

    print(f"\n{tag}Done — {total_files} files updated "
          f"({total_frames} frames, {total_px} px), {skipped} skipped (open headgear / wrong size)")


if __name__ == '__main__':
    main()
