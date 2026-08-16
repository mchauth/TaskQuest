#!/usr/bin/env python3
"""Rigorous per-sheet verification for the war-kilt legs legendaries.
For each of the 6 sheets, vs its source t4-pants sheet:
  1. source px dropped  = source silhouette pixels NOT present in output (0)
  2. active-frame parity = #frames with any source px == #frames with any output px
  3. accent-caused multi-component frames = frames whose OUTPUT has >1 connected
     component beyond what the SOURCE already has (0 -> every kilt fused)
  4. accent strays = output opaque pixels neither in-source nor 4-connected to
     the body mass (0)
"""
import numpy as np
from PIL import Image
from scipy import ndimage

FW, FH, COLS, NFR = 80, 64, 10, 70
CH = "sprites/preview_assets/char"
PREV = "_warkilt_legs_preview"
PAIRS = [
    ("armor_pants_4", "pants_warrior_legendary2"),
    ("pants_mage4", "pants_mage_legendary2"),
    ("pants_ranger4", "pants_ranger_legendary2"),
]


def sheet(path):
    return np.array(Image.open(path).convert("RGBA"))


def frames(arr):
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        yield fi, arr[r*FH:(r+1)*FH, c*FW:(c+1)*FW]


def ncomp(mask):
    return ndimage.label(mask)[1]


def check(src_stem, dst_stem, suf):
    src = sheet(f"{CH}/{src_stem}{suf}.png")
    dst = sheet(f"{PREV}/{dst_stem}{suf}.png")
    dropped = parity_src = parity_dst = multi = strays = 0
    for fi, sf in frames(src):
        df = dict(frames(dst))[fi]
        sa = sf[..., 3] > 0
        da = df[..., 3] > 0
        if sa.any():
            parity_src += 1
        if da.any():
            parity_dst += 1
        dropped += int((sa & ~da).sum())
        if not da.any():
            continue
        extra = ncomp(da) - (ncomp(sa) if sa.any() else 0)
        if extra > 0:
            multi += 1
        lbl, n = ndimage.label(da)
        body_labels = set(np.unique(lbl[sa])) - {0}
        connected = np.isin(lbl, list(body_labels)) if body_labels else np.zeros_like(da)
        stray_mask = da & ~sa & ~connected
        strays += int(stray_mask.sum())
    return dropped, parity_src, parity_dst, multi, strays


def main():
    allpass = True
    for src_stem, dst_stem in PAIRS:
        for suf in ("", "_f"):
            d, ps, pd, m, s = check(src_stem, dst_stem, suf)
            ok = (d == 0 and ps == pd and m == 0 and s == 0)
            allpass &= ok
            print(f"{dst_stem}{suf:2s}: dropped={d} parity={ps}/{pd} "
                  f"accent_multicomp_frames={m} accent_strays={s}  "
                  f"{'PASS' if ok else 'FAIL'}")
    print("\nALL PASS" if allpass else "\nFAILURES PRESENT")


if __name__ == "__main__":
    main()
