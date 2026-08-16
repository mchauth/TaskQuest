#!/usr/bin/env python3
"""Generate the Warrior 5th legendary L25 set — "Emerald Vanguard".

Follows gen_warrior_legendary4.py exactly (luminance-quantile color transfer of
an already-shaded, QA-passed warrior legendary geometry, edges forced to black
outline, interior mapped by luminance quantile onto a distinctive ramp).
Geometry/opacity untouched, so all active frames + animation are preserved by
construction.

Source geometry: warrior rare1 (Crimson Sentinel) sheets — chosen because they
already ship full male + female coverage for all four slots (helmet/shirt/pants/
boots), so the new set inherits complete gender parity with no extra work.

Ramp is a saturated emerald-jade family (deep forest-emerald shadow -> emerald
-> jade -> pale mint glint). Warrior's four existing legendaries are Crimson
Sentinel (red+gold), Shadow Warden (near-black+teal), Solar Paladin (gold+ivory)
and Amethyst Warlord (royal purple). Warrior has NO green anywhere in its tiers
(leather-brown/studded-black/chainmail-grey/silver/gold/icy-diamond) OR in any
prior legendary, so Emerald reads clearly as its own fifth legendary. It is a
pure saturated green distinct from the electric-teal accent of Shadow Warden.

Outputs to _warrior_legendary5_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_warrior_legendary5_preview'
FW, FH = 80, 64

SLOTS = {
    'helmet': 'helmet_rare1',
    'shirt':  'shirt_rare1',
    'pants':  'pants_rare1',
    'boots':  'boots_rare1',
}

# Emerald Vanguard ramp, darkest -> lightest.
RAMP = np.array([
    (6, 26, 18),     # deep forest-emerald shadow
    (12, 46, 30),    # dark emerald
    (18, 72, 46),    # emerald shadow
    (24, 104, 64),   # emerald
    (36, 148, 90),   # bright emerald
    (78, 190, 128),  # jade
    (150, 224, 180), # pale jade
    (226, 250, 236), # near-white mint glint
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
            out_name = f'{slot}_rare5{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
