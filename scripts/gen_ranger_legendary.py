#!/usr/bin/env python3
"""Generate the Ranger legendary L25 set — "Verdant Monarch".

Content gap: legendary (L25) loot existed for warrior (rare1-3) and, as of
2026-07-23, mage ("Astral Magus"). Ranger still had NO legendary set. This adds
the first ranger legendary, giving every class a legendary tier and mirroring
the warrior/mage structure.

Method — luminance-quantile color transfer (same proven, QA-safe technique as
scripts/gen_mage_legendary.py / gen_female_rare_armor.py): take the already-
shaded ranger t4 geometry as the silhouette source, force silhouette edges to
pure black outline, and map every interior pixel by its luminance quantile onto
a distinctive VERDANT->GOLD ramp. Geometry/opacity are untouched, so all active
frames and the animation are preserved by construction; QA is a formality. Run
scripts/sprite_shade.py afterwards for cosine relighting.

Palette is a bright, glowing emerald->radiant-gold family. The ranger armor
tiers are a muted, ever-darkening green family (t6 near-void). This legendary is
deliberately luminous and gold-crowned so it reads as its own item, not a
recolored tier.

Outputs to _ranger_legendary_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_ranger_legendary_preview'
FW, FH = 80, 64

# Source geometry: ranger t4 (L20 refined tier) — closest tier to L25.
SLOTS = {
    'helmet': 'helmet_ranger4',
    'shirt':  'shirt_ranger4',
    'pants':  'pants_ranger4',
    'boots':  'boots_ranger4',
}

# Verdant Monarch ramp, darkest -> lightest. Deep forest shadow through living
# emerald into a radiant chartreuse-gold crown highlight. Clearly distinct from
# the ranger tiers' dark, desaturated greens.
RAMP = np.array([
    (16, 30, 20),    # deep forest shadow
    (24, 58, 34),    # dark emerald
    (34, 96, 52),    # emerald
    (52, 140, 70),   # bright emerald
    (96, 176, 84),   # leaf green
    (170, 206, 96),  # chartreuse / gold-green
    (226, 224, 130), # pale gold
    (250, 240, 168), # radiant gold highlight
], dtype=np.uint8)


def load(name):
    return np.array(Image.open(CHAR + name + '.png').convert('RGBA'))


def lum(rgb):
    rgb = rgb.astype(np.float64)
    return (3 * rgb[..., 0] + 6 * rgb[..., 1] + rgb[..., 2]) / 10.0


def edge_mask(P):
    """Pixels with any transparent 4-neighbour (or frame border) = silhouette edge."""
    pad = np.pad(P, 1)
    n4 = (pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:])
    return P & ~n4


def quantile_map(base):
    """Recolor: edges -> black outline; interior -> ramp by luminance quantile."""
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
            # sanity: opacity must match source exactly (geometry preserved)
            assert np.array_equal(base[..., 3] > 10, recol[..., 3] > 10), \
                f'opacity mismatch {slot}{suf}'
            out_name = f'{slot}_rare_ranger1{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
