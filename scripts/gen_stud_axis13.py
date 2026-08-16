#!/usr/bin/env python3
"""THIRTEENTH net-new-geometry axis for ALL FOUR SLOTS — the STUDWORK / BRIGANDINE
family: a regular GRID of discrete rivet-studs (raised pips) tiled across the piece.
This is the repeated-POINT-GRID surface axis that none of the twelve existing
legendary axes per slot occupy. Where the 11th/12th axes laid CONTINUOUS parallel
lines (vertical fluting / horizontal lamellar bands), this lays a field of DISCRETE
raised points — a distinct geometric primitive.

Per slot it lands as the 13th distinct axis, avoiding that slot's prior repeats:
  * CHEST  — a brigandine coat: gilt rivet grid across the whole cuirass. Distinct
             from the single roundel boss (8th), the vertical flutes (11th), and the
             horizontal lamellar bands (12th): those are one-boss / parallel-lines,
             this is a full point-grid.
  * LEGS   — studded cuisses: rivet grid on the thighs. Distinct from every leg axis
             (stripes, bands, plates, garters) — none are a point-grid.
  * BOOTS  — hobnailed warboots: a grid of hobnail studs. Distinct from the vertical
             rivet-shaft SEAM (11th, a single continuous line) — this is a stud field.
  * HELMET — studded dome: rivet grid over the whole crown. Distinct from the
             rivet-RIM (10th, a single brow ring) — this covers the whole dome.

Authoring philosophy is identical to gen_lamellar_legendary.py / gen_flute_legendary.py:
stud pixels are painted ONLY onto pixels that are ALREADY opaque body pixels. Because
it never adds a pixel outside the existing silhouette it CANNOT create isolated pixels,
background bleed, or accent-caused multi-component frames — QA-safe purely by
construction. Sleep frames (fi>=60, lying down) get the recolor only — no studs.
Shading applied in-script via shade(); do NOT run sprite_shade.py again.

Per class the stud cap is the class accent family:
  * warrior — obsidian/steel body + GOLD rivet cap, dark-bronze shadow
  * mage    — arcane-violet body + CYAN rivet cap, deep-indigo shadow
  * ranger  — forest body + COPPER rivet cap, dark-bark shadow

Run from repo root:
  python3 scripts/gen_stud_axis13.py
Then QA (examples):
  python3 scripts/sprite_qa.py _brigandine_legendary_preview/shirt_warrior_legendary13.png
  python3 scripts/sprite_qa.py _studdome_helmet_preview/helmet_mage_legendary13.png --y-min 2
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR          # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18
MIN_PX = 12

# Per-class stud palettes: (CAP bright dome, SHADOW dark under-pixel).
STUD = {
    'warrior': ((232, 190, 70), (92, 66, 20)),      # gold cap, dark-bronze shadow
    'mage':    ((96, 210, 244), (30, 26, 84)),      # cyan cap, deep-indigo shadow
    'ranger':  ((206, 132, 66), (40, 28, 16)),      # copper cap, dark-bark shadow
}

# Per-class body tones: deep shadow / base / highlight.
BODY = {
    'warrior': ((28, 30, 36), (74, 78, 90), (128, 134, 150)),   # obsidian -> steel
    'mage':    ((20, 16, 54), (54, 42, 122), (120, 96, 200)),   # arcane violet
    'ranger':  ((20, 40, 18), (48, 88, 42), (98, 150, 82)),     # forest green
}

# One config block per slot. `largest` restricts studs to the biggest connected
# component (torso / dome) so raised arms are not studded; boots/legs stud all
# opaque pixels (both limbs). (gx, gy) = grid spacing in px.
SLOTS = {
    'chest': dict(
        outdir='_brigandine_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary13', gx=4, gy=4, largest=True,
    ),
    'legs': dict(
        outdir='_studded_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary13', gx=4, gy=4, largest=False,
    ),
    'boots': dict(
        outdir='_hobnail_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_hobnail', gx=3, gy=3, largest=False,
    ),
    'helmet': dict(
        outdir='_studdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary13', gx=3, gy=3, largest=True,
    ),
}


def load_any(fname):
    """Load a source sheet; if the female (_f) variant is absent (warrior boots are a
    single gender-shared sheet), fall back to the base sheet."""
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)


def put(fr, y, x, rgb):
    if 0 <= y < FH and 0 <= x < FW:
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def recolor(src, fr, a, D, M, L):
    v = src[..., :3].astype(np.float32).max(-1) / 255.0
    vref = float(np.median(v[a]))
    ratio = v / max(vref, 1e-3)
    for y, x in np.argwhere(a):
        q = ratio[y, x]
        tone = D if q < Q_LO else (L if q > Q_HI else M)
        put(fr, y, x, tone)


def draw_studs(fr, comp, cap, shadow, gx, gy):
    """Paint a regular grid of raised rivet-studs onto one component. A stud is a
    bright CAP pixel at each grid node plus a dark SHADOW pixel directly below it
    (only where that pixel is itself an opaque body pixel). Never paints outside the
    component, so it cannot create strays."""
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0, x0 = int(ys.min()), int(xs.min())
    opaque = set(zip(ys.tolist(), xs.tolist()))
    # Inset the grid one row/col so studs don't sit on the very outline edge.
    for (y, x) in opaque:
        if (y - y0) % gy == 1 and (x - x0) % gx == 1:
            put(fr, y, x, cap)
            if (y + 1, x) in opaque:            # bevel shadow beneath the cap
                put(fr, y + 1, x, shadow)


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    cap, shadow = STUD[cls]
    gx, gy, largest = cfg['gx'], cfg['gy'], cfg['largest']
    out = np.zeros_like(base)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = base[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        fr = out[sl]
        recolor(src, fr, a, D, M, L)
        if fi >= 60:                            # sleep: body only
            continue
        if largest:
            lbl, n = ndimage.label(a)
            if n >= 1:
                sizes = ndimage.sum(np.ones_like(lbl), lbl, index=range(1, n + 1))
                comp = (lbl == (int(np.argmax(sizes)) + 1))
            else:
                comp = a
        else:
            comp = a
        draw_studs(fr, comp, cap, shadow, gx, gy)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                arr = shade(arr, adj_min=-0.20, adj_max=0.25)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                Image.fromarray(arr).save(dst)
                print('wrote %-52s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
