#!/usr/bin/env python3
"""Generate the Mage 3rd legendary L25 set — "Bloodmoon Magus".

Follows gen_mage_legendary.py / _legendary2.py exactly (luminance-quantile color
transfer of the already-shaded mage t4 geometry, edges forced to black outline,
interior mapped by luminance quantile onto a distinctive ramp). Geometry/opacity
untouched, so all active frames + animation are preserved by construction.

Ramp is a blood-crimson family (deep blood shadow -> scarlet -> pale rose-white),
clearly distinct from the mage tiers (purple/void), the mage rare1 "Astral" set
(cyan->ivory) AND the mage rare2 "Ember" set (orange-dominant amber->gold): this
one stays pure red/scarlet with no orange, so it reads as its own third legendary.

Outputs to _mage_legendary3_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_mage_legendary3_preview'
FW, FH = 80, 64

SLOTS = {
    'helmet': 'helmet_mage4',
    'shirt':  'shirt_mage4',
    'pants':  'pants_mage4',
    'boots':  'boots_mage4',
}

# Bloodmoon ramp, darkest -> lightest. Pure red/scarlet -> pale rose-white.
RAMP = np.array([
    (24, 4, 8),      # deep blood shadow
    (58, 8, 16),     # dark maroon
    (104, 14, 24),   # maroon
    (150, 22, 32),   # crimson
    (194, 40, 48),   # scarlet
    (224, 78, 84),   # rose-red
    (240, 140, 148), # pale rose
    (255, 224, 228), # pale pink-white highlight
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
            out_name = f'{slot}_rare_mage3{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
