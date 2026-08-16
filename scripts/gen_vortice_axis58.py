#!/usr/bin/env python3
"""FIFTY-EIGHTH net-new-geometry axis for ALL FOUR SLOTS — the VORTICE family (COUNTER-HANDED
SCROLLS): the armour carries a field of small S-scrolls, and every one of them is OFFSET. Two arms
leave each hub, one above it and one below it, and they are thrown to OPPOSITE SIDES; each ends in a
volute curling outward. So a scroll has a HAND — and the scrolls next to it always have the other
one. Two scrolls sharing an edge of the lattice are never the same hand, anywhere on the piece.

    the ornament is  HUB    (the boss the two arms are thrown from)
                   + SPOKE  (the straight bar of an arm — the part that carries no information)
                   + HOOK   (the volute, one pixel curling outward at each arm's end: not what
                             makes the scroll chiral, but what makes a viewer able to SEE that it
                             is — see the note on the ALIGNED control)
                   + SHADE  (the shadow the scroll drops on the plate one row below itself)
                   + FIELD  (the enamel it is set into)
                   + DEEP   (that enamel at the piece's own edge)

*** THIS IS THE FIRST AXIS WHOSE ELEMENT IS CHIRAL. ***
The 57th was the first axis with an UP: turn a festoon over and the chains arch off their studs with
nothing holding them, so the picture is wrong. This is the same discovery made about the OTHER
reflection, and it is a strictly harder one, because a mirror is not a rotation and cannot be undone
by turning the piece in your hands. Take any of the fifty-seven and hold it up to a looking-glass. A
honeycomb comes back a honeycomb. The 44th's chevrons come back chevrons. The 54th's wire comes back
with the same route, the 55th's bands in the same order, the 57th's chains hanging exactly as they
hung. Every one of those motifs is either mirror-symmetric outright, or its mirror is one of its own
rotations, which is the same thing as far as a piece of armour is concerned — you can turn it round
and it is the motif again. THE SCROLL CANNOT BE TURNED BACK. Its mirror is a second object, it is on
the piece too, and the relation between the two of them is the ornament.

So the subject of this axis is not the elements, nor their arrangement, nor a force acting on them,
nor an order they were laid in. The subject is a property an element can have that has NO NUMBER
attached to it — no size, no pitch, no angle, no depth, nothing that can be more or less. A scroll
is one hand or it is the other, and the piece is organised by which.

*** AND THE TWO HANDS ARE THE SAME COLOUR. *** This is the single most important decision in the
file and the easiest one to get wrong. Painting the right-handed scrolls in one metal and the
left-handed ones in another would make the alternation instantly legible — and would make this the
26th TARTAN wearing a scroll, an axis of two COLOURS on a lattice, with the chirality a decoration
riding on top of it. The hands share one palette exactly so that the only thing distinguishing a
scroll from its neighbour is FORM.

Every near miss fails on something that can be CHECKED BY EXHAUSTING THE ROTATION GROUP.
  * The 16th TWILL (herringbone) — the reflex answer, since herringbone is a field that ALTERNATES
    between two mirrored dash directions and does it band by band. It fails on the definition. Its
    element is a straight dash, and a dash is not chiral: the mirror of a "/" is a "\\", and a "\\"
    is a "/" ROTATED A QUARTER TURN. Herringbone's two families are related by a rotation, so
    herringbone has no hands at all — it has two ORIENTATIONS, which is a thing forty of these axes
    have. A scroll's two arms are BOTH present in the same element, offset from each other, and no
    rotation of the whole element can swap which side each one is on.
  * The 44th ZIGZAG — the sharpest VISUAL near miss, because a field of alternating S and Z bars at
    13px is the thing a chevron field looks most like from across the room. It fails on the
    definition too, and cleanly: a chevron is symmetric about its own vertex, so its mirror is
    itself. The difference on the sheet is that a chevron's two limbs MEET, and a scroll's two arms
    DO NOT — they pass either side of the hub, which is the offset, which is the hand.
  * The 24th SPIRAL — the sharpest near miss on the OTHER clause, because a spiral genuinely IS
    chiral. Every spiral on that piece winds the same way, so the handedness is a global constant
    that no one on the piece can see, and mirroring the whole sheet gives back the 24th axis
    unchanged. A property that is constant over the field is not a structure OF the field. That is
    exactly the UNIFORM control: keep the scrolls, make them all one hand, and what comes back is an
    ordinary chiral wallpaper — handsome, and not this.
  * The 23rd MEANDER and the 30th CABLE — both have a handedness for the same reason and lose it the
    same way: one fret, one braid, one hand, everywhere, constant.
  * The 42nd STRIGIL and 11th FLUTING — parallel members with a repeat, and the thing this collapses
    into if the pitch is dropped to 5 and the scrolls run into one another.
  * The 40th DENTIL and 8th SIDE-STRIPE — brackets and bars thrown all the same way off a spine.
    This is precisely the ALIGNED control: throw a scroll's two arms to the SAME side of the hub
    instead of opposite sides, and the element acquires a mirror line through the hub and loses its
    hand — while every pixel count, the pitch, the palette and the lattice stay exactly as they are.
  * The 35th FACET, 36th QUILT, 39th GUILLOCHE, 45th ARCADE, 48th COSMATI — cells on a lattice,
    every one of them mirror-symmetric about its own axis, and every one therefore invariant under
    the operation this axis is about.
  * The 55th STRATA — the closest thing in the set to "the elements stand in a relation to their
    neighbours". Its relation is an ORDER: transitive, antisymmetric, composing into one global
    sequence. This one is an ALTERNATION, which is not an order at all — it is symmetric,
    irreflexive, and composes into a 2-COLOURING. An order has a first and a last; a 2-colouring has
    neither, and swapping its two colours changes nothing.
  * The 53rd GRANULATION and 47th MOKUME — the two axes whose element is determined by the body.
    Both determine a SCALAR, and a scalar has no hands.

Geometry, per connected component, in the component's own frame:
    lattice    hubs on a square lattice of pitch PITCH, phase chosen per component from a ladder
    scroll     hub + two arms, the upper thrown one way and the lower the other, each a straight bar
               of length ARM ending in a volute that curls one pixel further outward
    hand       hand(i, j) = the parity of i + j on the lattice, so no two lattice-adjacent scrolls
               ever share a hand — the alternation is a proper 2-colouring, and it is a 2-colouring
               of the same graph a checkerboard is, which is why it exists at all
    complete   a scroll is set only if EVERY one of its pixels lands on the piece. A clipped scroll
               is not a smaller scroll; it is a scroll with its hand cut off, and the acceptance
               test below is only meaningful because every scroll on the sheet can be read whole.
    relief     SHADE one row under every scroll pixel, so the scroll stands off its enamel

Authoring philosophy identical to gen_festoon_axis57.py / gen_slotwork_axis56.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing is added, nothing removed, the
silhouette is untouched, so the generator CANNOT create isolated pixels, background bleed, extra
components or a changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Fourteenth generator to call it in-line, after axes 45-57.

Run from repo root:
  python3 scripts/gen_vortice_axis58.py
  python3 scripts/gen_vortice_axis58.py --cells    # ASCII dump + the CHIRALITY acceptance test
  python3 scripts/gen_vortice_axis58.py --accept   # that test over every component of every frame
  python3 scripts/gen_vortice_axis58.py --swatch   # bare motif on a test plate, no sheets
  python3 scripts/gen_vortice_axis58.py --sweep    # pitch sweep + ALIGNED/UNIFORM/MIRROR controls
Then QA (examples):
  python3 scripts/sprite_qa.py _vortice_legendary_preview/shirt_warrior_legendary58.png
  python3 scripts/sprite_qa.py _vorticedome_helmet_preview/helmet_mage_legendary58.png --y-min 2
  python3 scripts/sprite_qa.py _vortice_boots_preview/boots_warrior_legendary_vortice.png --y-max 63
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

R_HUB, R_HOOK, R_SPOKE, R_SHADE, R_FIELD, R_DEEP = 0, 1, 2, 3, 4, 5

# --- The motif ---------------------------------------------------------------------------------
# A scroll is authored, not drawn: give it a radius and a number of arms and the cells fall out. The
# hook is a SINGLE pixel per arm and that is not a budget decision, it is the point — at this scale
# the difference between this axis and the 27th SUNBURST is exactly four pixels, one per arm, and if
# the difference needed more than that it would not be a difference of KIND.
#
# *** THE FIRST MOTIF WAS THROWN OUT ON SIGHT, AND IT IS WORTH RECORDING WHY. ***
# The obvious chiral element at this scale is a four-armed pinwheel: a hub, four arms on the
# cardinal directions, and a one-pixel hook at the end of each turning the same way round. It is
# chiral, it passes every clause below, it tiles, and rendered at 26x on the hands panel it is
# unmistakably a SWASTIKA. There is no palette, pitch or arm length that fixes that — the glyph IS
# a four-armed hooked cross — so the whole family is unusable and no amount of it being
# geometrically correct matters. Four arms are out.
#
# What replaces it is the S-SCROLL, and it happens to be a better statement of the axis anyway.
# TWO arms leave the hub, one above and one below, and they are thrown to OPPOSITE SIDES of it. Each
# ends in a VOLUTE — one pixel turning outward, the terminal curl of a scroll. It is the running
# scroll of every cornice and every illuminated border, it is the S and Z of the S/Z tetromino, and
# it carries its hand in a completely different place from the pinwheel: not in a rotation, but in
# WHICH WAY THE TWO ARMS ARE OFFSET FROM EACH OTHER.
#
# That relocation matters for the controls. The pinwheel loses its hand if you unbend the hooks; the
# scroll does NOT — a bare Z-bar with no volutes at all is still chiral, because the offset is still
# there. So the control that kills this motif is not "unbend it" but ALIGNED: throw both arms to the
# SAME side. The element then acquires a mirror line through the hub, and an element with a mirror
# line has no hand, whatever else is done to it. The volutes are what make the hand LEGIBLE at 13px;
# the offset is what makes it EXIST.
def _scroll(arm, hook=True, aligned=False):
    """Cells of ONE right-handed scroll as {(dx, dy): role}, hub at the origin.

    The upper arm (y = -1) runs right, the lower arm (y = +1) runs left, and each turns one pixel
    further outward at its end. `aligned` throws both arms the same way, which is the control.
    """
    cells = {(0, 0): R_HUB}
    for sgn in (+1, -1):
        y = -sgn
        d = 1 if aligned else sgn
        for k in range(0, arm + 1):
            cells[(d * k, y)] = R_SPOKE
        if hook:
            cells[(d * arm, 2 * y)] = R_HOOK
    cells[(0, 0)] = R_HUB
    return cells


# STANDARD gauge. Arms of length 2 with volutes: 9 pixels in a 5x5 box, of which 2 are volutes.
#   arm 1     the two arms are two pixels each, so the offset between them is a single pixel step
#             and the scroll reads as a lumpy dot. This gauge exists anyway, as THIN, for pieces
#             that can hold nothing bigger, and it drops the volutes to stay inside a 3x3.
#   arm 2     CHOSEN. Three pixels of straight bar, then a turn: the eye gets a direction
#             established and then broken, which is the whole read.
#   arm 3     a 7x7 box needs pitch 8, and a 13px torso then carries ONE scroll. One scroll has no
#             neighbour, and with no neighbour there is no alternation and no axis — it is a
#             NAMED MEDALLION IN A FIXED PLACE, which this set has as the 8th AEGIS ROUNDEL.
ARM = 2

# The lattice pitch. It has ONE hard constraint and it is asserted below: a scroll's box must not
# touch its neighbour's, or two scrolls fuse into one blob and the acceptance test reads the fused
# pair as a single unreadable element. Box side is 2*radius + 1, so PITCH > 2*radius + 1.
#   pitch 5   the boxes touch. Rendered, a scroll's lower volute lands against the next one's upper
#             bar and the field turns into a continuous ladder — which is the 42nd STRIGIL.
#   pitch 6   CHOSEN. Exactly one row of enamel between neighbouring scrolls, which is where the
#             shadow goes.
#   pitch 8   a 13px torso holds one column of scrolls, so all the alternation left on the piece is
#             vertical, and half of the axis is missing from half of the slots.
PITCH = 6

# Gauges for components too narrow for the standard scroll. Same shape of fallback as the 52nd's
# MARGIN_MIN, the 53rd's shot pass, the 54th's adaptive pitch, the 55th's spread, the 56th's phase
# and the 57th's THIN/TINY rhythms — the seventh appearance of the adaptive-boundary lesson, and the
# reason it keeps appearing is that a chausse leg is four pixels across and still has to carry the
# axis. Each gauge names its own motif and its own pitch; the assert below holds all of them.
#
# THIN drops the volutes, and that is not a compromise, it is the thing the ALIGNED control proves:
# the hand lives in the OFFSET, not in the curl. A bare S-pentomino — hub, one pixel up-and-right,
# one pixel down-and-left — is chiral, and the acceptance test below confirms it by exhaustion the
# same way it confirms the big one.
STD = dict(arm=ARM, hook=True, pitch=PITCH)
THIN = dict(arm=1, hook=False, pitch=4)

# *** THE MINIMAL CHIRAL POLYOMINO, AND IT IS NOT AN ARBITRARY SHAPE. ***
# Below the THIN gauge there is nothing left to shrink: a boot at this scale is a 3-to-4px-wide,
# 6px-tall L. So the last gauge is the SMALLEST SET OF PIXELS THAT CAN HAVE A HAND AT ALL — the S/Z
# tetromino, four pixels in a 2x3 box. Three pixels cannot do it: every triomino's mirror is one of
# its own rotations (the L-triomino is the near miss, and it is exactly the trap, because it LOOKS
# bent). This is the counterpart of the 57th's PENDANT, which is that axis's own element at span
# zero: it is not a second ornament bolted on to rescue the small pieces, it is this axis's own
# statement with everything removed that is not the hand.
TINY = dict(cells={(0, 0): R_HUB, (0, -1): R_SPOKE, (1, 0): R_SPOKE, (1, 1): R_HOOK}, pitch=4)

GAUGES = ('std', 'thin', 'tiny')


def gauge_cells(mode, aligned=False):
    if mode == 'tiny':
        # ALIGNED at this gauge collapses the tetromino onto the straight vertical triomino, whose
        # mirror is itself — the smallest possible statement that an aligned element has no hand.
        return ({(0, -1): R_SPOKE, (0, 0): R_HUB, (0, 1): R_SPOKE} if aligned
                else dict(TINY['cells']))
    p = STD if mode == 'std' else THIN
    return _scroll(p['arm'], hook=p['hook'], aligned=aligned)


def gauge_pitch(mode):
    return {'std': STD['pitch'], 'thin': THIN['pitch'], 'tiny': TINY['pitch']}[mode]


def _radius_of(cells):
    return max(max(abs(x), abs(y)) for x, y in cells)


# *** THE ONE HARD INVARIANT IN THIS FILE. *** A scroll's box must clear its neighbour's, or the two
# fuse and the reader below extracts a shape that is neither hand. Asserted at import for the same
# reason the 57th asserts TIER_P >= SAG_MAX + 3: breaking it is SILENT — the sheet still renders,
# still passes sprite_qa, and is simply not this axis any more.
for _m in GAUGES:
    _c = gauge_cells(_m)
    assert gauge_pitch(_m) > 2 * _radius_of(_c), (
        '%s: pitch %d does not clear a scroll of radius %d'
        % (_m, gauge_pitch(_m), _radius_of(_c)))

# A component with fewer than this many INTERIOR pixels is all boundary and cannot hold the standard
# scroll. Same constant and the same measured reason as the 52nd through 57th.
MARGIN_MIN = 20

# Per class, SIX stops: (hub, hook, spoke, shade, field, deep).
#   * ONE METAL FOR BOTH HANDS. See the header. If the hands were two colours this would be the 26th
#     TARTAN and the chirality would be riding along on top of a colour alternation that is doing
#     all the work. They are the same metal, lit the same way, and they differ only in shape.
#   * THE HOOK IS NOT THE BRIGHTEST STOP, AND THAT IS DELIBERATE. The instinct is to put the
#     brightest tone on the pixel that carries the axis. Measured on the swatch, that reads as four
#     loose sparks orbiting a dot — the hooks separate from their own arms and the scroll stops being
#     one object. HUB brightest, HOOK one step down, SPOKE one step below that: the arm then reads
#     as an arm that gets brighter toward its end and TURNS, which is what a bent metal spoke
#     catching a light from above actually does.
#   * THE HUE PLAN, chosen against the tiers this one will sit beside. 54th platinum on oxblood,
#     55th blackened iron on pale steel, 56th cool steel on hide, 57th three metals on saturated
#     TEXTILE. This one is metal on ENAMEL — hard, glassy, darker than the textile and more
#     saturated than the hides — and no class wears the metal it wore in 54-57: warrior COPPER (54
#     platinum, 55 blackened iron, 56 cool steel, 57 gold), mage PALE JADE (54 amber-gold, 55
#     amethyst, 56 ice-blue, 57 moon silver), ranger PEWTER (54 copper, 55 bog-oak, 56 bone, 57
#     verdigris bronze). Fields are DEEP TEAL / WARM UMBER / BURNT SIENNA, none of them used before.
#   * NO STOP NEAR PURE BLACK. The finishing pass carves the visor as black eye and mouth pixels and
#     a near-black darkest stop swallows them (the 49th's lesson). Every class's darkest stop —
#     SHADE — clears channel-sum 150: warrior 162, mage 150, ranger 158.
VORTICE = {
    # copper scrolls set into deep teal enamel.
    # *** THE HUB WAS FIRST (247,214,186) AND THAT IS A FACE. *** Rendered on the slots diagnostic,
    # the warrior hubs came out as pale peach specks sitting squarely on the skin ramp — the 47th's
    # lesson, and copper is the one metal in the set that walks into it, because a copper HIGHLIGHT
    # desaturates toward tan exactly the way lit skin does. Pulled back to a saturated copper that
    # is lighter than the hook and still unmistakably orange: the scroll stays one metal in three
    # tones and none of the three could be mistaken for a hand.
    'warrior': ((240, 178, 128), (206, 138, 90), (162, 98, 58),
                (30, 66, 66), (52, 110, 110), (38, 82, 82)),
    # pale-jade scrolls set into warm umber enamel
    'mage':    ((222, 248, 236), (176, 220, 200), (120, 170, 154),
                (66, 48, 36), (108, 76, 56), (84, 60, 44)),
    # pewter scrolls set into burnt-sienna enamel
    'ranger':  ((222, 230, 240), (176, 190, 208), (124, 140, 162),
                (78, 46, 34), (124, 74, 52), (98, 58, 42)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only: the enamel ramp plus the
# scroll's mid tone as the highlight, so the piece still reads as one object when no scroll is drawn.
BODY = {
    'warrior': ((38, 82, 82), (52, 110, 110), (206, 138, 90)),
    'mage':    ((84, 60, 44), (108, 76, 56), (176, 220, 200)),
    'ranger':  ((98, 58, 42), (124, 74, 52), (176, 190, 208)),
}

SLOTS = {
    'chest': dict(
        outdir='_vortice_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary58', largest=True,
    ),
    'legs': dict(
        outdir='_vortice_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary58', largest=False,
    ),
    'boots': dict(
        outdir='_vortice_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_vortice', largest=False,
    ),
    'helmet': dict(
        outdir='_vorticedome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary58', largest=True,
    ),
}

# The standing edge rule — brightest stop never on the silhouette, darkest stop never on the
# silhouette — applied by DEMOTION on boundary pixels. HOOK demotes to SPOKE and NOT to FIELD: a
# hook is the axis, and a hook that falls on the outline must get quieter, never disappear.
DEMOTE = {R_HUB: R_HOOK, R_HOOK: R_SPOKE, R_SPOKE: R_SPOKE,
          R_SHADE: R_DEEP, R_FIELD: R_DEEP, R_DEEP: R_DEEP}

_ROLE_CACHE = {}


# --- chirality, as a group action --------------------------------------------------------------
# Everything below operates on SETS OF CELLS, never on the parameters the cells were built from.
# That is the whole discipline of the acceptance test: the question "is this thing chiral" is
# answered by exhausting a group on the pixels, not by remembering that a hook was requested.
def _rot(cells):
    """One quarter turn about the hub: (x, y) -> (-y, x). Roles ride along with their cells."""
    return {(-y, x): r for (x, y), r in cells.items()}


def _mir(cells):
    """The reflection x -> -x. Any reflection will do; they differ from each other by a rotation."""
    return {(-x, y): r for (x, y), r in cells.items()}


def _norm(cells):
    return frozenset(cells)


def rotations(cells):
    out, c = [], dict(cells)
    for _ in range(4):
        out.append(_norm(c))
        c = _rot(c)
    return out


def is_chiral(cells):
    """CLAUSE 1, and the definition the whole axis rests on: a shape is chiral iff its mirror image
    is NOT one of its own rotations. Checked by exhausting the four rotations against the mirror —
    four comparisons, no geometry, no formula, no appeal to how the shape was built.

    This is what tells a scroll from a herringbone dash. The mirror of "/" is "\\", and "\\" is "/"
    turned a quarter turn, so a dash comes back unchanged and has no hand. The mirror of a scroll is
    a scroll that turns the other way, and no amount of turning the piece will fix it.
    """
    return _norm(_mir(cells)) not in rotations(cells)


def hand_of(patch):
    """Read a scroll's HAND off a set of pixels: +1 if the set is some rotation of the right-handed
    motif, -1 if it is some rotation of the left-handed one, 0 if it is neither.

    Note what this is NOT: it does not consult the lattice parity the scroll was painted from, and it
    does not consult the cell dictionary the painter used. It takes the pixels that are on the sheet
    and asks which of two objects they are a copy of. If the paint disagreed with the layout — a
    clipped arm, a neighbour's hook bleeding into the box, a demotion that ate a pixel — the answer
    comes back 0 and the acceptance test fails, which is exactly what it is for.

    It is also well defined, and it is clause 1 that makes it so: if the motif is chiral then no
    rotation of the right hand is ever equal to any rotation of the left, so at most one of the two
    can match. A scroll cannot be both hands, and the reader cannot quietly pick one.
    """
    p = _norm(patch)
    for mode in GAUGES:
        base = gauge_cells(mode)
        if p in rotations(base):
            return +1
        if p in rotations(_mir(base)):
            return -1
    return 0


def _neighbours(comp):
    left = np.zeros_like(comp)
    right = np.zeros_like(comp)
    up = np.zeros_like(comp)
    down = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    up[1:, :] = comp[:-1, :]
    down[:-1, :] = comp[1:, :]
    return left, right, up, down


def _interior(comp):
    left, right, up, down = _neighbours(comp)
    return comp & left & right & up & down


def _has_interior(comp):
    return int(_interior(comp).sum()) >= MARGIN_MIN


# --- layout ------------------------------------------------------------------------------------
def _layout_once(comp, mode, phx, phy, aligned=False, uniform=False, parity=0):
    """Set the scrolls on one component at one lattice phase.

    Returns a list of dicts: lattice index (i, j), hub pixel (cy, cx), intended hand, and the cells.
    A scroll is set only if EVERY pixel of it lands on the piece — see the header. That completeness
    rule is doing more work here than in any previous axis, because a clipped scroll does not merely
    look worse, it stops HAVING A HAND: three arms and a stump is a shape whose mirror IS one of its
    rotations, and the reader would be right to reject it.
    """
    h, w = comp.shape
    pitch = gauge_pitch(mode)
    right = gauge_cells(mode, aligned=aligned)
    left = _mir(right)
    out = []
    j = 0
    cy = phy
    while cy < h:
        i = 0
        cx = phx
        while cx < w:
            hand = +1 if (uniform or (i + j + parity) % 2 == 0) else -1
            cells = right if hand > 0 else left
            ok = True
            for (dx, dy) in cells:
                y, x = cy + dy, cx + dx
                if not (0 <= y < h and 0 <= x < w and comp[y, x]):
                    ok = False
                    break
            if ok:
                out.append(dict(i=i, j=j, cy=cy, cx=cx, hand=hand, cells=cells, mode=mode))
            i += 1
            cx += pitch
        j += 1
        cy += pitch
    return out


def _paint_roles(comp, scrolls):
    """Turn a set of placed scrolls into a role field. Shadows for ALL scrolls first, then the scrolls
    themselves, so a shadow can never land on top of a neighbour's arm — the same ordering rule the
    57th uses, and the reason the reader below can trust its boxes."""
    h, w = comp.shape
    role = np.where(comp, R_FIELD, -1).astype(np.int8)
    for wh in scrolls:
        for (dx, dy) in wh['cells']:
            y, x = wh['cy'] + dy + 1, wh['cx'] + dx
            if 0 <= y < h and comp[y, x] and role[y, x] == R_FIELD:
                role[y, x] = R_SHADE
    for wh in scrolls:
        for (dx, dy), r in wh['cells'].items():
            role[wh['cy'] + dy, wh['cx'] + dx] = r
    return role


def _read_patch(role, cy, cx, rad):
    """Pull one scroll back OFF THE PAINTED PIXELS: every pixel in the box around the hub whose role
    is HUB, HOOK or SPOKE, as offsets from the hub. Because PITCH > 2*rad (asserted at import) this
    box cannot contain any part of a neighbour, so what comes back is one scroll and nothing else."""
    h, w = role.shape
    out = set()
    for dy in range(-rad, rad + 1):
        for dx in range(-rad, rad + 1):
            y, x = cy + dy, cx + dx
            if 0 <= y < h and 0 <= x < w and role[y, x] in (R_HUB, R_HOOK, R_SPOKE):
                out.add((dx, dy))
    return out


def read_hands(role, scrolls):
    """Every scroll's hand, READ, plus the lattice index it was set at. Returns a list of
    (i, j, read_hand, intended_hand)."""
    out = []
    for wh in scrolls:
        rad = _radius_of(wh['cells'])
        patch = _read_patch(role, wh['cy'], wh['cx'], rad)
        out.append((wh['i'], wh['j'], hand_of(patch), wh['hand']))
    return out


# ---------------------------------------------------------------------------------------------
# THE ACCEPTANCE TEST — a GROUP ACTION read off the painted pixels.
#
# Every previous axis is accepted on a STATISTIC of its field (46th cell count, 48th size ratio,
# 50th glyph survival, 52nd distinct-hole appearances, 53rd radius histogram), on its TOPOLOGY
# (54th), on the ALGEBRA of an order relation (55th), on a CONSERVATION LAW along a traversal (56th)
# or on a PHYSICAL LAW (57th). This axis's content is that its element has a property no measurement
# returns — chirality is not a quantity, it is a fact about a SYMMETRY GROUP — so it is accepted by
# EXHAUSTING THAT GROUP on the pixels:
#
#   (1) CHIRAL       the motif's mirror is not any of its four rotations. Four set comparisons.
#                    This is the clause the ALIGNED control fails, and it fails on the FIRST scroll,
#                    because it is a fact about the element and not about the field.
#   (2) READABLE     every scroll on the piece matches some rotation of exactly ONE of the two
#                    hands. A clipped, fused or overpainted scroll matches neither: a violation.
#   (3) ALTERNATION  no two lattice-adjacent scrolls share a hand — a proper 2-colouring of the
#                    adjacency graph, verified on the hands that were READ, never on the parity they
#                    were painted from. This is the clause the UNIFORM control fails.
#   (4) BOTH HANDS   over a sheet, both hands occur, and in near-equal numbers. A population clause,
#                    asked of a sheet and not of a component, for the 57th's reason: a 13px boot may
#                    hold one scroll, and "the scrolls on this piece differ" is not a question one
#                    scroll can answer.
#
# *** WHAT IS DELIBERATELY NOT A CLAUSE, AND IT IS THE MOST INTERESTING THING IN THE FILE. ***
# The obvious fifth clause is the 57th's FLIP written for a mirror: reflect the finished sheet and
# demand that the acceptance test now FAIL, the way flipping a festoon makes the chains arch. IT
# DOES NOT FAIL, AND IT SHOULD NOT. Mirroring the field turns every right hand into a left and every
# left into a right, so all four clauses above still hold, exactly. The MIRROR control in --sweep
# renders this and reports it as a MEASUREMENT rather than a failure, the way the 56th reports LOCK
# and the 57th reports LINEAR — and the honest statement of it is worth having:
#
#     every element of this field is chiral, and the field is not.
#
# The alternation is an ACHIRAL STRUCTURE ASSEMBLED OUT OF CHIRAL PARTS. That is not a weakness in
# the axis, it is what distinguishes it from the 24th SPIRAL: a field with a global handedness is a
# field whose handedness nobody can see, because there is nothing on the piece to compare it with.
# Here both hands are present at every point of the piece, each one is the other's evidence, and
# what the mirror does is exchange two things that are both already there.
# ---------------------------------------------------------------------------------------------
def accepts(role, scrolls):
    """Clauses 1-3, on ONE COMPONENT."""
    if not scrolls:
        return False, 'no scroll is set on this component at any phase'
    for mode in {wh['mode'] for wh in scrolls}:
        if not is_chiral(gauge_cells(mode)):
            return False, ('the %s motif is its own mirror under some rotation: it has no hand'
                           % mode)
    hands = read_hands(role, scrolls)
    seen = {}
    for i, j, got, want in hands:
        if got == 0:
            return False, ('a scroll at lattice (%d,%d) reads as neither hand — it is clipped, '
                           'fused with a neighbour, or overpainted' % (i, j))
        if got != want:
            return False, ('the scroll at lattice (%d,%d) was set %s-handed and reads %s-handed'
                           % (i, j, 'right' if want > 0 else 'left',
                              'right' if got > 0 else 'left'))
        seen[(i, j)] = got
    for (i, j), hval in seen.items():
        for (di, dj) in ((1, 0), (0, 1)):
            nb = seen.get((i + di, j + dj))
            if nb is not None and nb == hval:
                return False, ('two scrolls sharing a lattice edge at (%d,%d) turn the same way'
                               % (i, j))
    return True, 'every scroll has a hand; no two neighbours share one'


def _params_for(comp):
    return ['std', 'thin', 'tiny'] if _has_interior(comp) else ['thin', 'tiny']


def set_whorls(comp, aligned=False, uniform=False, force_mode=None, force_pitch=None, parity=0):
    """Set the scrolls on a component: walk the phase ladder and keep the phase that puts BOTH HANDS
    on the piece, ties broken by total count and then toward the lowest phase. Falls back through
    the THIN and TINY gauges for components too narrow for the standard scroll.

    *** SCORED ON min(nRIGHT, nLEFT) FIRST AND ON COUNT SECOND, AND THAT ORDER IS THE 57th's LESSON
    APPLIED TO A DIFFERENT QUANTITY. *** The 57th learned to score its offset ladder on TOTAL SAG
    rather than on chain count, because count answers a question the axis is not about. The same
    thing is true here and it bites harder: scored on count alone, a torso's best phase puts four
    scrolls down a single column, which is four scrolls of ALTERNATING hand only if the column is
    read vertically — but measured, the phases that maximise count are the ones that hug the
    component's long axis, and on a 4px chausse leg they returned a column of scrolls that were ALL
    THE SAME HAND, because only every second lattice row had room. A field of one hand is the 24th
    SPIRAL, i.e. the axis is gone while every scroll is still there. Scoring on min(nR, nL) asks the
    question the axis is actually about: where on this body can BOTH hands be seen at once?

    Returns (role, scrolls, mode).
    """
    key = (comp.shape, comp.tobytes(), aligned, uniform, force_mode, force_pitch, parity)
    hit = _ROLE_CACHE.get(key)
    if hit is not None:
        return hit
    modes = [force_mode] if force_mode else _params_for(comp)
    best = None
    for mode in modes:
        pitch = force_pitch or gauge_pitch(mode)
        cand = None
        for phy in range(pitch):
            for phx in range(pitch):
                wl = _layout_once(comp, mode, phx, phy, aligned=aligned, uniform=uniform,
                                  parity=parity)
                nr = sum(1 for wh in wl if wh['hand'] > 0)
                nl = len(wl) - nr
                score = (min(nr, nl), len(wl))
                if cand is None or score > cand[0]:
                    cand = (score, mode, wl)
        if best is None or cand[0] > best[0]:
            best = cand
        # *** THE GAUGE IS CHOSEN BY WHETHER BOTH HANDS FIT, NOT BY WHETHER ANYTHING FITS, AND
        # THIS IS A RENDER-PAID LESSON. *** The first version dropped to the next gauge only when
        # the current one placed NO scroll at all. Measured, that is the wrong question: a chausse
        # leg and a 16px boot each held EXACTLY ONE standard scroll, the loop saw a non-zero count
        # and stopped, and the pieces came out with a single pinwheel at the hip and bare enamel
        # below it — a NAMED MEDALLION IN A FIXED PLACE, which is the 8th AEGIS ROUNDEL, and worse,
        # a piece carrying one hand and therefore no alternation at all. One scroll is not a small
        # amount of this axis; it is none of it, because the axis is a RELATION BETWEEN TWO WHORLS
        # and one scroll has no neighbour to stand in it. So a gauge is accepted only when it puts
        # both hands on the piece, and the leg drops to THIN — smaller scrolls, four times as many,
        # and the alternation legible down the whole thigh.
        if best[0][0] > 0:
            break
    score, mode, scrolls = best
    role = _paint_roles(comp, scrolls)
    out = (role, scrolls, mode)
    _ROLE_CACHE[key] = out
    return out


def paint_vortice(fr, comp_full, stops, **kw):
    """Paint the scroll field onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette."""
    if comp_full.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    role = set_whorls(comp, **kw)[0]
    interior = _interior(comp)
    boundary = comp & ~interior

    for y, x in zip(ys, xs):
        ly, lx = int(y) - y0, int(x) - x0
        r = int(role[ly, lx])
        if r < 0:
            continue
        rgb = stops[DEMOTE[r]] if boundary[ly, lx] else stops[r]
        fr[y, x, :3] = rgb
        fr[y, x, 3] = 255


def label4(mask):
    """Self-contained 4-connectivity connected-component labelling (scipy-free)."""
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


def comps_of(a, largest):
    lbl, n = label4(a)
    if n < 1:
        return []
    if largest:
        counts = np.bincount(lbl.ravel())
        counts[0] = 0
        return [(lbl == int(counts.argmax()))]
    return [(lbl == i) for i in range(1, n + 1)]


def comps_ordered(a, largest):
    """The components of a frame, each with a HAND PARITY, ordered left to right by centroid.

    *** WHEN A COMPONENT CAN HOLD ONLY ONE WHORL, ITS NEIGHBOUR IS THE OTHER COMPONENT. ***
    Measured over the batch, a boot at this scale is a 16-pixel L three or four pixels across and it
    holds exactly ONE scroll at every gauge and every phase — so the alternation, which is the whole
    axis, has nothing to happen between. Leaving it there would put the SAME hand on both boots of
    every pair, in every frame, side by side: the 24th SPIRAL, twice over, in the most conspicuous
    place on the sprite. So the parity of the lattice is offset by the component's own rank from the
    left, and the left boot and the right boot counter-turn.

    This is the same move the 57th makes with its PENDANT — the axis's own statement with everything
    removed that is not the subject — and it is arguably a stronger one, because it is not a reduced
    element but the SAME RELATION READ ONE SCALE UP: if two scrolls on a plate must turn opposite
    ways, so must two plates. It applies to the large components too, where it merely chooses which
    phase of the checkerboard they start on, so there is one rule and not two.

    Ordered by centroid rather than by label id on purpose: label order is raster-scan order, which
    swaps the two boots the moment one lifts above the other in a walk cycle, and the pair would
    then flip hands mid-stride.
    """
    cs = comps_of(a, largest)
    key = []
    for k, c in enumerate(cs):
        ys, xs = np.nonzero(c)
        key.append((float(xs.mean()), float(ys.mean()), k))
    order = sorted(range(len(cs)), key=lambda k: key[k])
    return [(cs[k], rank % 2) for rank, k in enumerate(order)]


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    stops = VORTICE[cls]
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
        # ONE LATTICE PER CONNECTED COMPONENT. A scroll is a thing riveted to a plate, and the
        # alternation is a statement about NEIGHBOURS ON THAT PLATE — two scrolls on opposite legs of
        # a pair of chausses are not neighbours in any sense a viewer can use, so a single lattice
        # spanning the bounding box would assert an adjacency that does not exist. (The 54th's
        # lesson, and the 57th's; here it is also what keeps the acceptance test honest.)
        for comp, parity in comps_ordered(a, largest):
            paint_vortice(fr, comp, stops, parity=parity)
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
    scroll field can be judged on a shape with the features the real slots have."""
    m = np.zeros((h, w), dtype=bool)
    _, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False
    return m


def swatch(path='_diag_vortice_swatch.png', zoom=12):
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_vortice(a, m, VORTICE[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def _big_comp(arr, fi=0):
    r, c = fi // COLS, fi % COLS
    src = arr[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def sweep(path='_diag_vortice_sweep.png', zoom=11):
    """Warrior chest and leg idle frames across the lattice pitch, plus the three CONTROLS.
    ALIGNED is the one to look at: it is this generator's own output with the lower arm thrown the
    same way as the upper one, so the hub, the arm length, the volutes, the lattice, the pixel count
    and the palette are all identical and the ONLY thing that has changed is which side of the hub
    one arm sits on. What comes back is a bracket — the 40th DENTIL — and it has no hand."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    variants = [('PITCH 6', dict()), ('PITCH 7', dict(force_pitch=7)),
                ('PITCH 8', dict(force_pitch=8)), ('THIN', dict(force_mode='thin')),
                ('TINY', dict(force_mode='tiny')),
                ('ALIGNED', dict(aligned=True)), ('UNIFORM', dict(uniform=True)),
                ('MIRROR', dict(_mirror=True))]
    cells = []
    for name, kw in variants:
        kw = dict(kw)
        do_mirror = kw.pop('_mirror', False)
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            comp = _big_comp(arr)
            fr = np.zeros_like(arr[0:FH, 0:FW])
            paint_vortice(fr, comp, VORTICE['warrior'], **kw)
            im = Image.fromarray(fr)
            if do_mirror:
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            col.append(im.crop(crop))
        cells.append((name, col))
    cw, ch = 28 * zoom, 26 * zoom
    pad, lab = 8, 18
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad * 2 + 2 * (ch + lab)),
                    (24, 24, 28, 255))
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
    print('wrote %s (pitch sweep + ALIGNED/UNIFORM/MIRROR controls - no sheets written)' % path)


def slots_diag(path='_diag_vortice_slots.png', zoom=10):
    """All three classes x all four slots, bare motif, no finishing pass."""
    srcs = [('chest', 'armor_chest_4.png', 'shirt_mage4.png', 'shirt_ranger4.png', True),
            ('legs', 'armor_pants_4.png', 'pants_mage4.png', 'pants_ranger4.png', False),
            ('boots', 'armor_boots_4.png', 'boots_mage4.png', 'boots_ranger4.png', False),
            ('helmet', 'helmet_rare1.png', 'helmet_mage4.png', 'helmet_ranger4.png', True)]
    crop = (26, 12, 58, 60)
    cw, chh = (crop[2] - crop[0]) * zoom, (crop[3] - crop[1]) * zoom
    pad, lab = 8, 16
    img = Image.new('RGBA', (pad + 4 * (cw + pad), pad + 3 * (chh + lab)), (24, 24, 28, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)
    except Exception:
        f = ImageFont.load_default()
    for ci, (kind, wf, mf, rf, largest) in enumerate(srcs):
        for ri, (cls, fn) in enumerate((('warrior', wf), ('mage', mf), ('ranger', rf))):
            arr = load_any(fn)
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            fr = np.zeros_like(src)
            recolor(src, fr, a, *BODY[cls])
            for comp, parity in comps_ordered(a, largest):
                paint_vortice(fr, comp, VORTICE[cls], parity=parity)
            cell = Image.fromarray(fr).crop(crop).resize((cw, chh), Image.NEAREST)
            x = pad + ci * (cw + pad)
            y = pad + ri * (chh + lab)
            img.alpha_composite(cell, (x, y))
            d.text((x + 2, y + chh), '%s %s' % (cls, kind), font=f, fill=(210, 210, 220, 255))
    img.convert('RGB').save(path)
    print('wrote %s (all classes x all slots, bare motif)' % path)


def visor_diag(path='_diag_vortice_visor.png', zoom=14):
    """The warrior dome's black eye and mouth slits, reading through the scroll field, m and f. A
    patterned dome is where the finishing pass's visor is most at risk of being swallowed — the
    49th's lesson — and a field of small bright metal shapes is the worst case for it.

    *** THIS PANEL IS BUILT WITH build(), ON THE WHOLE SHEET, AND THAT IS NOT LAZINESS. *** The
    first version assembled frame 0 by hand and handed a 70-frame array with ONE frame in it to
    finish_array. What came back was a pale dome with the slits half-swallowed — while the sheet the
    panel was supposed to be vouching for was correct, and stayed correct through two rounds of
    chasing the difference. The finishing pass does not treat a frame in isolation, so a diagnostic
    that feeds it a lone frame is testing something the generator never does. Second time this file
    has paid for the same mistake in the same function (see the recolor note in slots_diag): if a
    panel is meant to certify the output, it has to be the output.
    """
    crop = (28, 12, 52, 34)
    cells = []
    for suf in ('', '_f'):
        base = load_any('helmet_rare1%s.png' % suf)
        arr = build(base, SLOTS['helmet'], 'warrior')
        arr, _ = finish_array(
            arr, '%s/%s%s.png' % (SLOTS['helmet']['outdir'],
                                  SLOTS['helmet']['dst'] % 'warrior', suf))
        cells.append(('warrior dome %s' % ('f' if suf else 'm'),
                      Image.fromarray(arr[0:FH, 0:FW]).crop(crop)))
    cw = (crop[2] - crop[0]) * zoom
    chh = (crop[3] - crop[1]) * zoom
    pad = 10
    img = Image.new('RGBA', (pad + len(cells) * (cw + pad), pad + chh + 20), (24, 24, 30, 255))
    from PIL import ImageDraw, ImageFont
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)
    except Exception:
        f = ImageFont.load_default()
    x = pad
    for name, im in cells:
        img.alpha_composite(im.resize((cw, chh), Image.NEAREST), (x, pad))
        d.text((x + 2, pad + chh + 2), name, font=f, fill=(210, 210, 220, 255))
        x += cw + pad
    img.convert('RGB').save(path)
    print('wrote %s (visor slits reading through the scrolls)' % path)


def dump_cells():
    legend = {R_HUB: 'O', R_HOOK: '@', R_SPOKE: '#', R_SHADE: ':', R_FIELD: '-', R_DEEP: '.'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    print('== CLAUSE 1, THE MOTIF ITSELF: is the mirror one of the four rotations?')
    for mode in GAUGES:
        c = gauge_cells(mode)
        s = gauge_cells(mode, aligned=True)
        print('   %-5s scroll px=%-3d chiral=%-5s   |  ALIGNED control px=%-3d chiral=%s'
              % (mode, len(c), is_chiral(c), len(s), is_chiral(s)))

    allpass = all(is_chiral(gauge_cells(m)) for m in GAUGES)
    nR = nL = 0
    for label, comp in cases:
        role, scrolls, mode = set_whorls(comp)
        hands = read_hands(role, scrolls)
        nR += sum(1 for _, _, g, _ in hands if g > 0)
        nL += sum(1 for _, _, g, _ in hands if g < 0)
        print('== %s   area=%d scrolls=%d gauge=%s  (right %d / left %d)'
              % (label, int(comp.sum()), len(scrolls), mode,
                 sum(1 for _, _, g, _ in hands if g > 0),
                 sum(1 for _, _, g, _ in hands if g < 0)))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        ok, why = accepts(role, scrolls)
        allpass = allpass and ok
        print('   hands READ off the pixels: %s'
              % ' '.join('%s' % ('R' if g > 0 else ('L' if g < 0 else '?'))
                         for _, _, g, _ in hands))
        print('   %s   -> %s' % (why, 'PASS' if ok else 'FAIL'))

    both = nR > 0 and nL > 0
    print('== CLAUSE 4, BOTH HANDS over the population above: right %d / left %d  -> %s'
          % (nR, nL, 'PASS' if both else 'FAIL'))
    allpass = allpass and both

    for cname, kw, why in (
            ('ALIGNED  (both arms thrown to the SAME side of the hub — the axis\'s own output with '
             'one arm moved and NOTHING else changed, not even the pixel count; this is the 40th '
             'DENTIL)', dict(aligned=True),
             'an aligned element has a mirror line through its hub, so it has no hand at all and '
             'there is nothing left for its neighbours to alternate with'),
            ('UNIFORM  (every scroll right-handed — this is the 24th SPIRAL)', dict(uniform=True),
             'a handedness constant over the field is a handedness nobody on the piece can see'),
            ('MIRROR   (the axis\'s own output reflected). MEASURED, NOT ASSERTED, and it is the '
             'most interesting number in the file: this control PASSES, and it should. Reflecting '
             'the field exchanges two things that are both already on the piece. Reported for the '
             'same reason the 56th reports LOCK and the 57th reports LINEAR.',
             dict(_mirror=True),
             'every element of this field is chiral and the field is not: the alternation is an '
             'ACHIRAL STRUCTURE ASSEMBLED OUT OF CHIRAL PARTS, which is exactly what separates it '
             'from a field with one global hand')):
        kw = dict(kw)
        do_mirror = kw.pop('_mirror', False)
        nfail = nw = 0
        cR = cL = 0
        for _, comp in cases:
            c = comp[:, ::-1].copy() if do_mirror else comp
            role, scrolls, cmode = set_whorls(c, **kw)
            if do_mirror:
                role = role[:, ::-1].copy()
                scrolls = [dict(wh, cx=c.shape[1] - 1 - wh['cx'],
                               cells=_mir(wh['cells']), hand=-wh['hand']) for wh in scrolls]
            nw += len(scrolls)
            hands = read_hands(role, scrolls)
            cR += sum(1 for _, _, g, _ in hands if g > 0)
            cL += sum(1 for _, _, g, _ in hands if g < 0)
            ok, _ = accepts(role, scrolls)
            if not ok:
                nfail += 1
        print('== CONTROL: %s' % cname)
        print('   components=%d  scrolls=%d  right=%d left=%d  components failing acceptance=%d '
              ' -> %s' % (len(cases), nw, cR, cL, nfail,
                          'PASS' if nfail == 0 else 'FAIL'))
        print('   %s' % why)

    print('legend: O hub  # arm  @ the volute curling outward  : its shadow  - enamel  '
          '. enamel at the edge')
    print('ACCEPTANCE (a GROUP ACTION, not a statistic, a topology, an algebra, a conservation or a')
    print('physical law):')
    print('(1) CHIRAL      the motif\'s mirror is none of its four rotations — four set comparisons;')
    print('(2) READABLE    every scroll on the piece matches some rotation of exactly ONE hand;')
    print('(3) ALTERNATION no two lattice-adjacent scrolls share a hand, verified on the hands that')
    print('    were READ off the painted pixels and never on the parity they were painted from;')
    print('(4) BOTH HANDS  over a sheet, both hands occur.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def accept_all():
    """The acceptance test run over EVERY component of EVERY active frame of all 24 sheets — the
    same reading the --cells dump prints, but on the real bodies in every pose, because a constant
    tuned on the idle frame is not a constant that survives every pose (52nd through 57th)."""
    ncomp = nscroll = nfail = nbare = 0
    nR = nL = 0
    gauges = {}
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                sR = sL = 0
                for fi in range(60):
                    r, c = fi // COLS, fi % COLS
                    src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
                    a = src[..., 3] > 0
                    if not a.any():
                        continue
                    for comp_full, parity in comps_ordered(a, largest):
                        if comp_full.sum() < MIN_PX:
                            continue
                        ys, xs = np.nonzero(comp_full)
                        comp = comp_full[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
                        role, scrolls, mode = set_whorls(comp, parity=parity)
                        ncomp += 1
                        gauges[mode] = gauges.get(mode, 0) + 1
                        if not scrolls:
                            nbare += 1
                            nfail += 1
                            print('   VIOLATION %s %s%s frame %d: no scroll at any phase'
                                  % (kind, cls, suffix, fi))
                            continue
                        hands = read_hands(role, scrolls)
                        nscroll += len(hands)
                        sR += sum(1 for _, _, g, _ in hands if g > 0)
                        sL += sum(1 for _, _, g, _ in hands if g < 0)
                        cok, cwhy = accepts(role, scrolls)
                        if not cok:
                            nfail += 1
                            print('   VIOLATION %s %s%s frame %d: %s'
                                  % (kind, cls, suffix, fi, cwhy))
                if not (sR > 0 and sL > 0):
                    nfail += 1
                    print('   VIOLATION %s %s%s: BOTH HANDS fails on this sheet (right %d left %d)'
                          % (kind, cls, suffix, sR, sL))
                nR += sR
                nL += sL
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components               %d   %s' % (ncomp, gauges))
    print('  scrolls set              %d' % nscroll)
    print('  right-handed / left      %d / %d  (read off the pixels, not off the lattice parity)'
          % (nR, nL))
    print('  components with nothing  %d' % nbare)
    print('  clause violations        %d' % nfail)
    print('OVERALL: %s' % ('ALL PASS' if nfail == 0 else 'FAIL'))
    return nfail == 0


def main():
    if '--accept' in sys.argv:
        accept_all()
        return
    if '--cells' in sys.argv:
        dump_cells()
        return
    if '--swatch' in sys.argv:
        swatch()
        return
    if '--sweep' in sys.argv:
        sweep()
        slots_diag()
        visor_diag()
        return
    for kind, cfg in SLOTS.items():
        outdir = cfg['outdir']
        os.makedirs(outdir, exist_ok=True)
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                arr = build(base, cfg, cls)
                dst = '%s/%s%s.png' % (outdir, cfg['dst'] % cls, suffix)
                # MANDATORY finishing pass - never a bespoke shade() in a generator.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
