#!/usr/bin/env python3
"""
gen_weapons_v2.py — Rebuild all weapon sprites with:
  1. Per-frame rotation in slash frames 51-53 (matching source sword.png angles)
  2. Arc trail (white+lavender) for frame 54 on swords and staffs
  3. Redesigned bow shape (vertical bow, upper+lower limbs, string)
  4. Bow draw animation instead of slash (bow raises to vertical, arrow fires)
"""
import numpy as np
from PIL import Image

FW, FH, COLS, ROWS = 80, 64, 10, 7

# ── Source sprite analysis ───────────────────────────────────────────────────

def get_centroid(arr, fi):
    r, c = fi // COLS, fi % COLS
    sl = arr[r*FH:(r+1)*FH, c*FW:(c+1)*FW]
    op = np.argwhere(sl[..., 3] > 0)
    if len(op) == 0: return None, None
    return float(np.mean(op[:,1])), float(np.mean(op[:,0]))

def get_angle(arr, fi):
    r, c = fi // COLS, fi % COLS
    sl = arr[r*FH:(r+1)*FH, c*FW:(c+1)*FW]
    op = np.argwhere(sl[..., 3] > 0)
    if len(op) < 3: return 0.0
    ys, xs = op[:,0].astype(float), op[:,1].astype(float)
    cx, cy = np.mean(xs), np.mean(ys)
    pts = np.stack([xs-cx, ys-cy], axis=1)
    cov = pts.T @ pts / len(op)
    vals, vecs = np.linalg.eigh(cov)
    pv = vecs[:, np.argmax(vals)]
    return float(np.degrees(np.arctan2(pv[1], pv[0])))

SRC = np.array(Image.open('sprites/preview_assets/char/sword.png').convert('RGBA'))
src_cx0, src_cy0 = get_centroid(SRC, 0)
src_ang0 = get_angle(SRC, 0)

# Per-frame slash rotation deltas (relative to frame 0)
SLASH_ANGLES = {}
for fi in [51, 52, 53, 55]:
    SLASH_ANGLES[fi] = get_angle(SRC, fi) - src_ang0

# Slash centroids from source
SLASH_CX = {}; SLASH_CY = {}
for fi in range(COLS * ROWS):
    cx, cy = get_centroid(SRC, fi)
    if cx is not None: SLASH_CX[fi] = cx; SLASH_CY[fi] = cy

print("Slash angle deltas:", {k: f"{v:.1f}°" for k,v in SLASH_ANGLES.items()})

# Pre-compute extend positions: only use fr54 and fr55 (last 2 frames, reversed)
# fr54 = "extended/raised" position; fr55 = "idle/resting" position
DX_FR54 = round(SLASH_CX[54] - src_cx0)
DY_FR54 = round(SLASH_CY[54] - src_cy0)
DX_FR55 = round(SLASH_CX[55] - src_cx0)
DY_FR55 = round(SLASH_CY[55] - src_cy0)
print(f"Extend positions: fr54=({DX_FR54},{DY_FR54}), fr55=({DX_FR55},{DY_FR55})")

# ── Utility ──────────────────────────────────────────────────────────────────

def bezier_pts(p0, ctrl, p2, steps=14):
    """Quadratic Bezier curve from p0 to p2 with control point ctrl."""
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = round((1-t)**2 * p0[0] + 2*t*(1-t) * ctrl[0] + t**2 * p2[0])
        y = round((1-t)**2 * p0[1] + 2*t*(1-t) * ctrl[1] + t**2 * p2[1])
        pts.append((x, y))
    deduped = [pts[0]]
    for p in pts[1:]:
        if p != deduped[-1]:
            deduped.append(p)
    return deduped

def bresenham(x0, y0, x1, y1):
    pts = []
    dx, dy = abs(x1-x0), abs(y1-y0)
    sx, sy = (1 if x1>x0 else -1), (1 if y1>y0 else -1)
    err = dx - dy
    x, y = x0, y0
    while True:
        pts.append((x, y))
        if x == x1 and y == y1: break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x += sx
        if e2 < dx:  err += dx; y += sy
    return pts

def rotate_pixels(pix, angle_deg, around_cx, around_cy):
    if not pix: return {}
    rad = np.radians(angle_deg)
    cos_a, sin_a = np.cos(rad), np.sin(rad)
    result = {}
    for (x, y), color in pix.items():
        px, py = x - around_cx, y - around_cy
        nx = round(cos_a*px - sin_a*py + around_cx)
        ny = round(sin_a*px + cos_a*py + around_cy)
        if 0 <= nx < FW and 0 <= ny < FH and (nx,ny) not in result:
            result[(nx, ny)] = color
    return result

def translate_pixels(pix, dx, dy):
    result = {}
    for (x, y), color in pix.items():
        nx, ny = x+dx, y+dy
        if 0 <= nx < FW and 0 <= ny < FH and (nx,ny) not in result:
            result[(nx, ny)] = color
    return result

def centroid_of(pix):
    if not pix: return 0.0, 0.0
    xs = [p[0] for p in pix]; ys = [p[1] for p in pix]
    return float(np.mean(xs)), float(np.mean(ys))

def stamp(out, pix, gx, gy):
    for (x, y), color in pix.items():
        if 0 <= x < FW and 0 <= y < FH:
            out[gy+y, gx+x] = color

# ── Trail arc for frame 54 (swing trail) ─────────────────────────────────────

def make_trail_arc(trail_color_center, trail_color_edge):
    """Generate a diagonal sweep arc like the one in sword.png frame 54."""
    WHITE = trail_color_center
    LAV   = trail_color_edge
    pix = {}
    # Diagonal band: center line goes from upper-right to lower-left
    # y in [1,44], center_x = 47 - 0.59*y, half_width = 5 + 0.3*y
    for y in range(0, 46):
        cx_line = 47.0 - 0.59 * y
        hw = 5.0 + 0.3 * y
        x0 = round(cx_line - hw)
        x1 = round(cx_line + hw)
        for x in range(max(0, x0), min(FW, x1+1)):
            dist = abs(x - cx_line)
            if dist > hw - 1.5:
                color = LAV
            else:
                color = WHITE
            pix[(x, y)] = color
    return pix

def make_trail_frame55(trail_color_center, trail_color_edge):
    """Smaller fading trail for frame 55 (sword.png pattern)."""
    WHITE = trail_color_center
    LAV   = trail_color_edge
    pix = {}
    # Sword-like bottom arc: horizontal band around y=47-54
    for y in range(47, 55):
        cx_line = 16.0 + (y-47) * 2.0
        hw = 8.0 + (y-47)
        x0, x1 = round(cx_line - hw), round(cx_line + hw)
        for x in range(max(0, x0), min(FW, x1+1)):
            dist = abs(x - cx_line)
            if dist > hw - 1.5:
                color = LAV
            else:
                color = WHITE
            pix[(x, y)] = color
    # Small upper remnant
    for y in range(3, 7):
        cx_line = 36.0 - (y-3)*1.5
        for x in range(max(0, round(cx_line)-1), min(FW, round(cx_line)+2)):
            pix[(x, y)] = WHITE
    return pix

# ── Centroid-propagate pixels across all frames ───────────────────────────────

def build_sheet(f0, source_path, out_path, weapon_type='sword',
                trail_c=None, trail_e=None):
    """
    f0: dict of {(x,y): rgba_tuple} for frame 0
    source_path: reference sprite for centroid tracking (sword.png)
    weapon_type: 'sword', 'staff', or 'bow'
    trail_c/trail_e: trail center/edge colors for slash frame 54 (sword/staff only)
    """
    src_arr = np.array(Image.open(source_path).convert('RGBA'))
    out = np.zeros((ROWS*FH, COLS*FW, 4), dtype=np.uint8)

    cx0_src, cy0_src = get_centroid(src_arr, 0)
    cx0_f0, cy0_f0   = centroid_of(f0)

    for fi in range(COLS * ROWS):
        r, c = fi // COLS, fi % COLS
        gx, gy = c * FW, r * FH

        cx_src, cy_src = get_centroid(src_arr, fi)
        if cx_src is None: continue
        dx = round(cx_src - cx0_src)
        dy = round(cy_src - cy0_src)

        if weapon_type == 'sword':
            # Sword: full slash arc with rotation and trail.
            # +180° flips grip/blade so grip stays in hand during swing.
            if fi in [51, 52, 53]:
                angle_delta = SLASH_ANGLES.get(fi, 0.0) + 180.0
                pix2 = rotate_pixels(f0, angle_delta, cx0_f0, cy0_f0)
                pix2 = translate_pixels(pix2, dx, dy)
                stamp(out, pix2, gx, gy)
            elif fi == 54:
                if trail_c and trail_e:
                    trail = make_trail_arc(trail_c, trail_e)
                    stamp(out, trail, gx, gy)
                pix = translate_pixels(f0, dx, dy)
                dark_pix = {k: v for k, v in pix.items() if int(v[0])+int(v[1])+int(v[2]) < 90}
                stamp(out, dark_pix, gx, gy)
            elif fi == 55:
                if trail_c and trail_e:
                    trail = make_trail_frame55(trail_c, trail_e)
                    stamp(out, trail, gx, gy)
                pix = translate_pixels(f0, dx, dy)
                stamp(out, pix, gx, gy)
            else:
                pix = translate_pixels(f0, dx, dy)
                stamp(out, pix, gx, gy)

        elif weapon_type in ('staff', 'bow'):
            # Staff/bow: align weapon's OWN centroid to sword centroid target,
            # so bow/staff don't float above/beside the hand.
            if 50 <= fi <= 55:
                extended = fi in [51, 52, 53]
                target_fi = 54 if extended else 55
                target_cx = SLASH_CX.get(target_fi, cx_src)
                target_cy = SLASH_CY.get(target_fi, cy_src)
                # Translate so THIS weapon's centroid lands on the sword target
                actual_dx = round(target_cx - cx0_f0)
                actual_dy = round(target_cy - cy0_f0)
                pix = translate_pixels(f0, actual_dx, actual_dy)
                stamp(out, pix, gx, gy)

                if weapon_type == 'bow' and extended:
                    # Arrow shoots LEFT from bow centroid (toward the enemy)
                    # Short shaft: 12px, tip on left, feathers on right
                    SHAFT = (120, 80,  35, 255)
                    TIP   = (180, 180, 190, 255)
                    FEATH = (200, 60,  60, 255)
                    arrow_y = max(2, min(FH-3, round(target_cy)))
                    ax_r = max(2, round(target_cx) - 2)  # feather end (near bow)
                    ax_l = max(0, ax_r - 12)             # tip end (left)
                    for ax in range(ax_l, ax_r):
                        out[gy + arrow_y, gx + ax] = SHAFT
                    # Tip (arrowhead) at left end
                    for ay in [-1, 0, 1]:
                        r2 = gy + arrow_y + ay
                        if 0 <= r2 < out.shape[0] and gx + ax_l - 1 >= 0:
                            out[r2, gx + ax_l - 1] = TIP
                    # Feathers at right end
                    for ay in [-1, 1]:
                        r2 = gy + arrow_y + ay
                        if 0 <= r2 < out.shape[0] and gx + ax_r < out.shape[1]:
                            out[r2, gx + ax_r] = FEATH

                elif weapon_type == 'staff' and extended:
                    # Energy orb at staff tip (topmost pixel after translation)
                    tip_y_fr0 = min(y for x, y in f0.keys()) if f0 else round(cy0_f0)
                    tip_xs = [x for x, y in f0.keys() if abs(y - tip_y_fr0) <= 2]
                    tip_x_fr0 = round(float(np.mean(tip_xs))) if tip_xs else round(cx0_f0)
                    orb_x = round(tip_x_fr0 + actual_dx)
                    orb_y = round(tip_y_fr0 + actual_dy)
                    orb_core = trail_c if trail_c else (180, 120, 255, 255)
                    orb_glow = trail_e if trail_e else (220, 180, 255, 180)
                    for dy2 in range(-3, 4):
                        for dx2 in range(-3, 4):
                            r2 = gy + orb_y + dy2
                            c2 = gx + orb_x + dx2
                            if 0 <= r2 < out.shape[0] and 0 <= c2 < out.shape[1]:
                                dist = abs(dx2) + abs(dy2)
                                if dist <= 1:
                                    out[r2, c2] = orb_core
                                elif dist <= 4:
                                    out[r2, c2] = orb_glow
            else:
                pix = translate_pixels(f0, dx, dy)
                stamp(out, pix, gx, gy)

        else:
            pix = translate_pixels(f0, dx, dy)
            stamp(out, pix, gx, gy)

    Image.fromarray(out).save(out_path)
    print(f"  Saved: {out_path}")

def _bow_slash_frame(out, fi, f0, cx0, cy0, dx, dy, gx, gy, trail_c, trail_e):
    """Bow draw animation: bow raises to vertical, arrow fires."""
    WHITE = (255, 255, 255, 255)
    ARROW_SHAFT = (120, 80, 35, 255)
    ARROW_TIP   = (180, 180, 190, 255)
    ARROW_FEATHER = (200, 60, 60, 255)

    if fi == 50:
        # Start: bow at normal position
        pix = translate_pixels(f0, dx, dy)
        stamp(out, pix, gx, gy)
    elif fi == 51:
        # Bow rotated ~30° toward vertical (arm raising)
        pix = rotate_pixels(f0, -30, cx0, cy0)
        pix = translate_pixels(pix, dx - 4, dy - 8)
        stamp(out, pix, gx, gy)
    elif fi in [52, 53]:
        # Bow at full "draw" position — near-vertical, arm stopped
        # Rotate ~55° from base
        pix = rotate_pixels(f0, -55, cx0, cy0)
        pix = translate_pixels(pix, dx - 8, dy - 16)
        stamp(out, pix, gx, gy)
    elif fi == 54:
        # FIRE: bow at draw position + arrow streak going right
        pix = rotate_pixels(f0, -55, cx0, cy0)
        pix = translate_pixels(pix, dx - 8, dy - 16)
        stamp(out, pix, gx, gy)
        # Arrow streak: from grip outward to the right
        arrow_y = gy + 44
        arrow_x0 = gx + 44
        # Shaft
        for ax in range(arrow_x0, min(gx + FW, arrow_x0 + 20)):
            if 0 <= arrow_y < out.shape[0] and 0 <= ax < out.shape[1]:
                out[arrow_y, ax] = ARROW_SHAFT
        # Tip (arrowhead)
        tip_x = arrow_x0 + 20
        for ay in range(-2, 3):
            if abs(ay) <= 1:
                if 0 <= arrow_y+ay < out.shape[0] and 0 <= tip_x < out.shape[1]:
                    out[arrow_y+ay, tip_x] = ARROW_TIP
        # Feathers (back end)
        for ay in [-2, -1, 0, 1, 2]:
            if 0 <= arrow_y+ay < out.shape[0] and 0 <= arrow_x0+1 < out.shape[1]:
                if abs(ay) >= 1:
                    out[arrow_y+ay, arrow_x0+1] = ARROW_FEATHER
    elif fi == 55:
        # Bow relaxing back, faint arrow trail
        pix = rotate_pixels(f0, -30, cx0, cy0)
        pix = translate_pixels(pix, dx - 2, dy - 5)
        stamp(out, pix, gx, gy)
        # Faint arrow trail
        arrow_y = gy + 44
        for ax in range(gx+44, min(gx+FW, gx+60)):
            if 0 <= arrow_y < out.shape[0] and 0 <= ax < out.shape[1]:
                out[arrow_y, ax] = (200, 180, 140, 160)

# ── New bow frame-0 design (proper bow shape) ────────────────────────────────

def make_bow_frame0(limb_dark, limb_mid, limb_light, limb_hi, grip_dark, str_color):
    """
    Bow held diagonally: grip at upper-right area, upper limb curves to upper-left tip,
    lower limb curves to lower-right tip.  Gentle Bezier curves — visible arc, not extreme.
    """
    pix = {}
    bd = limb_dark; gd = limb_mid; gl = limb_light; gh = limb_hi
    sk = grip_dark; sr = str_color

    # ── Grip (leather wrap) x=39-42, y=44-48 ──
    for x in range(39, 43):
        for y in range(44, 49):
            pix[(x,y)] = sk
    for pt in [(38,44),(38,45),(38,46),(38,47),(38,48),
               (43,44),(43,45),(43,46),(43,47),(43,48),
               (39,43),(40,43),(41,43),(42,43),
               (39,49),(40,49),(41,49),(42,49)]:
        pix[pt] = bd

    # ── Upper limb: grip top (39,43) → tip (27,20)
    # Control pulled left so x monotonically decreases — clean ")" arc, no S
    upper_path = bezier_pts((39,43), (28, 30), (27,20))
    for i, (x,y) in enumerate(upper_path):
        t = i / max(len(upper_path)-1, 1)
        col_main = gd if t < 0.5 else gl
        col_edge = gl if t < 0.5 else gh
        if 0 <= x < FW and 0 <= y < FH:
            pix[(x,y)] = col_main
        if 0 <= x+1 < FW and 0 <= y < FH:
            pix.setdefault((x+1,y), col_edge)
        if 0 <= x-1 < FW and 0 <= y < FH:
            pix.setdefault((x-1,y), bd)
        if 0 <= x < FW and 0 <= y-1 < FH:
            pix.setdefault((x,y-1), bd)

    # ── Lower limb: grip bottom (43,49) → tip (52,63)
    # Control inside the endpoint range so x monotonically increases — no S
    lower_path = bezier_pts((43,49), (50, 53), (52,63))
    for i, (x,y) in enumerate(lower_path):
        t = i / max(len(lower_path)-1, 1)
        col_main = gd if t < 0.3 else gl
        col_edge = gl if t < 0.3 else gd
        if 0 <= x < FW and 0 <= y < FH:
            pix[(x,y)] = col_main
        if 0 <= x-1 < FW and 0 <= y < FH:
            pix.setdefault((x-1,y), col_edge)
        if 0 <= x+1 < FW and 0 <= y < FH:
            pix.setdefault((x+1,y), bd)
        if 0 <= x < FW and 0 <= y+1 < FH:
            pix.setdefault((x,y+1), bd)

    # ── String: tip to tip, gentle inward bow (string tension)
    str_path = bezier_pts((29, 20), (40, 42), (53, 62))
    for (x,y) in str_path:
        if 0 <= x < FW and 0 <= y < FH and (x,y) not in pix:
            pix[(x,y)] = sr

    return pix

# ── Weapon frame-0 pixel dicts ────────────────────────────────────────────────
# (Read existing sprites and extract frame 0 as pixel dict)

def extract_f0(path):
    arr = np.array(Image.open(path).convert('RGBA'))
    sl = arr[0:FH, 0:FW]
    pix = {}
    for y in range(FH):
        for x in range(FW):
            if sl[y,x,3] > 0:
                pix[(x,y)] = tuple(sl[y,x])
    return pix

# ── Trail colors per weapon type ──────────────────────────────────────────────

WHITE_TRAIL = (255,255,255,255)
LAV_TRAIL   = (174,161,188,255)

# Staff orb trail colors (per tier)
STAFF_TRAILS = {
    't1': ((180,120,255,255), (220,180,255,255)),   # purple
    't2': ((100,160,255,255), (160,200,255,255)),   # blue sapphire
    't3': ((80,220,120,255), (160,255,180,255)),    # emerald
    't4': ((255,200,60,255), (255,230,120,255)),    # topaz
    't5': ((255,80,80,255),  (255,160,120,255)),    # crimson
    't6': ((200,160,255,255),(160,200,255,255)),    # celestial
}

# ── Main generation ───────────────────────────────────────────────────────────

SRC_PATH = 'sprites/preview_assets/char/sword.png'
OUT_DIR  = 'sprites/preview_assets/char/'

# Female centroid source (use shirt_mage1 which we know exists)
import os
FEMALE_SRC = 'sprites/preview_assets/char/sword.png'  # same — flip is symmetric

# ── Generate all swords ───────────────────────────────────────────────────────
print("\n=== Swords ===")
for tier in ['t1','t2','t3','t4','t5','t6']:
    for g in ['m','f']:
        fname = f'{OUT_DIR}sword_warrior_{tier}_{g}.png'
        if not os.path.exists(fname):
            print(f"  SKIP (not found): {fname}"); continue
        f0 = extract_f0(fname)
        out_path = fname
        build_sheet(f0, SRC_PATH, out_path, weapon_type='sword',
                    trail_c=WHITE_TRAIL, trail_e=LAV_TRAIL)

# ── Generate all staffs ───────────────────────────────────────────────────────
print("\n=== Staffs ===")
for tier in ['t1','t2','t3','t4','t5','t6']:
    tc, te = STAFF_TRAILS.get(tier, (WHITE_TRAIL, LAV_TRAIL))
    for g in ['m','f']:
        fname = f'{OUT_DIR}staff_mage_{tier}_{g}.png'
        if not os.path.exists(fname):
            print(f"  SKIP: {fname}"); continue
        f0 = extract_f0(fname)
        build_sheet(f0, SRC_PATH, fname, weapon_type='staff',
                    trail_c=tc, trail_e=te)

# ── Generate all bows ─────────────────────────────────────────────────────────
print("\n=== Bows ===")

# Bow tier designs — (limb_dark, limb_mid, limb_light, limb_hi, grip_dark, str_color)
BOW_DESIGNS = {
    't1': ((30,15,5,255),(80,48,20,255),(115,75,32,255),(145,100,45,255),(45,28,10,255),(220,210,190,255)),
    't2': ((25,12,5,255),(95,55,20,255),(135,90,35,255),(165,120,50,255),(50,30,12,255),(210,215,200,255)),
    't3': ((20,10,5,255),(60,80,40,255),(90,120,55,255),(120,160,70,255),(30,50,20,255),(180,230,200,255)),
    't4': ((30,10,5,255),(140,60,20,255),(180,90,30,255),(220,130,50,255),(80,25,10,255),(255,200,100,255)),
    't5': ((10,5,20,255), (50,20,80,255),(80,40,120,255),(110,60,160,255),(30,10,50,255),(180,130,255,255)),
    't6': ((10,8,3,255),(180,150,20,255),(220,190,40,255),(255,230,80,255),(100,80,10,255),(255,240,200,255)),
}

for tier in ['t1','t2','t3','t4','t5','t6']:
    design = BOW_DESIGNS[tier]
    f0 = make_bow_frame0(*design)
    # Trail for bow (green-ish arrow streak, no arc)
    for g in ['m','f']:
        src_path = SRC_PATH  # use sword centroid for motion anchor
        out_path = f'{OUT_DIR}bow_ranger_{tier}_{g}.png'
        build_sheet(f0, src_path, out_path, weapon_type='bow',
                    trail_c=(220,200,140,255), trail_e=(180,160,100,255))

print("\nDone.")
