from PIL import Image
import numpy as np

ROOT = '/Users/matthauth/Projects/TaskQuest'
CHAR = f'{ROOT}/sprites/preview_assets/char'
DESKTOP = '/Users/matthauth/Desktop'

FW, FH = 80, 64
SCALE = 6
GREY = (150, 150, 150, 255)


def load_rgba(path):
    return np.array(Image.open(path).convert('RGBA'))


def frame0(arr):
    return arr[0:FH, 0:FW]


def alpha_composite(base, top):
    base = base.astype(np.float32)
    top = top.astype(np.float32)
    a = top[:, :, 3:4] / 255.0
    out = np.empty_like(base)
    out[:, :, :3] = base[:, :, :3] * (1 - a) + top[:, :, :3] * a
    out[:, :, 3:4] = np.clip(base[:, :, 3:4] + a * 255.0, 0, 255)
    return out.astype(np.uint8)


def on_grey(arr):
    bg = np.zeros_like(arr)
    bg[:, :, :] = GREY
    return alpha_composite(bg, arr)


def upscale(arr, scale=SCALE):
    return np.array(Image.fromarray(arr, 'RGBA').resize(
        (arr.shape[1] * scale, arr.shape[0] * scale), Image.NEAREST))


skin = frame0(load_rgba(f'{CHAR}/skin_m1.png'))

composites = {}
for tier in range(1, 7):
    armor_path = f'{CHAR}/leather_armor_1.png' if tier == 1 else f'{CHAR}/armor_chest_{tier}.png'
    armor = frame0(load_rgba(armor_path))
    comp = alpha_composite(skin, armor)
    composites[tier] = comp

    # individual preview (tiers 2-6) at 6x on grey
    if tier >= 2:
        big = upscale(on_grey(comp))
        Image.fromarray(big, 'RGBA').save(f'{DESKTOP}/armor_chest_{tier}_preview.png')
        print(f'Saved armor_chest_{tier}_preview.png ({big.shape[1]}x{big.shape[0]})')

# combined progression strip: tiers 1-6 side by side at 6x on grey
PAD = 8
cell_w = FW * SCALE
cell_h = FH * SCALE
strip_w = cell_w * 6 + PAD * 7
strip_h = cell_h + PAD * 2
strip = np.zeros((strip_h, strip_w, 4), dtype=np.uint8)
strip[:, :, :] = GREY

for i, tier in enumerate(range(1, 7)):
    big = upscale(on_grey(composites[tier]))
    x = PAD + i * (cell_w + PAD)
    y = PAD
    strip[y:y + cell_h, x:x + cell_w] = big

Image.fromarray(strip, 'RGBA').save(f'{DESKTOP}/armor_progression.png')
print(f'Saved armor_progression.png ({strip.shape[1]}x{strip.shape[0]})')
