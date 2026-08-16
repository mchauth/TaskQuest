#!/usr/bin/env python3
"""Generate a net-new-geometry HYPER-RARE legendary ranger helmet —
"Skyhunter's Plumed Hood" (helmet_ranger_legendary1 + _f).

Ranger counterpart to the warrior "Wyrmhorn Warhelm" and mage "Starweaver's
Crown": same authoring philosophy as gen_mage_crown_legendary.py — build
per-frame from an existing ranger helmet silhouette (helmet_ranger4[.png/_f]) so
every pose/animation is tracked, then draw NET-NEW accent geometry anchored to
the silhouette's own per-frame brim corners. Instead of the mage's arcane
crystal crown-fans this draws a pair of swept-back HAWK-FEATHER PLUMES that
flare up-and-outward from the hood's two brim corners — a grounded bird-of-prey
motif that matches the ranger "Skyhunter's Wings" chest, NOT a celestial/arcane
crown. This goes beyond a palette recolor and completes the ranger 4-slot
net-new-geometry showcase alongside the winged chest.

Each plume-fan is built exactly like the proven seraph ankle-wing / mage
crown-fan (off=1..outer each row, a continuous off=1 column) so it is
4-connected to the hood by construction — no floating components. Plumes are
drawn ONLY in out-of-silhouette space above the hood. Feathers are rigid, so —
like the horns and unlike the wings — the plumes simply track the head per frame
(no flutter). Helmets have no sleep frames (42 active); empty frames skipped.

Body recolor: helmet V quantized into the SAME forest->emerald->bronze ramp as
the ranger wings so the hood reads as one set with the chest and the cream/
russet plumes pop. Shading applied in-script via shade(); do NOT run
sprite_shade.py again on the output.

Run from repo root:
  python3 scripts/gen_ranger_crown_legendary.py
Then QA (plumes intentionally extend outside the normal helm silhouette, so a
background-bleed flag on the plume columns is expected -- that IS the legendary
silhouette, not strays):
  python3 scripts/sprite_qa.py \
    _ranger_crown_legendary_preview/helmet_ranger_legendary1.png --y-min 2
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Ranger legendary body ramp (shadow / base / highlight) -- matches the wings.
D = (22, 46, 28)       # deep forest shadow
M = (58, 120, 66)      # living emerald base
L = (206, 196, 128)    # pale bronze-gold highlight

# Hawk-plumage feather palette (leading light -> vane -> trailing) + outer edge,
# matches the ranger wing accent family so the hood and wings read as one set.
FE_L = (238, 224, 190)   # cream leading edge (feather tips catch light)
FE_M = (166, 116, 70)    # russet-brown body
FE_D = (104, 68, 42)     # dark-brown trailing / facet line
FE_ED = (58, 38, 26)     # outer outline
TIP = (246, 236, 208)    # bright feather tip at each plume point

# Plume-fan profile: dy (rows ABOVE the brim-corner anchor) -> outward reach.
# A hawk-feather fan that flares up-and-outward from each brim corner, framing
# the hood like a pair of raptor crest-feathers, tapering to a swept tip. Built
# like the proven seraph ankle-wing (off=1..outer each row, off=1 column
# continuous) so it stays 4-connected to the hood by construction.
FAN = {0: 2, 1: 3, 2: 4, 3: 5, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def fan_tone(dy, off, outer, is_tip):
    """Colour a plume-fan pixel: bright tip at the fan point, outline on the
    outer edge, cream inner leading edge, russet body, dark facet lines."""
    if is_tip:
        return TIP
    if off >= outer:
        rgb = FE_ED
    elif off >= outer - 1:
        rgb = FE_D
    elif off <= 1:
        rgb = FE_L
    else:
        rgb = FE_M
    if dy % 2 == 1 and off >= outer - 2 and rgb == FE_M:
        rgb = FE_D
    return rgb


def corner_anchor(a, sign):
    """Return (edge_x, anchor_y) at the outer brim corner for the given side:
    the outermost opaque column and the topmost row that reaches it. The fan's
    off=1 base pixel is edge-adjacent to this opaque pixel, guaranteeing the
    whole fan is 4-connected to the hood."""
    ys, xs = np.where(a)
    edge_x = int(xs.min()) if sign < 0 else int(xs.max())
    rows = ys[xs == edge_x]
    anchor_y = int(rows.min())
    return edge_x, anchor_y


def draw_fan(fr, a, edge_x, anchor_y, sign):
    """One hawk-plume fan flaring up-and-outward from a brim corner."""
    dymax = max(FAN)
    for dy, outer in FAN.items():
        y = anchor_y - dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                 # never overpaint the hood
                continue
            is_tip = (dy == dymax and off == outer)
            put(fr, y, x, fan_tone(dy, off, outer, is_tip))


def build(base):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue                        # empty / sleep frame -> skip
        fr = out[sl]

        # 1. quantized ranger-family recolor of the hood silhouette
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            put(fr, y, x, tone)

        # 2. hawk-plume fans (hood already drawn underneath). Each fan flares
        # up-and-outward from a brim corner and is 4-connected to the hood by
        # construction (off=1 base pixel edge-adjacent to the opaque corner).
        for sign in (-1, +1):
            edge_x, anchor_y = corner_anchor(a, sign)
            draw_fan(fr, a, edge_x, anchor_y, sign)
    return out


def main():
    os.makedirs('_ranger_crown_legendary_preview', exist_ok=True)
    for suffix in ('', '_f'):
        base = load('helmet_ranger4%s.png' % suffix)
        arr = build(base)
        arr = shade(arr, adj_min=-0.16, adj_max=0.24)
        dst = '_ranger_crown_legendary_preview/helmet_ranger_legendary1%s.png' % suffix
        Image.fromarray(arr).save(dst)
        print('wrote %s  (opaque_px=%d)' % (dst, int((arr[..., 3] > 0).sum())))


if __name__ == '__main__':
    main()
