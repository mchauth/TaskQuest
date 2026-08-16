#!/usr/bin/env python3
"""FIFTY-SIXTH net-new-geometry axis for ALL FOUR SLOTS — the SLOTWORK family (STRAPS THREADED
THROUGH THE PLATE): a few parallel straps are laid across the piece, and each one repeatedly
DISAPPEARS INTO A SLOT CUT IN THE PLATE, runs behind it for a couple of pixels, and comes back out
through a second slot. The straps never cross each other and never touch each other. The only thing
that ever happens on this armour is a strap going through the plate and coming back.

    the ornament is  FACE   (the strap's exposed surface where it is IN FRONT of the plate)
                   + LIP    (its lit edge, the 1px flank that faces the light)
                   + SHADE  (the strap's cast shadow on the plate — present ONLY where the strap is
                             in front, and stopping dead at the slot, which is the proof it went in)
                   + SLOT   (the mouth of the opening the strap passes through — a hole in the
                             plate, not a mark on it)
                   + KEEP   (the lit chamfer of that opening — the plate's own cut thickness,
                             on the PLATE's ramp, never the strap's)
                   + PLATE  (the plate: the majority material, and the OCCLUDER)

*** THIS IS THE FIRST AXIS IN WHICH THE GROUND IS AN OCCLUDER. ***
In all fifty-five prior axes the field is passive. Something is ON it — a cell, a member, a bead, a
wire, a pile of bands — and the field's entire job is to be the thing that is not the ornament. Even
the two axes that make depth their subject leave the field out of it: the 52nd AJOURE has two
surfaces, but the plate is always in front and the liner is always behind, everywhere, forever; the
55th STRATA piles bands on top of one another, and the plate underneath them is never over anything.
Here the plate CHANGES ITS RELATION TO THE STRAP ALONG THE STRAP'S OWN LENGTH: in front here, behind
there, over and over. The subject is not the strap's route (that is the 54th) and not the order the
straps were laid in (that is the 55th) — it is that the surface has two sides and the strap uses
both. Nothing in the fifty-five can be said to have a BACK.

The consequence is a law the ornament must obey and can be checked against: A STRAP MAY NOT LEAVE
THE SURFACE EXCEPT THROUGH A HOLE. Every interruption in a strap is bracketed by two slots; every
slot has strap on one side of it and plate on the other; the strap's cast shadow stops exactly where
the strap enters and starts again exactly where it comes out. Break any one of those and the piece
stops depicting a threading and starts depicting a row of separate objects.

Every near miss fails on something COUNTED.
  * The 30th CABLE and 39th GUILLOCHE — the reflex answer, since a strand there also goes under.
    It goes under ANOTHER STRAND: two members of the same kind, taking turns. The ground is not
    involved and there is no opening anywhere on the piece. Slot count 0 vs 3 to 6 per piece here,
    and the straps here never once cross.
  * The 52nd AJOURE — pierced plate over a lining, and the closest thing in the set to a hole. Its
    piercings show a SURFACE lying behind, which has no route, no ends and no length; and its
    plate-over-liner relation is FIXED — the same everywhere on the piece. Here the relation
    alternates along one member, which is the whole content. Two fixed layers are not a threading.
  * The 55th STRATA — bands laid across the piece, and this one has bands laid across the piece
    too. There the bands cross ONE ANOTHER and the content is which was laid first; here the straps
    are strictly PARALLEL (one angle per component, no crossings at all, by construction) and the
    content is what happens where a strap meets the PLATE.
  * The 54th LABYRINTH — one member with a route, but it lies on top for its whole length. It is
    traceable precisely because it never leaves. This is untraceable in the same sense and does not
    want to be: the interruptions are the point.
  * The 12th BANDED-LAMELLAR and 40th DENTIL — the failure mode this axis falls into if the rhythm
    is mistuned. Lamellae abut edge to edge and cover the piece; dentils are separate teeth hung on
    one fillet. Both are ROWS OF SEPARATE OBJECTS, and neither has any evidence that the gaps
    between them contain anything. That evidence is exactly the slot, which is why the NOSLOT
    control in --sweep collapses into them (measured: it fails the conservation law at every
    transition it has).
  * The 8th SIDE-STRIPE, 6th BALDRIC, 10th CROSS/TRIPLE-STRAP, 7th LACE-BOOTS — straps, but
    uninterrupted ones, or a fixed named accessory in a fixed place. The OVER control in --sweep IS
    the 8th side-stripe: keep everything and just never let the strap go under, and the axis is
    gone with the geometry completely unchanged.

Geometry, per connected component, in the component's own frame:
    direction  ONE angle for every strap on the component — parallel by construction, so no two
               straps ever meet and the 55th's subject cannot arise here even by accident
    across     straps every PITCH px along the normal; footprint LIP (1px, lit flank) + FACE
               (STRAP_W px), with a SH px cast SHADOW on the dark flank
    along      a period P_T of  VIS px in front | SLOT | KEEP | HID px behind | SLOT
               staggered by PHASE_STEP per strap so no two straps' slots line up (see LOCK)
    phase      chosen per component from the PHASES ladder: the offset that puts the most COMPLETE
               threading events on this particular silhouette
    relief     the cast shadow, and it does one job the axis cannot do without: it is present under
               a strap that is in front and absent where the strap is behind, so the shadow's own
               ENDS mark the two slots a second time

Authoring philosophy identical to gen_strata_axis55.py / gen_labyrinth_axis54.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing is added, nothing removed, the
silhouette is untouched, so the generator CANNOT create isolated pixels, background bleed, extra
components or a changed mask — QA-safe by construction. Sleep frames (fi >= 60) get a plain recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()`. See CONTEXT.md
"MANDATORY - the finishing pass". Twelfth generator to call it in-line, after axes 45-55.

Run from repo root:
  python3 scripts/gen_slotwork_axis56.py
  python3 scripts/gen_slotwork_axis56.py --cells    # ASCII dump + the CONSERVATION acceptance test
  python3 scripts/gen_slotwork_axis56.py --accept   # that test over every component of every frame
  python3 scripts/gen_slotwork_axis56.py --swatch   # bare motif on a test plate, no sheets
  python3 scripts/gen_slotwork_axis56.py --sweep    # pitch/width sweep + NOSLOT/OVER/LOCK controls
Then QA (examples):
  python3 scripts/sprite_qa.py _slotwork_legendary_preview/shirt_warrior_legendary56.png
  python3 scripts/sprite_qa.py _slotdome_helmet_preview/helmet_mage_legendary56.png --y-min 2
  python3 scripts/sprite_qa.py _slotwork_boots_preview/boots_warrior_legendary_slotwork.png --y-max 63
"""
import math
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

# --- Slotwork constants -----------------------------------------------------------------------
# The normal direction of the strap family, in degrees, so the straps themselves run at 45.
#
# *** RASTER LESSON, PAID FOR ON A RENDER. *** The first cut ran the straps 20 deg off horizontal,
# on the reasoning that a strap wraps a body ACROSS it. Rendered, the piece was CAMOUFLAGE: a
# shallow angle rasterises into long staircase treads of unequal length, so the strap's own edge is
# already broken up before the slots break it again, and the eye has nothing left to follow. At 45
# the raster is exact — one step across per step along, every step the same — so a strap is a clean
# unbroken diagonal and EVERY break in it is one the ornament put there on purpose. That is not a
# stylistic preference at this scale, it is the difference between a threading and a mottle.
# 45 also keeps the family off both of the axes an axis-aligned set would land on (the 12th
# BANDED-LAMELLAR reads horizontal, the 8th SIDE-STRIPE and 11th FLUTING read vertical).
ANGLE = 135.0

# ACROSS the strap. LIP 1 + FACE 2 = a 3px strap, plus a 1px cast shadow on the dark flank, laid
# every PITCH px. Swept on a real torso, dome and leg (--sweep).
#   PITCH 4  denser and, at first glance, the better-looking cut — but MEASURED on the real
#            components it puts plate at 41-44% and strap at 41-50%, i.e. THE OCCLUDER BECOMES THE
#            MINORITY MATERIAL. An occluder thinner than the thing it occludes is not believable,
#            and with no plate showing between one strap and the next there is nothing left for
#            them to be threaded THROUGH: it reads as the 12th BANDED-LAMELLAR. Rejected on the
#            measurement rather than on the look.
#   PITCH 5  CHOSEN. 3-4 straps on a torso, 3 on a leg, 3 on a dome; plate 53-61%, strap 29-36%.
#   PITCH 7+ 2 straps on a torso and 1 on a dome, each one a single wide pale wedge that dominates
#            the piece. One strap on a helmet is a chinstrap, not a field.
PITCH = 5
STRAP_W = 2
SH = 1

# ALONG the strap: VIS px in front, SLOT, KEEP, HID px behind, SLOT.  VIS + 2 + HID = P_T.
#
# *** THE SIZE LESSON, AND IT IS THE ONE THIS AXIS TURNS ON. ***
# The instinct at 13px is to shorten the period to get more events onto the piece, and it is exactly
# wrong, for two reasons that only showed up rendered.
#   1. A strap is only a strap while it is LONGER THAN IT IS WIDE. The strap is 3px across, so a
#      visible run of 3 is a 3x3 SQUARE: the piece stops being straps through a plate and becomes a
#      grid of little tiles with dark gaps — the 13th STUDWORK, or the 40th DENTIL if the rows are
#      read instead of the columns.
#   2. Worse, and this is what the first cut (VIS 5) actually looked like: at a short period the
#      strap is INTERRUPTED AS OFTEN AS IT IS PRESENT, so it reads as a dashed line, and at 13px a
#      dashed line does not read as one thing seen intermittently — it reads as a scatter of
#      separate blobs. The interruption has to be the exception, not the rhythm.
# VIS 8 against a 3px width, with a 5px interruption, gives a strap that is mostly THERE and goes
# under once. So the axis's element is not a mark, it is an EVENT — strap, hole, plate, hole, strap
# — and a 13px silhouette affords 1 to 3 of them per component. That is few, and it is the honest
# number: it is the same count the 55th's crossings run at, and the 54th gets ONE object on the
# whole piece.
#
# HID 3 (not 2): the hidden run has to carry the KEEP chamfer AND still show 2px of ordinary
# unbroken plate after it, or the interruption reads dark-bright-dark and the KEEP turns into a
# second little object sitting in the gap instead of the lit edge of the opening.
VIS, HID = 8, 3
P_T = VIS + HID + 2                      # 13

# Per-strap stagger, in along-px, so no two neighbouring straps put their slots at the same place.
# What it must do is keep the slots of straps k and k+1 well apart, and 4 out of a 13 period does
# that at every k. See the LOCK control: with a stagger of 0 the slots line up into a continuous
# line across the piece, and a continuous line across a piece of armour is not a set of openings, it
# is a SEAM — the 17th ASHLAR's joint, or the 55th's severing.
PHASE_STEP = 4

# The along-phase is chosen per component from this ladder — the offset that puts the most COMPLETE
# threading events (strap | slot | plate | slot | strap, with strap surviving on BOTH sides) onto
# this particular silhouette, ties broken toward the lowest offset so a sheet regenerates
# identically and male and female agree wherever their masks do.
# This is the fifth appearance of the same adaptive-boundary lesson (52nd MARGIN_MIN, 53rd shot
# pass, 54th adaptive pitch, 55th spread-then-count ladder) and by far the largest effect any of
# them has had. MEASURED: at a FIXED phase 0, 533 OF 985 COMPONENTS show no complete event at all —
# with a period of 13 on runs that are often only 10-18px long, whether the piece shows a threading
# or a plain stripe is decided almost entirely by where the period happens to start. On those frames
# the piece is the 8th SIDE-STRIPE. With the ladder, every component with the room for an event
# gets one, and every component without the room still gets a witnessed opening.
PHASES = tuple(range(P_T))

# A component with fewer than this many INTERIOR pixels is all boundary — a foot at this scale is
# four or five pixels across — and gets the THIN rhythm below instead. Same constant and the same
# measured reason as the 52nd's, 53rd's, 54th's and 55th's MARGIN_MIN: interior counts are chest 78,
# dome 59, legs 39, BOOTS 2 TO 8.
MARGIN_MIN = 20
THIN = dict(pitch=3, strap_w=1, vis=4, hid=2)     # P_T = 4 + 2 + 2 = 8

# Per class, SIX stops: (slot, keep, lip, face, shade, plate).
#   * THERE IS NO "DEEP" STOP, and that is not an omission — it is the first set in the axis series
#     without one. Every previous palette needed a second, darker field tone for the part of the
#     piece the ornament does not reach. Here the plate is not a background that the ornament sits
#     on; it is the OCCLUDER, the active half of the only relation the axis has. There is no part of
#     it that is uninvolved, so there is no tone for one.
#   * TWO RAMPS and the roles do not mix across them. LIP and FACE are the STRAP's; KEEP, SHADE and
#     PLATE are the PLATE's. KEEP is the trap: it is a bright pixel beside a dark hole and it wants
#     to be put on the strap's bright ramp, where it instantly reads as a chip of strap lying loose
#     in the gap. It is the plate's own cut thickness catching the light and it has to be a light
#     PLATE tone, or the hole stops being a hole.
#   * SLOT is the darkest stop in each class and it is the FIRST TIME THE DEFINING ELEMENT OF AN
#     AXIS IS DARK. That collides head-on with the helmet rule — the finishing pass carves the visor
#     as black eye and mouth pixels, and a near-black stop on the dome swallows the face slit (the
#     49th's lesson). Resolved by HUE rather than luminance: the slot is a desaturated COOL tone
#     against a warm plate, so it reads as an opening without going anywhere near black. Every
#     class's darkest stop clears channel-sum 150 — warrior 160, mage 170, ranger 152 — and
#     _diag_slotwork_visor.png shows the warrior dome's slits reading clean through the slots.
#   * A DARK MAJORITY, deliberately, because the 55th is the one pale-majority tier in the set and
#     the two will sit next to each other in the inventory grid.
#   * *** THE CONTRAST LESSON, PAID FOR ON A RENDER, AND THE SECOND HALF OF THE CAMOUFLAGE FIX. ***
#     The first cut gave the straps a near-white face (236,242,250 lip over 170,180,196 face) on a
#     plate around luminance 100 — a clean, obvious, high-contrast read on the 44px test plate, and
#     on the real 13px torso at avatar scale it was CAMOUFLAGE. A 3px pale strap on a 13px torso is
#     a quarter of the width of the piece, so at high contrast it stops being LINE-WORK and becomes
#     a SHAPE, and three bright shapes at 45 degrees with holes in them are a mottle. The straps are
#     now separated from the plate by HUE (cool steel against warm hide) with only a small luminance
#     step, and the single brightest note is the 1px LIP. This is the 52nd's "hue not luminance at
#     13px" principle, but the reason here is the opposite of the usual one: not that the eye cannot
#     resolve the step, but that it resolves it too well.
#   * Not a recolor of the neighbours: 52nd blued-steel/brass, 53rd gold/graphite, 54th
#     platinum/oxblood, 55th blackened-iron/pale-steel. Here the majority hue is the PLATE and it is
#     a HIDE tone in all three classes — walnut, aubergine, peat — which no prior tier has, and the
#     straps are the metal, which is the inversion of the usual arrangement as well.
#   * The pale strap stops stay off the skin ramp (cool steel, ice-blue, cool bone) — the 47th's
#     lesson about a warm off-white on a narrow female chest. Lower risk than usual here, since the
#     pale is 20% of the piece and always in a 3px strip, but the strap is the brightest thing on
#     the sheet and a warm one would read as a bare shoulder in exactly the wrong place.
SLOTWORK = {
    # burnished steel straps threaded through a dark walnut-hide plate
    'warrior': ((58, 50, 46), (150, 124, 96), (196, 206, 222), (138, 146, 160),
                (80, 62, 48), (122, 98, 74)),
    # ice-blue steel straps threaded through a dark aubergine plate
    'mage':    ((54, 46, 62), (146, 116, 152), (190, 204, 226), (130, 150, 180),
                (70, 50, 76), (110, 82, 116)),
    # cool bone straps threaded through a dark peat-green plate
    'ranger':  ((52, 56, 44), (150, 152, 116), (204, 208, 184), (148, 154, 128),
                (58, 64, 44), (96, 102, 66)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only; plate ramp plus the
# strap face as the highlight, so the piece reads as one object when no strap is drawn.
BODY = {
    'warrior': ((88, 68, 52), (120, 96, 74), (176, 188, 206)),
    'mage':    ((78, 56, 84), (108, 80, 114), (170, 190, 216)),
    'ranger':  ((70, 76, 48), (94, 100, 66), (182, 188, 162)),
}

SLOTS = {
    'chest': dict(
        outdir='_slotwork_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary56', largest=True,
    ),
    'legs': dict(
        outdir='_slotwork_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary56', largest=False,
    ),
    'boots': dict(
        outdir='_slotwork_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_slotwork', largest=False,
    ),
    'helmet': dict(
        outdir='_slotdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary56', largest=True,
    ),
}

R_SLOT, R_KEEP, R_LIP, R_FACE, R_SHADE, R_PLATE = 0, 1, 2, 3, 4, 5

# The standing edge rule — brightest stop never on the silhouette, darkest stop never on the
# silhouette — applied by DEMOTION on boundary pixels rather than by a bezel. SLOT demotes to SHADE
# and not to PLATE: a slot that runs off the edge of the piece is still a shadowed notch there, and
# flattening it to plain plate would erase the one thing on the sheet that says the strap went in.
DEMOTE = {R_SLOT: R_SHADE, R_KEEP: R_PLATE, R_LIP: R_FACE, R_FACE: R_FACE,
          R_SHADE: R_SHADE, R_PLATE: R_PLATE}

# state codes for the acceptance test
S_GAP, S_VIS, S_SLOT, S_HID = 0, 1, 2, 3


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


_ROLE_CACHE = {}


def _role_once(comp, phase, noslot=False, over=False, lock=False,
               pitch=None, strap_w=None, vis=None, hid=None):
    """One attempt at the role field, at a given along-PHASE. See role_field() for the wrapper.

    Returns (role, kidx, tidx, band) where `kidx` is the strap index at each pixel, `tidx` the
    integer along-coordinate, and `band` the strap's own footprint (lip+face, excluding the
    shadow) — the three things the acceptance test needs to walk a strap and read its states.
    """
    h, w = comp.shape
    framed = _has_interior(comp)
    pitch = (PITCH if framed else THIN['pitch']) if pitch is None else pitch
    strap_w = (STRAP_W if framed else THIN['strap_w']) if strap_w is None else strap_w
    vis = (VIS if framed else THIN['vis']) if vis is None else vis
    hid = (HID if framed else THIN['hid']) if hid is None else hid
    p_t = vis + hid + 2

    th = math.radians(ANGLE)
    nx, ny = math.cos(th), math.sin(th)          # across-strap normal
    ax, ay = -ny, nx                             # along-strap direction

    ys, xs = np.nonzero(comp)
    cy, cx = float(ys.mean()), float(xs.mean())
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    s = (xx - cx) * nx + (yy - cy) * ny
    t = (xx - cx) * ax + (yy - cy) * ay
    t = t - float(t[comp].min())

    k = np.round(s / pitch)
    u = s - k * pitch
    kidx = k.astype(np.int32)

    # The lit flank is the one whose outward normal faces the upper-left light.
    lit_hi = (nx + ny) < 0
    half = strap_w / 2.0 + 0.5
    if lit_hi:
        lip = (u >= half - 1.0) & (u < half)
        face = (u >= -half) & (u < half - 1.0)
        shadow = (u >= -half - SH) & (u < -half)
    else:
        lip = (u >= -half) & (u < -half + 1.0)
        face = (u >= -half + 1.0) & (u < half)
        shadow = (u >= half) & (u < half + SH)
    band = comp & (lip | face)

    stag = 0 if lock else PHASE_STEP
    p = np.mod(t + phase + stag * k, p_t)
    pi = np.floor(p).astype(np.int32)
    tidx = np.floor(t).astype(np.int32)

    is_vis = pi < vis
    is_slot_a = pi == vis
    is_keep = pi == vis + 1
    is_slot_b = pi == p_t - 1
    if over:                                     # CONTROL: the strap never goes under
        is_vis = np.ones_like(is_vis)
        is_slot_a = is_slot_b = is_keep = np.zeros_like(is_vis)
    is_slot = is_slot_a | is_slot_b

    role = np.where(comp, R_PLATE, -1).astype(np.int8)
    role[band & is_vis & face] = R_FACE
    role[band & is_vis & lip] = R_LIP
    # the shadow exists ONLY under a strap that is in front, and its ends mark the slots a second
    # time — that asymmetry is the cheapest and clearest evidence the strap really went under
    role[comp & shadow & is_vis] = R_SHADE
    if not noslot:
        role[band & is_slot] = R_SLOT
        # the lit chamfer of the opening: the plate's own cut thickness, one pixel deep, on the side
        # of the hole that faces the light
        if framed:
            role[band & is_keep] = R_KEEP
    return role, kidx, tidx, band


def _walk(role, kidx, tidx, band, comp):
    """Read the strap states back OFF THE PAINTED PIXELS, exactly as a viewer would: for each strap,
    for each step along it, is the strap in front (VIS), in a hole (SLOT), or gone (HID)?

    Returns (runs, viol) where runs is a list of state sequences (one per contiguous on-silhouette
    stretch of one strap) and viol a list of (kind, detail) violations of the conservation law.
    """
    runs = []
    if not band.any():
        return runs, []
    ks = np.unique(kidx[band])
    for k in ks:
        m = band & (kidx == k)
        if not m.any():
            continue
        tv = tidx[m]
        lo, hi = int(tv.min()), int(tv.max())
        seq = []
        for ti in range(lo, hi + 1):
            sel = m & (tidx == ti)
            if not sel.any():
                seq.append(S_GAP)
                continue
            r = role[sel]
            if (r == R_SLOT).any():
                seq.append(S_SLOT)
            elif ((r == R_FACE) | (r == R_LIP)).any():
                seq.append(S_VIS)
            else:
                seq.append(S_HID)
        # split on GAP: the strap has left the silhouette and come back somewhere else, which is a
        # fact about the body, not about the ornament
        cur = []
        for v in seq:
            if v == S_GAP:
                if cur:
                    runs.append(cur)
                cur = []
            else:
                cur.append(v)
        if cur:
            runs.append(cur)

    return runs, _walk_viol(runs)


def _walk_viol(runs):
    """THE CONSERVATION LAW, checked on the state sequences read off the pixels."""
    viol = []
    for run in runs:
        # compress to a state sequence
        comp_seq = []
        for v in run:
            if not comp_seq or comp_seq[-1] != v:
                comp_seq.append(v)
        for i in range(len(comp_seq) - 1):
            a, b = comp_seq[i], comp_seq[i + 1]
            if {a, b} == {S_VIS, S_HID}:
                viol.append(('vanished', 'strap goes from in-front to behind with no hole'))
        for i, v in enumerate(comp_seq):
            if v != S_SLOT:
                continue
            if not (0 < i < len(comp_seq) - 1):
                continue        # a hole at the end of a run: the piece simply stops there
            sides = {comp_seq[i - 1], comp_seq[i + 1]}
            if sides != {S_VIS, S_HID}:
                # a hole with strap on both sides, or plate on both sides, is a scratch on the
                # plate and not an opening in it
                viol.append(('bad-slot', 'a hole with the same thing on both sides'))
    return viol


def _maxrun(runs):
    return max((len(r) for r in runs), default=0)


def _legal_slots(runs):
    """Slots that are witnessed: strap on one side, plate on the other (or the piece's own edge)."""
    n = 0
    for run in runs:
        cs = []
        for v in run:
            if not cs or cs[-1] != v:
                cs.append(v)
        for i, v in enumerate(cs):
            if v != S_SLOT:
                continue
            sides = {cs[j] for j in (i - 1, i + 1) if 0 <= j < len(cs)}
            if sides in ({S_VIS, S_HID}, {S_VIS}, {S_HID}):
                n += 1
    return n


def _events(runs):
    """A COMPLETE threading event is VIS SLOT HID SLOT VIS — the strap survives on both sides of the
    interruption, so a viewer can see the same strap go in and come out. A slot at the edge of a run
    is a real threading too, but only a complete one is a witness that cannot be read any other way,
    so it is what the phase ladder maximises."""
    n = 0
    for run in runs:
        cs = []
        for v in run:
            if not cs or cs[-1] != v:
                cs.append(v)
        for i in range(len(cs) - 4):
            if cs[i:i + 5] == [S_VIS, S_SLOT, S_HID, S_SLOT, S_VIS]:
                n += 1
    return n


def room_for(comp):
    """The shortest strap run that can carry a COMPLETE event: 1px of strap, a hole, the hidden
    run, a hole, 1px of strap. A component whose longest run is shorter than this cannot show one
    and is not asked to — a foot is four pixels across."""
    framed = _has_interior(comp)
    hid = HID if framed else THIN['hid']
    return hid + 4


def accepts(runs, comp):
    """The acceptance test for one component, in full.

    (1) THE CONSERVATION LAW: no violations — a strap never leaves the surface except through a
        hole, and no hole has the same thing on both sides of it.
    (2) THE WITNESS: the threading must actually be VISIBLE on this silhouette. A component with
        room for a complete event (strap | hole | plate | hole | strap) must show at least one;
        a component too small for one must still show at least one witnessed opening. A piece
        with neither is not a worse version of this axis, it is the 8th SIDE-STRIPE.
    """
    _, viol = None, None
    viol = _walk_viol(runs)
    if viol:
        return False, viol[0][1]
    if _maxrun(runs) >= room_for(comp):
        if _events(runs) < 1:
            return False, 'no complete threading event on a component with room for one'
    elif _legal_slots(runs) < 1:
        return False, 'no opening at all — the strap never goes anywhere'
    return True, 'conservation law holds, threading witnessed'


def role_field(comp, noslot=False, over=False, lock=False,
               pitch=None, strap_w=None, vis=None, hid=None):
    """Classify every pixel of the component box into one of the six roles.

    Walks the PHASES ladder and keeps the offset that puts the most COMPLETE threading events on
    this silhouette, ties to the lowest offset. A phase that puts no event on the piece is not a
    slightly worse version of this axis, it is the 8th SIDE-STRIPE.

    `noslot`, `over` and `lock` exist only for --sweep: they are the three CONTROLS that show what
    this axis turns into when its defining property is removed.
      noslot  paint no slot pixels, so a strap simply stops and starts again. The geometry is
              otherwise identical and the piece becomes a row of separate tiles — the 12th
              BANDED-LAMELLAR / 40th DENTIL. Every transition then breaks the conservation law.
      over    never let the strap go under. The 8th SIDE-STRIPE, with nothing else changed.
      lock    all straps share one phase, so the slots line up across the piece into a continuous
              line, and a continuous line on armour is a SEAM, not a set of openings.
    """
    key = (comp.shape, comp.tobytes(), noslot, over, lock, pitch, strap_w, vis, hid)
    hit = _ROLE_CACHE.get(key)
    if hit is not None:
        return hit
    best = None
    for ph in PHASES:
        out = _role_once(comp, ph, noslot, over, lock, pitch, strap_w, vis, hid)
        runs, _ = _walk(out[0], out[1], out[2], out[3], comp)
        # complete events first, then witnessed openings — the tie-break is what serves a foot,
        # which has no room for a complete event and can still show the strap going in
        score = (_events(runs), _legal_slots(runs))
        if best is None or score > best[0]:
            best = (score, ph, out)
        if over:
            break
    _ROLE_CACHE[key] = best[2]
    return best[2]


def paint_slotwork(fr, comp_full, stops, **kw):
    """Paint the threading onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette."""
    if comp_full.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    role = role_field(comp, **kw)[0]
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


def build(base, cfg, cls):
    D, M, L = BODY[cls]
    stops = SLOTWORK[cls]
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
        # ONE STRAP FAMILY PER CONNECTED COMPONENT — a strap is fastened to a physical plate and
        # cannot span the gap between the two legs of a pair of chausses or between the left boot
        # and the right. Each component is its own piece of armour with its own openings.
        lbl, n = label4(a)
        if n < 1:
            continue
        if largest:
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comps = [(lbl == int(counts.argmax()))]
        else:
            comps = [(lbl == i) for i in range(1, n + 1)]
        for comp in comps:
            paint_slotwork(fr, comp, stops)
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
    threading can be judged on a shape with the features the real slots have."""
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


def swatch(path='_diag_slotwork_swatch.png', zoom=12):
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_slotwork(a, m, SLOTWORK[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def _big_comp(arr):
    src = arr[0:FH, 0:FW]
    a = src[..., 3] > 0
    lbl, n = label4(a)
    counts = np.bincount(lbl.ravel())
    counts[0] = 0
    return (lbl == int(counts.argmax())) if n else a


def sweep(path='_diag_slotwork_sweep.png', zoom=11):
    """Warrior chest and leg idle frames across pitch and strap width, plus the three CONTROLS."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    variants = [('PITCH 4', dict(pitch=4)), ('PITCH 5', dict(pitch=5)), ('PITCH 7', dict(pitch=7)),
                ('VIS 3', dict(vis=3)), ('W 3', dict(strap_w=3)),
                ('NOSLOT', dict(noslot=True)), ('OVER', dict(over=True)), ('LOCK', dict(lock=True))]
    cells = []
    for name, kw in variants:
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            comp = _big_comp(arr)
            fr = np.zeros_like(arr[0:FH, 0:FW])
            paint_slotwork(fr, comp, SLOTWORK['warrior'], **kw)
            col.append(Image.fromarray(fr).crop(crop))
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
    print('wrote %s (pitch/width sweep + NOSLOT/OVER/LOCK controls - no sheets written)' % path)


def dump_cells():
    legend = {R_SLOT: 'O', R_KEEP: '"', R_LIP: '+', R_FACE: '#', R_SHADE: ':', R_PLATE: '-'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        a = _big_comp(load_any(fname))
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    allpass = True
    for label, comp in cases:
        role, kidx, tidx, band = role_field(comp)
        runs, viol = _walk(role, kidx, tidx, band, comp)
        ev = _events(runs)
        nslot = int((role == R_SLOT).sum())
        plate = float(((role == R_PLATE) | (role == R_KEEP) | (role == R_SHADE)).sum())
        print('== %s   area=%d straps=%d framed=%s'
              % (label, int(comp.sum()), len(np.unique(kidx[band])) if band.any() else 0,
                 _has_interior(comp)))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        ok, _ = accepts(runs, comp)
        allpass = allpass and ok
        print('   slot px=%d  complete events=%d  plate share=%.0f%%  violations=%d  longest strap '
              'run=%d (room for an event needs %d)'
              % (nslot, ev, 100 * plate / max(1, int(comp.sum())), len(viol), _maxrun(runs),
                 room_for(comp)))
        print('   %s   -> %s' % (accepts(runs, comp)[1], 'PASS' if ok else 'FAIL'))

    # the three CONTROLS, on the real torso, so the failures are measured and not asserted
    comp = cases[1][1]
    for cname, kw, why in (
            ('NOSLOT (the strap just stops - 12th lamellar / 40th dentil)', dict(noslot=True),
             'a strap that leaves the surface with no hole to leave through'),
            ('OVER   (the strap never goes under - 8th side-stripe)', dict(over=True),
             'no openings at all, so nothing is threaded through anything'),
            ('LOCK   (every strap in phase - the slots become a seam)', dict(lock=True),
             'the openings line up into one continuous line across the piece')):
        role, kidx, tidx, band = role_field(comp, **kw)
        runs, viol = _walk(role, kidx, tidx, band, comp)
        ev = _events(runs)
        if kw.get('lock'):
            # a seam is not a conservation failure, it is a legibility one, so it is measured
            # differently: how many DISTINCT along-positions do the slots occupy per strap
            cols = set()
            ys2, xs2 = np.nonzero((role == R_SLOT))
            for y, x in zip(ys2, xs2):
                cols.add(int(tidx[y, x]))
            print('== CONTROL: %s' % cname)
            print('   distinct along-positions of the openings = %d (staggered gives many, a seam '
                  'gives few) -> %s' % (len(cols), why))
            continue
        print('== CONTROL: %s' % cname)
        print('   complete events=%d  violations=%d  -> %s  (%s)'
              % (ev, len(viol), 'PASS' if (not viol and ev >= 1) else 'FAIL', why))

    print('legend: # strap face  + lit strap edge  : its cast shadow  O the opening  " the lit '
          'chamfer of the opening  - plate')
    print('ACCEPTANCE (a CONSERVATION LAW along a traversal, not a statistic and not an algebra):')
    print('walk each strap and read its states off the painted pixels — in front, in a hole, gone.')
    print('A STRAP MAY NOT LEAVE THE SURFACE EXCEPT THROUGH A HOLE: no in-front/behind transition')
    print('without a slot between them, no slot with the same thing on both sides, and at least one')
    print('COMPLETE event (strap | hole | plate | hole | strap) per component that has room for it.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))
    return allpass


def accept_all():
    """The acceptance test run over EVERY component of EVERY active frame of all 24 sheets — the
    same walk the --cells dump prints, but on the real bodies in every pose, because a constant
    tuned on the idle frame is not a constant that survives every pose (the 52nd, 53rd, 54th and
    55th all paid for that lesson)."""
    ncomp = nstrap = nslot = nev = nviol = nsmall = 0
    for kind, cfg in SLOTS.items():
        largest = cfg['largest']
        for cls, srcstem in cfg['srcs'].items():
            for suffix in ('', '_f'):
                base = load_any('%s%s.png' % (srcstem, suffix))
                for fi in range(60):
                    r, c = fi // COLS, fi % COLS
                    src = base[r * FH:(r + 1) * FH, c * FW:(c + 1) * FW]
                    a = src[..., 3] > 0
                    if not a.any():
                        continue
                    lbl, n = label4(a)
                    if largest:
                        counts = np.bincount(lbl.ravel())
                        counts[0] = 0
                        comps = [(lbl == int(counts.argmax()))]
                    else:
                        comps = [(lbl == i) for i in range(1, n + 1)]
                    for comp_full in comps:
                        if comp_full.sum() < MIN_PX:
                            continue
                        ys, xs = np.nonzero(comp_full)
                        comp = comp_full[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
                        role, kidx, tidx, band = role_field(comp)
                        runs, viol = _walk(role, kidx, tidx, band, comp)
                        ok, why = accepts(runs, comp)
                        ncomp += 1
                        nstrap += len(np.unique(kidx[band])) if band.any() else 0
                        nslot += _legal_slots(runs)
                        nev += _events(runs)
                        if _maxrun(runs) < room_for(comp):
                            nsmall += 1
                        if not ok:
                            nviol += 1
                            print('   VIOLATION %s %s%s frame %d: %s' % (kind, cls, suffix, fi, why))
    print('ACCEPTANCE over every component of every active frame of all 24 sheets:')
    print('  components            %d' % ncomp)
    print('  straps                %d' % nstrap)
    print('  witnessed openings    %d' % nslot)
    print('  complete events       %d  (strap | hole | plate | hole | strap)' % nev)
    print('  too small for one     %d  (a foot; asked only for a witnessed opening)' % nsmall)
    print('  FAILURES              %d' % nviol)
    print('OVERALL: %s' % ('ALL PASS' if nviol == 0 else 'FAIL'))
    return nviol == 0


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
