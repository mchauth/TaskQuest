#!/usr/bin/env python3
"""Generate the Ranger 6th legendary L25 set — "Crimson Warden".

Follows gen_ranger_legendary5.py exactly (luminance-quantile color transfer of
the ranger t4 geometry, edges forced to black outline, interior mapped by
luminance quantile onto a distinctive ramp). Geometry/opacity untouched, so all
active frames + animation are preserved by construction.

Source geometry: ranger t4 sheets (helmet/shirt/pants/boots, male + female).

Ramp is a saturated ruby/crimson family (deep maroon shadow -> blood red ->
crimson -> scarlet -> pale rose glint). Ranger's five existing legendaries are
Verdant (emerald-gold), Frosthunter (steel-blue), Tideglass (teal), Nightbloom
(violet) and Emberwild (amber-copper), and its tiers are all dark green. Ranger
has NO pure red anywhere, so Crimson reads clearly as its own sixth legendary and
is distinct from the warm-orange Emberwild set (Crimson stays pure red, no
orange).

Outputs to _ranger_legendary6_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_ranger_legendary6_preview'
FW, FH = 80, 64

SLOTS = {
    'helmet': 'helmet_ranger4',
    'shirt':  'shirt_ranger4',
    'pants':  'pants_ranger4',
    'boots':  'boots_ranger4',
}

# Crimson Warden ramp, darkest -> lightest.
RAMP = np.array([
    (32, 6, 10),     # deep maroon shadow
    (60, 10, 16),    # dark blood
    (98, 16, 24),    # blood red
    (144, 24, 32),   # crimson shadow
    (190, 34, 42),   # crimson
    (222, 66, 66),   # scarlet
    (240, 128, 122), # coral-red
    (252, 208, 202), # pale rose glint
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
            out_name = f'{slot}_rare_ranger6{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
