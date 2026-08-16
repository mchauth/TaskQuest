#!/usr/bin/env python3
"""Generate the Warrior 4th legendary L25 set — "Amethyst Warlord".

Follows gen_mage_legendary4.py exactly (luminance-quantile color transfer of an
already-shaded, QA-passed warrior legendary geometry, edges forced to black
outline, interior mapped by luminance quantile onto a distinctive ramp).
Geometry/opacity untouched, so all active frames + animation are preserved by
construction.

Source geometry: warrior rare1 (Crimson Sentinel) sheets — chosen because they
already ship full male + female coverage for all four slots (helmet/shirt/pants/
boots), so the new set inherits complete gender parity with no extra work.

Ramp is a rich royal-amethyst family (deep violet shadow -> royal purple ->
bright amethyst -> pale lilac glint). Warrior's three existing legendaries are
Crimson Sentinel (red+gold), Shadow Warden (near-black+teal), and Solar Paladin
(gold+ivory). Warrior has no purple anywhere in its tiers (leather/steel/gold/
icy-diamond), so Amethyst reads clearly as its own fourth legendary and is
distinct from the icy-blue t6 Diamond Plate.

Outputs to _warrior_legendary4_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_warrior_legendary4_preview'
FW, FH = 80, 64

# slot -> source geometry sheet (warrior rare1)
SLOTS = {
    'helmet': 'helmet_rare1',
    'shirt':  'shirt_rare1',
    'pants':  'pants_rare1',
    'boots':  'boots_rare1',
}

# Amethyst Warlord ramp, darkest -> lightest.
RAMP = np.array([
    (26, 10, 40),    # deep violet shadow
    (44, 16, 70),    # dark royal purple
    (68, 26, 108),   # royal purple
    (98, 42, 150),   # amethyst
    (134, 70, 196),  # bright amethyst
    (176, 116, 224), # light violet
    (210, 170, 240), # pale lilac
    (240, 226, 250), # near-white lilac glint
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
            out_name = f'{slot}_rare4{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
