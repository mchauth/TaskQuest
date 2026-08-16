#!/usr/bin/env python3
"""FIFTY-THIRD net-new-geometry axis for ALL FOUR SLOTS — the GRANULATION family (a CONTACT PACKING
of graded spherical granules): the armour is covered in soldered metal beads of MANY DIFFERENT SIZES,
each one as large as the room it sits in allows, laid shoulder to shoulder so that they TOUCH, with
only slivers of the dark ground surviving in the interstices between them.

    the ornament is  GRANULE  (a convex bead, r=1 (5px) or r=2 (13px), modelled as a little DOME:
                               bright core, mid annulus, dark rim all the way round, rim one stop
                               darker on the down-right where the contact shadow falls, and a
                               specular pip set up-left of the core)
                   + SHOT     (a single-pixel granule, laid only on components too narrow to bead)
                   + CONTACT  (granules abut — the packing has no gap parameter, touching IS the axis)
                   + FILLET   (an interstitial pixel touching two different beads: solder wicked up
                               into the crease, and drawn evidence that the two are in contact)
                   + GROUND   (the dark solder bed, surviving in the wider hollows a circle packing
                               cannot fill)
                   + BEZEL    (a 1px solid margin around the silhouette; see MARGIN_MIN)

*** THIS IS THE FIRST PACKING AXIS. THE ELEMENT'S SIZE IS SET BY THE PIECE, NOT BY THE PATTERN. ***
Every one of the fifty-two prior axes fixes its element's size ONCE, in the generator, as a constant
of the ornament — a hexagon is a hexagon on the chest and the same hexagon on the boot, a coffer is a
coffer, a rune is a rune. The pattern is authored and then the silhouette is used as a stencil to cut
it out. Here the causal arrow runs the other way: the field is grown INTO the silhouette, largest
element first, each granule taking the biggest radius that will fit in the room still unclaimed at
that spot, so the ornament cannot be stated at all without the shape it lives on. Measured on the
real idle frames, the histogram is a different object on every slot — chest {r2: 3, r1: 8}, legs
{r2: 2, r1: 6}, helmet dome {r2: 2, r1: 5}, warrior boot {r2: 3, r1: 1, shot: 2} — and NONE of those
numbers is in this file. They are read off the armour. You cannot draw this axis on paper and then
apply it. THAT is the categorical step, and it is a different one from every claim made so far:
the 47th mokume is shape-CONFORMAL (its tone is a function of distance-to-edge) but its band spacing
is still a constant of the ornament; this is shape-DETERMINED, and its own spacing is an output.

The families it could be confused with, and why each fails:
  * The 13th STUDWORK is the near miss and the one both ends of the sweep collapse into. A rivet
    field is ONE radius on a PERIODIC GRID with ground all round every stud: any two neighbours are
    congruent, their spacing is the same everywhere on the piece and the same on every piece, and no
    stud ever touches another — the grid is the subject and the stud is just what marks it. Here
    there is no grid to mark: neighbours are routinely of different radius, the centre-to-centre
    distance is whatever the two radii happen to sum to, and the beads are IN CONTACT. Contact is
    load-bearing. Break it — force one pixel of ground between beads — and the field instantly reads
    as dots on a ground again, which is why there is no gap parameter to tune (see --sweep).
  * The 41st BEAD-AND-REEL and the 38th EGG-AND-DART do thread convex bodies along a track, but the
    track is RULED: a strict period, an element sized BY that period, and an alternation you can
    state in two symbols. The distinction survives at two radii because the two radii here are not
    an alternation — they do not take turns, their RATIO changes from slot to slot, and neither of
    them is on a track at all. Force the field to one radius (RMAX=1) and the distinction does die,
    but into the 13th studwork rather than into beading, because a single radius packed by room
    settles onto a quincunx.
  * The 46th CRAQUELURE is the other unruled field, and the difference is partition versus packing.
    Craquelure PARTITIONS: every pixel belongs to some cell, the cells share their boundaries, and
    the "ground" is a fracture line one pixel wide that is really just the shared edge. A packing
    does not partition: its bodies are convex, they meet at POINTS rather than along edges, and the
    ground is a genuine second thing that survives in the interstices with an area a circle packing
    can never close. Craquelure's cell sizes also come from a PRNG and mean nothing; these come from
    the silhouette and can be read off it.
  * The 48th COSMATI is the multi-scale axis, and its hierarchy is DISCRETE, FIXED-RATIO (8:5:2) and
    IDENTICAL IN EVERY BAY, because it is authored: you can name the three sizes before you have seen
    the armour. Here the size distribution is an outcome — no ratio, no fixed count, and a different
    histogram on every slot. `--cells` prints that histogram, and it is the acceptance test.
  * The 15th SCALE overlaps its elements, but in a fixed z-order given by a lattice; granules do not
    overlap at all. Contact is not overlap: nothing is hidden, and there is no order.
  * The 52nd AJOURE is the other axis that cares about the boundary, but through a constant 1px
    frame; the boundary here reaches all the way into the field, because it is what set every radius.

Geometry, per connected component, in the component's own frame:
    dist      = chamfer-(3,4) distance to the outside of the component, i.e. how much room is here
    order     = every body pixel, sorted by (dist DESC, y ASC, x ASC)   [fully deterministic, no RNG]
    place     = ONE FULL SWEEP PER RADIUS, largest first: every r=RMAX bead is placed everywhere it
                fits before any r=RMAX-1 is committed, and so on down to RMIN. That ordering is what
                makes the grading read — the big beads find all the open room, the small ones fill
                down into the taper and the corners — and doing it the other way round (one pass,
                best radius at each site) is a measured failure recorded below.
    disc(r)   = dx*dx + dy*dy <= r*r + 0.5     (r=0 a single pixel, r=1 a 5px plus, r=2 13px)
    dome      = tone by RADIUS FROM THE BEAD'S OWN CENTRE, not by light direction: rr<=0.36 core
                (LIT), rr<=0.74 annulus (MID), else rim — RIM if (dy+dx)>0 (the contact-shadow side)
                else DARK. Pip at (-1,-1). Light is upper-left as everywhere in this set, but it is
                a bias on a concentric field, never the field itself.
    fillet    = a leftover pixel 4-adjacent to two DIFFERENT beads -> DARK (solder in the crease)
    ground    = every remaining body pixel: the bed

Authoring philosophy identical to gen_ajoure_axis52.py / gen_flowgrain_axis51.py: every pattern pixel
is painted ONLY onto pixels ALREADY opaque in the body. Nothing is added, nothing is removed, the
silhouette is untouched, so the generator CANNOT create isolated pixels, background bleed, extra
components or a changed mask — it is QA-safe by construction. Sleep frames (fi >= 60) get a plain
body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()` — the canonical chain
(no-smooth shading with protect=False, shirt pauldron/gorget/chest-plate separation, helmet black
eye+mouth visor with NO full-silhouette rim, hat brim/crease folds for open headgear). See
CONTEXT.md "MANDATORY - the finishing pass".

Run from repo root:
  python3 scripts/gen_granulation_axis53.py
  python3 scripts/gen_granulation_axis53.py --cells    # ASCII dump + radius histogram + contact frac
  python3 scripts/gen_granulation_axis53.py --swatch   # bare motif on a test plate, no sheets
  python3 scripts/gen_granulation_axis53.py --sweep    # RMAX sweep + the forced-gap control
Then QA (examples):
  python3 scripts/sprite_qa.py _granulation_legendary_preview/shirt_warrior_legendary53.png
  python3 scripts/sprite_qa.py _granulationdome_helmet_preview/helmet_mage_legendary53.png --y-min 2
  python3 scripts/sprite_qa.py _granulation_boots_preview/boots_warrior_legendary_granule.png --y-max 63
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

# --- Granulation constants ------------------------------------------------------------------
# RMIN / RMAX bound the bead radius in pixels. Swept (--sweep) on a real torso AND a real leg, and
# as with the 49th, 50th, 51st and 52nd, BOTH ends fail INTO an older axis rather than into mush.
# The sweep was run and READ, not reasoned about, and it moved the answer down one notch from where
# the design started:
#   RMAX 1   every bead is a 5px plus and the largest-first packing has nothing to grade, so the
#            beads settle onto a near-regular quincunx of their own accord: 15 congruent studs at a
#            near-constant spacing on a torso. One size, one spacing, visible everywhere — the 13th
#            STUDWORK, which is precisely what this axis exists not to be. Size variety is not
#            decoration here, it is the whole claim.
#   RMAX 2   CHOSEN. Torso {r2: 3, r1: 8}, thigh {r2: 2, r1: 6}, dome {r2: 2, r1: 5}, boot
#            {r2: 3, r1: 1, shot: 2}. Two disc radii and, on the narrow fittings, the shot — three
#            classes across the set, a different mixture on every slot, and every bead touching at
#            least one neighbour (contact fraction 1.00 on all four).
#   RMAX 3   the design's first pick, and the render killed it. A 7px bead on a 13px torso is over
#            half the chest wide, so the packing puts ONE of them in the middle and pads round it:
#            measured {r3: 1, r2: 2, r1: 4}. At 1x that reads as a boss with filler round it, which
#            is the 8th AEGIS ROUNDEL's figure-ground — a device on a field, not a field — and worse,
#            the sweep frames for RMAX 3, 4 and 5 are nearly indistinguishable from each other, which
#            is the tell that the field has stopped being a field.
#   RMAX 4   a 13px torso holds one r=4 bead and crumbs. Same failure, further along.
#   RMAX 5   one bead per piece. A device, and not even a repeated one.
# The lesson generalises past this axis: THE ELEMENT CEILING IS SET BY THE NARROWEST SLOT THE FIELD
# HAS TO SURVIVE ON, not by the widest. It is the 47th's "pitch is set by the thinnest part" again,
# arrived at from the other direction — there the constraint was on spacing, here on the element.
RMIN = 1
RMAX = 2

# There is deliberately NO gap constant. A packing in which the bodies do not touch is not a packing,
# it is a scatter, and a scatter of convex bodies on a ground is the 13th studwork no matter how the
# sizes are graded. `--sweep` renders the forced-gap control (one pixel of ground driven between
# every pair) next to the real thing to make that concrete: the graded sizes survive and the axis
# does not, because with the contact broken there is nothing left to say the beads were PACKED
# rather than PLACED. Contact is the load-bearing property, so it is not exposed as a knob.
FORCE_GAP = 0

# A component needs at least this many INTERIOR pixels (all four 4-neighbours inside the component)
# before it is given the solid 1px BEZEL. Same constant and same reason as the 52nd's MARGIN_MIN,
# and it is here for the same measured fact: on the real idle frames the interior counts are chest
# 78, helmet dome 59, legs 39, but BOOTS 2 TO 8, because a foot at this scale is four or five pixels
# across and is ALL boundary. Bezel a boot and it is a flat recolor with not one bead on it. So a
# component with no real interior keeps its beads and gives up its bezel, and the standing edge rule
# — brightest stop never on the silhouette, darkest stop never on the silhouette (no dome ever grows
# the full-silhouette dark rim that mangles patterned helmets) — is honoured the other way instead,
# by demoting PIP/LIT and GROUND to MID and RIM to DARK on the boundary.
MARGIN_MIN = 20

# Per class, six stops: (pip, lit, mid, dark, rim, ground).
#   * The beads and the bed are DIFFERENT MATERIALS and the difference has to be carried by HUE —
#     at 13px a luminance step alone reads as shading, which is the lesson banked on the 52nd.
#     Each class pairs a bright bead metal with a contrasting dark bed.
#   * No stop is near pure black. HELMET constraint, not taste: the finishing pass carves the visor
#     as black eye and mouth pixels and a near-black stop on the dome swallows the face slit (the
#     49th's lesson). The darkest stop on every class clears channel-sum 150.
#   * The pale stops stay off the skin ramp — cool, never a warm off-white, which on a narrow female
#     chest reads as bare shoulder (the 47th's rose-gold lesson).
#   * RIM is the CONTACT SHADOW where two beads meet, so it belongs to the BEAD's ramp, not the
#     bed's: it is the bead's own far side turned away from the light, and painting it in the bed
#     tone would weld the beads to the ground and lose the sphere.
#   * The ranger pair is deliberately not the 52nd's green-birch-over-slate-blue again; the beads go
#     silver-jade and the bed goes deep forest, so the two adjacent legendary tiers do not read as
#     recolors of each other.
GRAIN = {
    # gold granules soldered on a graphite bed
    'warrior': ((255, 244, 206), (246, 214, 120), (198, 152, 58),
                (126, 88, 32), (86, 60, 26), (70, 74, 92)),
    # moonsilver granules on a violet-ink bed
    'mage':    ((244, 244, 255), (206, 208, 238), (150, 152, 196),
                (94, 96, 144), (62, 64, 106), (58, 46, 88)),
    # silver-jade granules on a deep forest bed
    'ranger':  ((236, 250, 240), (182, 220, 198), (120, 162, 138),
                (72, 108, 90), (46, 74, 60), (44, 58, 46)),
}

# Per-class body (ground) tones for the recolor, visible on sleep frames only; taken off the bead
# stops so the piece reads as one object when the packing is not drawn.
BODY = {
    'warrior': ((74, 84, 104), (196, 152, 58), (232, 196, 96)),
    'mage':    ((62, 44, 96), (154, 156, 196), (200, 202, 232)),
    'ranger':  ((46, 62, 44), (124, 164, 142), (176, 214, 192)),
}

# One config block per slot. `largest` restricts the field to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_granulation_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary53', largest=True,
    ),
    'legs': dict(
        outdir='_granulation_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary53', largest=False,
    ),
    'boots': dict(
        outdir='_granulation_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_granule', largest=False,
    ),
    'helmet': dict(
        outdir='_granulationdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary53', largest=True,
    ),
}

# role codes
R_PIP, R_LIT, R_MID, R_DARK, R_RIM, R_GROUND = 0, 1, 2, 3, 4, 5


def chamfer(mask):
    """Chamfer-(3,4) distance from every True pixel to the nearest False pixel (or off the array).

    Approximate Euclidean distance x3, which is all that is needed: it is used to ORDER the
    candidate centres (most room first) and to give the radius search a sensible starting guess.
    Two sequential passes; the boxes are ~30x30 so a Python loop is free here, and it keeps the
    generator scipy-free like every other axis script."""
    h, w = mask.shape
    BIG = 10 ** 6
    d = np.where(mask, BIG, 0).astype(np.int32)
    for y in range(h):
        for x in range(w):
            if d[y, x] == 0:
                continue
            best = d[y, x]
            if y > 0:
                if x > 0:
                    best = min(best, d[y - 1, x - 1] + 4)
                best = min(best, d[y - 1, x] + 3)
                if x < w - 1:
                    best = min(best, d[y - 1, x + 1] + 4)
            else:
                best = min(best, 3)             # off the top of the box is outside
            if x > 0:
                best = min(best, d[y, x - 1] + 3)
            else:
                best = min(best, 3)
            d[y, x] = best
    for y in range(h - 1, -1, -1):
        for x in range(w - 1, -1, -1):
            if d[y, x] == 0:
                continue
            best = d[y, x]
            if y < h - 1:
                if x > 0:
                    best = min(best, d[y + 1, x - 1] + 4)
                best = min(best, d[y + 1, x] + 3)
                if x < w - 1:
                    best = min(best, d[y + 1, x + 1] + 4)
            else:
                best = min(best, 3)
            if x < w - 1:
                best = min(best, d[y, x + 1] + 3)
            else:
                best = min(best, 3)
            d[y, x] = best
    return d


_DISC_CACHE = {}


def disc(r):
    """Offsets of a pixel-art disc of radius r.
    r=0 is a single pixel (the SHOT, the finest grain), r=1 a 5px plus, r=2 13px, r=3 29px."""
    if r in _DISC_CACHE:
        return _DISC_CACHE[r]
    off = [(dy, dx) for dy in range(-r, r + 1) for dx in range(-r, r + 1)
           if dy * dy + dx * dx <= r * r + 0.5]
    _DISC_CACHE[r] = off
    return off


def _neighbours(comp):
    """The four shifted copies of a mask, as (left, right, up, down) — i.e. for each pixel, whether
    its west/east/north/south neighbour is inside the component."""
    left = np.zeros_like(comp)
    right = np.zeros_like(comp)
    up = np.zeros_like(comp)
    down = np.zeros_like(comp)
    left[:, 1:] = comp[:, :-1]
    right[:, :-1] = comp[:, 1:]
    up[1:, :] = comp[:-1, :]
    down[:-1, :] = comp[1:, :]
    return left, right, up, down


def _has_interior(comp):
    """True if the component has a real inside — enough pixels with all four 4-neighbours in the
    component to be worth a bezel. False for every boot at this scale; see MARGIN_MIN."""
    left, right, up, down = _neighbours(comp)
    return int((comp & left & right & up & down).sum()) >= MARGIN_MIN


def pack(comp, rmax=None, rmin=None, gap=None, shot=False):
    """Grow the packing into one component. Returns a list of (cy, cx, r), largest-radius first.

    Deterministic — no RNG anywhere. The order is (most room, then top, then left), and the radius
    at each site is simply the largest that fits, so the same silhouette always yields the same
    packing and male/female sheets of the same item stay consistent frame to frame."""
    rmax = RMAX if rmax is None else rmax
    rmin = RMIN if rmin is None else rmin
    gap = FORCE_GAP if gap is None else gap
    h, w = comp.shape
    d = chamfer(comp)
    ys, xs = np.nonzero(comp)
    order = sorted(zip(ys.tolist(), xs.tolist()), key=lambda p: (-int(d[p[0], p[1]]), p[0], p[1]))
    claimed = np.zeros((h, w), dtype=bool)
    blocked = np.zeros((h, w), dtype=bool)      # claimed, dilated by `gap` (control only)
    out = []
    # STRICTLY LARGEST-FIRST, ONE FULL SWEEP PER RADIUS. This is the difference between a graded
    # packing and a big bead with crumbs round it, and the first cut got it wrong: walking the
    # candidates once in distance order and taking the largest radius that fits at each site places
    # ONE rmax bead and then, because every remaining high-distance pixel is a neighbour of that
    # bead and has no room left for another big one, fills the entire rest of the piece with rmin.
    # The histogram came out {1: 50, 2: 1, 3: 1} — one size in practice, which is the 13th studwork.
    # Sweeping the whole component for rmax first lets the big beads find EVERY open place before
    # anything small is committed, and only then do the mediums fill between them and the smalls
    # fill down into the taper and the corners. That ordering IS the grading, and the grading is
    # the axis.
    for r in range(rmax, rmin - 1, -1):
        for cy, cx in order:
            if claimed[cy, cx] or blocked[cy, cx]:
                continue
            ok = True
            n_in = 0
            for dy, dx in disc(r):
                y, x = cy + dy, cx + dx
                inside = (0 <= y < h and 0 <= x < w and comp[y, x])
                if inside:
                    n_in += 1
                    if blocked[y, x] or claimed[y, x]:
                        ok = False
                        break
                elif not shot:
                    # a framed component demands the whole bead sit inside the silhouette
                    ok = False
                    break
            # CLIPPED BEADS on a component with no interior. A boot is four or five pixels across,
            # so a 5px plus almost never fits whole and the strict test leaves the warrior boot with
            # TWO beads on it — a flat recolor with a couple of dots, which is not a slot delivery.
            # On such a fitting the bead is set proud of the edge and the silhouette cuts it, exactly
            # as a real bead soldered to a narrow strap is; three of its five pixels must still land
            # on the piece or it is a crumb rather than a bead.
            if ok and n_in < min(len(disc(r)), 3):
                ok = False
            if not ok:
                continue
            for dy, dx in disc(r):
                y, x = cy + dy, cx + dx
                if 0 <= y < h and 0 <= x < w and comp[y, x]:
                    claimed[y, x] = True
            if gap:
                for dy, dx in disc(r + gap):
                    y, x = cy + dy, cx + dx
                    if 0 <= y < h and 0 <= x < w:
                        blocked[y, x] = True
            out.append((cy, cx, r))

    # THE SHOT — the finest grain, a single pixel, and the third size class. A 13px torso has room
    # for exactly two disc radii (a 3px bead and a 5px bead; a 7px one is over half the chest wide
    # and stops being a member of a field at all — see --sweep), and two sizes is an alternation,
    # not a grading. Real granulation has the answer already: below the smallest bead the workshop
    # lays SHOT, single grains dropped into the crevices where nothing rounder will go. So the last
    # pass places a 1px granule on every leftover pixel that is COMPLETELY ENCLOSED by beads — all
    # four neighbours already claimed. That is deliberately restrictive: it takes the deep
    # interstices and leaves the wider hollows as bed, so the ground survives where it genuinely is
    # ground and the field gains a third size class without going solid.
    # THE SHOT — a single-pixel granule, the finest grain, and it exists for exactly ONE situation:
    # a component too narrow for the packing to get started. A boot at this scale is four or five
    # pixels across and is all boundary, so a 5px plus almost never fits: the whole warrior boot
    # takes TWO beads and is otherwise a flat recolor, which is not a slot delivery. This is the
    # same starvation the 52nd hit with its margin, and it gets the same adaptive answer — a
    # component with no real interior is allowed the finest grain, which is also what a real
    # workshop does, because shot is what you lay on a small fitting there is no room to bead.
    #
    # It is NOT switched on for the broad slots, and that is a measured decision rather than a
    # preference. On a torso the interstices between beads are almost all single pixels fully
    # enclosed by bead, so a shot pass there placed 56 grains against 11 beads, took the bed to 0%,
    # and turned the field into bright speckle with the beads lost inside it. The bed has to survive
    # for the contact to be visible.
    #
    # The rule is anti-adjacent (no grain of shot touching another) and the test is taken against a
    # SNAPSHOT of the beads. Without the snapshot the pass cascades — the first grain makes its
    # neighbour eligible, that one the next, and the component fills solid in a single sweep.
    if shot:
        beads = claimed.copy()
        placed = np.zeros((h, w), dtype=bool)
        for cy, cx in order:
            if claimed[cy, cx] or blocked[cy, cx]:
                continue
            n_bead = n_shot = 0
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                y, x = cy + dy, cx + dx
                if not (0 <= y < h and 0 <= x < w):
                    continue
                if beads[y, x]:
                    n_bead += 1
                if placed[y, x]:
                    n_shot += 1
            if n_bead >= 1 and n_shot == 0:
                claimed[cy, cx] = True
                placed[cy, cx] = True
                out.append((cy, cx, 0))
    return out


def role_field(comp, rmax=None, rmin=None, gap=None, shot=False):
    """Classify every pixel of the component box into one of the six roles, by growing the packing
    and then modelling each granule as a little sphere lit from the upper left.

    RIM is the granule's own down-right boundary — the contact shadow where it meets the next bead —
    and it is what makes a field of touching circles read as touching SPHERES rather than as a
    tessellation of discs."""
    h, w = comp.shape
    role = np.where(comp, R_GROUND, -1).astype(np.int8)
    granules = pack(comp, rmax, rmin, gap, shot)
    owner = -np.ones((h, w), dtype=np.int32)
    for i, (cy, cx, r) in enumerate(granules):
        for dy, dx in disc(r):
            y, x = cy + dy, cx + dx
            if 0 <= y < h and 0 <= x < w and comp[y, x]:
                owner[y, x] = i
    for cy, cx, r in granules:
        if r == 0:
            role[cy, cx] = R_LIT              # a single grain of shot in a crevice
            continue
        if r == 1:
            # too small for a specular pip; a 5px plus reads as a bead from the two lit arms alone
            role[cy, cx] = R_LIT
            for dy, dx, v in ((-1, 0, R_MID), (0, -1, R_MID), (0, 1, R_RIM), (1, 0, R_RIM)):
                if 0 <= cy + dy < h and 0 <= cx + dx < w and comp[cy + dy, cx + dx]:
                    role[cy + dy, cx + dx] = v
            continue
        # RADIAL dome shading — concentric, not directional. The first cut shaded each bead by the
        # light direction alone (bright upper-left crescent, dark lower-right), which is correct for
        # a sphere and completely illegible here: a packed field of crescents puts every bead's
        # bright side hard against its neighbour's dark side, the eye joins them across the contact,
        # and what comes out is a marbled diagonal streak — the piece reads as figured stone, not as
        # beads, and the sweep variants become indistinguishable from each other. A bead only reads
        # as a bead at this scale if its tone is a function of RADIUS FROM ITS OWN CENTRE: bright
        # core, mid annulus, dark rim all the way round, so the shape closes. The light survives as
        # a bias on top of that — the pip sits up-left of the core, and the rim goes one stop darker
        # on the down-right where the contact shadow falls — but the concentric ring is what carries
        # the form.
        for dy, dx in disc(r):
            y, x = cy + dy, cx + dx
            if not (0 <= y < h and 0 <= x < w and comp[y, x]):
                continue
            rr = (dy * dy + dx * dx) ** 0.5 / r
            if rr <= 0.36:
                role[y, x] = R_LIT
            elif rr <= 0.74:
                role[y, x] = R_MID
            else:
                role[y, x] = R_RIM if (dy + dx) > 0 else R_DARK
        if 0 <= cy - 1 < h and 0 <= cx - 1 < w and comp[cy - 1, cx - 1]:
            role[cy - 1, cx - 1] = R_PIP

    # THE FILLET. A circle packing can never close: however well the beads are graded there is
    # always an interstice left where three of them meet, and on a 13px slot those leftovers came to
    # 44% of the torso — at which point the bed is the majority of the piece and what the eye reads
    # is dark armour with some studs on it, i.e. the 13th studwork with a fussy stud. In real
    # granulation the beads are fused with solder that wicks up into the angle between them and
    # leaves a fillet, so an interstitial pixel touching TWO OR MORE DIFFERENT beads is not bed at
    # all — it is metal in the crease, and it takes the bead ramp's dark stop. The bed then survives
    # only where it genuinely is bed: the wider hollows that touch one bead or none. That both
    # halves the dark area and strengthens the one thing the axis rests on, because a fillet exists
    # only where two beads are in CONTACT and is therefore drawn evidence of it.
    for y in range(h):
        for x in range(w):
            if role[y, x] != R_GROUND:
                continue
            seen = set()
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                yy, xx = y + dy, x + dx
                if 0 <= yy < h and 0 <= xx < w and owner[yy, xx] >= 0:
                    seen.add(int(owner[yy, xx]))
            if len(seen) >= 2:
                role[y, x] = R_DARK
    return role


def paint_granulation(fr, comp_full, stops, rmax=None, rmin=None, gap=None):
    """Paint the packing onto one component. Only opaque body pixels are ever painted, so this
    cannot create strays and cannot change the silhouette.

    The BEZEL is applied last and overrides everything. On a component with a real interior every
    boundary pixel takes the solid MID stop: that is how a granulated panel is actually made (the
    beads are soldered inside a raised wire border, and a bead soldered on the very edge falls off),
    it keeps the brightest stop off the silhouette per the standing rule, and it keeps the darkest
    stop off it too, so no dome ever grows the full-silhouette dark rim. On a component with no
    interior — every boot — the bezel is skipped and the edge rule is honoured by demotion instead."""
    if comp_full.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    pip, lit, mid, dark, rim, ground = stops
    table = (pip, lit, mid, dark, rim, ground)

    left, right, up, down = _neighbours(comp)
    interior = comp & left & right & up & down
    boundary = comp & ~interior
    thin = comp & ~(left & right)
    framed = int(interior.sum()) >= MARGIN_MIN
    # An unframed component (every boot) is where the packing starves — see the shot pass in pack().
    role = role_field(comp, rmax, rmin, gap, shot=not framed)

    # demotion table for an unframed component's boundary: never the brightest, never the darkest
    demote = {R_PIP: R_MID, R_LIT: R_MID, R_MID: R_MID,
              R_DARK: R_DARK, R_RIM: R_DARK, R_GROUND: R_MID}

    for y, x in zip(ys, xs):
        ly, lx = int(y) - y0, int(x) - x0
        r = int(role[ly, lx])
        if r < 0:
            continue
        if thin[ly, lx] or (framed and boundary[ly, lx]):
            rgb = mid
        elif boundary[ly, lx]:
            rgb = table[demote[r]]
        else:
            rgb = table[r]
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
    stops = GRAIN[cls]
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
        paint_granulation(fr, comp, stops)
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
    packing can be judged on a shape with the features the real slots have — a wide open middle
    where the big beads should land, and taper and corners where the small ones should."""
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


def swatch(path='_diag_granulation_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the sphere modelling, the
    contact rims and — the thing that actually has to work — the GRADING (big beads in the open,
    small ones down in the taper and the corners) can be judged before any sheet is written."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_granulation(a, m, GRAIN[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def sweep(path='_diag_granulation_sweep.png', zoom=11):
    """Render the warrior chest and leg idle frames across the radius bound, plus the FORCED-GAP
    control, so the two collapses can be seen rather than asserted: at RMAX 1 and 2 into the 13th
    studwork and the 41st bead-and-reel, at RMAX 4 and 5 into a single boss (8th aegis roundel), and
    with the contact broken into a scatter of graded dots on a ground — studwork again."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    variants = [('RMAX=1', dict(rmax=1)), ('RMAX=2', dict(rmax=2)), ('RMAX=3', dict(rmax=3)),
                ('RMAX=4', dict(rmax=4)), ('RMAX=5', dict(rmax=5)),
                ('RMAX=2 GAP=1', dict(rmax=2, gap=1))]
    for name, kw in variants:
        col = []
        for arr, crop in ((base, (26, 20, 54, 46)), (legs, (26, 36, 54, 62))):
            src = arr[0:FH, 0:FW]
            a = src[..., 3] > 0
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            comp = (lbl == int(counts.argmax())) if n else a
            fr = np.zeros_like(src)
            paint_granulation(fr, comp, GRAIN['warrior'], **kw)
            col.append(Image.fromarray(fr).crop(crop))
        cells.append((name, col))
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
    print('wrote %s (radius sweep + forced-gap control - no sheets written)' % path)


def _contact_fraction(comp, granules):
    """Fraction of granules that touch (8-adjacency) at least one other granule. Contact is the
    load-bearing property of this axis; a low fraction means the field is a scatter, not a packing."""
    h, w = comp.shape
    owner = -np.ones((h, w), dtype=np.int32)
    for i, (cy, cx, r) in enumerate(granules):
        for dy, dx in disc(r):
            y, x = cy + dy, cx + dx
            if 0 <= y < h and 0 <= x < w and comp[y, x]:
                owner[y, x] = i
    touch = set()
    for y in range(h):
        for x in range(w):
            o = owner[y, x]
            if o < 0:
                continue
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < h and 0 <= xx < w and owner[yy, xx] >= 0 and owner[yy, xx] != o:
                        touch.add(o)
                        touch.add(int(owner[yy, xx]))
    return (len(touch) / len(granules)) if granules else 0.0


def dump_cells():
    """ASCII dump of the role field plus the RADIUS HISTOGRAM and the CONTACT FRACTION.

    These two numbers are the acceptance test for this axis, and they are the two ways it can die:
      * a histogram with ONE class in it means the packing had nothing to grade and the field is a
        regular stud grid — the 13th STUDWORK. Wanted: at least two classes on every slot, and a
        MIXTURE THAT DIFFERS BETWEEN SLOTS, which is the shape-determined claim made checkable.
      * a contact fraction near zero means the beads are not touching and the field is a scatter of
        dots on a ground — the 13th STUDWORK again, from the other direction. Wanted: > 0.8.
    Both are printed for the synthetic plate and for the real warrior torso, leg, boot and dome,
    because the whole point of a shape-determined axis is that the answer differs per slot."""
    legend = {R_PIP: '*', R_LIT: '#', R_MID: '+', R_DARK: '-', R_RIM: ',', R_GROUND: '.'}
    cases = [('synthetic plate 30x44', _test_plate())]
    for label, fname, largest in (('warrior torso', 'armor_chest_4.png', True),
                                  ('warrior legs', 'armor_pants_4.png', False),
                                  ('warrior boots', 'armor_boots_4.png', False),
                                  ('warrior dome', 'helmet_rare1.png', True)):
        src = load_any(fname)[0:FH, 0:FW]
        a = src[..., 3] > 0
        if largest:
            lbl, n = label4(a)
            counts = np.bincount(lbl.ravel())
            counts[0] = 0
            a = (lbl == int(counts.argmax())) if n else a
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    for label, comp in cases:
        shot = not _has_interior(comp)
        role = role_field(comp, shot=shot)
        gr = pack(comp, shot=shot)
        hist = {}
        for _, _, r in gr:
            hist[r] = hist.get(r, 0) + 1
        print('== %s   RMIN=%d RMAX=%d shot=%s' % (label, RMIN, RMAX, shot))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        print('   granules=%d  radius histogram=%s  distinct radii=%d  contact fraction=%.2f'
              % (len(gr), {k: hist[k] for k in sorted(hist)}, len(hist),
                 _contact_fraction(comp, gr)))
        print('   ground px=%d of %d (%.0f%% interstitial)'
              % (int((role == R_GROUND).sum()), int(comp.sum()),
                 100.0 * (role == R_GROUND).sum() / max(1, comp.sum())))
    print('legend: * pip  # lit  + mid  - dark/fillet  , contact rim  . solder bed')
    print('ACCEPTANCE: >=2 size classes per slot AND a mixture that differs between slots (one class')
    print('everywhere = the 13th studwork), plus a contact fraction > 0.8 (near 0 = a scatter of dots')
    print('on a ground, the 13th studwork again from the other side).')


def main():
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
                # save_finished() rather than a bare .save(): it writes the TaskQuestFinish
                # version stamp, without which a later bulk `sprite_finish.py <dir>` backfill
                # would run the whole chain over these sheets a SECOND time.
                arr, info = finish_array(arr, dst)
                save_finished(arr, dst)
                print('wrote %-64s opaque_px=%-6d finish=%s/%s'
                      % (dst, (arr[..., 3] > 0).sum(), info['slot'], info['variant']))


if __name__ == '__main__':
    main()
