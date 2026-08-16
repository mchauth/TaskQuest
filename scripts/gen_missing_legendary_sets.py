#!/usr/bin/env python3
"""Generate all missing legendary armor set pieces.

For every axis that has a legendary shirt (or helmet) but is missing matching
helmet/legs/boots (or shirt/legs/boots), this script generates the missing slots
as luminance-quantile 3-tone recolors of the standard t4 silhouettes, then runs
finish_array() which adds visor/pauldron/shading automatically.

Run from repo root:
    python3 scripts/gen_missing_legendary_sets.py

Then inspect staged dirs and run QA manually per slot type:
    python3 scripts/sprite_qa.py _baldric_helmet_preview/helmet_warrior_legendary_baldric.png --y-min 2
    python3 scripts/sprite_qa.py _baldric_legs_preview/pants_warrior_legendary_baldric.png --y-max 63
    python3 scripts/sprite_qa.py _baldric_boots_preview/boots_warrior_legendary_baldric.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprite_finish import finish_array          # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CHAR = os.path.join(ROOT, 'sprites', 'preview_assets', 'char') + os.sep

FW, FH, COLS, NFR = 80, 64, 10, 70
Q_LO, Q_HI = 0.85, 1.18

# ── source silhouettes per class per slot ─────────────────────────────────────
SHIRT_SRC  = {'warrior': 'armor_chest_4',  'mage': 'shirt_mage4',   'ranger': 'shirt_ranger4'}
LEGS_SRC   = {'warrior': 'armor_pants_4',  'mage': 'pants_mage4',   'ranger': 'pants_ranger4'}
BOOTS_SRC  = {'warrior': 'armor_boots_4',  'mage': 'boots_mage4',   'ranger': 'boots_ranger4'}
HELMET_SRC = {'warrior': 'helmet_rare1',   'mage': 'helmet_mage4',  'ranger': 'helmet_ranger4'}

# warrior boots have no female sheet
NO_FEMALE = {'warrior': {'boots'}}

# ── standard body palette shared by most accessory axes ───────────────────────
STD = {
    'warrior': ((28, 30, 36),  (74, 78, 90),   (128, 134, 150)),   # obsidian/steel
    'mage':    ((20, 16, 54),  (54, 42, 122),  (120,  96, 200)),   # arcane violet
    'ranger':  ((20, 40, 18),  (48, 88,  42),  ( 98, 150,  82)),   # forest green
}

# ── per-axis config ───────────────────────────────────────────────────────────
#
#  'palette': {class: (D, M, L)} — body ramp for recolor
#  'needs':   list of slots to generate ('shirt','helmet','legs','boots')
#  'classes': which classes need pieces
#
# Shirt-primary axes (have shirt, need helmet+legs+boots unless noted):
# Helmet-primary axes (have helmet, need shirt+legs+boots):
# Single-gender axes: see NO_FEMALE

AXES = {

    # ── shirt-primary, all-3-class (STD palette) ──────────────────────────────
    'baldric': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'cape': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'chevron': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'girdle': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'gorget': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'lamellar': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'pauldron': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'roundel': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),
    'tabard': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['helmet','legs','boots'],
    ),

    # ── flute: STD palette, helmet already staged, only legs+boots needed ──────
    'flute': dict(
        palette=STD, classes=['warrior','mage','ranger'],
        needs=['legs','boots'],
    ),

    # ── single-class shirt-primary axes ───────────────────────────────────────
    'mage_winged': dict(
        palette={
            'mage': ((46, 34, 96), (96, 74, 190), (196, 186, 250)),  # cosmic indigo
        },
        classes=['mage'],
        needs=['helmet','legs','boots'],
    ),
    'ranger_winged': dict(
        palette={
            'ranger': ((22, 46, 28), (58, 120, 66), (206, 196, 128)),  # forest→bronze
        },
        classes=['ranger'],
        needs=['helmet','legs','boots'],
    ),

    # ── winged: warrior-only shirt, boots staged, need helmet+legs ─────────────
    'winged': dict(
        palette={
            'warrior': ((150, 104, 32), (222, 176, 70), (250, 232, 168)),  # divine gold/white
        },
        classes=['warrior'],
        needs=['helmet','legs'],
    ),

    # ── helmet-primary axes: generate shirt+legs+boots ────────────────────────

    # crest: brass-galea warrior, cosmic mage, forest ranger
    'crest': dict(
        palette={
            'warrior': (( 58,  50,  38), (120, 104,  74), (202, 182, 132)),  # brass galea
            'mage':    (( 46,  34,  96), ( 96,  74, 190), (196, 186, 250)),  # cosmic
            'ranger':  (( 20,  44,  18), ( 44,  86,  34), (120, 150,  80)),  # forest
        },
        classes=['warrior','mage','ranger'],
        needs=['shirt','legs','boots'],
    ),

    # horned: warrior-only dark iron
    'horned': dict(
        palette={
            'warrior': ((38, 40, 48), (78, 82, 94), (150, 156, 172)),  # dark iron
        },
        classes=['warrior'],
        needs=['shirt','legs','boots'],
    ),

    # winghelm: same palette as winghelm helmet body (dark iron/cosmic/forest)
    'winghelm': dict(
        palette={
            'warrior': ((40, 42, 50), (92,  96, 110), (150, 156, 172)),  # dark iron→steel
            'mage':    ((16, 16, 58), (44,  40, 120), (110,  96, 200)),  # cosmic indigo
            'ranger':  ((18, 38, 16), (44,  84,  38), ( 92, 146,  78)),  # forest
        },
        classes=['warrior','mage','ranger'],
        needs=['shirt','legs','boots'],
    ),
}

# ── slot → (source dict, filename prefix, outdir suffix) ─────────────────────
SLOT_CFG = {
    'shirt':  (SHIRT_SRC,  'shirt',  '_{axis}_shirt_preview'),
    'helmet': (HELMET_SRC, 'helmet', '_{axis}_helmet_preview'),
    'legs':   (LEGS_SRC,   'pants',  '_{axis}_legs_preview'),
    'boots':  (BOOTS_SRC,  'boots',  '_{axis}_boots_preview'),
}


def load_img(name):
    path = CHAR + name + '.png'
    return np.array(Image.open(path).convert('RGBA'))


def recolor_sheet(arr, D, M, L):
    """Quantized 3-tone recolor of all opaque pixels across all frames."""
    out = np.zeros_like(arr)
    for fi in range(NFR):
        r, c = fi // COLS, fi % COLS
        sl = (slice(r * FH, (r + 1) * FH), slice(c * FW, (c + 1) * FW))
        src = arr[sl]
        fr = out[sl]
        a = src[..., 3] > 0
        if not a.any():
            continue
        v = src[..., :3].astype(np.float32).max(-1) / 255.0
        vref = float(np.median(v[a]))
        ratio = v / max(vref, 1e-3)
        for y, x in np.argwhere(a):
            q = ratio[y, x]
            tone = D if q < Q_LO else (L if q > Q_HI else M)
            fr[y, x, :3] = tone
            fr[y, x, 3] = 255
    return out


def gen_slot(axis, slot, cls, D, M, L, outdir):
    """Generate one slot for one class (male + female where applicable)."""
    src_dict, prefix, _ = SLOT_CFG[slot]
    src_base = src_dict[cls]

    no_fem = NO_FEMALE.get(cls, set())
    suffixes = [''] if slot in no_fem else ['', '_f']

    for suffix in suffixes:
        src_path = CHAR + src_base + suffix + '.png'
        if not os.path.exists(src_path):
            if suffix == '_f':
                print(f'  skip (no female source): {src_base}{suffix}.png')
                continue
            print(f'  ERROR missing source: {src_path}')
            continue

        arr = np.array(Image.open(src_path).convert('RGBA'))
        arr = recolor_sheet(arr, D, M, L)

        dst_name = f'{prefix}_{cls}_legendary_{axis}{suffix}.png'
        dst = os.path.join(outdir, dst_name)
        arr, _info = finish_array(arr, dst)
        Image.fromarray(arr).save(dst)
        opaque = int((arr[..., 3] > 0).sum())
        print(f'  wrote {dst}  (opaque={opaque})')


def main():
    os.chdir(ROOT)
    total_files = 0

    for axis, cfg in AXES.items():
        print(f'\n=== {axis.upper()} ===')
        for slot in cfg['needs']:
            src_dict, prefix, outdir_tpl = SLOT_CFG[slot]
            outdir = outdir_tpl.format(axis=axis)
            os.makedirs(outdir, exist_ok=True)

            for cls in cfg['classes']:
                D, M, L = cfg['palette'][cls]
                gen_slot(axis, slot, cls, D, M, L, outdir)
                total_files += 1

    print(f'\nDone — generated pieces for {len(AXES)} axes.')


if __name__ == '__main__':
    main()
