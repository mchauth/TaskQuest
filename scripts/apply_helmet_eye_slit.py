#!/usr/bin/env python3
"""Carve a proper eye/face slit into closed-helm sprites that lost theirs.

Many generated WARRIOR legendary helmets recolor every opaque pixel onto a metal
ramp, which overwrites the near-black face-slit that the base helmet (helmet_2 /
helmet_2_f) authors per-frame — leaving the character "blind" (solid metal over the
eyes). This restores the opening by copying the reference helmet's per-frame slit:

  * Build a per-frame mask of the near-black opaque pixels inside the face window
    of the gender-matched reference helmet (helmet_2 for male sheets, helmet_2_f
    for female sheets). This mask tracks the head through every pose exactly.
  * On the target sheet, repaint those masked pixels to near-black ONLY where the
    target is already opaque. No pixel is added outside the target silhouette, so
    the operation is QA-safe by construction (cannot create strays/bleed).

Reusable: import carve_eye_slit(target_rgba, gender) into a helmet generator and
call it as the final step, or run this file as a CLI to batch-fix existing sheets.

  # Fix specific sheets (gender inferred from _f suffix)
  python3 scripts/apply_helmet_eye_slit.py _visor_helmet_preview/helmet_warrior_legendary5.png ...

  # Dry-run report of carved-pixel counts
  python3 scripts/apply_helmet_eye_slit.py --dry-run FILE ...
"""
import os
import sys
import numpy as np
from PIL import Image

CH = "sprites/preview_assets/char"
FW, FH, COLS, NFR = 80, 64, 10, 70
# Face window (per 80x64 frame) where a slit legitimately lives. Wider than the
# eye band so full face-grilles (like helmet_2's) are captured.
FY0, FY1, FX0, FX1 = 23, 31, 31, 49
SLIT_RGB = (16, 14, 18)          # near-black slit interior
_REF_CACHE = {}


def _load(p):
    return np.array(Image.open(p).convert("RGBA"))


def _ref_mask(gender):
    """Per-frame boolean mask of the reference helmet's near-black face pixels."""
    key = 'f' if gender == 'f' else 'm'
    if key in _REF_CACHE:
        return _REF_CACHE[key]
    ref = _load(f"{CH}/helmet_2{'_f' if key == 'f' else ''}.png")
    m = np.zeros(ref.shape[:2], bool)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        fr = ref[sl]
        op = fr[..., 3] > 0
        lum = fr[..., :3].astype(int).sum(-1)
        win = np.zeros_like(op)
        win[FY0:FY1, FX0:FX1] = True
        m[sl] = op & win & (lum < 150)
    _REF_CACHE[key] = m
    return m


def carve_eye_slit(arr, gender='m'):
    """Return a copy of `arr` with the reference eye/face slit carved in (only over
    opaque target pixels). Safe to call as the final step of a helmet generator."""
    out = arr.copy()
    mask = _ref_mask(gender)
    if mask.shape != out.shape[:2]:
        raise ValueError("sheet size mismatch with reference helmet")
    apply = mask & (out[..., 3] > 0)
    out[apply, 0], out[apply, 1], out[apply, 2] = SLIT_RGB
    out[apply, 3] = 255
    return out, int(apply.sum())


def main(argv):
    dry = '--dry-run' in argv
    files = [a for a in argv if not a.startswith('--')]
    for f in files:
        gender = 'f' if f[:-4].endswith('_f') else 'm'
        arr = _load(f)
        fixed, n = carve_eye_slit(arr, gender)
        if dry:
            print(f"[dry] would carve {n:4d} px  ({gender})  {f}")
            continue
        Image.fromarray(fixed).save(f)
        print(f"carved {n:4d} px  ({gender})  {f}")


if __name__ == '__main__':
    main(sys.argv[1:])
