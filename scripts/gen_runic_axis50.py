#!/usr/bin/env python3
"""FIFTIETH net-new-geometry axis for ALL FOUR SLOTS — the RUNIC / EPIGRAPHIC family
(inscription registers): the plate is ruled into horizontal REGISTERS by a raised 2px RULE, and each
sunken channel between rules is CARVED WITH A LINE OF RUNES — angular 3x3 glyphs drawn from a
sixteen-letter alphabet, inlaid in bright wire, set on a common baseline with a clean gap between
one letter and the next.

    the ornament is  RULE    (the raised 2px fillet that divides one register from the next —
                              bright on top, its own shadow below)
                   + CHANNEL (the sunken bed: a dark cut-shadow row under the rule, the glyph
                              zone, and a lighter floor row where light pools at the bottom)
                   + GLYPH   (a rune from the alphabet, inlaid; its top edge catches the light)

*** THIS IS THE FIRST AXIS IN FIFTY WITH A VOCABULARY. ***
The subject of this axis is NOTATION. In every one of the forty-nine prior axes the field is built
from INSTANCES OF ONE ELEMENT — the plate carries a hexagon, or a scale, or an arch, or a shard,
over and over, and any two elements on the plate differ only in where they sit, how big they are, or
how far they are from a root. Here the elements are DIFFERENT FROM ONE ANOTHER BY DESIGN: sixteen
distinct closed forms from a finite alphabet, laid out in a sequence whose order is arbitrary. A
glyph's identity is not derived from anything — not from its position, not from its scale, not from
its parent — it is simply which letter it is. That is a relation no prior axis has, and the four
families it could be confused with each fail it in a different way:

  * The ruled-cell axes (11th-45th) stamp ONE congruent cell on a lattice. Every element is
    identical by construction; the field is a texture and any patch of it is interchangeable with
    any other patch. An inscription is not interchangeable with itself — move it three pixels along
    and you are reading different letters.
  * The 38th egg-and-dart is the nearest thing to a vocabulary in the prior set and is the sharpest
    near miss: it does put TWO different elements on the plate. But they are in STRICT ALTERNATION,
    which means the second element is fully determined by the first, so the pair is really one
    compound cell repeating — a two-syllable texture, not a language. The same is true of the 18th
    basketweave (alternating thread direction) and the 29th houndstooth (a colour-and-weave phase).
  * The 48th cosmati puts three genuinely different elements on the plate at once, and it is the
    other close call — but its ranks are a HIERARCHY: an element's identity IS its size, and knowing
    a Cosmati element is 2px tells you it is a tessera and where in the bay it must sit. All sixteen
    runes here are the same size and sit on the same baseline; size carries nothing.
  * The 46th craquelure is the only prior axis whose field is APERIODIC, and the relation between
    the two is worth stating exactly because it is an INVERSION. Craquelure has an aperiodic CARRIER
    (a jittered Voronoi partition) filled with uniform CONTENT (every shard is the same kind of
    thing, differing only by accident of the jitter). This axis has a strictly periodic carrier —
    the register grid is ruled, the letter pitch is constant, the baseline never wanders — filled
    with aperiodic CONTENT. Craquelure is disorder in the grid; runework is disorder in the text.
    They are the two halves of the same distinction and neither can be mistaken for the other at 1x:
    one has no straight lines anywhere, the other is nothing but straight lines.
  * The 49th dendrite is aperiodic-ish and multi-part, but its parts are ranked by DESCENT and are
    all the same mark; it has no alphabet and no baseline.

WHY IT READS AS WRITING AND NOT AS NOISE, which is the whole risk of a vocabulary axis at 13px.
Three things do the work, and all three are load-bearing:
  (1) The BASELINE. Every glyph in a register starts on the same row and is exactly 3 rows tall, so
      the eye gets a horizontal band of marks of equal height — the single strongest cue for text.
  (2) The GAP. GLYPH_P = 4 = 3 stroke columns + 1 empty column, so letters never touch. Two runes
      that fuse are one blob, and a row of blobs is the 40th dentil.
  (3) The RULE. A 2px raised fillet above and below each line of letters frames the text as a
      REGISTER, exactly as a carved stele or a coin legend does. Without it the marks float and the
      field does read as damage.
The alphabet itself is built for this: every glyph is 4-6 lit pixels of 9, connected, and drawn only
with straight strokes on the three axes a chisel can cut — which is what real rune-rows look like,
because they were carved with the grain of wood and stone.

RELIEF. The inscription is INCISED and then INLAID, so relief runs in two directions at once and the
axis is the first to do that: the rule stands PROUD (bright top pixel, its own shadow beneath), the
channel is SUNK (a dark cut-shadow row immediately under the rule, a lighter floor row at the
bottom where light reaches again), and the wire in the letters stands proud INSIDE the sunken
channel (a glyph pixel with no glyph pixel above it takes the bright inlay stop, the rest the mid).

Geometry per opaque body pixel in component-local (lx, ly), with BAND_P = 7:
    ry = (ly + VPHASE) % BAND_P            VPHASE puts the component's top row on the channel floor
    ry == 0            -> RULE top      (bright, demoted on a silhouette edge — see below)
    ry == 1            -> RULE underside
    ry == 2            -> CUT SHADOW    (the deepest bed stop, under the overhanging rule)
    ry == BAND_P - 1   -> CHANNEL FLOOR (the lifted bed stop)
    else               -> GLYPH ZONE, gy = ry - 3
        gxall = lx - HPHASE;  gcol = gxall % GLYPH_P;  gi = gxall // GLYPH_P
        gcol == 3      -> the inter-letter gap, plain bed
        else           -> VOCAB[hash(register_index, gi)][gy][gcol]

The hash is a deterministic integer mix of (register index, letter index), so the text is the same
every regeneration and male/female of an item carry the SAME inscription — but no two adjacent
letters are related, which is the point.

Per slot it lands as the 50th distinct axis:
  * CHEST  — runecarved cuirass: two full lines of text across the breast.
  * LEGS   — runecarved chausses: a column of letters down each thigh.
  * BOOTS  — runecarved sabatons: a legend around the instep.
  * HELMET — runecarved helm: one inscribed register across the brow, above the visor.

Authoring philosophy identical to gen_dendrite_axis49.py / gen_cosmati_axis48.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Because it never adds a pixel outside
the existing silhouette it CANNOT create isolated pixels, background bleed, or accent-caused
multi-component frames — QA-safe by construction. Sleep frames (fi >= 60) get a plain body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` — the canonical chain (no-smooth shading with protect=False,
shirt pauldron/gorget/chest-plate separation, helmet black eye+mouth visor with NO full-silhouette
rim, hat brim/crease folds for open headgear). See CONTEXT.md "MANDATORY — the finishing pass".

Run from repo root:
  python3 scripts/gen_runic_axis50.py
  python3 scripts/gen_runic_axis50.py --vocab    # ASCII dump of the alphabet + a sample text line
  python3 scripts/gen_runic_axis50.py --swatch   # bare motif on a test plate, no sheets written
  python3 scripts/gen_runic_axis50.py --sweep    # register-pitch sweep on a real torso AND a real leg
Then QA (examples):
  python3 scripts/sprite_qa.py _runic_legendary_preview/shirt_warrior_legendary50.png
  python3 scripts/sprite_qa.py _runicdome_helmet_preview/helmet_mage_legendary50.png --y-min 2
  python3 scripts/sprite_qa.py _runic_boots_preview/boots_warrior_legendary_runic.png --y-max 63
"""
import os
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_mage_ranger_tiers import load, CHAR                 # noqa: E402
from sprite_finish import finish_array, save_finished        # noqa: E402

FW, FH, COLS, NFR = 80, 64, 10, 70
MIN_PX = 12
Q_LO, Q_HI = 0.85, 1.18

# --- Runic constants ------------------------------------------------------------------------
# BAND_P is the vertical period of one REGISTER. Its budget is fixed at both ends: 2px of raised
# rule + 1px of cut shadow + 1px of channel floor = 4px of furniture, so the glyph zone is
# BAND_P - 4 rows and the alphabet needs 3 of them. That makes BAND_P = 7 the smallest pitch at
# which the axis exists at all, which is unusual — most of the fifty have a comfortable range and
# are tuned for taste. This one is tuned for SURVIVAL OF THE ALPHABET, and like the 49th it is
# bounded on BOTH sides by a collapse into an older axis rather than into mush.
# Swept 10/9/8/7/6 (--sweep) on a real torso AND a real leg:
#   10  a 13px torso holds ONE register and a thigh holds none — what is left is a single decorated
#       band across the chest, which is the 8th side-stripe with texture in it, or on a boot the
#       40th dentil. Too sparse and the axis stops being a SURFACE and becomes a belt.
#    9  the torso gets one full register and the top of a second; legs still go a whole limb with no
#       complete line of text. The extra bed rows read as blank plate, not as ornament.
#    8  1.6 registers on the torso, 1 on the leg, with a spare bed row inside each channel. Legible,
#       but the spare row loosens the band and the letters stop reading as sitting ON a baseline.
#    7  two full registers on the torso and nearly two on the thigh, the letters tight to their
#       rules, the whole surface inscribed — chosen.
#    6  the glyph zone drops to 2 rows and the 3-row alphabet is TRUNCATED: of sixteen letters only
#       about five remain distinguishable and the rest degenerate into the same pair of 2-row marks.
#       The vocabulary — which IS the axis — dies, and what is left is a dashed line between rules,
#       i.e. the 40th dentil again. Too dense and it collapses into the same old axis it collapses
#       into when too sparse, from the other direction.
BAND_P = 7        # rows per inscription register: 2 rule + 1 cut shadow + 3 glyph + 1 floor
GLYPH_P = 4       # 3 stroke columns + 1 empty column; letters must never touch
GLYPH_W = 3
GLYPH_H = 3
VPHASE = 6        # puts ly == 0 on the channel FLOOR, so no piece opens on a bright rule

# --- the alphabet ---------------------------------------------------------------------------
# Sixteen letters on a 3x3 chisel grid. Constraints, all deliberate:
#   * 4-6 lit pixels of 9. Below 4 a letter is a tick and the eye files it as damage; above 6 it is
#     a blob and neighbouring letters read as one mark.
#   * connected (8-way at minimum) — a rune is ONE cut, not two.
#   * straight strokes on the vertical, horizontal and the two diagonals only, which is what a
#     chisel working with the grain can actually cut, and what makes the set read as an alphabet
#     rather than as sixteen random bitmaps.
#   * no two letters equal, and no letter equal to another's mirror in the horizontal — a mirrored
#     pair reads as the same letter facing the other way and wastes a slot.
VOCAB = [
    ("X..", "XXX", "X.."),      # 0
    ("XX.", "X..", "XX."),      # 1
    (".X.", "XXX", ".X."),      # 2
    ("XX.", ".X.", ".XX"),      # 3
    (".XX", "XX.", "X.."),      # 4
    ("XXX", ".X.", ".X."),      # 5
    (".X.", ".X.", "XXX"),      # 6
    ("X..", "X..", "XXX"),      # 7
    ("XXX", "X..", "X.."),      # 8
    ("X.X", ".X.", "X.X"),      # 9
    ("XX.", "..X", "XX."),      # 10
    (".X.", "XX.", ".XX"),      # 11
    ("X.X", "XX.", "X.X"),      # 12
    ("X..", "XXX", "..X"),      # 13
    (".XX", "XX.", "..X"),      # 14
    ("X.X", "XXX", ".X."),      # 15
]

# Per class: five STONE stops (rule top / rule underside / cut shadow / bed / floor) and two INLAY
# stops (lit top edge of the wire / the wire's body).
#   * The bed stops must stay well clear of pure black — a HELMET constraint, not a taste one: the
#     finishing pass carves the visor as black eye and mouth pixels, and a near-black bed swallows
#     the face slit outright (the lesson the 49th paid for on its first cut).
#   * Every pale stop is clear of the skin palette. On a narrow female chest the rules are most of
#     what is visible and a warm off-white would read as bare skin at 1x (the 47th's rose gold).
STONE = {
    # oathstone: cold grey granite ruled in pale iron
    'warrior': ((152, 160, 174), (104, 112, 128), (40, 44, 56), (58, 62, 76), (76, 82, 98)),
    # obsidian stele: a violet-black volcanic glass, the first violet ground in the set
    'mage':    ((120, 106, 160), (82, 70, 116), (30, 24, 50), (46, 38, 72), (62, 52, 94)),
    # bog oak: black-brown drowned timber, the runes cut across the grain
    'ranger':  ((142, 118, 82), (98, 78, 52), (34, 30, 22), (52, 46, 32), (68, 60, 42)),
}
INLAY = {
    'warrior': ((242, 248, 255), (186, 200, 220)),   # quicksilver wire
    'mage':    ((176, 255, 246), (96, 206, 208)),    # witchfire, cyan-green against the violet
    'ranger':  ((250, 238, 150), (198, 178, 88)),    # pale gold, pushed yellow-green off skin
}

# Per-class body (ground) tones for the recolor, visible on sleep frames only; taken off the bed
# stops so the piece reads as one object.
BODY = {
    'warrior': ((30, 32, 42), (58, 62, 76), (104, 112, 128)),
    'mage':    ((24, 20, 40), (46, 38, 72), (92, 80, 130)),
    'ranger':  ((26, 22, 16), (52, 46, 32), (98, 84, 56)),
}

# One config block per slot. `largest` restricts the field to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_runic_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary50', largest=True,
    ),
    'legs': dict(
        outdir='_runic_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary50', largest=False,
    ),
    'boots': dict(
        outdir='_runic_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_runic', largest=False,
    ),
    'helmet': dict(
        outdir='_runicdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary50', largest=True,
    ),
}


def glyph_at(bi, gi):
    """Which letter stands at position `gi` of register `bi`.

    A deterministic integer mix rather than a PRNG, for two reasons. First, it must be stable: the
    male and female sheets of one item are generated in separate passes and MUST carry the same
    inscription, or the pair reads as two different objects. Second, it must be positional, so that
    a letter's identity depends on nothing but where it sits in the text — which is what makes the
    sequence aperiodic without being random per-run."""
    h = (bi * 0x9E3779B1 + gi * 0x85EBCA77 + 0xC2B2AE3D) & 0xFFFFFFFF
    h ^= (h >> 15)
    h = (h * 0x2545F491) & 0xFFFFFFFF
    h ^= (h >> 13)
    return VOCAB[h % len(VOCAB)]


def runic_tone(lx, ly, stone, inlay, hphase, edge_top=False, thin=False):
    """Tone for one body pixel at component-local (lx, ly).

    This function dispatches on WHICH LETTER the pixel belongs to, where forty-nine prior axes
    dispatch on where the pixel sits in one repeating cell. Two pixels at the same place in two
    different letters get different answers, and that is the axis.

    `edge_top` / `thin` implement the standing rule that a silhouette edge never carries an extreme
    of the ramp. The bright element here is a CONTINUOUS HORIZONTAL rule, so the way it goes wrong
    is the mirror of the 49th's bright vertical stem: a rule row landing on the topmost row of the
    dome draws a bright bar across the crown of the head, detached from the piece. Where the body
    has nothing above it, or is only 1px across, the rule drops to its underside stop."""
    rule_hi, rule_lo, cut, bed, floor = stone
    ry = (ly + VPHASE) % BAND_P
    if ry == 0:
        return rule_lo if (edge_top or thin) else rule_hi
    if ry == 1:
        return rule_lo
    if ry == 2:
        return cut                              # the rule overhangs the channel: deepest stop
    if ry == BAND_P - 1:
        return floor                            # light reaches the bottom of the cut again
    gy = ry - 3
    if gy >= GLYPH_H:                           # spare bed rows when BAND_P > 7 (sweep only)
        return bed
    gxall = lx - hphase
    gcol = gxall % GLYPH_P
    if gcol >= GLYPH_W:
        return bed                              # the gap between one letter and the next
    pat = glyph_at((ly + VPHASE) // BAND_P, gxall // GLYPH_P)
    if pat[gy][gcol] != 'X':
        return bed
    # the wire stands proud inside the sunken channel: its top edge catches the light
    return inlay[0] if (gy == 0 or pat[gy - 1][gcol] != 'X') else inlay[1]


def paint_runic(fr, comp, stone, inlay):
    """Paint the inscription onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays."""
    if comp.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp)
    y0, x0 = int(ys.min()), int(xs.min())
    w = int(xs.max()) - x0 + 1
    # centre a LETTER on the piece rather than letting the text start on the left bounding edge —
    # a letter cut in half by the silhouette on both sides reads as two ticks, not as text.
    hphase = ((w - GLYPH_W) // 2) % GLYPH_P
    left = np.zeros_like(comp)
    right = np.zeros_like(comp)
    up = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    up[1:, :] = comp[:-1, :]
    thin_m = comp & ~(left & right)
    edge_m = comp & ~up
    for y, x in zip(ys, xs):
        rgb = runic_tone(int(x) - x0, int(y) - y0, stone, inlay, hphase,
                         bool(edge_m[y, x]), bool(thin_m[y, x]))
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free).
    Returns (labels int32 array, n). Background (False) is label 0."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    n = 0
    stack = []
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and labels[sy, sx] == 0:
                n += 1
                labels[sy, sx] = n
                stack.append((sy, sx))
                while stack:
                    y, x = stack.pop()
                    if y > 0 and mask[y - 1, x] and labels[y - 1, x] == 0:
                        labels[y - 1, x] = n
                        stack.append((y - 1, x))
                    if y < h - 1 and mask[y + 1, x] and labels[y + 1, x] == 0:
                        labels[y + 1, x] = n
                        stack.append((y + 1, x))
                    if x > 0 and mask[y, x - 1] and labels[y, x - 1] == 0:
                        labels[y, x - 1] = n
                        stack.append((y, x - 1))
                    if x < w - 1 and mask[y, x + 1] and labels[y, x + 1] == 0:
                        labels[y, x + 1] = n
                        stack.append((y, x + 1))
    return labels, n


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


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    stone, inlay = STONE[cls], INLAY[cls]
    largest = cfg['largest']
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
            lbl, n = label4(a)
            if n >= 1:
                counts = np.bincount(lbl.ravel())
                counts[0] = 0
                comp = (lbl == int(counts.argmax()))
            else:
                comp = a
        else:
            comp = a
        paint_runic(fr, comp, stone, inlay)
        # connectivity guard (no-op by construction: only body pixels repainted)
        da = fr[..., 3] > 0
        lbl2, _ = label4(da)
        keep_labels = set(np.unique(lbl2[a])) - {0}
        keep = np.isin(lbl2, list(keep_labels)) if keep_labels else da
        for y, x in np.argwhere(da & ~keep):
            fr[y, x, :] = 0
    return out


# --- diagnostics ----------------------------------------------------------------------------
def _test_plate(w=44, h=30):
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the
    inscription can be judged on a shape that has the features real slots have."""
    m = np.zeros((h, w), dtype=bool)
    yy, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False          # neck notch
    return m


def swatch(path='_diag_runic_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the registers, the rules
    and the letter-to-letter variation can be judged before any sheet is written."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_runic(a, m, STONE[cls], INLAY[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only — no sheets written)' % path)


def sweep(path='_diag_runic_sweep.png', zoom=11):
    """Render the warrior chest idle frame at a range of register pitches, plus a leg frame, so the
    pitch can be judged on whether A WHOLE LINE OF TEXT survives on a real piece — and, at the
    bottom end, on whether the ALPHABET survives the truncation of the glyph zone."""
    global BAND_P
    keep = BAND_P
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    for p in (10, 9, 8, 7, 6):
        BAND_P = p
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comp = (lbl == int(counts.argmax())) if n else a
            fr = np.zeros_like(src)
            paint_runic(fr, comp, STONE['warrior'], INLAY['warrior'])
            col.append(Image.fromarray(fr).crop(crop))
        cells.append(('BAND_P=%d' % p, col))
    BAND_P = keep
    cw, ch = 28 * zoom, 26 * zoom
    pad, lab = 8, 18
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + 2 * (ch + lab)), (24, 24, 28, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
    except Exception:
        f = ImageFont.load_default()
    x = pad
    for name, col in cells:
        y = pad
        for im in col:
            img.alpha_composite(im.resize((cw, ch), Image.NEAREST), (x, y))
            d.text((x + 2, y + ch), name, font=f, fill=(210, 210, 220, 255))
            y += ch + lab
        x += cw + pad
    img.convert('RGB').save(path)
    print('wrote %s (pitch sweep — no sheets written)' % path)


def dump_vocab():
    """ASCII dump of the alphabet and of a sample inscription, which is the fastest way to confirm
    (a) that no two letters are equal or mirror-equal, (b) that every letter is connected and in the
    4-6 pixel band, and (c) that the hash actually produces a varied text rather than a short cycle
    that would turn the field back into a repeating cell."""
    print('alphabet: %d letters on a %dx%d chisel grid' % (len(VOCAB), GLYPH_W, GLYPH_H))
    for gy in range(GLYPH_H):
        print('  ' + '   '.join(v[gy].replace('X', '#') for v in VOCAB))
    lit = [sum(r.count('X') for r in v) for v in VOCAB]
    print('  lit px per letter: %s  (min %d, max %d)' % (lit, min(lit), max(lit)))
    seen = {}
    for i, v in enumerate(VOCAB):
        for key in (v, tuple(r[::-1] for r in v)):
            if key in seen and seen[key] != i:
                print('  !! letter %d duplicates letter %d (mirror-equal)' % (i, seen[key]))
            seen.setdefault(key, i)
    print('  no duplicate or mirror-duplicate letters' if len(seen) >= len(VOCAB) else '')
    print('\nsample text — 4 registers x 14 letters (as it lands on a plate):')
    for bi in range(4):
        idx = [VOCAB.index(glyph_at(bi, gi)) for gi in range(14)]
        print('  reg %d: %s' % (bi, ' '.join('%2d' % i for i in idx)))
        for gy in range(GLYPH_H):
            print('         ' + ' '.join(VOCAB[i][gy].replace('X', '#').replace('.', ' ')
                                         for i in idx))
    from collections import Counter
    hist = Counter(VOCAB.index(glyph_at(b, g)) for b in range(12) for g in range(12))
    print('\n  letter frequency over 144 positions: %s' % sorted(hist.items()))


def main():
    if '--vocab' in sys.argv:
        dump_vocab()
        return
    if '--swatch' in sys.argv:
        swatch()
        return
    if '--sweep' in sys.argv:
        sweep()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass — never a bespoke shade() in a generator.
                # save_finished() rather than a bare .save(): it writes the TaskQuestFinish
                # version stamp, without which a later bulk `sprite_finish.py <dir>` backfill
                # would run the whole chain over these sheets a SECOND time.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-62s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
