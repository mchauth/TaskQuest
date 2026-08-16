#!/usr/bin/env python3
"""Generate a net-new-geometry HYPER-RARE legendary mage helmet —
"Starweaver's Crown" (helmet_mage_legendary1 + _f).

Mage counterpart to the warrior "Wyrmhorn Warhelm": same authoring philosophy
as gen_horned_legendary_helm.py — build per-frame from an existing mage helmet
silhouette (helmet_mage4[.png/_f]) so every pose/animation is tracked, then draw
NET-NEW accent geometry anchored to per-frame skull-dome metrics (head_top, cx).
Instead of bone dragon horns this draws an arcane CROWN: three upswept crystal
SPIRES (a tall central prong + two outward-leaning flanking prongs, mirrored)
each capped by a bright star point. This goes beyond a palette recolor and pairs
with the already-staged mage winged chest ("Starweaver's Wings").

Spires are drawn ONLY in out-of-silhouette space above the helm. Each side spire
is root-bridged to the helm's ACTUAL per-row edge and the central spire is rooted
straight down onto the helm top, so helm+all-three-spires is a single connected
component (QA-safe). Crystal is rigid, so — like the horns and unlike the wings —
the spires simply track the head per frame (no flutter). Helmets have no sleep
frames (42 active); empty frames are skipped.

Body recolor: helmet V quantized into the SAME cosmic 3-tone ramp as the mage
wings (deep indigo -> arcane violet -> pale starlight) so the crown reads as one
set with the chest and the pale crystal spires pop. Shading applied in-script via
shade(); do NOT run sprite_shade.py again on the output.

Run from repo root:
  python3 scripts/gen_mage_crown_legendary.py
Then QA (note: spires intentionally extend outside the normal helm silhouette):
  python3 scripts/sprite_qa.py \
    _mage_crown_legendary_preview/helmet_mage_legendary1.png --y-min 2
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade          # noqa: E402
from rebuild_class_hats import make_head_dome_fn        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Cosmic mage body ramp (shadow / base / highlight) -- matches the mage wings
D = (46, 34, 96)       # deep indigo shadow
M = (96, 74, 190)      # arcane violet base
L = (196, 186, 250)    # pale starlight highlight

# Arcane crystal spire palette (light -> vane -> trailing) + outer edge, matches
# the wing accent family so the crown and wings read as one arcane set.
CR_L = (224, 246, 255)   # cyan-white lit face
CR_M = (150, 176, 244)   # nebula-blue body
CR_D = (110, 120, 214)   # violet trailing / facet line
CR_ED = (72, 70, 150)    # outer outline
STAR = (236, 244, 255)   # bright star point at each spire tip
ROOT = (150, 176, 250)   # dim arcane at the spire root

# Crown-fan profile: dy (rows ABOVE the brim-corner anchor) -> outward reach.
# A crystalline fan that flares up-and-outward from each brim corner, framing
# the wizard hat like a pair of crystal wings, then tapers to a star tip. The
# fan is built exactly like the proven seraph ankle-wing (off=1..outer each
# row, off=1 column continuous) so it stays 4-connected to the hat by
# construction — no floating components.
FAN = {0: 2, 1: 3, 2: 4, 3: 5, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def fan_tone(dy, off, outer, is_tip):
    """Colour a crown-fan pixel: bright star at the fan tip, outline on the
    outer edge, lit inner face, violet facet lines on alternating rows."""
    if is_tip:
        return STAR
    if off >= outer:
        rgb = CR_ED
    elif off >= outer - 1:
        rgb = CR_D
    elif off <= 1:
        rgb = CR_L
    else:
        rgb = CR_M
    if dy % 2 == 1 and off >= outer - 2 and rgb == CR_M:
        rgb = CR_D
    return rgb


def corner_anchor(a, sign):
    """Return (edge_x, anchor_y) at the outer brim corner for the given side:
    the outermost opaque column and the topmost row that reaches it. The fan's
    off=1 base pixel is edge-adjacent to this opaque pixel, guaranteeing the
    whole fan is 4-connected to the hat."""
    ys, xs = np.where(a)
    edge_x = int(xs.min()) if sign < 0 else int(xs.max())
    rows = ys[xs == edge_x]
    anchor_y = int(rows.min())
    return edge_x, anchor_y


def draw_fan(fr, a, edge_x, anchor_y, sign):
    """One crystal crown-fan flaring up-and-outward from a brim corner."""
    dymax = max(FAN)
    for dy, outer in FAN.items():
        y = anchor_y - dy
        for off in range(1, outer + 1):
            x = edge_x + sign * off
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if a[y, x]:                 # never overpaint the hat
                continue
            is_tip = (dy == dymax and off == outer)
            put(fr, y, x, fan_tone(dy, off, outer, is_tip))


def build(base, dome):
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue                        # empty / sleep frame -> skip
        fr = out[sl]

        # 1. quantized cosmic recolor of the helm silhouette
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            put(fr, y, x, tone)

        # 2. crown crystal-fans (hat already drawn underneath). Each fan flares
        # up-and-outward from a brim corner and is 4-connected to the hat by
        # construction (off=1 base pixel edge-adjacent to the opaque corner).
        for sign in (-1, +1):
            edge_x, anchor_y = corner_anchor(a, sign)
            draw_fan(fr, a, edge_x, anchor_y, sign)
    return out


def main():
    os.makedirs('_mage_crown_legendary_preview', exist_ok=True)
    for suffix, skin in (('', 'skin_m1.png'), ('_f', 'skin_f1.png')):
        base = load('helmet_mage4%s.png' % suffix)
        skin_sheet = load(skin)
        dome = make_head_dome_fn(skin_sheet)
        arr = build(base, dome)
        arr = shade(arr, adj_min=-0.16, adj_max=0.24)
        dst = '_mage_crown_legendary_preview/helmet_mage_legendary1%s.png' % suffix
        Image.fromarray(arr).save(dst)
        print('wrote %s  (opaque_px=%d)' % (dst, int((arr[..., 3] > 0).sum())))


if __name__ == '__main__':
    main()
