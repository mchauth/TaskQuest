#!/usr/bin/env python3
"""Generate the Ranger 5th legendary L25 set — "Emberwild Warden".

Follows gen_ranger_legendary4.py exactly (luminance-quantile color transfer of
the ranger t4 geometry, edges forced to black outline, interior mapped by
luminance quantile onto a distinctive ramp). Geometry/opacity untouched, so all
active frames + animation are preserved by construction.

Source geometry: ranger t4 sheets (helmet_ranger4 etc.) — same source as the
four prior ranger legendaries.

Ramp is a warm autumn amber-copper family (deep umber shadow -> burnt sienna ->
copper-orange -> amber -> pale gold glint). Ranger's four existing legendaries
are Verdant (emerald-gold), Frosthunter (steel-blue), Tideglass (teal) and
Nightbloom (violet-magenta). Ranger's tiers are all dark green; there is no warm
orange/amber anywhere in the class, so Emberwild reads clearly as its own fifth
legendary and is distinct from Verdant's green-dominant gold.

Outputs to _ranger_legendary5_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_ranger_legendary5_preview'
FW, FH = 80, 64

SLOTS = {
    'helmet': 'helmet_ranger4',
    'shirt':  'shirt_ranger4',
    'pants':  'pants_ranger4',
    'boots':  'boots_ranger4',
}

# Emberwild ramp, darkest -> lightest.
RAMP = np.array([
    (30, 12, 4),     # deep umber shadow
    (58, 22, 8),     # dark brown-ember
    (96, 38, 12),    # burnt sienna
    (140, 60, 18),   # copper-brown
    (188, 92, 24),   # copper-orange
    (222, 132, 40),  # amber-orange
    (240, 180, 82),  # amber
    (252, 226, 168), # pale gold glint
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
            out_name = f'{slot}_rare_ranger5{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
