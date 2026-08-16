#!/usr/bin/env python3
"""Generate the 8th legendary L25 set for all three classes.

Same QA-safe luminance-quantile color-transfer method as
gen_legendary7_all.py: edges forced to black outline, interior remapped by
luminance quantile onto a distinctive ramp. Geometry/opacity untouched, so all
active frames + animation are preserved by construction.

Source geometry per class (chosen for full male+female coverage):
  - warrior: rare1 (Crimson Sentinel) geometry
  - mage:    mage t4 geometry
  - ranger:  ranger t4 geometry

Ramps — each distinct from that class's tiers AND all seven prior legendaries:
  - Warrior "Molten Sovereign": copper-orange (deep umber -> burnt sienna ->
    copper -> burnt orange -> bright amber -> pale gold glint). Warrior has NO
    orange/copper anywhere (tiers leather-brown/steel/gold/icy-diamond; prior
    legendaries red/teal/gold/purple/green/rose/sapphire). Kept strongly orange
    so it is distinct from the yellow-gold Solar Paladin rare3.
  - Mage "Sapphire Magus": deep royal sapphire (deep navy -> cobalt -> royal
    blue -> azure -> pale sky). Mage's only blue-ish set is the saturated CYAN
    Astral rare1; a deep royal sapphire reads clearly as its own set. Tiers are
    purple/void, so sapphire is distinct there too.
  - Ranger "Rosewild Warden": rose-pink (deep wine -> dark rose -> rose -> hot
    pink -> pale blush). Ranger has NO pink anywhere (tiers dark green; prior
    legendaries green/teal/steel-blue/violet/amber/red/silver). Kept warm pink
    (strong magenta cast) so distinct from the pure-red Crimson rare6 and the
    violet Nightbloom rare4.

Outputs to _{class}_legendary8_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
FW, FH = 80, 64

SETS = {
    'warrior': {
        'out': '_warrior_legendary8_preview',
        'suffix': 'rare8',
        'slots': {'helmet': 'helmet_rare1', 'shirt': 'shirt_rare1',
                  'pants': 'pants_rare1', 'boots': 'boots_rare1'},
        'ramp': [
            (28, 12, 4),     # deep umber shadow
            (60, 24, 8),     # dark brown-red
            (102, 44, 10),   # burnt sienna
            (150, 70, 14),   # copper-brown
            (196, 100, 20),  # burnt orange
            (228, 134, 36),  # copper-orange
            (244, 176, 80),  # bright amber
            (252, 220, 150), # pale gold glint
        ],
    },
    'mage': {
        'out': '_mage_legendary8_preview',
        'suffix': 'rare_mage8',
        'slots': {'helmet': 'helmet_mage4', 'shirt': 'shirt_mage4',
                  'pants': 'pants_mage4', 'boots': 'boots_mage4'},
        'ramp': [
            (8, 14, 42),     # deep navy shadow
            (14, 26, 74),    # navy
            (22, 44, 116),   # deep cobalt
            (32, 68, 166),   # cobalt
            (48, 100, 210),  # royal blue
            (80, 140, 234),  # bright blue
            (140, 186, 244), # azure
            (210, 230, 252), # pale sky glint
        ],
    },
    'ranger': {
        'out': '_ranger_legendary8_preview',
        'suffix': 'rare_ranger8',
        'slots': {'helmet': 'helmet_ranger4', 'shirt': 'shirt_ranger4',
                  'pants': 'pants_ranger4', 'boots': 'boots_ranger4'},
        'ramp': [
            (44, 10, 26),    # deep wine shadow
            (82, 16, 48),    # wine
            (126, 24, 72),   # dark rose
            (170, 36, 100),  # rose
            (210, 60, 130),  # pink-rose
            (232, 100, 160), # hot pink
            (244, 150, 194), # light pink
            (252, 206, 226), # pale blush glint
        ],
    },
}


def load(name):
    return np.array(Image.open(CHAR + name + '.png').convert('RGBA'))


def lum(rgb):
    rgb = rgb.astype(np.float64)
    return (3 * rgb[..., 0] + 6 * rgb[..., 1] + rgb[..., 2]) / 10.0


def edge_mask(P):
    pad = np.pad(P, 1)
    n4 = (pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:])
    return P & ~n4


def quantile_map(base, ramp):
    ramp = np.array(ramp, dtype=np.uint8)
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
    idx = np.clip((q * (len(ramp) - 1)).round().astype(int), 0, len(ramp) - 1)
    out[interior, :3] = ramp[idx]
    out[interior, 3] = 255
    out[edges] = (0, 0, 0, 255)
    return out


def main():
    for cls, cfg in SETS.items():
        os.makedirs(cfg['out'], exist_ok=True)
        for slot, base_name in cfg['slots'].items():
            for suf in ('', '_f'):
                base = load(base_name + suf)
                recol = quantile_map(base, cfg['ramp'])
                assert np.array_equal(base[..., 3] > 10, recol[..., 3] > 10), \
                    f'opacity mismatch {cls} {slot}{suf}'
                out_name = f'{slot}_{cfg["suffix"]}{suf}.png'
                Image.fromarray(recol, 'RGBA').save(
                    os.path.join(cfg['out'], out_name))
                print(f'[{cls}] wrote {out_name}  '
                      f'(opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
