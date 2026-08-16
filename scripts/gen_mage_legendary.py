#!/usr/bin/env python3
"""Generate the Mage legendary L25 set — "Astral Magus".

Content gap: legendary (L25) sets existed only for the warrior class
(helmet/shirt/pants/boots rare1-3, both genders). Mage and ranger had no
legendary loot at all. This adds the first mage legendary set.

Method — luminance-quantile color transfer (same proven, QA-safe technique as
scripts/gen_female_rare_armor.py): take the already-shaded mage t4 geometry as
the silhouette source, force silhouette edges to pure black outline, and map
every interior pixel by its luminance quantile onto a distinctive ASTRAL ramp
(cosmic cyan -> starlight ivory). Geometry/opacity are untouched, so all 42
active frames and the animation are preserved by construction; QA is a
formality. Run scripts/sprite_shade.py afterwards for cosine relighting.

Palette is deliberately a cyan->white family, clearly distinct from the mage
tier armor (which is a purple/void family), so the legendary reads as its own
item rather than a recolored tier.

Outputs to _mage_legendary_preview/ (staged, not pushed).
"""
import os
import numpy as np
from PIL import Image

CHAR = 'sprites/preview_assets/char/'
OUT = '_mage_legendary_preview'
FW, FH = 80, 64

# Source geometry: mage t4 (L20 refined-plate robe) — closest tier to L25.
SLOTS = {
    'helmet': 'helmet_mage4',
    'shirt':  'shirt_mage4',
    'pants':  'pants_mage4',
    'boots':  'boots_mage4',
}

# Astral ramp, darkest -> lightest. Cosmic cyan into starlight ivory,
# with a warm gold glint at the very top band for a legendary highlight.
RAMP = np.array([
    (14, 22, 40),    # deep void-teal shadow
    (24, 44, 74),    # dark
    (40, 82, 116),   # mid-dark cyan
    (66, 128, 166),  # mid cyan
    (108, 178, 202), # light cyan
    (162, 214, 228), # pale ice
    (214, 240, 246), # near-white ice
    (248, 246, 226),  # warm starlight highlight (subtle gold)
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
            out_name = f'{slot}_rare_mage1{suf}.png'
            Image.fromarray(recol, 'RGBA').save(os.path.join(OUT, out_name))
            print(f'wrote {out_name}  (opaque_px={(recol[...,3]>10).sum()})')


if __name__ == '__main__':
    main()
