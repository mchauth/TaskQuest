#!/usr/bin/env python3
"""Throwaway probe for the 69th axis. Renders candidate rib fields on REAL components and
pushes them through finish_array before any generator is written (the 13px legibility lesson)."""
import os
import sys
import math
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array                       # noqa: E402

FW, FH, COLS = 80, 64, 10


def label4(mask):
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    n = 0
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and lab[sy, sx] == 0:
                n += 1
                lab[sy, sx] = n
                st = [(sy, sx)]
                while st:
                    y, x = st.pop()
                    for ny, nx in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n
                            st.append((ny, nx))
    return lab, n


def poles(mask, n):
    ys, xs = np.nonzero(mask)
    cy, cx = ys.mean(), xs.mean()
    out = []
    for j in range(n):
        th = 2 * math.pi * j / n
        sc = (ys - cy) * math.sin(th) + (xs - cx) * math.cos(th)
        best = np.flatnonzero(sc >= sc.max() - 1e-9)
        k = min(best, key=lambda i: (int(ys[i]), int(xs[i])))
        out.append((int(ys[k]), int(xs[k]), math.cos(2*math.pi*j/n)))
    if len({(y, x) for y, x, _ in out}) != n:
        return None
    return out


def solve(mask, pol):
    idx = {}
    pts = [(int(y), int(x)) for y, x in np.argwhere(mask)]
    fixed = {(y, x): v for y, x, v in pol}
    free = [p for p in pts if p not in fixed]
    for i, p in enumerate(free):
        idx[p] = i
    m = len(free)
    A = np.zeros((m, m))
    b = np.zeros(m)
    for p in free:
        i = idx[p]
        y, x = p
        deg = 0
        for q in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
            if q[0] < 0 or q[1] < 0 or q[0] >= mask.shape[0] or q[1] >= mask.shape[1]:
                continue
            if not mask[q]:
                continue
            deg += 1
            if q in fixed:
                b[i] += fixed[q]
            else:
                A[i, idx[q]] -= 1.0
        A[i, i] = deg if deg else 1.0
    u = np.full(mask.shape, np.nan)
    if m:
        sol = np.linalg.solve(A, b)
        for p, i in idx.items():
            u[p] = sol[i]
    for (y, x), v in fixed.items():
        u[y, x] = v
    return u


def ribs(mask, u, nb):
    fin = np.isfinite(u) & mask
    vals = u[fin]
    if vals.max() - vals.min() < 1e-9:
        return np.zeros_like(mask), np.zeros_like(mask)
    # EQUAL-AREA bands: the levels are the field's own quantiles, not a ladder of numbers.
    order = np.argsort(np.argsort(vals, kind='stable'), kind='stable')
    rank = np.zeros(mask.shape, int)
    rank[fin] = order
    q = np.zeros(mask.shape, int)
    q[fin] = np.clip(rank[fin] * nb // len(vals), 0, nb - 1)
    crest = np.zeros_like(mask)
    dark = np.zeros_like(mask)
    h, w = mask.shape
    for y in range(h):
        for x in range(w):
            if not fin[y, x]:
                continue
            for ny, nx in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                if 0 <= ny < h and 0 <= nx < w and fin[ny, nx]:
                    if q[y, x] > q[ny, nx]:
                        crest[y, x] = True
                    elif q[y, x] < q[ny, nx]:
                        dark[y, x] = True
    dark &= ~crest
    return crest, dark


PAL = {'warrior': ((238, 178, 132), (170, 102, 64), (100, 58, 38)),
       'mage':    ((216, 168, 232), (146, 96, 176), (86, 54, 106)),
       'ranger':  ((206, 210, 214), (128, 134, 142), (72, 78, 86))}
NPOLE = {'warrior': 2, 'ranger': 3, 'mage': 4}


def render(src, cls, fi):
    r, c = fi // COLS, fi % COLS
    sl = (slice(r*FH, (r+1)*FH), slice(c*FW, (c+1)*FW))
    base = load(src)
    frame = base[sl]
    a = frame[..., 3] > 0
    out = np.zeros((FH, FW, 4), base.dtype)
    crestc, midc, darkc = PAL[cls]
    out[a, :3] = midc
    out[a, 3] = 255
    lab, n = label4(a)
    got = 0
    for i in range(1, n+1):
        comp = lab == i
        if comp.sum() < 12:
            continue
        pol = poles(comp, NPOLE[cls])
        if pol is None:
            continue
        u = solve(comp, pol)
        nb = max(3, min(7, int(round(math.sqrt(comp.sum()) / 2.0))))
        cr, dk = ribs(comp, u, nb)
        out[dk, :3] = darkc
        out[cr, :3] = crestc
        got += int(cr.sum())
    return out, got


def main():
    cases = [('armor_chest_4.png', 'warrior', 0), ('shirt_ranger4.png', 'ranger', 0),
             ('shirt_mage4.png', 'mage', 0), ('armor_pants_4.png', 'warrior', 0),
             ('helmet_rare1.png', 'warrior', 0), ('armor_boots_4.png', 'warrior', 0)]
    tiles = []
    for src, cls, fi in cases:
        fr, got = render(src, cls, fi)
        print('%-20s %-8s crest=%d' % (src, cls, got))
        sheet = np.zeros((FH*7, FW*10, 4), np.uint8)
        sheet[0:FH, 0:FW] = fr
        fin, info = finish_array(sheet.copy(), '_tmp/%s_%s.png' % (cls, src))
        tiles.append((fr, fin[0:FH, 0:FW]))
    Z = 14
    CW, CH = 26, 34
    W = len(tiles) * CW * Z
    out = Image.new('RGBA', (W, CH*Z*2), (24, 24, 30, 255))
    for i, (raw, fin) in enumerate(tiles):
        a = raw[..., 3] > 0
        ys, xs = np.nonzero(a)
        y0 = max(0, int((ys.min()+ys.max())//2) - CH//2)
        x0 = max(0, int((xs.min()+xs.max())//2) - CW//2)
        for j, im in enumerate((raw, fin)):
            sub = im[y0:y0+CH, x0:x0+CW]
            p = Image.fromarray(sub).resize((CW*Z, CH*Z), Image.NEAREST)
            out.paste(p, (i*CW*Z, j*CH*Z), p)
    out.save('_tmp/_proto_anneal.png')
    print('wrote _tmp/_proto_anneal.png')


if __name__ == '__main__':
    main()
