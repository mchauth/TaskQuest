#!/usr/bin/env python3
"""Generate the 9th legendary L25 set for all three classes.

Same QA-safe luminance-quantile color-transfer method as
gen_legendary8_all.py: edges forced to black outline, interior remapped by
luminance quantile onto a distinctive ramp. Geometry/opacity untouched, so all
active frames + animation are preserved by construction.

Source geometry per class (chosen for full male+female coverage):
  - warrior: rare1 (Crimson Sentinel) geometry
  - mage:    mage t4 geometry
  - ranger:  ranger t4 geometry

Ramps — each distinct from that class's tiers AND all eight prior legendaries.
Eight sets have used the easy hues, so #9 deliberately reaches for the clearest
remaining gaps per class:
  - Warrior "Tidewarden Sovereign": teal / turquoise (deep teal -> turquoise ->
    aqua -> pale mint glint). Warrior has NO full teal/turquoise body anywhere:
    tiers are leather-brown/steel/chainmail/silver/gold/icy-diamond, and the
    only teal in the legendaries is a THIN accent on the near-black Shadow
    Warden (rare2). A saturated all-turquoise body reads clearly as its own set
    and is distinct from the green Emerald rare5 (no blue) and the blue Azure
    rare7 (no green).
  - Mage "Celestial Magus": radiant opal / pearl-white (deep slate-lilac ->
    soft lavender-grey -> warm ivory -> pure white glint). Mage has no
    white/pearl set: prior legendaries are cyan/orange/red/green/rose-magenta/
    silver/gold/sapphire and the tiers are purple/void. Kept warm-ivory-white
    (not the cool STEEL-blue of Mithril rare6) so it reads as luminous pearl,
    distinct from Mithril's metallic grey.
  - Ranger "Sunspear Warden": pure warm gold / yellow (deep bronze-brown ->
    antique gold -> amber-gold -> bright yellow-gold -> pale gold-white).
    Ranger has no yellow-gold set: tiers are dark green; prior legendaries are
    green/steel-blue/teal/violet/copper-amber/red/silver/pink. Kept a clean
    YELLOW-gold, distinct from the copper-ORANGE Emberwild rare5 (which is warm
    but orange-brown, not yellow) and the neutral-silver Moonsilver rare7.

Outputs to _{class}_legendary9_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
FW, FH = 80, 64

SETS = {
    'warrior': {
        'out': '_warrior_legendary9_preview',
        'suffix': 'rare9',
        'slots': {'helmet': 'helmet_rare1', 'shirt': 'shirt_rare1',
                  'pants': 'pants_rare1', 'boots': 'boots_rare1'},
        'ramp': [
            (4, 30, 34),     # deep teal shadow
            (8, 52, 58),     # dark teal
            (12, 82, 90),    # teal
            (16, 116, 126),  # bright teal
            (24, 152, 160),  # turquoise
            (46, 188, 190),  # aqua-turquoise
            (120, 218, 214), # aqua
            (206, 244, 240), # pale mint glint
        ],
    },
    'mage': {
        'out': '_mage_legendary9_preview',
        'suffix': 'rare_mage9',
        'slots': {'helmet': 'helmet_mage4', 'shirt': 'shirt_mage4',
                  'pants': 'pants_mage4', 'boots': 'boots_mage4'},
        'ramp': [
            (56, 52, 78),    # deep slate-lilac shadow
            (86, 82, 112),   # slate-lilac
            (120, 116, 146), # muted lavender-grey
            (156, 152, 178), # soft lavender-grey
            (192, 188, 206), # pale lilac
            (222, 218, 224), # warm pearl
            (240, 238, 234), # warm ivory
            (253, 252, 250), # pure white glint
        ],
    },
    'ranger': {
        'out': '_ranger_legendary9_preview',
        'suffix': 'rare_ranger9',
        'slots': {'helmet': 'helmet_ranger4', 'shirt': 'shirt_ranger4',
                  'pants': 'pants_ranger4', 'boots': 'boots_ranger4'},
        'ramp': [
            (48, 30, 6),     # deep bronze-brown shadow
            (84, 54, 10),    # bronze
            (124, 84, 14),   # antique gold
            (166, 118, 20),  # amber-gold
            (206, 156, 28),  # gold
            (234, 190, 44),  # bright yellow-gold
            (246, 216, 96),  # light gold
            (252, 238, 170), # pale gold-white glint
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
