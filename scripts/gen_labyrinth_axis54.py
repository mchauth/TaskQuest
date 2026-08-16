#!/usr/bin/env python3
"""FIFTY-FOURTH net-new-geometry axis for ALL FOUR SLOTS — the LABYRINTH family (ONE continuous
wire): the armour is not covered with a field of ornaments at all. It carries a SINGLE raised wire,
soldered to the plate, which enters the piece at one terminal bead, winds back and forth to visit
every part of it, never once touching or crossing itself, and leaves at the other terminal bead.

    the ornament is  WIRE     (a 1px raised round wire — the whole ornament, one object)
                   + TERMINAL (the wire's two ends, finished as a bright bead; there are exactly
                               TWO on the piece and they are how you know it is one wire)
                   + LIP      (the lit approach on the wire's upper-left flank)
                   + SHADE    (the cast shadow on the wire's lower-right flank)
                   + FLOOR    (the sunk channel the wire winds through)
                   + GROUND   (the deep floor, where the channel is widest)
                   + BEZEL    (a 1px solid margin around the silhouette; see MARGIN_MIN)

*** THIS IS THE FIRST AXIS THAT IS ONE OBJECT. ***
Every one of the fifty-three prior axes is a FIELD — a plurality. Forty stamp a congruent cell on a
lattice, ten run a congruent member along a track, and the recent ones break the cell's content
(48th cosmati a hierarchy, 49th dendrite a descent, 50th runic a vocabulary), its carrier (46th
craquelure aperiodic, 51st flowgrain continuous), its depth (52nd ajoure two surfaces) or its size
(53rd granulation shape-determined) — but in every single one you can point at MANY things and ask
how they relate to each other. Here you cannot: there is exactly one thing on the piece, and the
question the ornament answers is not "how do the elements relate" but "WHERE DOES IT GO". Its
subject is CONNECTIVITY. The 53rd's granules number 11 on a torso and 4 on a boot; this axis's wires
number ONE on the torso and ONE on the boot and ONE on the helmet, and that is not a coincidence of
tuning, it is the definition. A viewer can put a finger on a terminal bead and trace, and the trace
will reach the other terminal having passed through every pixel of wire on the piece. Nothing in the
fifty-three prior axes can be traced, because none of them is connected, and connectedness is not a
property you can add to a field by tuning it — it is a different kind of object.

The families it could be confused with each fail differently, and every one of them fails on a
property that can be COUNTED rather than argued:
  * The 23rd MEANDER is the near miss and the first thing anyone will say. A Greek key is also a
    single wandering line — but it is a PERIODIC BAND: one congruent fret unit translated along a
    track, so the line's whole itinerary is stated by two numbers and repeats every period, and you
    can cut the band anywhere and get the same ornament back. Here there is no unit, no period and
    no track. The wire's every turn is decided by the requirement to reach the parts of THIS
    silhouette it has not been to yet, so no two turns are the same turn and the itinerary cannot be
    stated without the piece. Cut it anywhere and you have destroyed the one property it has.
  * The 49th DENDRITE is the closest topologically and the sharpest distinction, because both are
    acyclic and both are connected: a dendrite is a TREE, this is a PATH, and a path is exactly a
    tree with no branching. The counted difference is the branch count — every dendrite pixel with
    three wire neighbours is a branch point and there are dozens; here there are ZERO, by
    construction and by assertion in the acceptance test — and the endpoint count: a tree has many
    tips, a path has EXACTLY TWO. Let branching in and this axis IS the 49th, which is why the
    generator refuses it rather than damping it.
  * The NET axes (14th lattice, 17th ashlar, 19th honeycomb, 20th trellis, 21st chainmail, 33rd
    octagram) are connected too — and are all CYCLE. A net is nothing but its loops: its cells are
    its subject and every one of them is a closed circuit. A path has no cycle at all, so it encloses
    nothing, so it has no cells, and the space it winds through is one single connected channel
    rather than a set of compartments. Loop count is the check: a net's is large, this axis's is 0.
    Close the wire's two ends together and the loop count goes to 1 and the terminals vanish — and
    what you get is not this axis but a very long cell boundary, which is why the wire is deliberately
    left OPEN.
  * The 30th CABLE and 39th GUILLOCHE interlace, and interlace needs at least two strands and a
    crossing. One strand, and it is self-avoiding: it never crosses itself, so there is no over, no
    under and no braid. The wire's turns look busy in the same way a braid does and the difference is
    visible at 1x in the channel — a braid's ground is a chain of closed eyes, a labyrinth's ground is
    one continuous corridor you could also trace.
  * The 46th CRAQUELURE is the other axis with no repeating unit, and it is a PARTITION: junctions of
    degree three everywhere, every pixel in some cell. This is degree two everywhere and encloses
    nothing. Aperiodicity is what they share; it is the weakest thing about either of them.
  * The 51st FLOWGRAIN has curves that turn as they please, but it has infinitely many of them,
    parallel and never meeting, and its subject is their DIRECTION. Here there is one curve and its
    direction at a point tells you nothing; where it has BEEN is the whole content.

Geometry, per connected component, in the component's own frame:
    elig      = the pixels the wire may occupy: the component's INTERIOR if it has one, else the
                whole component (see MARGIN_MIN — a boot is all boundary and has no interior)
    lattice   = nodes at every PITCH-th row and column, PHASED TO THE COMPONENT'S CENTROID so the
                wire is centred on the piece and does not run its turns off one edge (the 49th's
                lesson, and the reason there is no bright rim)
    adjacency = two nodes PITCH apart, orthogonally, with every pixel of the segment between them
                eligible
    path      = the longest SIMPLE path through that graph: Warnsdorff greedy from every node as a
                start, then a deterministic BACKBITE improvement. No RNG anywhere, so a silhouette
                always yields the same wire and the male and female sheets of one item agree.
    wire      = the node pixels plus every pixel of every traversed segment
    terminals = the first and last node of the path
    relief    = wire is CREST; a field pixel with wire above/left of it is in the wire's cast SHADOW;
                one with wire below/right of it is the lit LIP; the rest is FLOOR, and GROUND where
                the channel is widest.

Authoring philosophy identical to gen_granulation_axis53.py / gen_ajoure_axis52.py: every pattern
pixel is painted ONLY onto pixels ALREADY opaque in the body. Nothing is added, nothing removed, the
silhouette is untouched, so the generator CANNOT create isolated pixels, background bleed, extra
components or a changed mask — it is QA-safe by construction. Sleep frames (fi >= 60) get a plain
body recolor.

FINISHING PASS: this generator does NOT shade for itself. Every sheet goes through
`sprite_finish.finish_array(arr, dst)` and is written with `save_finished()` — the canonical chain
(no-smooth shading with protect=False, shirt pauldron/gorget/chest-plate separation, helmet black
eye+mouth visor with NO full-silhouette rim, hat brim/crease folds for open headgear). See
CONTEXT.md "MANDATORY - the finishing pass". Tenth generator to call it in-line, after axes 45-53.

Run from repo root:
  python3 scripts/gen_labyrinth_axis54.py
  python3 scripts/gen_labyrinth_axis54.py --cells    # ASCII dump + the TOPOLOGY acceptance test
  python3 scripts/gen_labyrinth_axis54.py --swatch   # bare motif on a test plate, no sheets
  python3 scripts/gen_labyrinth_axis54.py --sweep    # PITCH sweep + the branching/closed controls
Then QA (examples):
  python3 scripts/sprite_qa.py _labyrinth_legendary_preview/shirt_warrior_legendary54.png
  python3 scripts/sprite_qa.py _labyrinthdome_helmet_preview/helmet_mage_legendary54.png --y-min 2
  python3 scripts/sprite_qa.py _labyrinth_boots_preview/boots_warrior_legendary_maze.png --y-max 63
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

# --- Labyrinth constants ---------------------------------------------------------------------
# PITCH is the lattice spacing: the wire runs between nodes PITCH apart, so PITCH-1 pixels of
# channel separate two parallel runs of wire. Swept (--sweep) on a real torso AND a real leg, and as
# with the 49th through 53rd, BOTH ends fail INTO an older axis rather than into mush.
#   PITCH 2  the design predicted a dither here and the sweep says otherwise, so the real reason is
#            recorded instead of the guessed one: at PITCH 2 the maze is perfectly legible and it is
#            FLAT. One pixel of channel separates two runs of wire, that pixel always has wire above
#            or to the left of it, so it always takes SHADE and the LIP role NEVER FIRES ANYWHERE ON
#            THE PIECE — the lit approach has nowhere to be. With only the shadow half of the pair
#            surviving there is nothing to say the wire stands proud, and a line with no relief drawn
#            on a plate is the 23rd MEANDER's kind of mark, not this one's. The secondary cost is
#            that wire plus shadow take ~50% of the piece, so the enamel field stops being a field.
#            THE LESSON: check which ROLES a pitch can still express, not just whether the motif
#            resolves. A pitch that resolves and cannot shade is worse than one that shades.
#   PITCH 3  CHOSEN. Two pixels of channel between parallel runs, which is exactly enough to carry
#            the SHADE/LIP pair that says the wire stands proud, and enough nodes on every slot for
#            the path to have to make real decisions: torso 20, thigh 14, dome 15, boot 6 (all
#            measured, --cells). Every turn is visible as a turn.
#   PITCH 4  three pixels of channel and only three or four node columns across a 13px torso, so the
#            path spends most of its length in long straight parallel runs with a turn at each end.
#            Long parallel verticals on a cuirass are the 11th FLUTING with a join at the top, and
#            the sweep frames show exactly that.
#   PITCH 5  one or two runs on a torso and one on a boot. Not a labyrinth, not even a line family —
#            a broad stripe down the piece, i.e. the 8th SIDE-STRIPE.
# Same shape of result as the 50th runic's BAND_P and the 52nd's BAR/OPEN: the usable window for a
# 13px slot is one notch wide, and it is bounded by an older axis on both sides.
PITCH = 3

# A component with fewer than this many INTERIOR pixels (all four 4-neighbours inside the component)
# gets no BEZEL and lays its wire on the whole component instead of on the interior only. Same
# constant and the same measured reason as the 52nd's MARGIN_MIN and the 53rd's: on the real idle
# frames the interior counts are chest 78, helmet dome 59, legs 39 — but BOOTS 2 TO 8, because a
# foot at this scale is four or five pixels across and is ALL boundary. Restrict a boot's wire to its
# interior and there is no wire. So an interior-less component gives up its margin and keeps its
# ornament, and the standing edge rule — brightest stop never on the silhouette, darkest stop never
# on the silhouette, so no dome ever grows the full-silhouette dark rim that mangles patterned
# helmets — is honoured the other way instead, by demotion (see `DEMOTE`).
MARGIN_MIN = 20

# Backbite iterations. The greedy Warnsdorff walk alone typically reaches 80-90% of the nodes; the
# backbite (extend the endpoint if it can, otherwise reverse the tail at a neighbour of the endpoint,
# which keeps the path simple and the same length but hands it a different endpoint) closes almost
# all of the rest. It is capped because coverage is an acceptance criterion, not an obsession — a
# wire that misses two nodes in a corner is still one wire.
BACKBITE = 900

# A component whose lattice yields fewer than this many nodes gets a finer pitch, one notch at a
# time, down to PITCH_MIN. This is the third appearance of the same adaptive-boundary lesson (the
# 52nd's MARGIN_MIN, the 53rd's shot pass) and it is here for the same measured reason: at PITCH 3
# a torso gives 8 nodes and a thigh 5, but a BOOT gives 4 and reaches only 2 of them, which is a
# wire with one bend in it — a tick mark, not a labyrinth. The wire is the ornament, so a component
# that cannot hold a wire long enough to turn twice is given a finer lattice rather than a bare
# recolor. It is deliberately NOT applied to the broad slots: at PITCH 2 the channel is one pixel
# wide, it cannot carry the SHADE/LIP pair, and a 2px alternation across a whole cuirass is the
# dither the sweep rejects.
MIN_NODES = 7
PITCH_MIN = 2

# Per class, six stops, ordered BRIGHTEST FIRST: (term, crest, lip, floor, shade, ground).
#   * TERM and CREST are the WIRE'S ramp; LIP, FLOOR, SHADE and GROUND are the FIELD'S. That split
#     is the first thing this palette got wrong and it inverted the whole image. LIP is the lit
#     approach on the field beside the wire, so the first cut painted it in a pale metal grey on the
#     reasoning that "the lit side is bright" — and because a 3px period gives one pixel of wire to
#     two of field, putting one of those two field pixels on the metal ramp handed the metal TWO
#     THIRDS of the piece. The lit field then welded to the wire it was supposed to sit beside, the
#     two fused into one broad pale mass, and what was left reading as a line was the dark remainder:
#     the figure and the ground had swapped, and the traceable thing was the gap rather than the
#     wire. A field pixel takes a FIELD tone however brightly lit it is. Same failure the 52nd
#     recorded when a mid-luminance liner turned its holes into inlay, arrived at from the other end.
#   * The wire and the plate are DIFFERENT MATERIALS and the difference is carried by HUE, not by a
#     luminance step — at 13px a luminance step alone reads as shading (the 52nd's lesson). Each
#     class pairs a wire metal against a contrasting enamelled field.
#   * No stop is near pure black. HELMET constraint, not taste: the finishing pass carves the visor
#     as black eye and mouth pixels and a near-black stop on the dome swallows the face slit (the
#     49th's lesson). Every class's darkest stop clears channel-sum 150.
#   * The pale stops stay OFF the skin ramp — cool, never a warm off-white, which on a narrow female
#     chest reads as bare shoulder (the 47th's rose-gold lesson). The one warm pale stop in the set
#     is the ranger TERM, and it is allowed because a terminal is TWO PIXELS on a component; the
#     rule is about stops that cover area.
#   * JUDGE A FIELD STOP AFTER THE FINISHING PASS, NOT BEFORE — a new lesson, and both classes that
#     needed re-pitching needed it for this reason. The chain shades with `protect=False` and lifts
#     the lit side hard, so a stop chosen to look right in the generator is not the stop that
#     reaches the sheet. The first cut's warrior oxblood (134,66,64) came out of the finish as a
#     pale SALMON, which is a weak partner for a platinum wire, and its ranger walnut (104,78,54)
#     came out as a light tan sitting squarely ON THE SKIN RAMP — a whole field of it, which is the
#     47th's failure at maximum area rather than on one stop. Both were dropped roughly two steps
#     and the ranger moved off brown entirely: copper wire on DEEP TEAL, which also puts more air
#     between this tier and its neighbours (the 52nd's ranger is green-birch over slate-blue, the
#     53rd's silver-jade on deep forest, and no prior ranger tier uses a warm metal at all).
#   * Deliberately not a recolor of the neighbouring tiers. The 53rd is gold-on-graphite,
#     moonsilver-on-violet, silver-jade-on-forest; the 52nd is blued-steel-over-brass,
#     moonsilver-lilac-over-teal, green-birch-over-slate-blue. Here the FIELD hue — which is the
#     majority of the pixels and therefore what carries at 1x — is oxblood, indigo and walnut, none
#     of which either neighbour uses; and the warrior is deliberately NOT gold for the third tier
#     running.
WIRE = {
    # platinum wire on an oxblood enamel field
    'warrior': ((250, 250, 252), (206, 216, 226), (146, 72, 68),
                (112, 52, 52), (86, 40, 44), (76, 36, 40)),
    # amber-gold wire on an indigo enamel field
    'mage':    ((255, 244, 200), (240, 204, 116), (92, 100, 178),
                (66, 72, 142), (50, 54, 108), (44, 48, 96)),
    # copper wire on a deep teal enamel field
    'ranger':  ((255, 236, 206), (226, 150, 92), (56, 112, 110),
                (40, 90, 90), (34, 74, 76), (28, 62, 64)),
}

# Per-class body tones for the plain recolor, visible on sleep frames only; taken off the field stops
# so the piece reads as one object when the wire is not drawn.
BODY = {
    'warrior': ((84, 42, 46), (150, 76, 72), (206, 214, 224)),
    'mage':    ((46, 50, 102), (78, 84, 156), (238, 204, 122)),
    'ranger':  ((32, 70, 72), (52, 108, 106), (226, 150, 92)),
}

# One config block per slot. `largest` restricts the wire to the biggest connected component
# (torso / dome) so raised arms are not covered; boots/legs pattern all opaque pixels.
SLOTS = {
    'chest': dict(
        outdir='_labyrinth_legendary_preview',
        srcs={'warrior': 'armor_chest_4', 'mage': 'shirt_mage4', 'ranger': 'shirt_ranger4'},
        dst='shirt_%s_legendary54', largest=True,
    ),
    'legs': dict(
        outdir='_labyrinth_legs_preview',
        srcs={'warrior': 'armor_pants_4', 'mage': 'pants_mage4', 'ranger': 'pants_ranger4'},
        dst='pants_%s_legendary54', largest=False,
    ),
    'boots': dict(
        outdir='_labyrinth_boots_preview',
        srcs={'warrior': 'armor_boots_4', 'mage': 'boots_mage4', 'ranger': 'boots_ranger4'},
        dst='boots_%s_legendary_maze', largest=False,
    ),
    'helmet': dict(
        outdir='_labyrinthdome_helmet_preview',
        srcs={'warrior': 'helmet_rare1', 'mage': 'helmet_mage4', 'ranger': 'helmet_ranger4'},
        dst='helmet_%s_legendary54', largest=True,
    ),
}

# role codes, brightest first so DEMOTE can be stated as "never the extremes"
R_TERM, R_CREST, R_LIP, R_FLOOR, R_SHADE, R_GROUND = 0, 1, 2, 3, 4, 5

# On an interior-less component (every boot) there is no bezel to keep the extremes off the
# silhouette, so they are kept off it by demotion instead: the brightest stop (TERM) and the darkest
# (GROUND) are both pulled one step in. The wire itself survives as CREST, which is the point — the
# 53rd's demotion table flattened a boot's ornament to a single mid tone and this one must not.
DEMOTE = {R_TERM: R_CREST, R_CREST: R_CREST, R_LIP: R_LIP,
          R_FLOOR: R_FLOOR, R_SHADE: R_SHADE, R_GROUND: R_FLOOR}


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


def _interior(comp):
    left, right, up, down = _neighbours(comp)
    return comp & left & right & up & down


def _has_interior(comp):
    """True if the component has a real inside — enough pixels with all four 4-neighbours in the
    component to be worth a bezel. False for every boot at this scale; see MARGIN_MIN."""
    return int(_interior(comp).sum()) >= MARGIN_MIN


def lattice(elig, pitch):
    """Node set and adjacency for one component.

    The lattice is PHASED TO THE COMPONENT'S CENTROID rather than to its bounding box corner. That
    is the 49th dendrite's lesson restated: a lattice phased to a corner puts its outermost row hard
    against one edge of the silhouette on some pieces and a full pitch away on others, so the wire
    hugs one side of the chest and leaves a bare band down the other — which at 1x reads as an 8th
    side-stripe with texture next to it, not as an ornament that fills the piece."""
    ys, xs = np.nonzero(elig)
    if len(ys) == 0:
        return [], {}
    oy = int(round(float(ys.mean()))) % pitch
    ox = int(round(float(xs.mean()))) % pitch
    h, w = elig.shape
    nodes = [(int(y), int(x)) for y, x in zip(ys, xs)
             if int(y) % pitch == oy and int(x) % pitch == ox]
    nset = set(nodes)
    adj = {n: [] for n in nodes}
    for (y, x) in nodes:
        for dy, dx in ((pitch, 0), (0, pitch)):
            m = (y + dy, x + dx)
            if m not in nset:
                continue
            # the whole segment between the two nodes must be eligible, or the wire would have to
            # leave the interior (framed) or leave the silhouette (unframed) to get there
            ok = True
            for k in range(1, pitch):
                yy, xx = y + (dy // pitch) * k, x + (dx // pitch) * k
                if not (0 <= yy < h and 0 <= xx < w and elig[yy, xx]):
                    ok = False
                    break
            if ok:
                adj[(y, x)].append(m)
                adj[m].append((y, x))
    for n in adj:
        adj[n].sort()
    return nodes, adj


def longest_path(nodes, adj, backbite=None):
    """The longest SIMPLE path through the lattice graph. Deterministic: no RNG anywhere.

    Two phases, and the second is what makes the axis work rather than merely exist.
      1. WARNSDORFF from every node as a start. At each step move to the unvisited neighbour with
         the fewest unvisited neighbours of its own (ties by y then x). That is the classic
         knight's-tour heuristic and for the same reason: it takes the constrained corners of the
         silhouette while they are still reachable, instead of stranding them.
      2. BACKBITE. Warnsdorff typically strands two or three nodes anyway. If the endpoint has an
         unvisited neighbour, extend to it; otherwise pick a neighbour of the endpoint that IS on
         the path and reverse the tail beyond it. The reversal keeps the path simple and the same
         length but hands it a DIFFERENT endpoint, from which an extension may exist — so the path
         walks around its own dead ends. The neighbour is chosen by iteration index, which is what
         keeps a stochastic algorithm deterministic here.

    A HAMILTONIAN path does not always exist (a lattice on an irregular silhouette is bipartite and
    the two colour classes rarely balance), so this maximises coverage rather than demanding it, and
    `--cells` reports what fraction was reached. That is honest: a wire that misses one node in a
    corner is still one wire, and the acceptance test that actually matters is the topology, not
    the length."""
    if not nodes:
        return []
    backbite = BACKBITE if backbite is None else backbite
    best = []
    for s in nodes:
        pth = [s]
        vis = {s}
        while True:
            cand = [v for v in adj[pth[-1]] if v not in vis]
            if not cand:
                break
            cand.sort(key=lambda v: (sum(1 for w in adj[v] if w not in vis), v[0], v[1]))
            pth.append(cand[0])
            vis.add(cand[0])
        if len(pth) > len(best):
            best = pth
        if len(best) == len(nodes):
            return best

    pth = list(best)
    vis = set(pth)
    for it in range(backbite):
        if len(pth) == len(nodes):
            break
        e = pth[-1]
        nb = adj[e]
        if not nb:
            break
        ext = [v for v in nb if v not in vis]
        if ext:
            ext.sort(key=lambda v: (sum(1 for w in adj[v] if w not in vis), v[0], v[1]))
            pth.append(ext[0])
            vis.add(ext[0])
            if len(pth) > len(best):
                best = list(pth)
            continue
        v = nb[it % len(nb)]
        i = pth.index(v)
        if i >= len(pth) - 2:
            pth.reverse()
            continue
        pth = pth[:i + 1] + pth[i + 1:][::-1]
    return best


_ROLE_CACHE = {}


def role_field(comp, pitch=None, branch=False, closed=False, adapt=True):
    """Classify every pixel of the component box into one of the six roles.

    `branch` and `closed` exist only for --sweep: they are the two CONTROLS that show what this axis
    turns into when its defining property is removed. `branch` lets the wire fork (a spanning tree
    instead of a path) — that is the 49th DENDRITE. `closed` joins the two terminals when they
    happen to be adjacent — that is a cycle, i.e. one very long net cell, the 14th LATTICE's kind of
    object. Neither is reachable from the real generator."""
    pitch = PITCH if pitch is None else pitch
    key = (comp.shape, comp.tobytes(), pitch, branch, closed, adapt)
    hit = _ROLE_CACHE.get(key)
    if hit is not None:
        return hit

    h, w = comp.shape
    framed = _has_interior(comp)
    elig = _interior(comp) if framed else comp
    nodes, adj = lattice(elig, pitch)
    # ADAPTIVE PITCH — see MIN_NODES. A component too small to hold a wire that turns is given a
    # finer lattice rather than left as a flat recolor.
    while adapt and len(nodes) < MIN_NODES and pitch > PITCH_MIN:
        pitch -= 1
        nodes, adj = lattice(elig, pitch)

    wire = np.zeros((h, w), dtype=bool)
    terms = []
    if branch:
        # CONTROL ONLY — a spanning tree, i.e. the 49th dendrite. Deterministic BFS.
        seen = set()
        edges = []
        for s in nodes:
            if s in seen:
                continue
            seen.add(s)
            q = [s]
            while q:
                n = q.pop(0)
                for m in adj[n]:
                    if m not in seen:
                        seen.add(m)
                        edges.append((n, m))
                        q.append(m)
        path = []
        for a, b in edges:
            _stroke(wire, a, b, elig)
        for n in nodes:
            wire[n] = elig[n]
    else:
        path = longest_path(nodes, adj)
        for a, b in zip(path, path[1:]):
            _stroke(wire, a, b, elig)
        for n in path:
            wire[n] = elig[n]
        if len(path) >= 2:
            if closed and abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) == pitch:
                _stroke(wire, path[0], path[-1], elig)   # CONTROL ONLY
            else:
                terms = [path[0], path[-1]]

    role = np.where(comp, R_GROUND, -1).astype(np.int8)
    role[comp & wire] = R_CREST

    # RELIEF. The wire is round and stands proud of the plate, and the light is upper-left as
    # everywhere in this set. A field pixel with wire ABOVE or LEFT of it lies in the wire's cast
    # shadow; one with wire BELOW or RIGHT of it faces the wire's lit flank. Two pixels of channel
    # at PITCH 3 is exactly enough to show one of each, which is why 3 is the smallest pitch at
    # which the wire reads as RAISED rather than as a drawn line — and a drawn line on a plate is
    # the 23rd meander's kind of mark, not this one's.
    up_left = np.zeros((h, w), dtype=bool)
    dn_right = np.zeros((h, w), dtype=bool)
    up_left[1:, :] |= wire[:-1, :]
    up_left[:, 1:] |= wire[:, :-1]
    up_left[1:, 1:] |= wire[:-1, :-1]
    dn_right[:-1, :] |= wire[1:, :]
    dn_right[:, :-1] |= wire[:, 1:]
    dn_right[:-1, :-1] |= wire[1:, 1:]
    field = comp & ~wire
    role[field & up_left] = R_SHADE
    role[field & ~up_left & dn_right] = R_LIP
    # FLOOR where the channel is narrow, GROUND where it opens out — the far corners of a silhouette
    # the lattice could not reach. Keeping those two apart is what stops an unreachable corner
    # reading as a blank patch of a different garment.
    near = np.zeros((h, w), dtype=bool)
    for dy in (-2, -1, 0, 1, 2):
        for dx in (-2, -1, 0, 1, 2):
            sy0, sy1 = max(0, dy), h + min(0, dy)
            sx0, sx1 = max(0, dx), w + min(0, dx)
            near[sy0:sy1, sx0:sx1] |= wire[sy0 - dy:sy1 - dy, sx0 - dx:sx1 - dx]
    role[field & ~up_left & ~dn_right & near] = R_FLOOR

    # THE TERMINALS. Exactly two on the piece, and they are the axis's own signature: they say that
    # what you are looking at has ends, therefore is not a net and not a field, therefore can be
    # traced. They are painted last so nothing overrides them.
    for t in terms:
        if comp[t]:
            role[t] = R_TERM

    out = (role, wire, path, nodes)
    _ROLE_CACHE[key] = out
    return out


def _stroke(wire, a, b, elig):
    """Lay the wire along the straight segment between two adjacent nodes."""
    (y0, x0), (y1, x1) = a, b
    n = max(abs(y1 - y0), abs(x1 - x0))
    sy = (y1 - y0) // n if n else 0
    sx = (x1 - x0) // n if n else 0
    for k in range(n + 1):
        y, x = y0 + sy * k, x0 + sx * k
        if 0 <= y < wire.shape[0] and 0 <= x < wire.shape[1] and elig[y, x]:
            wire[y, x] = True


def paint_labyrinth(fr, comp_full, stops, pitch=None, branch=False, closed=False, adapt=True):
    """Paint the wire onto one component. Only opaque body pixels are ever painted, so this cannot
    create strays and cannot change the silhouette.

    The BEZEL is applied last and overrides everything. On a component with a real interior every
    boundary pixel takes the solid LIP stop: that is how a wired panel is actually made (the wire is
    laid inside a raised border and a wire soldered on the very edge peels), it keeps the brightest
    stop off the silhouette per the standing rule, and it keeps the darkest stop off it too, so no
    dome ever grows the full-silhouette dark rim. On a component with no interior — every boot — the
    bezel is skipped and the edge rule is honoured by DEMOTE instead."""
    if comp_full.sum() < MIN_PX:
        return
    ys, xs = np.nonzero(comp_full)
    y0, x0 = int(ys.min()), int(xs.min())
    y1, x1 = int(ys.max()), int(xs.max())
    comp = comp_full[y0:y1 + 1, x0:x1 + 1]

    term, crest, lip, floor, shade, ground = stops
    table = (term, crest, lip, floor, shade, ground)

    role, _, _, _ = role_field(comp, pitch, branch, closed, adapt)
    interior = _interior(comp)
    boundary = comp & ~interior
    left, right, _, _ = _neighbours(comp)
    thin = comp & ~(left & right)
    framed = int(interior.sum()) >= MARGIN_MIN

    for y, x in zip(ys, xs):
        ly, lx = int(y) - y0, int(x) - x0
        r = int(role[ly, lx])
        if r < 0:
            continue
        if thin[ly, lx] or (framed and boundary[ly, lx]):
            rgb = lip
        elif boundary[ly, lx]:
            rgb = table[DEMOTE[r]]
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
    stops = WIRE[cls]
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
        # ONE WIRE PER CONNECTED COMPONENT — and this is not a detail, it is the axis's own claim
        # applied honestly. A wire is a physical object soldered to a physical plate, so it cannot
        # jump the gap between the two legs of a pair of chausses or between the left boot and the
        # right one; those are separate pieces of armour and each carries its own wire with its own
        # two terminals. The first cut passed the whole opaque mask in as one blob, and because a
        # path cannot cross the gap it filled ONE leg and left the other a flat recolor. Splitting
        # by component is what makes the ornament land on every piece.
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
            paint_labyrinth(fr, comp, stops)
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
    """A synthetic armour-ish plate: a rounded slab with a neck notch and a waist pinch, so the wire
    can be judged on a shape with the features the real slots have — a wide open middle it has to
    fill, and taper and corners it has to reach into without stranding them."""
    m = np.zeros((h, w), dtype=bool)
    _, xx = np.mgrid[0:h, 0:w]
    cx = w / 2.0
    for y in range(h):
        ty = y / (h - 1.0)
        hw = 8.5 - 4.0 * abs(ty - 0.55) - 2.5 * max(0.0, 0.18 - ty) * 6.0
        hw = max(hw, 1.5)
        m[y, :] = np.abs(xx[y, :] - cx) <= hw
    m[0:3, int(cx) - 2:int(cx) + 3] = False          # neck notch
    return m


def swatch(path='_diag_labyrinth_swatch.png', zoom=12):
    """Render the bare motif on the test plate for all three classes, so the relief (crest / lit lip
    / cast shadow), the terminal beads and — the thing that actually has to work — the TRACE (that
    the eye can follow one wire from one bead to the other) can be judged before any sheet."""
    m = _test_plate()
    h, w = m.shape
    pad = 3
    tw, th = w * zoom, h * zoom
    img = Image.new('RGBA', (tw * 3 + pad * 4, th + pad * 2), (24, 24, 28, 255))
    for k, cls in enumerate(('warrior', 'mage', 'ranger')):
        a = np.zeros((h, w, 4), dtype=np.uint8)
        paint_labyrinth(a, m, WIRE[cls])
        t = Image.fromarray(a).resize((tw, th), Image.NEAREST)
        img.paste(t, (pad + k * (tw + pad), pad))
    img.save(path)
    print('wrote %s (motif only - no sheets written)' % path)


def sweep(path='_diag_labyrinth_sweep.png', zoom=11):
    """Render the warrior chest and leg idle frames across PITCH, plus the two CONTROLS, so the
    collapses can be seen rather than asserted: at PITCH 2 into a dither (16th twill), at 4 and 5
    into parallel runs (11th fluting / 8th side-stripe), with branching allowed into the 49th
    dendrite, and with the wire closed into a single long net cell."""
    base = load_any('armor_chest_4.png')
    legs = load_any('armor_pants_4.png')
    cells = []
    variants = [('PITCH=2', dict(pitch=2)), ('PITCH=3', dict(pitch=3)), ('PITCH=4', dict(pitch=4)),
                ('PITCH=5', dict(pitch=5)), ('P=3 BRANCH', dict(pitch=3, branch=True)),
                ('P=3 CLOSED', dict(pitch=3, closed=True))]
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
            paint_labyrinth(fr, comp, WIRE['warrior'], adapt=False, **kw)
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
    print('wrote %s (pitch sweep + branch/closed controls - no sheets written)' % path)


def topology(wire, path, nodes):
    """The acceptance test, and it is a NEW KIND of one. Every previous axis is accepted on a
    STATISTIC of its field — the 46th's cell count, the 48th's size ratio, the 50th's glyph
    survival, the 52nd's distinct-hole appearances, the 53rd's radius histogram and contact
    fraction. A field is the sort of thing you can only measure. This axis is ONE object, so it is
    accepted on its TOPOLOGY, which is not a measurement but a fact:

        components == 1      it is one wire, not several
        branch points == 0   no wire pixel has three wire neighbours -> a path, not the 49th's tree
        endpoints == 2       exactly two terminals -> not a cycle, so not a net cell
        loops == 0           it encloses nothing -> not the 14th lattice
        traceable == True    walking from one terminal reaches EVERY wire pixel and arrives at the
                             other -> the claim the whole axis rests on, checked rather than argued
    """
    h, w = wire.shape
    ys, xs = np.nonzero(wire)
    px = list(zip(ys.tolist(), xs.tolist()))
    if not px:
        return dict(n=0, comps=0, branch=0, ends=0, loops=0, traceable=False, cover=0.0)
    pset = set(px)

    def nb(p):
        y, x = p
        return [q for q in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)) if q in pset]

    deg = {p: len(nb(p)) for p in px}
    branch = sum(1 for p in px if deg[p] >= 3)
    ends = sum(1 for p in px if deg[p] == 1)
    # components + cyclomatic number (loops) of the wire graph
    seen = set()
    comps = 0
    edges = 0
    for s in px:
        if s in seen:
            continue
        comps += 1
        seen.add(s)
        st = [s]
        while st:
            p = st.pop()
            for q in nb(p):
                edges += 1
                if q not in seen:
                    seen.add(q)
                    st.append(q)
    edges //= 2
    loops = edges - len(px) + comps
    # traceable: walk from one end and see whether every wire pixel is reached in order
    traceable = False
    if ends == 2 and branch == 0 and comps == 1:
        start = next(p for p in px if deg[p] == 1)
        walk = [start]
        prev = None
        cur = start
        while True:
            nxt = [q for q in nb(cur) if q != prev]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
            walk.append(cur)
        traceable = (len(walk) == len(px) and deg[walk[-1]] == 1)
    return dict(n=len(px), comps=comps, branch=branch, ends=ends, loops=loops,
                traceable=traceable, cover=(len(path) / len(nodes)) if nodes else 0.0)


def dump_cells():
    """ASCII dump of the role field plus the TOPOLOGY acceptance test on every real slot."""
    legend = {R_TERM: '@', R_CREST: '#', R_LIP: '+', R_FLOOR: '-', R_SHADE: ',', R_GROUND: '.'}
    cases = [('synthetic plate 30x44', _test_plate())]
    # Every case is ONE CONNECTED COMPONENT — a single leg, a single boot — because that is the
    # unit the wire is laid on (see build()).
    for label, fname in (('warrior torso', 'armor_chest_4.png'),
                         ('warrior leg', 'armor_pants_4.png'),
                         ('warrior boot', 'armor_boots_4.png'),
                         ('warrior dome', 'helmet_rare1.png')):
        src = load_any(fname)[0:FH, 0:FW]
        a = src[..., 3] > 0
        lbl, n = label4(a)
        counts = np.bincount(lbl.ravel())
        counts[0] = 0
        a = (lbl == int(counts.argmax())) if n else a
        ys, xs = np.nonzero(a)
        cases.append((label, a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]))

    allpass = True
    for label, comp in cases:
        role, wire, path, nodes = role_field(comp)
        t = topology(wire, path, nodes)
        framed = _has_interior(comp)
        print('== %s   PITCH=%d framed=%s' % (label, PITCH, framed))
        for y in range(comp.shape[0]):
            print('   ' + ''.join(legend[int(v)] if comp[y, x] else ' '
                                  for x, v in enumerate(role[y])))
        ok = (t['comps'] == 1 and t['branch'] == 0 and t['ends'] == 2
              and t['loops'] == 0 and t['traceable'])
        allpass = allpass and ok
        print('   nodes=%-3d visited=%-3d coverage=%.2f  wire px=%d of %d (%.0f%%)'
              % (len(nodes), len(path), t['cover'], t['n'], int(comp.sum()),
                 100.0 * t['n'] / max(1, comp.sum())))
        print('   components=%d  branch points=%d  endpoints=%d  loops=%d  traceable=%s   -> %s'
              % (t['comps'], t['branch'], t['ends'], t['loops'], t['traceable'],
                 'PASS' if ok else 'FAIL'))
    print('legend: @ terminal bead  # wire  + lit lip  - channel floor  , cast shadow  . deep floor')
    print('ACCEPTANCE (topology, not statistics): components 1, branch points 0, endpoints 2,')
    print('loops 0, traceable True — ONE open wire that can be walked end to end. Branch points > 0')
    print('is the 49th dendrite; loops > 0 is the 14th lattice; components > 1 is a field again and')
    print('the axis has no claim left at all.')
    print('OVERALL: %s' % ('ALL PASS' if allpass else 'FAIL'))


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
