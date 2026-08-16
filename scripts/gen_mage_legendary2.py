#!/usr/bin/env python3
"""Generate the Mage 2nd legendary L25 set — "Ember Magus".

Follows gen_mage_legendary.py exactly (luminance-quantile color transfer of the
already-shaded mage t4 geometry, edges forced to black outline, interior mapped
by luminance quantile onto a distinctive ramp). Geometry/opacity untouched, so
all active frames + animation are preserved by construction.

Ramp is a molten fire family (deep ember -> molten orange -> pale gold-white),
clearly distinct from the mage tiers (purple/void) AND from the mage rare1
"Astral" set (cyan->ivory), so it reads as its own second legendary.

Outputs to _mage_legendary2_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_mage_legendary2_preview'
FW, FH = 80, 64

SLOTS = {
    'helmet': 'helmet_mage4',
    'shirt':  'shirt_mage4',
    'pants':  'pants_mage4',
    'boots':  'boots_mage4',
}

# Ember ramp, darkest -> lightest.
RAMP = np.array([
    (30, 8, 6),      # deep ember shadow
    (66, 16, 10),    # dark red
    (122, 28, 14),   # red
    (176, 52, 18),   # red-orange
    (216, 96, 26),   # orange
    (240, 150, 44),  # amber
    (250, 204, 96),  # gold
    (255, 244, 196), # pale gold-white highlight
], dtype=np.uint8)


def load(name):
    return np.array(Image.open(CHAR + name + '.png').convert('RGBA'))


def lum(rgb):
    rgb = rgb.astype(np.float64)
    return (3 * rgb[..., 0] + 6 * rgb[..., 1] + rgb[..., 2]) / 10.0


def edge_mask(P):
    pad = np.pad(P, 1)
    n4 = (pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:])
    return P & ~n4


def quantile_map(base):
    out = np.zeros_like(base)
    P = base[..., 3] > 10
    edges = np.zeros_like(P)
    for r in range(7):
        for c in range(10):
            sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
            edges[sl] = edge_mask(P[sl])
    interior = P & ~edges
    src_l = lum(base[interior][:, :3])
    ref = np.sort(src_l)
    q = np.searchsorted(ref, src_l, side='left') / max(1, len(ref) - 1)
    idx = np.clip((q * (len(RAMP) - 1)).round().astype(int), 0, len(RAMP) - 1)
    out[interior, :3] = RAMP[idx]
    out[interior, 3] = 255
    out[edges] = (0, 0, 0, 255)
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    for slot, base_name in SLOTS.items():
        for suf in ('', '_f'):
            base = load(base_name + suf)
            recol = quantile_map(base)
            assert np.array_equal(base[..., 3] > 10, recol[..., 3] > 10), \
                f'opacity mismatch {slot}{suf}'
            out_name = f'{slot}_rare_mage2{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
