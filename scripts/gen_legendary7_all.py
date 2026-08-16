#!/usr/bin/env python3
"""Generate the 7th legendary L25 set for all three classes.

Same QA-safe luminance-quantile color-transfer method as
gen_warrior_legendary6.py / gen_mage_legendary6.py / gen_ranger_legendary6.py:
edges forced to black outline, interior remapped by luminance quantile onto a
distinctive ramp. Geometry/opacity untouched, so all active frames + animation
are preserved by construction.

Source geometry per class (chosen for full male+female coverage):
  - warrior: rare1 (Crimson Sentinel) geometry
  - mage:    mage t4 geometry
  - ranger:  ranger t4 geometry

Ramps — each distinct from that class's tiers AND all six prior legendaries:
  - Warrior "Azure Sovereign": royal sapphire (deep navy -> cobalt -> azure ->
    pale sky). Warrior's only blue is the PALE icy-diamond t6; a saturated deep
    sapphire reads clearly as its own set. Distinct from all other warrior
    legendaries (red/teal/gold/purple/green/rose).
  - Mage "Gilded Magus": pure warm gold (deep bronze-brown -> amber-gold ->
    bright gold -> pale gold-white). Mage has NO yellow-gold set anywhere (prior
    are cyan/orange/red/green/rose-magenta/silver; tiers purple/void). Kept
    yellow-gold (not the red-orange of Ember rare2).
  - Ranger "Moonsilver Warden": neutral silver/platinum (deep slate -> grey ->
    silver -> platinum -> white). Ranger has no neutral silver; distinct from the
    steel-BLUE Frosthunter (kept neutral grey, zero blue cast) and from all other
    ranger legendaries (green/teal/violet/amber/red).

Outputs to _{class}_legendary7_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
FW, FH = 80, 64

SETS = {
    'warrior': {
        'out': '_warrior_legendary7_preview',
        'suffix': 'rare7',
        'slots': {'helmet': 'helmet_rare1', 'shirt': 'shirt_rare1',
                  'pants': 'pants_rare1', 'boots': 'boots_rare1'},
        'ramp': [
            (10, 16, 40),    # deep navy shadow
            (18, 30, 68),    # navy
            (28, 48, 104),   # deep cobalt
            (40, 72, 150),   # cobalt
            (58, 104, 196),  # royal blue
            (90, 146, 226),  # azure
            (140, 186, 240), # bright azure
            (206, 228, 250), # pale sky glint
        ],
    },
    'mage': {
        'out': '_mage_legendary7_preview',
        'suffix': 'rare_mage7',
        'slots': {'helmet': 'helmet_mage4', 'shirt': 'shirt_mage4',
                  'pants': 'pants_mage4', 'boots': 'boots_mage4'},
        'ramp': [
            (40, 24, 6),     # deep bronze-brown shadow
            (72, 46, 12),    # dark bronze
            (110, 74, 18),   # antique gold
            (150, 108, 26),  # amber-gold
            (190, 146, 36),  # gold
            (222, 182, 60),  # bright gold
            (242, 214, 118), # pale gold
            (252, 240, 200), # pale gold-white glint
        ],
    },
    'ranger': {
        'out': '_ranger_legendary7_preview',
        'suffix': 'rare_ranger7',
        'slots': {'helmet': 'helmet_ranger4', 'shirt': 'shirt_ranger4',
                  'pants': 'pants_ranger4', 'boots': 'boots_ranger4'},
        'ramp': [
            (26, 28, 32),    # deep slate shadow
            (48, 52, 58),    # slate
            (78, 84, 92),    # grey
            (112, 120, 130), # cool grey
            (148, 156, 166), # silver-grey
            (184, 192, 202), # silver
            (216, 222, 230), # platinum
            (244, 248, 252), # white glint
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
