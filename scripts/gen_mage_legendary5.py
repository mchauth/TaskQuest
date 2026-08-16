#!/usr/bin/env python3
"""Generate the Mage 5th legendary L25 set — "Rosethorn Magus".

Follows gen_mage_legendary4.py exactly (luminance-quantile color transfer of the
mage t4 geometry, edges forced to black outline, interior mapped by luminance
quantile onto a distinctive ramp). Geometry/opacity untouched, so all active
frames + animation are preserved by construction.

Source geometry: mage t4 sheets (helmet_mage4 etc.) — same source as the four
prior mage legendaries.

Ramp is a saturated rose-magenta family (deep wine shadow -> magenta -> hot pink
-> pale blush glint). Mage's four existing legendaries are Astral (cyan), Ember
(orange), Bloodmoon (pure red) and Malachite (green). Mage's tiers are all
purple/void. A hot pink-magenta is distinct from the purple tiers (it is pink,
not violet), from Bloodmoon's pure red (it carries strong blue/magenta, reading
clearly pink), and from every other legendary. Reads as its own fifth set.

Outputs to _mage_legendary5_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_mage_legendary5_preview'
FW, FH = 80, 64

SLOTS = {
    'helmet': 'helmet_mage4',
    'shirt':  'shirt_mage4',
    'pants':  'pants_mage4',
    'boots':  'boots_mage4',
}

# Rosethorn ramp, darkest -> lightest.
RAMP = np.array([
    (34, 6, 24),     # deep wine shadow
    (62, 10, 42),    # dark rose
    (98, 16, 68),    # wine-magenta
    (146, 24, 100),  # magenta
    (196, 40, 130),  # bright magenta
    (228, 82, 158),  # hot pink
    (244, 150, 194), # pink
    (252, 216, 232), # pale blush glint
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
            out_name = f'{slot}_rare_mage5{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
