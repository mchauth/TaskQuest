#!/usr/bin/env python3
"""TWELFTH net-new-geometry BOOTS showcase per class — a PUTTEE WRAP: repeated
DIAGONAL wrap-lines spiralling up the boot shaft (leg-wrapping / spiral puttee).
This brings the boots slot to TWELVE distinct axes. It is the repeated-parallel-
DIAGONAL axis none of the eleven existing legendary boots occupy:

  * legendary_greave    — a tall shin GREAVE + knee-cop.
  * legendary_cuff      — a wide folded cavalier CUFF.
  * legendary_sabaton   — a forward-raked poulaine TOE.
  * legendary_spur      — a heel rowel-SPUR wheel.
  * legendary_wing      — diagonal ankle WINGS (silhouette).
  * legendary_claw      — downward beast-CLAW talons (silhouette).
  * legendary_lace      — a single diagonal cross-lacing 'X'.
  * legendary_strap     — a SINGLE horizontal buckle strap.
  * legendary_toecap    — a reinforced steel TOE-CAP.
  * legendary_tristrap  — THREE horizontal straps (repeated-HORIZONTAL).
  * legendary_rivetshaft— a single VERTICAL riveted seam.
  * this PUTTEE WRAP lays a SERIES of evenly-spaced DIAGONAL wrap-lines up the shaft
    — the repeated-parallel-DIAGONAL axis, distinct from the single crossing 'X'
    lace, the repeated horizontal straps, and the vertical seam. A flat repaint that
    adds no silhouette pixels.

Authoring philosophy is identical to gen_rivetshaft_boots.py: wrap pixels are
painted ONLY onto pixels that are ALREADY opaque body pixels. Painted per boot
COMPONENT. QA-safe purely by construction — it can never add a pixel outside the
existing silhouette.

Sleep frames (fi>=60) get the recolor only. Shading applied in-script via shade();
do NOT run sprite_shade.py again.

Per class the wrap hue is the class accent family:
  * warrior "Warlord's Wrapped Warboots" — dark-steel body + steel wrap, gold pin
  * mage    "Astral Spiral-Striders"     — deep-violet body + silver wrap, cyan pin
  * ranger  "Warden's Puttee Field-Boots"— bark-brown body + tan wrap, copper pin

Run from repo root:
  python3 scripts/gen_puttee_boots.py
Then QA:
  python3 scripts/sprite_qa.py _puttee_boots_preview/boots_warrior_legendary_puttee.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, shade, CHAR    # noqa: E402


def load_any(fname):
    """Load a source sheet; if the female (_f) variant is absent (warrior boots are
    a single gender-shared sheet), fall back to the base sheet."""
    if os.path.exists(os.path.join(CHAR, fname)):
        return load(fname)
    if fname.endswith('_f.png'):
        return load(fname[:-6] + '.png')
    raise FileNotFoundError(fname)

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# Diagonal wrap: for a boot component we compute a diagonal coordinate
# d = (x - x0) + (y - y0); wrap lines fall on d % PERIOD < 1 (the lit strand), with
# a dark shadow strand one step above. A single bright pin sits on the lowest line.
PERIOD = 4
MIN_PX = 8

# body : deep shadow / base / highlight
# wrap : STRAND (lit wrap line) / SHADOW (dark under-strand) / PIN (bright pin)
CLASSES = {
    'warrior': dict(
        src='armor_boots_4', dst='boots_warrior_legendary_puttee',
        body=((36, 40, 48), (78, 84, 96), (132, 140, 156)),     # dark steel
        wrap=((190, 196, 212), (46, 50, 60), (232, 190, 70)),   # steel strand, dark under, gold pin
    ),
    'mage': dict(
        src='boots_mage4', dst='boots_mage_legendary_puttee',
        body=((22, 14, 48), (58, 40, 112), (110, 84, 190)),     # deep violet
        wrap=((196, 202, 224), (34, 26, 82), (96, 210, 244)),   # silver strand, dark under, cyan pin
    ),
    'ranger': dict(
        src='boots_ranger4', dst='boots_ranger_legendary_puttee',
        body=((34, 24, 14), (74, 52, 30), (122, 90, 52)),       # bark brown
        wrap=((176, 138, 84), (40, 28, 16), (206, 132, 66)),    # tan strand, dark under, copper pin
    ),
}


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


def draw_wrap(fr, comp, pal):
    """Paint repeated diagonal wrap-lines up one boot component."""
    STRAND, SHADOW, PIN = pal
    ys, xs = np.where(comp)
    if ys.size < MIN_PX:
        return
    y0 = int(ys.min())
    x0 = int(xs.min())
    lowest = None                       # painted pixel with the largest y on a strand
    for y, x in zip(ys, xs):
        d = (x - x0) + (y - y0)
        m = d % PERIOD
        if m < 1.0:                     # lit wrap strand
            put(fr, y, x, STRAND)
            if lowest is None or y > lowest[0]:
                lowest = (y, x)
        elif m < 2.0:                   # dark under-strand
            put(fr, y, x, SHADOW)
    # a single bright pin on the lowest wrap line
    if lowest is not None:
        put(fr, lowest[0], lowest[1], PIN)


def build(base, cfg):
    D, M, L = cfg['body']
    pal = cfg['wrap']
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
        if fi >= 60:                       # sleep: body only
            continue
        lbl, n = ndimage.label(a)
        for k in range(1, n + 1):
            draw_wrap(fr, lbl == k, pal)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = ndimage.label(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


def main():
    outdir = '_puttee_boots_preview'
    os.makedirs(outdir, exist_ok=True)
    for name, cfg in CLASSES.items():
        for suffix in ('', '_f'):
            base = load_any('%s%s.png' % (cfg['src'], suffix))
            arr = build(base, cfg)
            arr = shade(arr, adj_min=-0.20, adj_max=0.25)
            dst = '%s/%s%s.png' % (outdir, cfg['dst'], suffix)
            Image.fromarray(arr).save(dst)
            print('wrote %-48s opaque_px=%d' % (dst, (arr[..., 3] > 0).sum()))


if __name__ == '__main__':
    main()
