#!/usr/bin/env python3
"""Diagnostic for the 60th axis clause-4 FAIL.

Recomputes the batch word statistics four ways, to separate a defect in the ORNAMENT from a
defect in the ESTIMATOR:

  A  readable reeds, compacted   -- exactly what accept_all() does today (and note the compaction
                                    splices non-adjacent reeds into one string)
  B  readable reeds, split into MAXIMAL CONTIGUOUS RUNS -- same sample, no splicing
  C  interior reeds of those runs -- a reed both of whose neighbours are also readable
  D  every letter the word PLACES on the component, readable or not -- the ground truth, i.e. what
     the ornament actually is, as opposed to what survives the silhouette
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_cadence_axis60 as G  # noqa: E402


def runs_of(read):
    out, cur = [], []
    for v in read:
        if v is None:
            if cur:
                out.append(cur)
            cur = []
        else:
            cur.append(v)
    if cur:
        out.append(cur)
    return out


def ratio(words):
    flat = [c for w in words for c in w]
    nn = sum(1 for c in flat if c == G.NARROW)
    nw = len(flat) - nn
    return nn, nw, nn / float(max(nw, 1))


def main():
    A, B, C, D = [], [], [], []
    ncomp = 0
    for kind, cfg in G.SLOTS.items():
        for cls, srcstem in cfg['srcs'].items():
            stops = G.CADENCE[cls]
            for suffix in ('', '_f'):
                base = G.load_any('%s%s.png' % (srcstem, suffix))
                for fi in range(60):
                    r, c = fi // G.COLS, fi % G.COLS
                    src = base[r * G.FH:(r + 1) * G.FH, c * G.FW:(c + 1) * G.FW]
                    a = src[..., 3] > 0
                    if not a.any():
                        continue
                    fr = np.zeros_like(src)
                    for comp_full in G.comps_of(a, cfg['largest']):
                        if comp_full.sum() < G.MIN_PX:
                            continue
                        info = G.paint_cadence(fr, comp_full, stops)
                        read, _ = G.read_word(fr, comp_full, stops, info)
                        ncomp += 1
                        A.append([v for v in read if v is not None])
                        rs = runs_of(read)
                        B.extend(rs)
                        for run in rs:
                            if len(run) > 2:
                                C.append(run[1:-1])
                        D.append(list(info['letters']))
    print('components %d' % ncomp)
    for name, W in (('A readable, compacted ', A), ('B readable, runs      ', B),
                    ('C run interiors       ', C), ('D word as placed      ', D)):
        nn, nw, r = ratio(W)
        print('  %s narrow %-6d wide %-6d ratio %.4f   err vs phi %+0.4f'
              % (name, nn, nw, r, r - G.PHI))
    print()
    for name, W in (('A', A), ('B', B), ('C', C), ('D', D)):
        f = [len(G.factors(W, n)) for n in range(1, 6)]
        obs = [sum(max(0, len(w) - n + 1) for w in W) for n in range(1, 6)]
        bad = G.runs_ok(W)
        print('  %s complexity %s   (want 2,3,4,5,6)  windows %s  forbidden %d'
              % (name, f, obs, len(bad)))


if __name__ == '__main__':
    main()
