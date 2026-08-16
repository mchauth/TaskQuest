# TaskQuest Project Context

## Project
- **Name**: TaskQuest — pixel art RPG habit tracker
- **Repo**: mchauth/TaskQuest-HTML (GitHub Pages)
- **Main file**: index.html
- **Access token**: <YOUR_GITHUB_TOKEN>

---

## MANDATORY — the finishing pass (read this before generating anything)

**Every sprite sheet a generator produces MUST go through `scripts/sprite_finish.py`.**
Do not write your own shading in a new `gen_*.py`. In the generator, replace the
per-script `shade(...)` call with:

```python
from sprite_finish import finish_array
arr, info = finish_array(arr, dst)     # dst = the filename about to be saved
Image.fromarray(arr).save(dst)
```

This is what gives every new design, automatically:

| Slot | Applied |
|---|---|
| helmet | **black eye + mouth slits** (one of 5 visor variants, hashed from the filename) |
| helmet with no face coverage | it's a hat/hood → brim + crease fold shading instead |
| shirt | shoulder/pauldron plates, metallic sheen, gorget, chest plate separation |
| all slots | no-smooth shading with `protect=False` |

Two rules that are easy to get wrong and have both caused real damage:

1. **`protect=False` is required when shading armour.** The shader's skin/hair guard
   misreads gold, tan and brown armour as hair and leaves 30–57% of it unshaded while
   shading its neighbours — the sheet comes out patchy. `finish_array` handles this;
   any other shading call must pass it too.
2. **No full-silhouette dark rim on helmets.** A visor is only the black eye/mouth
   pixels plus local brow/cheek shading. Darkening the whole helmet boundary swamps
   coloured and patterned domes.

Scope: generate into staged `_*_preview/` dirs only. **Never write to
`sprites/preview_assets/char/`** — that is what the app currently ships.
Full detail: SPRITE_SPEC.md §0.

---

## STAGED — awaiting daily approval (do NOT push until Matt OKs)

- **78th net-new-geometry axis — WARRANT (the plate carries TWO ornaments in two inks — a PACKING of
  POSTS and a COVERING of GROOVES — and the law is that THEY COUNT THE SAME, which is a PROOF, drawn
  on the garment, that no plate on this silhouette could ever carry more), all 4 slots**
  (2026-08-10): the ground is a BAY GRID — the cloth is cut into three-pixel CELLS on one phase of a
  three-pixel grid, and the cells, the BANDS they lie in and the FILES they stand in all belong to
  the silhouette; the painter says only which of the nine phases it used, and the plate is its own
  key, because a post's own two pixels give the phase away. A PILLAR is a bright post two pixels tall
  standing in the lower middle of a cell with a hard shadow down its left flank, and no two pillars
  share a band or a file. A LINTEL is a dark DASHED groove incised along a whole band or down a whole
  file, and every cell the garment offers lies under one.
  **THIS IS THE FIRST LAW IN THE PROJECT THAT CERTIFIES SOMETHING ABOUT EVERY OTHER PLATE ON THE SAME
  GARMENT.** The 77th CLASP said that nothing could be added to THIS PLATE and nothing taken from it —
  a statement about one picture and its neighbours, and a plate can be pinned and still be a poor
  plate. This one closes that gap the only way a picture can, **by carrying its own proof**: a packing
  can never outnumber a covering, so a plate on which the two are EQUAL has forced both to the same
  number, and that number is then the most posts the garment can hold AND the fewest grooves that can
  cover it. 77th = PINNED, a local fact. 78th = PROVED, a global one, and the certificate is four
  numbers the reader counts off the plate rather than a search through the pictures nobody drew.
  (König's theorem is what does the work, and it is why the second ink is on the garment at all: the
  posts alone would be a CLAIM, the posts and the grooves together are an ARGUMENT.)
  **CLASS IDENTITY IS A SIDE — HOW MUCH OF THE PROOF LIES DOWN**: warrior 0 (the argument stands up
  entirely, every groove in it a file), mage 1, ranger 2. Exactly one end of every post's cell is
  sealed — forced by the equality, not chosen — so the class is read by counting the lying grooves and
  nothing else. **FIRST CLASS IDENTITY THAT IS A PROPERTY OF THE ARGUMENT AND NOT OF THE ORNAMENT THE
  READER CAME TO LOOK AT**: two plates of different classes can carry THE VERY SAME POSTS in the very
  same cells, pixel for pixel identical in their bright ink, and differ only in how they prove it is
  the best packing there is. Not a count (67th), ceiling (68th), multipole order (69th), motions
  (70th), fraction of a move (71st), coalition (72nd), precision (73rd), obstructions (74th), depth
  (75th), excess (76th) or price (77th) — every one of those is a fact about the marks. Counting the
  LYING grooves rather than the standing ones is itself arithmetic and not taste: on a garment taller
  than it is wide the standing grooves are nearly all of them and their number moves pose to pose,
  while the lying ones are few and steady. `--reach` enumerates every minimum covering each garment
  admits and tries every way of handing the three identities out: **this batch's assignment dresses
  15/24 and IS the best any assignment could do.**
  **THE ACCEPTANCE TEST IS A NEW KIND — AN AUDIT.** Every previous test interrogates the plate and
  takes the plate's own arithmetic as the standard. This one does not trust it at all: for every
  shipped pose the file recomputes, from the outline alone and by two completely different methods —
  Kuhn's augmenting paths for the packing, a branching search over the cells for the covering — the
  largest packing and the smallest covering the garment admits, and asks whether the ink agrees.
  **525/525 shipped plates agree, with slack zero everywhere.** First test whose subject is a claim
  the plate makes about pictures other than itself.
  **EIGHT CLAUSES — the most any axis has carried**, because there are two ornaments to keep honest:
  GRID, POST, ROOK, SHIELD, WARRANT, SIDE, LIVE, LEGIBLE. **15/24 sheets ALL PASS** (525 plates,
  1602 posts stood, 1602 grooves incised, **0 violations on all eight clauses**, 0 silent).
  **NINE CONTROLS.** RANDOM 429/525 (the null hypothesis — a random set of cells of the right size is
  sometimes a packing, and the file says so), DEAD 0/78 live=78, UNSEALED 0/525 (SHIELD and WARRANT
  both), OVERSEALED 0/525, SHORT 0/525 — **and OVERSEALED and SHORT break the SAME clause from
  OPPOSITE ends, which is what it means for a law to be an EQUALITY and not a bound** — SWAPPED 0/444
  (LAWFUL AND MISNAMED), OFFGRID 0/525, CLIPPED 0/525, FLAT 0/525.
  **THE GROOVES ARE DASHED, AND THAT IS STRUCTURAL AS WELL AS DECORATIVE.** A solid rule every three
  pixels is fluting, and the 11th and 43rd axes are already fluting; dashing also puts each of the
  four kinds of mark on its OWN residue class of the grid — band grooves (0,1) (0,2), file grooves
  (1,2) (2,2), flanks (1,0) (2,0), posts (1,1) (2,1) — so no mark can counterfeit another however
  short it is, and the reading is unambiguous by arithmetic rather than by luck.
  **ALL SIX BOOTS ARE PLAIN AND REPORTED**: a boot in its worst pose is 27 pixels of cloth, which at
  three pixels of pitch is ONE cell — one post, one groove, equal in number and saying nothing
  whatever, which is exactly what clause LIVE is for. Relief survives the finishing pass at 95–100%.
  Repaint only, silhouette untouched (**0 dropped**; chest strays 510/440 identical to the approved
  72nd–77th batches — the finishing pass's shoulder plates), **sprite_qa 24/24 ALL PASS** (helmets
  `--y-min 2`, pants/boots `--y-max 63`). Palettes deliberately unrelated to the 74th–77th: warrior
  **DEEP TEAL cloth, IRON grooves, PALE GOLD posts**, ranger **PLUM and IVORY**, mage **MOSS and ICE**.
  Staged in `_warrant_legendary_preview/`, `_warrant_legs_preview/`, `_warrant_boots_preview/`,
  `_warrantdome_helmet_preview/`. Approval panels `_PREVIEW_warrant_*.png`; evidence
  `_ZOOM_warrant_certificate.png` (one cuirass with every cell ringed, and the two rivals the
  arithmetic rules out — a fifth post with nowhere to stand, and a covering one groove short that
  leaves a cell naked) and **`_ZOOM_warrant_side.png`, the panel no previous axis could have made**:
  three plates carrying IDENTICAL posts, pixel for pixel, proving three different classes. Generator
  `scripts/gen_warrant_axis78.py`, panels `scripts/preview_axis78.py`.

- **77th net-new-geometry axis — CLASP (the ornament is a set of CLASPS on the garment's own
  lattice, and the law is that the plate is a KNIFE EDGE — NOTHING CAN BE ADDED TO IT AND NOTHING
  CAN BE TAKEN AWAY), all 4 slots** (2026-08-10): the ground is every cloth pixel on one phase of a
  three-pixel grid, so the SOCKETS belong to the silhouette and the painter says only which of the
  nine phases it used — the plate is its own key, because a clasp's two ends are sockets. A clasp is
  a straight bright bar four pixels long joining two neighbouring sockets, lying down or standing
  up, with a hard shadow one down and one left; a socket with no clasp on it carries no ink at all,
  so the reader can see at a glance which sockets are MARRIED and which are BARE.
  **THIS IS THE FIRST LAW IN THE PROJECT THAT IS NOT MONOTONE.** The 68th SEME (a Sidon set) is
  broken by ADDING a mark and survives every deletion; the 76th GAUGE (a complete ruler) is broken
  by TAKING one away and survives every addition; **this one survives neither.** The 76th said of
  the 68th that a law about a set of marks may forbid a repeat or forbid a gap and there is no third
  thing to say — true of laws about DISPLACEMENTS, and the wrong level. One level up a law can be
  closed downwards, closed upwards, or closed neither way, the first seventy-six axes are all of the
  first two kinds, and **this is the third, so the sentence is finished.** The consequence is the
  thing to look at: **THE PICTURE IS PINNED** — no ornament on a lawful plate could have been added
  and none could be spared.
  **CLASS IDENTITY IS A PRICE — what it would cost to carry one more clasp**: warrior 1 (break one
  clasp and two can be made where it was), mage 2, ranger **NOTHING WILL DO IT** — a ranger plate
  already carries the most clasps its garment can ever hold. **FIRST CLASS IDENTITY WHOSE THIRD
  VALUE IS NOT A NUMBER**, and the reader can say so rather than merely fail to find one, because
  Berge's theorem makes it a NON-EXISTENCE: a pairing is the largest there is exactly when no
  alternating chain runs between two bare sockets. It is also **the first class identity that is a
  PLAN THE LAW FORBIDS THE READER TO CARRY OUT** — the price is about a picture better than the one
  shipped that the law will not let anybody paint. Which identity went to which class is arithmetic
  and not taste: `--reach` tries all six ways and this one dresses 17 sheets against 14 for the
  worst.
  **THE ACCEPTANCE TEST IS A NEW KIND — A SQUEEZE.** Every previous axis is broken ONE WAY; this one
  is squeezed from both sides at once. **5866 additions tried and 2916 removals tried across the
  batch, and not one of either left a lawful plate.** The two halves are refused in different
  places and that is worth watching: an addition is caught by the **EYE** (two clasps that meet are
  drawn as one long or one bent bright thing, so the plate stops being made of clasps), a removal by
  the **ARITHMETIC** (what it leaves behind still looks like clasps). Six clauses: LATTICE, BAR,
  KNIFE, PRICE, LIVE, LEGIBLE. **17/24 sheets ALL PASS** (595 plates, 2916 clasps, 1530 sockets left
  bare, **0 violations on all six clauses**, 0 silent).
  **THE SEVEN PLAIN SHEETS ARE PROVED IMPOSSIBLE, NOT UNFOUND.** Where the painter's search gives up
  `--reach` lists EVERY pinned pairing the lattice admits, phase by phase — each vertex in turn left
  bare or married to a later neighbour, so every pairing is reached exactly once — and asks the
  question of all of them. A boot at three pixels of pitch is four or five sockets and a price of
  two needs a chain of six, so five of the six boots are refused by arithmetic; the male mage
  leggings and the female mage cuirass each fail on ONE pose, enumerated in full.
  **NINE CONTROLS.** RANDOM 85/340 (the null hypothesis), DEAD 0/390, **DOUBLED 0/330 knife=330 and
  BROKEN 0/340 knife=292 — the pair no previous axis could have run**, SWAPPED 0/317 (LAWFUL AND
  MISNAMED), OFFGRID 0/307, CLIPPED 0/340, FLAT silent — and **NUDGED 32/320, the axis's honest
  weakness**: a clasp re-married to a different neighbour is sometimes just another lawful plate of
  the same class, and the file says so.
  **TWO THINGS THE PANEL REJECTED BEFORE THIS SHIPPED.** (1) A pitch of TWO was rendered through
  `finish_array()` and looked at: a maximal pairing has to cover nearly every socket, so at that
  pitch the plate came out **more than half bright** — a field, which is camouflage, the legibility
  pass's finding reached this time through DENSITY rather than hue or geometry. Three pixels of
  pitch is ~15% ink. (2) The first draft let the painter leave clasps with nothing dark under them;
  RELIEF IS NOT DECORATION, so `shadowless()` is in the painter's cost function and clause LEGIBLE
  never has to catch it. Relief survives the finishing pass at 96–100%. Repaint only, silhouette
  untouched (0 dropped; chest strays 510/440 identical to the approved 72nd–76th batches — that is
  the finishing pass's shoulder plates), **sprite_qa 24/24 ALL PASS** (helmets `--y-min 2`,
  pants/boots `--y-max 63`). Palettes deliberately unrelated to the 73rd–76th: warrior **OXBLOOD AND
  PEWTER**, ranger **SLATE BLUE AND WHEAT**, mage **BRONZE AND ORCHID**.
  Staged in `_clasp_legendary_preview/`, `_clasp_legs_preview/`, `_clasp_boots_preview/`,
  `_claspdome_helmet_preview/`. Approval panels `_PREVIEW_clasp_*.png`; evidence
  `_ZOOM_clasp_pinned.png` (**the only panel in the project that has to show its plate's neighbours
  in BOTH directions** — as shipped, plus one clasp, minus one clasp, both unlawful and for opposite
  reasons), `_ZOOM_clasp_price.png` (every socket ringed, and the cheapest improvement drawn over
  the plate that may not make it; the ranger has no chain at all). Generator
  `scripts/gen_clasp_axis77.py`, panels `scripts/preview_axis77.py`.

- **76th net-new-geometry axis — GAUGE (the ornament is a set of TICKS standing on a RULE, and the
  law is that NO LENGTH THE RULE SPANS IS MISSING FROM IT), all 4 slots** (2026-08-10): the ground is
  an unbroken run of cloth two rows deep; the painter says WHERE to rule and nothing else, because
  **the ticks must reach BOTH ENDS of the run they stand on, so the span belongs to the silhouette
  and a painter cannot buy an easy law by measuring less than the garment offers.** A tick is a post
  two pixels tall with a hard shadow one down and one left, so a rule reads as a comb with irregular
  teeth; any two ticks measure the pixels between them.
  **THIS IS THE FIRST LAW THAT IS A COMPLETENESS.** Seventy-five axes are satisfied by the marks that
  are THERE; this one is about the marks that are NOT, so the reader's job is to go looking for a
  hole. **EXACT COMPLEMENT OF THE 68th SEMÉ, AND THERE IS NO THIRD THING TO SAY** — a set of marks on
  a line may be forbidden to REPEAT a displacement (a Sidon set, the 68th) or forbidden to MISS one
  (a complete ruler, this), and that exhausts the sentence.
  **CLASS IDENTITY IS AN EXCESS — how many more ticks the WHOLE PLATE carries than the fewest that
  could have done its job**: mage 0, ranger 1, warrior 2. **FIRST CLASS IDENTITY THAT NO SINGLE
  ORNAMENT ON THE PLATE CARRIES** — every comb on a warrior cuirass is usually exactly the comb a
  mage would have worn, and the whole difference is two ticks somewhere on the garment, so **the
  reader has to TOTAL THE PLATE.** It is also the first class that is a COMPARISON WITH SOMETHING
  NOBODY DREW, and the first output that cannot be computed from the picture alone. That it is a
  plate-wide total is also what holds the three classes at ONE DENSITY: the first draft spent the
  excess on every rule and the warrior came out a solid bright bar over a solid dark one, which is a
  rib and not a comb — the 75th's lichen finding arrived at through arithmetic instead of hue.
  **THE ACCEPTANCE TEST IS A NEW KIND — AN EXHAUSTION**, over every mark set SMALLER than the one in
  hand: 51,964 of them across the wardrobe, none of which exists, each with a length it cannot
  measure. **The first clause in the project whose subject is pictures that do not exist.** Six
  clauses: RULE, POST, GAUGE, EXCESS, LIVE, LEGIBLE. **15/24 sheets ALL PASS** (525 plates, 2053
  rules, 9618 ticks, **0 violations on all six clauses**, 0 silent).
  **THE MAGE'S ROBUSTNESS IS A THEOREM AND THE OTHER TWO CLASSES' IS AN EXPERIMENT.** A mage rule
  carries the proved minimum, so one tick fewer is fewer than the span can be measured with — proved
  in a line, never checked. `--controls dropped-why` takes every tick off every rule in turn: a
  dropped tick leaves the gauge standing **0% of the time for the mage, 8% for the ranger, 20% for
  the warrior**. **THE EXCESS IS A LICENCE TO LOSE ORNAMENT, and that is the licence being spent.**
  **NINE CONTROLS.** RANDOM 93/321 (the null hypothesis), DEAD 0/356 (live=356), DROPPED 67/321,
  SPARE 0/321, SWAPPED 0/309 (LAWFUL AND MISNAMED), OFFRULE 0/307, CLIPPED 0/321, FLAT silent —
  and **NUDGED 185/321, which is the axis's honest weakness and the file says so**: completeness is
  a property of a set of DISTANCES and not of a PLACE, so a tick moved one pixel is often just
  another lawful gauge. `--minima` prints why RANDOM scores as well as it does — on a span of 3 every
  mark set of the right size measures everything, on a span of 12 one in 28 does and on 21 one in
  692, and the wardrobe is mostly short runs.
  **THE NINE PLAIN SHEETS ARE PROVED IMPOSSIBLE, AND SO IS THE COVERAGE ITSELF.** A rule can absorb
  only so many ticks before it has four in a row and stops being a comb, so every pose has a CEILING
  on the excess it could ever wear (`--reach`); every plain pose is under it. The warrior sabaton's
  ceiling is not low but EMPTY — 35 poses of 35 with no run of four pixels two rows deep anywhere.
  **And all six ways of handing the three excesses to the three classes are tried: four give 15
  sheets and two give 14, so THE BATCH IS AT ITS OWN CEILING** — the first time an axis can say that
  about its own coverage. Relief survives the finishing pass at 96–100%. Repaint only, silhouette
  untouched (0 dropped; chest strays 510/440 identical to the approved 72nd–75th batches — that is
  the finishing pass's shoulder plates), **sprite_qa 24/24 ALL PASS** (helmets `--y-min 2`,
  pants/boots `--y-max 63`). Palettes deliberately unrelated to the 72nd–75th: warrior **WALNUT AND
  FROST**, ranger **DEEP TEAL AND AMBER**, mage **PLUM AND CHARTREUSE**.
  Staged in `_gauge_legendary_preview/`, `_gauge_legs_preview/`, `_gauge_boots_preview/`,
  `_gaugedome_helmet_preview/`. Approval panels `_PREVIEW_gauge_*.png`; evidence
  `_ZOOM_gauge_minima.png` (**the only panel in the project whose subject is pictures that do not
  exist** — every mark set smaller than the minimum for one real span, each with the length it cannot
  measure), `_ZOOM_gauge_hole.png` (the law, and what breaking it looks like),
  `_ZOOM_gauge_reading.png` (the reading done on the page). Generator `scripts/gen_gauge_axis76.py`,
  panels `scripts/preview_axis76.py`.

- **75th net-new-geometry axis — CONFLUENCE (the ornament is a set of LOADED PILES, and the law is
  that THE PICTURE THEY BECOME IS THE SAME PICTURE WHOEVER RUNS THEM — and that picture is nowhere
  on the plate), all 4 slots** (2026-08-10): the board is every cloth pixel of one lattice at a
  three-pixel pitch, and **the painter never says which of the nine it used**, because exactly one of
  them makes the picture parse at all — the plate is its own decoder, and the constraint the painter
  accepts in exchange is checked at the easel with the reader's own parser. A socket holds one, two
  or three chips, drawn as a cluster that grows in a fixed order — centre, then right, then down —
  so **a stud is one, a dash is two and an L is three**, each with a hard shadow one down and one
  left. Empty sockets carry no ink. **A pile of one is settled and a pile of two or three is LOADED,
  so the reader can see at a glance which sockets are about to go off.** The move is a TOPPLE: a
  loaded socket gives one chip to the socket on its right and one to the socket below, and chips
  aimed off the cloth are gone.
  **THIS IS THE FIRST INVARIANT THAT IS A UNIQUENESS OF OUTCOME RATHER THAN A CONSTANCY.**
  Seventy-four axes name something that DOES NOT MOVE, and the 74th ATTRITION is the extreme case:
  wreck the ornament and a number is still standing. This names something that MOVES and says the
  reader has no say in where it moves TO. **Exact complement of the 74th** — that one says *do what
  you like and this number will not change*, this one says *do what you like and you will end up in
  the same place*, and those are the only two things a reader with its hands on an artefact can be
  told.
  **IT IS ALSO THE FIRST LAW WHOSE SUBJECT IS A PICTURE THAT WAS NEVER PAINTED.** The plate ships a
  loaded arrangement; the arrangement the law is about is the one it settles into, and that one is
  not on the plate, not in the file, and was drawn by nobody. The 69th ANNEAL came nearest and from
  the other side — there the interior was the part nobody AUTHORED, but you could still see it.
  **THE HALT IS PROVED, NOT BUDGETED.** Weight every chip by how far it has left to travel (columns
  to its right plus rows below it, plus two); a topple takes two chips of weight w and puts back two
  of weight w−1, so the total falls by exactly two every time and cannot go negative. **The first
  termination argument in the project, and the reason this axis has no MAX_ITERS anywhere in it.**
  **CLASS IDENTITY IS A DEPTH — the greatest number of times any ONE socket has to topple**: mage 1,
  ranger 2, warrior 3. Not a count (67th), ceiling (68th), multipole order (69th), number of motions
  (70th), fraction of a move (71st), coalition size (72nd), precision (73rd) or number of
  obstructions (74th): **every previous class is a number of THINGS and this is the first that is a
  number of TIMES.** An output, and well defined only because the tally of topples is itself
  order-independent — which clause CONFLUENCE measures rather than assumes.
  **THE ACCEPTANCE TEST IS A RACE**: the same plate is settled under six deliberately hostile
  schedules (lowest-first, highest-first, fullest-first and three random orders) and all six must
  agree pixel for pixel AND socket for socket. Six clauses: BOARD, PILE, LIVE, HALT, CONFLUENCE,
  DEPTH. **19/24 sheets ALL PASS** (665 plates, 9424 chips, **0 violations on all six clauses**, 0
  silent), **7224 topples played over 3990 races and every race ended in the same place.**
  **THE FIVE THAT DO NOT ARE PROVED IMPOSSIBLE RATHER THAN UNFOUND, AND FOR THE PRICE OF ONE
  SETTLING.** The tally of topples is MONOTONE in the load, so filling every socket to the most its
  cloth can show and settling that once gives the deepest avalanche a garment could EVER carry —
  a genuine upper bound, not a sample. Both warrior sabatons have a ceiling of ZERO on all 35 poses
  (a sabaton is 30 pixels, which is four sockets, and a toppled chip has nowhere to land); the male
  chausses hit a ceiling of two on one pose where the warrior needs three; male mage boots one pose;
  male ranger boots six. `--ceiling` prints the theorem — where the 74th needed an enumeration over
  every subset of every parity, monotonicity hands this over in one settling a pose.
  **NINE CONTROLS.** RANDOM 98/382 (the null hypothesis — one plate in four is its class by
  accident, because there are only three classes). DEAD 0/346, SWAPPED 0/374, MALFORMED 0/375,
  CROWDED 0/407, OFFGRID 2/377, FLAT silent. **The pair that inverts the 74th: TOPPLED 301/377
  CLEAN and SPENT 0/377.** `--controls toppled-why` enumerates EVERY legal move of EVERY shipped
  plate — **1299 moves, and 1299 of them leave the destination exactly where it was; 221 of them
  spend the class, spread over 221 different plates.** So **WHERE A PLATE HAS A WEAK POINT IT HAS
  EXACTLY ONE**: 221 plates have a single stud that is the difference between a warrior and a
  ranger, 156 have none at all, and no plate in the wardrobe has two. Nothing in the 74th had a weak
  point of any kind — that is what an invariance buys and what a confluence does not.
  **TWO THINGS THE PANEL REJECTED BEFORE THIS SHIPPED.** (1) The warrior was OLIVE with PALE JADE
  chips and read as **LICHEN** — a green field with green marks is a mottle, which is camouflage,
  the same finding the 13px legibility pass has made about three geometries, arrived at this time
  through the HUE and not the geometry. Gunmetal with warm gold separates in hue as well as value.
  (2) The painter first MINIMISED the load and the mage came out carrying **two chips on the whole
  plate** — lawful, and not a pattern. **The class is an INTERVAL of loads, not a load**, so the
  painter spends that freedom on a constant density (FILL = 1 chip per socket) across all three
  classes: a mage plate and a warrior plate look like the same family and read as different laws.
  Repaint only, silhouette untouched (0 dropped; chest strays 510/440 identical to the approved
  72nd–74th batches — that is the finishing pass's shoulder plates), **sprite_qa 24/24 ALL PASS**
  (helmets `--y-min 2`, pants/boots `--y-max 63`), relief survives the finishing pass at 92–100%.
  Palettes deliberately unrelated to the 71st–74th: warrior **GUNMETAL AND PALE GOLD**, ranger
  **BLACK CHERRY AND MINT**, mage **SEA GREEN AND ICE PINK**.
  Staged in `_confluence_legendary_preview/`, `_confluence_legs_preview/`,
  `_confluence_boots_preview/`, `_confluencedome_helmet_preview/`. Approval panels
  `_PREVIEW_confluence_*.png`; evidence `_ZOOM_confluence_race.png` (**the only panel in the project
  that has to draw something the batch does not ship** — one cuirass half way through two opposite
  schedules, which are different pictures, and the end of each, which are the same picture),
  `_ZOOM_confluence_piles.png` (the reading done on the page), `_ZOOM_confluence_weak.png` (the one
  stud carrying the class). Generator `scripts/gen_confluence_axis75.py`, panels
  `scripts/preview_axis75.py`.

- **74th net-new-geometry axis — ATTRITION (the ornament is a BOARD OF SOCKETS, some of them filled,
  and the law is a number THAT NO AMOUNT OF DESTROYING THE ORNAMENT CAN CHANGE), all 4 slots**
  (2026-08-10): the board is every cloth pixel of one parity at a three-pixel pitch, so it belongs to
  the silhouette and not to the painter, who chooses only which of the nine parities. A filled socket
  is a bright PEG with a hard shadow one down and one left; **the empty sockets carry no ink and do
  not need to, because any one peg fixes the parity and the outline supplies every other socket for
  nothing.** The move is a JUMP — a peg hops its neighbour into the socket beyond **and the peg it
  jumped is taken off the plate.** The law is the plate's value, two sums in GF(4), one along each
  diagonal, **and no jump can move it** (the three sockets a jump touches are consecutive along a
  diagonal, and w² + w + 1 = 0).
  **THIS IS THE FIRST INVARIANT THAT SURVIVES THE DESTRUCTION OF THE ORNAMENT THAT CARRIES IT.**
  Seventy-three axes state a law about a picture: take a mark off the 68th and its Sidon set is
  broken, a bar off the 70th and its flex is a different number, a rod off the 72nd and the secret is
  gone, a beacon off the 73rd and the ground stops being addressable. Here **the reader is invited to
  take the ornament apart** until half or two thirds of it is gone and the number is exactly where it
  was. **The law is not a property of the plate; it is a property of every plate the plate can
  become**, and the picture the batch ships is only the one the painter happened to stop at.
  **EXACT COMPLEMENT OF THE 66th DOVETAIL** — that was an impossibility of ACTION whose acceptance
  test was satisfied by FAILING to take the artefact apart; this is an INDIFFERENCE to action whose
  acceptance test is satisfied by SUCCEEDING and finding the law standing in the rubble. Those are
  the only two things a reader with its hands on an artefact can find out, and this is the second.
  Also the third kind of orbit fact after the 63rd (a history somebody else produced) and the 71st (a
  game against an opponent): **a history the reader makes itself, and any history it likes.**
  **CLASS IDENTITY IS A NUMBER OF OBSTRUCTIONS** — a lone peg has both coordinates non-zero always,
  so a coordinate that vanishes is a door that has closed and the plate can never be played down to a
  single peg. Mage 0 (and it can therefore **name the ninth of the board its last peg must stand
  on**, before a move is played), ranger 1, warrior 2. Not a count (67th), ceiling (68th), multipole
  order (69th), number of motions (70th), fraction of a move (71st), coalition size (72nd) or
  precision (73rd): **every previous class counts something the plate HAS; this counts what it has
  LOST.** An output — two sums and a look at which are zero.
  **THE ACCEPTANCE TEST IS A NEW KIND — A DEMOLITION**: the reader rebuilds the board off the pegs and
  the outline, then plays the plate to pieces at random until no jump is left, recomputing the value
  after every one. Six clauses: BOARD, VALUE, DESTINY, STABLE, LIVE, LEGIBLE. **Clause LIVE is the
  first clause in the project that demands the artefact be DESTRUCTIBLE** — a still life keeps its
  value for the wrong reason, because nothing can happen to it. Clause DESTINY is verified by
  checking **every way the plate could end**: 130 mage plates name their last socket and 0 cannot, 0
  ranger and 0 warrior plates can name one and 235 confirm it the hard way over 2903 sockets.
  **20/24 sheets ALL PASS** (700 plates, 5194 pegs, **0 violations on all six clauses**, 0 silent),
  **2707 jumps played and 2707 pegs destroyed by the reader, and the value never moved once.** The
  four that do not are boots: a jump is seven pixels end to end at this pitch and a sabaton is not
  seven pixels of anything. Every subset of every one of the nine parities was enumerated pose by
  pose — warrior **30 of 34 PROVED IMPOSSIBLE**, ranger male 11 of 11, mage male 10 of 10 — so this
  is the garment and not the search, and **the sabaton is the one garment in the wardrobe with
  nothing left to lose.**
  **NINE CONTROLS**, scored on how many plates trip no clause at all: **JUMPED 335/335 — MEANT TO
  PASS, and the only control in seventy-four axes this project wants to get through**: a plate
  advanced by one legal move is a different picture with two fewer pegs and the same plate, so the
  orbit is run as a control. SWAPPED 0/368 (LAWFUL AND MISNAMED), DEAD 0/372, OFFGRID 0/365 (the
  value untouched — a stray is in neither sum — and refused anyway, because the reader can no longer
  say what the BOARD is; that is the price of not painting the empty sockets), CROWDED 0/416, FLAT
  silent. **THE THREE ILLEGAL ALTERATIONS LAND ON TOP OF EACH OTHER AT A QUARTER** — SLID 95/365,
  TOGGLED 84/363, RANDOM 76/365 — because the value has only sixteen states, and the file prints that
  rather than hiding it, **because it is the finding: every illegal alteration is worth exactly what
  starting over is worth, and the legal one costs nothing at all.**
  **THE PITCH IS THE MOST EXPENSIVE NUMBER IN THE FILE AND LEGIBILITY WON THE ARGUMENT.** At a
  two-pixel pitch the axis reaches 22/24 sheets — and the approval panel showed why that is the wrong
  answer: a regular lattice of bright pixels with a regular lattice of shadows beside them stops
  reading as studs and reads as **GINGHAM**, which is the camouflage the 13px legibility pass has
  already rejected three geometries for. At three the sockets are a ninth of the cloth, the pegs
  scatter, and the plate reads as a studded plate — at the cost of two sheets. Repaint only,
  silhouette untouched (0 dropped; chest strays 510/440 identical to the approved 72nd and 73rd
  batches — that is the finishing pass's shoulder plates), **sprite_qa 24/24 clean**, relief survives
  the finishing pass at 95–100%. Palettes deliberately unrelated to the 70th–73rd: warrior
  **SLATE-TEAL AND BONE**, ranger **PEAT AND OXIDE RED**, mage **NIGHT BLUE AND SILVER-LILAC**.
  Staged in `_attrition_legendary_preview/`, `_attrition_legs_preview/`, `_attrition_boots_preview/`,
  `_attritiondome_helmet_preview/`. Approval panels `_PREVIEW_attrition_*.png`; evidence
  `_ZOOM_attrition_orbit.png` (**the only panel in the project that shows one plate as four different
  pictures** — as shipped, after one jump, half way down, played out, with the same number under each),
  `_ZOOM_attrition_board.png` (the law stated), `_ZOOM_attrition_controls.png`.
  Generator `scripts/gen_attrition_axis74.py`, panels `scripts/preview_axis74.py`.

- **73rd net-new-geometry axis — SURVEY (the ornament is a set of BEACONS, and the law is that they
  give every pixel of the garment AN ADDRESS OF ITS OWN), all 4 slots** (2026-08-10): each beacon is
  a bright CORE pixel with its four orthogonal ARMS, drawn wherever the cloth has room for them —
  and **every arm that is missing is missing because there is no cloth to put it on**, which the
  reader checks against the silhouette and which is the whole of what makes the figure's centre
  nameable. The address of any pixel is its list of distances to the beacon centres, and the law is
  that **no two pixels of the piece share one.**
  **THIS IS THE FIRST INVARIANT WHOSE SUBJECT IS THE PIXELS THAT CARRY NO ORNAMENT.** Seventy-two
  axes state a law about the marks — the 68th's displacements, the 70th's bars, the 71st's stalks,
  the 72nd's rods — and in every one of them, delete the ornament and you have deleted the thing the
  law is about. Here **the ornament is the INSTRUMENT and the plain field is the SUBJECT**: every
  beacon pixel exists only to be measured FROM, and what the law constrains is the cloth between
  them, which carries no crest at all. The 69th ANNEAL came nearest and from the other side — there
  the interior was the part NOBODY AUTHORED; here it is the part the law is entirely about.
  **EXACT COMPLEMENT OF THE 68th SEMÉ, AND INDISTINGUISHABLE FROM IT BY EYE** — SEMÉ forbids the
  MARKS to repeat a displacement, SURVEY forbids the CLOTH to repeat an address, and there is no
  third half of a picture for a law to be about. **Exact complement of the 62nd DATUM** as well: one
  origin outside the piece fixing where the ornament goes, against several origins inside it fixing
  where every pixel of the PIECE is.
  **THE THIRD AND LAST WAY AN INVARIANT CAN DEPEND ON ITS READER.** 71st GAMBIT needed an OPPONENT
  (a mind), 72nd QUORUM needed a HOLDING (how much of the plate you have), 73rd SURVEY needs an
  **INSTRUMENT** — how well you can measure.
  **CLASS IDENTITY IS A PRECISION**, the coarsest rule under which the survey still stands, over a
  nested chain of four (EXACT `q` / HALF `⌊2√q⌋` / STEP `⌊√q⌋` / COARSE `⌊√q⌋//2`): warrior **STEP**
  (whole pixels), ranger **HALF**, mage **EXACT and nothing coarser**. Not a count (67th), ceiling
  (68th), multipole order (69th), number of motions (70th), fraction of a move (71st) or coalition
  size (72nd) — **a tolerance on somebody else's ruler**, and because the rules are nested the answer
  is unique and is an OUTPUT.
  **THE AMOUNT OF ORNAMENT IS DERIVED AND NOT CHOSEN, WHICH IS NEW.** Nobody tells this axis how many
  beacons to draw; the class fixes the precision, the precision and the body fix the count, and the
  painter then **TAKES ORNAMENT BACK** — every beacon it can do without is removed (clause TIGHT is
  satisfied at the easel, not demanded of the plate). Measured: **the blunter the instrument the more
  beacons the plate must carry** — mage 2, ranger 3, warrior 4–5.
  **THE CLASS THAT IS HARDEST TO DRAW IS THE EASIEST TO READ, WHICH INVERTS THE WHOLE PROJECT.** Every
  previous axis's expensive class is expensive on its own account; this warrior is expensive **on
  behalf of somebody else**, carrying the extra beacons so that a reader who cannot tell 4.9 pixels
  from 5.1 can still find out where he is standing. **THE COST OF THE PLATE IS THE READER'S COMFORT.**
  **THE ACCEPTANCE TEST IS A NEW KIND — A SURVEY**: the reader stands on every pixel of the piece in
  turn and writes down what it can see. Six clauses: GROUND, SURVEY, PRECISION, TIGHT, CLEAR,
  LEGIBLE. **Clause PRECISION is the first clause in the project that demands the ornament be
  INSUFFICIENT for something** — the survey must FAIL one rule coarser, or the plate is a different
  class wearing this one's colours; that clause is what makes the class an output rather than a
  label. Clause GROUND is checked against the silhouette, so **a beacon clipped by the edge of the
  cloth is lawful and a beacon pruned by a careless hand is not, and nobody has to tell the reader
  which is which.**
  **20/24 sheets ALL PASS** (700 plates, 2003 beacons, **0 violations on all six clauses**, 0 silent).
  The four that do not are three boots and one legs sheet, and they fail **in the order of the
  instrument**: warrior (STEP) sabatons 23/35 either gender and male chausses 33/35; ranger (HALF)
  male sabatons 32/35; mage (EXACT) carries every slot in every pose. An exhaustive search over every
  lawful placement rescues only **3 of the warrior's 12 missing sabaton poses**, so nine of them are
  a fact about the garment and not about the search — and that distinction was worth drawing, because
  the ranger's HOOD was reported PLAIN in all 35 poses by the first draft and an exhaustive search
  proved a lawful survey existed in all 35: **the failure was in the SEARCH.** Pure greed put its
  first beacon where it cut the most ties on its own and left nowhere legal for a third on a
  47-pixel hood; restarting the greed from each well-spread candidate in turn recovers every pose.
  **NINE CONTROLS**, scored on how many plates trip *no* clause at all: CLIPPED 0/407 (an arm pruned
  where the cloth would have taken it — the law untouched and caught anyway), ALIGNED 0/379, SWAPPED
  0/407 (LAWFUL AND MISNAMED), HUDDLED 13/416, SPARE 17/407, RANDOM 67/401 (**the number to beat —
  beaten 700 to nothing**), NUDGED 207/405, CROWDED 327/415, FLAT silent 407/407.
  **THE MAGE IS LEGIBLE BY ARITHMETIC AND NOT BY DESIGN, AND THE FILE SAYS SO.** Two pixels share an
  EXACT address under two beacons iff they are reflections in the line through the beacon centres,
  and reflection carries the integer lattice into itself only when that line is horizontal, vertical
  or at 45°. Counted (`--controls aligned-why`): **all 140 two-beacon mage plates lie along a
  direction the grid does NOT respect, 0 along one it does.** Control ALIGNED is that sentence
  switched off.
  **NUDGED IS WEAK AND THAT IS THE FINDING**: a survey survives a beacon moving one pixel where the
  72nd's shares provably could not. Geometry has slack; arithmetic has none.
  Repaint only, silhouette untouched (0 dropped; chest strays identical to the approved 72nd batch —
  that is the finishing pass's shoulder plates), **sprite_qa 24/24 clean**, relief survives the
  finishing pass at 93–100%. Palettes deliberately unrelated to the 69th–72nd: warrior **GRAPHITE AND
  SIGNAL ORANGE**, ranger **MULBERRY AND LINEN**, mage **AUBERGINE AND CITRON**.
  Staged in `_survey_legendary_preview/`, `_survey_legs_preview/`, `_survey_boots_preview/`,
  `_surveydome_helmet_preview/`. Approval panels `_PREVIEW_survey_*.png`; evidence
  `_ZOOM_survey_addresses.png` (the law stated), `_ZOOM_survey_ground.png` (**the only panel in 73
  axes whose subject is the pixels between the marks** — the plate at its own rule with no red
  anywhere, and one rule coarser with every collision painted), `_ZOOM_survey_controls.png`.
  Generator `scripts/gen_survey_axis73.py`, panels `scripts/preview_axis73.py`.

- **72nd net-new-geometry axis — QUORUM (the ornament is a SET OF SHARES OF A SECRET, and the law is
  that any k of them say it and any k-1 of them say nothing), all 4 slots** (2026-08-10): each rod is
  a straight run of exactly five pixels laid on the garment — level, upright or on either diagonal —
  and exactly one pixel of it is a BEAD. The bead's position along the rod, counted from the rod's
  top-left end, is the number that rod holds (0–4); the rods are ranked top to bottom, so the highest
  is share 1. The law is that the shares lie on a polynomial over GF(5) of degree exactly k−1 whose
  value at zero is **the secret, 3, on every plate of every class in the wardrobe** — and x = 0 is the
  one abscissa with no rod on it, so **the one thing every plate is about is the one place it
  deliberately leaves empty**.
  **THIS IS THE FIRST INVARIANT THAT TREATS TWO READERS DIFFERENTLY.** Seventy-one axes say the same
  thing to everybody who looks: the 67th's census, the 68th's refusal to repeat, the 69th's
  equilibrium, the 70th's flex, the 71st's value — two readers who can run the test get the same
  answer. This axis's answer depends on **how much of the plate the reader holds.** Hold k rods and
  the secret is yours; hold k−1 and four of the five secrets are still standing. The law is therefore
  half a statement about the pixels and half **a statement about somebody's ignorance**, and the
  second half is what is new.
  **THE INVARIANT IS A NON-EVENT.** The 66th DOVETAIL was an impossibility of ACTION (nothing can be
  carried away); the 67th COLOPHON an assertion, and so the first plate that could be FALSE; the 69th
  ANNEAL an absence of AUTHORSHIP. This is an impossibility of **KNOWLEDGE**, and it is the exact
  complement of the 67th: that was the first plate that could lie, this is **the first plate that can
  refuse to answer.**
  **THE ACCEPTANCE TEST IS A NEW KIND — AN INTERROGATION — AND HALF OF IT LOOKS FOR A NON-RESULT.**
  (a) it RECONSTRUCTS: every k-subset of the shares is interpolated at zero by Lagrange, all of them
  must agree, and what they agree on must be 3. (b) it INTERROGATES: every (k−1)-subset is held up
  against every polynomial of the right degree and must leave **four secrets standing, one plate
  apiece**. Clause IGNORANCE is **the first clause in the project that passes by FINDING something
  rather than by finding nothing wrong** — it fails if it counts three survivors, not if it counts a
  violation. Six clauses: QUORUM, IGNORANCE, DEGREE, DISTINCT, CLEAR, LEGIBLE.
  **THE LEAK IS EXACTLY ONE SECRET AND THE FILE DECLINES TO ROUND IT AWAY.** Shamir's scheme is
  perfectly secret when the leading coefficient may be anything; this axis insists the degree be
  exactly k−1, because a degenerate plate would be readable by fewer rods than its class admits. That
  insistence kills exactly one candidate secret, so the axis **buys clause DEGREE for log2(5/4) of a
  bit** and says so.
  **CLASS IDENTITY IS THE SIZE OF A COALITION** — warrior k=4, ranger k=3, mage k=2. Not a count
  (67th), a ceiling (68th), a multipole order (69th), a number of motions (70th) or a fraction of a
  move (71st): **a number of parties**, and the first class that is a property of the plate's READERS.
  Like the 71st's it cannot be seen; unlike the 71st's it can be LEARNED by anyone holding enough of
  the plate, so **the plate carries two grades of knowledge at once** — a public threshold and a
  private secret.
  **THE MINIMUM IS NOT DERIVED FROM THE CLASS, IT IS THE CLASS**, which inverts every preceding axis's
  arithmetic — and the sabaton decides the batch. **20/24 sheets ALL PASS** (700 plates, 2720 shares,
  0 violations on all six clauses); the four that do not are all boots and they fail **in the order of
  the quorum**: mage (k=2) female 35/35 and male 30/35, ranger (k=3) female 35/35 and male 10/35,
  warrior (k=4) 0/35 either way. Chest, legs and helmet carry every class in every pose.
  **NINE CONTROLS**, scored on how many plates trip *no* clause at all: NUDGED 0/40, SHORT 0/43,
  SWAPPED 0/39, FLAT 0/40, RANDOM 3/40 (the number to beat — beaten 700 to nothing), CYCLED 14/40,
  RAMP 15/40, CROWDED 13/43, RESORTED 33/40.
  **THE TWO RANK CONTROLS FOUND TWO THEOREMS** (`--controls resorted-why`): (i) reversing four rods
  sends x → 5−x, which in GF(5) is −x, and f(−x) has the same constant term — measured, the secret is
  unchanged on 35/35 four-rod plates, so **a full plate may be read from either end of its rank**;
  (ii) every power x^j for j ≤ 3 sums to zero over GF(5), so a warrior (k = n = 4) has secret −(sum of
  its beads) — and a sum has no order, so **all 24 permutations of a warrior's rods reconstruct**
  (35/35, against 0/35 for mage and ranger). **The warrior's plate is therefore not a threshold scheme
  but a CHECKSUM** whose law reads "the four beads sum to two". Clause IGNORANCE is untouched; what
  the warrior has spent is its ORDER. Nobody designed that asymmetry and it is reported, not buried.
  Repaint only, silhouette untouched (0 dropped; chest strays identical to the approved 71st batch —
  that is the finishing pass's shoulder plates), sprite_qa 24/24 clean, relief survives the finishing
  pass at 99–100%. Palettes deliberately unrelated to the 68th–71st: warrior INDIGO AND MOONWHITE,
  ranger UMBER AND WHEAT, mage JADE AND SEAFOAM.
  Staged in `_quorum_legendary_preview/`, `_quorum_legs_preview/`, `_quorum_boots_preview/`,
  `_quorumdome_helmet_preview/`. Approval panels `_PREVIEW_quorum_*.png`; evidence
  `_ZOOM_quorum_shares.png` (the half that can be shown), `_ZOOM_quorum_ignorance.png` (the half that
  cannot, so it is counted), `_ZOOM_quorum_controls.png`, `_ZOOM_quorum_visor.png`.
  Generator `scripts/gen_quorum_axis72.py`, panels `scripts/preview_axis72.py`.

- **71st net-new-geometry axis — GAMBIT (the ornament is a POSITION IN A GAME, and the law is what
  the position is WORTH when both sides play perfectly), all 4 slots** (2026-08-10): each stalk is a
  chain of pixels rooted on the piece's own silhouette and growing inward, every pixel of it one
  EDGE, and every edge painted in one of two stops — the brightest is LEFT's claim, the next is
  RIGHT's, and each carries a dark witness. The game is Blue–Red Hackenbush: a player may cut an
  edge of their own colour, everything no longer joined to the GROUND falls off, and the player with
  no move loses. The law is that **the whole plate is worth exactly v — nothing (warrior), half a
  move (ranger), a quarter (mage)**.
  **THIS IS THE FIRST INVARIANT THAT REQUIRES AN OPPONENT.** Seventy axes state something the plate
  alone settles: most of them a FACT (no piece can be carried away, 66th; the registers count
  themselves, 67th; no displacement repeats, 68th; every free pixel is the mean of its neighbours,
  69th), one of them a BEHAVIOUR (push it and count the ways it gives, 70th). Every one of those can
  be asked by an inspector working alone. **This one cannot.** Its answer is the end of an argument
  between two parties with opposite interests, each assumed to play as well as it is possible to
  play. There is nobody on the plate and no argument on the plate. **THE PLATE IS NOT DESCRIBED, AND
  IT IS NOT LOADED — IT IS CONTESTED.**
  **IT COMPLETES A TRIPLE WITH THE 66th AND THE 70th.** 66th DOVETAIL: can a part be taken away? —
  the adversary is a HAND. 70th TRUSS: what would it do if pushed? — the adversary is a FORCE. 71st
  GAMBIT: what if somebody WANTED it gone? — **the adversary is a MIND that has read the plate as
  carefully as the reader has and wants the opposite thing from it.**
  **THE ACCEPTANCE TEST IS A NEW KIND — A SOLUTION — AND IT IS DONE TWICE BY TWO METHODS THAT SHARE
  NOTHING.** (a) it RECKONS: Berlekamp's rule turns each word into a number and the numbers add,
  because disjoint games add. (b) it PLAYS: it builds the real game tree and solves it by minimax,
  with no arithmetic in it anywhere. **Clause PLAYOUT is the first clause in the project that could
  contradict another clause of its own axis** — everything else here is checked once, this is
  checked by a formula and then again by an exhaustive argument. Clauses: (1) **VALUE** the sum is
  exactly v, so **the class is an OUTPUT**; (2) **PLAYOUT** the minimax outcome agrees with the sign
  of that number — v=0 must mean WHOEVER MOVES FIRST LOSES; (3) **CONTEST** every stalk holds an
  edge of each colour; (4) **GROUNDED** every stalk is a simple path with **exactly one** end on the
  silhouette (two ground ends and the word can be read backwards, which is a different number; no
  ground end and there is no word); (5) **CLEAR** stalks stand apart and account for every crest
  pixel; (6) **LEGIBLE** a witness beside every crest pixel, no 2×2 crest block. **AXIS ALL PASS:
  21 of 24 sheets, 735 plates, 0 violations on all six clauses, and 0 plates over the playout cap —
  every plate's game was actually solved, and the formula and the search never once disagreed.**
  **IT IS THE 60th CADENCE TURNED INSIDE OUT.** The 60th admits exactly one word of each length (the
  Fibonacci prefix) and forbids every other; **this admits EVERY word and constrains only what they
  come to when added up**. One axis forbids all but one arrangement, the other permits every
  arrangement and constrains only the total, and there is no third way a sequence can carry a law.
  **CLASS IDENTITY IS A FRACTION OF A MOVE, AND IT IS THE FIRST CLASS THAT CANNOT BE SEEN** —
  warrior 0 (a drawn game), ranger 1/2, mage 1/4. Not a count (67th), not a ceiling (68th), not the
  order of a multipole (69th), not a number of motions (70th), and unlike all of those **it cannot
  be counted by eye**: two plates one edge apart are two different classes and look alike. The axis
  is honest about that rather than pretending otherwise.
  **THE MINIMA ARE THEOREMS AND THEY RUN THE OPPOSITE WAY FROM THE 68th's AND THE 70th's.** No stalk
  is ever worth nothing (|v| ≥ m − (1 − 2^−(L−m)) > 0), so **a drawn game needs TWO stalks** while a
  ranger is "+-" and a mage is "+--"; and **the class's DENOMINATOR is a lower bound on its longest
  stalk** (a quarter is the third halving, so it needs three edges). Here the BALANCED class is the
  expensive one, not the freest. **The boots fail in exactly that predicted order:** ranger contested
  in all 42 poses, male mage short of three edges in 6 poses, warrior unable to fit two stalks in 17
  — warrior m/f and mage m are **PLAIN and reported**, with the theorem beside them.
  **THE EIGHT CONTROLS — six false, one lawful and misnamed, one ABSENT.** **FRINGE** (striped
  "+-+-", the picture a person draws) VALUE 47/47 — **the only control that looks exactly like the
  axis and is wrong every time**. **RANDOM** 45/47, so 2 in 47 come right by luck and that is the
  number to beat. **MONO** VALUE 39 / CONTEST 43, **and 4 plates the reader cannot see at all** —
  one stalk in one colour shows three stops instead of four and is a STRIPE, not a position.
  **FLOATING** GROUNDED 37/37: the same stalks grown from an interior pixel, and in Hackenbush
  anything not joined to the ground is already gone, so however much ink is on the plate **THE
  POSITION IS EMPTY — the only control in 71 axes that is not wrong but ABSENT**. **BRANCHED** (the
  49th DENDRITE's shape) GROUNDED 41/41, with 7 reported undrawable because a two-pixel stalk has no
  middle to branch and a control that has turned back into the axis is not a control. **REVERSED**
  VALUE 42/47 — every pixel keeps its colour, every stalk its length and place, **only the order
  turns round**, and its 5 misses are a theorem rather than noise: plates whose word multiset is
  closed under reversal, which is a warrior's most natural route to zero (`--controls reversed-why`
  lists every one). **SWAPPED** LAWFUL AND MISNAMED. **TRUNCATED** (one edge rubbed off one stalk)
  VALUE 40/40 — **cannot miss, by theorem**; the first draft rubbed an edge off EVERY stalk and
  scored 20 of 40, because losing +1/4 here and −1/4 there leaves the plate worth what it was:
  **MORE DAMAGE IS EASIER TO SURVIVE THAN LESS.**
  **THE RENDER-PAID LESSONS, THREE.** (a) **THE LENGTH IS PART OF THE SOLVE.** Two stalks two pixels
  long can only be ±1/2 apiece: they can make a drawn game and they cannot make a quarter of a move.
  Growing every stalk to its maximum and then looking for colours could not draw a mage on anything
  narrower than a torso. (b) **CUTTING A STALK BACK CAN LAND ITS TIP ON THE SILHOUETTE**, and a
  stalk with two ground ends is worth two different numbers depending which end you start from —
  eight poses of the warrior's cuirass and twelve of the female's were lost to this, and the symptom
  was a plate the reader simply refused to read. Those lengths are no longer offered to the solver.
  (c) **THE RETRY MUST BE GEOMETRIC BEFORE IT IS CHROMATIC** — the solve is exhaustive, so re-hashing
  the words on the same stalks is one attempt done four times; rotating which anchors are used is a
  different set of stalks and therefore a different question.
  **THE POSITION IS THE WHOLE PLATE, NOT THE PART** — the exact opposite of the 70th, where a
  framework is a local object and two legs are two structures. Hackenbush positions ADD over their
  components, so the balance is struck across the whole garment at once. Repaint only, silhouette
  untouched, QA-safe by construction; sleep frames plain. **Twenty-seventh generator to call
  `sprite_finish.finish_array` in-line.** Survival through the finishing pass: chest 99%, legs 100%,
  boots 100%, helmet 96%.
  Files: `scripts/gen_gambit_axis71.py`, `scripts/preview_axis71.py`; staged in
  `_gambit_legendary_preview/`, `_gambit_legs_preview/`, `_gambit_boots_preview/`,
  `_gambitdome_helmet_preview/` (24 sheets, **QA 24/24 PASS**, 0 dropped / strays identical to the
  67th–70th chests, which is the finishing pass's own pauldrons).
  Previews: `_PREVIEW_gambit_legendary.png`, `_PREVIEW_gambit_legs.png`, `_PREVIEW_gambit_boots.png`,
  `_PREVIEW_gambitdome_helmet.png`, `_ZOOM_gambit_words.png` (ground ends ringed gold, free ends
  blue, with each word, its value and the minimax playout printed beside it),
  `_ZOOM_gambit_controls.png` (one cuirass: shipped, REVERSED, MONO, FLOATING).
  ⚠️ **On approval:** register as L72 in the LOOT_TABLE alongside the 69th and 70th.

- **70th net-new-geometry axis — TRUSS (the ornament is a BAR FRAMEWORK, and the law is about what
  it would do IF YOU PUSHED IT), all 4 slots** (2026-08-10): joints are pixels of the part's own
  mask, bars are straight runs of crest between two joints each with its own dark witness, and the
  law is that **the rigidity matrix has a kernel of exactly 3 + k** — three of those motions are the
  plane's own two translations and rotation, and the rest are the class.
  **THIS IS THE FIRST INVARIANT THAT IS A BEHAVIOUR RATHER THAN A FACT.** All sixty-nine axes before
  it state something TRUE OF THE PIXELS AS THEY LIE — a statistic holds among the shards (46th), a
  wire is connected (54th), three hoops stand in 3:2:1 (61st), the studs exclusive-or to zero (64th),
  no piece can be carried away (66th), the registers count themselves (67th), no displacement repeats
  (68th), every free pixel is the mean of its neighbours (69th) — and every one of those can be
  checked by an inspector forbidden to touch the plate. **This one cannot.** The claim is not about
  the ornament's positions but about its VELOCITIES: hold the bars rigid, let the joints move, and
  ask how many ways the figure can be set going. Nothing on the plate is moving and nothing ever
  moves. **THE PLATE IS NOT DESCRIBED, IT IS LOADED.**
  **THE PAIR WITH THE 66th, ITS EXACT COMPLEMENT.** The 66th DOVETAIL's law is that NO PART CAN BE
  REMOVED and its ornament is a spanning tree; here NO PART CAN MOVE, and the 66th's own spanning
  tree is control TREE, which reads a DOF of 1, 2 or 3 where the class wants 0, 1 or 2.
  **CONNECTED IS NOT RIGID, and control TREE is that difference stated as an integer.**
  **THE ACCEPTANCE TEST IS A NEW KIND: A FLEX.** The reader recovers the joints (the brightest stop)
  and the bars (pairs of joints joined by an unbroken crest run) off the pixels, writes down the
  RIGIDITY MATRIX and takes its RANK. **The first acceptance test in the project that is linear
  algebra on the plate's own coordinates, and the first whose verdict changes if the ornament is
  drawn identically but PLACED differently.** Clauses: (1) **FLEX** dim ker R = 3+k, so **the class
  is an OUTPUT**; (2) **TIGHT** rank R = |E| — every bar is load-bearing, the 66th's question
  answered with "nothing here is only decoration"; (3) **SPARSE** the Laman count over every subset
  (no s joints span more than 2s−3 bars), coordinate-free; (4) **CLOSED** degree ≥ 2 everywhere and
  connected — a bar with a free end is a whisker; (5) **CLEAR** the recovered bars have pairwise
  disjoint interiors and account for every crest pixel, so **a wrong reading fails a clause of its
  own and the reader does not have to be trusted**; (6) **LEGIBLE** a witness beside every crest
  pixel, no 2×2 crest block away from a joint. **AXIS ALL PASS: 19 of 24 sheets, 718 plates
  inspected, 0 violations on all six clauses.**
  **THE CONSTRUCTION IS A THEOREM, NOT A SEARCH.** A SEED CYCLE of 3+k joints, then every further
  joint added with EXACTLY TWO BARS to joints already placed — a Henneberg type-I extension, which
  changes neither independence nor the number of motions. So |E| = 2n−3−k and DOF = k for every n,
  and **the ornament GROWS WITHOUT EVER CHANGING HOW FREE IT IS**: a torso with ten bars is the same
  object as a pauldron with three, because the freedom is in the SEED and every later bar buys a
  joint rather than stiffness. (The LAW is a theorem; the LEGIBILITY is a search — the joint count
  comes down a step at a time until the picture can be read back, which is the 69th's "the body
  disposes" in another register.)
  **CLASS IDENTITY IS THE FREEDOM OF THE SEED** — warrior a **TRIANGLE** (k=0, cannot move), ranger a
  **QUADRILATERAL** (k=1, lozenges one way), mage a **PENTAGON** (k=2, lozenges two) — not an integer
  written on the plate (67th), not a ceiling (68th), not the order of a multipole (69th), but **THE
  NUMBER OF WAYS THE FIGURE COULD FALL DOWN**, and countable by eye.
  **TWO MINIMA, BOTH THEOREMS.** (a) degree ≥ 2 with k motions forces n ≥ 3+k, so **the minimum SIZE
  depends on the class** and, as in the 68th, the FREEST class is the EXPENSIVE one. (b) A framework
  needs a CYCLE and a cycle needs the part to ENCLOSE something — **a sabaton in most poses is a
  ribbon two pixels wide and a ribbon has no interior**, so it is not a matter of size but of WIDTH.
  Five of six boots sheets are therefore a plain recolor and are reported as such; the female
  ranger's boot is the one wide enough in all forty-two poses and it is trussed.
  **THE EIGHT CONTROLS — six false, one lawful and misnamed, one DEAD.** **TREE** (= the 66th) 40
  drawable, FLEX 41 / CLOSED 41 and nothing else. **GRID** (= the 14th LATTICE) FLEX 39, DOFs read
  2/3/5/7/8/9 — **it looks the stiffest and it is the floppiest thing in the file**. **TRELLIS**
  (= the 20th) is genuinely rigid and fails anyway (FLEX 26, TIGHT 3, CLOSED 36, CLEAR 13) because it
  is rigid many times over — **the two nearest visual neighbours in the project fail for exactly
  OPPOSITE reasons**. **COLLINEAR** is **DEAD as a picture** (collinear bars lie on top of one
  another, 0 of 48 drawable) and is therefore MEASURED instead: keep each shipped framework's graph
  exactly and slide its joints onto the part's widest row — **355 of 355 gain motions**, which is why
  clause FLEX is a rank at real coordinates and not a Laman count. **DENSE** 3 of 48 drawable, all
  false. **BRACED** 24 of 48 drawable, all 24 false on FLEX — an extra bar that can be drawn on a
  hinged piece always REMOVES a hinge. **WHISKER** FLEX 41 / CLOSED 41: a whisker adds exactly one
  motion, so without CLOSED **a warrior with one whisker IS a ranger**. **SWAPPED** is LAWFUL AND
  MISNAMED — FLEX names the class it actually is.
  **THE RENDER-PAID LESSONS, FOUR.** (a) **BRESENHAM IS NOT SYMMETRIC IN ITS ENDPOINTS** — the
  painter walks a bar from the joint it placed first and the reader from the joint it found first,
  and on any half-pixel slope the two runs differ; an un-canonicalised reader lost one bar in five,
  silently, as a degree-one joint. (b) **A 2×2 OF CREST AT A JOINT IS NOT A BLOT, IT IS A JOINT** —
  refusing every 2×2 cost 174 of the first 200 warrior torsos their ornament, because two Bresenham
  staircases arriving from different quarters put four crest pixels in a square whether you like it
  or not. (c) **THE SEED IS WALKED ROUND, NOT SCATTERED** — ordering candidates by "farthest from
  everything chosen" builds a self-crossing tour whose closing bar treads on its opening one; taking
  the candidate one angular step of 2π/m ahead produces a simple polygon, and it is what let the
  ranger's forty-five-pixel hat carry a quadrilateral at all. (d) **A CONTROL MUST STAY A CONTROL** —
  the legibility retry drops a joint at a time and eventually lands on the lawful seed, so DENSE and
  BRACED silently turned into the axis and scored zero violations; a retry that has abolished the
  thing being tested is refused and the plate is reported undrawable. (e) **A DEGENERACY HAS TO BE
  EXACT** — sliding COLLINEAR's joints onto the principal axis and rounding to pixels leaves them
  NEAR a line, integer rounding restores general position, and the control scored 0 of 355.
  Every part is trussed separately (a framework is a local object; two legs are two structures).
  Repaint only, silhouette untouched, QA-safe by construction; sleep frames plain. **Twenty-sixth
  generator to call `sprite_finish.finish_array` in-line.** Survival through the finishing pass:
  chest 98%.
  Files: `scripts/gen_truss_axis70.py`, `scripts/preview_axis70.py`; staged in
  `_truss_legendary_preview/`, `_truss_legs_preview/`, `_truss_boots_preview/`,
  `_trussdome_helmet_preview/` (24 sheets, **QA 24/24 ALL PASS**, 0 dropped / strays identical to the
  67th–69th chests, which is the finishing pass's own pauldrons).
  Previews: `_PREVIEW_truss_legendary.png`, `_PREVIEW_truss_legs.png`, `_PREVIEW_truss_boots.png`,
  `_PREVIEW_trussdome_helmet.png`, `_ZOOM_truss_seed.png` (the seed cycle traced in gold, the
  Henneberg joints ringed in blue), `_ZOOM_truss_controls.png` (one cuirass, four frameworks).
  ⚠️ **On approval:** register as L71 in the LOOT_TABLE alongside the 68th and 69th.

- **69th net-new-geometry axis — ANNEAL (the plate is pinned at a few points of its own outline and
  then LET GO, and the ornament is where it stopped), all 4 slots** (2026-08-10): n pixels of a
  part's outline — the farthest pixel in each of n equal directions about the part's own centroid —
  are HELD at fixed potentials, every other pixel is free, and the plate is the unique state in
  which **every pixel that is not a pole is the mean of its neighbours**. The ribs are the level
  lines of that state: one pixel of crest with a dark witness across the level it stands on.
  **THIS IS THE FIRST INVARIANT THAT IS AN EQUILIBRIUM.** All sixty-eight axes before it are
  CONSTRUCTIONS — somebody decided where the ornament went, if not pixel by pixel then rule by rule,
  and the rule is ours: a pitch (11th), a lattice (13th), a hung chain (57th), a growth rule applied
  row after row (65th), a spanning tree of keys (66th), a self-describing word (67th), a scatter
  with no repeated relation (68th). Here **nothing in the interior is authored and there is nothing
  to author**. THE PLATE IS NOT DRAWN, IT IS SOLVED.
  **THE PAIR WITH THE 65th, ITS EXACT COMPLEMENT.** The 65th CASCADE's vertical direction is a
  HISTORY and the plate remembers exactly how it was made. This one has no history and cannot be
  given one — clause AMNESIA re-relaxes each plate from six different starts (zero, +1, −1, the
  47th's distance transform, two seeded random interiors) and all six arrive at the same picture,
  **90 of 90**. The 65th is a plate with a direction of time in it; this is a plate in which time
  has run out.
  **THE ACCEPTANCE TEST IS A NEW KIND: A RECOMPUTATION.** Every reader before this one was handed a
  picture and asked a question about it. This one is handed the MASK, told nothing — not the class,
  not the palette, not the poles, not the band count — **draws the ornament itself** and demands the
  plate pixel for pixel. **The first acceptance test in sixty-nine whose expected value is not a
  predicate but a picture, and the first that could have produced the item it is inspecting.**
  Clauses: (1) **RECOMPUTE** exactly one n of {2,3,4} may reproduce the plate, so **the class is an
  OUTPUT** (0 violations, 0 plates admitted two n); (2) **MEAN-VALUE** no free pixel is a strict
  local extremum — the discrete maximum principle, exact, and a clause an eye can also check (0
  violations, worst mean-value residual 5.6e-16, reported); (3) **AMNESIA** 0 of 90; (4)
  **DEPENDENCE** raise one pole by one and **EVERY free pixel must move** — bit-for-bit, no
  tolerance — 0 of 65 053 deaf over 200 parts, with 557 one-neighbour **hangnails** excluded and
  counted (a pixel with a single neighbour IS that neighbour); (5) **LEGIBLE** 0 blots, 0 ribs
  without a witness; (6) **POLES** 838 of 838 plates name their own class, 2 mute plates reported.
  **AXIS ALL PASS on 840 plates.**
  **THE EIGHT CONTROLS — six false, one lawful and misnamed, one DEAD.** **DISTANCE** (= the 47th
  MOKUME drawn by this axis's own painter) 14 068 violations, **18 of 24 sheets cannot be drawn at
  all**, 683 maximum-principle violations because the distance transform has a RIDGE of local maxima
  down every limb, and **13 175 of 13 175 free pixels deaf on DEPENDENCE** — the distinctness
  argument stated as a number instead of as an opinion; its ribs are CLOSED and hug the outline,
  this axis's are OPEN and run rim to rim. **HALFWAY** (25 sweeps instead of equilibrium) 1 685 —
  **INVISIBLE at 13px and false**, and false in the only way this axis can be: a plate that was
  still moving. **LINEAR** (a flat ramp, which IS harmonic and passes the maximum principle) 4 724 —
  and it is where this axis **degenerates into the 11th FLUTING**, so the amount by which an annealed
  plate is not a reed is the amount by which the body is not a box. **PINNED** (one interior source)
  905 — **and it scored ZERO until the reader stopped being handed the painter's list of what was
  held**; a reader that is told which pixels are poles will forgive any pin you like. **NOISE** 10
  249. **GROUNDED** (Dirichlet rim instead of insulated) 291 and 12 of 24 sheets undrawable — **an
  insulated rim is why a rib can END on the silhouette**, and a rib that cannot end on the
  silhouette is a closed curve, and a closed curve is the 47th again. **SWAPPED** (another class's
  n) **LAWFUL AND MISNAMED — it fails nothing and clause RECOMPUTE names the class it actually is**,
  which is the finding: n is not a decoration on the law, it is the whole of what a class is here.
  **ONEPOLE** is **DEAD** — the equilibrium of a body with one held pixel and an insulated rim is
  the CONSTANT field, and a constant field has no contour anywhere: not one plate in twenty-four
  sheets has a single rib. **The axis's minimum is TWO and it is a theorem — a potential needs a
  DIFFERENCE, you cannot make a picture out of one number** — and unlike the 66th (a dovetail is
  four pixels across; one could imagine a smaller dovetail) nothing can be imagined smaller.
  **CLASS IDENTITY IS THE ORDER OF A MULTIPOLE** — warrior **n=2** DIPOLE, ranger **n=3** TRIPOLE,
  mage **n=4** QUADRUPOLE, pole values cos(2πj·⌊n/2⌋/n) so they sum to zero for every n and no class
  is secretly a brighter version of another. **And it is VISIBLE, which is rare**: a dipole's ribs
  cross the plate, a tripole's stack, a quadrupole's stand on end — nobody has to be told which
  class is which.
  **THE RENDER-PAID LESSONS, SIX.** (a) **THE LEVELS ARE QUANTILES, NOT A LADDER.** Cutting the
  field at equal VALUES left the middle of every torso blank — an insulated field moves fast at its
  poles and hardly at all in the interior. Equal-AREA bands put the ribs where the ornament is.
  (b) **THERE IS NO PITCH IN THIS AXIS AND THE BAND COUNT IS AN OUTPUT.** nbands() proposes and the
  body disposes: the count comes down a step at a time until no pixel is on the high side of one
  level and the low side of another (a rib with no field to stand on) and no four crest pixels make
  a 2×2 blot. (c) **THE FIELD IS FLATTENED BEFORE THE RIBS GO ON** — the source sheet's inherited
  highlights are the same lightest stop the ribs are painted in, and a reader told nothing cannot
  tell an inherited highlight from a rib. Every tone on an annealed plate is put there by the
  equilibrium. (d) **A POLE IS THE FARTHEST PIXEL IN ITS DIRECTION THAT IS NOT ALREADY HELD** — a
  chausse comes to a point at the hip, so its topmost pixel and its rightmost pixel ARE THE SAME
  PIXEL, and a first draft that simply refused the collision lost twelve poses of the mage's legs
  and twenty-nine of the mage's sabatons. (e) **THE READER MUST NOT SEE THE PAINTER'S FIXTURES** —
  see control PINNED. (f) **THE STOPS ARE COUNTED, NOT MEASURED**: one tone is a plate with nothing
  on it, TWO tones can only be dark and crest (a rib and its witness always come together, so on a
  sabaton the ornament uses every pixel there is and no field is left over), three are dark/field/
  crest. Taking the ground to be "whatever there is most of" is true of a torso and false of a boot.
  **DISTINCTNESS.** 47th MOKUME is the nearest neighbour in the project and it is control DISTANCE —
  closed vs open contours, local vs global, a ridge of local maxima vs a field with none, all three
  measured. 51st FLOWGRAIN is also a field and it is AUTHORED: change the 51st's rim and its
  interior does not move. 11th FLUTING / 43rd GADROON are control LINEAR. 55th STRATA / 40th DENTIL
  have a pitch; this has none.
  Every part is annealed separately (a potential is a local object; two legs are two bodies), which
  is the exact opposite of the 67th, whose census had to be of the whole garment. Repaint only,
  silhouette untouched, QA-safe by construction; sleep frames plain. **Twenty-fifth generator to
  call `sprite_finish.finish_array` in-line.**
  Files: `scripts/gen_anneal_axis69.py`, `scripts/preview_axis69.py`; staged in
  `_anneal_legendary_preview/`, `_anneal_legs_preview/`, `_anneal_boots_preview/`,
  `_annealdome_helmet_preview/` (24 sheets, **QA 24/24 ALL PASS**, 0 dropped / strays identical to
  the 67th and 68th chests, which is the finishing pass's own pauldrons). Survival through the
  finishing pass: chest 97%, legs 100%, boots 100%, helmet 94%.
  Previews: `_PREVIEW_anneal_legendary.png`, `_PREVIEW_anneal_legs.png`,
  `_PREVIEW_anneal_boots.png`, `_PREVIEW_annealdome_helmet.png`, `_ZOOM_anneal_field.png`
  (the poles ringed — the entire input), `_ZOOM_anneal_controls.png` (one cuirass, four fields).
  ⚠️ **On approval:** register as L70 in the LOOT_TABLE alongside the 68th.

- **68th net-new-geometry axis — SEMÉ (the plate is POWDERED with studs and the law is about the
  VECTORS BETWEEN THEM), all 4 slots** (2026-08-10, generated earlier the same day and previously
  undocumented — the sheets were staged and QA-clean but never written up): a stud is one pixel of
  crest with a dark witness beside it; the relation is the DISPLACEMENT between two studs, a vector
  and not a distance; and the law is that **no displacement occurs more than LAMBDA times on the
  plate, and some displacement occurs exactly LAMBDA times**.
  **THE FIRST AXIS WHOSE LAW IS A REFUSAL TO REPEAT.** An ornament is definitionally a thing that
  repeats, and sixty-seven axes are built out of repetition — even the aperiodic 46th repeats a
  STATISTIC. At LAMBDA=1 the plate contains no repeated configuration of any kind, at any scale, in
  any direction: **an ornament whose entire content is that it is not an ornament.**
  **THE PAIR WITH THE 13th, WHICH IS ITS EXACT NEGATION.** The 13th STUDWORK's every neighbouring
  displacement is THE SAME; this one's is never the same; **the two plates cannot be told apart by
  looking**, and control GRID is the 13th rendered by this axis's own painter to prove it.
  **ACCEPTANCE — AN AUTOCORRELATION, THEN A RECONSTRUCTION.** The reader forms the multiset of all
  C(k,2) displacements and **throws the positions away**; everything after that is done on a bag of
  arrows with no plate attached. Clauses RECOVERY / SPECTRUM / TIGHT / **REBUILD** (handed only the
  arrows, rebuild every point set that could have produced them — the answer must be the plate and
  its point reflection and nothing else; a third solution is a HOMOMETRIC TWIN and is reported) /
  **BLIND** (no origin, no pitch, no phase, no up: slide it, turn it, the law is untouched) /
  LEGIBLE. **The first reader in sixty-eight whose input is not a picture.**
  **CONTROLS:** GRID (= the 13th), RANDOM (chance satisfies the strict class 35.7% of the time, so
  **one warrior plate is worth half a bit and THE EVIDENCE IS THE WARDROBE** — 280 lawful warrior
  plates against 0.357^280 ≈ 10⁻¹²⁵), LOOSE, TIGHTLESS (vacuous for the warrior, and the file says
  so rather than pretending the clause does the same work in all three classes), SLIDE and TURN
  (both LAWFUL, and that is the axis's blindness stated as controls rather than as a boast), FUSED,
  DENSE. **A SIDON SET IS HEREDITARY, so this axis has NO FRAGILE CLAUSE and does not claim one** —
  strike a stud from a warrior plate and every surviving relation is still unique. It is the first
  axis in sixty-eight asked the 66th's question ("is any of this ornament merely ornament?") that
  answers **no**.
  **CLASS IDENTITY IS A CEILING ON REPETITION** — warrior LAMBDA=1, ranger 2, mage 3 — the first
  class identity in the project that is a PERMISSION rather than a form, and **the assignment is
  upside down**: LAMBDA=1 needs two studs, LAMBDA=3 needs a four-stud chain in step, so the strict
  law is the CHEAP one and the permissive law is the EXPENSIVE one. The warrior takes the strictest
  because a warrior sabaton in mid-jump is twelve pixels in a 5×4 box. **Every previous axis got
  harder as its law got stricter.**
  **RENDER-PAID:** an ornament re-scattered every frame is not an ornament but STATIC — the driver
  warm-starts from the previous pose in box-relative coordinates; a stud is ONE pixel and buys its
  relief from a dark 4-neighbour (a domino would make the mark's position ambiguous and this axis is
  all positions); the witness may not be demanded BELOW or the boots lose every stud on their bottom
  row; Chebyshev 2, not Manhattan 2, because through the finishing pass a diagonal pair reads as one
  short bar.
  Files: `scripts/gen_seme_axis68.py`, `scripts/preview_axis68.py`; staged in
  `_seme_legendary_preview/`, `_seme_legs_preview/`, `_seme_boots_preview/`,
  `_semedome_helmet_preview/` (24 sheets, **QA 24/24 ALL PASS**, all stamped
  `TaskQuestFinish=2026-08-01.6`). Previews `_PREVIEW_seme_*.png`, `_ZOOM_seme_arrows.png`,
  `_ZOOM_seme_grid.png`, `_ZOOM_seme_chest.png`, `_ZOOM_seme_head.png`.
  ⚠️ **On approval:** register as L69 in the LOOT_TABLE.

- **67th net-new-geometry axis — COLOPHON (the plate is ruled into REGISTERS and the registers COUNT
  THEMSELVES), chest + legs + helmet (boots ruled and EMPTY — see the theorem below)** (2026-08-10):
  the piece is ruled into bands, each opened by a 1px sunken groove that crosses the whole piece, and
  each band carries some number of raised BOSSES — two pixels of crest on the band's mid field. The
  law: **the number of bosses in register i is the number of registers that hold exactly i bosses.**
  **THIS IS THE FIRST AXIS WHOSE INVARIANT THE PLATE ITSELF ASSERTS.** All sixty-six before it are
  sentences WE say about the pixels — a statistic holds among the shards (46th), a wire is connected
  (54th), three hoops stand in 3:2:1 (61st), the studs exclusive-or to zero (64th), each row is the
  image of the row above (65th), no part can be carried away (66th) — the claim living in the spec and
  the plate being only the evidence. Here the claim is ON THE PLATE: the registers are a statement
  ("two registers hold none, none holds one, two hold two") and the acceptance test does not bring a
  claim to the pixels, it READS THE CLAIM OFF THE PIXELS and checks the pixels against it, consulting
  nothing outside. **It is the first plate in sixty-seven that could be FALSE.**
  **THE PAIR WITH THE 64th.** The 64th TALLY's studs carry a Hamming codeword: the plate CAN BE WRONG
  AND KNOW IT, invariant = REDUNDANCY, and what is checked is conformity to a CODE that lives outside
  the plate. The 67th's registers carry a census of themselves: the plate CAN SAY SOMETHING FALSE,
  invariant = SELF-REFERENCE, and its truth is not conformity to anything — it is CONSISTENCY WITH
  ITSELF.
  **Acceptance test — a NEW KIND: a SELF-AUDIT.** The reader is told nothing: not the class, not the
  word, not the number of registers, not which way they run. Clauses: (1) **RECOVERY** registers and
  boss counts read back exactly as driven, and **exactly ONE of the two readings of a piece may be a
  ruling** — the orientation is an OUTPUT (0 of 630 plates admitted two); (2) **DESCRIPTIVE** for
  every i, count(register i) == #{j : count(register j) == i}, from the recovered counts alone, **no
  tolerance constant anywhere in the file**; (3) **EXHAUSTION** the complete set of self-descriptive
  words is brute-forced for every length the body can hold and printed as an OUTPUT — k=4 has exactly
  two, k=5 exactly one, **k=6 NONE**, k=7 one, k=8 one — so **this is the first axis whose three class
  identities were not CHOSEN but ENUMERATED**; (4) **INDIFFERENCE** every boss is re-driven to a
  different lawful station and the word must come back IDENTICAL (2622 of 2730 stations moved) —
  **the first axis in sixty-seven that is invariant under moving its own elements**: pitch, phase,
  order, spacing and symmetry, the stuff the first sixty-six were made of, are all free here and the
  ornament survives their destruction; (5) **FRAGILE** strike one boss out of the pixels, or add one,
  and DESCRIPTIVE must fail — **NOTHING IN THIS ORNAMENT IS ORNAMENT**; (6) **LEGIBLE** every boss
  states itself on two pixels and both are required, and every groove must be complete.
  **THE EIGHT CONTROLS — five false, two DEAD, one lawful and unpayable. BLANK** (ruled, no bosses,
  0000: digits sum to 0 where they must sum to k) 630 violations, lower boundary, = the 11th FLUTING
  with grooves. **UNIFORM** (one boss per register, 1111) 630 — THE HONEST NEAR MISS, same relief same
  busyness one more pixel moved, and it **IS the 13th STUDWORK and the 40th DENTIL**; the control that
  proves the axis is ARITHMETIC AND NOT DECORATION. **SUMONLY** (0022 / 00122, found by search not
  hand-written) 525 — **SUM = k IS NECESSARY AND NOT SUFFICIENT, the bug this axis would have shipped
  with, invisible at 13px**. **PERMUTED** (0202 / 2101 / 12002) 595 — the axis's exact MULTISET of
  counts in the wrong registers, so the plate's histogram is right and the plate is wrong; the control
  that separates the axis's **two blindnesses** (where a boss sits is nothing, where a REGISTER sits is
  the whole law). **OFFBYONE** 1890, the worst score. **SINGLE** (a boss one pixel wide) and
  **UNRULED** (the groove left off the empty registers) are **DEAD — not one plate in twenty-four
  sheets can be READ, so there is nothing left to be right or wrong about**; SINGLE is why a boss is a
  domino and UNRULED is why **an empty band that is not ruled is not a register holding zero, it is no
  register at all** (2020 would read as a two-register plate). **LONG** (3211000, k=7) is **the only
  control that does not fail, and that is its finding**: 18 of 24 sheets cannot hold seven registers
  and go silent, so the axis's maximum word length is BODILY, not arithmetic.
  **CLASS IDENTITY IS A NUMBER THAT DESCRIBES ITSELF** — warrior **2020**, mage **21200**, ranger
  **1210**. Not a colour (64th), not a rule (65th), not a graph (66th), not a ratio (61st). The
  assignment is a bijection onto a provably complete set; WHICH class gets which was decided by the
  bodies — the mage's word is the long one because a wizard hat holds seven registers, and the ranger's
  is 1210 because a six-row hood read across the brow holds four and **2020 (two registers of two
  bosses) will not fit in it**.
  **THE AXIS HAS A MINIMUM AND THE MINIMUM IS A THEOREM: FOUR REGISTERS.** There is no self-descriptive
  word of length one, two or three — all 1 + 4 + 27 candidates enumerated, none works. A pair of
  sabatons ruled as one piece holds three registers, and read across the toes a groove would have to
  cross the gap between the feet where there are no pixels to be dark in. So **the boots of all three
  classes are RULED AND LEFT EMPTY and reported** — this axis's own BLANK control worn as an item,
  exactly as the 66th wore its GLUE there, except that **the 66th missed a sabaton by a pixel and this
  one misses by a THEOREM: no arithmetic closes the gap.** ⚠️ **DECISION FOR MATT: ship the 6 boot
  sheets as banded-but-silent sabatons, or skip the boots slot for this axis and register only 18?**
  **A SHEET IS RULED IN ALL FORTY-TWO POSES OR IN NONE** — an ornament that appears in some frames of a
  walk and not others reads as a BUG, not as a hard case. And the test of fit is not "can it be driven"
  but "can it be driven AND READ BACK EXACTLY". **ONE PIECE, ONE RULING, ONE WORD**: a register runs
  across BOTH legs, because the census is of the GARMENT — ruling the two shapes separately was the
  first draft and it gave the READER a choice (two legs ruled alike are also a lawful ruling of the
  pair, so the same pixels carried two words and nothing said which).
  **THE RENDER-PAID LESSONS, FOUR.** (a) **GROOVE_MIN was 3 for an afternoon and it cost the axis every
  helmet** — the crown of a dome is two pixels wide, so the first groove of every helmet was invisible
  and no helmet had a ruling at all; in the RIGHT reading a fully dark row can only BE a groove, so the
  threshold protects against nothing and the job of discriminating the wrong reading belongs to the
  exact structural test (opens on row 0, ≥2 registers, none shorter than 2 rows). (b) **TWO BOSSES GO
  CORNERWISE, NEVER SIDE BY SIDE** — side by side they need five columns and a sabaton is four; the
  64th paid for the same lesson from the other end (two-symbol relief in ROWS fuses into fluting bars).
  (c) **FIRST-FIT IS NOT GOOD ENOUGH** — greedy takes the leftmost station, blocks its own neighbour,
  and declares the plate impossible with nothing wrong with the body; `drive_band` backtracks and
  `bands_search` will cut the registers unevenly, and between them they rescued four whole sheets that
  were going out silent for want of a three-pixel-wide register. (d) **THE REGISTERS NEED NOT BE THE
  SAME HEIGHT** — nothing in the law says they are; only the reader's grip on which way the plate runs,
  and that grip is a groove on the first row, not a measurement.
  Palette — three temperatures, unrelated to the 64th (bronze/ice/bone), 65th (argent/gold/rose) and
  66th (basalt/porphyry/sandstone) so the four most recent axes cannot be mistaken for a recolor set:
  warrior **GARNET** (deep red iron), mage **CELADON** (cold green-grey glaze), ranger **OLIVE BRASS**;
  darkest channel-sums 206 / 224 / 194, all clear of the visor's black slits.
  Slots: chest Cuirass `shirt_%s_legendary67`, legs Chausses `pants_%s_legendary67`, helmet Helm
  `helmet_%s_legendary67`, boots Sabatons `boots_%s_legendary_colophon` (silent). Generator
  `scripts/gen_colophon_axis67.py` (repaint-only, QA-safe by construction — every pattern pixel painted
  ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4`, no scipy;
  twenty-third generator to call `sprite_finish.finish_array` in-line after axes 45–66; carries
  `--words`, `--cells`, `--accept`, `--controls`, `--survive`, `--sweep`). **Result: 630 plates, 2730
  registers, 2730 bosses — RECOVERY 0 violations and 0 plates admitted two readings; DESCRIPTIVE 0;
  EXHAUSTION 0; INDIFFERENCE 0 with 2622 of 2730 stations re-driven and 0 plates where nothing moved;
  FRAGILE 0 of 3219 struck plates still lawful and 0 added bosses still lawful; LEGIBLE 0. ALL PASS,
  five controls FAIL, two are DEAD, and LONG is lawful and unaffordable.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**, the 6 chests gaining +510 (m) /
  +440 (f) px — identical to the axis-45…66 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Survival through the finishing pass (reported, never a
  clause, and measured as LOCAL CONTRAST because the pass lays a cosine ramp across the sheet and a
  strict three-stop decode of a finished chest scores 0% while saying nothing about what a player can
  see): grooves still darker than their own register on **96% (chest) / 100% (legs) / 92% (helmet)**,
  bosses still lighter than their own row on **72% / 100% / 100%**. Staged in
  `_colophon_legendary_preview/`, `_colophon_legs_preview/`, `_colophon_boots_preview/`,
  `_colophondome_helmet_preview/`. Previews `_PREVIEW_colophon_legendary.png`,
  `_PREVIEW_colophon_legs.png`, `_PREVIEW_colophon_boots.png`, `_PREVIEW_colophondome_helmet.png`
  (built by `scripts/preview_axis67.py`); zooms `_ZOOM_colophon_chest.png`, `_ZOOM_colophon_head.png`,
  and the two that are the axis's real evidence — **`_ZOOM_colophon_census.png`** (one real cuirass with
  every register bracketed and counted, beside the plate's own sentence checked against the plate,
  register by register) and **`_ZOOM_colophon_lies.png`** (THE SAME CUIRASS FOUR TIMES: as shipped, then
  UNIFORM, PERMUTED and OFFBYONE — same ruling, same relief, same palette, within one boss of the same
  pixel count, and three of them say something false about themselves. If they cannot be told apart by
  eye, that is the finding).
  **On approval:** copy the 18 speaking PNGs (24 if the boots ship) to `sprites/preview_assets/char/`,
  add **L69** legendary LOOT_TABLE entries — `shirt_%s_legendary67` / `pants_%s_legendary67` /
  `helmet_%s_legendary67` (+ `boots_%s_legendary_colophon` if kept), m + f per slot per class,
  `rarity:'legendary'`.

- **66th net-new-geometry axis — DOVETAIL (the plate is cut into STONES, and the stones are cut so
  that the plate CANNOT BE TAKEN APART), all 4 slots** (2026-08-10): the field is ruled into 4x4
  stones, each one raised — lit on its top and right, shadowed below and left, so every seam reads as
  a hard 1px groove — and here and there a seam JOGS: a KEY, one stone's tail driven two pixels into
  its neighbour and two pixels wide at its far end, which cannot come back out through its own
  throat. Three pixels per joint. **THIS IS THE FIRST AXIS WHOSE INVARIANT IS AN IMPOSSIBILITY.**
  All sixty-five before it assert that something IS SO of the plate — a statistic holds among the
  shards (46th), a wire is connected (54th), three hoops stand in 3:2:1 (61st), the raised studs
  exclusive-or to zero (64th), each row is the image of the row above it (65th) — positive sentences
  whose subject is the pixels in front of you, every one settled by looking hard enough. This one
  asserts that **A SET IS EMPTY**: the set of motions that take a part of the plate away from the
  rest. It is not satisfied by anything the ornament does; it is satisfied by **what nothing can do
  to it**, and it is the first invariant whose subject is not the plate but **the plate's PARTS AND
  THEIR FREEDOM**.
  **THE PAIR WITH THE 65th.** The 65th CASCADE's invariant is a CAUSE — given its seed the plate
  could not have been otherwise, and the law runs FORWARD through the picture. The 66th's is a
  CONSTRAINT — the plate cannot BECOME otherwise, and the law forbids every path OUT of the picture.
  One says how the plate got here; the other says it is not leaving.
  **Acceptance test — a NEW KIND: a DISASSEMBLY, the first test that tries to DESTROY the artefact
  rather than read it.** Every predecessor's reader is a measurement — of an area, a winding number,
  a syndrome, a rule; even the 64th, which damaged its own sheets, damaged them in order to READ
  something back. This reader is a pair of hands: it recovers the stones from the pixels and then,
  for every one of the 2^n−2 ways of parting the plate and each of four directions, **takes hold and
  pulls**. Nothing is measured anywhere in the test; something is ATTEMPTED, 4·(2^n−2) times per
  plate, and the axis is that it never once succeeds. Clauses: (1) **TILING** the recovered stones
  partition the plate, all 4-connected, no gaps, no overlaps (GLUE fails here and nowhere else);
  (2) **SEIZED** no proper non-empty subset can be translated away in N/S/E/W — checked as strong
  connectivity of the blocking digraph AND **cross-checked by BRUTE FORCE over every subset**,
  because a theorem quoted is not a theorem run; **no tolerance constant anywhere in the file**;
  (3) **INTERLOCK** strike every key out and SEIZED must fail — the keys do the work, not the
  accident of which stone lies outside (RIVET fails); (4) **LOAD-BEARING** strike out any ONE key
  and SEIZED must fail — **NOTHING IN THIS ORNAMENT IS ORNAMENT**; (5) **REACH** every single stone
  blocked in all four directions — the WEAK clause, written down so the bug can be seen nearly
  passing it; (6) **LEGIBLE** every key states itself twice, at its neck and at its tail, and the
  pixels must report the joint EXACTLY as it was driven.
  **THE SIX CONTROLS. ASHLAR** (plain courses, no keys) is the lower collapse boundary and **is the
  17th axis exactly** — named rather than avoided, as the 65th named the 11th and the 16th; every
  course walks off (377 loose stones, 228 partings). **RIVET** replaces each key with a stud sitting
  ON the seam, symmetric, crossing nothing — identical failure profile to ASHLAR to the number, and
  it **is the 13th STUDWORK**; THE CONTROL THAT PROVES THE AXIS IS GEOMETRY AND NOT DECORATION.
  **PERCELL** is the class's tree with ONE INTERIOR KEY REMOVED: every stone still keyed, nothing
  moves on its own (9 loose stones of 240), and the plate comes apart in BLOCKS 36 plates out of 60
  — **the bug this axis would have shipped with, and it is invisible at 13px**; it is why SEIZED is
  about SUBSETS and why no per-stone test will ever do its work. **RING** (tree + one chord) and
  **REDUNDANT** (a key on every seam) teach the same unexpected lesson: **KEYS INTERFERE** — a
  surplus key is cut out of a stone that has already given three pixels to another, so it destroys
  the bite of the key it crowds, and REDUNDANT's stones are eaten hollow by their own joinery (54
  keys no longer readable at all). More joinery is not more holding. **GLUE** (one stone over the
  whole plate) passes SEIZED, INTERLOCK, LOAD-BEARING and REACH vacuously — the upper collapse
  boundary and the only reason clause TILING is counted.
  **CLASS IDENTITY IS THE SHAPE OF A GRAPH.** A dovetail is a full lock in the plane, so the keys are
  the edges of a graph on the stones and SEIZED holds exactly when that graph is CONNECTED — which
  costs n−1 edges, the provable minimum, so **the ornament is a SPANNING TREE**. Which tree is the
  class: warrior **CHAIN** (boustrophedon path, mean max degree 2.05), mage **RADIAL** (breadth-first
  from the middle stone, 1.21), ranger **COMB** (a spine with teeth, 1.28) — all recovered from the
  pixels by a reader never told the class. Not a colour (the 64th's identity was the mid tone), not a
  rule (the 65th's was the automaton).
  **THE RENDER-PAID LESSONS, THREE.** (a) **A STONE IS 4x4 AND THERE IS NO SMALLER NUMBER** — the key
  is a tail two deep whose far end is two wide, and for the lock to bite in BOTH senses of an axis
  the stone it enters must keep material on BOTH sides of the tail: two + one + one. (b) **THE
  SABATON IS THE AXIS'S OWN LIMIT, AND IT IS STATED RATHER THAN FAKED** — a boot is fourteen pixels
  of ragged diagonal with no solid 3x4 window anywhere in it, so THE JOINT DOES NOT FIT and the boots
  are cut as ONE UNCUT STONE, which is this axis's own GLUE control worn as an item. It is the first
  axis in sixty-six with a MINIMUM SIZE. (c) **WHERE THE BODY WILL NOT TAKE A KEY THERE IS NO SEAM** —
  two stones the silhouette is too ragged to dovetail are not left lying against each other (that is
  precisely the parting the axis forbids); they are cut as ONE STONE, which is what a mason does, and
  the merging repeats until the key graph reaches every stone. A plate that will not hold at all is
  left uncut and REPORTED, never shipped as a plate that quietly fails its own law.
  Palette — three building stones in three temperatures: warrior **BASALT** (cold blue-grey), mage
  **PORPHYRY** (imperial violet), ranger **SANDSTONE** (warm ochre); darkest channel-sums
  230/236/198, all clear of the visor's black slits. The sandstone was pulled two steps deeper than
  first drawn: at (222,202,164) its crest sat almost exactly on the skin ramp and the ranger jerkin
  dissolved into the ranger.
  Slots: chest Cuirass `shirt_%s_legendary66`, legs Chausses `pants_%s_legendary66`, boots Sabatons
  `boots_%s_legendary_dovetail`, helmet Helm `helmet_%s_legendary66`. Generator
  `scripts/gen_dovetail_axis66.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4`, no
  scipy; twenty-second generator to call `sprite_finish.finish_array` in-line after axes 45–65;
  carries `--cells`, `--trees`, `--accept`, `--controls`, `--survive`, `--sweep`). **Result: 497
  plates read, 1572 stones cut, 957 keys driven, 94 keys struck as idle — TILING 0 violations;
  SEIZED 0 plates part, 0 partings, and all 497 plates BRUTE-FORCED over every subset in all four
  directions; INTERLOCK 0; LOAD-BEARING 0; REACH 0 loose stones; LEGIBLE 0 keys misreported. ALL
  PASS, and all six controls FAIL.** 488 plates too small or too ragged to joint, painted as one
  uncut stone and reported.
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**, the 6 chests gaining +510 (m) /
  +440 (f) px — identical to the axis-45…65 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Survival through the finishing pass (reported, never a
  clause; measured RELATIVELY, since the finishing pass puts a cosine ramp across the sheet and an
  absolute three-stop reader is meaningless afterwards): chest 80%, legs 100%, helmet 50%. Staged in
  `_dovetail_legendary_preview/`, `_dovetail_legs_preview/`, `_dovetail_boots_preview/`,
  `_dovetaildome_helmet_preview/`. Previews `_PREVIEW_dovetail_legendary.png`,
  `_PREVIEW_dovetail_legs.png`, `_PREVIEW_dovetail_boots.png`, `_PREVIEW_dovetaildome_helmet.png`
  (built by `scripts/preview_axis66.py`); zooms `_ZOOM_dovetail_chest.png`,
  `_ZOOM_dovetail_head.png`, `_ZOOM_dovetail_tree.png` (every key ringed, the three trees side by
  side) and the artefact that is the axis's real evidence — **`_ZOOM_dovetail_disassembly.png`**, one
  real cuirass three times: as shipped and holding, the same stones with the keys struck out, and the
  same plate again with the stone that now walks off DRAGGED OUT OF IT. Same stones, same silhouette,
  same palette; the only difference is three pixels per joint.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L68** legendary
  LOOT_TABLE entries — `shirt_%s_legendary66` / `pants_%s_legendary66` /
  `boots_%s_legendary_dovetail` / `helmet_%s_legendary66`, m + f per slot per class,
  `rarity:'legendary'`.

- **65th net-new-geometry axis — CASCADE (an engraving that is not laid out but GROWN — every row
  the image of the row above it under one fixed nearest-neighbour rule), all 4 slots** (2026-08-09,
  documented 2026-08-10): the field is ruled into 2x1 ribs, each one either a RISE (lit on its left
  face) or a FALL (the same rib lit on its right face), and the law is `row r+1 = f(row r)` for a
  fixed f of (left, centre, right). The plate has a seed row and everything under it is consequence.
  **THIS IS THE FIRST AXIS WHOSE INVARIANT IS A CAUSE.** All sixty-four before it are RELATIONS —
  a statistic among shards (46th), a connected wire (54th), three hoops in 3:2:1 (61st), studs that
  exclusive-or to zero (64th) — sentences about pixels that are all equally present, checkable by
  holding the sheet still. This is a sentence about pixels PRODUCING other pixels: **the vertical
  direction of the plate is not a direction here, it is a HISTORY.** The 57th FESTOON gave the set an
  UP and the 55th STRATA gave it a BEFORE; this gives it an up that IS a before, each row not merely
  later than the one above it but caused by it.
  **Acceptance test — a NEW KIND: an INDUCTION, the first reader that is told nothing and RECOVERS
  THE GENERATOR FROM THE ARTEFACT.** Every predecessor's reader is an instrument brought to the sheet
  already knowing what it wants to measure — an area, a winding number, a syndrome. This one is
  handed the pixels and the mask, watches which triples are followed by which cell, and if that
  correspondence is a FUNCTION it has found the law and prints it by its Wolfram number. **The rule
  number appears nowhere in the test; it is an OUTPUT.** Clauses: (1) **DETERMINISM** no triple ever
  followed by two different things; (2) **REPLAY** the table is fitted on the TOP HALF of each plate
  and must predict the BOTTOM half cell-exactly — a forward prediction, because a table fitted on all
  the data and checked against all the data is a tautology; **no tolerance constant anywhere in the
  file**; (3) **RADIUS** radius one sufficient and radius zero contradictory (else every column is
  independent and it is the 11th FLUTING with extra steps); (4) **DEPENDENCE** the recovered rule is
  none of the eight projections (identity, shift, complement, constant) — the rules that make a
  picture out of nothing happening; (5) **SENSITIVITY** one seed cell turned over must never die,
  must SATURATE THE LIGHT CONE, and must grow strictly faster than the 12.0 a translation scores;
  (6) **LEGIBLE** every cell states its value on two stacked pixel pairs, both required to agree.
  **THE EXACT COMPLEMENT OF THE 64th.** The two ask the same question — WHAT DOES ONE WRONG PIXEL
  DO? — and answer it oppositely, and between them close it. The 64th: one flipped stud changes
  exactly ONE stud and the plate says its NUMBER; damage bounded, local, named; invariant =
  REDUNDANCY. The 65th: one flipped seed cell changes an ever-widening cone and no plate can say
  which cell it was, because a thousand wounds produce a thousand equally lawful plates; damage
  unbounded, non-local, anonymous; invariant = DETERMINISM. Redundancy buys the location of an error
  at the price of studs spent on nothing; determinism buys the whole plate for eight bits and a seed
  at the price of never being able to repair it. **Measured: one flipped cell costs the 64th exactly
  1 and costs this axis 45.0–76.0 cells over twelve rows.**
  **THE SIX CONTROLS. STATIC** (rule 204) passes DETERMINISM and REPLAY perfectly and forever because
  nothing ever happens — the lower collapse boundary, and it is the 11th FLUTING exactly. **SHIFT**
  (rule 170) is THE HONEST NEAR MISS: a genuine deterministic radius-one automaton carrying no
  information at all, and it looks exactly like the 16th TWILL — the reason clause DEPENDENCE is
  written down. **RANDOM** is the upper collapse boundary and at 13px is nearly indistinguishable
  from the axis by eye. **REPEAT** (four honest rows then tiled) is the bug this axis would have
  shipped with and is invisible — three rows in four perfectly lawful, seams two pixels tall, and it
  is exactly why clause REPLAY has no tolerance. **WIDE** (radius two) is not wrong, it is EXPENSIVE
  — the control that makes RADIUS a statement about economy. **REVERSED** proves the plate's arrow of
  time is a fact about the pixels and not a labelling convention.
  **CLASS IDENTITY IS THE LAW, not the palette**: warrior **rule 30** (chaotic, non-additive), mage
  **rule 90** (l XOR r), ranger **rule 150** (l XOR c XOR r) — all recovered from the pixels by the
  reader, never told to it. **THE SEED IS A FULL ROW, never a single lit cell** — a single cell under
  an additive rule draws a Sierpinski triangle and collides head-on with the 48th COSMATI. Two
  engraving stops per class and no third tone: warrior **ARGENT ON WINE**, mage **GOLD ON ABYSS**
  (the only warm-on-cold pair), ranger **ROSE ON OLIVE**; darkest channel-sums 200/218/194, clear of
  the visor's black slits. **The lit/dark ratio is held near 1.8, not the 3.5 the first draw used** —
  a 2px rib with a white face and a near-black face is not relief, it is a printed stripe, and the
  first render came out as barber-pole; relief at this scale wants the two faces of ONE material.
  The vertical split is the one arrangement the 64th could not use (its two-symbol relief had to go
  on a diagonal or rows fused into fluting bars); this axis can afford it only because the automaton
  guarantees no column stays in one state for long — the ornament shows the DOMAIN WALLS, and in an
  automaton the walls are the content.
  Slots: chest `shirt_%s_legendary65`, legs `pants_%s_legendary65`, boots
  `boots_%s_legendary_cascade`, helmet `helmet_%s_legendary65`. Generator
  `scripts/gen_cascade_axis65.py` (repaint-only, QA-safe by construction; twenty-first generator to
  call `sprite_finish.finish_array` in-line after axes 45–64; carries `--law`, `--cells`,
  `--controls`, `--accept`, `--sensitivity`, `--survive`, `--sweep`). **Result: 249 plates read,
  7290 cells engraved, 3113 verifiable — CLAUSE 1 0/3113 contradictions; CLAUSE 2 0/2546 predictions
  wrong; CLAUSE 3 3/3 classes; CLAUSE 4 rules 30/90/150 recovered; CLAUSE 5 all three saturate and
  never die; CLAUSE 6 0/7290 witness disagreements. ALL PASS, and all six controls FAIL.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**, the 6 chests gaining +510 (m) /
  +440 (f) px — identical to the axis-45…64 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Survival through the finishing pass (reported, never a
  clause): chest 88.6%, helmet 77.8%, legs 100%. Staged in `_cascade_legendary_preview/`,
  `_cascade_legs_preview/`, `_cascade_boots_preview/`, `_cascadedome_helmet_preview/`. Previews
  `_PREVIEW_cascade_legendary.png`, `_PREVIEW_cascade_legs.png`, `_PREVIEW_cascade_boots.png`,
  `_PREVIEW_cascadedome_helmet.png`; zooms `_ZOOM_cascade_chest.png`, `_ZOOM_cascade_head.png`,
  `_ZOOM_cascade_growth.png` and `_ZOOM_cascade_divergence.png` — the last being the axis's real
  evidence, one seed cell turned over and the cone of consequence spreading beneath it.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L67** legendary
  LOOT_TABLE entries — `shirt_%s_legendary65` / `pants_%s_legendary65` /
  `boots_%s_legendary_cascade` / `helmet_%s_legendary65`, m + f per slot per class,
  `rarity:'legendary'`.

- **64th net-new-geometry axis — TALLY (a mosaic of raised and sunken tesserae whose arrangement is
  a CODEWORD), all 4 slots** (2026-08-09): the plate is covered in 2x2 tesserae, each one either a
  BOSS (lit at the upper-left corner, shadowed at the lower-right) or a PIT (the same tessera with
  the light and the shadow swapped). Two symbols, one alphabet, and a law binding them: the studs are
  numbered along the plate and **the exclusive-or of the numbers of every RAISED stud is zero**.
  Five or six studs on a cuirass are not message at all; they exist to make that sum come out.
  **THIS IS THE FIRST AXIS THAT CAN BE WRONG AND KNOW IT.** All sixty-three before it are claims
  that a piece IS a certain way, checked by an instrument brought from outside — chip a shard off
  the 46th CRAQUELURE and the piece is silently a slightly different piece, and nothing in it
  objects. Turn ONE tessera over here — two pixels — and the exclusive-or is not merely nonzero, **it
  is the NUMBER OF THE STUD THAT WAS TURNED**, with no table and no search, because the check studs
  sit at the powers of two and so the syndrome IS the address.
  **THE INVARIANT IS REDUNDANCY, WHICH NO PREDECESSOR HAS BEEN.** The 50th RUNIC gave the piece an
  alphabet and no grammar; the 60th CADENCE gave it a grammar (which strings are legal); this gives
  it a CODE, and a code is not a bigger grammar — a grammar says which strings are legal, a code says
  the legal strings are FAR APART. So the invariant is not a property of the ornament in front of you
  at all: it is a property of **the ornaments it is NOT** (no two legal plates differ in fewer than
  three studs). **The first invariant in sixty-four axes whose subject is the SET rather than the
  member.**
  **Acceptance test — a NEW KIND: a DECODING, and the first test in sixty-four axes RUN ON SHEETS
  THAT HAVE BEEN DELIBERATELY DAMAGED.** Predecessors are accepted on a statistic (46/48/50/52/53), a
  topology (54), an algebra (55), a conservation law (56), a physical law (57), a group action (58),
  a census (59), a formal language (60), a similarity (61), a registration (62) or a kinematics (63)
  — and every one of those readers only ever sees correct input, which cannot tell a check from a
  coincidence. Clauses: (1) **SYNDROME** every plate decodes to zero, no tolerance; (2) **LOCATION**
  turn over stud i and the syndrome read back off the DAMAGED pixels equals i exactly — this is what
  separates a code from a checksum, and it makes the generator produce sheets it does not want;
  (3) **DISTANCE** no two legal plates closer than three studs, verified exhaustively over every
  weight-1 and weight-2 error at every realised length rather than cited; (4) **PAYLOAD** the message
  is not degenerate; (5) **RATE** the check costs exactly ceil(log2(n+1)) studs, the provable
  minimum; (6) **LEGIBLE** every stud carries its value on TWO OPPOSITE CORNERS, so no single pixel
  is a single point of failure.
  **THE SIX CONTROLS. RAW** (the field drawn straight from the message, the check asserted and never
  solved for) is the bug this axis would have shipped with and is visually identical to it — it is
  the 13th STUDWORK with a second symbol. **BLANK** (every stud sunk) passes SYNDROME, LOCATION,
  DISTANCE and RATE, because an empty sum is zero; it is the lower collapse boundary and the reason
  clause PAYLOAD exists. **CHECKSUM** (one check stud, the parity of the whole plate) is the honest
  near miss: cheaper, identical to look at, detects any single flip and cannot say where. **MIRROR**
  (the right half repeats the left) is redundancy without a code — n/2 studs spent, distance two, and
  a flip names a PAIR. **MAJORITY-3** passes 1, 2 and 3 honestly and spends two thirds of the plate
  to do what six studs do; it is the control that makes RATE mean something. **DENSE** (the tessera
  shrunk to 1x1) has a better rate on paper and one witness per stud — the upper collapse boundary,
  paid in legibility rather than arithmetic (measured: **79/79 studs survive the finishing pass at
  2x2 against 369/408 = 90.4% at 1x1**).
  **THE RENDER-PAID LESSONS, TWO.** (a) *The first draw put the three tones in ROWS* — crest row, mid
  row, dark row, flipped for a pit — and every tessera in a grid row then had its bright pixels on
  the same scanline, so runs of like symbols fused into horizontal bars and the cuirass came out as
  blotchy streaks, i.e. as a bad copy of the 11th FLUTING. **Putting the two tones on a DIAGONAL
  breaks the horizontal continuity by construction** and the plate reads as hammered metal. (b) *The
  first full run of clause PAYLOAD failed exactly one plate of 696* — a female warrior cuirass on
  slash frame 55, whose silhouette leaves only eight live tesserae of which four are check: four
  message studs is sixteen messages and one of them is the empty one, at which point a legal codeword
  is also an unengraved plate. **THE BLANK CONTROL IS REACHABLE, about once in sixteen on the
  smallest plates.** The fix was not to loosen the clause but to remove the degenerate message from
  the alphabet (a message that says the same thing in every stud says nothing), at an exactly stated
  price of two unreachable messages per plate.
  **THE CODEWORD SPANS THE PIECE, NOT THE COMPONENT.** A single sabaton is four pixels wide and holds
  six tesserae, and a code on six studs is four parts check to two parts message. So the two boots
  are ONE plate: turn over a stud on the left foot and some of the studs that name it are on the
  right one — **the redundancy is deliberately NON-LOCAL**. On the cuirass and the helm, one
  component each, nothing changes.
  Palette — warrior **BRONZE ON OXBLOOD**, mage **ICE ON DEEP TEAL**, ranger **BONE ON MOSS**;
  darkest channel-sums 200/212/194, all clear of the visor's black slits. Half of every tessera is
  the MID tone whatever the stud says, so **class identity lives in the mid** — the three mids are in
  three different temperatures (bronze-orange / steel-teal / sage-green) on purpose.
  Slots: chest Cuirass `shirt_%s_legendary64`, legs Chausses `pants_%s_legendary64`, boots Sabatons
  `boots_%s_legendary_tally`, helmet Helm `helmet_%s_legendary64`. Generator
  `scripts/gen_tally_axis64.py` (repaint-only, QA-safe by construction — every pattern pixel painted
  ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4`, no scipy;
  calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line, twentieth generator to do
  so after axes 45-63; carries `--code`, `--cells`, `--controls`, `--accept`, `--survive`,
  `--sweep`). **Result: 696 plates over all 24 sheets — 0 clause violations; 2604 single-stud wounds
  inflicted, re-rendered and re-read from the pixels, 0 misnamed; 318 distinct codewords; raised-stud
  fraction 0.222..0.800 (median 0.462); 144 plates too small to code (small sabatons and hoods on
  turned-away frames), painted plain and reported. ALL PASS.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45…63 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Sub-3px islands: 206 generated against 218 in the
  SOURCE sheets — none introduced. Staged in `_tally_legendary_preview/`, `_tally_legs_preview/`,
  `_tally_boots_preview/`, `_tallydome_helmet_preview/`. Previews `_PREVIEW_tally_legendary.png`,
  `_PREVIEW_tally_legs.png`, `_PREVIEW_tally_boots.png`, `_PREVIEW_tallydome_helmet.png` (built by
  `scripts/preview_axis64.py`); zooms `_ZOOM_tally_chest.png`, `_ZOOM_tally_head.png`, and the
  artefact that is the axis's real evidence — **`_ZOOM_tally_decode.png`**, a pristine cuirass beside
  four copies each with one tessera turned over, the number the plate reports printed under each and
  **the ring drawn FROM THE SYNDROME rather than from any record of the damage**, landing on the
  broken stud every time.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L66** legendary
  LOOT_TABLE entries — `shirt_%s_legendary64` / `pants_%s_legendary64` /
  `boots_%s_legendary_tally` / `helmet_%s_legendary64`, m + f per slot per class,
  `rarity:'legendary'`.

- **63rd net-new-geometry axis — CURRENT (level bands whose PHASE TRAVELS with the animation, one
  whole period per loop), all 4 slots** (2026-08-09): the piece is ruled into level bands — a bright
  CREST on its own one-row SHADE on a broad FIELD, period 4.5px — and the bands MOVE. Their phase
  advances every frame by P/L, where L is the length of the animation loop that frame belongs to, so
  the pattern comes back exactly where it started at the end of every cycle. The generator is never
  told a speed. It is told a WINDING NUMBER, which is 1, and it divides: P/5 on the idle, P/8 on the
  walk and the run, P/4 on the jump and the cheer, P/6 on the slash. **Four different speeds in one
  sheet, none of them written down anywhere, all of them consequences of a single integer.**
  **THIS IS THE FIRST AXIS WHOSE INVARIANT IS NOT A PROPERTY OF A PICTURE.** All sixty-two before it
  are claims about pixels that are on a sheet at the same time — the 46th about the areas of shards,
  the 54th about the connectivity of a wire, the 61st about the proportions of three hoops. Even the
  62nd DATUM, the only one that ever needed more than one sheet, is a claim about four sheets
  AGREEING, which is still a claim about a picture, just a bigger picture. Every one of them can be
  settled by looking. This one cannot: the invariant is a CLOSURE, it is not true or false of frame
  12 or of any frame, it is a property of frames 10..17 taken IN ORDER and joined end to end.
  **Shuffle the eight walk frames and the axis is gone while every pixel of every frame is
  untouched.**
  **Acceptance test — a NEW KIND: a KINEMATICS, the first claim that requires the frames to be put
  in order.** Predecessors are accepted on a statistic (46/48/50/52/53), a topology (54), an algebra
  (55), a conservation law (56), a physical law (57), a group action (58), a census (59), a formal
  language (60), a similarity (61) or a registration (62). (1) **ADVANCE** one (phase0, step)
  explains every row of every frame of a loop — the step is an OUTPUT of the measurement, never an
  input; (2) **CLOSURE** the step is IMPOSED at exactly one period per loop, only the starting phase
  left free, and not one row may disagree — a WINDING NUMBER; (3) **INVISIBLE** — the negative
  clause, and the one that says this is not any of the other sixty-two — every single frame ALONE is
  a valid static profile at some phase, i.e. **one picture carries no evidence whatever**; (4)
  **SPEED-VARIES** at least three distinct steps are realised over the batch; (5) **ONE PERIOD**
  exactly one P everywhere.
  **THERE IS NO TOLERANCE CONSTANT ANYWHERE IN THE FILE, AND THAT IS THE MAIN THING THE TEST GOT
  RIGHT.** An earlier draft measured the free step, multiplied by L, divided by P and asked whether
  the answer was near 1 — and "near" had to be set at 0.10 with the axis scoring 0.95 and the
  nearest control 1.11, a number chosen to sit in a gap. The gap was real; the constant was not. The
  free step is only ever known as an INTERVAL (every step inside it explains the loop perfectly —
  that is what INVISIBLE guarantees), so closure is not measured and compared, it is imposed and
  checked. Zero rows disagree or some do.
  **THE SIX CONTROLS, AND FOUR OF THEM FAIL THE SAME CLAUSE ON PURPOSE — with four different winding
  numbers, which is the clause saying WHAT each of them is rather than merely rejecting it.
  STATIC** (winding 0) is the 11th FLUTING and this axis's lower collapse boundary: it advances
  perfectly uniformly, by nothing, so it PASSES ADVANCE. **CONSTANT-SPEED** (winding L/8) is the
  honest near miss and the entire reason the step is derived rather than chosen — it is RIGHT on the
  walk and the run and wrong on the other four loops, which is a visible pop at the loop point
  forever. **NEAREST-INT** (the step rounded to a whole pixel, because pixels are integers) is the
  bug the axis would have shipped with: the phase is a threshold on a continuous coordinate, not a
  translation of a bitmap, and sub-pixel phase costs nothing. **DOUBLE** (winding 2) is the hard
  bound and it is Nyquist rather than taste: the shortest loop in the game is four frames, so at
  winding 2 its step is exactly P/2 and up and down produce identical sheets. **SMEAR** — the crest
  widened in proportion to the step, which is how a still picture usually says "moving" — is the
  most tempting wrong answer and the only one that changes the PROFILE rather than the phase; it
  fails all three clauses, reported rather than engineered away, because the reader is mode-blind
  and **INVISIBLE is logically prior to the other two: a phase measured off a profile the reader
  does not recognise is not a measurement of anything.** **RANDOM-PHASE** is the upper collapse
  boundary — all of the motion, none of the kinematics, and it boils.
  **THE PRICE IS PAID IN THE DELIVERABLE AGAIN, AND IN THE GAME.** The 62nd could not be judged on
  one sheet so its panel became a dressed character; this cannot be judged on one PICTURE, so the
  panel becomes a FILMSTRIP and a GIF — `_ZOOM_current_strip.png` (the idle loop plus THE WRAP
  FRAME, each figure beside its own measured crest/shade/field comb, above the same loop under
  CONSTANT-SPEED) and `_ANIM_current_walk.gif` (axis and control looping side by side) are the real
  evidence, and the four slot grids are correctly indistinguishable from fluting. Stated bluntly
  rather than argued away: **A PLAYER LOOKING AT A PAUSED GAME SEES THE 11th AXIS.** This axis
  spends its whole budget on the half of the time the character is animating.
  **THE RENDER-PAID LESSONS, THREE, ALL ABOUT MEASURING THE RIGHT THING.** (a) *The first reader
  measured each frame's phase and then differenced consecutive frames, and failed the axis on 19 of
  153 component-cycles* — every one a six-row sabaton or a helmet dome, with nothing wrong with the
  sprites. Differencing two noisy numbers doubles the noise, and the phase of ONE short component is
  intrinsically noisy: a whole interval of phases produces identical pixels, about P²/6E wide, which
  is 0.22px on a fifteen-row chest and 0.56px on a six-row boot — larger than the step being
  measured. The fix was not a looser tolerance but to fit the TRAJECTORY: one (phase0, step) against
  every row of every frame at once. **That is the thesis, not a convenience — the phase of a single
  picture is a poor measurement and the motion across the loop is a good one, which is exactly what
  it means for the invariant to belong to the sequence rather than to any of its members.** (b) *The
  search grid has to contain the axis's own motion.* On a grid of 0.025px the walk failed ADVANCE by
  ONE row in 120 because 0.5625 is not a multiple of 0.025. The grid is now P/lcm(4,5,6,8) = P/120 —
  derived from the app's frame budget, like everything else here. (c) *The strip's first marker
  ringed the TOPMOST crest and jumped about*, because the topmost crest is not a thing that
  persists: when the comb travels up, the top tooth leaves the plate and the one below becomes
  "topmost". The whole comb is marked instead — the same mistake, in a new place, as the 61st's
  reader segmenting hoops at their seams: measuring a feature the ornament does not have.
  Palette — warrior **EMBER ON IRON**, mage **ARC-WHITE ON INDIGO**, ranger **WISP ON BARK**;
  darkest channel-sums 248/224/188, all clear of the visor's black slits. The three FIELDS are in
  three different temperatures (cool grey / violet / warm brown) on purpose: the first render gave
  warrior and ranger two olives four units apart and at 13px they were the same armour in different
  hats. **Class identity on this axis has to live in the FIELD**, because the crest is the brightest
  thing on the sheet and is nearly white on all three by design. The period split was 0.28/0.50 and
  came out STRIPED — equal parts light and dark read as a wasp, not a relief; 0.24/0.46 gives one
  lit row, one dark row under it and enough plate between for the crest to be an event on a surface.
  Slots: chest Cuirass `shirt_%s_legendary63`, legs Chausses `pants_%s_legendary63`, boots Sabatons
  `boots_%s_legendary_current`, helmet Helm `helmet_%s_legendary63`. Generator
  `scripts/gen_current_axis63.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4`, no
  scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line, nineteenth
  generator to do so after axes 45-62; carries `--cycles`, `--cells`, `--controls`, `--accept`,
  `--sweep`). **Result: 153 component-cycles over all 24 sheets — 0 clause violations; every one
  closes on exactly one period with zero rows unexplained; 4 distinct speeds measured (0.5625,
  0.75, 0.90, 1.125 px/frame) against 4 distinct loop lengths; all 153 free-winding intervals
  contain 1. ALL PASS.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45…62 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Sub-3px islands: 206 generated against 218 in the
  SOURCE sheets — none introduced. Staged in `_current_legendary_preview/`, `_current_legs_preview/`,
  `_current_boots_preview/`, `_currentdome_helmet_preview/`. Previews `_PREVIEW_current_legendary.png`,
  `_PREVIEW_current_legs.png`, `_PREVIEW_current_boots.png`, `_PREVIEW_currentdome_helmet.png` (built
  by `scripts/preview_axis63.py`); zooms `_ZOOM_current_chest.png`, `_ZOOM_current_head.png`, and the
  two artefacts that are the axis's real evidence — **`_ZOOM_current_strip.png`** and
  **`_ANIM_current_walk.gif`, the first artefact in sixty-three axes that has to be PLAYED rather
  than looked at**.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L65** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **62nd net-new-geometry axis — DATUM (one oblique rib lattice laid across the whole suit from
  the crown of the wearer's skull), all 4 slots** (2026-08-09): the piece is ruled with one family
  of straight oblique ribs — a bright CREST sitting directly on its own cast SHADE, on a broad
  FIELD — and the position of every rib is `u = -1(x - x_datum) + 2(y - y_datum)` mod 10, where the
  datum is not on the armour at all. It is the CROWN OF THE WEARER'S SKULL, taken per gender and
  per frame off the skin sheet. Pitch 4.47px, slant one pixel down every two across, leaning LEFT
  because the character faces left.
  **THIS IS THE FIRST AXIS WHOSE ORIGIN IS OUTSIDE THE PIECE.** All sixty-one before it anchor to
  the component they are drawn on — the 11th flutes from the plate's own edge, the 46th tiles from
  its own box, the 47th measures distance to its own silhouette, the 53rd sizes beads from the room
  it leaves, the 57th hangs swags from its own top, the 60th windows its word at its own leading
  edge, the 61st derives every length from its own extent. That is why each of them is a property
  of a SHEET, and it is also why on every one of them the seam between two pieces of a suit is a
  discontinuity: two ornaments made of the same stuff, meeting. This one has no sheet-level
  existence. Ask it where a rib goes on a boot and it cannot answer from the boot; it goes where the
  head is. **Four sheets that never saw each other come out registered, and the evidence is a thing
  no previous axis could even be asked for: DRESS THE CHARACTER AND THE RIBS CROSS THE SEAMS.**
  **Acceptance test — a NEW KIND: a REGISTRATION, a claim about a shared FRAME OF REFERENCE.**
  Predecessors are accepted on a statistic (46/48/50/52/53), a topology (54), an algebra (55), a
  conservation law (56), a physical law (57), a group action (58), a census (59), a formal language
  (60) or a similarity (61). The 61st is the only one that needed more than one picture and what it
  needed was a RANGE OF SIZES; this needs pictures **of different things, made in separate runs,
  that must agree about where the world is** — so the test is run on a SUIT, not a sheet.
  (1) **ON-LATTICE** every painted pixel carries the role u mod P gives it; (2) **SEAMLESS** the
  phase estimated INDEPENDENTLY off each of the four slot sheets is the same phase in every frame;
  (3) **EXTERNAL** — the negative clause, and the one that says this is not any of the other
  sixty-one — the phase is NOT recoverable from the piece; (4) **BODY-TRACKING** the residual is
  zero in body coordinates in all 35 active frames while taking 9 distinct values in sheet
  coordinates; (5) **ONE LATTICE** exactly one (A,B,P) over the whole batch, and it is OBLIQUE.
  **THE FIVE CONTROLS, AND THE FIRST OF THEM IS THE ENTIRE POINT. SELF-ANCHORED** — every component
  its own origin, i.e. **WHAT ALL SIXTY-ONE PRIOR AXES DO** — is indistinguishable from this axis
  on any single sheet, by eye or by any test that looks at one sheet, and disagrees with itself
  across the four slots in **35/35** frames of the suit (EXTERNAL 0.995 against the axis's 0.156).
  **FRAME-ANCHORED** (canvas corner) is the honest near miss in the other direction: it PASSES
  SEAMLESS and fails BODY-TRACKING, i.e. its ribs stand still while the character walks through
  them — that defect is the whole reason the datum is a body landmark. **PER-SLOT-PITCH** is the
  adaptive-boundary rule nine earlier axes carry as their lesson and the 61st makes compulsory;
  here it is fatal (two pitches cannot cross a seam). **HORIZONTAL** is registered too and fails
  only OBLIQUE — *a level line crossing a seam would have lined up by accident*, which is why the
  ribs are slanted. **RANDOM-PHASE** is the upper collapse boundary (the 46th with a slant).
  **THE PRICE IS THE EXACT REVERSE OF THE 61st, AGAIN DELIBERATELY.** Canon fits the ornament to the
  piece so completely it has no size of its own; this refuses to look at the piece, so the piece has
  **no say** — a sabaton catches a crest, or catches only shade, and nothing is done about it,
  because doing something about it IS the SELF-ANCHORED control. Second cost, and a first for the
  set: **the ornament cannot be judged on a single sheet**, so the deliverable itself changes —
  `_ZOOM_datum_suit.png` (a DRESSED character beside the same character under SELF-ANCHORED) is the
  real evidence, not the slot grids.
  **THE RENDER-PAID LESSONS, THREE, AND ALL THREE ABOUT LOOKING BEFORE COMMITTING.** (a) *The 62nd
  slot was first designed as an elementary CELLULAR AUTOMATON* — rule 90 seeded by the component's
  own top row, an ornament that is GROWN rather than drawn, accepted by re-simulating it. Rendered
  on real components through `finish_array` it came back at ~50% density and read as
  **salt-and-pepper camouflage** on every rule tried (90/150/22/30). Killed before a generator
  existed. The 13px legibility lesson in a new disguise: **a rule can be beautiful and its orbit
  still be noise.** (b) *The datum cannot be the topmost pixel of the wearer* — in the CHEER frames
  both hands are raised ABOVE the head, so the top row is a pair of fists. The crown is found
  instead by matching **the skull's own 5 -> 7 -> 9 profile** (a run of 5-6 with nothing above it
  that widens by one each side for two rows); this is the Known-Issues "never trust per-frame head
  width on row 4" lesson, and the fix is to look for the skull's SHAPE rather than its EXTREME. All
  35 active frames resolve for both genders, and the result is skin-tone independent. (c) *The
  RANDOM-PHASE control passed SEAMLESS the first time it ran*, because its RNG was seeded per sheet
  and every slot therefore drew the SAME sequence — **a synchronised control, not a random one**.
  Seeded from the slot as well. Also: HORIZONTAL fails BODY-TRACKING as well as OBLIQUE, and the
  reason is worth keeping — with A=0 the coordinate is 2y, so it samples only five of its own ten
  profile positions and **cannot identify its own phase to better than ±1**. A level lattice on an
  integer grid is degenerate: one more argument for OBLIQUE than the clause was written for.
  Female sheets that fall back to the male source art still take the **female** datum, because the
  wearer is female even when the garment art is shared.
  Palette — warrior **STORM PEWTER**, mage **COBALT**, ranger **MOSS**; darkest channel-sums
  270/244/210, all clear of the visor's black slits; crests chosen for what they BECOME after the
  finishing pass lifts the sheet (the 61st's salmon lesson).
  **NO COMPONENT LABELLING ANYWHERE IN THE GENERATOR, and that is a property rather than an
  omission** — a pixel is told its role by its own coordinates and the wearer's crown and does not
  need to know which garment it is on. `label4` appears only in the acceptance test and the
  diagnostics; every prior axis begins by segmenting the sheet.
  Slots: chest Cuirass `shirt_%s_legendary62`, legs Chausses `pants_%s_legendary62`, boots Sabatons
  `boots_%s_legendary_datum`, helmet Helm `helmet_%s_legendary62`. Generator
  `scripts/gen_datum_axis62.py` (repaint-only, QA-safe by construction — every pattern pixel painted
  ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4`, no scipy;
  calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line, eighteenth generator to
  do so after axes 45-61; carries `--lattice`, `--cells`, `--accept`, `--profiles`, `--sweep`).
  **Result: 1074 components across all 24 sheets x 35 active frames — 0 off-lattice; 840/840 sheet
  phases match the datum; 210/210 suit-frames have all four slots in agreement; EXTERNAL 0.156
  against the SELF-ANCHORED control's 0.995; body residual {0} across 9 distinct sheet phases; one
  lattice (-1, 2, 10). ALL PASS.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45…61 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Sub-3px islands: 206 generated against 218 in the
  SOURCE sheets — none introduced. Staged in `_datum_legendary_preview/`, `_datum_legs_preview/`,
  `_datum_boots_preview/`, `_datumdome_helmet_preview/`. Previews `_PREVIEW_datum_legendary.png`,
  `_PREVIEW_datum_legs.png`, `_PREVIEW_datum_boots.png`, `_PREVIEW_datumdome_helmet.png` (built by
  `scripts/preview_axis62.py`); zooms `_ZOOM_datum_chest.png`, `_ZOOM_datum_head.png`, and the two
  panels that draw the test itself — **`_ZOOM_datum_suit.png`, THE AXIS DRAWN**: a dressed character
  beside the same character under SELF-ANCHORED, where one rib followed from the shoulder crosses
  the seams unbroken on the left and steps at every seam on the right; and
  **`_ZOOM_datum_controls.png`, THE CLAUSES DRAWN**: the dressed warrior under the axis and each of
  the five controls with the clauses each fails.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L64** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **61st net-new-geometry axis — CANON (three hoops in the proportions 3 : 2 : 1, and no length
  anywhere), all 4 slots** (2026-08-08): whatever the piece is, it is divided top to bottom into
  exactly THREE raised hoops in the proportions 3 : 2 : 1, and each hoop is divided into
  1 : 1 : 2 : 1 : 1 in its own turn — shade, field, crest, field, shade. There is no pitch, there is
  no gauge, and there is not one length measured in pixels anywhere in the generator. The armour is
  told a proportion and works out its own sizes.
  **THIS IS THE FIRST AXIS WHOSE INVARIANT IS A RATIO AND NOT A LENGTH.** Every one of the sixty
  before it fixes a distance — the 11th flutes every 3, the 40th hangs a tooth every 4, the 46th
  takes 4.5, the 51st 3.6, the 52nd keeps two periods coprime, and even the 60th's irrational pitch
  is a pitch, in pixels, the same on a cuirass as on a sabaton. That constancy is exactly what makes
  those axes read as a MATERIAL. This one has none: ask it how wide a hoop is and it has no answer
  until it is shown the piece. On a warrior chest of 15 rows the hoops come out **8, 4, 3**; on the
  sabaton of the same suit, 6 rows, they come out **3, 2, 1** — and 3 : 2 : 1 is exactly six parts,
  so the smallest piece in the game is the ornament at its irreducible minimum, ONE PIXEL TO THE
  PART. The boot is not a detail of the cuirass; it is the same drawing printed small.
  **Acceptance test — a NEW KIND: a claim of SIMILARITY, by measurement.** Predecessors are accepted
  on a statistic (46/48/50/52/53), a topology (54), an algebra (55), a conservation law (56), a
  physical law (57), a group action (58), a census (59) or a formal language (60) — every one of
  them a statement about ONE picture. This one cannot be made about one picture at all: a single
  hoop pattern is in 3 : 2 : 1 or it is not, and that is arithmetic. The claim is that several
  hundred pictures **spanning a factor of nearly five in size are the same picture**, related by a
  scale factor and nothing else. (1) **PARTITION** exactly one crest run per hoop over a fully
  readable extent; (2) **PLACED** the crest CENTRES are where the canon puts them, re-derived from
  the component's own extent alone — a crest sits in the middle of its hoop whatever length it is,
  so where the crests are IS a measurement of where the hoops are, and this clause is about the
  proportion and nothing else; (3) **SELF-SIMILAR** each crest RUN LENGTH is the quarter its own
  hoop's canon gives it, so the crest scales too — about the inside of a hoop and nothing else;
  (4) **CANONICAL** the umbrella, row for row; (5) **SCALE-FREE** the batch spans >= x2 in gauge,
  without which the other four are satisfiable by an axis that never has to scale anything.
  **THE FIVE CONTROLS DO NOT EACH FAIL A DIFFERENT CLAUSE — THEY FAIL IN TWO GROUPS, AND THE SPLIT
  IS EXACTLY THE SPLIT BETWEEN THE AXIS'S TWO LEVELS**, which is reported rather than tidied away.
  FIXED-3 (a 3px hoop everywhere) fails PARTITION with five crest runs on a chest and two on a boot
  — it is the 11th FLUTING exactly, this axis's lower collapse boundary. **EQUAL (1 : 1 : 1) is the
  control the axis exists against**: it is the 12th axis's BANDED LAMELLAR, it is what anyone draws
  first, its crest centres land **2.5 rows off** on a warrior chest — and on a six-row sabaton it is
  2:2:2 against this axis's 3:2:1, ONE PIXEL, which is the whole content of the axis. GOLDEN
  (1 : phi : phi^2) fails PLACED by 4.5 rows and exists to show the test discriminates WHICH ratio
  and not merely "unequal". **FIXED-CREST is the sharpest near miss and the only control that
  reaches SELF-SIMILAR with the proportion already right** — hoops proportional, crest pinned at 1px
  the way every other axis in the set pins it, so the plate goes flat: a hoop whose highlight does
  not grow with it stops being a roll and becomes a panel with a wire down it.
  **THE PRICE IS THE EXACT REVERSE OF THE 60th, DELIBERATELY.** Cadence forbids per-component
  adaptation outright (a word re-phased per plate is a different word per plate). This axis is
  nothing BUT per-component adaptation and it is compulsory, because a hoop sized from anywhere
  except its own component breaks the similarity. The 60th is one text quoted everywhere at constant
  type size; this is one figure printed at whatever size the paper is. A named consequence rather
  than a hidden one: **the ornament BREATHES** — a leg that lengthens by a row through the run cycle
  gets a proportionally taller hoop on that frame, which on a fixed-gauge axis would be the pattern
  sliding under the animation and here is the axis working.
  **THE RENDER-PAID LESSONS, BOTH OF THEM ABOUT MEASURING RATHER THAN ABOUT ARMOUR.** (a) *The first
  reader segmented hoops at their SEAMS* and split every hoop whose crest is more than one row —
  which on this axis is most of them, since the crest is a quarter of the hoop. Worse, even repaired
  it could not have worked: **a seam is the one feature of this ornament that cannot be located from
  the pixels**, because two adjacent hoops each contribute shade rows to it and nothing in the
  picture says where one lot ends. The CREST RUNS have neither problem — one per hoop, never
  adjacent under this canon — so the whole test is a function of them. (b) *The first draft reported
  only the FIRST clause a component tripped over*, and the controls table then said true but
  misleading things (EQUAL was recorded as failing SELF-SIMILAR because that check happened to run
  first, when what is actually wrong with EQUAL is the proportion). **A test that reports the first
  thing it trips over is reporting the order of its own source code.** All failing clauses are now
  reported. (c) Palette: the warrior crest was chosen in the swatch and came back **salmon** in the
  preview, because the finishing pass lifts a sheet before anything else touches it — **a crest is
  chosen for what it becomes, not for what it is**; dropped 236,198,190 -> 232,176,164.
  Geometry: `parts()` divides by CUMULATIVE rounded boundaries, not by rounding each part against
  its own ideal — that is the REMAINDER control and the bug the axis would have shipped with (it
  leaves a row over on **32 of the 194 extents from 6 to 199**; the canon leaves one over on none,
  because its parts are differences of integers). Three tones, no fourth: **no silhouette rim**,
  because a rim is a one-pixel feature and a rimmed row is a row the reader cannot measure — no
  censored sample, unlike the 60th. Palette — warrior oxidised **CRIMSON STEEL**, mage **AMETHYST**,
  ranger **DEEP TEAL**; darkest channel-sums 204/308/264, all clear of the visor's black slits.
  Slots: chest Cuirass `shirt_%s_legendary61`, legs Chausses `pants_%s_legendary61`, boots Sabatons
  `boots_%s_legendary_canon`, helmet Helm `helmet_%s_legendary61`. Generator
  `scripts/gen_canon_axis61.py` (repaint-only, QA-safe by construction — every pattern pixel painted
  ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4()`, no scipy;
  calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line, seventeenth generator to
  do so after axes 45-60; carries `--canon`, `--cells`, `--accept`, `--swatch`, `--sweep`).
  **Result: 985 components across all 24 sheets x 60 active frames — 951 carrying the canon, 34
  shorter than six rows reported not failed; 0 clause violations; 17 distinct extents from 6 to 23
  rows; gauge 2 .. 9.5 px, span x4.75. ALL PASS.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45…60 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. The 22 sub-3px islands the whole-sheet sweep finds are
  all present in the SOURCE sheets (verified pixel-for-pixel) — inherited, not introduced. Staged in
  `_canon_legendary_preview/`, `_canon_legs_preview/`, `_canon_boots_preview/`,
  `_canondome_helmet_preview/`. Previews `_PREVIEW_canon_legendary.png`, `_PREVIEW_canon_legs.png`,
  `_PREVIEW_canon_boots.png`, `_PREVIEW_canondome_helmet.png` (built by `scripts/preview_axis61.py`);
  zooms `_ZOOM_canon_chest.png`, `_ZOOM_canon_head.png`, and TWO panels that draw the test itself —
  **`_ZOOM_canon_scale.png`, THE AXIS DRAWN**: the same ornament on plates of 6/10/15/22/30 rows with
  the hoop widths under each, which is also the panel showing the property no fixed-pitch axis can
  have — this ornament cannot go too fine to see, because it has no gauge to be too fine at; and
  **`_ZOOM_canon_controls.png`, THE CLAUSES DRAWN**: the same chest from the canon and from each of
  the five controls with the clauses each fails, where EQUAL is the cell to stare at.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L63** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **60th net-new-geometry axis — CADENCE (reeds of two widths whose ORDER is the ornament), all 4
  slots** (2026-08-08): the piece is ruled edge to edge with raised reeds of exactly TWO widths, in
  one metal, one relief, one light — and the ORDER in which the two widths follow one another is the
  whole ornament. Nothing else varies. A reed opens on a bright CREST row and closes on a SHADE row;
  a WIDE reed, and only a wide reed, has one flat FIELD row between them. There is one kind of
  element, it comes in two sizes, and everything this axis has to say is in the sequence.
  **THIS IS THE FIRST AXIS WHOSE DEFINING CONSTANT IS IRRATIONAL.** All fifty-nine before it have a
  pitch and every pitch is a ratio of whole numbers — the 11th flutes every 3, the 40th hangs a
  tooth every 4, and even the 51st's 3.6 and the 46th's 4.5 mean "3.6 pixels of the same thing over
  and over". A rational pitch is a PROMISE THAT THE ORNAMENT REPEATS, and all fifty-nine keep it.
  This one has a pitch of phi reeds per wide reed, so it cannot repeat — not on a torso, not on a
  tabard the size of a wall, not ever. The word the reeds spell is the mechanical word of slope
  alpha = (sqrt5-1)/2 — the Fibonacci word — and it is not an arbitrary aperiodic sequence: among
  all sequences over two letters that never repeat it is the one with the FEWEST distinct subwords
  it is possible to have, exactly n+1 of each length n. A periodic word runs out of subwords (never
  more than its period); a random word has 2^n. **n+1 is the unique value in between and it is the
  signature of an irrational slope.** alpha's continued fraction is all ones, i.e. it is the
  WORST-approximable number there is, and that is not decoration: a slope near a rational produces
  long stretches indistinguishable from the RATIONAL control on a piece the size of a boot.
  **Acceptance test — a NEW KIND: a statement about a FORMAL LANGUAGE.** Predecessors are accepted
  on a statistic (46/48/50/52/53), a topology (54), the algebra of an order (55), a conservation law
  along a traversal (56), a physical law (57), a group action (58) or a census of a group (59). Here
  the ornament is read off the painted pixels AS A WORD — a finite string over WIDE and NARROW — and
  the batch is asked which LANGUAGE its strings belong to by counting distinct subwords. Nothing
  weaker will do, because the claim is not about any one piece but about what the pieces have in
  common. (1) **QUOTED** every readable reed carries the letter the word puts at that position;
  (2) **BALANCED** WW never occurs and NNN never occurs; (3) **COMPLEX** exactly n+1 distinct
  subwords of length n; (4) **GOLDEN** narrow-to-wide is phi.
  **THE FOUR CONTROLS EACH FAIL AT A DIFFERENT LENGTH, AND TOGETHER THEY PIN THE AXIS FROM BOTH
  SIDES.** UNIFORM |F(1)|=1 — and it is not a straw man, it is the 11th FLUTING exactly, i.e. this
  axis's lower collapse boundary: take the second letter away and you are back at axis 11.
  ALTERNATING (slope 1/2) |F(2)|=2 — the 38th EGG-AND-DART. RANDOM |F(2)|=4 with touching wide reeds
  — aperiodicity WITHOUT a law, i.e. the 46th CRAQUELURE, the upper boundary. **RATIONAL (slope 3/5,
  a Fibonacci convergent) is the control the axis exists against and the only one a viewer could
  mistake for a pass**: balanced, no WW, no NNN, and by eye it IS this axis — it saturates at
  |F(5)|=5 instead of 6, because a periodic word can never have more subwords than its period.
  Rationalise the slope and the axis collapses into 11/38/40; randomise it and it collapses into 46;
  it lives in the one place that is neither, and there is exactly one such place per irrational.
  **THE PRICE IS THE EXACT OPPOSITE OF EVERY PRECEDENT IN THE SET — the first time in sixty axes
  that ADAPTATION IS THE ERROR.** Nine axes carry the adaptive-boundary lesson: choose the gauge,
  phase or pitch PER COMPONENT from what that component can show. This axis is forbidden to. A word
  re-phased to suit each plate would be a DIFFERENT word on each plate, and then there is no one
  word for the pieces to be windows of and no language to test. So the reeds are laid from one
  infinite word with no search and no scoring anywhere in the file, and each component takes the
  window its own position selects (k0 = round(min t)); the reeds are anchored to each component's
  leading edge so nothing slides under the walk cycle, and they are still all quotations from one
  text.
  **THE RENDER-PAID LESSON, AND IT IS A STATISTICAL ONE: A STATISTIC READ OFF A CENSORED SAMPLE IS
  THE STATISTIC OF THE CENSORING.** The first acceptance run over the finished batch FAILED clause 4
  — narrow:wide came back **1.7519** against phi = 1.6180. Nothing was wrong with the armour. A reed
  is only readable if the silhouette leaves all its rows on the plate, and a WIDE reed is 3 rows
  where a NARROW reed is 2, so a wide reed is systematically likelier to be clipped and discarded:
  the sample was censored by an event whose probability depends on the very quantity being measured
  — textbook length-biased sampling, biased toward narrow BY CONSTRUCTION. Measured three ways
  (`scripts/_diag_cadence_ratio.py`): readable reeds **1.7519** (err +0.134), reeds INTERIOR to a
  maximal readable run **1.6131** (err -0.005), the word AS PLACED on the bodies **1.6343** (err
  +0.016, the uncensored ground truth). **The fix is not a wider tolerance — that is tuning a test
  until it passes.** Clause 4 is now asked of run interiors, reeds admitted because their NEIGHBOURS
  were readable rather than because of their own width, which the clipping cannot bias; clauses 2-3
  stay on the full runs, which have 5x the windows and are immune anyway because complexity counts
  DISTINCT subwords and is blind to how often each occurs. Because the estimator got 25x more
  accurate the tolerance was **TIGHTENED 0.12 -> 0.05**, which strengthens the test exactly where it
  matters: the RATIONAL control's frequency is 3/2 = 1.5 (err 0.118) and it now fails clause 4 as
  well as clause 3, so the nearest rational to this axis is excluded twice over. All four controls
  now fail on frequency AND on complexity.
  **A SECOND, LATENT HOLE CLOSED IN THE SAME PASS.** The reader flattened its per-reed read-back
  with `[v for v in read if v is not None]`, which SPLICES the reeds either side of an unreadable
  one into a single string. On this batch the gaps are terminal and the two agree exactly, so no
  sheet was ever wrong — but a gap mid-component would have manufactured an adjacency that is not in
  the word and clause 3 would have counted the spliced pair as legitimate and accepted it. A window
  onto a text is a CONTIGUOUS piece of it; two fragments are two windows. Now split into maximal
  runs (`runs_of`), with zero change to the reported numbers.
  Geometry: banding on a raked coordinate t = (x+3y)/sqrt10 (neither the 11th's verticals nor the
  50th's horizontals); reeds cut from the component's own leading edge at w = 2 (NARROW) or 3
  (WIDE); the two letters open and close IDENTICALLY (asserted at import) so WIDTH and nothing else
  tells them apart — a wide reed is a narrow reed with ONE ROW OF FIELD INSERTED. 3:2 is the
  smallest pair of reed heights tellable apart across a 13px torso after the finishing pass; at 4:3
  a warrior chest holds five reeds and a boot holds one. NARROW is the COMMON letter (frequency
  alpha = 0.618) so a wide reed reads as an ACCENT in a run of narrow ones rather than as a ground
  with stripes on it. Palette — FOUR stops (crest/field/shade/edge), ONE ramp, no second colour
  family anywhere, because the two letters must not be distinguishable by tincture (the exact
  complement of the 59th, whose two tinctures share one FORM so only colour tells them apart); the
  classes separate by TEMPERATURE not hue — warrior oxidised **BRASS**, mage **MOONSTONE**, ranger
  **VERDIGRIS BRONZE**. No stop near black (darkest channel-sums 218/312/206) so the visor's slits
  survive the reeding.
  Slots: chest Cuirass `shirt_%s_legendary60`, legs Chausses `pants_%s_legendary60`, boots Sabatons
  `boots_%s_legendary_cadence`, helmet Helm `helmet_%s_legendary60`. Generator
  `scripts/gen_cadence_axis60.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, silhouette untouched; self-contained `label4()`, no
  scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line, sixteenth
  generator to do so after axes 45-59; carries `--word`, `--cells`, `--accept`, `--swatch`,
  `--sweep`).
  **Result: 985 components across all 24 sheets x 60 active frames — 667 quoting >= 3 reeds, 318
  shorter windows reported not failed; 3239 letters read off pixels; 0 clause-1 violations;
  complexity 2/3/4/5/6 at lengths 1-5 over 3239/2254/1317/650/267 windows; 0 forbidden subwords;
  narrow 813 / wide 504 = 1.6131 on run interiors. ALL PASS.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…59 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry. Staged in
  `_cadence_legendary_preview/`, `_cadence_legs_preview/`, `_cadence_boots_preview/`,
  `_cadencedome_helmet_preview/`. Previews `_PREVIEW_cadence_legendary.png`,
  `_PREVIEW_cadence_legs.png`, `_PREVIEW_cadence_boots.png`, `_PREVIEW_cadencedome_helmet.png`
  (built by `scripts/preview_axis60.py`); zooms `_ZOOM_cadence_chest.png`, `_ZOOM_cadence_head.png`,
  and TWO panels that draw the test itself — **`_ZOOM_cadence_word.png`, THE CLAUSE DRAWN**: the
  same chest painted from the axis's word and from each of the four controls with |F(1..5)| and the
  frequency under each, where the RATIONAL cell is the one to stare at because it is the one that
  looks right and is not; and **`_ZOOM_cadence_censor.png`, THE ESTIMATOR DRAWN**: the same plate
  showing every reed the word places / the reeds that survive to be read / the run interiors, with
  the three batch ratios under them.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L62** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **59th net-new-geometry axis — COUNTERCHANGE (a two-tincture vair that trades places across an
  undrawn division), all 4 slots** (2026-08-08): the piece is covered edge to edge in a heraldic
  VAIR — interlocking bells, one tincture pointing up and the other down, an exact 50/50 partition —
  and somewhere across it the metal and the colour TRADE PLACES. Nothing marks where. No line, no
  border, no seam, no rivet. The division is visible only because every bell that straddles it comes
  out half one tincture and half the other, and because from there on the metal is doing what the
  colour was doing.
  **THIS IS THE FIRST AXIS WHOSE SYMMETRY IS AN ANTISYMMETRY.** The 58th was the first whose ELEMENT
  was chiral, accepted by exhausting a rotation group on the pixels; this is the next question about
  the same machinery and a harder one, because the operation the piece is invariant under is NOT A
  MOTION. Fold the piece along its division: every shape lands on a shape and every one is the wrong
  tincture, so the fold is not a symmetry. Leave it flat and swap the two tinctures: nothing has
  moved, so that is not a symmetry either. Do BOTH and the piece is itself again, pixel for pixel.
  The invariance belongs to neither the geometry nor the colouring but only to their PRODUCT — in
  crystallography a black-and-white or Shubnikov operation, and no axis in the set has had one. All
  fifty-eight before are invariant under some subgroup of the ordinary motions of the plane; the
  58th denied one of those motions to its ELEMENT, and this one denies the whole group to the
  PICTURE and hands it back only on condition that the palette move too.
  **THE CONSEQUENCE THAT MAKES IT VISIBLE IS FORCED, NOT CHOSEN.** An antisymmetry can have no fixed
  pixel — a pixel it leaves in place would have to be the opposite tincture to itself, and there is
  no such tincture — so the mirror cannot run ALONG a row, it must run BETWEEN two, and the two rows
  it runs between are each other's opposites at every column. That run of contrast reversals, with
  nothing drawn on it, IS the division. It is also precisely what a translation cannot produce,
  which is the whole distinctness argument: a **CHEQUY** is antisymmetric too (shift one square,
  swap the colours), but that operation moves every point, so it leaves nothing anywhere to see it
  by — a chequy has no division and no place, it is the SAME EVERYWHERE. Other near misses: **26th
  TARTAN** — swap its colours and you get a different tartan, and this axis is the exact complement
  of the 58th's tartan decision (there the two hands had to share one METAL so only form told them
  apart; here the two tinctures share one FORM so only colour does). **29th HOUNDSTOOTH / 18th
  BASKETWEAVE** — real two-colour weaves, antisymmetric under translations, so no locus. **37th
  COFFER / 43rd GADROON** — inversions applied uniformly, which produce a SECOND PIECE; here both
  states are on the SAME piece and the ornament is the boundary. **52nd AJOURÉ** — two surfaces with
  a definite front and back; here there is one surface and "which tincture is the ornament" HAS NO
  ANSWER, which is the content, not vagueness. **55th STRATA** — an ORDER; this is an EXCHANGE, an
  involution with no first and no last. **8th AEGIS ROUNDEL / 7th GIRDLE** — an object at a place;
  this puts no object anywhere, it puts an EVENT along a line.
  **THE RULE OF TINCTURE IS IN THE PALETTE AND IT IS A LEGIBILITY LAW, NOT A CONVENTION.** Never
  colour on colour, never metal on metal — because the two tinctures must be told apart across ONE
  pixel after the finishing pass has shaded both. So every class is one METAL against one COLOUR and
  the gap between the families is the largest value gap any axis has used. Heraldry admits exactly
  two metals and there are three classes, so rather than invent a third the class reads off the
  COLOUR, and the three colours are the three the set has never used: warrior **OR on AZURE**, mage
  **ARGENT on PURPURE**, ranger **OR on VERT**. Darkest stops clear channel-sum 150 (warrior 182,
  mage 174, ranger 152) so the visor's black slits survive on the dark half of a dome
  (`_diag_cchange_visor.png`).
  **THREE RENDER-PAID / CENSUS-PAID LESSONS.** (1) *THE FOLD MUST CROSS THE FUR'S GRAIN.* A 50/50 fur
  with congruent tinctures is necessarily antisymmetric under its own half-period shift — that shift
  is WHY the two classes are congruent — and a fold laid parallel to it leaves it intact: a torso
  folded per pale came back with THIRTEEN antisymmetries, one of them the fold and twelve of them
  the vair's own shift. So the fur carries a GRAIN and the division family is taken perpendicular to
  it (per fess with an upright fur, per pale with a quarter-turned one); the shift then carries
  points over the line, is negated twice, and dies. (2) *AN OPERATION'S VERDICT IS ONLY AS GOOD AS
  THE SHARE OF THE PIECE THAT WITNESSES IT, AND THE SHARE IS A HALF.* At 0.30 a warrior leg reported
  three antisymmetries; measured, the fold is witnessed by 66 of its 98 pixels and each phantom by
  30. Every fold in the batch clears 0.5; nothing else comes near. (3) *WHEN A PIECE IS TOO SMALL TO
  BE FOLDED, ITS OTHER HALF IS THE OTHER PIECE.* A boot is a 16px L and no line can be drawn through
  it with a fur on both sides; folding them anyway produced 61 violations, every one a boot or a
  walk-frame leg. So the LEFT boot carries the fur and the RIGHT boot its negative, both read out of
  ONE fur in the frame's coordinates, ordered by CENTROID and never by label id (raster order swaps
  the pair mid-stride). This is the 58th's PENDANT move and here it is the stronger statement: on a
  torso the line is undrawn but does lie somewhere on the plate; on a pair of boots it is not on
  either piece at all, and they are still each other's negative in every frame of the walk.
  Geometry: vair gauges **STD 4x4 / THIN 3x4 / TINY 2x4** (2x2 would be the CHEQUY control, so the
  smallest gauge is deliberately the smallest fur that is not one); division at an ODD offset, each
  side holding ≥25% of the component; the fur's phase chosen per component to bring the two
  tinctures closest to equal area AS PAINTED ON THAT BODY (ninth appearance of the adaptive-boundary
  lesson, first time applied to AREA); relief = a pixel takes its own tincture's shade tone iff the
  pixel above is the other tincture — applied to BOTH tinctures identically, because a light that
  favours one of them answers the question the axis exists to leave open. Generator
  `scripts/gen_counterchange_axis59.py` (repaint-only, QA-safe by construction; self-contained
  `label4()`, no scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line,
  fifteenth generator to do so after axes 45-58; carries `--cells`, `--accept`, `--swatch`,
  `--sweep`).
  **Acceptance test — a NEW KIND: an ANTISYMMETRY, by CENSUS OF THE GROUP.** Every previous axis is
  accepted on a statistic (46/48/50/52/53), a topology (54), the algebra of an order (55), a
  conservation law along a traversal (56), a physical law (57) or a group action on one element
  (58). Here every candidate operation — translations in a window, every odd-offset per-fess and
  per-pale reflection — is sorted into SYMMETRY / ANTISYMMETRY / neither on the PAINTED tincture,
  read back off the pixels by nearest palette stop and blind to tone. (1) **ANTISYMMETRIC** the fold
  is an antisymmetry at every supported pixel — the SAME control (identical fur, gauge, phase,
  palette, pixel counts, fold removed) fails here. (2) **DIVIDED FUR** both tinctures occur on BOTH
  sides — the PLAIN control (a bare party per fess) fails here, and it is the sharpest near miss
  because it passes clause 1 perfectly. (3) **SOLITARY** the fold is the ONLY antisymmetry — the
  CHEQUY control fails here with 139. (4) **NEITHER IS THE GROUND** the two tinctures are within 15%
  of equal area — UNIFORM fails here.
  **ORDINARY SYMMETRIES ARE MEASURED AND REPORTED, NOT FORBIDDEN, and the first draft had that
  wrong.** Clause 2 originally read "nothing at all is an ordinary symmetry", which is incoherent: a
  periodic ornament has translation symmetries by definition and so does every one of the 58. What
  is true and better: this piece has ordinary symmetries exactly like its predecessors, AND one
  operation none of them has, which no motion can supply. Reported the way the 56th reports LOCK,
  the 57th LINEAR and the 58th MIRROR.
  **Result: 985 components across all 24 sheets × 60 active frames — 729 FOLDED (603 per pale / 126
  per fess, clauses 1-3) and 256 PAIRED (the boots and a few walk-frame legs, held to the pair
  clause); 84 lone small components reported; 39,201 metal / 39,244 colour pixels, imbalance 0.0005;
  0 clause violations.** Gauges: std 632 / thin 353.
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…58 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_counterchange_legendary_preview/`,
  `_counterchange_legs_preview/`, `_counterchange_boots_preview/`, `_cchangedome_helmet_preview/`.
  Previews: `_PREVIEW_counterchange_legendary.png`, `_PREVIEW_counterchange_legs.png`,
  `_PREVIEW_counterchange_boots.png`, `_PREVIEW_cchangedome_helmet.png` (built by
  `scripts/preview_axis59.py`); zooms `_ZOOM_counterchange_chest.png`,
  `_ZOOM_counterchange_head.png` and **`_ZOOM_counterchange_fold.png` — THE CLAUSE DRAWN**: the same
  chest four times, as it is / folded / palette-swapped / both, where cell 4 is cell 1 pixel for
  pixel and neither cell 2 nor cell 3 is, checked in code on the panel itself over 98 witnessed
  pixels. **That panel is drawn on TINCTURE ONLY, flat, with no relief and no edge tone, and that is
  not a simplification for the viewer — the first version used the finished pixels and cell 4 came
  back unequal on 37 of 135, because the shade is cast by a light from above that a fold turns over.
  The tone is not part of the ornament; the test is blind to it and so must the panel be.**
  Diagnostics `_diag_cchange_swatch.png`, `_diag_cchange_sweep.png` (gauge sweep plus the SAME,
  CHEQUY, PLAIN and UNIFORM controls on a real torso and leg), `_diag_cchange_slots.png`,
  `_diag_cchange_visor.png`.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L61** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **58th net-new-geometry axis — VORTICE (counter-handed S-scrolls), all 4 slots**
  (2026-08-08): the armour carries a field of small S-scrolls. Two arms leave each hub, one above it
  and one below it, and they are thrown to OPPOSITE SIDES of it; each ends in a volute curling one
  pixel further outward. So a scroll has a HAND — and the scrolls next to it always have the other
  one. No two scrolls sharing an edge of the lattice are ever the same hand, anywhere on the piece.
  **THIS IS THE FIRST AXIS WHOSE ELEMENT IS CHIRAL.** The 57th was the first axis with an UP; this is
  the same discovery made about the OTHER reflection, and a strictly harder one, because a mirror is
  not a rotation and cannot be undone by turning the piece in your hands. Hold any of the fifty-seven
  up to a looking-glass and it comes back itself: a honeycomb is a honeycomb, the 54th's wire has the
  same route, the 55th's bands the same order, the 57th's chains hang exactly as they hung. Every one
  of those motifs is either mirror-symmetric outright or its mirror is one of its own rotations —
  which is the same thing as far as a piece of armour is concerned, since you can turn it round and
  it is the motif again. The scroll cannot be turned back. Its mirror is a SECOND OBJECT, it is on
  the piece too, and the relation between the two of them is the ornament. The subject is therefore a
  property an element can have that **has no number attached to it** — no size, no pitch, no angle,
  no depth, nothing that can be more or less. A scroll is one hand or the other and the piece is
  organised by which.
  **AND THE TWO HANDS ARE THE SAME COLOUR** — the single most important decision in the file. Paint
  the right-handed scrolls in one metal and the left-handed ones in another and this becomes the 26th
  TARTAN wearing a scroll: an axis of two COLOURS on a lattice with the chirality riding on top. One
  palette, one metal, one light; the only thing telling a scroll from its neighbour is FORM.
  Every near miss fails on something checkable by exhausting the rotation group. The **16th TWILL**
  (herringbone) is the reflex answer since it alternates two mirrored dash families band by band, and
  it fails on the definition: a dash is not chiral, because the mirror of "/" is "\", and "\" is "/"
  rotated a quarter turn — herringbone has two ORIENTATIONS, not two hands. The **44th ZIGZAG** is
  the sharpest VISUAL near miss (alternating S and Z bars at 13px is what a chevron field looks like
  from across the room) and fails the same way: a chevron is symmetric about its own vertex, and on
  the sheet its two limbs MEET where a scroll's two arms pass either side of the hub. The **24th
  SPIRAL** is the sharpest near miss on the other clause because a spiral genuinely IS chiral — but
  every spiral there winds the same way, so the handedness is a global constant nobody on the piece
  can see and mirroring the sheet gives the 24th back unchanged; that is the UNIFORM control exactly.
  **23rd MEANDER / 30th CABLE** — one fret, one braid, one hand, constant. **40th DENTIL / 8th
  SIDE-STRIPE** — brackets thrown all the same way off a spine, which is the ALIGNED control. **42nd
  STRIGIL / 11th FLUTING** — what this collapses into at pitch 5. **35th/36th/39th/45th/48th** — all
  cells with their own mirror line. **55th STRATA** is the closest "relation between neighbours" and
  its relation is an ORDER (transitive, antisymmetric, one global sequence) where this is an
  ALTERNATION (symmetric, irreflexive, a 2-COLOURING — no first, no last, and swapping the two
  colours changes nothing). **53rd GRANULATION / 47th MOKUME** determine a SCALAR, and a scalar has
  no hands.
  **THE FIRST MOTIF WAS THROWN OUT ON SIGHT AND THAT IS THE MOST IMPORTANT LESSON IN THE BATCH.** The
  obvious chiral element at this scale is a four-armed pinwheel — hub, four cardinal arms, a one-pixel
  hook at each end turning the same way. It is chiral, it passed all four clauses, it tiled, and
  rendered at 26x on the hands panel it is unmistakably a SWASTIKA. No palette, pitch or arm length
  fixes that, because the glyph IS a four-armed hooked cross; geometric correctness is not a defence.
  **Four arms are out of this set permanently.** What replaced it is better anyway: TWO arms offset
  either side of the hub — the running scroll of every cornice, the S and Z of the S/Z tetromino —
  and it relocates the hand from a ROTATION to an OFFSET, which changes the controls. Unbending the
  volutes does NOT kill it (a bare Z-bar is still chiral), so the control is not "straighten" but
  **ALIGNED**: throw both arms the same side, the element gains a mirror line through its hub, and it
  has no hand at all — with the pixel count, pitch, palette and lattice untouched. The volutes are
  what make the hand LEGIBLE at 13px; the offset is what makes it EXIST.
  Geometry, per connected component: hubs on a square lattice of **PITCH 6**, phase chosen per
  component from a ladder; scroll = hub + two arms of **ARM 2** each ending in a volute (9px in a 5x5
  box); hand = parity of i+j, so the alternation is a proper 2-colouring of the checkerboard graph; a
  scroll is set only if EVERY pixel of it lands on the piece, because a clipped scroll does not have
  a smaller hand, it has NO hand; SHADE one row under every scroll pixel. Gauges **STD** (arm 2 with
  volutes, pitch 6) / **THIN** (arm 1, volutes dropped, 5px, pitch 4 — and dropping them is not a
  compromise, it is what the ALIGNED control proves: the hand lives in the offset) / **TINY** (the
  **minimal chiral polyomino**, the 4px S/Z tetromino in a 2x3 box — three pixels cannot do it, since
  every triomino's mirror is one of its own rotations, and the L-triomino is the trap because it
  LOOKS bent). PITCH > 2*radius asserted at import: breaking it fuses neighbouring scrolls silently
  and the sheet still passes sprite_qa while no longer being this axis.
  **THREE RENDER-PAID LESSONS.** (1) *The gauge is chosen by whether BOTH HANDS fit, not by whether
  anything fits.* Dropping to the next gauge only when the current one placed NO scroll left a
  chausse leg and a 16px boot each holding EXACTLY ONE standard scroll — one pinwheel at the hip and
  bare enamel below, i.e. a NAMED MEDALLION IN A FIXED PLACE (the 8th AEGIS ROUNDEL), and worse, one
  hand and therefore no alternation. One scroll is not a small amount of this axis, it is NONE of it,
  because the axis is a RELATION BETWEEN TWO SCROLLS. The leg drops to THIN and carries four.
  (2) *When a component can hold only one scroll, its neighbour is the OTHER COMPONENT* — the boots.
  The lattice parity is offset by the component's rank from the left, so the left boot and the right
  boot counter-turn; ordered by CENTROID and not by label id, because label order is raster-scan
  order and would swap the pair mid-stride in a walk cycle. This is the 57th's PENDANT move and
  arguably stronger: not a reduced element but THE SAME RELATION READ ONE SCALE UP. Eighth appearance
  of the adaptive-boundary lesson (52nd MARGIN_MIN → 57th THIN/TINY). (3) *A diagnostic that does not
  build its frame the way the generator does is worse than no diagnostic* — `visor_diag` handed
  `finish_array` a 70-frame array with ONE frame in it and came back with a pale dome and half-eaten
  slits while the sheet it was vouching for was correct, twice, through two rounds of chasing the
  difference. It now calls `build()` on the whole sheet.
  Palette — SIX stops per class (hub / hook / spoke / shade / field / deep), metal on **ENAMEL**
  (harder and glassier than the 57th's textile, more saturated than the 54-56 hides), and no class
  wears the metal it wore in 54-57: warrior **COPPER** on deep teal, mage **PALE JADE** on warm
  umber, ranger **PEWTER** on burnt sienna. The HOOK is deliberately NOT the brightest stop — putting
  the brightest tone on the pixel that carries the axis reads as loose sparks orbiting a dot and the
  volutes separate from their own arms; HUB brightest, HOOK one step down, SPOKE below that, so the
  arm brightens toward its end and TURNS. The warrior hub was first (247,214,186) and **that is a
  face** — copper's highlight desaturates toward tan exactly the way lit skin does (the 47th's
  lesson), so it was pulled back to a saturated (240,178,128). No stop near black: darkest stops
  clear channel-sum 150 (warrior 162, mage 150, ranger 158) and the dome's `great` visor reads clean
  through the scrolls in `_diag_vortice_visor.png`.
  Slots: chest Cuirass `shirt_%s_legendary58`, legs Chausses `pants_%s_legendary58`, boots Sabatons
  `boots_%s_legendary_vortice`, helmet Helm `helmet_%s_legendary58`. Generator
  `scripts/gen_vortice_axis58.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, so the silhouette never changes; self-contained NumPy
  `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line,
  fourteenth generator to do so after axes 45-57; carries `--cells`, `--accept`, `--swatch` and
  `--sweep`).
  **Acceptance test — a NEW KIND: a GROUP ACTION.** Every previous axis is accepted on a STATISTIC of
  its field (46th, 48th, 50th, 52nd, 53rd), on its TOPOLOGY (54th), on the ALGEBRA of an order (55th),
  on a CONSERVATION LAW along a traversal (56th) or on a PHYSICAL LAW (57th). Chirality is not a
  quantity — it is a fact about a SYMMETRY GROUP — so this one is accepted by exhausting that group
  on the pixels. (1) **CHIRAL**: the motif's mirror is none of its four rotations — four set
  comparisons, and the clause that separates it from herringbone. (2) **READABLE**: every scroll on
  the piece matches some rotation of exactly ONE of the two hands (clause 1 is what makes this well
  defined — a scroll cannot be both, and the reader cannot quietly pick one); a clipped, fused or
  overpainted scroll matches neither and is a violation. (3) **ALTERNATION**: no two lattice-adjacent
  scrolls share a hand, verified on the hands that were READ off the painted pixels and never on the
  parity they were painted from. (4) **BOTH HANDS**, over a sheet.
  **Result: 985 components across all 24 sheets × 60 active frames, 2282 scrolls set, 1155 right /
  1127 left read off the pixels, 0 components left bare, 0 clause violations.** Gauges in use: std
  431 / thin 432 / tiny 122. Controls: ALIGNED fails CHIRAL on every component; UNIFORM fails
  ALTERNATION. **MIRROR is reported as a MEASUREMENT and PASSES, and that is the most interesting
  result in the file** — the way the 56th reports LOCK and the 57th reports LINEAR. The obvious fifth
  clause would be the 57th's FLIP written for a mirror: reflect the sheet and demand failure. It does
  not fail and it should not. Reflecting the field turns every right hand into a left and every left
  into a right, so all four clauses still hold exactly, and the honest statement is: **every element
  of this field is chiral, and the field is not.** The alternation is an ACHIRAL STRUCTURE ASSEMBLED
  OUT OF CHIRAL PARTS — which is precisely what separates it from the 24th SPIRAL, where a global
  handedness is a handedness nobody on the piece can see. Here both hands are present at every point,
  each is the other's evidence, and what the mirror does is exchange two things already there.
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…57 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_vortice_legendary_preview/`,
  `_vortice_legs_preview/`, `_vortice_boots_preview/`, `_vorticedome_helmet_preview/`.
  Previews: `_PREVIEW_vortice_legendary.png`, `_PREVIEW_vortice_legs.png`,
  `_PREVIEW_vortice_boots.png`, `_PREVIEW_vorticedome_helmet.png` (built by
  `scripts/preview_axis58.py`); zooms `_ZOOM_vortice_chest.png`, `_ZOOM_vortice_head.png` and
  **`_ZOOM_vortice_hands.png` — clause 1 DRAWN**: the right-handed scroll and its four quarter-turns
  beside its MIRROR, at a size where "the mirror is not any of them" can be checked by eye in two
  seconds; diagnostics `_diag_vortice_swatch.png`, `_diag_vortice_sweep.png` (pitch sweep plus the
  ALIGNED, UNIFORM and MIRROR controls on a real torso and leg), `_diag_vortice_slots.png` and
  `_diag_vortice_visor.png`.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L60** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **57th net-new-geometry axis — FESTOON (hanging swags, sag set by span), all 4 slots**
  (2026-08-08): the armour carries chains hung between studded anchors, and every one of them SAGS.
  The sag is not a style, it is a consequence: a chain hung between two points that are further
  apart hangs deeper, so a wide chain across the shoulders bellies well below its studs while the
  short one at the waist barely dips. The shadow under each chain WIDENS at its belly, where the
  chain hangs slackest and therefore stands furthest off the plate — the same fact stated a second,
  independent way. Nothing on this piece is laid out; everything on it is HUNG.
  **THIS IS THE FIRST AXIS THAT HAS AN UP.** Turn any of the fifty-six a half-turn and the ornament
  is intact: a honeycomb is the same honeycomb, the 54th's wire has the same route, the 55th's bands
  the same order, the 56th's straps go through the same holes. What changes is the LIGHTING and only
  the lighting — every prior axis is a GEOMETRY invariant under a half-turn wearing a lit flank that
  is not, and every one of them could be worn upside down. This one cannot. Turned over, the chains
  ARCH off their studs and hold themselves there with nothing in the picture holding them, so the
  picture is simply wrong. The subject is not the elements, nor how they relate, nor the order they
  were laid in, nor which side of the surface they are on: it is that the ornament is **subject to a
  force that comes from outside it**, and the whole field records the direction of that force.
  Every near miss fails on something COUNTED. The **34th SEIGAIHA** is the reflex answer since it is
  a field of arcs — its arcs are CONGRUENT and stamped on a half-drop LATTICE, where here no two
  chains of different span are congruent and an anchor sits where the BODY's own edge at that row
  puts it, so the piece's width chooses the span and the span chooses the sag; the UNIFORM control
  IS the 34th (hold sag constant, change nothing else, and every arc is still there and the axis is
  gone). The **22nd WAVE** is the sharpest formal near miss because a sine is exactly what a festoon
  is not: symmetric about its own midline, hence its own half-turn, crests and troughs
  interchangeable — a festoon has round bellies pointing down and sharp cusps pointing UP, so a
  viewer can read which way is up off the ornament alone. The **15th SCALE / 31st OGEE** are curved
  cells, congruent, on a lattice, orientation-free. The **41st BEAD-AND-REEL / 30th CABLE** are
  genuinely threaded strings and both STRAIGHT and PERIODIC — their route is two numbers and does
  not know where it is on the body. The **53rd GRANULATION** is the closest "size is an output" and
  fails twice over: its output is a SCALAR read off the local distance transform and its beads are
  SIMILAR (a big bead is a small one scaled), where here the output is a CURVE and the determining
  quantity is the SPAN BETWEEN TWO ANCHORS, not the room at a point. The **47th MOKUME** is
  shape-conformal but its tone is a function of distance-to-edge, a scalar field with no direction
  in it at all. The **8th SIDE-STRIPE / 10th CROSS / 12th BANDED-LAMELLAR** are straight members
  between two points, and the TAUT control lands precisely there: same anchors, same count, same
  palette, zero sag, straps again. The **7th LACE-BOOTS / 6th BALDRIC** are named accessories.
  Geometry, per connected component: tiers every **TIER_P 7** rows, first at an OFFSET chosen per
  component from a ladder; on a tier row the component's own opaque run, inset 1px, divided into
  `round(L / SPAN_TARGET 9)` chains so a wide row carries more and a narrow row fewer; each chain a
  shallow catenary `y = y0 + SAG*(1-u²)` with **SAG = clamp(round(span²/20), 1, 4)** — the span
  SQUARED, which is the shallow-catenary law; LIP above, a 1px core SHADE below, and CAST, a second
  shadow row under the belly only. A chain is hung only if EVERY pixel of its curve lands on the
  piece.
  **SIX TUNING LESSONS, all six paid for on a render or a measurement rather than argued:**
  (1) *A constant tuned on the test plate is not a constant that survives the armour.* SAG_DEN 32
  was set on the 30px synthetic plate, which affords spans of 7–12. A 13px torso's inset run is 4–9,
  so every chain on every real slot came out at sag 1 and the span law had nothing to say. SAG_DEN
  20 puts the interesting part of the curve inside the range the bodies actually offer.
  (2) *Score the offset ladder on TOTAL SAG, not on chain count.* Scoring on count picks the offset
  whose tiers land where the body is NARROWEST — a narrow run still splits into one chain while a
  wide run can lose its chain entirely to the completeness rule — so the ladder systematically chose
  the shallowest reading of every piece. Total sag asks the opposite question: where can a chain
  actually be seen to hang? Count survives as the tie-break. Sixth appearance of the adaptive-
  boundary lesson (52nd MARGIN_MIN, 53rd shot pass, 54th adaptive pitch, 55th spread, 56th phase).
  (3) *MIN_SPAN 4 left every piece 80% bare, and that is the 6th BALDRIC.* At a 4px minimum the
  generator hung exactly ONE chain on a torso, a leg, a boot and a dome — a handsome necklace and a
  NAMED ACCESSORY IN A FIXED PLACE, which this set already has four times. A torso is 13px at the
  shoulders and 6px at the waist, so with the 1px inset every tier below the first was silently
  dropped. At MIN_SPAN 3 the waist carries a short shallow chain and the shoulders a long deep one,
  and THAT PAIR IS THE AXIS: two chains on one piece, different because the body under them is.
  (4) *The anchor inset is a preference, not a rule.* A single chausse leg is FOUR pixels across;
  inset it and nothing is left to hang anything between, so the legs slot came out as one chain at
  the waist and two bare legs below — the 7th SWORD-BELT. Where the inset leaves no room the studs
  go on the edge instead, which is what a real chain mount looks like at that size anyway.
  (5) *TIER_P >= SAG_MAX + 3 is a clearance, not a taste, and it is now ASSERTED at import.* The
  TINY rhythm was first written with tier pitch 4 against a max sag of 2, which leaves a belly and
  the studs below it TWO rows apart: the chains fuse into one continuous zigzag — the 44th ZIGZAG,
  precisely the axis this one must not collapse into — and the acceptance test then traced one chain
  onto the other and called the second taut. 65 failures, all on 30px boots, all from that slip.
  (6) *A chain is a connected thing and must be READ as one.* The reader first scanned a band of
  rows around the tier line; a deep swag comes within TIER_P − SAG_MAX = 3 rows of the tier above,
  so the scan picked up the neighbouring chain and failed correct sheets. No band width works — the
  fix is to TRACE from the stud, which is also what a viewer's eye does. Its tie-break matters too:
  "ties downward, because a chain hangs" is true of a chain and false of a reader, since on the
  CLIMBING half the correct next pixel is one row UP.
  Palette — **SIX** stops per class (boss / lip / link / shade / cast / field) and the **FIRST
  PALETTE IN THE SERIES WITH TWO SHADOW STOPS**: the 55th's lesson said a shadow landing on two
  MATERIALS needs two tones; this is the same lesson for a different reason — the shadow lands on
  one material and changes its WIDTH. Axes 52–56 are all metal on metal or hide; this one is metal
  on **TEXTILE**, so the fields are saturated and chromatic rather than neutral — warrior GOLD on
  CRIMSON velvet, mage MOON SILVER on MIDNIGHT SEA-BLUE, ranger VERDIGRIS BRONZE on MULBERRY-PLUM
  (the one complementary pair in the series). Three different metals, none of them the metal that
  class wore in 54–56. No stop near black: every class's darkest stop clears channel-sum 150
  (warrior 154, mage 170, ranger 158) and the warrior dome's `great` visor reads clean through the
  chains in `_diag_festoon_visor.png`.
  Slots: chest Cuirass `shirt_%s_legendary57`, legs Chausses `pants_%s_legendary57`, boots Sabatons
  `boots_%s_legendary_festoon`, helmet Helm `helmet_%s_legendary57`. Generator
  `scripts/gen_festoon_axis57.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, so the silhouette never changes; self-contained
  NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()`
  in-line, thirteenth generator to do so after axes 45–56; carries `--cells` for an ASCII dump plus
  the EQUILIBRIUM acceptance test and the four controls, `--accept` for that test over every
  component of every frame, `--swatch` for the bare motif on a synthetic notched/waisted test plate,
  and `--sweep` for the tier/span sweep plus the FLIP, TAUT, UNIFORM and LINEAR controls on a real
  torso AND a real leg).
  **Acceptance test — a NEW KIND.** Every previous axis is accepted on a STATISTIC of its field
  (46th cell count, 48th size ratio, 50th glyph survival, 52nd distinct-hole appearances, 53rd
  radius histogram), on its TOPOLOGY (54th), on the ALGEBRA of a relation (55th) or on a
  CONSERVATION LAW along a traversal (56th) — all of them facts about the ornament ALONE. This
  axis's content is a relation between the ornament and something OUTSIDE it, so it is accepted on a
  **PHYSICAL LAW: does this thing hang?** (1) PENDENCY — every chain's lowest point is strictly
  below both of its own studs; (2) SINGLE BELLY — traced stud to stud it descends then climbs, one
  minimum, no inflection; (3) THE SPAN LAW — no chain on a piece hangs shallower than a narrower
  one, and across the batch at least two distinct sags occur, so the sags are ORDERED BY SPAN and
  not all the same. Every quantity is TRACED off the painted pixels, never taken from the formula.
  **Result: 985 components across all 24 sheets × 60 active frames, 1765 chains hung, mean read sag
  1.54px, 0 pendency/belly failures, 0 span-law inversions, 0 components left bare.** Controls: FLIP
  fails pendency at every chain — **the first control in the series that IS the axis's own output,
  transformed**, which is only possible because it is the first axis a transform can break; TAUT
  fails at every chain (51/51 on the case set); UNIFORM passes pendency and fails NOT CONGRUENT.
  **LINEAR is reported as a MEASUREMENT and not asserted**, the way the 56th reports LOCK: with sag
  an integer 1–4 over the span range a 13px body affords, a square law and a linear one round onto
  nearly the same values, so the raster confirms that the sags are ordered and non-uniform but
  cannot separate the square from a proportion. The intended "NOT SIMILAR" clause was cut for
  exactly this reason — stated pairwise it fails correct sheets on rounding alone (spans 4 and 5
  both round to sag 1, ratios 0.25 and 0.20).
  Two more measured facts. The span law is stated **within one rhythm**: run naively over the batch
  it reported 44,969 inversions on sheets in which every component was individually correct, because
  a 3px boot runs the TINY rhythm at SAG_DEN 6 while a torso runs STD at 20 — a different GAUGE of
  chain, the way a watch chain and an anchor chain both obey the physics while neither predicts the
  other's sag. And 42 of 985 components — always ONE BOOT OF A PAIR, a 12–17px L-shaped blob four
  pixels across — can hang no swag at any offset under any rhythm, since a swag needs its belly to
  land on the piece. Leaving them flat is the 54th's measured failure (one leg wired, the other
  blank) and worse here because the two boots sit side by side in every frame, so they get the
  **PENDANT**: a chain hung from two studs that COINCIDE, which hangs straight down. Not a second
  element bolted on — this axis's own element at span 0, and the purest statement it has, since a
  plumb line is gravity and nothing else.
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…56 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_festoon_legendary_preview/`,
  `_festoon_legs_preview/`, `_festoon_boots_preview/`, `_festoondome_helmet_preview/`.
  Previews: `_PREVIEW_festoon_legendary.png`, `_PREVIEW_festoon_legs.png`,
  `_PREVIEW_festoon_boots.png`, `_PREVIEW_festoondome_helmet.png` (built by
  `scripts/preview_axis57.py`); zooms `_ZOOM_festoon_chest.png`, `_ZOOM_festoon_head.png`;
  diagnostics `_diag_festoon_swatch.png` (bare motif, all 3 classes), `_diag_festoon_sweep.png`
  (tier/span sweep plus the FLIP, TAUT, UNIFORM and LINEAR controls on a real torso and leg),
  `_diag_festoon_slots.png` (all 3 classes × all 4 slots, bare motif, no finishing pass) and
  `_diag_festoon_visor.png` (the warrior dome's black eye and mouth slits reading clean through the
  chains, m + f).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L59** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **56th net-new-geometry axis — SLOTWORK (straps threaded through the plate), all 4 slots**
  (2026-08-08): a few parallel straps run across the piece at 45 degrees, and each one disappears
  into a SLOT cut in the plate, passes behind it for two or three pixels, and comes back out through
  a second slot on the same line. Its cast shadow is present under it where it is in front and
  absent in the gap, so the shadow's own ends mark the two openings a second time. The straps never
  cross one another and never touch.
  **THIS IS THE FIRST AXIS IN WHICH THE GROUND IS AN OCCLUDER.** In all fifty-five prior axes the
  field is passive: something is ON it — a cell, a member, a bead, a wire, a pile of bands — and the
  field's whole job is to be the thing that is not the ornament. Even the two axes that make depth
  their subject leave the field out of it. The 52nd AJOURE has two surfaces, but the plate is in
  front and the liner is behind, everywhere, always; the 55th STRATA piles bands on one another and
  the plate under them is never over anything. Here the plate CHANGES ITS RELATION TO THE STRAP
  ALONG THE STRAP'S OWN LENGTH — in front here, behind there — so the subject is not the member's
  route (54th) and not the order the members were laid in (55th), it is that the surface has two
  sides and the strap uses both. Nothing in the fifty-five can be said to have a BACK.
  The consequence is a law the ornament must obey and can be checked against: **A STRAP MAY NOT
  LEAVE THE SURFACE EXCEPT THROUGH A HOLE.**
  Every near miss fails on something COUNTED. The **30th CABLE / 39th GUILLOCHE** are the reflex
  answer since a strand there also goes under — it goes under ANOTHER STRAND, two members of the
  same kind taking turns, with no opening anywhere on the piece (slot count 0 vs 3-6 here) and here
  the straps never cross at all. The **52nd AJOURE** is the closest thing in the set to a hole, but
  its piercings show a SURFACE, which has no route, no ends and no length, and its plate-over-liner
  relation is fixed everywhere; two fixed layers are not a threading. The **55th STRATA** also lays
  bands across the piece, but there the bands cross ONE ANOTHER; here they are strictly parallel by
  construction and the content is what happens where a strap meets the PLATE. The **54th LABYRINTH**
  is one member with a route that lies on top for its whole length — it is traceable precisely
  because it never leaves. The **12th BANDED-LAMELLAR / 40th DENTIL** are the failure mode this axis
  falls into if the rhythm is mistuned: rows of separate objects with no evidence that the gaps
  contain anything, and that evidence is exactly the slot (the NOSLOT control fails the conservation
  law at every transition it has). The **8th SIDE-STRIPE / 6th BALDRIC / 10th CROSS / 7th LACE** are
  uninterrupted straps or a fixed named accessory — the OVER control IS the 8th side-stripe, with
  the geometry completely unchanged and the axis gone.
  Geometry, per connected component: straps every PITCH 5 px along the normal, footprint LIP 1 +
  FACE 2 with a 1px cast SHADOW on the dark flank; along the strap a period of VIS 8 in front,
  SLOT, KEEP (the lit chamfer of the opening), HID 3 behind, SLOT; staggered PHASE_STEP 4 per strap;
  the along-phase chosen per component from a ladder.
  **FOUR TUNING LESSONS, all four paid for on a render rather than argued:**
  (1) *A shallow angle is not a strap, it is camouflage.* The first cut ran the straps 20 degrees off
  horizontal, which rasterises into staircase treads of unequal length — the strap's own edge is
  already broken before the slots break it, and the eye has nothing to follow. At **45 degrees** the
  raster is exact, one step across per step along, so the strap is a clean unbroken diagonal and
  EVERY break in it is one the ornament put there.
  (2) *The interruption must be the exception, not the rhythm.* At VIS 5 the strap is interrupted as
  often as it is present, and at 13px a dashed line does not read as one thing seen intermittently,
  it reads as a scatter of separate blobs (the 13th STUDWORK / 40th DENTIL). **VIS 8** against a 3px
  width gives a strap that is mostly THERE and goes under once — so the element is not a mark, it is
  an EVENT, and a 13px silhouette affords 1 to 3 of them.
  (3) *The occluder must be the majority material, and that is a measurement, not a taste.* PITCH 4
  is denser and looks better at first glance, but measures plate 41-44% against strap 41-50%: the
  occluder becomes the minority, there is no plate left between one strap and the next for them to
  be threaded THROUGH, and it reads as the 12th BANDED-LAMELLAR. **PITCH 5** measures plate 53-61%.
  (4) *High contrast is what turned the first cut into camouflage, and the fix is hue.* A near-white
  strap over a luminance-100 plate is a clean read on the 44px test plate and a mottle on the real
  13px torso: a 3px pale strap is a quarter of the width of the piece, so at high contrast it stops
  being LINE-WORK and becomes a SHAPE. The straps are now separated from the plate by HUE (cool
  steel against warm hide) with a small luminance step, the single brightest note being the 1px lip.
  Same principle as the 52nd's "hue not luminance at 13px", opposite reason: not that the eye cannot
  resolve the step, but that it resolves it too well.
  Palette — **SIX** stops per class (slot / keep / lip / face / shade / plate) and **THE FIRST SET IN
  THE SERIES WITH NO "DEEP" STOP**: every previous palette needed a second darker field tone for the
  part of the piece the ornament does not reach, but here the plate is not a background, it is the
  OCCLUDER — the active half of the only relation the axis has — so no part of it is uninvolved.
  Warrior burnished STEEL straps through a dark WALNUT hide plate; mage ICE-BLUE through AUBERGINE;
  ranger cool BONE through PEAT-GREEN. A dark majority on purpose, since the 55th is the one
  pale-majority tier and the two sit side by side in the grid; and a HIDE plate in all three classes,
  which no prior tier has. SLOT is the darkest stop in each class and **the first time the defining
  element of an axis is DARK**, which collides head-on with the helmet visor rule — resolved by hue,
  the slot being a desaturated cool tone against a warm plate, with every class's darkest stop
  clearing channel-sum 150 (warrior 154, mage 162, ranger 152) and the warrior dome's `grille`
  slits reading clean through the slots in `_diag_slotwork_visor.png`.
  Slots: chest Cuirass `shirt_%s_legendary56`, legs Chausses `pants_%s_legendary56`, boots Sabatons
  `boots_%s_legendary_slotwork`, helmet Helm `helmet_%s_legendary56`. Generator
  `scripts/gen_slotwork_axis56.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, so the silhouette never changes; self-contained
  NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()`
  in-line, twelfth generator to do so after axes 45-55; carries `--cells` for an ASCII dump plus the
  conservation acceptance test and the three controls, `--accept` for that test over every component
  of every frame, `--swatch` for the bare motif on a synthetic notched/waisted test plate, and
  `--sweep` for the pitch/width sweep plus the NOSLOT, OVER and LOCK controls on a real torso AND a
  real leg).
  **Acceptance test — a NEW KIND.** Every previous axis is accepted on a STATISTIC of its field (the
  46th's cell count, 48th's size ratio, 50th's glyph survival, 52nd's distinct-hole appearances,
  53rd's radius histogram), on its TOPOLOGY (54th) or on the ALGEBRA of a relation (55th). This
  axis's content is a THING THAT HAPPENS ALONG A LENGTH, so it is accepted on a **CONSERVATION LAW
  READ OFF A TRAVERSAL**: walk each strap and classify each step from the painted pixels as IN
  FRONT, IN A HOLE or GONE, then require that no in-front/behind transition happens without a slot
  between them, that no slot has the same thing on both sides of it, and that every component with
  the room shows at least one COMPLETE event (strap | hole | plate | hole | strap) while every
  component without the room still shows a witnessed opening. **Result: 985 components across all 24
  sheets × 60 active frames, 3166 straps, 4237 witnessed openings, 1262 complete events, 186
  components too small for one, 0 failures.** The NOSLOT control fails at every transition it has;
  the OVER control passes the law trivially and shows 0 events, which is the point — it is the 8th
  side-stripe. The phase ladder is doing real work: **at a fixed phase, 533 of 985 components show
  no complete event at all.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…55 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_slotwork_legendary_preview/`,
  `_slotwork_legs_preview/`, `_slotwork_boots_preview/`, `_slotdome_helmet_preview/`.
  Previews: `_PREVIEW_slotwork_legendary.png`, `_PREVIEW_slotwork_legs.png`,
  `_PREVIEW_slotwork_boots.png`, `_PREVIEW_slotdome_helmet.png` (built by
  `scripts/preview_axis56.py`); zooms `_ZOOM_slotwork_chest.png`, `_ZOOM_slotwork_head.png`;
  diagnostics `_diag_slotwork_swatch.png` (bare motif, all 3 classes), `_diag_slotwork_sweep.png`
  (pitch/width sweep plus the NOSLOT, OVER and LOCK controls on a real torso and leg),
  `_diag_slotwork_slots.png` (all 3 classes × all 4 slots, bare motif, no finishing pass) and
  `_diag_slotwork_visor.png` (the warrior dome's black eye and mouth slits reading clean through the
  straps and slots, m + f).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L58** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **55th net-new-geometry axis — STRATA (lap-jointed bands in a readable order), all 4 slots**
  (2026-08-08): the armour is built up out of a handful of broad straight bands laid ACROSS the
  piece at different angles, one after another. Each new band passes OVER every band already there
  and casts a hard shadow onto it, so at every crossing one band is whole and the other stops dead
  at its edge — and the same band wins every crossing it is in. Nothing is woven.
  **THIS IS THE FIRST AXIS WITH A TIME ORDER.** All fifty-four prior axes are SIMULTANEOUS: ask a
  honeycomb, a runic register, a granulated bead field or the 54th's single wire "which part of this
  was made first" and the ornament has no answer, because every one of them is a STATE and every
  part of it is as old as every other part. Here the whole content is a HISTORY. The elements are
  not related by position, size, descent, connectivity or size-from-shape; they are related by
  PRECEDENCE, which is a different kind of relation because it is transitive and antisymmetric. A
  viewer reads the piece pairwise — this band is severed by that one, so that one is later — and
  those local facts compose, with no contradiction, into ONE global sequence over the whole piece.
  It is the exact complement of the 54th, which is why it follows it: that axis is one member that
  never crosses itself and its subject is where the member GOES; this is several members whose only
  content is how they CROSS.
  Every near miss fails on something COUNTED. The **30th CABLE / 39th GUILLOCHE** are the first
  thing anyone will say and they are WEAVES: a strand goes over at one crossing and UNDER at the
  next, by definition, because that reciprocity is what makes a weave hold — so a weave's relation
  is inconsistent per pair and its precedence graph has a CYCLE. The **16th TWILL** and **18th
  BASKETWEAVE** fail identically at a smaller scale. The **26th TARTAN** is the sharpest near miss
  because its bands genuinely do just cross: what a sett does at a crossing is BLEND into a third,
  denser tone belonging to neither band, which is exactly what says NEITHER is on top; here no
  crossing ever produces a third tone. The **15th SCALE** has a z-order, but a POSITIONAL one — every
  scale laps the next in the same direction, all elements congruent, the "order" just a restatement
  of the lattice; here the members are not congruent, the order is not derivable from position, and
  it is GLOBAL. The **52nd AJOURE** occludes, but its plate-over-liner is a fixed PAIR in the same
  relation everywhere, and two is not an order. The **8th SIDE-STRIPE / 11th FLUTING / 42nd STRIGIL
  / 43rd GADROON / 44th ZIGZAG** are parallel families — parallel members never cross, so they have
  nothing to order.
  Geometry, per connected component: band count from area (3 on a torso, a dome and a thigh, 2 on a
  foot); band k takes `ANGLES[k]` from a fixed list whose smallest separation is 45° so no crossing
  is glancing; band k sits at `FRACS[k]` of the component's own extent along its own normal, with
  `FRACS[0] = 0.5` so the FIRST band laid runs through the middle and every later band has the best
  chance of crossing it; footprint is a 1px LIP on the lit flank plus a 2px FACE, with a 1px cast
  SHADOW immediately outside on the dark flank, painted onto whatever is under it at the time.
  **FOUR TUNING LESSONS, all four paid for on a render rather than argued:**
  (1) *A shadow that lands on two different materials needs two different stops, which is why the
  palette has SEVEN and not six.* A later band's shadow falling on an EARLIER BAND must be dark
  metal; the same shadow falling on bare plate must be dark plate. Give both one shared dark tone
  and the shadow stops reading as cast BY something ONTO something and starts reading as a third
  material — at which point the only depth cue the axis has is gone and so is the axis.
  (2) *Rivet only the TOP band.* The first cut riveted every band, which put six bright pips on a
  91px helmet dome, and a scatter of bright pips on a ground at this scale is not a set of
  fastenings, it is the **13th STUDWORK** showing through. Riveting only the band that is over
  everything gives exactly two pips per component and says something the axis wants said: the last
  strap laid is the one that pins the pile down.
  (3) *N=4 and N=5 are over-filled and collapse into an older axis.* Rendered at 20x on the real
  torso and dome, band coverage runs 71–74%, the plate survives only in the corners, and with no
  ground between them the bands stop reading as straps laid ON something and start reading as a
  mottle — the **12th BANDED-LAMELLAR** with the lames out of register. N=3 is the choice on every
  real slot (coverage ~55–65%, three crossings) and it is also exactly the smallest number that can
  carry an ORDER rather than a fixed pair. N=2 on a foot is honest but it is a PAIR, not a sequence.
  (4) *A constant tuned on the IDLE frame is not a constant that survives every POSE — and the fix
  is a ladder, not a smaller constant.* At a fixed band spread the acceptance test failed the
  TOTALITY clause on 25 of 985 components (the long thin leg in the run poses, the chest in the
  cheer poses, two female boot frames). Clamping every piece tighter piles all three bands into one
  knot in the middle and gives back the bare margin the 49th warned about, so the generator walks a
  ladder of spreads (0.60 → 0.40 → 0.22) and then, if the silhouette is a U — a torso with both arms
  RAISED, whose centroid falls in the GAP between the arms — continues downward through the band
  count itself (N−1, N−2, … 2). Fourth appearance of the same adaptive-boundary lesson after the
  52nd's MARGIN_MIN, the 53rd's shot pass and the 54th's adaptive pitch. Result: 0 of 985.
  Palette — seven stops per class (rivet / lip / face / bshade / plate / shade / deep), the first
  four on the BAND's ramp and the last three on the PLATE's. **DELIBERATE INVERSION: in all three
  classes the band is the DARK material and the plate is the PALE one.** Every recent tier is a
  bright figure on a dark field (52nd, 53rd, 54th all), so this one reads unmistakably different at
  1x in the inventory grid before any pattern resolves — and it serves the axis, because a dark
  band's cast shadow onto a pale plate is the strongest possible statement of the one relation the
  ornament exists to state. Warrior BLACKENED IRON with brass rivets on pale steel; mage AMETHYST
  with moon-white rivets on pale ash-lilac; ranger BOG-OAK GREEN with bone rivets on pale lichen.
  What carries at 1x is the majority hue, which here is the PLATE, and no prior tier in the set has
  a pale majority at all. DEEP sits only ONE step off PLATE — three steps down and the untouched
  corners read as stains rather than as plate the pile does not reach. No stop near pure black:
  every class's darkest stop clears channel-sum 150, verified on the warrior dome whose `great`
  visor reads clean through the bands.
  Slots: chest Cuirass `shirt_%s_legendary55`, legs Chausses `pants_%s_legendary55`, boots Sabatons
  `boots_%s_legendary_strata`, helmet Helm `helmet_%s_legendary55`. Generator
  `scripts/gen_strata_axis55.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, so the silhouette never changes; self-contained
  NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()`
  in-line, eleventh generator to do so after axes 45–54; carries `--cells` for an ASCII dump plus
  the ORDER acceptance test and the WEAVE control, `--swatch` for the bare motif on a synthetic
  notched/waisted test plate, and `--sweep` for the N=2/3/4/5 sweep plus the WEAVE, FLAT and W=3
  controls on a real torso AND a real leg).
  **Acceptance test — a NEW KIND.** Every previous axis is accepted on a STATISTIC of its field (the
  46th's cell count, 48th's size ratio, 50th's glyph survival, 52nd's distinct-hole appearances,
  53rd's radius histogram) or, in the 54th, on its TOPOLOGY. This axis's content is a RELATION, so
  it is accepted on the ALGEBRA of that relation, read back off the painted pixels rather than off
  the painting order: **CONSISTENT** (no pair resolves two ways), **ACYCLIC** (precedence is a real
  order, not an Escher staircase) and **TOTAL** (the crossings that actually exist on this
  silhouette are enough to chain every band into one unique sequence with no ties). **Result: 985
  components across all 24 sheets × 60 active frames, 2623 crossings read, 0 inconsistent, 0 cyclic,
  0 non-total.** The WEAVE control, run on the same torso, fails on the first clause and its rule —
  `1 over 0, 0 over 2, 2 over 1` — closes on itself, so there is no first band.
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…54 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_strata_legendary_preview/`,
  `_strata_legs_preview/`, `_strata_boots_preview/`, `_stratadome_helmet_preview/`.
  Previews: `_PREVIEW_strata_legendary.png`, `_PREVIEW_strata_legs.png`, `_PREVIEW_strata_boots.png`,
  `_PREVIEW_stratadome_helmet.png` (built by `scripts/preview_axis55.py`); zooms
  `_ZOOM_strata_chest.png`, `_ZOOM_strata_head.png`; diagnostics `_diag_strata_swatch.png` (bare
  motif, all 3 classes), `_diag_strata_sweep.png` (N=2/3/4/5 plus the WEAVE, FLAT and W=3 controls on
  a real torso and leg), `_diag_strata_nsweep.png` (N=2…5 zoomed on the real torso and dome — the
  frames the band-count decision was actually read off), `_diag_strata_slots.png` (all 3 classes ×
  all 4 slots, bare motif, no finishing pass) and `_diag_strata_visor.png` (the warrior dome's black
  eye and mouth slits reading clean through the bands, m + f).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L57** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **54th net-new-geometry axis — LABYRINTH (one continuous wire), all 4 slots** (2026-08-08): the
  armour carries no field of ornaments at all. It carries a SINGLE raised wire, soldered to an
  enamelled plate, which enters at one terminal bead, winds back and forth to visit every part of
  the piece, never once touches or crosses itself, and leaves at the other terminal bead.
  **THIS IS THE FIRST AXIS THAT IS ONE OBJECT.** All fifty-three prior axes are a PLURALITY: forty
  stamp a congruent cell on a lattice, ten run a congruent member along a track, and the recent ones
  break the cell's content (48th a hierarchy, 49th a descent, 50th a vocabulary), its carrier (46th
  aperiodic, 51st continuous), its depth (52nd two surfaces) or its size (53rd shape-determined) —
  but in every one of them you can point at MANY things and ask how they relate. Here you cannot.
  There is exactly one thing on the piece and the question it answers is not "how do the elements
  relate" but "WHERE DOES IT GO": its subject is CONNECTIVITY. The 53rd's granules number 11 on a
  torso and 4 on a boot; this axis's wires number ONE on the torso, ONE on each leg, ONE on each
  boot and ONE on the dome, and that is not a tuning outcome, it is the definition. A viewer can put
  a finger on a terminal bead and trace, and reach the other terminal having passed through every
  wire pixel on the piece. Nothing in the fifty-three can be traced, and connectedness is not a
  property you can add to a field by tuning it.
  Every near miss fails on something COUNTED rather than argued. The **23rd MEANDER** is the first
  thing anyone will say and it is a PERIODIC BAND — one congruent fret unit translated along a
  track, the whole itinerary stated by two numbers, cut it anywhere and you get the same ornament
  back; here every turn is decided by which parts of THIS silhouette the wire has not reached yet,
  no two turns are the same turn, and cutting it destroys the only property it has. The **49th
  DENDRITE** is the sharpest, since both are connected and acyclic: a dendrite is a TREE, this is a
  PATH, and a path is exactly a tree with no branching — branch points 0 vs dozens, endpoints
  exactly 2 vs many tips. The **NET axes** (14th lattice, 17th ashlar, 19th honeycomb, 20th trellis,
  21st chainmail, 33rd octagram) are connected too and are all CYCLE: a net is nothing but its
  loops, its cells are its subject; a path has loop count 0, encloses nothing, has no cells, and the
  space it winds through is ONE continuous corridor you could also trace. The **30th CABLE / 39th
  GUILLOCHE** need two strands and a crossing; one strand, self-avoiding, no over, no under. The
  **46th CRAQUELURE** is a partition with degree-3 junctions everywhere; this is degree ≤2
  everywhere. The **51st FLOWGRAIN** has infinitely many curves and its subject is their DIRECTION;
  here there is one curve and where it has BEEN is the whole content.
  Geometry, per connected component: `elig` = the component's INTERIOR if it has one, else the whole
  component; a node lattice at every PITCH-th row and column **phased to the component's CENTROID**
  (the 49th's lesson — a corner-phased lattice hugs one edge and leaves a bare band, i.e. an 8th
  side-stripe with texture beside it); nodes PITCH apart are adjacent when every pixel of the
  segment between them is eligible; the wire is the **longest SIMPLE path** through that graph
  (Warnsdorff greedy from every node as a start, then a deterministic BACKBITE — extend the endpoint
  if it can, else reverse the tail at a neighbour of the endpoint, which keeps the path simple and
  the same length but hands it a different endpoint, so the path walks around its own dead ends).
  **PITCH 3**, **MIN_NODES 7 / PITCH_MIN 2**, **BACKBITE 900**, **MARGIN_MIN 20** (reused unchanged
  from the 52nd and 53rd). No RNG anywhere, so a silhouette always yields the same wire and the male
  and female sheets of one item agree.
  **FOUR TUNING LESSONS, all four paid for on a render rather than argued:**
  (1) *A field role must take a FIELD tone however brightly lit it is, and it inverted the picture.*
  LIP is the lit approach on the plate beside the wire, and the first cut painted it in a pale metal
  grey because "the lit side is bright". At a 3px period one pixel of wire has two of field beside
  it, so putting one of those two on the metal ramp handed the metal TWO THIRDS of the piece: the
  lit field welded to the wire it was meant to sit beside, the two fused into one broad pale mass,
  and what was left reading as a line was the dark remainder. The figure and the ground had swapped
  and the traceable thing was the GAP. This is the 52nd's mid-luminance-liner failure arrived at
  from the other end.
  (2) *Check which ROLES a pitch can still express, not just whether the motif resolves.* The design
  predicted PITCH 2 would be a dither and the sweep says otherwise: at PITCH 2 the maze is perfectly
  legible and it is FLAT. One pixel of channel separates two runs, that pixel always has wire above
  or left of it so it always takes SHADE, and **the LIP role never fires anywhere on the piece** —
  with only the shadow half of the pair surviving nothing says the wire stands proud, and a line
  with no relief drawn on a plate is the 23rd MEANDER's kind of mark. A pitch that resolves and
  cannot shade is worse than one that shades. (PITCH 4 → long parallel runs with a turn at each end,
  i.e. the 11th FLUTING with a join; PITCH 5 → one run on a torso, the 8th SIDE-STRIPE. Bounded by
  an older axis on both sides, as with the 49th–53rd.)
  (3) *One wire PER CONNECTED COMPONENT, not per bounding blob.* A wire is soldered to a plate and
  cannot jump the gap between the two legs of a pair of chausses or between the left boot and the
  right. The first cut passed the whole opaque mask in as one blob and, because a path cannot cross
  a gap, filled ONE leg and left the other a flat recolor.
  (4) *Judge a field stop AFTER the finishing pass, not before* — a new lesson, and both classes that
  needed re-pitching needed it for this reason. The chain shades with `protect=False` and lifts the
  lit side hard, so a stop chosen in the generator is not the stop that reaches the sheet. The
  warrior's oxblood (134,66,64) came out of the finish as a pale SALMON — a weak partner for a
  platinum wire — and the ranger's walnut (104,78,54) came out a light tan sitting squarely ON THE
  SKIN RAMP, which is the 47th's rose-gold failure at maximum area rather than on one stop. Both
  dropped ~2 steps and the ranger moved off brown entirely.
  Palette — six stops per class, brightest first (term / crest / lip / floor / shade / ground), with
  TERM and CREST on the WIRE's ramp and the other four on the FIELD's: warrior PLATINUM wire on
  OXBLOOD; mage AMBER-GOLD on INDIGO; ranger COPPER on DEEP TEAL (no prior ranger tier uses a warm
  metal, which puts air between this and the 52nd's green-birch-over-slate-blue and the 53rd's
  silver-jade-on-forest; the warrior is deliberately NOT gold for the third tier running). No stop
  near pure black — the helmet constraint, since the finishing pass carves the visor as black eye
  and mouth pixels; every class's darkest stop clears channel-sum 150, verified on the warrior dome
  whose `grille` visor reads clean through the wire.
  Slots: chest Cuirass `shirt_%s_legendary54`, legs Chausses `pants_%s_legendary54`, boots Sabatons
  `boots_%s_legendary_maze`, helmet Helm `helmet_%s_legendary54`. Generator
  `scripts/gen_labyrinth_axis54.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, so the silhouette never changes; self-contained
  NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()`
  in-line, tenth generator to do so after axes 45–53; carries `--cells` for an ASCII dump plus the
  TOPOLOGY acceptance test, `--swatch` for the bare motif on a synthetic notched/waisted test plate,
  and `--sweep` for the PITCH 2/3/4/5 sweep plus the BRANCH and CLOSED controls on a real torso AND
  a real leg).
  **Acceptance test — a NEW KIND.** Every previous axis is accepted on a STATISTIC of its field (the
  46th's cell count, 48th's size ratio, 50th's glyph survival, 52nd's distinct-hole appearances,
  53rd's radius histogram and contact fraction), because a field is the sort of thing you can only
  measure. This axis is one object, so it is accepted on its TOPOLOGY, which is a fact rather than a
  measurement: components 1, branch points 0, endpoints 2, loops 0, traceable True. Branch points
  > 0 is the 49th dendrite; loops > 0 is the 14th lattice; components > 1 and it is a field again
  with no claim left. **Result: 985 wired components across all 24 sheets × 60 active frames, 0
  topology violations — every single component carries exactly one traceable open wire.**
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…53 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_labyrinth_legendary_preview/`,
  `_labyrinth_legs_preview/`, `_labyrinth_boots_preview/`, `_labyrinthdome_helmet_preview/`.
  Previews: `_PREVIEW_labyrinth_legendary.png`, `_PREVIEW_labyrinth_legs.png`,
  `_PREVIEW_labyrinth_boots.png`, `_PREVIEW_labyrinthdome_helmet.png` (built by
  `scripts/preview_axis54.py`); zooms `_ZOOM_labyrinth_chest.png`, `_ZOOM_labyrinth_head.png`;
  diagnostics `_diag_labyrinth_swatch.png` (bare motif, all 3 classes), `_diag_labyrinth_sweep.png`
  (PITCH 2/3/4/5 plus the BRANCH and CLOSED controls on a real torso and leg),
  `_diag_labyrinth_pitch.png` (PITCH 2/3/4 zoomed on the real torso and dome — the frames the pitch
  decision was actually read off) and `_diag_labyrinth_visor.png` (the warrior dome's black eye and
  mouth slits reading clean through the wire, m + f).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L56** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **53rd net-new-geometry axis — GRANULATION (a contact packing of graded beads), all 4 slots**
  (2026-08-08): the armour is covered in soldered metal beads of DIFFERENT SIZES, each one as large
  as the room it sits in allows, laid shoulder to shoulder so that they TOUCH, with the dark solder
  bed surviving only in the hollows a circle packing cannot close.
  **THIS IS THE FIRST PACKING AXIS, AND THE FIRST WHOSE ELEMENT SIZE IS AN OUTPUT RATHER THAN A
  CONSTANT.** All fifty-two prior axes fix the element's size once, in the generator: a hexagon is
  the same hexagon on the chest and on the boot, a coffer is a coffer, a rune is a rune. The pattern
  is authored and the silhouette is then used as a stencil to cut it out. Here the causal arrow runs
  the other way — the field is GROWN INTO the silhouette, largest bead first, each taking the biggest
  radius that fits in the room still unclaimed — so the ornament cannot be stated without the shape
  it lives on. Measured on the real idle frames the histogram is a different object on every slot:
  chest `{r2: 3, r1: 8}`, legs `{r2: 2, r1: 6}`, dome `{r2: 2, r1: 5}`, boot `{r2: 3, r1: 1,
  shot: 2}` — and **none of those numbers is in the generator**; they are read off the armour.
  The families it could be confused with each fail differently. The **13th STUDWORK** is the near
  miss and the one both ends of the sweep collapse into: a rivet field is ONE radius on a PERIODIC
  GRID with ground all round every stud, so any two neighbours are congruent, the spacing is the same
  everywhere and on every piece, and no stud ever touches another — the grid is the subject and the
  stud only marks it. Here there is no grid: neighbours are routinely different sizes, centre-to-
  centre distance is whatever the two radii sum to, and the beads are IN CONTACT. Contact is
  load-bearing, which is why there is no gap knob to tune — the `GAP=1` control in `--sweep` forces
  one pixel of bed between every pair and the field instantly reverts to graded dots on a ground,
  i.e. studwork with jitter. The **41st BEAD-AND-REEL / 38th EGG-AND-DART** thread convex bodies
  along a RULED track with a strict period and an element sized BY that period; two radii here are
  not an alternation — they do not take turns, their ratio changes slot to slot, and neither is on a
  track. The **46th CRAQUELURE** is the other unruled field and the difference is partition versus
  packing: craquelure partitions (every pixel in some cell, boundaries shared, the "ground" just the
  shared edge) and its cell sizes come from a PRNG and mean nothing; a packing's bodies are convex,
  meet at points, leave a genuine interstitial bed, and its sizes are readable off the silhouette.
  The **48th COSMATI** is multi-scale but DISCRETE, FIXED-RATIO (8:5:2) and identical in every bay,
  because it is authored — you can name its three sizes before seeing the armour. The **15th SCALE**
  overlaps on a lattice in a fixed z-order; contact is not overlap, nothing is hidden, there is no
  order. The **47th MOKUME** is shape-CONFORMAL (tone = f(distance-to-edge)) but its band spacing is
  still a constant of the ornament; this is shape-DETERMINED and its spacing is an output.
  Geometry, per component, in the component's own frame: chamfer-(3,4) distance to the outside gives
  the room; candidates are ordered (dist DESC, y, x) with no RNG anywhere; **one full sweep per
  radius, largest first**; `disc(r) = dy²+dx² <= r²+0.5` (r=0 one pixel, r=1 a 5px plus, r=2 13px).
  **FOUR TUNING LESSONS, all four paid for on a render rather than argued:**
  (1) *Largest-first must be one sweep PER RADIUS, not the best radius at each site.* Walking the
  candidates once in distance order and taking the largest radius that fits places ONE big bead and
  then — because every remaining high-distance pixel is its neighbour and has no room left — fills
  the entire rest of the piece with the minimum. Histogram came out `{1: 50, 2: 1, 3: 1}`: one size
  in practice, which is the 13th studwork. Sweeping the whole component for the big beads BEFORE
  anything small is committed is what produces the grading, and the grading is the axis.
  (2) *A bead must be shaded CONCENTRICALLY, not by light direction.* The first cut shaded each bead
  as a sphere — bright upper-left crescent, dark lower-right — which is optically right and
  completely illegible: in a packed field every bead's bright side lands hard against its
  neighbour's dark side, the eye joins them across the contact, and the piece comes out as a marbled
  diagonal streak that reads as figured stone. Tone must be f(radius from the bead's OWN centre):
  bright core, mid annulus, dark rim all the way round, so the shape closes. The light survives as a
  bias on top — pip up-left of the core, rim one stop darker on the down-right contact side.
  (3) *The element ceiling is set by the NARROWEST slot, not the widest.* RMAX=3 was the design's
  first pick and the sweep killed it: a 7px bead is over half a 13px torso wide, so the packing puts
  ONE in the middle and pads round it (`{r3: 1, r2: 2, r1: 4}`), which at 1x is a boss with filler —
  the 8th aegis roundel's figure-ground — and the RMAX 3/4/5 sweep frames are nearly identical to
  each other, the tell that the field has stopped being a field. **RMAX=2 chosen.** This is the
  47th's "pitch is set by the thinnest part" reached from the other side: there it constrained
  spacing, here the element.
  (4) *Two starvation fixes, both scoped to where the packing actually starves.* The FILLET — an
  interstitial pixel touching two DIFFERENT beads takes the bead ramp's dark stop, as solder wicked
  into the crease — cuts the bed from 44% to 34% of a torso and is drawn evidence of contact, since
  a fillet exists only where two beads touch. The SHOT (a 1px granule) and CLIPPED beads (a bead set
  proud of the edge, cut by the silhouette, 3 of its 5 px still on the piece) fire ONLY on a
  component with no interior — every boot, which is 4–5px across and all boundary, and which the
  strict rules left with TWO beads and an otherwise flat recolor. Both are deliberately OFF on the
  broad slots: a shot pass on a torso placed 56 grains against 11 beads, took the bed to 0% and
  turned the field into bright speckle with the beads lost inside it. The bed has to survive for the
  contact to be visible. Same adaptive-boundary shape as the 52nd's `MARGIN_MIN`, which is reused
  unchanged (20) for the bezel.
  Palette — six stops per class (pip / lit / mid / dark / rim / ground), pairing a bright bead metal
  with a contrasting dark bed, because at 13px a luminance step alone reads as shading: warrior GOLD
  on GRAPHITE; mage MOONSILVER on VIOLET INK; ranger SILVER-JADE on DEEP FOREST (deliberately not the
  52nd's green-birch-over-slate-blue, so adjacent legendary tiers do not read as recolors). No stop
  near pure black — the helmet constraint, since the finishing pass carves the visor as black eye and
  mouth pixels; every class's darkest stop clears channel-sum 150, verified on the warrior dome whose
  `great` visor reads clean through the beading.
  Slots: chest Cuirass `shirt_%s_legendary53`, legs Chausses `pants_%s_legendary53`, boots Sabatons
  `boots_%s_legendary_granule`, helmet Helm `helmet_%s_legendary53`. Generator
  `scripts/gen_granulation_axis53.py` (repaint-only, QA-safe by construction — every pattern pixel
  painted ONLY onto already-opaque body pixels, so the silhouette never changes; self-contained NumPy
  `label4()` and chamfer distance, NO scipy; calls `sprite_finish.finish_array(arr, dst)` +
  `save_finished()` in-line, ninth generator to do so after axes 45–52; carries `--cells` for an
  ASCII dump plus the per-slot radius histogram and contact fraction that are the acceptance test,
  `--swatch` for the bare motif on a synthetic notched/waisted test plate, and `--sweep` for the
  RMAX 1–5 sweep plus the forced-gap control on a real torso AND a real leg).
  24 sheets: **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**;
  the 6 chests each gain +510 (m) / +440 (f) px — identical to the axis-45…52 figures, i.e. the
  finishing pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. **Acceptance test result:** ≥2 size classes on every slot,
  a different mixture on each, contact fraction 1.00 on chest / boots / dome and 0.88 on legs.
  Staged in `_granulation_legendary_preview/`, `_granulation_legs_preview/`,
  `_granulation_boots_preview/`, `_granulationdome_helmet_preview/`. Previews:
  `_PREVIEW_granulation_legendary.png`, `_PREVIEW_granulation_legs.png`,
  `_PREVIEW_granulation_boots.png`, `_PREVIEW_granulationdome_helmet.png` (built by
  `scripts/preview_axis53.py`); zooms `_ZOOM_granulation_chest.png`, `_ZOOM_granulation_head.png`;
  diagnostics `_diag_granulation_swatch.png` (bare motif, all 3 classes) and
  `_diag_granulation_sweep.png` (the RMAX 1/2/3/4/5 sweep plus the GAP=1 control on a real torso and
  leg).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L55** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **52nd net-new-geometry axis — AJOURÉ / OPENWORK (a pierced plate over a second surface),
  all 4 slots** (2026-08-08): the armour is a solid sheet fretted through with a field of small
  square openings on 2px bars, and behind it — visible only through those openings — lies a LINING
  of a different metal carrying a grain of its own.
  **THIS IS THE FIRST AXIS WITH TWO SURFACES, AND OCCLUSION IS THE SUBJECT.** All fifty-one prior
  axes model ONE skin: however elaborate they get, every pixel belongs to the same continuous
  surface and its tone is a statement about the SHAPE of that surface — the 11th flute is that skin
  folded, the 37th coffer is it sunk, the 46th craquelure is it broken, the 47th mokume is its
  boundary read inward, the 51st flowgrain is its grain. Depth in all fifty-one is RELIEF, a few
  tenths of a pixel of modelled height on one sheet. Here there are two sheets at two depths with
  air between them, and a pixel's first question is not "where on the surface am I" but "WHICH
  SURFACE AM I ON" — which buys the one thing relief cannot: a pixel of the lower surface tells you
  about a place the upper surface is NOT.
  The families it could be confused with each fail differently. The **OUTLINE-NET axes** (14th
  lattice, 17th ashlar, 19th honeycomb, 20th trellis, 21st chainmail) are the obvious near miss,
  since a fret is also a net with holes in it, and two things separate them at 1x. First, their
  member is a 1px LINE — a drawn boundary between cells of the same body — where the member here is
  a 2px BAR carrying its own two-stop relief (lit lip on the edge that overhangs the hole, dull back
  on the far side), which is what makes it read as a SHEET that has been pierced rather than a line
  that has been drawn. Second and decisively, what shows in a net axis's holes is the BODY: same
  material, same tone, phase-locked to the net because it IS the net's ground, so any two holes are
  identical. What shows here is a different material at a different hue with a pattern of its own
  that is NOT phase-locked to the openings, so any two neighbouring holes DIFFER — and the amount
  they differ by is exactly how far the hidden surface has moved. That mismatch is the evidence of a
  continuous thing behind, and it is the whole axis. The **37th coffer** and **45th arcade** are
  recesses: their floor is the same material one level down, off the same ramp, uniform within a
  cell and necessarily identical in every cell, because a recess has no existence apart from the
  thing it is recessed into — a liner does. The **13th studwork** is the exact inverse operation
  (material added on a grid, not removed), and the inverse of a hole is a boss, not a second
  surface. The **26th tartan / 33rd octagram** do superpose two line families but IN THE SAME
  PLANE — both visible everywhere, crossings the interesting part; here the second family is
  visible NOWHERE except through the first, there are no crossings, and the relation is not overlay
  but occlusion.
  Geometry, on the component's own bbox with **BAR 2 / OPEN 2 (period P = 4)**: `hole` where
  `y%P>=BAR and x%P>=BAR`; `shadow` at the hole's (BAR,BAR) corner — the corner nearest the
  upper-left light, which the overhanging lip shades; `lip` = a web pixel with a hole directly below
  or right; `back` = a web pixel with a hole directly above or left; `web` = the fret's crossing
  nodes. Liner banding `(x+y) % LINER_P < LINER_W` at **LINER_P 7 / LINER_W 3**, at 45° to the
  square fret above it.
  **FOUR TUNING LESSONS, all four paid for on a first cut:**
  (1) *The liner's grain must be COARSER than the aperture.* First cut ran a 1px grain on period 3.
  An opening is 2x2 and shows three pixels of liner, so a fine grain drops one bright pixel
  somewhere different in each hole and the plate SPARKLES — scattered glints, not a surface.
  Continuity across an occluder can only be read at a scale the occluder does not destroy, so the
  grain must be legible at the scale of the HOLE GRID: at 7/3 a band spans two to three openings, a
  run of holes lights together along a diagonal while their neighbours stay dark, and THAT the eye
  joins into one surface passing behind the bars.
  (2) *The two periods must stay COPRIME.* gcd(7,4)=1, so the liner's phase advances three pixels
  from each opening to the next and the hole appearances cycle instead of repeating. Share a factor
  and the grain phase-locks to the lattice, every hole shows the identical pixels, the liner becomes
  part of the cell, and the axis has silently collapsed into the 37th coffer with a fussier floor.
  `--cells` prints the distinct-appearance count; **1 is the failure**.
  (3) *The liner is IN SHADE and must be painted that way.* First cut ran it mid-luminance (brass
  150, teal 190) on the reasoning that a second metal should hold its own. It cannot: a hole filled
  with a tone as bright as the plate stops reading as an OPENING and reads as an INLAY, a stone set
  into the surface — the 13th studwork with coloured bosses. A hole is dark first and coloured
  second, so every liner stop now sits at or below the plate's darkest stop, which is also
  physically correct. `shadow` is a darkened LINER tone, never a darkened plate tone; a
  plate-coloured shadow inside the hole reads as more plate and closes the hole up.
  (4) *The MARGIN has to be adaptive.* Every piece carries a solid 1px frame around its silhouette —
  that is how real ajouré is made (a pierced panel with no margin has no edge strength), it keeps
  the brightest stop off the silhouette per the standing rule since the 47th, and it keeps the
  darkest stop off it too, so no dome ever grows the full-silhouette dark rim. But measured on the
  real idle frames the interior pixel counts are chest 78, dome 59, legs 39 — and **boots 2 to 8**,
  because a foot at this scale is four or five pixels across and is ALL boundary. Framing a boot
  left it a flat recolor with not one opening on it. So `MARGIN_MIN = 20`: a component with no real
  interior keeps its openings and gives up its frame, and the edge rule is honoured the other way
  instead (on an unframed component no boundary pixel may take the bright `lip` stop). This is also
  what real ajouré does — the pierced field lives on the broad plates and small fittings are pierced
  right out to their edge.
  Palette — six stops per class (lip / web / back / shadow / liner_hi / liner_lo), each pairing a
  plate metal with a CONTRASTING liner metal, because at 13px a luminance step alone reads as
  shading and only hue says "different material": warrior BLUED STEEL over BRASS; mage
  MOONSILVER-LILAC over ARCANE TEAL; ranger GREEN-BIRCH over SLATE-BLUE (pushed off the tan skin
  ramp, and no warm off-white anywhere — the 47th's rose-gold lesson). No stop is near pure black —
  a HELMET constraint, since the finishing pass carves the visor as black eye and mouth pixels and a
  near-black stop swallows the face slit (the 49th's lesson); verified on the warrior dome, whose
  `nasal` visor reads clean through the piercing.
  Slots: chest Ajouré Cuirass `shirt_%s_legendary52`, legs Chausses `pants_%s_legendary52`, boots
  Sabatons `boots_%s_legendary_ajoure`, helmet Helm `helmet_%s_legendary52`. Generator
  `scripts/gen_ajoure_axis52.py` (repaint-only, QA-safe by construction — the fretwork painted ONLY
  onto already-opaque body pixels, so the holes are PAINTED, not cut, and the silhouette never
  changes; self-contained NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` +
  `save_finished()` in-line, eighth generator to do so after axes 45–51; carries `--cells` for an
  ASCII dump of the role field plus the distinct-hole-appearance count that is the actual acceptance
  test, `--swatch` for the bare motif on a synthetic notched/waisted test plate, and `--sweep` for
  the BAR/OPEN sweep on a real torso AND a real leg). 24 sheets: **sprite_qa ALL 24 PASS** (helmets
  `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask
  parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m) / +440 (f)
  px — identical to the axis-45…51 figures, i.e. the finishing pass's asymmetric shoulder/pauldron
  caps, not stray geometry; all 24 carry the `TaskQuestFinish=2026-08-01.6` stamp. Staged in
  `_ajoure_legendary_preview/`, `_ajoure_legs_preview/`, `_ajoure_boots_preview/`,
  `_ajouredome_helmet_preview/`. Previews: `_PREVIEW_ajoure_legendary.png`,
  `_PREVIEW_ajoure_legs.png`, `_PREVIEW_ajoure_boots.png`, `_PREVIEW_ajouredome_helmet.png` (built
  by `scripts/preview_axis52.py`); zooms `_ZOOM_ajoure_chest.png`, `_ZOOM_ajoure_head.png`;
  diagnostics `_diag_ajoure_swatch.png` (bare motif, all 3 classes) and `_diag_ajoure_sweep.png`
  (the BAR/OPEN 1·2 / 2·2 / 2·3 / 3·3 / 2·4 sweep on a real torso and leg).
  **BAR/OPEN sweep, bounded at both ends by a collapse into an older axis:** BAR 1 OPEN 2 (P=3) → a
  1px web is a LINE, not a pierced sheet; it cannot carry the lit-lip / dull-back pair that says
  "plate with thickness", the relief collapses, and what is left is a drawn grid over a darker
  ground, i.e. the **14th lattice** — the second surface is still there but nothing signals that it
  is one. BAR 2 OPEN 2 (P=4) → three hole columns across a 13px torso, four down a thigh, bars
  carrying both stops, liner bands spanning two to three openings — **chosen**. BAR 2 OPEN 3 (P=5)
  → only two hole columns survive inside the margin, and a row of large dark squares in a light
  field is the **37th coffer**. BAR 3 OPEN 3 (P=6) → one hole column on a torso, none on a boot;
  not a field. BAR 2 OPEN 4 (P=6) → the hole is wide enough that the liner becomes the SUBJECT with
  a frame around it, which is the **45th arcade**'s figure-ground, not this one's.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L54** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **51st net-new-geometry axis — FLOWGRAIN (a continuous director field with topological defects),
  all 4 slots** (2026-08-08): the surface is figured with one unbroken family of raised ridges whose
  DIRECTION IS A FUNCTION OF POSITION — the grain sweeps across the plate at about -28°, wraps around
  a KNOT where the ridges close on themselves, and splits at a DELTA where two streams of grain part
  company. It is the figure in a burl, the water in a pattern-welded blade around a punched eye, the
  flow in a fingerprint.
  **This is the FIRST CONTINUOUS-FIELD AXIS AND THE FIRST WITH NO REPEATING MEMBER.** Every one of
  the fifty prior axes is generated by a UNIT: forty stamp a congruent cell on a lattice (hexagon,
  scale, arch, coffer, bay), ten run a congruent member along a track (flute, wave, meander, cable,
  guilloche, strigil, gadroon, zigzag), and the three most recent break the unit's CONTENT — 48th
  cosmati gives it a hierarchy of sizes, 49th dendrite gives it descent, 50th runic gives it a
  vocabulary — but all three still lay that content into a ruled periodic carrier, and in all fifty
  you can point at the thing that repeats. Here you cannot. Tone is an ANALYTIC FUNCTION of position,
  `t = frac(PHI(x,y) / 2π)`, and no two ridges on the plate are congruent: different lengths,
  different curvatures, different orientations, some closing into loops and some running off the
  silhouette. The axis is not a pattern placed on the armour, it is a FIELD the armour was cut out
  of, and what makes it read as ornament rather than noise is not a grid — it is the field's
  SINGULARITIES. The families it could be confused with each fail that differently. The line axes
  (11th fluting, 22nd wave, 30th cable, 42nd strigil, 43rd gadroon, 44th zigzag) all have a GLOBAL
  DIRECTION — a flute is vertical everywhere, a strigil is the same S at every column, a wave is one
  sine translated; rotate the piece and you can still name the single direction the family runs.
  Here there is no such direction: the grain turns through the vertical at the knot and comes back
  the other way past the delta, so direction is a LOCAL property, which is the subject. The **47th
  mokume** is the sharpest near miss because it is also unruled and its bands also curve — but
  mokume's bands are CONTOURS OF THE SILHOUETTE (tone = f(distance-to-edge)), so its figure is a
  property of the OUTLINE and every band is a scaled copy of the boundary, closed and nested;
  flowgrain's ridges are contours of a field that knows nothing about the outline, are open, are not
  nested, cross the silhouette at every angle, and survive reshaping the piece. Nesting is
  containment; this is flow. The **24th spiral / 28th concentric** close their curves around TILED
  centres, a periodic lattice of cores each of whose neighbourhoods repeats; this axis has TWO
  singular points on the whole piece, of TWO KINDS (+2 knot, −2 delta), and away from them the field
  is organised around nothing. The **46th craquelure** is the only other axis with no repeating unit,
  and the relation is the exact opposite failure of periodicity: craquelure is DISORDER without
  periodicity (a jittered partition, no straight line anywhere, every junction an accident of a
  PRNG), flowgrain is SMOOTH ORDER without periodicity (one differentiable function, no randomness
  at all, every ridge parallel to its neighbour everywhere, and the only two places anything happens
  fixed by topology rather than chance). One is noise, the other a flow.
  **RELIEF, and the second new thing here:** every prior axis picks its stop from WHERE a pixel sits
  in the cell; this one picks the crest stop from WHICH WAY THE RIDGE POINTS — a crest running square
  to the light (upper-left, as everywhere in the set) takes the bright nickel stop, one running along
  it takes the dull one, so the highlight MIGRATES along the grain as the direction turns. That is
  orientation-dependent shading, only possible on an axis whose subject is orientation.
  Geometry: `PHI = (2π/PITCH)·(x·cosALPHA + y·sinALPHA) + Σ qᵢ·w(rᵢ)·atan2(y−dyᵢ, x−dxᵢ)`, with
  **PITCH 3.6**, **ALPHA 62°** (the gradient direction, so ridges run perpendicular — 62° puts the
  prevailing grain off every family axis in the set: horizontal reads as 47th mokume or banded
  lamellar, vertical as 11th fluting or 43rd gadroon, 45° as 16th twill), **KNOT (+2) at (0.32, 0.30)
  and DELTA (−2) at (0.62, 0.52)** of the component bbox — the knot LEFT of centre and high, because
  the character faces LEFT and the organising feature belongs on the lit side.
  **FOUR TUNING LESSONS, all four paid for on a first cut:**
  (1) *The charge must be an INTEGER.* atan2 jumps 2π across its branch cut, so the phase jumps
  `q·2π` along a ray out of each core and the banding `frac(PHI/2π)` only hides that jump when q is a
  whole number of periods. The honest half-charge of a real fingerprint delta (q=½) leaves half a
  period of mismatch along a straight line right across the piece — and a straight discontinuity is
  the one thing a flow must not have: it reads as a scratch, or worse as a plate seam, and the armour
  looks like two pieces butted together. Swept 1/2/3: at 1 the grain barely bends on a 13px torso and
  the axis is a diagonal 11th fluting; at 2 the knot closes inside 5px and the delta's split is
  legible; at 3 the spacing at the cores compresses past 1px and both cores smear.
  (2) *`w(r) = r²/(r²+CORE_R²)` is load-bearing, not cosmetic.* An undamped atan2 has unbounded
  gradient at its centre, so ridge spacing collapses to nothing there and the knot comes out as a 3px
  smear of alternating pixels — the mush the 30th cable was retuned to avoid. At **CORE_R 3.0**,
  |∇PHI| p95/median on a 13x20 torso falls from **2.53 to 1.39**: nowhere is the spacing more than a
  third tighter than the carrier's. A real ridge core is a tight curve, not a singularity.
  (3) *The defect pair must be TIGHT.* Spread to opposite corners (0.36,0.32)/(0.68,0.70) the field
  rotates through 90° across the whole middle of the plate, which lands a broad horizontal band on
  the chest and reads as the **8th side-stripe** with texture in it. Within ~7px the disturbance stays
  local, the rest of the piece keeps its sweep, and the two singular points read as FEATURES of a
  flow instead of as a seam between two textures.
  (4) *A migrating highlight has to be a shimmer, not an element.* First cut ran the crest stops 236
  against 170 on a 0.45 threshold; with the light up-left, a 45° ridge PARALLEL to it is the only
  orientation that goes fully dull (horizontal, vertical and the other diagonal all sit at 0.71+), so
  most of the plate lit up and the band where the field turns horizontal came out as one hard white
  bar — a bar reads as a BELT. Crest stops brought within ~46 levels of each other and **FACE_T 0.86**
  (only crests within ~10° of square-on lift).
  Palette — five stops per class (crest square to light / crest along it / flank / groove / deep):
  warrior PATTERN-WELDED STEEL, cold greys with nickel crests, the water in the billet; mage
  AETHER CURRENT, deep indigo shot with luminous ice (first indigo ground in the set — the 50th's
  mage ground is violet-black and the two are only ever seen side by side); ranger FIGURED OLIVE ASH,
  green-grey heartwood with pale sage-gold figure, pushed green deliberately clear of tan skin. No
  stop is near pure black — a HELMET constraint, not taste, since the finishing pass carves the visor
  as black eye and mouth pixels and a near-black groove swallows the face slit (the 49th's lesson).
  Slots: chest Pattern-Welded Cuirass `shirt_%s_legendary51`, legs Chausses `pants_%s_legendary51`,
  boots Sabatons `boots_%s_legendary_flowgrain`, helmet Helm `helmet_%s_legendary51`. Generator
  `scripts/gen_flowgrain_axis51.py` (repaint-only, QA-safe by construction — the grain painted ONLY
  onto already-opaque body pixels; self-contained NumPy `label4()`, NO scipy; calls
  `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line, seventh generator to do so
  after axes 45–50; carries `--field` for an ASCII dump of the field plus the |∇PHI| statistics that
  are the actual acceptance test, `--swatch` for the bare motif on a synthetic notched/waisted test
  plate, and `--sweep` for the PITCH sweep on a real torso AND a real leg). 24 sheets:
  **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots
  `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6
  chests each gain +510 (m) / +440 (f) px — identical to the axis-45…50 figures, i.e. the finishing
  pass's asymmetric shoulder/pauldron caps, not stray geometry; all 24 carry the
  `TaskQuestFinish=2026-08-01.6` stamp. Staged in `_flowgrain_legendary_preview/`,
  `_flowgrain_legs_preview/`, `_flowgrain_boots_preview/`, `_flowgraindome_helmet_preview/`.
  Previews: `_PREVIEW_flowgrain_legendary.png`, `_PREVIEW_flowgrain_legs.png`,
  `_PREVIEW_flowgrain_boots.png`, `_PREVIEW_flowgraindome_helmet.png` (built by
  `scripts/preview_axis51.py`); zooms `_ZOOM_flowgrain_chest.png`, `_ZOOM_flowgrain_head.png`;
  diagnostics `_diag_flowgrain_swatch.png` (bare motif, all 3 classes) and
  `_diag_flowgrain_sweep.png` (the PITCH 5.5/4.5/4.0/3.6/3.0 sweep on a real torso and leg).
  **PITCH sweep, bounded at both ends by a collapse into an older axis — and, unlike the 49th and
  50th, into a DIFFERENT axis at each end:** 5.5 → 3 ridges on a 13px torso and 2 on a thigh, which
  the eye reads as contours of the silhouette, i.e. the **47th mokume**, and the knot has no room to
  close; 4.5 → 4 ridges, knot closes only just, delta falls off the hip; 4.0 → 5 ridges, both
  defects legible; **3.6 → 6 ridges on the torso and 4 down a thigh, knot closing inside 5px, clean
  3-stop crest/flank/groove profile — chosen**; 3.0 → the profile loses its flank, each ridge becomes
  a 1px light/1px dark pair, convex relief is gone, and a hatch that fine reads as the **16th twill**
  with a wobble — direction, the entire subject, becomes unreadable exactly when there is most of it
  on the plate.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L53** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **50th net-new-geometry axis — RUNIC / EPIGRAPHIC (ruled inscription registers), all 4 slots**
  (2026-08-08): the plate is ruled into horizontal REGISTERS by a raised 2px FILLET, and each sunken
  channel between rules is CARVED WITH A LINE OF RUNES — angular 3x3 glyphs drawn from a
  sixteen-letter alphabet, inlaid in bright wire, set on a common baseline with a clean gap between
  one letter and the next.
  **This is the FIRST AXIS IN FIFTY WITH A VOCABULARY.** In every one of the forty-nine prior axes
  the field is built from INSTANCES OF ONE ELEMENT — the plate carries a hexagon, or a scale, or an
  arch, or a shard, over and over, and any two elements differ only in where they sit, how big they
  are, or how far they are from a root. Here the elements are DIFFERENT FROM ONE ANOTHER BY DESIGN:
  sixteen distinct closed forms, laid out in a sequence whose order is arbitrary. A glyph's identity
  is not derived from anything — not from position, not from scale, not from a parent — it is simply
  which letter it is. The subject of the axis is NOTATION. The four families it could be confused
  with each fail that in a different way. The ruled-cell axes (11th–45th) stamp ONE congruent cell,
  so the field is a texture and any patch of it is interchangeable with any other patch; an
  inscription is not interchangeable with itself — move it three pixels along and you are reading
  different letters. The **38th egg-and-dart** is the sharpest near miss because it does put TWO
  different elements on the plate, but they are in STRICT ALTERNATION, so the second is fully
  determined by the first and the pair is really one compound cell repeating — a two-syllable
  texture, not a language (same for 18th basketweave's alternating thread direction and 29th
  houndstooth's colour-and-weave phase). The **48th cosmati** is the other close call, with three
  genuinely different elements at once, but its ranks are a HIERARCHY: an element's identity IS its
  size, and knowing a Cosmati element is 2px tells you it is a tessera and where in the bay it must
  sit. All sixteen runes here are the same size on the same baseline; size carries nothing. The
  **46th craquelure** is the only prior aperiodic axis and the relation is an exact INVERSION worth
  keeping: craquelure is an aperiodic CARRIER (jittered Voronoi) filled with uniform CONTENT (every
  shard the same kind of thing, differing by accident of the jitter); this is a strictly periodic
  carrier — ruled registers, constant letter pitch, a baseline that never wanders — filled with
  aperiodic CONTENT. Craquelure is disorder in the grid, runework is disorder in the text, and
  neither can be mistaken for the other at 1x: one has no straight lines anywhere, the other is
  nothing but straight lines. The **49th dendrite** is multi-part but its parts are ranked by
  DESCENT and are all the same mark; no alphabet, no baseline.
  **WHY IT READS AS WRITING AND NOT AS NOISE — the whole risk of a vocabulary axis at 13px. Three
  things do the work and all three are load-bearing:** (1) the BASELINE — every glyph in a register
  starts on the same row and is exactly 3 rows tall, which is the single strongest cue for text;
  (2) the GAP — `GLYPH_P = 4` = 3 stroke columns + 1 empty column, so letters never touch, because
  two runes that fuse are one blob and a row of blobs is the **40th dentil**; (3) the RULE — a 2px
  raised fillet above and below each line frames the marks as a REGISTER exactly as a carved stele
  or a coin legend does, and without it the marks float and the field does read as damage. The
  alphabet is built for the same end: every letter is 4–6 lit pixels of 9, connected, and drawn only
  with straight strokes on the three axes a chisel can cut — which is what real rune-rows look like,
  because they were carved with the grain of wood and stone. Letters are chosen by a deterministic
  integer mix of (register index, letter index), never a PRNG, so the male and female sheets of one
  item carry the SAME inscription — a pair with different text reads as two different objects.
  **RELIEF runs in two directions at once, the first in the set to do so:** the rule stands PROUD
  (bright top pixel, its own shadow beneath), the channel is SUNK (a dark cut-shadow row immediately
  under the overhanging rule, a lighter floor row at the bottom where light reaches again), and the
  wire in the letters stands proud INSIDE the sunken channel (a glyph pixel with no glyph pixel
  above it takes the bright inlay stop, the rest the mid).
  Geometry per opaque body pixel in component-local (lx,ly) with **BAND_P=7**:
  `ry = (ly + VPHASE) % BAND_P`; `ry==0` → RULE top, `ry==1` → RULE underside, `ry==2` → CUT SHADOW,
  `ry==BAND_P-1` → CHANNEL FLOOR, else GLYPH ZONE with `gy = ry-3`, `gxall = lx - HPHASE`,
  `gcol = gxall % GLYPH_P` (`gcol==3` is the inter-letter gap) and the letter
  `VOCAB[hash(ly//BAND_P, gxall//GLYPH_P)]`.
  **TUNING — this axis is tuned for SURVIVAL OF THE ALPHABET, not for taste, and its budget is
  fixed at both ends:** 2px rule + 1px cut shadow + 1px floor = 4px of furniture, so the glyph zone
  is `BAND_P-4` rows and the alphabet needs 3 of them, which makes 7 the smallest pitch at which the
  axis exists at all. Like the 49th it is bounded on BOTH sides by a collapse into an OLDER axis
  rather than into mush, and — unusually — into the SAME old axis from both directions. Swept
  10/9/8/7/6 (`--sweep`, on a real torso AND a real leg): at 10 a 13px torso holds ONE register and
  a thigh holds none, so what is left is a single decorated band across the chest — the **8th
  side-stripe** with texture in it, or on a boot the **40th dentil**; the axis stops being a SURFACE
  and becomes a belt. At 9 the torso gets one full register and the top of a second and the legs
  still go a whole limb with no complete line of text. At 8 there are 1.6 registers on the torso and
  1 on the leg, legible, but the spare bed row inside each channel loosens the band and the letters
  stop reading as sitting ON a baseline. At **7** there are two full registers on the torso and
  nearly two on the thigh, letters tight to their rules, the whole surface inscribed — chosen. At 6
  the glyph zone drops to 2 rows and the 3-row alphabet is TRUNCATED: of sixteen letters only about
  five stay distinguishable and the rest degenerate into the same pair of 2-row marks — the
  vocabulary, which IS the axis, dies, and what is left is a dashed line between rules, the 40th
  dentil again.
  **The standing edge rule, in the horizontal:** the bright element here is a CONTINUOUS HORIZONTAL
  rule, so it goes wrong as the mirror of the 49th's bright vertical stem — a rule row landing on
  the topmost row of the dome draws a bright bar across the crown, detached from the piece. `VPHASE`
  is set so a component's top row lands on the channel FLOOR, and any rule pixel with nothing opaque
  above it, or on a part only 1px across, drops to the rule's underside stop. `HPHASE` centres a
  LETTER on the piece rather than letting the text start on the left bounding edge, since a letter
  cut in half by the silhouette on both sides reads as two ticks, not as text.
  Palette — five STONE stops (rule top / rule underside / cut shadow / bed / floor) plus two INLAY
  stops per class: warrior OATHSTONE, cold grey granite ruled in quicksilver wire; mage OBSIDIAN
  STELE, a violet-black volcanic glass (the first violet ground in the set) inlaid in witchfire
  cyan-green; ranger BOG OAK, black-brown drowned timber with pale gold cut across the grain, pushed
  yellow-green deliberately clear of tan skin. Every bed stop stays well clear of pure black — a
  HELMET constraint, not a taste one, since the finishing pass carves the visor as black eye and
  mouth pixels and a near-black bed swallows the face slit (the lesson the 49th paid for).
  Slots: chest Runecarved Cuirass `shirt_%s_legendary50`, legs Runecarved Chausses
  `pants_%s_legendary50`, boots Runecarved Sabatons `boots_%s_legendary_runic`, helmet Runecarved
  Helm `helmet_%s_legendary50`. Generator `scripts/gen_runic_axis50.py` (repaint-only, QA-safe by
  construction — the inscription painted ONLY onto already-opaque body pixels; self-contained NumPy
  `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()` in-line,
  sixth generator to do so after axes 45–49; carries `--vocab` for an ASCII dump of the alphabet and
  a sample inscription, `--swatch` for the bare motif on a synthetic notched/waisted test plate, and
  `--sweep` for the BAND_P sweep on a real torso AND a real leg). 24 sheets: **sprite_qa ALL 24
  PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45/46/47/48/49 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry; all 24 carry the `TaskQuestFinish=2026-08-01.6` stamp.
  Staged in `_runic_legendary_preview/`, `_runic_legs_preview/`, `_runic_boots_preview/`,
  `_runicdome_helmet_preview/`. Previews: `_PREVIEW_runic_legendary.png`, `_PREVIEW_runic_legs.png`,
  `_PREVIEW_runic_boots.png`, `_PREVIEW_runicdome_helmet.png` (built by `scripts/preview_axis50.py`);
  zooms `_ZOOM_runic_chest.png`, `_ZOOM_runic_head.png`; diagnostics `_diag_runic_swatch.png` (bare
  motif, all 3 classes) and `_diag_runic_sweep.png` (the BAND_P=10/9/8/7/6 sweep on a real torso and
  leg).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add **L52** legendary
  LOOT_TABLE entries per slot/class (m + f).

- **49th net-new-geometry axis — DENDRITE / FROST-FERN (recursive branching crystal), all 4 slots**
  (2026-08-08): a field of raised vertical STEMS from which FRONDS spring at 45° in alternating
  succession up the stem, each frond splitting at its tip into a FORK of two shorter members — the
  branching habit of a native-metal dendrite in ore, and of frost on a cold window.
  **This is the FIRST BRANCHING AXIS IN FORTY-NINE — the first whose motif is a TREE.** The subject
  is DESCENT: an element's identity comes from its distance from the root ALONG THE STRUCTURE, not
  from its position on the plate and not from its size class. The three families it could be
  confused with each fail that in a different way. The ruled-cell axes (11th–45th) stamp a CLOSED
  FIGURE on a lattice; a closed figure has an inside and an outside, every part of it is coequal,
  and there is no parent and no child anywhere in the family. The line axes — 11th fluting, 22nd
  wave, 23rd meander, 24th spiral, 30th cable, 39th guilloche, 42nd strigil, 43rd gadroon, 44th
  zigzag — run UNBRANCHED members: a meander turns corners and a cable crosses its neighbour, but
  follow any of their lines end to end and it has exactly two ends and no forks. The 46th craquelure
  is the instructive near miss, the only prior axis with genuine 3-way junctions, but a craquelure
  net is a PARTITION — its junctions are unordered, every hairline coequal, no root, no growth
  direction, and cutting one member leaves a net rather than orphaning a subtree; a dendrite is
  ACYCLIC and DIRECTED. The 48th cosmati is the other near miss: it also puts several sizes on the
  plate, but its ranks are DISJOINT STAMPED ELEMENTS whose rank IS their size, touching nothing and
  related only by the bay they share, whereas here the ranks are CONNECTED and the rank IS the
  connection — a fork member is one because of what it grows out of, and would still be one if it
  were as long as its parent. The 47th mokume nests closed loops, and nesting is containment, not
  descent. **TAPER, and the one honest compromise at this scale:** a real dendrite's members get
  THINNER each generation, but at 13px the stem is already 1px, so thickness cannot carry rank and
  the axis spends its two remaining channels on it — LENGTH (stem continuous, frond `FROND_L`=3,
  fork `BARB_L`=1) and VALUE (the ramp steps down one stop per generation, and a frond dims again
  along its own length as it runs away from the stem). **RELIEF is the first in the set carried by
  what the ornament does TO THE GROUND rather than by a gradient across the ornament:** the crystal
  stands proud of a flat matrix, so a ground pixel whose UPPER-LEFT neighbour belongs to the tree
  takes the darker of two bedding stops — a genuine cast shadow, and the only relief cue available
  to a figure that is 1px wide everywhere. Geometry: the tile is not a per-pixel membership test but
  GROWN, by a recursive `grow()` that paints a member then spawns its children, writing with
  wraparound into a (`FROND_P` x `TRUNK_P`) periodic buffer — the code expresses descent because
  descent is the subject. `TRUNK_P = 2*FROND_L+1 = 7` so opposing fronds from adjacent stems
  interlock with a 1px matrix gap and never fuse into a lattice.
  **THREE TUNING LESSONS, all three paid for on the first cut:**
  (1) *A branching axis needs the child on the TIP, not on the flank.* The first cut sprouted
  lateral barbs off the middle of each frond on the MIRRORED diagonal; because a mirrored barb
  points back toward the stem it drops into the gap between one frond and the next, and coverage
  went to 50% and the whole field collapsed into an undifferentiated checker with no generation
  legible. Forking only at the tip (two children on the axis directions bracketing the parent's
  heading) keeps the matrix open, and an open matrix is what lets a 1px tree read as a tree at all.
  (2) *This is the first axis whose pitch is bounded on BOTH sides by a collapse into an OLDER AXIS
  rather than into mush.* Swept `FROND_P` at 12/10/8/6/4 (`--sweep`, on a real torso AND a real
  leg): at 12 the torso fits ONE frond per stem and the leg none, leaving bright bare verticals on
  a dark ground — that is the **11th fluting**; at 10 the leg still goes a whole stem without a
  frond; at **8** the torso carries 2–3 fronds per stem with the fork intact and open matrix
  between, the leg carries 2, and stem/frond/fork are simultaneously legible — chosen; at 6 the
  fronds of one stem run into the fronds of the next, the eye joins neighbouring diagonals across
  the closed gaps, and the field reads as one continuous diagonal weave — that is the **16th twill
  herringbone**; at 4 coverage passes 45% and it is a checker of 1px marks. Judged on the wide
  `--swatch` plate, where the crowding shows a pitch before it shows on a real torso.
  (3) *NO BRIGHT RIM — the standing helmet rule, in the other direction.* The stem is the brightest
  stop in the ramp and runs unbroken top to bottom, so with the lattice unphased the `lx==0` stem
  landed exactly on the component's leftmost column and the warrior dome came out as **two white
  bars framing the face** with the ornament invisible behind them, and the mage hat grew a white bar
  hanging beside the cheek. Two fixes, both kept: the lattice is PHASED by `(w//2) % TRUNK_P` so a
  stem runs down the CENTRE of each component (which is also the right composition for armour — one
  bright spine up the breastbone and over the crown), and any stem pixel where the body is not
  opaque on BOTH sides (a hat brim, a hood flap, a boot cuff) is DEMOTED to the frond stop, so no
  1px protrusion can carry the extreme of the ramp. The silhouette edge is never allowed the top or
  the bottom of the ramp, whichever end it is.
  **A BEDDING LESSON THAT IS A HELMET CONSTRAINT, NOT A TASTE ONE:** the matrix BASE must stay well
  clear of pure black, because the finishing pass carves the visor as black eye and mouth pixels and
  a near-black matrix swallows the face slit outright — a first cut at warrior (34,34,42) / mage
  (16,26,46) produced a featureless dark lump with no readable face. Both stops were lifted; final
  warrior (50,50,62)/(28,28,36) magnetite, mage (36,52,82)/(18,28,50) black ice, ranger
  (66,48,30)/(36,26,16) umber gossan. Palette is a four-stop metal ramp per class spent one stop per
  generation: warrior native SILVER in magnetite, mage HOARFROST on black ice (the coldest ramp in
  the set), ranger native GOLD in umber gossan, pushed to a saturated amber deliberately clear of
  tan skin — the lesson the 47th's rose gold cost a whole cut to learn.
  Slots: chest Dendrite-Cuirass `shirt_%s_legendary49`, legs Dendrite-Chausses
  `pants_%s_legendary49`, boots Dendrite-Sabatons `boots_%s_legendary_dendrite`, helmet
  Dendrite-Dome `helmet_%s_legendary49`. Generator `scripts/gen_dendrite_axis49.py` (repaint-only,
  QA-safe by construction — the tree painted ONLY onto already-opaque body pixels; self-contained
  NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` + `save_finished()`
  in-line, fifth generator to do so after axes 45–48; carries `--tile` for an ASCII dump of the
  grown tile, `--swatch` for the bare motif on a synthetic notched/waisted test plate, and `--sweep`
  for the FROND_P sweep on a real torso AND a real leg). 24 sheets: **sprite_qa ALL 24 PASS**
  (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45/46/47/48 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry; all 24 carry the `TaskQuestFinish=2026-08-01.6` stamp.
  Staged in `_dendrite_legendary_preview/`, `_dendrite_legs_preview/`, `_dendrite_boots_preview/`,
  `_dendritedome_helmet_preview/`. Previews: `_PREVIEW_dendrite_legendary.png`,
  `_PREVIEW_dendrite_legs.png`, `_PREVIEW_dendrite_boots.png`, `_PREVIEW_dendritedome_helmet.png`
  (built by `scripts/preview_axis49.py`); zooms `_ZOOM_dendrite_chest.png`, `_ZOOM_dendrite_head.png`;
  diagnostics `_diag_dendrite_swatch.png` (bare motif, all 3 classes) and `_diag_dendrite_sweep.png`
  (the FROND_P=12/10/8/6/4 sweep on a real torso and leg).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add L51 legendary LOOT_TABLE
  entries per slot/class (m + f).

- **48th net-new-geometry axis — COSMATESQUE / OPUS SECTILE (hierarchical stone inlay), all 4 slots**
  (2026-08-07): a field of square marble PANELS, each framed by a 1px pale FILLET band and filled
  with a large central ROUNDEL of porphyry ringed by four small square TESSERAE of a second stone —
  the quincunx bay of a Cosmati pavement, the inlaid floors of the Roman basilicas.
  **This is the FIRST HIERARCHICAL, MULTI-SCALE AXIS IN FORTY-EIGHT.** Every one of the
  forty-seven prior axes has exactly ONE characteristic element size. The ruled lattices (11th–45th)
  stamp a single congruent cell on a lattice, so every element is the same size by construction; the
  46th craquelure broke periodicity but its shards still all sit in one size band (they vary by a
  jitter, not a scale factor, and a field of slightly-different shards still reads as "one size of
  shard"); the 47th mokume broke positionality but every lamina in the nest is the same PB thick.
  Cosmatesque puts THREE DELIBERATELY DIFFERENT SIZES on the plate at once in a fixed ratio —
  an 8px panel, a 5px roundel, a 2px tessera, **8 : 5 : 2** — so the eye reads a large form, a medium
  form and a small form simultaneously and infers a COMPOSITION rather than a texture. That is the
  subject of the axis: not a motif but a hierarchy of motifs (four ranks counting the 1px crossing
  node). The palette carries the second half of the argument — **MATERIAL IS A FUNCTION OF SCALE**:
  the big element is porphyry, the small element a contrasting marble, the frame white marble, the
  bedding dark. Three stones, one per rank, which is how a real Cosmati panel is cut and which is
  what keeps the hierarchy alive where the silhouette is too narrow for a whole bay — a 4–5px limb
  still shows fillet + roundel edge + a corner stone in three distinguishable stones. (Contrast the
  47th, whose two ramps alternate band-to-band with no regard to size, because its subject was two
  metals forge-welded rather than a composition.) Geometry per opaque body pixel in component-local
  (lx,ly): `ax,ay = lx%P, ly%P` with **P=PANEL=8**; `ax==0 or ay==0` → FILLET (and `ax==0 and ay==0`
  → the brighter NODE); else interior `ix,iy = ax-1,ay-1` over `0..S-1`, `S=P-1`, `c=(S-1)/2`:
  `|ix-c|+|iy-c| <= RR=2.0` → ROUNDEL, else both `ix` and `iy` within `TESS=2` of an interior corner
  → TESSERA, else GROUND (the bedding/spandrel). Relief follows scale rather than being uniform:
  opus sectile is FLUSH inlay, so nothing is embossed — instead the roundel, the only element wide
  enough to hold a gradient, is a polished disc lit `lit=(-dx-dy)/(2·RR)` (>0.34 HI / <−0.34 LO /
  else MID), while a 2x2 tessera can carry exactly ONE highlight so its upper-left pixel takes the
  bright stone and the other three the base — one pip. Rendering a 5px element with a three-tone
  gradient and a 2px element with a single pip is not a shortcut, it is what keeps the two ranks
  distinguishable at 1x. **TUNING — the pitch failure mode here is different from either of the last
  two axes and is worth keeping:** the 46th needed a SMALL pitch (an aperiodic field must show
  several cells before the eye accepts they differ) and the 47th needed a pitch set by the THINNEST
  part (a contour nest's band count is the piece's half-thickness). A hierarchical axis needs a pitch
  large enough to hold **ALL THREE RANKS INSIDE ONE BAY AT ONCE** — otherwise the composition
  collapses to whichever rank survives, and that surviving rank is then indistinguishable from an
  older single-scale axis. Swept 10/9/8/7/6 (`--sweep`, on a real torso AND a real leg): at 10 one
  bay is wider than the 13px torso, so the chest shows ONE roundel adrift in bedding with the frame
  reduced to a stray edge line — an impoverished 28th concentric; at 9 the frame reads on two sides
  but the tesserae come in unpaired and both legs go a whole bay without a roundel; at **8** the
  torso holds ~1.7 bays across and 2 down with frame, roundel and all four tesserae legible together
  and a thin limb still showing three stones — chosen; at 7 the interior drops to 6px and the
  roundel's outer pixels become ORTHOGONALLY ADJACENT to the tesserae (interior (1,2) roundel vs
  (1,1) tessera), fusing the quincunx into one blob per bay — a fused blob is a single element, so
  the hierarchy collapses to one rank plus a frame, i.e. the 17th ashlar with a filling; at 6 it is
  worse than fused — at S=5 the roundel mathematically SWALLOWS the tessera cells outright
  (`|1-2|+|1-2| = 2 <= RR`) and the small rank does not render at all. Distinct from 17th ashlar
  (rectangular OUTLINE cells on a bond — the nearest neighbour by silhouette, and the separation IS
  the axis: an ashlar cell is EMPTY, one scale, a plain outline; a Cosmati bay is a frame with a
  composition inside it in two further sizes and two further stones), 14th lattice / 19th honeycomb /
  20th trellis / 21st chainmail (congruent one-scale nets), 37th coffer (one sunken bevelled cell
  with nothing set into it), 13th studwork (a point-grid of rivets — only the small rank, on no
  frame), **25th argyle** (a SOLID-FILLED diagonal-diamond field — named explicitly because at 8px
  the roundel resolves to a diamond, but argyle's diamonds are one size, tile edge-to-edge with
  nothing between them, and have no frame and no subordinate stones), 26th tartan (crossing bold
  bands with a brighter overlap node — the nearest thing to the fillet-and-node grid, but the field
  between tartan's bands is plain cloth with nothing set into it and no second or third size), 46th
  craquelure (irregular but single-scale, and a partition rather than a composition), 47th mokume
  (shape-conformal, but every lamina the same thickness). **A SECOND PALETTE LESSON, and it is about
  which element the eye colour-matches on:** a first cut gave all three classes a warm gold small
  rank (giallo / gold / copper) and warrior and mage came out indistinguishable at 1x — the tesserae
  are the busiest element on the plate, so they, not the roundel, are what class identity actually
  hangs on. Warrior therefore takes VERDE ANTICO against its porphyry, which is also the canonical
  Roman pairing (the two stones a Cosmati panel is literally cut from); mage keeps gold against
  lapis; ranger keeps copper, warm-brown enough not to read as mage's gold. Final: warrior imperial
  porphyry roundel + verde antico tesserae + carrara fillet + basalt bedding, mage lapis lazuli +
  gold + moonstone + indigo slate, ranger verde antico serpentine + copper + ivory + bog oak. Every
  pale value is deliberately clear of the skin palette — on a narrow female chest the fillet grid is
  most of what is visible, and a warm off-white would read as bare skin at 1x, the lesson the 47th's
  rose gold cost a whole cut to learn. Slots: chest Cosmati-Cuirass `shirt_%s_legendary48`, legs
  Cosmati-Chausses `pants_%s_legendary48`, boots Cosmati-Sabatons `boots_%s_legendary_cosmati`,
  helmet Cosmati-Dome `helmet_%s_legendary48`. Generator `scripts/gen_cosmati_axis48.py`
  (repaint-only, QA-safe by construction — panels painted ONLY onto already-opaque body pixels;
  self-contained NumPy `label4()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` in-line,
  fourth generator to do so after axes 45–47; carries `--swatch` for the bare motif on a synthetic
  notched/waisted test plate and `--sweep` for the PANEL sweep on a real torso AND a real leg, which
  is how the pitch was judged). 24 sheets (4 slots x 3 classes x m+f): **sprite_qa ALL 24 PASS**
  (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45/46/47 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry; all 24 carry the `TaskQuestFinish=2026-08-01.6` stamp.
  Staged in `_cosmati_legendary_preview/`, `_cosmati_legs_preview/`, `_cosmati_boots_preview/`,
  `_cosmatidome_helmet_preview/`. Previews: `_PREVIEW_cosmati_legendary.png`,
  `_PREVIEW_cosmati_legs.png`, `_PREVIEW_cosmati_boots.png`, `_PREVIEW_cosmatidome_helmet.png`
  (built by `scripts/preview_axis48.py`); zooms `_ZOOM_cosmati_chest.png`, `_ZOOM_cosmati_head.png`;
  diagnostics `_diag_cosmati_swatch.png` (bare motif, all 3 classes) and `_diag_cosmati_sweep.png`
  (the PANEL=10/9/8/7/6 sweep on a real torso and leg).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add L50 legendary LOOT_TABLE
  entries per slot/class (m + f).

- **47th net-new-geometry axis — MOKUME / CONTOUR-LAMINATION (shape-conformal metal laminae), all 4 slots**
  (2026-08-07): a forged billet of alternating metal LAMINAE ground back until the layers surface as
  a nest of closed CONTOUR BANDS running PARALLEL TO THE EDGE OF THE PIECE — the ring figure of
  Japanese mokume-gane, and the figure a topographic map draws around a hill.
  **This is the FIRST SHAPE-CONFORMAL AXIS IN FORTY-SEVEN.** Every one of the forty-six prior axes
  computes tone from a function of ABSOLUTE POSITION, `tone = f(lx, ly)` — the pixel's coordinates
  inside the component bbox. That is true of the ruled lattices (11th–45th) *and* of the 46th, which
  broke periodicity but is still a jittered Voronoi evaluated at a position: the pattern is stamped
  on from outside and the silhouette merely crops it, so sliding the body one pixel left shows a
  different part of the wallpaper. Mokume computes tone from the DISTANCE TO THE SILHOUETTE,
  `tone = f(d(x,y))`, with d the chamfer distance transform of the component's own opaque mask.
  The ornament is therefore a property OF THE PIECE: every band is an inward offset of the outline,
  so the figure wraps a boot differently from a breastplate, flows around the arm gap instead of
  being cut by it, pinches where the plate necks, and closes into an island at the thickest point.
  Chamfer d (orthogonal 1, diagonal √2) by min-plus relaxation — self-contained NumPy `chamfer()`,
  **no scipy** — so the outermost body pixel sits at d=1. Band 0 is the single outermost ring
  (`d <= RIM_D=1.5`); behind it `b = 1 + floor((d-RIM_D)/PB)` with **PB=1.7**. `b%2==0` → PALE
  lamina ramp, `b%2==1` → DARK. A pixel within `SEAM_PX=0.85` of a band's **INNER** boundary is the
  SEAM, the step down to the next lamina, and takes that ramp's LO. Lighting is genuinely 3D and
  follows the band: the lamina's outward normal is −grad(d), so
  `lit = (gx+gy)/(√2·|grad d|)` → `>0.30` HI / `<−0.30` LO / else MID, and each band is bright along
  its upper-left arc and falls away along its lower-right arc all the way round the nest. Where
  `|grad d| < 0.12` (the medial axis, the flat top of the mound) the normal is undefined → MID.
  **THREE DESIGN RULES WORTH KEEPING:** (1) *the rim band must be the PALE metal.* A contour axis
  necessarily puts its outermost band on the silhouette, and the standing rule is that a dark
  full-silhouette rim swamps a coloured or patterned dome — running the outer lamina bright turns
  that unavoidable edge band into a chased bright outline instead of the known failure mode, and the
  SEAM is pinned to the band's INNER edge for the same reason. (2) *the rim band gets its own
  thinner allotment (1px), not a full PB.* First cut gave band 0 a full lamina; because a contour
  nest counts inward from the rim that put the widest palest band on the outside of everything and
  the alternation only began two pixels in — thin limbs came out a flat sheet of one metal and the
  torso read as "silver plate with a dark inlay" rather than as a laminate. (3) *pitch is set by the
  THINNEST part that must read, not the widest.* This is the exact mirror of the 46th's lesson: an
  aperiodic axis needs a SMALL pitch because it must show several cells; a contour nest's band count
  is set by the piece's HALF-THICKNESS, because the nest runs from rim to medial axis and stops — a
  ~13px torso is ~7px to its medial axis but a 4–5px limb is barely 2. Swept 2.6/2.3/2.0/1.7/1.4
  (`--sweep`): at 2.6–2.3 a 4px limb holds ONE band and the whole leg goes a single flat metal; at
  2.0 limbs alternate but the torso stops at three bands and still reads concentric; at 1.4 the
  0.85px seam is 60% of the lamina so every band is mostly its own shadow line. **1.7** gives limbs
  rim+core and the torso 4–5 bands with the waist pinch and sternum island both legible.
  Distinct from 28th concentric (CIRCLES of fixed radius step around *tiled centres* on a lattice —
  many identical ring families, positional; mokume has ONE nest per component, its bands are not
  circles and no two are similar), 24th spiral (a single continuous curve winding into tiled
  centres; mokume bands are closed and disjoint), 21st chainmail (a lattice of overlapping circles),
  15th scale / 34th seigaiha (identical arcs and fans stamped on a lattice), 11th fluting / 42nd
  strigil / 43rd gadroon / 44th zigzag (linear ridges in a FIXED direction — a mokume band changes
  direction continuously and returns to where it started), 46th craquelure (aperiodic, but a
  PARTITION into cells meeting at 3-way junctions; mokume has no cells and no junctions, only
  disjoint nested loops), and from a plain "outline + inner outline" (the nest is 3–5 bands deep in
  alternating METALS with a normal-lit round). First palette built on **TWO independent three-tone
  metal ramps** instead of one five-tone quintet — the subject is literally two metals forge-welded,
  and alternating whole ramps band-to-band is what makes the laminae read as different MATERIALS
  rather than different brightnesses of one: warrior shakudo (blue-black) + FINE SILVER, mage niello
  (violet-black) + ROSE GOLD, ranger kuromido (chocolate-black) + WHITE BRONZE. The mage rose gold
  is deliberately pushed PINK, not peach — a first cut at (146,84,68)/(214,140,116)/(252,208,188)
  was a warm tan and, because the female chest is narrow enough that the rim band is most of what
  you see of it, the whole robe read as BARE SKIN at 1x. **Any pale ramp on this axis must clear the
  skin palette**, since the rim band is the one part of a contour nest guaranteed to be visible on
  every piece however thin. Slots: chest Mokume-Cuirass `shirt_%s_legendary47`, legs Mokume-Chausses
  `pants_%s_legendary47`, boots Mokume-Sabatons `boots_%s_legendary_mokume`, helmet Mokume-Dome
  `helmet_%s_legendary47`. Generator `scripts/gen_mokume_axis47.py` (repaint-only, QA-safe by
  construction — bands painted ONLY onto already-opaque body pixels; self-contained NumPy `label4()`
  and `chamfer()`, NO scipy; calls `sprite_finish.finish_array(arr, dst)` in-line, third generator
  to do so after axes 45–46; carries `--swatch` for the bare motif on a synthetic notched/waisted
  test plate and `--sweep` for the PB sweep on a real torso AND a real leg, which is how the pitch
  was judged). 24 sheets (4 slots x 3 classes x m+f): **sprite_qa ALL 24 PASS** (helmets
  `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask
  parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m) / +440 (f)
  px — identical to the axis-45/46 figures, i.e. the finishing pass's asymmetric shoulder/pauldron
  caps, not stray geometry. Staged in `_mokume_legendary_preview/`, `_mokume_legs_preview/`,
  `_mokume_boots_preview/`, `_mokumedome_helmet_preview/`. Previews:
  `_PREVIEW_mokume_legendary.png`, `_PREVIEW_mokume_legs.png`, `_PREVIEW_mokume_boots.png`,
  `_PREVIEW_mokumedome_helmet.png` (built by `scripts/preview_axis47.py`); zoom
  `_ZOOM_mokume_chest.png`; diagnostics `_diag_mokume_swatch.png` (bare motif, all 3 classes) and
  `_diag_mokume_sweep.png` (the PB=2.6/2.3/2.0/1.7/1.4 sweep on a real torso and leg).
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add L49 legendary LOOT_TABLE
  entries per slot/class (m + f).

- **46th net-new-geometry axis — CRAQUELURE / KINTSUGI (crackle-glaze shard field), all 4 slots**
  (2026-08-07): an all-over field of IRREGULAR CONVEX GLAZE SHARDS divided by a branching network of
  hairline FRACTURES filled with bright metal — a crazed ceramic glaze mended in the kintsugi manner.
  **This is the FIRST APERIODIC AXIS IN FORTY-SIX.** Every one of the forty-five prior axes is
  strictly periodic: one congruent cell stamped on a lattice, so every cell is the same shape and
  size and its edges run in two or three fixed directions. Craquelure has NO repeating cell at all —
  the field is a Voronoi partition of a JITTERED point set, so every shard is a different polygon
  with a different area, a different edge count and edges at arbitrary angles, and its vertices are
  3-way Y-junctions rather than the 4-way crossings of a ruled or woven net. That irregularity IS
  the ornament. Seeds sit on a grid of pitch **PX=4.5** in component-local coords, each displaced by
  a deterministic per-cell jitter of up to **JIT=1.55** px hashed from the integer cell index (so a
  sheet regenerates bit-identically — verified by md5 — and the m/f sheets of an item crack along
  the same lines). For each opaque body pixel the nine candidate seeds in the surrounding 3x3 block
  give d1 (nearest), d2 (runner-up) and the owning shard's hash; the Voronoi EDGE FIELD is
  `e = d2 - d1`, zero exactly on a shard boundary. `e<=0.13` → FISSURE CORE (RIM) / `e<=0.64` →
  FISSURE (HILIT) / else SHARD INTERIOR. Using `d2-d1` rather than a distance-to-line test is what
  keeps the fissure ONE PIXEL wide of its own accord all the way round every polygon and closes it
  exactly at the Y-junctions — no edge list to walk, no seam to mis-join. Shard interior: each shard
  is a shallow dome under the upper-left light, `lit = (-ox-oy)/2.3` from the owning seed —
  `lit>0.55` MID (lit crown) / `lit<-0.35` GROUND / else SHADOW; then each shard gets its OWN kiln
  depth (one shard in six a level lighter, one in six a level darker, from its hash) so neighbouring
  plates sit at visibly different glaze densities as a real crackle glaze does; finally
  `e<=1.0 and lit<0` → GROUND, the plate lip tipping down into the crack, which is what makes the
  shards read as separate raised pieces rather than a flat printed net. Because `e` collapses over a
  WIDER area at a 3-way junction than along a straight run, the RIM tone lands mostly on the
  junctions — the metal reads as POOLING where three cracks meet, exactly as kintsugi does.
  **TUNING NOTE — two cuts were thrown out first, and the first one is the lesson:** the sibling
  axes sit at a cell pitch of 6-9 px (39th guilloche PX8/PY7, 45th arcade PX7/PY9) and the first cut
  copied that at PX=6 — wrong for this motif and wrong for a generalizable reason. *A periodic axis
  only has to show ONE cell for the eye to infer the whole field; an APERIODIC one has to show
  SEVERAL, because the whole subject is that no two cells are alike.* At PX=6 a ~13px torso holds
  barely two shards, so a single crack ran across an otherwise flat plate and read as a scratch, not
  a crackle; a sweep at 6/5/4.5/4/3.5 settled on 4.5 (below 4 the shards drop under ~4 interior px
  and the field turns to noise). Second cut: `E_VEIN=1.20` gave a 2-3px vein that ate more of the
  field than the shards did — the crack must be THINNER than the plates it divides, hence 0.64.
  JIT was swept 1.35/1.55/1.75/1.95: at 1.35 too many bisectors still line up with the base grid and
  long dead-straight vein columns show through — the exact periodic look this axis exists to avoid.
  The repeated motif is AN IRREGULAR FIELD OF CONVEX GLAZE SHARDS DIVIDED BY A BRANCHING HAIRLINE
  FRACTURE NET; none of the 45 prior axes occupy it. The other "outline net" axes are the ones to
  separate it from and the separation is categorical — 14th lattice (identical congruent DIAMONDS,
  two fixed edge directions, 4-way crossings), 17th ashlar (identical RECTANGLES on a bond), 19th
  honeycomb (identical regular HEXAGONS), 20th trellis (identical TRIANGLES, three fixed
  directions), 21st chainmail (closed overlapping CIRCLES — not a partition of the surface at all),
  33rd octagram / 32nd quatrefoil (a single stamped star/rosette repeated on a lattice): in every
  one of those the cell is the SAME cell everywhere. Also not 29th houndstooth (jagged but strictly
  periodic woven check), 35th facet / 36th quilt (regular raised pyramids / regular diamond
  cushions), 37th coffer (sunken congruent rectangles), 39th guilloche (an interlace, not a
  partition), 45th arcade (identical round-headed niches on piers — the most rigidly periodic axis
  in the set). First FIRED-CERAMIC palette (45th arcade broke the metal streak with carved masonry;
  this is glaze), and the first all-over axis where the LINE is the BRIGHT element and the FIELD the
  dark one, so it cannot be confused at a glance with the 45th's pale stone or the 43rd's gilt
  reeds: warrior tenmoku iron-black & persimmon glaze mended in GOLD, mage aubergine iron-purple
  glaze mended in PLATINUM (held deliberately down off pure white — a first cut at
  (196,198,216)/(250,252,255) read as light noise rather than metal on dark glaze), ranger celadon
  ash-green glaze mended in COPPER. Slots: chest Craquelure-Cuirass `shirt_%s_legendary46`, legs
  Craquelure-Chausses `pants_%s_legendary46`, boots Craquelure-Sabatons
  `boots_%s_legendary_craquelure`, helmet Craquelure-Dome `helmet_%s_legendary46`. Generator
  `scripts/gen_craquelure_axis46.py` (repaint-only, QA-safe by construction — net painted ONLY onto
  already-opaque body pixels; self-contained NumPy `label4()`, NO scipy; calls
  `sprite_finish.finish_array(arr, dst)` in-line, second generator to do so after axis 45; carries a
  `--swatch` flag that renders the bare motif for all 3 classes with no sheets written, which is how
  the pitch sweep was judged). 24 sheets (4 slots x 3 classes x m+f): **sprite_qa ALL 24 PASS**
  (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame
  opaque-mask parity vs source **18/24 exact, 0 dropped on all 24**; the 6 chests each gain +510 (m)
  / +440 (f) px — identical to the axis-45 figures, i.e. the finishing pass's asymmetric
  shoulder/pauldron caps, not stray geometry. Staged in `_craquelure_legendary_preview/`,
  `_craquelure_legs_preview/`, `_craquelure_boots_preview/`, `_craqueluredome_helmet_preview/`.
  Previews: `_PREVIEW_craquelure_legendary.png`, `_PREVIEW_craquelure_legs.png`,
  `_PREVIEW_craquelure_boots.png`, `_PREVIEW_craqueluredome_helmet.png` (built by
  `scripts/preview_axis46.py`); zooms `_ZOOM_craquelure_chest.png`, `_diag_craquelure_zoom.png`
  (chest/helm/legs/boots at 22x), `_diag_craquelure_swatch.png` (the bare motif on a flat field, all
  3 classes), `_diag_craq_sweep.png` (the PX=6/5/4.5/4/3.5 pitch sweep on a real torso),
  `_diag_craq_jit.png` (the JIT sweep). **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L48 legendary LOOT_TABLE entries per slot/class (m + f).

- **45th net-new-geometry axis — ARCADE / BLIND ARCADING (Romanesque wall arcade), all 4 slots**
  (2026-08-06): a run of ROUND-HEADED RECESSED NICHES, each a stepped semicircular ARCH springing
  from a shared vertical PIER, with an IMPOST block at the springing — the blind wall arcade that
  bands Romanesque apses, font bowls and cloister walls. This is the first axis whose repeating
  cell is a piece of ARCHITECTURAL STRUCTURE (arch + supporting pier + impost + the recess they
  enclose) rather than a ridge, a tile, a boss or a woven band. Bay pitch PX=7 across (5px niche +
  2px shared pier), course pitch PY=9 down, springing at row 3. Rather than threshold a circle —
  which does not survive at this scale, see the tuning note — the NICHE OPENING is authored as an
  explicit stepped round-arch profile and the ring is derived as its 4-neighbour boundary, so the
  head is guaranteed to close in whole pixels: per opaque body pixel in component-local (lx,ly),
  `yy = ly%PY`, `dx = (lx%PX)-3`, opening half-width = **wall band (closed) at yy=0 / 0 at yy=1 /
  1 at yy=2 / 2 otherwise** (a 1→3→5 px step). Open pixel = sunken NICHE → GROUND (deepest tone).
  Closed pixel with an open 4-neighbour = the ARCH RING / JAMB / PIER: open-below-and-right → RIM
  (upper-left corner) / open-below → HILIT (crown & haunch) / open-right → RIM (left jamb, lit) /
  open-left → MID (right jamb falling away) / open-above → SHADOW (sill). Closed with no open
  neighbour: `yy==3 & |dx|>=2` → IMPOST block on the pier → HILIT, else flat SPANDREL/wall band →
  SHADOW. Piers are SHARED (the |dx|=3 column of one bay abuts |dx|=-3 of the next → one 2px pier,
  lit left column / shaded right), so the arch feet land exactly on a pier. Uses all FIVE tones
  with distinct jobs — unusually, GROUND is load-bearing here (sunken niche) with SHADOW as the
  wall plane behind, so the recess never merges with the wall it is cut into. **TUNING NOTE — two
  cuts were thrown out first:** PX=5/R=2.3 with a 2px-thick roll filled the whole head and the
  axis degenerated into a plain rectangular grid; PX=6/R=2.9 with a 1px ring gave a rectangle with
  clipped top corners. A 5px opening is the MINIMUM that can show an arch at all (the 1-3-5 step),
  hence PX=7. The repeated motif is A COLONNADE OF ROUND-HEADED RECESSED NICHES ON PIERS; none of
  the 44 prior axes occupy it. Distinct from 11th fluting / 43rd gadroon (bare parallel
  channels/rods running the full height — no arch, no impost, no enclosed cell; the arcade shaft is
  a SHORT pier that stops at an impost and CARRIES an arch), 40th dentil (its fillet is the nearest
  thing to an impost, but a dentil tooth is a plain rectangular block with nothing springing from
  it), 15th scale (a bare one-way imbricated arc — the arcade arch is a modelled ring standing on
  piers over a sunken bay), 31st ogee (CUSPED POINTED oval cell from two identical curved ribs —
  the arcade cell is a SEMICIRCULAR head on STRAIGHT vertical legs, flat-bottomed), 34th seigaiha
  (nested triple arcs opening downward, overlapping — the arcade arch is single, not nested, and
  stands on piers), 37th coffer (sunken RECTANGLE with four flat bevel walls — the arcade niche is
  a sunken ROUND-HEADED cell), 17th ashlar (flat rectangular outline, no relief, no arch).
  First axis to reach for CARVED STONE rather than a metal — it is architecture, so it gets a
  MASONRY quintet all of its own (no metal anywhere in it): warrior rose porphyry & ivory
  (dark maroon-stone / oxblood / dusty rose / pale ivory-pink / white), mage lapis & moonstone
  (midnight blue / deep lapis / azure stone / pale moonstone / white), ranger serpentine & ivory
  (deep pine-stone / serpentine / sage stone / pale ivory-green / white). Slots: chest
  Arcade-Cuirass `shirt_%s_legendary45`, legs Arcade-Chausses `pants_%s_legendary45`, boots
  Arcade-Sabatons `boots_%s_legendary_arcade`, helmet Arcade-Dome `helmet_%s_legendary45`.
  Generator `scripts/gen_arcade_axis45.py` (repaint-only, QA-safe by construction — net painted
  ONLY onto already-opaque body pixels; self-contained NumPy `label4()`, NO scipy). **First
  generator to call `sprite_finish.finish_array(arr, dst)` in-line instead of a bespoke `shade()`**
  — every prior axis was shaded by hand in its own script and backfilled later. 24 sheets (4 slots
  x 3 classes x m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source **18/24 exact, 0
  dropped on all 24**; the 6 chests each gain +510 (m) / +440 (f) px — those are the finishing
  pass's asymmetric shoulder/pauldron caps at frame rows 32-37, ~15 px/frame over 35 frames, i.e.
  the intended sculptural plates, not stray geometry. Staged in `_arcade_legendary_preview/`,
  `_arcade_legs_preview/`, `_arcade_boots_preview/`, `_arcadedome_helmet_preview/`. Previews:
  `_PREVIEW_arcade_legendary.png`, `_PREVIEW_arcade_legs.png`, `_PREVIEW_arcade_boots.png`,
  `_PREVIEW_arcadedome_helmet.png` (built by `scripts/preview_axis45.py`); zooms
  `_ZOOM_arcade_chest.png`, `_diag_arcade_zoom.png` (chest/legs/helm at 14x), `_diag_arcade_swatch.png`
  (the bare motif on a flat field, all 3 classes). **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L47 legendary LOOT_TABLE entries per slot/class (m + f).

- **44th net-new-geometry axis — ZIGZAG / DANCETTE (Norman chevron molding), all 4 slots**
  (2026-07-29): an all-over field of nested, RAISED CONVEX V-RIDGES that fold the plate into a
  stack of chevrons — the classic Romanesque zigzag/dancette run across arch voussoirs and doorway
  orders. This is the ANGULAR member of the linear-ridge family and sits beside its siblings: 11th
  fluting (straight vertical CONCAVE grooves, incised), 43rd gadroon (straight vertical CONVEX
  reeds, raised), 42nd strigil (curved vertical CONCAVE S-flutes, sine-bowed), and now 44th zigzag
  (folded horizontal CONVEX V-ridges, triangle-folded). Where gadroon raises dead-straight vertical
  rods and strigil bows its flutes into a smooth SINE S, zigzag FOLDS its raised ridge with a hard
  TRIANGLE: each ridge runs as a horizontal band whose centre-line is deflected up/down by a
  triangle wave of the column, bending the band into a crisp V — stacked band over band it reads as
  nested chevrons with dead-straight diagonal arms meeting at a sharp point (triangle, never a
  smooth curve). Ridge-band pitch PY=4 down, chevron period PX=6 across, fold amplitude AMP=2
  (~33deg arms). Per opaque body pixel in component-local (lx,ly): t=frac(lx/PX),
  zig=AMP*(2*|t-0.5|) (triangle: 0 at chevron centre, AMP at shared point), phase=(ly+zig)/PY,
  u=frac(phase), c=u-0.5 (crest c=0, quirk valley c=+/-0.5). Shaded ACROSS the band under an
  upper-left light: `|c|>=0.42`=QUIRK valley between chevron ridges (SHADOW, thin sunken line) /
  `-0.42<c<=-0.12`=upper shoulder facing light (RIM) / `-0.12<c<0.12`=folded ridge crest (HILIT) /
  `0.12<=c<0.42`=lower shoulder falling away (MID). The repeated motif is a DENSE FIELD OF NESTED
  RAISED V-CHEVRON RIDGES; none of the 43 prior axes occupy it. Distinct from 11th fluting (straight
  concave incised — zigzag is folded convex raised), 12th lamellar (straight flat horizontal bands —
  zigzag folds each band into a V with convex relief), 16th twill/herringbone (broken texture of
  tiny disconnected dashes — zigzag is continuous full-length V-ridges with relief), 22nd wave (ONE
  smooth SINE ribbon — zigzag is a whole field of hard ANGULAR triangle-folded ridges), 23rd meander
  (turns only 90deg into a rectilinear key — zigzag turns at an ACUTE point into a diagonal V), 42nd
  strigil (SINE-bowed CONCAVE incised flutes — zigzag is TRIANGLE-folded CONVEX raised ridges), 43rd
  gadroon (dead-straight vertical reeds — zigzag folds into horizontal V's). **NOT the old 9th-axis
  "chevron" chest accent** (a single FLAT printed V-stripe on one slot, flagged for 3/4 rework) —
  this is a full-field RAISED convex chevron RELIEF on all four slots; stem is `zigzag` to avoid the
  old chevron files. STORM-FORGED metals with its OWN quintet (NOT the gilt-gold of 43, burnished
  copper/steel-blue/jade of 42, nor cast-bronze cornice of 37-41): warrior storm-forged gunmetal &
  silver (dark-gunmetal / slate / steel / bright-steel / white), mage arcane cobalt (deep-navy /
  indigo / cobalt / sky-blue / white), ranger storm verdigris (dark-iron-green / pine / verdigris /
  pale-jade / pale-mint). Slots: chest Zigzag-Cuirass `shirt_%s_legendary44`, legs Zigzag-Chausses
  `pants_%s_legendary44`, boots Zigzag-Sabatons `boots_%s_legendary_zigzag`, helmet Zigzag-Dome
  `helmet_%s_legendary44`. Generator `scripts/gen_zigzag_axis44.py` (repaint-only, QA-safe by
  construction — net painted ONLY onto already-opaque body pixels; self-contained NumPy `label4()`,
  NO scipy). 24 sheets (4 slots x 3 classes x m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`,
  pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source
  **24/24 exact (0 dropped / 0 strays)**. Staged in `_zigzag_legendary_preview/`,
  `_zigzag_legs_preview/`, `_zigzag_boots_preview/`, `_zigzagdome_helmet_preview/`. Previews:
  `_PREVIEW_zigzag_legendary.png`, `_PREVIEW_zigzag_legs.png`, `_PREVIEW_zigzag_boots.png`,
  `_PREVIEW_zigzagdome_helmet.png` (built by `scripts/preview_axis44.py`); zoom
  `_ZOOM_zigzag_chest.png`. **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add
  L46 legendary LOOT_TABLE entries per slot/class (m + f).

- **43rd net-new-geometry axis — GADROON / REEDING, all 4 slots**
  (2026-07-29): an all-over field of parallel, DEAD-STRAIGHT vertical CONVEX ROUNDED REEDS — fat
  half-round rods standing proud of the plate, separated by a thin sunken quirk line — the classical
  gadrooning/reeding that runs down silver hollow-ware, column shafts and furniture legs.
  Deliberately the INVERSE RELIEF of the 11th axis fluting, exactly as the 37th coffer is the inverse
  relief of the 35th facet: fluting CUTS concave grooves in (groove bottom→shadow, ridge crest→bright
  rim); gadroon RAISES convex reeds out (rounded reed body→lit crown, thin quirk valley between
  reeds→shadow). Reed pitch PX=4.5 across; per opaque body pixel in component-local (lx,ly):
  u=frac(lx/PX), c=u−0.5 (reed crown c=0, quirk valley c=±0.5); under upper-left light
  `|c|>=0.42`=QUIRK valley between reeds (SHADOW, thin sunken line) / `−0.42<c<=−0.12`=left shoulder
  facing light (RIM, brightest catch) / `−0.12<c<0.12`=rounded reed crown (HILIT) /
  `0.12<=c<0.42`=right shoulder falling away (MID). The repeated motif is a DENSE FIELD OF PARALLEL
  CONVEX VERTICAL REEDS; none of the 42 prior axes occupy it. Distinct from 11th fluting (its CONVEX
  INVERSE — raised bright rods+dark quirks vs incised dark channels+bright ridges), 42nd strigil
  (curved concave incised S-flutes vs straight raised convex reeds), 41st bead-and-reel (horizontal
  string of discrete spheres+disks vs continuous vertical rods), 30th cable (braids/crosses two
  strands vs parallel non-crossing reeds). BRIGHT GADROONED PRECIOUS-METAL with its OWN quintet (NOT
  the burnished polished-metal of 42, nor cast-bronze cornice of 37-41): warrior gilt gold
  (dark-bronze / amber / gold / bright-gold / pale-gold-white), mage silvered amethyst (deep-violet /
  plum / lilac / pale-silver / white), ranger antique verdant-gold (deep-forest / bottle / mossy-gold
  / pale-gold-green / pale-mint). Slots: chest Gadroon-Cuirass `shirt_%s_legendary43`, legs
  Gadroon-Chausses `pants_%s_legendary43`, boots Gadroon-Sabatons `boots_%s_legendary_gadroon`,
  helmet Gadroon-Dome `helmet_%s_legendary43`. Generator `scripts/gen_gadroon_axis43.py`
  (repaint-only, QA-safe by construction — net painted ONLY onto already-opaque body pixels;
  self-contained NumPy `label4()`, NO scipy). 24 sheets (4 slots x 3 classes x m+f): **sprite_qa
  ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`);
  per-frame opaque-mask parity vs source **24/24 exact (0 dropped / 0 strays)**. Staged in
  `_gadroon_legendary_preview/`, `_gadroon_legs_preview/`, `_gadroon_boots_preview/`,
  `_gadroondome_helmet_preview/`. Previews: `_PREVIEW_gadroon_legendary.png`,
  `_PREVIEW_gadroon_legs.png`, `_PREVIEW_gadroon_boots.png`, `_PREVIEW_gadroondome_helmet.png`
  (built by `scripts/preview_axis43.py`); zoom `_ZOOM_gadroon_chest.png`. **On approval:** copy the
  24 PNGs to `sprites/preview_assets/char/`, add L45 legendary LOOT_TABLE entries per slot/class
  (m + f).

- **42nd net-new-geometry axis — STRIGIL / STRIGILLATION, all 4 slots**
  (2026-07-29): an all-over field of densely-packed CURVED vertical FLUTES that sweep down the
  plate in a shallow S — the classical strigil ornament carved across Roman sarcophagi and
  bath-house walls. Where the 11th axis fluting runs its grooves DEAD-STRAIGHT, the strigil BENDS
  each flute into a gentle S-curve so the surface reads as a raked field of curved gouged channels.
  Flute pitch PX=4.0 across; each flute bowed by warping its horizontal
  phase with a sine of the row: phase=lx+AMP*sin(2pi*ly/LAM), AMP=1.7, LAM=19 (~one S per
  torso/dome); u=frac(phase/PX), c=u-0.5 (groove bottom c=0, shared ridge crest c=+/-0.5). Per
  opaque body pixel under an upper-left light: `|c|>=0.40`=convex RIDGE crest between flutes (bright
  RIM) / `-0.40<c<=-0.12`=left wall (MID, side away from light) / `-0.12<c<0.12`=groove bottom
  (SHADOW, the deep gouged incision) / `0.12<=c<0.40`=right rising wall (HILIT, faces up-left into
  the light). The repeated motif is a DENSE FIELD OF PARALLEL CURVED S-FLUTES; none of the 41 prior
  axes occupy it. Distinct from 11th fluting (grooves DEAD-STRAIGHT & vertical — strigil BOWS every
  flute into an S), 22nd wave (ONE horizontal sine ribbon — strigil is a whole field of many
  parallel vertical curved grooves), 15th scale (short one-way stacked arcs — strigil flute is one
  continuous full-height channel), 30th cable (braids two strands over-under — strigil flutes run
  parallel, never cross). Reads as POLISHED-METAL GOUGED RELIEF with its OWN metal quintet (NOT the
  cast-bronze cornice metals of 37-41): warrior burnished copper (dark-umber ground / copper shadow
  / rose-copper mid / bright-copper hilit / pale-gold rim), mage burnished steel-blue (slate /
  steel-blue / pale-steel / ice-blue / white), ranger burnished jade-bronze (deep-pine / bottle /
  jade / bright-jade / pale-mint). Slots: chest Strigil-Cuirass `shirt_%s_legendary42`, legs
  Strigil-Chausses `pants_%s_legendary42`, boots Strigil-Sabatons `boots_%s_legendary_strigil`,
  helmet Strigil-Dome `helmet_%s_legendary42`. Generator `scripts/gen_strigil_axis42.py`
  (repaint-only, QA-safe by construction — net painted ONLY onto already-opaque body pixels;
  self-contained NumPy `label4()`, NO scipy). 24 sheets (4 slots x 3 classes x m+f): **sprite_qa
  ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`);
  per-frame opaque-mask parity vs source **24/24 exact (0 dropped / 0 strays)**. Staged in
  `_strigil_legendary_preview/`, `_strigil_legs_preview/`, `_strigil_boots_preview/`,
  `_strigildome_helmet_preview/`. Previews: `_PREVIEW_strigil_legendary.png`,
  `_PREVIEW_strigil_legs.png`, `_PREVIEW_strigil_boots.png`, `_PREVIEW_strigildome_helmet.png`
  (built by `scripts/preview_axis42.py`); zoom `_ZOOM_strigil_chest.png`. **On approval:** copy the
  24 PNGs to `sprites/preview_assets/char/`, add L44 legendary LOOT_TABLE entries per slot/class
  (m + f).

- **41st net-new-geometry axis — BEAD-AND-REEL / ASTRAGAL, all 4 slots**
  (2026-07-29): an all-over field of horizontal COURSES, each course a STRING threaded with an
  alternating rhythm of round convex spherical BEADS and thin lens-shaped REEL disk-spacers seen
  edge-on — the classical astragal bead molding that runs beneath egg-and-dart on cornices, coins
  and picture-frames. Course pitch PY=7 down; along each course round BEADS of radius RB=2.3 repeat
  at pitch PX=6, with a thin REEL disk (half-width RW=1.0, half-height RH=2.5) at every
  bead-to-bead boundary; band half-height BH=2.8 (beyond it → recessed GROUND channel between
  courses). Per opaque body pixel in component-local (lx,ly): nearest course centre jc=round(ly/PY),
  dy_c=ly−jc·PY; if |dy_c|>BH → GROUND; nearest bead ib=round(lx/PX), dx_b=lx−ib·PX,
  rr=hypot(dx_b,dy_c); `rr<=RB`=BEAD raised SPHERE shaded round under upper-left light
  (lit=(−dx_b−dy_c)/RB: >0.85 RIM white crown catch / >0.15 HILIT / >−0.55 MID / else SHADOW
  lower-right terminator); else nearest REEL at half-boundary ir=floor(lx/PX)+0.5,
  `|dx_r|<=RW & |dy_c|<=RH`=thin convex DISK spacer (litr=−dy_c/RH: >0.55 RIM top edge / >−0.1
  HILIT / >−0.6 MID / else SHADOW bottom); else recessed GROUND. The repeated motif is a THREADED
  STRING OF ALTERNATING ROUND SPHERES + THIN DISK REELS. Completes the classical cast-bronze
  cornice trio (bead-and-reel + egg-and-dart 38th + dentil 40th run together on real moldings).
  Distinct from 38th egg-and-dart (TWO-element band of tall OVOID + POINTED dart — bead-and-reel is
  round SPHERE + round-edged DISK, no ovoids/points), 13th studwork (isolated round rivets on a 2-D
  area grid — bead-and-reel is a CONTINUOUS 1-D string, each a full relief sphere, with lens reels
  between beads), 21st chainmail / 28th concentric (OPEN rings — bead is a SOLID convex sphere not
  an outline), 40th dentil (RECTANGULAR teeth hung from a fillet — bead-and-reel is round spheres +
  disks threaded on a string, no straight block edges/fillet). Cast-bronze astragal relief —
  warrior gilt-bronze (dark-bronze ground / bronze shadow / brass mid / bright-gold hilit /
  white-gold rim), mage silvered-violet (midnight / indigo / steel-violet / bright-silver / pale),
  ranger bronzed-forest (deep-forest / bottle / bronze-green / bright-emerald / pale-green) — same
  metals as 37/38/39/40. Slots: chest Bead-and-Reel Cuirass `shirt_%s_legendary41`, legs
  Bead-and-Reel Chausses `pants_%s_legendary41`, boots Bead-and-Reel Sabatons
  `boots_%s_legendary_beadreel`, helmet Bead-and-Reel Dome `helmet_%s_legendary41`. Generator
  `scripts/gen_beadreel_axis41.py` (repaint-only, QA-safe by construction — net painted ONLY onto
  already-opaque body pixels; self-contained NumPy `label4()`, NO scipy). 24 sheets (4 slots × 3
  classes × m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source **24/24 exact (0
  dropped / 0 strays)**. Staged in `_beadreel_legendary_preview/`, `_beadreel_legs_preview/`,
  `_beadreel_boots_preview/`, `_beadreeldome_helmet_preview/`. Previews:
  `_PREVIEW_beadreel_legendary.png`, `_PREVIEW_beadreel_legs.png`, `_PREVIEW_beadreel_boots.png`,
  `_PREVIEW_beadreeldome_helmet.png` (built by `scripts/preview_axis41.py`); zoom
  `_ZOOM_beadreel_chest.png`. **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`,
  add L43 legendary LOOT_TABLE entries per slot/class (m + f).

- **40th net-new-geometry axis — DENTIL / DENTILATED-CORNICE, all 4 slots**
  (2026-07-29): an all-over field of horizontal COURSES, each course a continuous bright top
  FILLET from which hangs a BROKEN ROW OF DISCRETE RAISED RECTANGULAR TEETH ("dentils")
  separated by square recessed GAPS ("interdentils") — the classical dentil molding run under a
  cornice. Course pitch PY=7 down; along each course teeth at pitch PX=5, width TW=3 (gap=2),
  hung TH=4 deep below a FILLET_H=1 continuous lip. Per opaque body pixel in component-local
  (lx,ly): v=ly%PY, u=lx%PX; `v<FILLET_H`=fillet (top row RIM / body HILIT); `v<FILLET_H+TH &
  u<TW`=raised tooth block relief under upper-left light (top-left corner RIM cap / top|left
  HILIT / right|bottom SHADOW / interior MID); else recessed GROUND (gap + channel below teeth).
  Distinct from 12th lamellar (CONTINUOUS horizontal bands, no gaps — dentil BREAKS the band into
  teeth + adds block relief), 37th coffer (SUNKEN 2-D grid, reversed bevel — dentil is RAISED 1-D
  course, normal relief, hung from a fillet), 13th studwork (round rivets vs rect teeth), 17th
  ashlar (flat outline vs solid raised block), 38th egg-and-dart (TWO alternating elements vs ONE
  repeated tooth). Cast-bronze cornice relief — warrior gilt-bronze / mage silvered-violet /
  ranger bronzed-forest (same metals as 37/38/39). Slots: chest Dentil-Cuirass
  `shirt_%s_legendary40`, legs Dentil-Chausses `pants_%s_legendary40`, boots Dentil-Sabatons
  `boots_%s_legendary_dentil`, helmet Dentil-Dome `helmet_%s_legendary40`. Generator
  `scripts/gen_dentil_axis40.py` (repaint-only, QA-safe by construction; self-contained NumPy
  `label4()`, NO scipy). 24 sheets (4 slots × 3 classes × m+f): **sprite_qa ALL 24 PASS**
  (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame
  opaque-mask parity vs source **24/24 exact (0 dropped / 0 strays)**. Staged in
  `_dentil_legendary_preview/`, `_dentil_legs_preview/`, `_dentil_boots_preview/`,
  `_dentildome_helmet_preview/`. Previews: `_PREVIEW_dentil_legendary.png`,
  `_PREVIEW_dentil_legs.png`, `_PREVIEW_dentil_boots.png`, `_PREVIEW_dentildome_helmet.png`
  (built by `scripts/preview_axis40.py`); zoom `_ZOOM_dentil_chest.png`. **On approval:** copy the
  24 PNGs to `sprites/preview_assets/char/`, add L42 legendary LOOT_TABLE entries per slot/class
  (m + f).

- **39th net-new-geometry axis — GUILLOCHE / BRAIDED-RIBBON EYE-CHAIN, all 4 slots**
  (2026-07-29): an all-over field of horizontal bands, each band woven from TWO counter-phase
  SINE RIBBONS (period PX=8, amplitude AMP=2) that braid OVER-UNDER as they run and, between
  every pair of crossings, bulge apart to enclose a near-CIRCULAR EYE holding a bezel-set
  central BOSS/pip — the classical running guilloche (Tuscan border / banded interlace).
  Band pitch PY=7 down; two centre-lines r1=yb+AMP*sin(2pi*lx/PX), r2=yb-AMP*sin(...); they
  CROSS at s=0 (every half period) and pull apart at |s|=1, so a row of eyes sits on the band
  line (one per half period). At each crossing ONE ribbon passes OVER (over-strand alternates
  by crossing parity floor(lx/(PX/2))%2) = a true interlace. Ribbon HW=1.25 shaded as a
  rounded metal TUBE (upper edge HILIT / lower edge SHADOW / crown MID / extreme edge RIM);
  each eye = recessed GROUND floor + RIM boss catch (PIP=1.05). Distinct from 30th cable (two
  strands twist down a VERTICAL column, enclose NOTHING — guilloche runs HORIZONTAL and
  encloses a CHAIN OF EYES), 22nd wave (ONE sine ribbon), 31st ogee (POINTED-oval woven cells
  vs ROUND braided eyes), 21st/28th/32nd (static rings/lobes vs OVER-UNDER braid). Cast-bronze
  damascened interlace — warrior gilt-bronze / mage silvered-violet / ranger bronzed-forest.
  Slots: chest Guilloche-Cuirass `shirt_%s_legendary39`, legs Guilloche-Chausses
  `pants_%s_legendary39`, boots Guilloche-Sabatons `boots_%s_legendary_guilloche`, helmet
  Guilloche-Dome `helmet_%s_legendary39`. Generator `scripts/gen_guilloche_axis39.py`
  (repaint-only, QA-safe by construction; self-contained NumPy label4(), NO scipy). 24 sheets
  (4 slots x 3 classes x m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants/boots
  `--y-max 63`); per-frame opaque-mask parity vs source **24/24 exact (0 dropped / 0 strays)**.
  Staged in `_guilloche_legendary_preview/`, `_guilloche_legs_preview/`,
  `_guilloche_boots_preview/`, `_guillochedome_helmet_preview/`. Previews:
  `_PREVIEW_guilloche_legendary.png`, `_PREVIEW_guilloche_legs.png`,
  `_PREVIEW_guilloche_boots.png`, `_PREVIEW_guillochedome_helmet.png` (built by
  `scripts/preview_axis39.py`); zoom `_ZOOM_guilloche_chest.png`. **On approval:** copy the 24
  PNGs to `sprites/preview_assets/char/`, add L41 legendary LOOT_TABLE entries per slot/class
  (m + f).

- **38th net-new-geometry axis — EGG-AND-DART / OVOLO / EGG-AND-TONGUE, all 4 slots**
  (2026-07-29): an all-over field of horizontal bands, each band an alternating run of a RAISED
  CONVEX OVOID ("egg") ringed by a bright bezel SHELL and a slender downward-pointing DART
  ("tongue"/arrowhead) set in the gap between every pair of eggs — the classical ovolo enrichment
  carved on cornices and picture-frames. Rectangular lattice (egg pitch PX=7 across, band pitch
  PY=8 down); egg centres at (i·PX, j·PY), dart centres in the gaps at ((i2+0.5)·PX, j·PY). Per
  opaque body pixel in component-local coords (lx,ly): nearest egg (dxe,dye), elliptical metric
  ee=hypot(dxe/RX, dye/RY) with RX=2.4/RY=3.2 (taller-than-wide ovoid); lit=−(dxe/RX)−(dye/RY)
  (upper-left light). `ee<=1`=EGG interior — `ee<=CATCH`(0.42) & lit>EDGE(0.34)=RIM white crown
  catch-light / lit>EDGE=HILIT lit upper-left flank / lit<−EDGE=SHADOW lower-right flank / else
  MID side; `ee<=1+SHELL`(0.34)=bright bezel SHELL ring (RIM); dart lozenge
  `|ddx|/DW+|ddy|/DH<=1` (DW1.35/DH3.0)=raised DART tongue (HILIT body, RIM tip catch near point);
  else recessed GROUND channel. The repeated motif is the ALTERNATING RAISED-OVOID + POINTED-DART
  two-element enrichment; none of the 37 prior axes occupy it. Distinct from 13th studwork
  (isolated bare round rivets — egg is an elongated ovoid ringed by a shell and interleaved with
  darts), 15th scale (open one-way arcs — egg is a closed convex boss with a full bezel), 31st
  ogee (pointed-oval CELLS woven from a continuous rib net — egg-and-dart is a row of DISCRETE
  raised bosses with separate darts between), 35th facet (angular pyramid), 36th quilt (diamond
  cushion + sunken button), 37th coffer (sunken rectangular panel). Reads as CAST-BRONZE OVOLO
  ENRICHMENT with a white catch-light on each ovoid crown. Per class: warrior gilt-bronze
  (dark-bronze ground / bronze shadow / brass mid / bright-gold hilit / white-gold rim), mage
  silvered-violet (midnight / indigo / steel-violet / bright-silver / pale), ranger bronzed-forest
  (deep-forest / bottle / bronze-green / bright-emerald / pale-green). Slots: chest Ovolo-Cuirass
  `shirt_%s_legendary38`, legs Ovolo-Chausses `pants_%s_legendary38`, boots Ovolo-Sabatons
  `boots_%s_legendary_eggdart`, helmet Ovolo-Dome `helmet_%s_legendary38`. Generator
  `scripts/gen_eggdart_axis38.py` (repaint-only, QA-safe by construction — net painted ONLY onto
  already-opaque body pixels; self-contained NumPy `label4()`, NO scipy). 24 sheets (4 slots × 3
  classes × m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source **24/24 exact (0
  dropped / 0 strays)**. Staged in `_eggdart_legendary_preview/`, `_eggdart_legs_preview/`,
  `_eggdart_boots_preview/`, `_eggdartdome_helmet_preview/`. Previews:
  `_PREVIEW_eggdart_legendary.png`, `_PREVIEW_eggdart_legs.png`, `_PREVIEW_eggdart_boots.png`,
  `_PREVIEW_eggdartdome_helmet.png` (built by `scripts/preview_axis38.py`); zoom
  `_ZOOM_eggdart_chest.png`. **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`,
  add L40 legendary LOOT_TABLE entries per slot/class (m + f).

- **37th net-new-geometry axis — COFFER / CAISSON / SUNKEN-PANEL, all 4 slots**
  (2026-07-29): an all-over field of RECESSED RECTANGULAR PANELS on an orthogonal lattice
  (pitch P=7). The shared GRID between cells stands proud as a bright LAND; each cell dives into
  a flat recessed FLOOR through four bevelled REVEAL walls shaded in REVERSE of a raised boss —
  under an upper-left light the TOP/LEFT reveals fall to SHADOW and the BOTTOM/RIGHT reveals
  catch the HILIT, proving the panel is cut INTO the plate. A jewel PIP is bezel-set at each
  sunken floor centre. Per opaque body pixel (component-local lx,ly): u=frac(lx/P), v=frac(ly/P),
  du=min(u,1-u), dv=min(v,1-v), de=min(du,dv); `de<=LAND`(0.12)=proud grid / `de<=LAND+BEV`
  (BEV0.17)=reveal wall (du<dv→left/right, else top/bottom; near-edge SHADOW, far-edge HILIT) /
  `dc=hypot(u-.5,v-.5)<=PIPR`(0.13)=jewel pip / else recessed floor. Deliberately the INVERSE
  RELIEF of the 35th facet (facet = RAISED pyramid, bright APEX pip at cell centre, seam recessed
  at edges; coffer = SUNKEN flat floor, DARK at centre, proud bright GRID at edges, reversed
  bevel). Distinct from 36th quilt (rounded convex cushion on DIAMOND lattice + round sunken
  buttons — coffer is angular flat-floored rectangular recess on ORTHOGONAL lattice, straight
  reveals, no rounding/diamonds/round-buttons), 17th ashlar (flat rectangular OUTLINE only, no
  relief — same relation facet has to 14th lattice), 13th studwork (isolated RAISED round rivets),
  26th tartan (flat crossed bands). Reads as CAST-BRONZE CAISSON PANELLING. Per class: warrior
  gilt-bronze (dark-bronze floor / bronze shadow-reveal / brass grid / bright-gold hilit-reveal /
  white-gold pip), mage silvered-violet (midnight / indigo / steel-violet / bright-silver / pale),
  ranger bronzed-forest (deep-forest / bottle / bronze-green / bright-emerald / pale-green). Slots:
  chest Caisson-Cuirass `shirt_%s_legendary37`, legs Caisson-Chausses `pants_%s_legendary37`,
  boots Caisson-Sabatons `boots_%s_legendary_coffer`, helmet Caisson-Dome `helmet_%s_legendary37`.
  Generator `scripts/gen_coffer_axis37.py` (repaint-only, QA-safe by construction — net painted
  ONLY onto already-opaque body pixels; self-contained NumPy `label4()`, NO scipy). 24 sheets
  (4 slots × 3 classes × m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62`
  / f `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source **24/24 exact
  (0 dropped / 0 strays)**. Staged in `_coffer_legendary_preview/`, `_coffer_legs_preview/`,
  `_coffer_boots_preview/`, `_cofferdome_helmet_preview/`. Previews: `_PREVIEW_coffer_legendary.png`,
  `_PREVIEW_coffer_legs.png`, `_PREVIEW_coffer_boots.png`, `_PREVIEW_cofferdome_helmet.png` (built
  by `scripts/preview_axis37.py`); zoom `_ZOOM_coffer_chest.png`. **On approval:** copy the 24 PNGs
  to `sprites/preview_assets/char/`, add L39 legendary LOOT_TABLE entries per slot/class (m + f).

- **36th net-new-geometry axis — QUILTED / CAPITONNE / TUFTED DIAMOND-CUSHION, all 4 slots**
  (2026-07-29): an all-over field of CONVEX PADDED DIAMOND CUSHIONS on a DIAGONAL lattice, each
  cushion bulging up between four SUNKEN BUTTON TUFTS at the lattice nodes (button-tufted
  upholstery / Chesterfield quilting / padded gambeson). Per opaque body pixel in component-local
  coords (lx, ly) the diamond lattice is s=lx+ly, t=lx-ly with pitch P=7; buttons sit at integer
  (s/P, t/P), cushion crowns at the cell centres. With gs=frac(s/P), gt=frac(t/P): dn=dist to
  nearest cell corner (button), dc=dist to cell centre (crown), lit=gs-0.5 (upper-left light in
  the rotated frame) — `dn<=BUT`(0.16)=sunken BUTTON dimple (darkest) / `dc<=PIPR`(0.14) & lit<0 =
  soft CROWN highlight (graded, NOT a hard pip) / `dc<=CUSH`(0.42): lit<-EDGE=lit face RIB_HI,
  lit>EDGE=shadow face, else side RIB_MID / beyond CUSH = puckered SEAM. The repeated motif is the
  CONVEX ROUNDED DIAMOND CUSHION pinned by a SUNKEN BUTTON at each node; none of the 35 prior axes
  occupy it. Its closest relative is the 35th facet (the other RELIEF axis) but is an INVERSE
  relief: facet = ANGULAR four-sided PYRAMID on a SQUARE lattice rising to a BRIGHT WHITE-HOT APEX
  PIP with hard flat facets; quilt = SMOOTH ROUNDED convex cushion on a DIAMOND lattice with a soft
  graded crown and a DARK SUNKEN BUTTON at the corners (bright-point-up-at-centre vs
  soft-bulge-with-sunken-corner-button). Distinct from 25th argyle (FLAT solid-filled diagonal
  diamonds — quilt diamond is a graded convex DOME + button, a relief not a fill), 14th lattice
  (diamond OUTLINE only), 13th studwork (isolated RAISED round rivets on a plain ground — here the
  whole surface is edge-to-edge cushions and the round features are SUNKEN buttons at shared
  nodes). Reads as TUFTED PADDED UPHOLSTERY (quilted jewelled velvet stitched with metal buttons).
  Per class: warrior gilt-buttoned oxblood (dark-bronze button / bronze seam / gold-brown mid /
  bright-gold hi / pale-gold crown), mage silver-buttoned violet (indigo / deep-violet / violet /
  lilac / white), ranger copper-buttoned forest (bottle / deep-green / green / bright-green /
  pale-green). Slots: chest Quilted-Gambeson `shirt_%s_legendary36`, legs Quilted-Chausses
  `pants_%s_legendary36`, boots Quilted-Sabatons `boots_%s_legendary_quilt`, helmet Quilted-Coif
  `helmet_%s_legendary36`. Generator `scripts/gen_quilt_axis36.py` (repaint-only, QA-safe by
  construction — net painted ONLY onto already-opaque body pixels; self-contained NumPy `label4()`,
  NO scipy). 24 sheets (4 slots × 3 classes × m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`,
  pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source
  **24/24 exact (0 dropped / 0 strays)**, frame-presence 24/24 exact. Staged in
  `_quilt_legendary_preview/`, `_quilt_legs_preview/`, `_quilt_boots_preview/`,
  `_quiltdome_helmet_preview/`. Previews: `_PREVIEW_quilt_legendary.png`, `_PREVIEW_quilt_legs.png`,
  `_PREVIEW_quilt_boots.png`, `_PREVIEW_quiltdome_helmet.png` (built by `scripts/preview_axis36.py`);
  zoom `_ZOOM_quilt_chest.png`. **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`,
  add L38 legendary LOOT_TABLE entries per slot/class (m + f).

- **35th net-new-geometry axis — FACET / DIAMOND-POINT / PYRAMIDAL-BOSS, all 4 slots**
  (2026-07-29): an all-over tessellation of RAISED FOUR-FACET PYRAMIDS (diamond-point
  rustication / faceted-gem bosses). The body is tiled by a square lattice (pitch P=6); every
  cell is a little four-sided pyramid rising to a bright apex at the cell centre, its four
  TRIANGULAR FACES (left / top / right / bottom) each FLAT-SHADED by the direction it faces
  under an upper-left light, with a dark recessed VALLEY seam in the channels between
  neighbouring pyramids and a white-hot apex PIP at each summit. Per opaque body pixel in
  component-local coords (lx, ly) anchored at the component bbox top-left: nearest apex on the
  square lattice, offset (u,v) in [-P/2,P/2]; distance to nearest cell edge `edge =
  min(P/2-|u|, P/2-|v|)` picks the valley seam (`edge<=SEAM`, SEAM=0.7); within PIP=0.85 of the
  apex = summit pip; else the dominant axis + sign picks the face — `|u|>=|v|` LEFT(u<0)=lit
  crest / RIGHT(u>=0)=shadow, else TOP(v<0)=mid / BOTTOM(v>=0)=shadow. The repeated motif is
  the SOLID-MODELLED FOUR-FACET PYRAMID with directional facet shading; none of the 34 prior
  axes occupy it. Critically distinct by being a RELIEF, not a line/arc/point/outline on a flat
  ground: the 25th argyle FILLS each lozenge with ONE flat colour and the 14th lattice draws
  the diamond OUTLINE, whereas the facet cell is a raised pyramid whose four faces each take a
  DIFFERENT tone by tilt (a directional bevel, not a fill); not the 13th studwork (ISOLATED
  round rivet dots on a plain ground — facet field is edge-to-edge pyramids tiling the WHOLE
  surface, meeting along shared valley seams), not the 17th ashlar (flat outline cells, no
  relief), not the 27th sunburst (open rays). Generator `scripts/gen_facet_axis35.py`
  (repaint-only, QA-safe by construction — net painted ONLY onto already-opaque body pixels;
  self-contained NumPy `label4()`, NO scipy). Reads as CUT GEMSTONES bezel-set in metal. Per
  class: warrior topaz-and-gold (bronze-shadow valley / shadow-gold face / brass face /
  bright-gold lit face / white-gold pip), mage sapphire-and-silver (midnight valley / indigo /
  blue / bright-blue lit / pale pip), ranger emerald-and-bronze (deep-forest valley / bottle /
  emerald / bright-emerald lit / pale-green pip). Slots: chest Facet-Cuirass
  `shirt_%s_legendary35`, legs Facet-Chausses `pants_%s_legendary35`, boots Facet-Sabatons
  `boots_%s_legendary_facet`, helmet Facet-Dome `helmet_%s_legendary35`. 24 sheets (4 slots × 3
  classes × m+f): **sprite_qa ALL 24 PASS** (helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask parity vs source **24/24 exact (0
  dropped / 0 strays)**. Staged in `_facet_legendary_preview/`, `_facet_legs_preview/`,
  `_facet_boots_preview/`, `_facetdome_helmet_preview/`. Previews:
  `_PREVIEW_facet_legendary.png`, `_PREVIEW_facet_legs.png`, `_PREVIEW_facet_boots.png`,
  `_PREVIEW_facetdome_helmet.png` (built by `scripts/preview_axis35.py`); zoom
  `_ZOOM_facet_chest.png`. **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`,
  add L37 legendary LOOT_TABLE entries per slot/class (m + f).

- **34th net-new-geometry axis — SEIGAIHA / OCEANIC WAVE-SCALE, all 4 slots**
  (2026-07-29): an all-over field of overlapping FANS, where each fan is a stack of THREE NESTED
  CONCENTRIC ARCS (multi-arc scale) bulging upward, laid on a HALF-DROP lattice (pitch PX=6 across,
  PY=3 down, odd rows shifted PX/2) so the fans interlock into continuous concentric-wave rows — the
  classic blue-ocean-wave / fish-scale pattern (青海波). Per opaque body pixel each pixel is assigned
  to the NEAREST fan apex at-or-above it (so every fan opens DOWNWARD = a scallop); its distance d to
  that apex folded into the nested-arc period (RINGSTEP=2.0, outermost arc at R=6=the scallop rim)
  gives the tone: crest (`dline≤RIB·CROWN`, RIB=0.62) / flank (`≤RIB`) / trough (`≤RIB+0.5`) / body
  ground (smooth scale face), with a bright jewelled CORE/pip (PIP=0.9) at each apex. The repeated
  motif = the MULTI-ARC NESTED FAN; none of the 33 prior axes occupy it. Distinct from 15th scale
  (ONE convex arc per scale — seigaiha stacks THREE nested arcs per fan and interlocks them on a
  half-drop), 28th concentric (CLOSED full rings around ONE tiled centre — seigaiha draws only the
  lower-fan scallop arcs on a dense overlapping lattice = interlocking half-circle waves, not a
  bullseye), 21st chainmail (single non-overlapping ring per centre), 24th spiral (one continuous
  coil of GROWING radius). Generator `scripts/gen_seigaiha_axis34.py` (repaint-only, QA-safe by
  construction — net painted ONLY onto already-opaque body pixels; includes a self-contained NumPy
  4-connectivity `label4()` so it needs NO scipy). Reads as DAMASCENED WAVE-INLAY on polished plate
  (mid-tone burnished metal ground + bright inlaid metal arc + jewelled apex core). Per class:
  warrior gilt wave on gunmetal (dark-steel trough / brass flank / bright-gold crest / pale-gold
  pip), mage silver wave on violet-steel (indigo / steel-blue / white-silver / pale pip), ranger
  copper wave on bronzed-forest (bottle / bronze / bright-copper / pale pip). Slot dst stems: chest
  Wavescale-Cuirass `shirt_%s_legendary34`, legs Wavescale-Chausses `pants_%s_legendary34`, boots
  Wavescale-Sabatons `boots_%s_legendary_seigaiha`, helmet Wavescale-Dome `helmet_%s_legendary34`.
  24 sheets (4 slots × 3 classes × m+f) staged in `_seigaiha_legendary_preview/`,
  `_seigaiha_legs_preview/`, `_seigaiha_boots_preview/`, `_seidome_helmet_preview/`. Previews:
  `_PREVIEW_seigaiha_legendary.png`, `_PREVIEW_seigaiha_legs.png`, `_PREVIEW_seigaiha_boots.png`,
  `_PREVIEW_seidome_helmet.png` (built by `scripts/preview_axis34.py`). QA: ALL 24 PASS (helmets
  `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame opaque-mask
  parity vs source 0/24 (0 opaque-px diff, 0 frame-presence mismatch — all frames/animation
  preserved by construction). **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`,
  add L36 legendary LOOT_TABLE entries per slot/class (m + f).

- **33rd net-new-geometry axis — OCTAGRAM / EIGHT-POINT STAR-AND-CROSS / GIRIH, all 4 slots**
  (2026-07-28): an all-over tessellation of straight-edged EIGHT-POINTED STARS whose points nearly
  touch tip-to-tip, leaving a small rotated-square "cross" interstice between every block of four.
  Each star is the octagram {8/2} — an axis-aligned SQUARE (`fA=max(|dx|,|dy|)-W`, W=2.35) overlaid
  with a 45deg-rotated square / diamond of equal circumradius (`fB=(|dx|+|dy|)-W·√2`); the union
  boundary is the eight-pointed star outline (axis-square edge where outside the diamond and vice
  versa, joined with TOL=0.55), stroked crest/flank/groove by min distance over the nearest 3×3
  nodes (lattice pitch P=7), with a jewelled CORE/pip at each star centre. Repeated motif = the
  EIGHT-POINTED STAR OUTLINE; none of the 32 prior axes occupy it. Distinct from 32nd quatrefoil
  (CURVED four-lobe rosette — octagram is STRAIGHT-EDGED eight-point star = two overlaid squares),
  14th lattice / 25th argyle (single diamond/lozenge — octagram is a diamond AND a square as an
  OUTLINE, not a solid fill), 27th sunburst (open rays — octagram is a CLOSED star polygon), 19th
  honeycomb / 20th trellis / 17th ashlar (convex 6/3/4-sided cells — octagram repeat is a
  re-entrant non-convex 8-point star). Reads as DAMASCENED STAR-INLAY on polished plate (mid-tone
  burnished metal ground + bright inlaid metal star outline + jewelled core), apart from 32nd
  quatrefoil (pierced gothic tracery) and 31st ogee (woven damask brocade). Per class: warrior gilt
  star on gunmetal (dark-steel groove / brass flank / bright-gold crest / pale-gold pip), mage
  silver star on violet-steel (indigo / steel-blue / white-silver / pale pip), ranger copper star
  on bronzed-forest (bottle / bronze / bright-copper / pale pip). Slots: chest Starplate-Cuirass
  `shirt_%s_legendary33`, legs Starplate-Chausses `pants_%s_legendary33`, boots Starplate-Sabatons
  `boots_%s_legendary_octagram`, helmet Starplate-Dome `helmet_%s_legendary33`. Generator
  `scripts/gen_octagram_axis33.py` (repaint-only, QA-safe by construction — net painted ONLY onto
  already-opaque body pixels; needs scipy). All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa
  ALL 24 PASS**, repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**. Staged in
  `_octagram_legendary_preview/`, `_octagram_legs_preview/`, `_octagram_boots_preview/`,
  `_octadome_helmet_preview/`. Previews: `_PREVIEW_octagram_legendary.png`,
  `_PREVIEW_octagram_legs.png`, `_PREVIEW_octagram_boots.png`, `_PREVIEW_octadome_helmet.png`
  (built by `scripts/preview_axis33.py`). QA flags: helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`. **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L35 legendary LOOT_TABLE entries per slot/class (m + f).

- **32nd net-new-geometry axis — QUATREFOIL / GOTHIC TRACERY / CLOVERLEAF, all 4 slots**
  (2026-07-28): an all-over net of FOUR-LOBED cusped rosettes — pierced cathedral tracery. At every
  lattice node (orthogonal pitch P=7) four equal circular LOBES sit offset up/down/
  left/right (LOBE=1.7, LR=1.7 so each lobe passes through the node centre = true clover); the four
  lobe arcs meet at four inward CUSPS enclosing a four-petal rosette, and neighbouring rosettes
  touch at cusps leaving a concave-square pierce, with a jewelled CORE (PIP) at each centre. Per
  opaque pixel the min RING distance |dist_to_lobe_centre − LR| over the nearest 3×3 nodes' 4 lobes
  picks crest (`≤RIB·CROWN`, RIB=0.9) / flank (`≤RIB`) / groove (`≤RIB+0.6`) / body ground. The
  motif is the QUATREFOIL — a compound outline of FOUR circular lobes meeting at four cusps, four-
  fold symmetric; none of the 31 prior axes occupy it. Distinct from 21st chainmail (ONE circle per
  centre — quatrefoil stamps FOUR meeting at cusps), 28th concentric (NESTED rings around one point
  — quatrefoil lobes are offset, never nested), 31st ogee (TWO-cusp pointed oval on vertical rib net
  — quatrefoil is a FOUR-cusp four-lobe rosette on an orthogonal lattice), 15th scale (arcs face ONE
  way, stay open — quatrefoil lobes face FOUR ways and close). Generator
  `scripts/gen_quatrefoil_axis32.py` (repaint-only, QA-safe by construction — net painted ONLY onto
  already-opaque body pixels; needs scipy). Reads as PIERCED GOTHIC TRACERY (dark enamel ground +
  bright metal filigree rosette + jewelled core), apart from the 31st ogee (woven damask brocade)
  and 21st chainmail (blued rings). Per class: warrior bronze-on-oxblood (garnet groove / bronze
  flank / gold crest / pale pip), mage silver-on-midnight-blue (indigo / steel / moonsilver / pip),
  ranger antique-gold-on-mossy-green (bottle / antique-gold / gold / pip). Slots: chest Tracery-
  Cuirass `shirt_%s_legendary32`, legs Tracery-Chausses `pants_%s_legendary32`, boots Tracery-
  Sabatons `boots_%s_legendary_quatrefoil`, helmet Tracery-Dome `helmet_%s_legendary32`. All 24
  sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24 PASS**, repaint-only mask check **0/24
  mismatch (0 dropped / 0 strays)**. Staged in `_quatrefoil_legendary_preview/`,
  `_quatrefoil_legs_preview/`, `_quatrefoil_boots_preview/`, `_quatredome_helmet_preview/`.
  Previews: `_PREVIEW_quatrefoil_legendary.png`, `_PREVIEW_quatrefoil_legs.png`,
  `_PREVIEW_quatrefoil_boots.png`, `_PREVIEW_quatredome_helmet.png` (built by
  `scripts/preview_axis32.py`). QA flags: helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`,
  boots `--y-max 63`. **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add L34
  legendary LOOT_TABLE entries per slot/class (m + f).

- **31st net-new-geometry axis — OGEE / ONION / DAMASK, all 4 slots** (2026-07-28): an
  all-over net of POINTED-OVAL (ogee) cells — the damask / onion-dome / brocade lattice.
  Parallel vertical ribs at pitch PX=6 run down the whole body, but NEIGHBOURING ribs undulate
  in OPPOSITE phase (`xc_k(ly)=k·PX + AMP·sin(2π·ly/PY)·(-1)^k`, PY=8, AMP=1.6) so adjacent ribs
  alternately PINCH to a cusp and BULGE to a belly, enclosing a stacked column of pointed-oval
  cells that touch at their cusps; a bright BOSS/pip sits at each cell centre on a
  half-pitch-offset brick lattice. Per opaque pixel the min distance to the nearest of the three
  candidate ribs picks crest (`≤RIB·CROWN`, RIB=0.9) / flank (`≤RIB`) / groove (`≤RIB+0.75`) /
  body ground. The repeated motif is the OGEE CELL — a closed cell whose boundary is a cyma
  (S-curve) meeting at top and bottom cusps; none of the thirty prior legendary axes per slot
  occupy it. Critically distinct from the 11th FLUTING (dead-straight parallel ribs that never
  touch and enclose nothing — ogee ribs pinch and enclose pointed ovals), the 22nd WAVE (ONE
  open undulating ribbon — ogee is a field of CLOSED cells), the 30th CABLE (two strands crossing
  OVER-UNDER into a solid rope down a column — ogee ribs never cross, they only pinch/bulge
  leaving an OPEN cell), and every straight-edged/circular/hex cell net (14th lattice diamond,
  19th honeycomb hex, 21st chainmail circle) by the cusped POINTED-OVAL cell shape. Generator
  `scripts/gen_ogee_axis31.py` (repaint-only, QA-safe by construction — net painted ONLY onto
  already-opaque body pixels; needs scipy). Reads apart from the 30th cable (braided metal rope),
  29th houndstooth (flat two-tone cloth) and 28th concentric (engraved burnished metal) as a rich
  WOVEN DAMASK BROCADE: a deep saturated cloth ground + bright metallic-thread ogee rib + pale
  boss (cloth-of-gold/silver). Per class: warrior crimson-and-gold damask (garnet groove / bronze
  flank / bright-gold crest / pale-gold pip), mage royal-violet-and-silver (indigo groove / silver
  flank / moonsilver crest / pale pip), ranger forest-and-antique-gold (bottle groove / antique-gold
  flank / gold crest / pale pip). Slots: chest Damask-Cuirass `shirt_%s_legendary31`, legs
  Damask-Chausses `pants_%s_legendary31`, boots Damask-Sabatons `boots_%s_legendary_ogee`, helmet
  Damask-Dome `helmet_%s_legendary31`. All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa ALL
  24 PASS**, repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**. Staged in
  `_ogee_legendary_preview/`, `_ogee_legs_preview/`, `_ogee_boots_preview/`,
  `_ogeedome_helmet_preview/`. Previews: `_PREVIEW_ogee_legendary.png`, `_PREVIEW_ogee_legs.png`,
  `_PREVIEW_ogee_boots.png`, `_PREVIEW_ogeedome_helmet.png` (built by `scripts/preview_axis31.py`).
  QA flags: helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`.
  **On approval:** copy the 24 PNGs to `sprites/preview_assets/char/`, add L33 legendary
  LOOT_TABLE entries per slot/class (m + f).

- **30th net-new-geometry axis — CABLE / ROPE-TWIST / TORSADE, all 4 slots** (2026-07-28): an
  all-over field of TWO intertwining strands that braid around each other and cross OVER-UNDER
  at a regular pitch down parallel cable columns — the twisted-rope / cable-knit / barley-sugar
  column. Within each COLW=5 column two rounded strands swing in OPPOSITE phase down the body
  (`xa=AMP*sin(2π·ly/PITCH)`, `xb=-xa`, PITCH=6, AMP=1.15, R=1.25); the strand momentarily in
  front (`cos(phase)>=0`) is drawn on top, each strand tube-shaded (bright crown near centreline
  / mid flank), with a dark recessed groove between and beside the strands. The repeated motif
  is the TWO-STRAND TRAVELLING BRAID (torsade); none of the twenty-nine prior legendary axes per
  slot occupy it. Critically distinct from the 22nd WAVE (a SINGLE undulating sine ribbon — cable
  is TWO strands actually crossing over AND under one another), the 24th SPIRAL (one coil winding
  AROUND a fixed centre — cable strands TRAVEL down a column twisting about EACH OTHER, not
  orbiting a point), the 21st CHAINMAIL (closed separate rings — cable strands are continuous,
  never closing), and the 11th FLUTING (straight parallel ribs that never cross — cable ribs
  braid across one another). Tuned high-frequency (narrow 5px columns, thin 1.25px strands, 6px
  pitch) so the braid reads on a ~14px torso. Generator `scripts/gen_cable_axis30.py`
  (repaint-only, QA-safe by construction — rope painted ONLY onto already-opaque body pixels;
  needs scipy). Reads APART from the 24th spiral (verdigris volute) and 29th houndstooth (flat
  two-tone cloth) as a lustrous braided METAL rope — a twisted torc / barley-sugar column. Per
  class: warrior molten-gold rope (deep-umber groove / bronze flank / bright-gold crown), mage
  moonsilver-violet rope (deep-violet groove / silver flank / white-silver crown), ranger
  verdigris-copper rope (deep-forest groove / copper flank / pale-gold crown). Slots: chest
  Torc-Cable Cuirass `shirt_%s_legendary30`, legs Cable-Chausses `pants_%s_legendary30`, boots
  Cable-Sabatons `boots_%s_legendary_cable`, helmet Cable-Dome `helmet_%s_legendary30`. All 24
  sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24 PASS**, repaint-only mask check **0/24
  mismatch (0 dropped / 0 strays)**. Staged in `_cable_legendary_preview/`, `_cable_legs_preview/`,
  `_cable_boots_preview/`, `_cabledome_helmet_preview/`. Previews: `_PREVIEW_cable_legendary.png`,
  `_PREVIEW_cable_legs.png`, `_PREVIEW_cable_boots.png`, `_PREVIEW_cabledome_helmet.png` (built by
  `scripts/preview_axis30.py`). QA flags: helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`. **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L32 legendary LOOT_TABLE entries per slot/class (m + f).

- **29th net-new-geometry axis — HOUNDSTOOTH / DOGTOOTH / BROKEN-CHECK, all 4 slots**
  (2026-07-28): an all-over TWO-TONE field of interlocking JAGGED four-pointed "broken check"
  cells — the classic couture DOGTOOTH — produced by the genuine color-and-weave effect of a
  2/2 twill woven from bands of 4 dark + 4 light warp and weft. Per opaque body pixel in
  component-local coords (lx, ly): `warp_on_top = ((lx-ly) % 4) < 2` (2/2 twill),
  `warp_dark = (lx % 8) < 4`, `weft_dark = (ly % 8) < 4`, `is_dark = warp_dark if warp_on_top
  else weft_dark` — so the broken check is authentically woven, not faked. The repeated motif
  is the INTERLOCKING JAGGED BROKEN-CHECK; none of the twenty-eight prior legendary axes per
  slot occupy it. This is the SECOND (and last) solid-fill axis, deliberately paired against
  the 25th ARGYLE as its jagged foil: argyle fills SMOOTH straight-edged diamond lozenges on a
  clean diagonal checker, whereas houndstooth cells are JAGGED — each solid shape throws
  pointed teeth that HOOK into the neighbour, an interlocking notched tessellation, not smooth
  lozenges. Distinct from the 16th twill/herringbone (short parallel diagonal DASHES that never
  close into shapes — houndstooth is a closed AREA fill), the 18th basketweave (plain
  straight-edged checker), and the 26th tartan (crossing continuous bands over a ground —
  houndstooth has no bands, only tessellating hooked cells). Generator
  `scripts/gen_houndstooth_axis29.py` (repaint-only, QA-safe by construction — textile painted
  ONLY onto already-opaque body pixels; needs scipy). Reads apart from the 25th argyle (jewel
  body + gold diamond) and 28th concentric (burnished-metal target-work): a fine TWO-TONE woven
  couture cloth with a dark ground + light tooth. Per class: warrior jet-black ground +
  bone-white tooth (iconic monochrome dogtooth), mage deep-violet ground + pale-lilac tooth,
  ranger deep-forest ground + oat-cream tooth. Slots: chest Houndstooth-Cuirass
  `shirt_%s_legendary29`, legs Houndstooth-Chausses `pants_%s_legendary29`, boots
  Houndstooth-Sabatons `boots_%s_legendary_houndstooth`, helmet Houndstooth-Dome
  `helmet_%s_legendary29`. All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24
  PASS**, repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**. Staged in
  `_houndstooth_legendary_preview/`, `_houndstooth_legs_preview/`, `_houndstooth_boots_preview/`,
  `_houndsdome_helmet_preview/`. Previews: `_PREVIEW_houndstooth_legendary.png`,
  `_PREVIEW_houndstooth_legs.png`, `_PREVIEW_houndstooth_boots.png`,
  `_PREVIEW_houndsdome_helmet.png` (built by `scripts/preview_axis29.py`). QA flags: helmets
  `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`. **On approval:** copy
  the 24 PNGs to `sprites/preview_assets/char/`, add L31 legendary LOOT_TABLE entries per
  slot/class (m + f).

- **28th net-new-geometry axis — CONCENTRIC / TARGET / RIPPLE-RING, all 4 slots** (2026-07-28):
  an all-over field of tiled CENTRES, each ringed by a set of NESTED CLOSED RINGS at growing
  radius (r=1,2,3,4 — Chebyshev square rings) sharing ONE origin — a bullseye / target /
  tree-ring / water-ripple look — with a bright CORE dot at each centre and the nested rings
  ALTERNATING a bright ring-CREST (odd r) and dark ring-GROOVE (even r) so the concentric
  banding reads. The repeated motif is the NESTED CONCENTRIC RING SET: several SEPARATE closed
  loops of increasing radius stacked around a common point; none of the twenty-seven prior
  legendary axes per slot occupy it. Critically distinct from the 21st CHAINMAIL (a tiled field
  of SINGLE same-radius interlinked rings, one ring per centre) — concentric stacks MULTIPLE
  nested rings of growing radius around ONE centre, a bullseye not a single-ring mesh. Distinct
  from the 24th SPIRAL (ONE CONTINUOUS coil whose radius grows as it winds) — concentric rings
  are separate closed loops, never joined into a coil. Distinct from the 27th SUNBURST (STRAIGHT
  rays shooting OUT from the centre) — concentric are CLOSED CURVED rings encircling the centre,
  no radial rays. Distinct from the 15th scale (short OPEN arcs, no shared centre) and 3rd
  studwork (isolated points, no rings). Generator `scripts/gen_concentric_axis28.py`
  (repaint-only, QA-safe by construction — rings painted ONLY onto already-opaque body pixels;
  needs scipy). To read APART from the 27th sunburst (near-void body with bright rays bursting
  out) the concentric family INVERTS the contrast: a LIGHTER burnished-metal body with the rings
  ENGRAVED as recessed dark grooves + a bright raised ring-crest — target-work in light metal,
  not light bursting from darkness; reads apart from tartan (woven) and argyle (jewel+gold) too.
  Per class: warrior burnished-bronze body + gold ring-crest + umber groove + bright core
  (aegis-ring), mage pale-silver-violet + violet crest + deep-violet groove + white core (oracle
  ripple), ranger pale-sage-bronze + gold crest + forest groove + pale-gold core (tideward).
  Slots: chest Aegis-Ring/Ripple/Tideward Cuirass `shirt_%s_legendary28`, legs Chausses
  `pants_%s_legendary28`, boots Sabatons `boots_%s_legendary_concentric`, helmet Oracle-Dome
  `helmet_%s_legendary28`. All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24 PASS**,
  repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**. Staged in
  `_concentric_legendary_preview/`, `_concentric_legs_preview/`, `_concentric_boots_preview/`,
  `_oracledome_helmet_preview/`. Previews: `_PREVIEW_concentric_legendary.png`,
  `_PREVIEW_concentric_legs.png`, `_PREVIEW_concentric_boots.png`,
  `_PREVIEW_oracledome_helmet.png` (built by `scripts/preview_axis28.py`). QA flags: helmets
  `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`. **On approval:** copy
  the 24 PNGs to `sprites/preview_assets/char/`, add L30 legendary LOOT_TABLE entries per
  slot/class (m + f).

- **27th net-new-geometry axis — SUNBURST / RADIANT / COMPASS, all 4 slots** (2026-07-28): an
  all-over field of tiled RADIATING CENTRES, each emitting STRAIGHT RAYS that shoot OUTWARD
  from a shared origin point in every principal direction (horizontal + vertical + both
  diagonals — a compass-rose / solar-burst / asterisk star), with a brighter CORE dot at each
  centre; rays bounded in length (reach R=4, pitch 10) so discrete star-bursts read across the
  body. The repeated motif is the RADIAL BURST: many straight lines sharing ONE origin fanning
  out omnidirectionally — occupied by none of the twenty-six prior legendary axes per slot.
  Critically distinct from the 11th FLUTING (vertical parallel lines) and 12th LAMELLAR
  (horizontal parallel lines): those are single-direction parallel families that never share
  an origin; sunburst rays all emanate from one point and fan out in every direction. Distinct
  from the 14th LATTICE / 20th TRELLIS (fixed line families meshing into closed cells) — a
  burst is a discrete radiating star, not a cellular mesh. Distinct from the 24th SPIRAL (one
  continuous CURVED coil winding AROUND a centre) — these are STRAIGHT rays shooting straight
  OUT, no winding. Distinct from the 3rd STUDWORK (isolated points, no rays) and the 8th
  aegis-roundel chest (single central emblem, not an all-over tiled burst field). Generator
  `scripts/gen_sunburst_axis27.py` (repaint-only, QA-safe by construction — rays/cores painted
  ONLY onto already-opaque body pixels; needs scipy). RADIANT / SOLAR / ASTRAL theme reads
  apart from the 26th tartan (woven highland clan-cloth) and 25th argyle (regal jewel body +
  gold diamond): a deep near-void body with BRIGHT RADIATING RAYS + white-hot core — light
  bursting out of darkness, celestial not woven. Per class: warrior obsidian-black body +
  molten-gold rays + white-hot core, mage deep-void indigo + astral-cyan rays + white star
  core, ranger dark bottle-green + amber-dawn rays + pale-gold core. Slots: chest
  Radiant-Cuirass `shirt_%s_legendary27`, legs Radiant-Chausses `pants_%s_legendary27`, boots
  Radiant-Sabatons `boots_%s_legendary_sunburst`, helmet Radiant-Dome `helmet_%s_legendary27`.
  All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24 PASS**, repaint-only mask
  check **0/24 mismatch (0 dropped / 0 strays)**. Staged in `_sunburst_legendary_preview/`,
  `_sunburst_legs_preview/`, `_sunburst_boots_preview/`, `_sunburstdome_helmet_preview/`.
  Previews: `_PREVIEW_sunburst_legendary.png`, `_PREVIEW_sunburst_legs.png`,
  `_PREVIEW_sunburst_boots.png`, `_PREVIEW_sunburstdome_helmet.png` (built by
  `scripts/preview_axis27.py`). QA flags: helmets `--y-min 2`, pants m `--y-max 62` / f
  `--y-max 63`, boots `--y-max 63`. **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L29 legendary LOOT_TABLE entries per slot/class (m + f).

- **26th net-new-geometry axis — TARTAN / PLAID / SETT, all 4 slots** (2026-07-28): an
  all-over field of CROSSING FULL-LENGTH ORTHOGONAL BANDS — bold vertical AND bold horizontal
  bands laid over the whole body SIMULTANEOUSLY — with a distinct BRIGHTER THIRD TONE painted
  at every crossing NODE (the woven "sett"), plus a thin single-pixel over-check guard line
  midway between the bold bands. The repeated motif is the THREE-LEVEL WOVEN CROSSING
  (body / single band / brighter overlap node); none of the twenty-five prior legendary axes
  per slot occupy it. Critically distinct from the 11th FLUTING (vertical lines only) and the
  12th LAMELLAR (horizontal lines only): tartan lays BOTH directions over the whole body at
  once AND adds a third crossing-node tone — a multi-level woven check, not a one-direction
  line field. Distinct from the 18th BASKETWEAVE (which alternates thread DIRECTION per checker
  tile with no overlap tone) — tartan runs continuous full-length bands in both directions
  everywhere with a distinct sett node. Distinct from the 17th ASHLAR (rectangular cell
  OUTLINES, empty interiors) — tartan fills BANDS and NODES, not cell edges. Generator
  `scripts/gen_tartan_axis26.py` (repaint-only, QA-safe by construction — bands painted ONLY
  onto already-opaque body pixels; needs scipy). WOVEN-CLOTH / highland theme reads apart from
  the 25th argyle (regal jewel body + gold diamond) and 24th spiral (verdigris teal + copper):
  a deep muted highland ground with BOLD contrasting bands and a bright sett — clan-cloth, not
  metal. Per class: warrior charcoal-black body + crimson bands + bone-white sett (Royal
  Stewart vibe), mage midnight-indigo + violet-blue bands + silver sett, ranger bottle-green +
  saffron-gold bands + cream sett. Slots: chest Tartan-Cuirass `shirt_%s_legendary26`, legs
  Tartan-Chausses `pants_%s_legendary26`, boots Tartan-Sabatons `boots_%s_legendary_tartan`,
  helmet Tartan-Dome `helmet_%s_legendary26`. All 24 sheets (4 slots × 3 classes × m/f):
  **sprite_qa ALL 24 PASS**, repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**.
  Staged in `_tartan_legendary_preview/`, `_tartan_legs_preview/`, `_tartan_boots_preview/`,
  `_tartandome_helmet_preview/`. Previews: `_PREVIEW_tartan_legendary.png`,
  `_PREVIEW_tartan_legs.png`, `_PREVIEW_tartan_boots.png`, `_PREVIEW_tartandome_helmet.png`
  (built by `scripts/preview_axis26.py`). QA flags: helmets `--y-min 2`, pants m `--y-max 62`
  / f `--y-max 63`, boots `--y-max 63`. **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L28 legendary LOOT_TABLE entries per slot/class (m + f).

- **25th net-new-geometry axis — ARGYLE / HARLEQUIN, all 4 slots** (2026-07-28): an all-over
  field of SOLID-FILLED DIAMONDS laid on the diagonal — a rotated checkerboard that fills
  alternate lozenge cells with a bright gold tone while the others keep the jewel body,
  overlaid with a fine cream cross-stitch line along both diagonals. The SOLID FILLED LOZENGE
  CELL is the motif and the FIRST solid-fill tessellation axis; none of the twenty-four prior
  legendary axes per slot occupy it. Critically distinct from the 14th LATTICE (which draws
  the diamond OUTLINE net — thin crossing diagonal lines with EMPTY interiors); here alternate
  diamonds are FILLED SOLID, a two-tone AREA tessellation not a line net. Distinct from every
  other prior axis, all of which are line / point / arc / coil / ring or open-cell-OUTLINE
  fields — this is the only axis whose cells are FILLED. Generator
  `scripts/gen_argyle_axis25.py` (repaint-only, QA-safe by construction — diamonds painted
  ONLY onto already-opaque body pixels; needs scipy). REGAL JEWEL theme reads apart from the
  24th spiral's verdigris teal: a rich saturated body per class with a bright warm GOLD diamond
  and pale CREAM cross-stitch — warrior crimson-wine body + gold diamond, mage royal-violet +
  pale-gold, ranger bottle-green + antique-brass. Slots: chest Harlequin-Cuirass
  `shirt_%s_legendary25`, legs Harlequin-Chausses `pants_%s_legendary25`, boots
  Harlequin-Sabatons `boots_%s_legendary_argyle`, helmet Harlequin-Dome
  `helmet_%s_legendary25`. All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24
  PASS**, repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**. Staged in
  `_argyle_legendary_preview/`, `_argyle_legs_preview/`, `_argyle_boots_preview/`,
  `_argyledome_helmet_preview/`. Previews: `_PREVIEW_argyle_legendary.png`,
  `_PREVIEW_argyle_legs.png`, `_PREVIEW_argyle_boots.png`, `_PREVIEW_argyledome_helmet.png`
  (built by `scripts/preview_axis25.py`). QA flags: helmets `--y-min 2`, pants m `--y-max 62`
  / f `--y-max 63`, boots `--y-max 63`. **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L27 legendary LOOT_TABLE entries per slot/class (m + f).

- **24th net-new-geometry axis — SPIRAL / VOLUTE / WHORL, all 4 slots** (2026-07-28): an
  all-over field of tiled CONTINUOUS CURVED COILS, each winding around a centre with radius
  growing per turn (Archimedean whorl — snail-shell / ionic-volute / fingerprint look). The
  curved-spiral axis none of the twenty-three prior legendary axes per slot occupy. Distinct
  from the 23rd meander (that spiral turns only at RIGHT ANGLES; this coils on a smooth
  CURVE), from the 22nd wave (that line translates along a rail; this WINDS AROUND a fixed
  centre), from the 15th scale (short open arcs, no centre) and the 21st chainmail (closed
  same-radius rings that never coil). Adjacent tiles alternate spin so whorls interlock.
  Generator `scripts/gen_spiral_axis24.py` (repaint-only, QA-safe by construction — coil
  painted ONLY onto already-opaque body pixels; needs scipy). VERDIGRIS / patinated-copper
  theme: cool teal-green oxidized-copper body per class with a bright warm COPPER coil seam
  and dark under-coil relief — reads apart from meander's dark oxidized body + antique-gold
  key. Per class: warrior verdigris-teal body + rose-copper coil, mage teal-indigo +
  pale-aqua-copper, ranger moss-teal + antique-copper. Slots: chest Volute-Cuirass
  `shirt_%s_legendary24`, legs Volute-Chausses `pants_%s_legendary24`, boots Volute-Sabatons
  `boots_%s_legendary_spiral`, helmet Volute-Dome `helmet_%s_legendary24`. All 24 sheets
  (4 slots × 3 classes × m/f): **sprite_qa ALL 24 PASS**, repaint-only mask check **0/24
  mismatch (0 dropped / 0 strays)**. Staged in `_spiral_legendary_preview/`,
  `_spiral_legs_preview/`, `_spiral_boots_preview/`, `_spiraldome_helmet_preview/`. Previews:
  `_PREVIEW_spiral_legendary.png`, `_PREVIEW_spiral_legs.png`, `_PREVIEW_spiral_boots.png`,
  `_PREVIEW_spiraldome_helmet.png` (built by `scripts/preview_axis24.py`). QA flags: helmets
  `--y-min 2`, pants/boots `--y-max 63`. **On approval:** copy the 24 PNGs to
  `sprites/preview_assets/char/`, add L26 legendary LOOT_TABLE entries per slot/class (m + f).

- **21st net-new-geometry axis — CHAINMAIL / RING-MAIL, all 4 slots** (2026-07-28): a
  staggered field of small interlinked CLOSED CIRCLES (mail rings) — the annular /
  closed-curve axis none of the twenty prior legendary axes per slot occupy. Closed cell
  = CIRCLE, distinct from every polygon axis (triangle-trellis 20th, hexagon-honeycomb
  19th, rectangle-ashlar 17th, diamond-lattice 14th), from the OPEN curved arcs of the
  15th scale field, and from all line/point axes. Generator `scripts/gen_chainmail_axis21.py`
  (repaint-only, QA-safe by construction — rings painted ONLY onto already-opaque body
  pixels; needs scipy). Blued-steel theme: bright polished-steel ring seam over a per-class
  blued-iron body (warrior gunmetal / mage blue-steel / ranger green-steel) — reads apart
  from the 20th trellis (silver net over warm/indigo/olive metallic body). Slots: chest
  Ringmail-Hauberk `shirt_%s_legendary21`, legs Mail-Chausses `pants_%s_legendary21`,
  boots Mail-Sabatons `boots_%s_legendary_chainmail`, helmet Mail-Coif
  `helmet_%s_legendary21`. All 24 sheets (4 slots × 3 classes × m/f): **sprite_qa ALL 24
  PASS**, repaint-only mask check **0/24 mismatch (0 dropped / 0 strays)**. Staged in
  `_chainmail_legendary_preview/`, `_chainmail_legs_preview/`, `_chainmail_boots_preview/`,
  `_chaincoif_helmet_preview/`. Previews: `_PREVIEW_chainmail_legendary.png`,
  `_PREVIEW_chainmail_legs.png`, `_PREVIEW_chainmail_boots.png`,
  `_PREVIEW_chaincoif_helmet.png` (built by `scripts/preview_axis21.py`). QA flags: helmets
  `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`. **On approval:**
  copy the 24 PNGs to `sprites/preview_assets/char/`, add L25 legendary LOOT_TABLE entries
  per slot/class (m + f).

---

## Sprite System

### Sheet dimensions
- 800×448px per sheet
- Frame size: 80×64px
- Layout: 10 cols × 7 rows = 70 frames total

### Hair file naming
- Formula: `fileNum = (hairStyle - 1) * 5 + hairNum`
- `hairNum` 1–5 = Dark / Auburn / Red / Blonde / Silver
- All hair sheets: `sprites/preview_assets/char/hair_m{N}.png`
- `skin.png` = skin-only sheet used as composite base

### Critical rule
**Frame-by-frame processing is mandatory** — never stamp frame 0 across all 70 frames or animation breaks.

---

## Male Hairstyles (hair_m1–30)

| Style | Files | Name | Status |
|-------|-------|------|--------|
| 1 | hair_m1–5 | Short | ✅ DONE, clean |
| 2 | hair_m6–10 | Long | ✅ DONE, clean |
| 3 | hair_m11–15 | Medium | ✅ DONE, clean |
| 4 | hair_m16–20 | Ponytail | ✅ DONE, clean |
| 5 | hair_m21–25 | Mohawk | ✅ DONE — spike shape, kept from repo |
| 6 | hair_m26–30 | Man-Bun | ✅ DONE — hand-painted minimal man-bun, June 2026 |

### index.html STYLE_NAMES
```js
['Short', 'Long', 'Medium', 'Ponytail', 'Mohawk', 'Man-Bun']
```

---

## Next Up
- Female warrior helmets (helmet_2–6 are male-only; female warriors have no headgear past t1)

### Reference Designs (upcoming — not yet generated)

**Cowl Helmets** (script: `scripts/redesign_cowl_helmets.py`)

| Item | File | Description |
|------|------|-------------|
| Mage Legendary Cowl | `sprites/preview_assets/char/helmet_mage_legendary_cowl.png` | Hood + attached cape, midnight blue with silver trim; `hatType:'hood'`; female version needed |
| Ranger Legendary Cowl | `sprites/preview_assets/char/helmet_ranger_legendary_cowl.png` | Hood + attached cape, forest green with leather trim; `hatType:'hood'`; female version needed |

**Hood behavior (`hatType:'hood'` in LOOT_TABLE):** When a hood is equipped, `getCharLayers()` in `index.html` renders long/medium/ponytail hair styles as short hair (bangs only). Mohawk and man-bun are unaffected. The cowl sprite draws only the hood cap and hanging cape — the chest area is transparent so the equipped shirt shows through underneath.

**Winged Plate** (script: `scripts/legendary_armor_t1.py`)

| Item | File | Description |
|------|------|-------------|
| Divine Seraph Plate with Wings | `sprites/preview_assets/char/shirt_warrior_legendary1.png` | Gold plate armor with large angelic wings extending beyond body silhouette; warrior legendary shirt; female version (`shirt_warrior_legendary1_f.png`) also needed |

## Awaiting daily approval (staged in working tree, NOT pushed)
- **18th net-new-geometry axis — ALL FOUR SLOTS (HYPER-RARE)** (2026-07-28): a distinct EIGHTEENTH net-new-geometry showcase per slot — the BASKETWEAVE / WICKER family: an interlaced ORTHOGONAL WOVEN field (a checkerboard of square tiles, even tiles carrying short HORIZONTAL weft threads and odd tiles short VERTICAL warp threads, with an under-thread shadow for plaited over/under depth). Distinct from every prior axis: 12th continuous horizontal (no checker/vertical), 16th twill (SHORT DIAGONAL dashes, not orthogonal), 17th ashlar (continuous mortar outlining CLOSED rectangular cells, not solid thread bundles in a checker), 13th point grid (dots, not strokes). All four slots are REPAINT-ONLY (painted solely onto pixels already opaque in the source) -> QA-safe by construction; ALL 24 sheets sprite_qa ALL PASS, 0 dropped/0 strays; sleep frames recolor-only. Dark-leather/bronze-thread palette per class (warrior tanned-leather+bronze, mage indigo+silver, ranger bark-green+tan-straw) so it reads apart from the warm-sandstone ashlar 17th and frost-steel twill 16th. Generated by `scripts/gen_basketweave_axis18.py`; previews `scripts/preview_axis18.py`.
  - **CHEST** `shirt_*_legendary18` + `_f`, staged in `_basketweave_legendary_preview/` (Warlord's Woven Cuirass / Astral Wickerweave Robe / Warden's Woven Jerkin).
  - **LEGS** `pants_*_legendary18` + `_f`, staged in `_basketweave_legs_preview/`.
  - **BOOTS** `boots_*_legendary_basket` + `_f`, staged in `_basketweave_boots_preview/`.
  - **HELMET** `helmet_*_legendary18` + `_f`, staged in `_basketdome_helmet_preview/`.
- **10th net-new-geometry axis — ALL FOUR SLOTS (HYPER-RARE)** (2026-07-28): a distinct TENTH net-new-geometry showcase per slot, bringing chest/legs/boots/helmet to 10-axis parity. All four are REPAINT-ONLY (painted solely onto pixels already opaque in the source `a`) → QA-safe by construction: isolated pixels / background bleed / accent-caused multi-component are impossible, and the opaque mask is identical to source so all frames + animation are preserved. Rigorous verify across all 24 sheets (6 per slot, all 3 classes m+f): opaque_diff=0 and active-frame parity preserved on every sheet (shirt/pants/boots 45/45, helmet 42/42); `sprite_qa.py` ALL PASS on all 24 (shirt defaults, pants m `--y-max 62`/f `--y-max 63`, boots `--y-max 63`, helmet `--y-min 2`). Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. Sleep frames (fi≥60) get the recolor only. Previews: `_PREVIEW_legendary10_axes.png` (each new piece over base body, 4 axes × 6 variants) + `_PREVIEW_legendary10_fullset.png` (full assembled outfit). The four axes:
  - **CHEST — Heraldic Cross** `shirt_*_legendary10` + `_f`, via `scripts/gen_cross_legendary.py`, staged in `_cross_legendary_preview/`. A bold VERTICAL spine crossed by a HORIZONTAL bar forming a couped '+' on the torso (painted on the largest/torso component only) — the cruciform axis distinct from the vertical-only tabard(4), horizontal-only girdle(7), circular roundel(8) and V chevron(9). warrior "Crusader's Cross" (obsidian body + ivory cross, crimson selvage), mage "Astral Rood" (violet body + gold cross, cyan pip), ranger "Warden's Cross" (forest body + pale-bone cross, emerald pip). **On approval:** copy 6 PNGs to `sprites/preview_assets/char/`, add 6 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary') `shirt_warrior_legendary10` classes:['warrior'], `shirt_mage_legendary10` classes:['mage'], `shirt_ranger_legendary10` classes:['ranger'] — m (`..._legendary10.png`) + f (`..._legendary10_f.png`) per slot.
  - **LEGS — Cross-Garter** `pants_*_legendary10` + `_f`, via `scripts/gen_crossgarter_legs.py`, staged in `_crossgarter_legs_preview/`. Two crossing diagonals (an X) bound over each SHIN (per leg-component), the lattice axis distinct from the single sword-belt diagonal(7), vertical side-stripe(8) and horizontal knee-band(9). warrior "Warlord's Cross-Garter" (steel body + oxblood straps, gold knot), mage "Astral Bindings" (violet body + silver straps, cyan knot), ranger "Warden's Leg-Wraps" (forest body + tan straps, copper knot). **On approval:** copy 6 PNGs to char/, add 6 LOOT_TABLE entries (slot:'pants', level:25, rarity:'legendary') `pants_warrior_legendary10`/`pants_mage_legendary10`/`pants_ranger_legendary10` — m + f per slot.
  - **BOOTS — Triple-Strap** `boots_*_legendary_tristrap` + `_f`, via `scripts/gen_tristrap_boots.py` (female warrior source via `_fem_warrior_boots_preview/` fallback), staged in `_tristrap_boots_preview/`. THREE stacked horizontal buckle-straps up each boot shaft (per foot-component), the repeated-band axis distinct from the single instep strap(8), toe-cap(9) and all toe/heel/wing motifs. warrior "Warlord's Triple-Strap" (dark-steel + oxblood straps, gold buckles), mage "Astral Buckles" (violet + silver straps, cyan buckles), ranger "Warden's Field-Boots" (bark-brown + tan straps, copper buckles). **On approval:** copy 6 PNGs to char/, add 6 LOOT_TABLE entries (slot:'boots', level:25, rarity:'legendary') `boots_warrior_legendary_tristrap`/`boots_mage_legendary_tristrap`/`boots_ranger_legendary_tristrap` — m (`..._tristrap.png`) + f (`..._tristrap_f.png`) per slot.
  - **HELMET — Rivet-Rim** `helmet_*_legendary10` + `_f`, via `scripts/gen_rivet_helmet.py`, staged in `_rivet_helmet_preview/`. A reinforcing band low on the helm rim studded with a regular row of METAL rivets (drawn on the largest helm component), the studded-construction axis distinct from the jewelled diadem(7, coloured gems higher on the brow), vertical comb(8) and cheek-plates(9); sits above the face slit so eyes still read. warrior "Warlord's Riveted Helm" (dark-iron + steel band, gold rivets), mage "Astral Riveted Circlet" (indigo + silver band, cyan rivets), ranger "Warden's Studded Hood" (forest + bronze band, copper rivets). **On approval:** copy 6 PNGs to char/, add 6 LOOT_TABLE entries (slot:'helmet', level:25, rarity:'legendary') `helmet_warrior_legendary10`/`helmet_mage_legendary10`/`helmet_ranger_legendary10` — m + f per slot.
- **Jewelled Brow-Band / Diadem-Circlet net-new-geometry helmets — all classes (HYPER-RARE)** (2026-07-27): a SEVENTH net-new-geometry HELMET showcase per class — a bold HORIZONTAL jewelled BROW-BAND / DIADEM CIRCLET wrapping the helmet brow, bringing HELMET to 7-axis parity with chest and legs. Distinct from all six prior helmet geometries, every one of which is a SILHOUETTE EXTENSION reaching past the head (up-out horns l1 / up crest l2 / wide wings l3 / down aventail l4 / forward visor l5 / branching antler l6); the diadem adds ZERO silhouette pixels — it is a repaint band across the brow, the surface-band axis (exactly parallel to how the girdle became the chest 7th and the leg-baldric the legs 7th). Repaint-only onto opaque helm pixels → QA-safe by construction. `helmet_warrior_legendary7` "Sovereign's Diadem" (dark-iron helm + gold circlet, ruby gems), `helmet_mage_legendary7` "Astral Circlet" (indigo helm + silver circlet, sapphire gems), `helmet_ranger_legendary7` "Warden's Circlet" (forest helm + bronze circlet, emerald gems) — all + `_f` (6 sheets). Generated by `scripts/gen_diadem_helmet.py` (girdle authoring model), staged in `_diadem_helmet_preview/`, all 6 QA PASS (sprite_qa --y-min 2). Preview `_PREVIEW_diadem_helmet.png`. **On approval:** copy 6 PNGs to `sprites/preview_assets/char/`, add LOOT_TABLE entries mirroring the prior legendary helmet blocks.
- **Cross-Lacing / Strapped net-new-geometry boots — all classes (HYPER-RARE)** (2026-07-27): a SEVENTH net-new-geometry BOOTS showcase per class — a diagonal CROSS-LACING X-pattern with bright side EYELETS repainted up the boot, bringing BOOTS to 7-axis parity with chest and legs. Distinct from all six prior boots geometries, every one of which is a SILHOUETTE EXTENSION adding mass around the foot (up greave / wide cuff / forward sabaton / rear spur / diagonal wing / down claw); the lacing adds ZERO silhouette pixels — it is a woven surface pattern (per-foot X, drawn per connected component so two-foot poses each get their own lacing). Repaint-only onto opaque boot pixels → QA-safe by construction. `boots_warrior_legendary_lace` "Ironlace Warboots" (dark-steel boot, pale-iron laces, gold eyelets), `boots_mage_legendary_lace` "Astral Laced Striders" (violet boot, silver laces, cyan eyelets), `boots_ranger_legendary_lace` "Wildlace Striders" (bark-brown boot, tan rawhide laces, bone eyelets) — all + `_f` (6 sheets). Generated by `scripts/gen_lace_boots.py` (girdle authoring model), staged in `_lace_boots_preview/`, all 6 QA PASS (sprite_qa --y-max 63). Preview `_PREVIEW_lace_boots.png`. **On approval:** copy 6 PNGs to `sprites/preview_assets/char/`, add LOOT_TABLE entries mirroring the prior legendary boots blocks.
- **Horizontal War-Belt / Girdle net-new-geometry chests — all classes (HYPER-RARE)** (2026-07-27): a SEVENTH net-new-geometry CHEST silhouette per class — a bold HORIZONTAL WAR-BELT wrapping the midriff. Occupies the last unused primary axis, distinct from all six prior chest geometries: winged (l1) flares UP-at-BACK, pauldron (l2) spikes UP-at-SHOULDER-CORNERS, cape (l3) drapes OUT-at-SIDES, tabard (l4) hangs DOWN-CENTRE, gorget (l5) rises UP-at-NECK, baldric (l6) lays a DIAGONAL band — this girdle wraps a HORIZONTAL band across the WAIST. `shirt_warrior_legendary7` "Sovereign's War-Belt" (obsidian/steel body + bronze-leather belt, silver studs), `shirt_mage_legendary7` "Astral Girdle" (arcane-violet body + gold belt, starlight studs), `shirt_ranger_legendary7` "Warden's War-Belt" (forest body + oxblood belt, gold studs) — each + `_f` (6 sheets). Generated by `scripts/gen_girdle_legendary.py`, the direct successor to `gen_baldric_legendary.py` and sharing its key robustness win: the belt accent only REPAINTS pixels that are ALREADY opaque body pixels (`a`), so it adds ZERO new silhouette pixels — isolated pixels / background bleed / accent-caused multi-component frames are impossible BY CONSTRUCTION. Body = the class t4 chest silhouette (`armor_chest_4`/`shirt_mage4`/`shirt_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp (0 px dropped). Accent = a horizontal band placed at `BAND_FRAC=0.64` down each frame's body-mass vertical extent, `BAND_HALF=1.6` px thick: lit CROWN centre-row, dark selvage top/bottom rims, periodic bright STUDS every 3 columns, and a central square BUCKLE — all clamped to `a`, so the belt tracks the torso through every pose/animation exactly. Sleep frames (fi≥60) get the recolor only — no belt (matches winged/pauldron/cape/tabard/gorget/baldric convention). Same per-frame CONNECTIVITY GUARD kept for uniformity (a no-op here by construction). Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: `sprite_qa.py` (shirt defaults) reports ALL PASS CLEAN on all 6 sheets; rigorous opaque-mask parity vs source = 0 added / 0 dropped across all 45 active frames on every sheet (6/6 sheets clean), so all frames + animation preserved. Staged in `_girdle_legendary_preview/`, preview `_PREVIEW_girdle_legendary.png` (idle frame × m/f, all 3 classes) + belt-zoom `_ZOOM_girdle_belt.png`, awaiting daily approval; brings the CHEST slot to a 7-axis net-new-geometry showcase (up-back / up-shoulder / out-sides / down-centre / up-neck / diagonal / horizontal) for all three classes. **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary') — `shirt_warrior_legendary7` "Sovereign's War-Belt" classes:['warrior'], `shirt_mage_legendary7` "Astral Girdle" classes:['mage'], `shirt_ranger_legendary7` "Warden's War-Belt" classes:['ranger'] — one gender:'m' (`..._legendary7.png`) + one gender:'f' (`..._legendary7_f.png`) per slot.
- **Branching Antler-Crown net-new-geometry helmets — all classes (HYPER-RARE)** (2026-07-27): a SIXTH net-new-geometry HELMET silhouette per class — a great BRANCHING ANTLER RACK. A near-VERTICAL beam climbs from each crown corner and throws off multiple FORKED TINES that break OUTWARD, so the head reads as a multi-pronged stag/beast rack — the BRANCHING axis none of the five prior helmets touch (l1 smooth up-out horns/crown/plume, l2 straight-up crest fin, l3 wide-out wings, l4 down-sides aventail, l5 forward visored faceplate). `helmet_warrior_legendary6` "Dreadhorn Warcrown" (dark-iron helm + pale iron-bone antlers), `helmet_mage_legendary6` "Astral Antler-Crown" (cosmic-indigo helm + cyan/violet crystal tines), `helmet_ranger_legendary6` "Wildhorn Stag-Crown" (forest helm + warm natural stag-bone antlers) — each + `_f` (6 sheets). Generated by `scripts/gen_antler_helmet.py`, same authoring philosophy as `gen_visor_helmet.py`/`gen_winghelm_legendary.py`: bodies are the class helmet silhouettes (`helmet_rare1`/`helmet_mage4`/`helmet_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp; the net-new accent is, per side, a 4-connected staircase BEAM rooted one row ABOVE that crown corner's own topmost helm pixel (`crown_corner()` finds the corner on the TOP_BAND), plus FORKED TINES branching off beam points via a Bresenham-style `walk()` that advances one axis per step so every antler pixel shares an edge with the previous (branches fused to the beam → beam fused to the helm by construction). All antler px clamped to y≥`Y_MIN=2` (QA head zone) and drawn ONLY in transparent space (never overpaint the helm). Same per-frame CONNECTIVITY GUARD as the visor/wing (`ndimage.label`, 4-conn) drops any antler px not 4-connected to the body mass, so accent strays are 0 by construction. Beam anchored per-frame relative to each helmet's own top contour → tracks the animation bob. Sleep/empty helmet frames skipped. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks ALL PASS on all 6 sheets (via `/tmp/verify_batch.py`): source px dropped = 0, active-frame parity 42/42 vs source m+f, 0 accent-caused multi-component frames, 0 accent strays. `sprite_qa.py --y-min 2` reports ALL PASS CLEAN on all 6 sheets (the up-biased beam keeps the antlers inside the x30–55 body box → no background-bleed flag). Staged in `_antler_helmet_preview/`, preview `_PREVIEW_antler_helmet.png` (idle/walk/run/cheer/slash × m/f + iso helm-over-skin, all 3 classes) + head-zoom `_ZOOM_antler_head.png`, awaiting daily approval; completes a 6-axis helmet showcase (up-out / straight-up / wide-out / down-sides / forward / branching) for all three classes. **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'helmet', level:25, rarity:'legendary') — `helmet_warrior_legendary6` "Dreadhorn Warcrown" classes:['warrior'], `helmet_mage_legendary6` "Astral Antler-Crown" classes:['mage'], `helmet_ranger_legendary6` "Wildhorn Stag-Crown" classes:['ranger'] — one gender:'m' (`..._legendary6.png`) + one gender:'f' (`..._legendary6_f.png`) per slot.
- **Downward Beast-Claw Talon net-new-geometry boots — all classes (HYPER-RARE)** (2026-07-27): a SIXTH net-new-geometry BOOTS silhouette per class — BEAST-CLAW TALONS that splay DOWNWARD from the sole (a set of claw-points hanging below and slightly outward from the foot). Occupies the DOWNWARD axis none of the five prior boots touch (greave up-shin, cuff wide-ankle, sabaton forward-toe-along-ground, spur heel-out, wing diagonal-ankle). Where the sabaton rakes its point sideways ALONG the ground, these claws drop BELOW it — the foot reads as a raptor claw gripping the earth. `boots_warrior_legendary_claw` "Ironrend Talons" (dark-steel boot + pale iron claws), `boots_mage_legendary_claw` "Voidrend Talons" (deep-violet boot + amethyst/lilac claws), `boots_ranger_legendary_claw` "Wildclaw Talons" (bark-brown boot + bone-white claws) — each + `_f` (6 sheets). Generated by `scripts/gen_claw_boots.py`, same authoring philosophy as `gen_sabaton_boots.py`: bodies are the class t4 boot silhouettes (`armor_boots_4`/`boots_mage4`/`boots_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp; the net-new accent is, for each contiguous foot-run on the boot's bottom row (`runs_on_row()`), up to 3 claws (left/middle/right of the run) each a contiguous DOWNWARD staircase (`CLAW_LEN=3`) rooted directly below an opaque sole pixel — the middle claw drops straight, the outer two drift out per row so the set splays; every claw px is 4-connected UP to the foot by construction. Same per-frame CONNECTIVITY GUARD as the sabaton/spur (`ndimage.label`, 4-conn) drops any claw px not 4-connected to the body, so accent strays are 0 by construction. Drawn ONLY in transparent space below the sole (never overpaint the boot). Sleep frames (fi≥60) get the recolor only — no talons. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks ALL PASS on all 6 sheets (via `/tmp/verify_batch.py`): source px dropped = 0, active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames, 0 accent strays. `sprite_qa.py --y-max 63` reports ALL PASS CLEAN on all 6 sheets. Staged in `_claw_boots_preview/`, preview `_PREVIEW_claw_boots.png` (idle/walk/run/cheer/slash × m/f + iso boots-over-skin, all 3 classes) + foot-zoom `_ZOOM_claw_foot.png`, awaiting daily approval; completes a 6-axis boots showcase (up-shin / wide-ankle / forward-toe / heel-spur / ankle-wing / downward-claw) for all three classes — brings ALL FOUR slots (chest/helmet/legs/boots) to full 6-axis net-new-geometry parity. **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'boots', level:25, rarity:'legendary') — `boots_warrior_legendary_claw` "Ironrend Talons" classes:['warrior'], `boots_mage_legendary_claw` "Voidrend Talons" classes:['mage'], `boots_ranger_legendary_claw` "Wildclaw Talons" classes:['ranger'] — one gender:'m' (`..._claw.png`) + one gender:'f' (`..._claw_f.png`) per slot.
- **Diagonal Baldric net-new-geometry chests — all classes (HYPER-RARE)** (2026-07-25): a SIXTH net-new-geometry CHEST silhouette per class — a bold DIAGONAL BALDRIC/sash crossing the torso from the right shoulder to the left hip (new DIAGONAL axis vs up-back wings / up-shoulder pauldrons / out-sides cape / down-centre tabard / up-neck gorget). `shirt_warrior_legendary6` "Sovereign's Baldric" (obsidian body + oxblood strap, gold studs) / `shirt_mage_legendary6` "Astral Baldric" (violet body + cyan strap, starlight studs) / `shirt_ranger_legendary6` "Warden's Baldric" (forest body + tan-leather strap, bronze studs), + `_f` (6 sheets). Generated by `scripts/gen_baldric_legendary.py`. Robustness win: the strap only REPAINTS already-opaque body pixels (never adds silhouette px), so isolated pixels / bleed / accent-caused multi-component are impossible by construction. QA-passed clean (0 dropped, 45/45 parity, 0 accent-added components, 0 strays; sprite_qa ALL PASS 6/6). Staged in `_baldric_legendary_preview/`. Preview `_PREVIEW_baldric_legendary.png`. Completes 6-axis chest showcase all classes.
- **Standing-Collar Gorget net-new-geometry chests — all classes (HYPER-RARE)** (2026-07-25): a FIFTH net-new-geometry CHEST silhouette per class — a standing high-collar GORGET that rises UP-and-OUTWARD from the NECK, a pair of collar plates peaking just either side of the throat (offset ~2–3px from centre) and tapering down toward the outer shoulders, leaving the front-centre throat open. Occupies a NEW silhouette AXIS distinct from all four existing chest geometries: winged flares UP-at-the-BACK, pauldrons spike UP at the two OUTER SHOULDER CORNERS, cape drapes OUT at the SIDES, tabard hangs DOWN the front-CENTRE — this gorget adds mass UP at the CENTRE-NECK (peaks NEAR the throat, not the outer corners). `shirt_{warrior,mage,ranger}_legendary5` + `_f` (6 sheets): warrior "Sovereign's Gorget" (obsidian/steel body + bright SILVER-plate collar), mage "Runeguard Gorget" (arcane-violet body + AMBER-GOLD rune collar), ranger "Warden's Gorget" (forest body + VERDIGRIS-copper patina collar) — each collar hue distinct from that class's four prior legendary chests. Generated by `scripts/gen_gorget_legendary.py`, same authoring philosophy as `gen_tabard_legendary.py`: bodies are the class t4 chest silhouettes (`armor_chest_4`/`shirt_mage4`/`shirt_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp; the net-new accent is a standing collar drawn ONLY in transparent space ABOVE the torso's top rows, where EACH collar column is stacked directly above THAT column's own topmost opaque body pixel (`neck_top_band()` finds the shoulder/neck band; `collar_height()` gives the peak-either-side-of-throat profile) — so every collar pixel is 4-connected to the body by construction (each column chains straight down to its own shoulder), plus a 1px outward TRIM curl on the tall neck-side plates. Same per-frame CONNECTIVITY GUARD as the tabard/cape (`ndimage.label`, 4-conn) drops any collar pixel not 4-connected to the body mass (never touches body px), so accent strays are 0 by construction. Collar clamped to y≥`Y_MIN=2` (QA head zone). Sleep frames (fi≥60) get the recolor only — no collar. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks ALL PASS on all 6 sheets (via `scripts/verify_gorget.py`): source px dropped = 0, active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames, 0 accent strays. `sprite_qa.py` (shirt defaults) reports ALL PASS CLEAN on all 6 sheets (the collar stays inside the character zone → no background-bleed flag). Staged in `_gorget_legendary_preview/`, preview `_PREVIEW_gorget_legendary.png` (idle/walk/run/cheer/slash × m/f + iso-no-hair, all 3 classes) + neck-zoom `_ZOOM_gorget_collar.png`, awaiting daily approval; completes a 5-axis chest showcase (up-back / up-shoulder / out-sides / down-centre / up-neck) for all three classes. **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary') — `shirt_warrior_legendary5` "Sovereign's Gorget" classes:['warrior'], `shirt_mage_legendary5` "Runeguard Gorget" classes:['mage'], `shirt_ranger_legendary5` "Warden's Gorget" classes:['ranger'] — one gender:'m' (`..._legendary5.png`) + one gender:'f' (`..._legendary5_f.png`) per slot.
- **Rowel-Spur net-new-geometry boots — all classes (HYPER-RARE)** (2026-07-25): a FOURTH net-new-geometry BOOTS silhouette per class — a KNIGHT'S ROWEL-SPUR that projects OUTWARD from the HEEL at ankle height and is tipped by a small spiked star-WHEEL (rowel), bringing the boots slot to a FOUR-silhouette showcase at parity with chest/helmet/legs (which each already have four). Fourth silhouette AXIS for boots, distinct from all three existing: the greave adds mass ABOVE (tall-narrow shin plate to a knee-cop), the cuff flares mass to the SIDE at the ankle (low-wide cavalier fold), the sabaton adds mass at the BOTTOM (forward-raked poulaine toe on the ground row), and this spur adds mass at the HEEL — a thin arm projecting outward ABOVE the ground/toe zone and BELOW the shin, capped by the signature spiked ROWEL WHEEL (unique to this boot; none of the other three have a wheel). `boots_{warrior,mage,ranger}_legendary_spur` + `_f` (6 sheets): warrior "Ironclad Rowel-Spurs" (dark-steel boot + warm-GOLD rowel), mage "Astral Rowel-Striders" (deep-violet boot + cyan-starlight rowel), ranger "Wildspur Treads" (bark-brown boot + burnished-COPPER rowel) — each spur hue chosen distinct from that class's greave/cuff/sabaton accents. Generated by `scripts/gen_spur_boots.py`, same authoring philosophy as `gen_sabaton_boots.py`: bodies are the class t4 boot silhouettes (`armor_boots_4`/`boots_mage4`/`boots_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp; the net-new accent is, on a single heel row `SP_DY=3` above the boot's own bottom row, a contiguous horizontal ARM of length `ARM=3` laid outward from that row's own leftmost/rightmost boot pixel, tipped by a rowel WHEEL (lit hub + dark spikes out/up/down) — every accent pixel 4-connected to the body mass by construction (the arm is a contiguous run from the boot edge, each spike touches the hub which touches the arm). Same per-frame CONNECTIVITY GUARD as the sabaton/cuff/greave (`ndimage.label`, 4-conn) drops any accent pixel not 4-connected to the body mass (never touches body px), so accent strays are 0 by construction. Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body). Sleep frames (fi≥60) get the recolor only — no spur. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks ALL PASS on all 6 sheets (via `scripts/verify_spur.py`): source px dropped = 0, active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames, 0 accent strays. `sprite_qa.py --y-max 63` reports ALL PASS CLEAN on all 6 sheets (the spur stays inside the character zone → no background-bleed flag this time, unlike the sabaton toe). Staged in `_spur_boots_preview/`, preview `_PREVIEW_spur_boots.png` (idle/walk/run/cheer/slash × m/f, all 3 classes) + heel-zoom `_ZOOM_spur_wheel.png`, awaiting daily approval; completes the 4-silhouette boots showcase (up-shin greave / wide-ankle cuff / forward-toe sabaton / heel rowel-spur) for all three classes. **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'boots', level:25, rarity:'legendary') — `boots_warrior_legendary_spur` "Ironclad Rowel-Spurs" classes:['warrior'], `boots_mage_legendary_spur` "Astral Rowel-Striders" classes:['mage'], `boots_ranger_legendary_spur` "Wildspur Treads" classes:['ranger'] — one gender:'m' (`..._spur.png`) + one gender:'f' (`..._spur_f.png`) per slot.
- **Aventail net-new-geometry helmets — all classes (HYPER-RARE)** (2026-07-25): a FOURTH net-new-geometry HELMET silhouette per class — a CAMAIL/AVENTAIL that hangs mail DOWNWARD from the helmet rim along both sides of the face to the shoulders, framing the face (centre columns left open). Occupies the previously-unused DOWNWARD axis vs the three existing helmet silhouettes (up-out horns L1 / straight-up crest L2 / wide-out wings L3). helmet_{warrior,mage,ranger}_legendary4 (+_f), 6 sheets via scripts/gen_aventail_helmet.py, drape anchored per-frame relative to each helmet's own bottom contour (tracks animation bob), connectivity-guarded. QA clean: 0 dropped, 42/42 parity, 0 accent multicomp, 0 accent strays, sprite_qa ALL PASS. Staged in _aventail_helmet_preview, preview _PREVIEW_aventail_helmet.png. Per class: warrior "Ironmaw Camail" (dark steel + silver mail), mage "Nightweave Veil" (indigo + starlight-silver), ranger "Thornmesh Aventail" (bronze/verdigris scale). Completes a 4-axis helmet showcase (up-out / straight-up / wide-out / downward) across all 3 classes.
- **Raked-Poulaine net-new-geometry boots — all classes (HYPER-RARE)** (2026-07-25): a THIRD net-new-geometry BOOTS silhouette per class — a pointed WAR-SABATON whose toe rakes FORWARD into a long tapering poulaine claw-point along the GROUND, completing the boots showcase to three distinct silhouettes (matching chest/helmet/legs, which each already have three). This is the third silhouette AXIS for boots: the greave adds mass ABOVE (tall-narrow shin plate climbing to a knee-cop, top-anchored), the cuff flares mass to the SIDE at the ankle (low-wide cavalier fold, ankle/top-anchored), and this sabaton adds mass at the BOTTOM (a forward-raked toe LONGEST on the ground row, tapering up) — up / out-at-ankle / forward-at-toe, the same three-way silhouette contrast the legs draw (short-flaps/soft-drape/stiff-plate) and helmets draw (up-out horns / straight-up crest / wide-out wing-helm). `boots_{warrior,mage,ranger}_legendary_sabaton` + `_f` (6 sheets): warrior "Dreadclaw Sabatons" (dark-steel boot + pale iron claw-points), mage "Hexbite Striders" (deep violet + amethyst/lilac claw-points), ranger "Beastfang Treads" (bark-brown + bone-white claw-points) — each claw hue chosen distinct from BOTH that class's greave AND cuff boots. Generated by `scripts/gen_sabaton_boots.py`, same authoring philosophy as `gen_cuff_boots.py`/`gen_greave_boots.py`: bodies are the class t4 boot silhouettes (`armor_boots_4`/`boots_mage4`/`boots_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp; the net-new accent, for each of the bottom `TOE_H=3` boot rows, takes that row's own leftmost/rightmost boot pixel and rakes a contiguous run OUTWARD along the ground — longest on the very bottom row (`TOE_MAX=5`) and `TOE_TAPER=2` px shorter per row up, so the toe sweeps to a point at the ground and pulls back in above it. Each run starts edge-adjacent to that row's own boot pixel and is contiguous, so every toe pixel is 4-connected to the body mass by construction; outermost px = dark claw TIP, innermost = shadow crease, rest alternate lit/mid metal. Same per-frame CONNECTIVITY GUARD as the cuff/greave (`ndimage.label`, 4-conn) drops any toe pixel not 4-connected to the body mass (never touches body px), so accent strays are 0 by construction. Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body). Sleep frames (fi≥60) get the recolor only — no toe. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks ALL PASS on all 6 sheets (via `scripts/verify_sabaton.py`): source px dropped = 0, active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames, 0 accent strays. `sprite_qa.py --y-max 63` reports ONLY the expected 1px BACKGROUND-BLEED at (29,63) — the forward toe-claw tip legitimately extends past the x30–55 body box, exactly like the winged/cuff/greave accents (the female warrior sheet passes clean); no ISOLATED/LONE-INNER-BLACK/STRAY/FLOAT on any sheet, the authoritative rigorous verify is clean. Staged in `_sabaton_boots_preview/`, preview `_PREVIEW_sabaton_boots.png` (idle/walk/run/cheer/slash × m/f, all 3 classes) + toe-zoom `_ZOOM_sabaton_toe.png`, awaiting daily approval; completes the 3-silhouette boots showcase (up-shin greave / wide-ankle cuff / forward-toe sabaton) for all three classes. **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'boots', level:25, rarity:'legendary') — `boots_warrior_legendary_sabaton` "Dreadclaw Sabatons" classes:['warrior'], `boots_mage_legendary_sabaton` "Hexbite Striders" classes:['mage'], `boots_ranger_legendary_sabaton` "Beastfang Treads" classes:['ranger'] — one gender:'m' (`..._sabaton.png`) + one gender:'f' (`..._sabaton_f.png`) per slot.
- **Folded-Cuff net-new-geometry boots — all classes (HYPER-RARE)** (2026-07-25): a SECOND net-new-geometry BOOTS silhouette per class — a low, WIDE folded-cuff CAVALIER BOOT whose turned-down cuff flares HORIZONTALLY OUTWARD at the ankle, well beyond the leg's width. Deliberate low-wide read, the opposite of the already-staged tall-narrow greave boots (which climb the shin to a knee-cop): same silhouette-contrast philosophy as the legs (stiff-plate faulds vs soft war-kilt) and helmets (straight-up crest vs wide-out wing-helm). `boots_{warrior,mage,ranger}_legendary_cuff` + `_f` (6 sheets): warrior "Bulwark Warboots" (gunmetal boot + gold cuff), mage "Nightveil Striders" (deep indigo + pale-cyan cuff), ranger "Pathwarden Boots" (bark-brown + olive/tan cuff). Generated by `scripts/gen_cuff_boots.py` (t4-boot silhouette recolored per-frame via luminance-quantile mapping + folded cuff flared outward from each top boot row, per-frame connectivity guard). QA-passed: verify_cuff.py 0 dropped / 45-45 parity / 0 accent-multicomp / 0 accent strays on all 6, sprite_qa ALL PASS. Staged in `_cuff_boots_preview/`, preview `_PREVIEW_cuff_boots.png`, awaiting daily approval; gives the boots slot a 2-silhouette showcase (tall-narrow greave + low-wide cuff). **On approval:** copy the 6 sheets into `sprites/preview_assets/char/` and register in LOOT_TABLE.
- **Lamellar-Fauld net-new-geometry legs — all classes (HYPER-RARE)** (2026-07-25): a THIRD net-new-geometry LEGS silhouette per class — segmented LAMELLAR PLATE FAULDS: a stiff, tiered plate skirt of stacked horizontal armor bands hanging from the hips, distinct from BOTH prior legendary legs. `legendary1` (Seraph Greaves / Starweaver Robe-Tassets / Skyhunter Pelt-Tassets) are SHORT PAIRED hip-flaps (~6 rows); `legendary2` (Warlord's Battle-Kilt / Astral Ritual-Skirt / Wildwood War-Kilt) is a long SMOOTH cloth drape that widens MONOTONICALLY to a soft flared hem; these faulds are STIFF METAL PLATE — the outer edge is TIERED/STEPPED (each lamellar band steps in 1px at its seam then holds) and every band carries a dark top-seam shadow + a lit plate-top highlight so the skirt reads as a stack of overlapping metal lames (horizontal banding vs the kilt's vertical pleats). `pants_warrior_legendary3` "Warlord's Bronze Faulds" (obsidian body + warm brass/bronze plates), `pants_mage_legendary3` "Astral Rune-Faulds" (arcane-violet body + cyan/teal rune-plates), `pants_ranger_legendary3` "Wildwood Scale-Faulds" (forest body + burnished-copper scale-plates) — each + `_f` (6 sheets); each plate hue chosen distinct from that class's cloth war-kilt (warrior crimson / mage midnight / ranger umber). Generated by `scripts/gen_faulds_legs.py`, same authoring philosophy as `gen_warkilt_legs.py`: bodies are the class t4 pants silhouettes (`armor_pants_4` / `pants_mage4` / `pants_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp; the net-new accent is, for each side, a fauld hugging that leg's OUTER edge (`FAULD_ROWS=20` knee-length, `MAXW=4`, `BAND_H=4`-row lames, hem hard-capped at `Y_HEM_MAX=58` to stay out of the y≥60 foot/background zone), off=1 always edge-adjacent to that row's own outer edge and off-ranges contiguous 1..width, so each side's fauld is one 4-connected component fused to the body. Same per-frame CONNECTIVITY GUARD as the kilt/cape (`ndimage.label`, 4-conn) drops any fauld pixel not 4-connected to the body mass (never touches body px), so accent strays are 0 by construction. Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body); sleep frames (fi≥60) get the recolor only — no faulds. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks all PASS on all 6 sheets (via `scripts/verify_faulds.py`): source px dropped = 0, active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames, 0 accent strays. `sprite_qa.py` PASS clean on the 4 male + female-warrior sheets; the two WIDE female hems (mage/ranger) trip ONLY the expected accent background-bleed flag (4px at x28–29, plate legitimately extends past the x30–55 body box, exactly like the war-kilt female mage/ranger) — no ISOLATED / LONE-INNER-BLACK / STRAY / FLOAT on any sheet; the authoritative rigorous verify is clean. Staged in `_faulds_legs_preview/`. Preview: `_PREVIEW_faulds_legs.png` (idle/walk/run/cheer/slash × m/f + isolated fauld-over-skin, all 3 classes). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'pants', level:25, rarity:'legendary') — `pants_warrior_legendary3` "Warlord's Bronze Faulds" classes:['warrior'], `pants_mage_legendary3` "Astral Rune-Faulds" classes:['mage'], `pants_ranger_legendary3` "Wildwood Scale-Faulds" classes:['ranger'] — one gender:'m' (`..._legendary3.png`) + one gender:'f' (`..._legendary3_f.png`) per slot. Gives each class a THIRD net-new-geometry legs silhouette (stiff tiered plate-fauld) alongside its short tassets + draped war-kilt — completing a three-silhouette legs showcase (short-flaps / soft-drape / stiff-plate) for all three classes.
- **Winged net-new-geometry helmets — all classes (HYPER-RARE)** (2026-07-25): a THIRD net-new-geometry helmet silhouette per class — a WINGED HELM whose accent is a pair of feathered wings sweeping WIDE and HORIZONTALLY OUTWARD from the sides of the head. This occupies the previously-unused SIDEWAYS axis: both prior legendary helmets extend UPWARD (the first helmets — Wyrmhorn horns / Starweaver crown-fans / Plumed-Hood crest-feathers — spread UP-and-OUTWARD above the skull; the second, the Crest circlets, are a single NARROW TALL vertical fin). These wings are a broad, low, near-horizontal fan, clearly distinct from both. `helmet_warrior_legendary3` "Valkyr War-Wings" (white→gold seraph plumage on a dark-iron→steel helm), `helmet_mage_legendary3` "Astral Aether-Wings" (cyan→violet arcane wings off the cosmic wizard-hat brim), `helmet_ranger_legendary3` "Falcon Wing-Helm" (cream→russet hawk plumage off the forest hood) — each + `_f` (6 sheets). Generated by `scripts/gen_winghelm_legendary.py`, same authoring philosophy as `gen_crest_legendary.py` / `gen_cape_legendary.py`: bodies are the class helmet silhouettes (`helmet_rare1` / `helmet_mage4` / `helmet_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp (warrior dark-iron→steel, mage cosmic indigo→violet, ranger forest); the net-new accent is, for each side, a feathered wing CENTRED ON THAT SIDE'S WIDEST ROW (the brim / skull-full-width band, found per-frame via `side_edges()`), spanning `BAND_UP=3` rows above to `BAND_DN=2` below with outward reach tapering `TAPER=2` px/row from `SPAN_MAX=10` → a wing/leaf profile; every wing row draws a contiguous outward run off=1..span starting edge-adjacent to that row's own outer edge, so off=1 is always horizontally adjacent to a body pixel and the whole wing is one 4-connected component fused to the helm. Every wing pixel is clamped to y≥`Y_MIN=2` (QA head zone) so wings sit at head height (y~18–30) and never intrude on the torso/floor. Same per-frame CONNECTIVITY GUARD as the cape/greave (`ndimage.label`, 4-conn) drops any wing pixel not 4-connected to the body mass (never touches body px), so accent strays are 0 by construction. Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body). Helmet sheets are empty on the sleep frames, so those are simply skipped. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks all PASS on all 6 sheets (via `scripts/verify_winghelm.py`): source px dropped = 0 (silhouette fully preserved by construction), active-frame parity 42/42 vs source m+f, 0 accent-caused multi-component frames (every wing connects to the helm on every pose), 0 accent strays. `sprite_qa.py --y-min 2` reports ONLY BACKGROUND-BLEED at the wing columns (wings legitimately extend past the x30–55 body box, exactly like the winged/horned chests+helms) — no ISOLATED / LONE-INNER-BLACK / STRAY / FLOAT on any sheet; the authoritative rigorous verify is clean. Staged in `_winghelm_legendary_preview/`. Preview: `_PREVIEW_winghelm_legendary.png` (idle/walk/run/cheer/slash × m/f, all 3 classes). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'helmet', level:25, rarity:'legendary') — `helmet_warrior_legendary3` "Valkyr War-Wings" classes:['warrior'], `helmet_mage_legendary3` "Astral Aether-Wings" classes:['mage'], `helmet_ranger_legendary3` "Falcon Wing-Helm" classes:['ranger'] — one gender:'m' (`..._legendary3.png`) + one gender:'f' (`..._legendary3_f.png`) per slot. Gives each class a THIRD net-new-geometry helmet (wide side-wing silhouette) alongside its up-sweeping horns/crown/plume + tall vertical crest — completing a three-axis helmet showcase (up-out / straight-up / wide-out) for all three classes.
- **War-Kilt net-new-geometry legs — all classes (HYPER-RARE)** (2026-07-25): a SECOND net-new-geometry LEGS silhouette per class — a knee-length draped WAR-KILT that hangs from the hips and flares OUTWARD toward its hem, distinct from the already-staged first legendary legs (Seraph Greaves / Starweaver's Robe-Tassets / Skyhunter's Pelt-Tassets), which are SHORT PAIRED hip-flaps (~6 rows). The kilt is a CONTINUOUS draped skirt down the OUTER edge of each leg from hip to ~knee, flaring to a wide pleated hem — reads as a full A-line skirt on the female avatars, a heavy side-drape on the male. `pants_warrior_legendary2` "Warlord's Battle-Kilt", `pants_mage_legendary2` "Astral Ritual-Skirt", `pants_ranger_legendary2` "Wildwood War-Kilt" — each + `_f` (6 sheets). Generated by `scripts/gen_warkilt_legs.py`, same authoring philosophy as `gen_cape_legendary.py`: bodies are the class t4 pants silhouettes (`armor_pants_4` / `pants_mage4` / `pants_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class-distinct 3-tone ramp (warrior obsidian→steel, mage arcane-violet, ranger forest); the net-new accent is a draped kilt sheet hugging each OUTER leg edge in a class-distinct fabric+trim palette chosen distinct in HUE (warrior crimson→ember + gold-stud hem, mage midnight→starfield + silver hem, ranger umber→moss leather + tan hem), with an alternating vertical-pleat shading that reads as fabric folds (distinguishing it from the smoother cape). Per leg row the kilt's off=1 column is edge-adjacent to that row's own outer edge, off-ranges are contiguous 1..width with width changing ≤1/row (1px at hip → `MAXW=5` at hem, length capped at `KILT_ROWS=20`, hem hard-capped at `Y_HEM_MAX=58` to stay out of the y≥60 foot/background zone for both genders), so each side's kilt is one connected component fused to the body. Same per-frame CONNECTIVITY GUARD as the cape (`ndimage.label`, 4-conn) drops any kilt pixel not 4-connected to the body mass (never touches body px), so accent strays are 0 by construction. Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body). Sleep frames (fi≥60) get the recolor only — no kilt. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: rigorous checks all PASS on all 6 sheets (via `scripts/verify_warkilt.py`): source px dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames (every kilt connects to the body on every pose), 0 accent strays. `sprite_qa.py` (males + female warrior) PASS clean; the two WIDE female hems (mage/ranger) trip only the expected accent background-bleed flag at x<30 (kilt fabric legitimately extends past the x30–55 body box, exactly like the winged/caped chests) — the authoritative rigorous verify is clean. Staged in `_warkilt_legs_preview/`. Preview: `_PREVIEW_warkilt_legs.png` (idle/walk/run/cheer/slash × m/f + isolated kilt-over-skin, all 3 classes). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'pants', level:25, rarity:'legendary') — `pants_warrior_legendary2` "Warlord's Battle-Kilt" classes:['warrior'], `pants_mage_legendary2` "Astral Ritual-Skirt" classes:['mage'], `pants_ranger_legendary2` "Wildwood War-Kilt" classes:['ranger'] — one gender:'m' (`..._legendary2.png`) + one gender:'f' (`..._legendary2_f.png`) per slot. Gives each class a SECOND net-new-geometry legs silhouette (draped war-kilt) alongside its first tasset legs.
- **Crest net-new-geometry helmets — all classes (HYPER-RARE)** (2026-07-25): a SECOND net-new-geometry helmet silhouette per class, a tall VERTICAL CREST/PLUME rising straight up from the crown — a NARROW, TALL profile deliberately distinct from the wide PAIRED side-flares of the first helmets (warrior Wyrmhorn horns, mage Starweaver crown-fans, ranger Plumed-Hood crest-feathers, all of which spread UP-and-OUTWARD to the sides). `helmet_warrior_legendary2` "Legion War-Crest" (crimson horsehair crest on a brass galea), `helmet_mage_legendary2` "Astral Spire Circlet" (amethyst crystal spire w/ gold star tip on the cosmic-recolored wizard hat), `helmet_ranger_legendary2` "Falcon War-Plume" (hawk-feather plume w/ pale tip on the forest-recolored hood) — each + `_f` (6 sheets). Generated by `scripts/gen_crest_legendary.py`, same authoring philosophy as `gen_horned_legendary_helm.py` / `gen_mage_crown_legendary.py`: bodies are the class helmet silhouettes (`helmet_rare1` / `helmet_mage4` / `helmet_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class 3-tone ramp (warrior brass, mage cosmic indigo→violet→starlight, ranger forest), and the net-new accent is a single tall vertical fin. CONNECTIVITY BY CONSTRUCTION: the crest is centered on the column of each frame's TOPMOST opaque crown pixel (`anchor_x`) and starts one row above it, so every crest row shares column `anchor_x` (one 4-connected blob) and the root pixel sits directly above the opaque crown (fused to the helm); all crest pixels are above the topmost opaque row so nothing ever overpaints the helm. Height is CLAMPED per-frame so the tip stays y≥2 (QA head zone) — important for the mage, whose cone hat tip is already high (min top row y=8 vs warrior y=17 / ranger y=14) — and the leaf width profile always tapers to a 1px tip so a shortened crest (mage) still reads as a spire. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: all 6 sheets PASS `sprite_qa.py --y-min 2` CLEAN (crest stays inside the head zone → no background-bleed flag, unlike the horns/wings). Rigorous checks all PASS on all 6 sheets (via `scripts/verify_crest.py`): source px dropped = 0 (silhouette fully preserved by construction), active-frame parity 42/42 vs source m+f, crest present on all 42 active frames, 0 accent-caused multi-component frames, 0 accent strays. Staged in `_crest_legendary_preview/`. Preview: `_PREVIEW_crest_legendary.png` (idle/walk/run/cheer/slash × m/f, all 3 classes). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'helmet', level:25, rarity:'legendary') — `helmet_warrior_legendary2` "Legion War-Crest" classes:['warrior'], `helmet_mage_legendary2` "Astral Spire Circlet" classes:['mage'], `helmet_ranger_legendary2` "Falcon War-Plume" classes:['ranger'] — one gender:'m' (`..._legendary2.png`) + one gender:'f' (`..._legendary2_f.png`) per slot. Gives each class a SECOND net-new-geometry helmet (tall vertical-crest silhouette) alongside its first horns/crown/plumed-hood helmet.
- **Draped-Warcape net-new-geometry chests — all classes (HYPER-RARE)** (2026-07-25): a THIRD net-new-geometry chest showcase per class, changing the silhouette with a CAPE that drapes DOWN each side of the torso and flares OUTWARD toward the hem — distinct from BOTH the already-staged winged chests (flare UP at the back) AND the pauldron chests (spike UP at the shoulders). `shirt_warrior_legendary3` "Warlord's Warcape", `shirt_mage_legendary3` "Astral Shroud", `shirt_ranger_legendary3` "Wildwood Cloak" — each + `_f` (6 sheets). Generated by `scripts/gen_cape_legendary.py`, same authoring philosophy as `gen_pauldron_legendary.py`: bodies are the class t4 chest silhouettes (`armor_chest_4` / `shirt_mage4` / `shirt_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class-distinct 3-tone ramp (warrior obsidian→steel, mage arcane-violet, ranger forest), and the net-new accent is a pair of draped CAPE sheets that hug each side edge of the torso and flare outward toward the hem, in a class-distinct fabric+trim palette chosen distinct in HUE from every prior legendary (warrior crimson→ember fabric + gold trim, mage midnight→starfield fabric + silver trim, ranger umber→moss leather + tan-fur trim). Per body row the cape's off=1 column is edge-adjacent to that row's own outer edge, and off-ranges are contiguous 1..width with width changing ≤1/row (widening down the body, `HEM_DROP=4`, hard-capped at `Y_HEM_MAX=52` so the hem stays inside the QA character zone for BOTH genders → no background-bleed flag, like the seraph legs), so each side's cape is one connected component fused to the torso. A per-frame CONNECTIVITY GUARD (`ndimage.label`, 4-conn) drops any cape pixel not 4-connected to the body mass — needed because a few contorted poses (female slash fi=55) split the torso edge and stranded a 3px hem fragment; the guard removes ONLY such floaters (never body px), so accent strays are 0 by construction on every frame. Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body). Sleep frames (fi≥60) get the recolor only — no cape. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: all 6 sheets PASS `sprite_qa.py` CLEAN (default shirt flags — no bleed). Rigorous checks all PASS on all 6 sheets (via `scripts/verify_cape.py`): source px dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames (every cape connects to the body on every pose), 0 accent strays. Staged in `_cape_legendary_preview/`. Preview: `_PREVIEW_cape_legendary.png` (idle/walk/run/cheer/slash × m/f + isolated chest-over-skin, all 3 classes). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary') — `shirt_warrior_legendary3` "Warlord's Warcape" classes:['warrior'], `shirt_mage_legendary3` "Astral Shroud" classes:['mage'], `shirt_ranger_legendary3` "Wildwood Cloak" classes:['ranger'] — one gender:'m' (`..._legendary3.png`) + one gender:'f' (`..._legendary3_f.png`) per slot. Gives each class a THIRD net-new-geometry chest (draped-cape silhouette) alongside its winged + pauldron chests — completing a three-silhouette chest showcase (back / shoulders / sides) for all three classes.
- **Great-Pauldron net-new-geometry chests — all classes (HYPER-RARE)** (2026-07-25): a SECOND net-new-geometry chest showcase per class, changing the silhouette at the SHOULDERS (distinct from the already-staged winged chests, which flare at the back). `shirt_warrior_legendary2` "Colossus Pauldrons", `shirt_mage_legendary2` "Archon's Mantle", `shirt_ranger_legendary2` "Wildwarden's Spaulders" — each + `_f` (6 sheets). Generated by `scripts/gen_pauldron_legendary.py`, same authoring philosophy as `gen_seraph_legs.py`: bodies are the class t4 chest silhouettes (`armor_chest_4` / `shirt_mage4` / `shirt_ranger4` + `_f`) recolored per-frame via luminance-QUANTILE mapping onto a class-distinct 3-tone ramp (warrior obsidian→steel, mage arcane-violet, ranger forest), and the net-new accent is a pair of large layered SPAULDERS (shoulder plate tapering to a spike) fanning UP-and-OUTWARD from each shoulder corner, mirrored L/R, in a class-distinct spike palette (warrior molten-copper, mage prismatic cyan-crystal, ranger bone-white). Spaulders use the proven seraph `side_anchor()` pattern at the silhouette TOP band (`shoulder_anchor()`), with contiguous off-ranges so each plate is 4-connected to the torso by construction (dy=0 off=1 pixel is horizontally edge-adjacent to a body shoulder pixel). Accents drawn ONLY in transparent out-of-silhouette space (never overpaint the body). Sleep frames (fi>=60) get the recolor only — no spaulders. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: all 6 sheets PASS `sprite_qa.py` clean (default shirt flags). Rigorous checks all PASS on all 6 sheets (via `/tmp/verify_pauldron.py`): source px dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source m+f, 0 accent-caused multi-component frames (every spaulder connects to the body on every pose), 0 accent strays. Staged in `_pauldron_legendary_preview/`. Preview: `_PREVIEW_pauldron_legendary.png` (idle/walk/run/cheer/slash × m/f + isolated chest-over-skin, all 3 classes). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary') — `shirt_warrior_legendary2` "Colossus Pauldrons" classes:['warrior'], `shirt_mage_legendary2` "Archon's Mantle" classes:['mage'], `shirt_ranger_legendary2` "Wildwarden's Spaulders" classes:['ranger'] — one gender:'m' (`..._legendary2.png`) + one gender:'f' (`..._legendary2_f.png`) per slot. Gives each class a SECOND net-new-geometry chest (shoulder silhouette) alongside its winged chest.
- **Ranger net-new-geometry helmet + legs — "Skyhunter's Plumed Hood" (helmet) + "Skyhunter's Pelt-Tassets" (pants) + "Skyhunter's Talon Striders" (boots) (ranger, HYPER-RARE)** (2026-07-25): completes the ranger 4-slot net-new-geometry showcase called for by the ranger winged-chest note ("a matching ranger helmet/pants/boots set could follow"), giving the ranger the same full showcase as the warrior (winged chest + horned helm + Seraph greaves/sabatons) and the mage (winged chest + Starweaver crown/tassets/striders). `helmet_ranger_legendary1` + `_f`, `pants_ranger_legendary1` + `_f`, `boots_ranger_legendary1` + `_f` (6 sheets). Generated by `scripts/gen_ranger_crown_legendary.py` (helmet) and `scripts/gen_ranger_legs_legendary.py` (pants+boots), same authoring philosophy as the mage crown/legs gens: bodies are the ranger `helmet_ranger4` / `pants_ranger4` / `boots_ranger4` silhouettes recolored via per-frame luminance-QUANTILE mapping onto the SAME forest→emerald→bronze-gold 3-tone ramp as the Skyhunter's Wings chest (deep forest shadow → living emerald base → pale bronze-gold highlight), and all net-new accent geometry uses the identical HAWK-plumage palette (cream leading edge → russet-brown vane → dark-brown trailing, dark outline, bright feather tips) so all four slots read as one grounded bird-of-prey set (NOT celestial/arcane). HOOD: a pair of swept-back hawk crest-feather PLUMES that flare UP-and-OUTWARD from the hood's two brim corners (each capped by a bright feather tip), framing the head like raptor crest-feathers. Uses the same `corner_anchor()` + seraph ankle-wing fan pattern as the mage crown (off=1..outer each row, continuous off=1 column) so each plume is 4-connected to the hood by construction — NOT the skull-dome anchor (correct call: the mage crown lesson about anchoring accents to the garment's own brim corner applies here too). TASSETS: trailing hunter's pelt-streamers sweeping down-and-out from each hip. STRIDERS: small talon ankle-fins fanning up-and-out from each foot. Tassets/striders use the seraph `side_anchor()` at the silhouette top-band so they root at hip/ankle corners and share an edge with the body. Sleep frames (fi≥60) get the ranger recolor only — no accents. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: all 6 sheets PASS `sprite_qa.py` clean (helmet `--y-min 2`, pants `--y-max 62`, boots `--y-max 63`) — no background-bleed or stray flags on any sheet. Rigorous checks all PASS on all 6 sheets: source px dropped = 0 (silhouette fully preserved by construction), active-frame parity (helmet 42/42, pants/boots 45/45) vs source m+f, presence parity 70/70, 0 TRUE accent-caused floats (every plume/tasset/strider is 4-connected to the body on every pose — verified by binary-dilation adjacency to source), 0 strays-not-in-source. NOTE: the ranger hood silhouette is natively a 3-component shape (hood dome + 2 side pieces) in `helmet_ranger4`, so the output helmet reports 3 components/frame — this is IDENTICAL to the source component count (pre-existing SOURCE geometry inherited, not accents), same convention as the ranger winged chest's small in-source islands. Staged in `_ranger_crown_legendary_preview/` (helmet) + `_ranger_legs_legendary_preview/` (pants+boots). Preview: `_PREVIEW_ranger_crown_legs.png` (full Skyhunter avatar + isolated hood/tassets/striders, idle/walk/run/cheer/slash × m/f). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (level:25, rarity:'legendary', classes:['ranger']) — `helmet_ranger_legendary1` "Skyhunter's Plumed Hood" (slot:'helmet'), `pants_ranger_legendary1` "Skyhunter's Pelt-Tassets" (slot:'pants'), `boots_ranger_legendary1` "Skyhunter's Talon Striders" (slot:'boots') — one gender:'m' (`..._ranger_legendary1.png`) + one gender:'f' (`..._ranger_legendary1_f.png`) per slot. With the winged chest already staged, ranger then has a full 4-slot net-new-geometry showcase — completing net-new-geometry showcases across ALL THREE classes (warrior Seraph+Wyrmhorn, mage Starweaver, ranger Skyhunter).
- **Mage net-new-geometry legs + crown — "Starweaver's Crown" (helmet) + "Starweaver's Robe-Tassets" (pants) + "Starweaver's Comet Striders" (boots) (mage, HYPER-RARE)** (2026-07-25): completes the mage 4-slot net-new-geometry showcase called for by the mage winged-chest note ("a matching mage helmet/pants/boots set could follow"), giving the mage the same full showcase as the warrior (winged chest + horned helm + Seraph greaves/sabatons). `helmet_mage_legendary1` + `_f`, `pants_mage_legendary1` + `_f`, `boots_mage_legendary1` + `_f` (6 sheets). Generated by `scripts/gen_mage_crown_legendary.py` (helmet) and `scripts/gen_mage_legs_legendary.py` (pants+boots), same authoring philosophy as `gen_horned_legendary_helm.py` / `gen_seraph_legs.py`: bodies are the mage `helmet_mage4` / `pants_mage4` / `boots_mage4` silhouettes recolored via per-frame luminance-QUANTILE mapping onto the SAME cosmic 3-tone ramp as the Starweaver's Wings chest (deep indigo shadow → arcane violet base → pale starlight highlight), and all net-new accent geometry uses the identical arcane crystal palette (cyan-white lit face → nebula-blue → violet trailing, dim outline, bright star tips) so all four slots read as one arcane set. CROWN: a pair of crystalline crown-fans that flare UP-and-OUTWARD from the wizard hat's two brim corners (each capped by a bright star point), framing the hat like crystal wings. IMPORTANT lesson: the mage helmet is a TALL wizard-hat cone, so the skull-dome anchor used by the warrior horned helm is WRONG here (spires float off the cone) — instead each crown-fan is anchored to the hat silhouette's own outer brim corner (`corner_anchor()`) and built with the proven seraph ankle-wing fan pattern (off=1..outer each row, continuous off=1 column) so it is 4-connected to the hat by construction. TASSETS: trailing arcane hip-streamers sweeping down-and-out from each hip. STRIDERS: small comet ankle-fins fanning up-and-out from each foot. Tassets/striders use the seraph `side_anchor()` at the silhouette top-band so they root at hip/ankle corners and share an edge with the body. Sleep frames (fi≥60) get the cosmic recolor only — no accents. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: all 5 legs sheets + the female helmet PASS `sprite_qa.py` clean; the male helmet reports ONLY BACKGROUND-BLEED (2px at x=29, the left crown-fan tip) outside the x30–55 character zone — this is the intentional crown silhouette itself, NOT a stray (same convention as the horned helm / winged chest). Rigorous checks all PASS on all 6 sheets: source px dropped = 0 (silhouette fully preserved by construction), active-frame parity (helmet 42/42, pants/boots 45/45) vs source m+f, 0 accent-caused multi-component frames (every accent connects to the body on every pose), 0 accent strays. Staged in `_mage_crown_legendary_preview/` (helmet) + `_mage_legs_legendary_preview/` (pants+boots). Preview: `_PREVIEW_mage_crown_legs.png` (full Starweaver avatar + isolated crown/tassets/striders, idle/walk/run/cheer/slash × m/f). **On approval:** copy the 6 PNGs to `sprites/preview_assets/char/`, and add 6 LOOT_TABLE entries (level:25, rarity:'legendary', classes:['mage']) — `helmet_mage_legendary1` "Starweaver's Crown" (slot:'helmet'), `pants_mage_legendary1` "Starweaver's Robe-Tassets" (slot:'pants'), `boots_mage_legendary1` "Starweaver's Comet Striders" (slot:'boots') — one gender:'m' (`..._mage_legendary1.png`) + one gender:'f' (`..._mage_legendary1_f.png`) per slot. With the winged chest already staged, mage then has a full 4-slot net-new-geometry showcase; a matching ranger helmet/pants/boots set would complete showcases across all three classes.
- **Ranger winged legendary — "Skyhunter's Wings" (ranger chest, HYPER-RARE)** (2026-07-25): the ranger-class counterpart to the warrior "Divine Seraph Plate" and mage "Starweaver's Wings" — the FIRST ranger sprite that goes BEYOND a palette recolor, completing the "each class has a winged hyper-rare" showcase trio. `shirt_ranger_legendary1` + `_f` (2 sheets). Generated by `scripts/gen_ranger_winged_legendary.py`, same authoring philosophy as `gen_mage_winged_legendary.py`: body is the `shirt_ranger4[_f]` t4-chest silhouette (full m+f coverage → 45 active frames, tracks every pose) recolored via per-frame luminance-QUANTILE mapping onto a glowing ranger-family 3-tone ramp (deep forest shadow → living emerald base → pale bronze-gold highlight; leans bronze vs. the Verdant Monarch emerald so it reads as its own item). Wings are hand-authored HAWK-plumage geometry deliberately natural/earthy (cream leading edge → russet-brown vane → dark-brown trailing edge, dark outer outline, primaries separated every 3rd row) and — unlike the warrior/mage — carry NO halo, so the piece reads unmistakably as a grounded hunter's bird-of-prey wing, not a celestial/arcane one. The wing profile is deliberately BROADER + FLATTER (a "soaring hawk" span that opens fast and holds, tapering to a swept primary tip) vs. the mage/warrior upswept angelic fan. Wings are mirrored L/R, drawn UNDER the chest and anchored per-frame to the skull-dome cx + shoulder row, with subtle ±1px flutter across each animation row (run/slash tuck 1px). Each wing is guaranteed 4-connected to the body by a per-pose nearest-pixel ROOT bridge (`bridge_to_body()`), and bronze pauldron caps are drawn OVER the chest at the wing roots. Sleep frames (fi≥60, lying down) get the verdant recolor only — no wings — matching the winged-chest convention. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: `sprite_qa.py` reports ONLY BACKGROUND-BLEED (wing-plumage tones) at the wing columns outside the x30–55 character zone — these are the intentional wings, i.e. the legendary silhouette itself, NOT strays. Rigorous checks all PASS: source chest px dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source (m+f), wing-presence parity 35/35 m+f, 0 accent-caused multi-component frames (every wing bridges to the body on every pose), 0 accent strays (the small islands per sheet — e.g. a 1px at (33,44)m / (42,45)f — are verified all_in_source=True, i.e. pre-existing SOURCE geometry inherited by every ranger-t4-derived legendary, not accents). Staged in `_ranger_winged_legendary_preview/`. Preview: `_PREVIEW_ranger_winged_legendary.png` (idle/walk/run/cheer/slash × m/f). **On approval:** copy the 2 PNGs to `sprites/preview_assets/char/`, and add 2 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary', classes:['ranger']) — `shirt_ranger_legendary1` "Skyhunter's Wings" gender:'m' (file `shirt_ranger_legendary1.png`) + gender:'f' (file `shirt_ranger_legendary1_f.png`). Note: with this, all three classes now have a winged net-new-geometry chest showcase; a matching ranger helmet/pants/boots set could follow in later daily batches to give the ranger a full 4-slot showcase like the warrior.
- **Mage winged legendary — "Starweaver's Wings" (mage chest, HYPER-RARE)** (2026-07-25): the mage-class counterpart to the warrior "Divine Seraph Plate" — the FIRST mage sprite that goes BEYOND a palette recolor (net-new arcane wing geometry giving a dramatic bigger-than-normal silhouette). `shirt_mage_legendary1` + `_f` (2 sheets). Generated by `scripts/gen_mage_winged_legendary.py`, same authoring philosophy as `gen_winged_legendary.py`: body is the `shirt_mage4[_f]` t4-robe silhouette (full m+f coverage → 45 active frames, tracks every pose) recolored via per-frame luminance-QUANTILE mapping onto a cosmic 3-tone ramp (deep indigo shadow → arcane violet base → pale starlight highlight). Wings are hand-authored feathered geometry deliberately kept COOL/arcane (cyan-white leading edge → nebula-blue vane → violet trailing edge, dim-violet ribs, shaded outer outline) so the piece reads unmistakably as arcane mage magic and is NOT a recolor of the warrior's warm white/gold wing. Wings are mirrored L/R, drawn UNDER the robe and anchored per-frame to the skull-dome cx + shoulder row, with subtle ±1px flutter across each animation row (run/slash tuck 1px). Distinct from the warrior halo: instead of a free-floating halo (which would be an isolated component), each wing is guaranteed 4-connected to the body by a per-pose nearest-pixel ROOT bridge (`bridge_to_body()` — draws a straight ROOT line from the wing pixel nearest the body to the nearest body pixel, closing whatever gap the pose leaves; the mage robe is narrower than the warrior plate so a fixed offset would float the wing), and arcane shoulder caps are drawn OVER the robe at the wing roots. Sleep frames (fi≥60, lying down) get the cosmic recolor only — no wings — matching the winged-chest + hat convention. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: `sprite_qa.py` reports ONLY BACKGROUND-BLEED (69 px/sheet) at the wing columns outside the x30–55 character zone — these are the intentional wings, i.e. the legendary silhouette itself, NOT strays (no ISOLATED/STRAY/LONE-INNER-BLACK/FLOAT categories on either sheet). Rigorous checks all PASS: source robe px dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source (m+f), 0 accent-caused multi-component frames (every wing bridges to the body on every pose), 0 accent strays (the single 1px island per sheet is pre-existing SOURCE geometry, not an accent — kept to preserve the source). Staged in `_mage_winged_legendary_preview/`. Preview: `_PREVIEW_mage_winged_legendary.png` (idle/walk/run/cheer/slash × m/f). **On approval:** copy the 2 PNGs to `sprites/preview_assets/char/`, and add 2 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary', classes:['mage']) — `shirt_mage_legendary1` "Starweaver's Wings" gender:'m' (file `shirt_mage_legendary1.png`) + gender:'f' (file `shirt_mage_legendary1_f.png`). Note: this gives the mage class its first net-new-geometry showcase piece (paralleling the warrior Divine Seraph); a matching mage helmet/pants/boots set could follow in later daily batches, and a ranger equivalent would complete net-new-geometry showcases across all three classes.
- **Horned legendary helmet — "Wyrmhorn Warhelm" (warrior helmet, HYPER-RARE)** (2026-07-25): the second sprite that goes BEYOND a palette recolor, and the first net-new geometry in the *helmet* slot (the winged Seraph is a chest). `helmet_warrior_legendary1` + `_f` (2 sheets). Generated by `scripts/gen_horned_legendary_helm.py`, same authoring philosophy as `gen_winged_legendary.py`: body is the `helmet_rare1[_f]` silhouette (full m+f coverage → 42 active frames, tracks every pose) recolored via per-frame luminance-QUANTILE mapping onto a dark-iron 3-tone ramp (deep iron shadow → iron base → steel highlight) so the pale bone horns pop. Horns are hand-authored net-new geometry — a pair of curved dragon horns (ivory highlight → bone base → bone shadow, dark outer outline, ridge-notch segmentation every 3rd row) sweeping up-and-outward ~8px above and ~11px out from the skull, mirrored L/R, anchored per-frame to the skull-dome (`make_head_dome_fn`) head_top+cx so they track the head on every frame incl. the head-turn on cheer. Because horns are rigid bone they simply track the head (no flutter — cleaner and more physically correct than the fluttering wings). Each horn is root-bridged to the helm's ACTUAL per-row edge (the helm edge narrows at head_top, widens just below, so a fixed offset would detach one horn — the bridge closes the real gap), making helm+both-horns a single connected component. Helmets have no sleep frames; empty frames skipped. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: `sprite_qa.py --y-min 2` reports BACKGROUND-BLEED at the horn tips (y=29 row bone tones) — these are the intentional horns exceeding the normal helm zone, i.e. the legendary silhouette itself, NOT strays. Rigorous checks all PASS: source helm pixels dropped = 0 (silhouette fully preserved by construction), active-frame parity 70/70 vs source (m+f), 0 multi-component frames (both horns connect), 0 sub-3px islands. Staged in `_horned_legendary_preview/`. Preview: `_PREVIEW_horned_legendary.png` (idle/walk/run/cheer × m/f). **On approval:** copy the 2 PNGs to `sprites/preview_assets/char/`, and add 2 LOOT_TABLE entries (slot:'helmet', level:25, rarity:'legendary', classes:['warrior']) — `helmet_warrior_legendary1` "Wyrmhorn Warhelm" gender:'m' (file `helmet_warrior_legendary1.png`) + gender:'f' (file `helmet_warrior_legendary1_f.png`). Note: pairs naturally with the winged Divine Seraph chest as a net-new-geometry showcase set; matching pants/boots could follow in later daily batches.
- **Winged legendary — "Divine Seraph Plate" (warrior chest, HYPER-RARE)** (2026-07-24): the first sprite that goes BEYOND a palette recolor — net-new angel-wing geometry giving a dramatic bigger-than-normal silhouette. `shirt_warrior_legendary1` + `_f` (2 sheets). Generated by `scripts/legendary_armor_t1.py`: body is the `shirt_rare1[_f]` silhouette (full m+f coverage → tracks every pose) recolored via per-frame luminance-QUANTILE mapping onto a 6-step gold plate ramp (seams land darkest, trim near-white); black source-edge pixels kept as pure outline. Wings are hand-authored feathered geometry (white leading edge → warm-white vane → pale-gold trailing edge, dim-gold ribs, shaded outline), mirrored L/R, drawn UNDER the plate and anchored per-frame to the skull-dome cx + garment neck row, so they spread ~13px beyond the body on every upright frame with subtle pose tracking; gold pauldron caps mount the wing roots over the shoulders. Sleep frames (fi≥60) get the gold plate only (character lies down — house convention). Wing colors all pass sprite_shade's accent test (r≥230 & g≥190) so the cosine shader freezes them and the white/gold never crushes. QA: `sprite_qa.py` reports BACKGROUND-BLEED at x≤29 / x≥56 — these are the intentional wings exceeding the x30–55 character zone, i.e. the legendary silhouette itself, NOT strays. Rigorous checks all PASS: source body pixels dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source (m+f), and after clearing 3 sub-3px islands (sanctioned <3px auto-fix) there are 0 stray/floating components on any frame. Staged in `_winged_legendary_preview/`. Preview: `_PREVIEW_winged_legendary.png` (idle/walk/run/jump/cheer/slash × m/f). **On approval:** copy the 2 PNGs to `sprites/preview_assets/char/`, and add 2 LOOT_TABLE entries (slot:'shirt', level:25, rarity:'legendary', classes:['warrior']) — `shirt_warrior_legendary1` "Divine Seraph Plate" gender:'m' (file `shirt_warrior_legendary1.png`) + gender:'f' (file `shirt_warrior_legendary1_f.png`). Note: this is a chest-only showcase piece; a matching helmet/pants/boots set could follow in later daily batches if the wings are approved.
- **Seraph legs — "Divine Seraph Greaves" (pants) + "Divine Seraph Sabatons" (winged boots) (warrior, HYPER-RARE)** (2026-07-25): completes the net-new-geometry Divine Seraph set called for by the winged-chest note ("matching pants/boots could follow"). `pants_warrior_legendary1` + `_f` and `boots_warrior_legendary1` + `_f` (4 sheets). Generated by `scripts/gen_seraph_legs.py`, same authoring philosophy as `gen_winged_legendary.py`: body is the `pants_rare1[_f]` / `boots_rare1[_f]` silhouette (full m+f coverage → 45 active frames, tracks every pose) recolored via per-frame luminance-QUANTILE mapping onto the SAME Divine gold 3-tone ramp as the chest (deep gold shadow → gold base → pale gold highlight), and net-new feather geometry uses the identical FE feather palette (white → warm-white → pale-blue vane, dim outline). GREAVES: a pair of hanging feathered hip-tassets that sweep down-and-outward from each hip corner (dy 0–5, mirrored L/R). SABATONS: a pair of small angel ANKLE-WINGS (Hermes motif) fanning up-and-outward from the outer-top edge of each foot (dy 0–5, mirrored L/R). Accents anchored per-frame at the TOP band of the silhouette (hip / ankle) via `side_anchor()` so they root at the correct corner on every pose, drawn ONLY in transparent out-of-silhouette space and sharing an edge with the garment so each accent is connected to its own leg/foot (no isolated pixels). Sleep frames (fi≥60, lying down) get the gold recolor only — no accents — matching the winged chest and the hat convention. Shading applied in-script via `shade()` — do NOT run `sprite_shade.py` again. QA: all 4 sheets PASS `sprite_qa.py` (pants `--y-max 62`, boots `--y-max 63`) — accents sit within the character zone so there is NO background-bleed flag this time. Rigorous checks all PASS: source pixels dropped = 0 (silhouette fully preserved by construction), active-frame parity 45/45 vs source (all m+f), 0 detached/new components (every accent overlaps + connects to its source foot/hip; the boots' two-foot multi-component and any <3px bits are pre-existing SOURCE geometry, not accents), 0 accent strays. Staged in `_seraph_legs_preview/`. Preview: `_PREVIEW_seraph_legs.png` (full Seraph avatar + isolated greaves/sabatons over skin, idle/walk/run/cheer/slash × m/f). **On approval:** copy the 4 PNGs to `sprites/preview_assets/char/`, and add 4 LOOT_TABLE entries (level:25, rarity:'legendary', classes:['warrior']) — `pants_warrior_legendary1` "Divine Seraph Greaves" (slot:'pants') gender:'m' (`pants_warrior_legendary1.png`) + gender:'f' (`pants_warrior_legendary1_f.png`); `boots_warrior_legendary1` "Divine Seraph Sabatons" (slot:'boots') gender:'m' (`boots_warrior_legendary1.png`) + gender:'f' (`boots_warrior_legendary1_f.png`). With the winged chest + horned helm already staged, warrior then has a full 4-slot net-new-geometry showcase (Seraph theme on chest/pants/boots, Wyrmhorn helm).
- **Female legendary helmets** (2026-07-23): helmet_rare1_f (Crimson Sentinel Helm), helmet_rare2_f (Shadow Warden Helm), helmet_rare3_f (Solar Paladin Helm). The female legendary sets already ship shirt/pants/boots `_rare*_f` in LOOT_TABLE, but the matching female helm sprites — though present in `sprites/preview_assets/char/` and passing QA — were never registered, so female warriors can't complete the L25 sets. Verified: all 3 PASS hat QA (`--y-min 2`), 42/42 active frames match male, presence-mismatch 0. Staged in `_fem_rare_helmet_preview/`. Preview: `PREVIEW_female_rare_helmets.png`. **On approval (no new sprite copy needed — files already in char/):** add 3 LOOT_TABLE entries mirroring the male `helmet_rare1/2/3` block but gender:'f', file `..._f.png`: helmet_rare1_f "Crimson Sentinel Helm", helmet_rare2_f "Shadow Warden Helm", helmet_rare3_f "Solar Paladin Helm" (slot:'helmet', level:25, rarity:'legendary', classes:['warrior']).
- **Female colored starter skirts** (2026-07-23): Blue/Green/Orange/Purple skirts — the pants-slot color gap (males had 5 colored starter pants in `clothing/male/*_Pants.png`; females had only the single `clothing/female/Skirt.png`). Generated by `scripts/gen_female_skirts.py` as a **pure palette swap** of the approved Skirt.png onto the exact male colored-pants ramps (per-color 4-shade + darkened deep-shadow; outline kept black). Geometry identical to source (10196 opaque px, matching shape distribution) so all frames/animation preserved by construction; all 4 QA PASS (`--y-max 63`). Staged in `_fem_skirt_preview/`. Preview: `PREVIEW_female_skirts.png`. On approval: copy the 4 PNGs to `sprites/preview_assets/clothing/female/` (as `Blue_Skirt.png` etc.), and add LOOT_TABLE `f` pants entries mirroring the male `m_pants_*` block (gender:'f', slot:'pants', skirt:true, level:1): f_skirt_blue "Azure Skirt", f_skirt_green "Forest Skirt", f_skirt_orange "Ember Skirt", f_skirt_purple "Shadow Skirt".
- **Female warrior tier boots** (2026-07-23): leather_boots_1_f + armor_boots_2–6_f — the last missing female-warrior slot (chest/pants/helmets already had 6-tier progressions; boots existed only as the 3 rare sabatons). Generated via `scripts/gen_female_warrior_boots.py`, which reuses the proven `gen_female_leggings.gen_frame` run-mapping (male boot runs → female foot silhouette, ground-aligned, per-frame) and a boot-safe repair (gap-fill + hole-fill only; no downward cuff extension). All 6 shaded + QA PASS (`--y-max 63`), per-frame parity verified 45/45 active frames vs male. Staged in `_fem_warrior_boots_preview/`. Preview: `PREVIEW_female_warrior_boots.png`. On approval: copy 6 sheets to `sprites/preview_assets/char/`, and add LOOT_TABLE `_f` boot entries (leather_boots_1_f L1, armor_boots_2_f L5, _3_f L10, _4_f L20, _5_f L30, _6_f L40; gender:'f', slot:'boots', classes:['warrior']).
- **Female hairstyles 5–6** (2026-07-23): style 5 **Bob** = hair_f21–25, style 6 **Pixie** = hair_f26–30. Derived subtractively from Short (hair_f1–5) via `scripts/gen_female_hair_5_6.py` (per-frame crown-relative clip; Bob=crown+8, Pixie=crown+6, side taper). All 5 colors, all 10 sheets QA PASS, per-frame animation verified intact. Staged in `_fem_hair_preview/`. On approval: copy to `sprites/preview_assets/char/`, and update index.html FEMALE_STYLE_NAMES to `[['1','Short'],['2','Long'],['3','Braid'],['4','Updo'],['5','Bob'],['6','Pixie']]`. Reaches male/female style parity (6 each).

- **Ranger legendary set — "Verdant Monarch" (L25)** (2026-07-23): first legendary loot for the ranger class — with this, all three classes (warrior/mage/ranger) have a legendary set. helmet/shirt/pants/boots `_rare_ranger1` + `_f` (8 sheets). Generated by `scripts/gen_ranger_legendary.py`: luminance-quantile color transfer (same QA-safe method as `gen_mage_legendary.py`) of the ranger t4 geometry onto a distinctive **Verdant Monarch** ramp (living emerald → radiant chartreuse-gold), clearly distinct from the ranger tiers' muted/darkening green family. Silhouette edges forced to black outline; opacity/geometry identical to source (verified equal opaque masks), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source, 70/70 frames identical (helmet 42 active, shirt/pants/boots 45 active). Staged in `_ranger_legendary_preview/`. Preview: `PREVIEW_ranger_legendary.png`. **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `classes:['ranger']`, `level:25`, `rarity:'legendary'`: `helmet_rare_ranger1` "Verdant Monarch Hood", `shirt_rare_ranger1` "Verdant Monarch Cloak", `pants_rare_ranger1` "Verdant Monarch Leggings", `boots_rare_ranger1` "Verdant Monarch Boots" — one `gender:'m'` (file `..._rare_ranger1.png`) and one `gender:'f'` (file `..._rare_ranger1_f.png`) per slot. Next daily batches can extend with rare_mage2/3 and rare_ranger2/3.

- **Mage legendary set — "Astral Magus" (L25)** (2026-07-23): first legendary loot for a non-warrior class — legendary sets previously existed only for warrior. helmet/shirt/pants/boots `_rare_mage1` + `_f` (8 sheets). Generated by `scripts/gen_mage_legendary.py`: luminance-quantile color transfer (same QA-safe method as `gen_female_rare_armor.py`) of the mage t4 geometry onto a distinctive **Astral** ramp (cosmic cyan → starlight ivory), clearly distinct from the mage tiers' purple family. Silhouette edges forced to black outline; opacity/geometry identical to source (verified equal opaque masks), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants/boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42/42, shirt/pants/boots 45/45). Staged in `_mage_legendary_preview/`. Preview: `PREVIEW_mage_legendary.png`. **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `classes:['mage']`, `level:25`, `rarity:'legendary'`: `helmet_rare_mage1` "Astral Magus Hat", `shirt_rare_mage1` "Astral Magus Robe", `pants_rare_mage1` "Astral Magus Leggings", `boots_rare_mage1` "Astral Magus Boots" — one `gender:'m'` (file `..._rare_mage1.png`) and one `gender:'f'` (file `..._rare_mage1_f.png`) per slot. Next daily batches can extend with rare_mage2/3 and ranger legendaries.

- **Mage 2nd legendary set — "Ember Magus" (L25)** (2026-07-23): second mage legendary (mage rare1 = Astral Magus). helmet/shirt/pants/boots `_rare_mage2` + `_f` (8 sheets). Generated by `scripts/gen_mage_legendary2.py`: same QA-safe luminance-quantile color transfer as `gen_mage_legendary.py` of the mage t4 geometry onto a distinctive **Ember** ramp (deep ember → molten orange → pale gold-white), clearly distinct from the mage tiers' purple/void family AND from the cyan Astral rare1 set. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_mage_legendary2_preview/`. Preview: `PREVIEW_legendary2.png` (top two rows). **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage2`, `classes:['mage']`, `level:25`, `rarity:'legendary'`: `helmet_rare_mage2` "Ember Magus Hat", `shirt_rare_mage2` "Ember Magus Robe", `pants_rare_mage2` "Ember Magus Leggings", `boots_rare_mage2` "Ember Magus Boots" — one `gender:'m'` (file `..._rare_mage2.png`) and one `gender:'f'` (file `..._rare_mage2_f.png`) per slot.

- **Ranger 2nd legendary set — "Frosthunter" (L25)** (2026-07-23): second ranger legendary (ranger rare1 = Verdant Monarch). helmet/shirt/pants/boots `_rare_ranger2` + `_f` (8 sheets). Generated by `scripts/gen_ranger_legendary2.py`: same QA-safe method of the ranger t4 geometry onto a distinctive **Frosthunter** ramp (deep steel shadow → desaturated icy blue → white glint), clearly distinct from the ranger tiers' green family, from the gold Verdant rare1 set, and from the mage Astral set's saturated cyan (Frost is grey-blue). Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks), so all frames + animation preserved by construction. All 8 shaded + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_ranger_legendary2_preview/`. Preview: `PREVIEW_legendary2.png` (bottom two rows). **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger2`, `classes:['ranger']`, `level:25`, `rarity:'legendary'`: `helmet_rare_ranger2` "Frosthunter Hood", `shirt_rare_ranger2` "Frosthunter Cloak", `pants_rare_ranger2` "Frosthunter Leggings", `boots_rare_ranger2` "Frosthunter Boots" — one `gender:'m'` (file `..._rare_ranger2.png`) and one `gender:'f'` (file `..._rare_ranger2_f.png`) per slot. Next daily batches can extend with rare_mage3 / rare_ranger3.

- **Mage 3rd legendary set — "Bloodmoon Magus" (L25)** (2026-07-23): third mage legendary (rare1 = Astral cyan, rare2 = Ember orange). helmet/shirt/pants/boots `_rare_mage3` + `_f` (8 sheets). Generated by `scripts/gen_mage_legendary3.py`: same QA-safe luminance-quantile color transfer of the mage t4 geometry onto a distinctive **Bloodmoon** ramp (deep blood shadow → crimson/scarlet → pale rose-white), deliberately kept pure red with no orange so it is distinct from the mage tiers' purple/void family, the cyan Astral rare1 set AND the orange-dominant Ember rare2 set. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_mage_legendary3_preview/`. Preview: `PREVIEW_legendary3.png` (top two rows). **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage3`, `classes:['mage']`, `level:25`, `rarity:'legendary'`: `helmet_rare_mage3` "Bloodmoon Magus Hat", `shirt_rare_mage3` "Bloodmoon Magus Robe", `pants_rare_mage3` "Bloodmoon Magus Leggings", `boots_rare_mage3` "Bloodmoon Magus Boots" — one `gender:'m'` (file `..._rare_mage3.png`) and one `gender:'f'` (file `..._rare_mage3_f.png`) per slot. This gives mage 3 legendary sets, matching warrior's 3.

- **Ranger 3rd legendary set — "Tideglass" (L25)** (2026-07-23): third ranger legendary (rare1 = Verdant gold, rare2 = Frosthunter steel-blue). helmet/shirt/pants/boots `_rare_ranger3` + `_f` (8 sheets). Generated by `scripts/gen_ranger_legendary3.py`: same QA-safe method of the ranger t4 geometry onto a distinctive **Tideglass** ramp (deep teal shadow → saturated aqua → pale seafoam → near-white glint), a saturated blue-green distinct from the ranger tiers' dark green family, the emerald-gold Verdant rare1 set AND the desaturated steel-blue Frosthunter rare2 set. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_ranger_legendary3_preview/`. Preview: `PREVIEW_legendary3.png` (bottom two rows). **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger3`, `classes:['ranger']`, `level:25`, `rarity:'legendary'`: `helmet_rare_ranger3` "Tideglass Hood", `shirt_rare_ranger3` "Tideglass Cloak", `pants_rare_ranger3` "Tideglass Leggings", `boots_rare_ranger3` "Tideglass Boots" — one `gender:'m'` (file `..._rare_ranger3.png`) and one `gender:'f'` (file `..._rare_ranger3_f.png`) per slot. All three classes now have 3 legendary sets each (warrior rare1/2/3, mage Astral/Ember/Bloodmoon, ranger Verdant/Frosthunter/Tideglass).

- **Mage 4th legendary set — "Malachite Magus" (L25)** (2026-07-23): fourth mage legendary (rare1 = Astral cyan, rare2 = Ember orange, rare3 = Bloodmoon red). helmet/shirt/pants/boots `_rare_mage4` + `_f` (8 sheets). Generated by `scripts/gen_mage_legendary4.py`: same QA-safe luminance-quantile color transfer of the mage t4 geometry onto a distinctive **Malachite** ramp (deep forest shadow → jade → bright verdant → pale mint glint), a saturated green — mage has no green anywhere else (tiers are purple/void), so it is distinct from the tiers AND all three prior mage legendaries. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_mage_legendary4_preview/`. Preview: `PREVIEW_legendary4.png` (top two rows). **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage4`, `classes:['mage']`, `level:25`, `rarity:'legendary'`: `helmet_rare_mage4` "Malachite Magus Hat", `shirt_rare_mage4` "Malachite Magus Robe", `pants_rare_mage4` "Malachite Magus Leggings", `boots_rare_mage4` "Malachite Magus Boots" — one `gender:'m'` (file `..._rare_mage4.png`) and one `gender:'f'` (file `..._rare_mage4_f.png`) per slot. Gives mage 4 legendary sets.

- **Ranger 4th legendary set — "Nightbloom" (L25)** (2026-07-23): fourth ranger legendary (rare1 = Verdant gold, rare2 = Frosthunter steel-blue, rare3 = Tideglass teal). helmet/shirt/pants/boots `_rare_ranger4` + `_f` (8 sheets). Generated by `scripts/gen_ranger_legendary4.py`: same QA-safe luminance-quantile color transfer of the ranger t4 geometry onto a distinctive **Nightbloom** ramp (deep violet shadow → royal purple → magenta → pale lilac glint), a saturated violet-magenta — ranger has no purple anywhere else (tiers are dark green), so it is distinct from the tiers AND all three prior ranger legendaries. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_ranger_legendary4_preview/`. Preview: `PREVIEW_legendary4.png` (bottom two rows). **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger4`, `classes:['ranger']`, `level:25`, `rarity:'legendary'`: `helmet_rare_ranger4` "Nightbloom Hood", `shirt_rare_ranger4` "Nightbloom Cloak", `pants_rare_ranger4` "Nightbloom Leggings", `boots_rare_ranger4` "Nightbloom Boots" — one `gender:'m'` (file `..._rare_ranger4.png`) and one `gender:'f'` (file `..._rare_ranger4_f.png`) per slot. Mage and ranger now have 4 legendary sets each.

- **Warrior 4th legendary set — "Amethyst Warlord" (L25)** (2026-07-24): fourth warrior legendary, bringing warrior to parity with mage and ranger (which each had 4 while warrior had only 3: rare1 = Crimson Sentinel red+gold, rare2 = Shadow Warden black+teal, rare3 = Solar Paladin gold+ivory). helmet/shirt/pants/boots `_rare4` + `_f` (8 sheets). Generated by `scripts/gen_warrior_legendary4.py`: same QA-safe luminance-quantile color transfer as the mage/ranger legendary generators, but sourced from the warrior **rare1** geometry (chosen because rare1 already ships full male+female coverage for all four slots, so the new set inherits complete gender parity). Ramp is a distinctive royal **Amethyst** family (deep violet shadow → royal purple → bright amethyst → pale lilac glint) — warrior has no purple anywhere in its tiers (leather/steel/gold/icy-diamond), so it reads clearly as its own fourth legendary and is distinct from the icy-blue t6 Diamond Plate AND all three prior warrior legendaries. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_warrior_legendary4_preview/`. Preview: `_PREVIEW_warrior_legendary4.png`. **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `_rare4`, `classes:['warrior']`, `level:25`, `rarity:'legendary'`: `helmet_rare4` "Amethyst Warlord Helm", `shirt_rare4` "Amethyst Warlord Cuirass", `pants_rare4` "Amethyst Warlord Greaves", `boots_rare4` "Amethyst Warlord Sabatons" — one `gender:'m'` (file `..._rare4.png`) and one `gender:'f'` (file `..._rare4_f.png`) per slot. All three classes then have 4 legendary sets each.

- **Warrior 5th legendary set — "Emerald Vanguard" (L25)** (2026-07-24): fifth warrior legendary (rare1 = Crimson Sentinel red+gold, rare2 = Shadow Warden black+teal, rare3 = Solar Paladin gold+ivory, rare4 = Amethyst Warlord purple). helmet/shirt/pants/boots `_rare5` + `_f` (8 sheets). Generated by `scripts/gen_warrior_legendary5.py`: same QA-safe luminance-quantile color transfer as the prior legendary generators, sourced from the warrior **rare1** geometry (full male+female coverage → complete gender parity). Ramp is a saturated **Emerald** family (deep forest-emerald shadow → emerald → jade → pale mint glint) — warrior has NO green anywhere in its tiers (leather/studded/chainmail/silver/gold/icy-diamond) or in any prior legendary, and pure emerald is distinct from Shadow Warden's electric-teal accent. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_warrior_legendary5_preview/`. Preview: `_PREVIEW_warrior_legendary5.png`. **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `_rare5`, `classes:['warrior']`, `level:25`, `rarity:'legendary'`: `helmet_rare5` "Emerald Vanguard Helm", `shirt_rare5` "Emerald Vanguard Cuirass", `pants_rare5` "Emerald Vanguard Greaves", `boots_rare5` "Emerald Vanguard Sabatons" — one `gender:'m'` (file `..._rare5.png`) and one `gender:'f'` (file `..._rare5_f.png`) per slot.

- **Mage 5th legendary set — "Rosethorn Magus" (L25)** (2026-07-24): fifth mage legendary (rare1 = Astral cyan, rare2 = Ember orange, rare3 = Bloodmoon red, rare4 = Malachite green). helmet/shirt/pants/boots `_rare_mage5` + `_f` (8 sheets). Generated by `scripts/gen_mage_legendary5.py`: same QA-safe luminance-quantile color transfer of the mage t4 geometry onto a distinctive **Rosethorn** ramp (deep wine shadow → magenta → hot pink → pale blush glint), a saturated rose-magenta — distinct from mage's purple/void tiers (pink not violet), from Bloodmoon's pure red (strong magenta cast reads clearly pink), and from all other legendaries. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_mage_legendary5_preview/`. Preview: `_PREVIEW_mage_legendary5.png`. **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage5`, `classes:['mage']`, `level:25`, `rarity:'legendary'`: `helmet_rare_mage5` "Rosethorn Magus Hat", `shirt_rare_mage5` "Rosethorn Magus Robe", `pants_rare_mage5` "Rosethorn Magus Leggings", `boots_rare_mage5` "Rosethorn Magus Boots" — one `gender:'m'` (file `..._rare_mage5.png`) and one `gender:'f'` (file `..._rare_mage5_f.png`) per slot.

- **Ranger 5th legendary set — "Emberwild Warden" (L25)** (2026-07-24): fifth ranger legendary (rare1 = Verdant gold, rare2 = Frosthunter steel-blue, rare3 = Tideglass teal, rare4 = Nightbloom violet). helmet/shirt/pants/boots `_rare_ranger5` + `_f` (8 sheets). Generated by `scripts/gen_ranger_legendary5.py`: same QA-safe luminance-quantile color transfer of the ranger t4 geometry onto a distinctive **Emberwild** ramp (deep umber shadow → burnt sienna → copper-orange → amber → pale gold glint), a warm autumn amber-copper — ranger has no warm orange/amber anywhere (tiers are dark green), so it is distinct from the tiers, from Verdant's green-dominant gold, and from all other legendaries. Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0), so all frames + animation preserved by construction. All 8 shaded + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); per-frame parity 0 mismatch vs source (helmet 42 active, shirt/pants/boots 45 active). Staged in `_ranger_legendary5_preview/`. Preview: `_PREVIEW_ranger_legendary5.png`. **On approval:** copy the 8 PNGs to `sprites/preview_assets/char/`, and add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger5`, `classes:['ranger']`, `level:25`, `rarity:'legendary'`: `helmet_rare_ranger5` "Emberwild Warden Hood", `shirt_rare_ranger5` "Emberwild Warden Cloak", `pants_rare_ranger5` "Emberwild Warden Leggings", `boots_rare_ranger5` "Emberwild Warden Boots" — one `gender:'m'` (file `..._rare_ranger5.png`) and one `gender:'f'` (file `..._rare_ranger5_f.png`) per slot. All three classes then have 5 legendary sets each.

- **6th legendary sets — all classes (L25)** (2026-07-24): a distinct sixth legendary per class, bringing warrior/mage/ranger to 6 legendary sets each. Generated by `scripts/gen_warrior_legendary6.py`, `scripts/gen_mage_legendary6.py`, `scripts/gen_ranger_legendary6.py` — same QA-safe luminance-quantile color transfer as prior legendary generators (warrior sourced from rare1 geometry for full male+female coverage; mage/ranger from their t4 geometry). Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0 across all 8 sheets per set), so all frames + animation preserved by construction. All 24 sheets shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`). Preview: `_PREVIEW_legendary6.png`. Ramps chosen distinct from each class's tiers AND all five prior legendaries:
  - **Warrior — "Rose Quartz Sovereign"** `_rare6` + `_f`: soft salmon-rose (deep wine-rose → rose → salmon pink → pale blush). Warrior has no pink anywhere; kept warm/pink (not magenta) so distinct from pure-red Crimson Sentinel. Staged in `_warrior_legendary6_preview/`. **On approval:** copy 8 PNGs to `sprites/preview_assets/char/`, add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `_rare6`, `classes:['warrior']`, `level:25`, `rarity:'legendary'`: `helmet_rare6` "Rose Quartz Helm", `shirt_rare6` "Rose Quartz Cuirass", `pants_rare6` "Rose Quartz Greaves", `boots_rare6` "Rose Quartz Sabatons" — one `gender:'m'` (`..._rare6.png`) and one `gender:'f'` (`..._rare6_f.png`) per slot.
  - **Mage — "Mithril Magus"** `_rare_mage6` + `_f`: cool mithril/platinum (deep steel-blue → slate → silver → platinum → white glint). Mage has no cool silver-white set (prior are cyan/orange/red/green/rose-magenta; tiers purple/void). Staged in `_mage_legendary6_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage6`, `classes:['mage']`, L25 legendary: `helmet_rare_mage6` "Mithril Magus Hat", `shirt_rare_mage6` "Mithril Magus Robe", `pants_rare_mage6` "Mithril Magus Leggings", `boots_rare_mage6` "Mithril Magus Boots" — m (`..._rare_mage6.png`) + f (`..._rare_mage6_f.png`) per slot.
  - **Ranger — "Crimson Warden"** `_rare_ranger6` + `_f`: pure ruby/crimson (deep maroon → blood red → crimson → scarlet → pale rose). Ranger has no red anywhere (tiers dark green); kept pure red with no orange so distinct from warm-orange Emberwild. Staged in `_ranger_legendary6_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger6`, `classes:['ranger']`, L25 legendary: `helmet_rare_ranger6` "Crimson Warden Hood", `shirt_rare_ranger6` "Crimson Warden Cloak", `pants_rare_ranger6` "Crimson Warden Leggings", `boots_rare_ranger6` "Crimson Warden Boots" — m (`..._rare_ranger6.png`) + f (`..._rare_ranger6_f.png`) per slot.

- **7th legendary sets — all classes (L25)** (2026-07-24): a distinct seventh legendary per class, bringing warrior/mage/ranger to 7 legendary sets each. Generated by `scripts/gen_legendary7_all.py` — same QA-safe luminance-quantile color transfer as prior legendary generators (warrior sourced from rare1 geometry for full male+female coverage; mage/ranger from their t4 geometry). Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0 across all 8 sheets per set, total 0/24), so all frames + animation preserved by construction. All 24 sheets shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`). Preview: `_PREVIEW_legendary7.png`. Ramps chosen distinct from each class's tiers AND all six prior legendaries:
  - **Warrior — "Azure Sovereign"** `_rare7` + `_f`: royal sapphire (deep navy → cobalt → royal blue → azure → pale sky). Warrior's only blue is the PALE icy-diamond t6; a saturated deep sapphire reads clearly as its own set and is distinct from all other warrior legendaries (red/teal/gold/purple/green/rose). Staged in `_warrior_legendary7_preview/`. **On approval:** copy 8 PNGs to `sprites/preview_assets/char/`, add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `_rare7`, `classes:['warrior']`, `level:25`, `rarity:'legendary'`: `helmet_rare7` "Azure Sovereign Helm", `shirt_rare7` "Azure Sovereign Cuirass", `pants_rare7` "Azure Sovereign Greaves", `boots_rare7` "Azure Sovereign Sabatons" — one `gender:'m'` (`..._rare7.png`) and one `gender:'f'` (`..._rare7_f.png`) per slot.
  - **Mage — "Gilded Magus"** `_rare_mage7` + `_f`: pure warm gold (deep bronze-brown → antique gold → amber-gold → bright gold → pale gold-white). Mage has NO yellow-gold set anywhere (prior are cyan/orange/red/green/rose-magenta/silver; tiers purple/void); kept yellow-gold, not the red-orange of Ember rare2. Staged in `_mage_legendary7_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage7`, `classes:['mage']`, L25 legendary: `helmet_rare_mage7` "Gilded Magus Hat", `shirt_rare_mage7` "Gilded Magus Robe", `pants_rare_mage7` "Gilded Magus Leggings", `boots_rare_mage7` "Gilded Magus Boots" — m (`..._rare_mage7.png`) + f (`..._rare_mage7_f.png`) per slot.
  - **Ranger — "Moonsilver Warden"** `_rare_ranger7` + `_f`: neutral silver/platinum (deep slate → grey → silver → platinum → white). Ranger has no neutral silver; kept zero blue cast so it is distinct from the steel-BLUE Frosthunter rare2 AND all other ranger legendaries (green/teal/violet/amber/red). Staged in `_ranger_legendary7_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger7`, `classes:['ranger']`, L25 legendary: `helmet_rare_ranger7` "Moonsilver Warden Hood", `shirt_rare_ranger7` "Moonsilver Warden Cloak", `pants_rare_ranger7` "Moonsilver Warden Leggings", `boots_rare_ranger7` "Moonsilver Warden Boots" — m (`..._rare_ranger7.png`) + f (`..._rare_ranger7_f.png`) per slot. All three classes then have 7 legendary sets each.

- **8th legendary sets — all classes (L25)** (2026-07-25): a distinct eighth legendary per class, bringing warrior/mage/ranger to 8 legendary sets each. Generated by `scripts/gen_legendary8_all.py` — same QA-safe luminance-quantile color transfer as prior legendary generators (warrior sourced from rare1 geometry for full male+female coverage; mage/ranger from their t4 geometry). Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch 0 AND opaque-px-diff 0 across all 24 sheets, total 0/24), so all frames + animation preserved by construction. All 24 sheets shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`). Preview: `_PREVIEW_legendary8.png`. Ramps chosen distinct from each class's tiers AND all seven prior legendaries:
  - **Warrior — "Molten Sovereign"** `_rare8` + `_f`: copper-orange (deep umber → burnt sienna → copper → burnt orange → bright amber → pale gold glint). Warrior has NO orange/copper anywhere (tiers leather-brown/steel/gold/icy-diamond; prior legendaries red/teal/gold/purple/green/rose/sapphire); kept strongly orange so distinct from the yellow-gold Solar Paladin rare3. Staged in `_warrior_legendary8_preview/`. **On approval:** copy 8 PNGs to `sprites/preview_assets/char/`, add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `_rare8`, `classes:['warrior']`, `level:25`, `rarity:'legendary'`: `helmet_rare8` "Molten Sovereign Helm", `shirt_rare8` "Molten Sovereign Cuirass", `pants_rare8` "Molten Sovereign Greaves", `boots_rare8` "Molten Sovereign Sabatons" — one `gender:'m'` (`..._rare8.png`) and one `gender:'f'` (`..._rare8_f.png`) per slot.
  - **Mage — "Sapphire Magus"** `_rare_mage8` + `_f`: deep royal sapphire (deep navy → cobalt → royal blue → azure → pale sky). Mage's only blue-ish set is the saturated CYAN Astral rare1; deep royal sapphire reads clearly as its own set (tiers purple/void). Staged in `_mage_legendary8_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage8`, `classes:['mage']`, L25 legendary: `helmet_rare_mage8` "Sapphire Magus Hat", `shirt_rare_mage8` "Sapphire Magus Robe", `pants_rare_mage8` "Sapphire Magus Leggings", `boots_rare_mage8` "Sapphire Magus Boots" — m (`..._rare_mage8.png`) + f (`..._rare_mage8_f.png`) per slot.
  - **Ranger — "Rosewild Warden"** `_rare_ranger8` + `_f`: rose-pink (deep wine → dark rose → rose → hot pink → pale blush). Ranger has NO pink anywhere (tiers dark green; prior legendaries green/teal/steel-blue/violet/amber/red/silver); kept warm pink (strong magenta cast) so distinct from the pure-red Crimson rare6 and violet Nightbloom rare4. Staged in `_ranger_legendary8_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger8`, `classes:['ranger']`, L25 legendary: `helmet_rare_ranger8` "Rosewild Warden Hood", `shirt_rare_ranger8` "Rosewild Warden Cloak", `pants_rare_ranger8` "Rosewild Warden Leggings", `boots_rare_ranger8` "Rosewild Warden Boots" — m (`..._rare_ranger8.png`) + f (`..._rare_ranger8_f.png`) per slot. All three classes then have 8 legendary sets each.

- **9th legendary sets — all classes (L25)** (2026-07-25): a distinct ninth legendary per class, bringing warrior/mage/ranger to 9 legendary sets each. Generated by `scripts/gen_legendary9_all.py` — same QA-safe luminance-quantile color transfer as prior legendary generators (warrior sourced from rare1 geometry for full male+female coverage; mage/ranger from their t4 geometry). Silhouette edges forced to black; opacity/geometry identical to source (verified equal opaque masks + per-frame presence-mismatch **0/24** across all 24 sheets), so all frames + animation preserved by construction. All 24 sheets shaded (`sprite_shade.py`) + QA PASS (helmets `--y-min 2`, pants m `--y-max 62` / f `--y-max 63`, boots `--y-max 63`); active-frame counts correct (helmet 42, shirt/pants/boots 45). Preview: `_PREVIEW_legendary9.png`. Note: eight prior sets have used the easy hues, so #9 reaches for the clearest remaining per-class gaps — distinctness is now getting tight, worth flagging for future batches. Ramps:
  - **Warrior — "Tidewarden Sovereign"** `_rare9` + `_f`: teal/turquoise (deep teal → turquoise → aqua → pale mint). Warrior has NO full teal body — the only teal in its legendaries is a thin ACCENT on the near-black Shadow Warden rare2; distinct from green Emerald rare5 (no blue) and blue Azure rare7 (no green). Staged in `_warrior_legendary9_preview/`. **On approval:** copy 8 PNGs to `sprites/preview_assets/char/`, add 8 LOOT_TABLE entries mirroring the warrior `helmet_rare1` block but `_rare9`, `classes:['warrior']`, `level:25`, `rarity:'legendary'`: `helmet_rare9` "Tidewarden Helm", `shirt_rare9` "Tidewarden Cuirass", `pants_rare9` "Tidewarden Greaves", `boots_rare9` "Tidewarden Sabatons" — one `gender:'m'` (`..._rare9.png`) and one `gender:'f'` (`..._rare9_f.png`) per slot.
  - **Mage — "Celestial Magus"** `_rare_mage9` + `_f`: radiant opal/pearl-white (deep slate-lilac → soft lavender-grey → warm ivory → pure white glint). Mage has no white/pearl set (prior are cyan/orange/red/green/rose-magenta/silver/gold/sapphire; tiers purple/void); kept warm-ivory-white (not the cool STEEL-blue of Mithril rare6) so it reads as luminous pearl. Staged in `_mage_legendary9_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the mage rare1 block but `_rare_mage9`, `classes:['mage']`, L25 legendary: `helmet_rare_mage9` "Celestial Magus Hat", `shirt_rare_mage9` "Celestial Magus Robe", `pants_rare_mage9` "Celestial Magus Leggings", `boots_rare_mage9` "Celestial Magus Boots" — m (`..._rare_mage9.png`) + f (`..._rare_mage9_f.png`) per slot.
  - **Ranger — "Sunspear Warden"** `_rare_ranger9` + `_f`: pure warm gold/yellow (deep bronze-brown → antique gold → amber-gold → bright yellow-gold → pale gold-white). Ranger has no yellow-gold set (tiers dark green; prior legendaries green/steel-blue/teal/violet/copper-amber/red/silver/pink); kept a clean YELLOW-gold, distinct from the copper-ORANGE Emberwild rare5 and neutral-silver Moonsilver rare7. Staged in `_ranger_legendary9_preview/`. **On approval:** copy 8 PNGs to char/, add 8 LOOT_TABLE entries mirroring the ranger rare1 block but `_rare_ranger9`, `classes:['ranger']`, L25 legendary: `helmet_rare_ranger9` "Sunspear Warden Hood", `shirt_rare_ranger9` "Sunspear Warden Cloak", `pants_rare_ranger9` "Sunspear Warden Leggings", `boots_rare_ranger9` "Sunspear Warden Boots" — m (`..._rare_ranger9.png`) + f (`..._rare_ranger9_f.png`) per slot. All three classes then have 9 legendary sets each.

## Recently completed
- **Female class hats t2–6** (2026-07-23): helmet_mage2–6_f + helmet_ranger2–6_f generated via `scripts/gen_female_class_hats.py`, all PASS shade+QA. Closed the gap where female mage/ranger had no headgear past level 1. LOOT_TABLE `_f` entries added. Staged in working tree; deploy pending.

---

## Key Workflow Rules

1. **Always update CONTEXT.md before every git push**
2. **Always show preview to user (via Dispatch) BEFORE pushing to GitHub**
3. Generate previews with Python/Pillow writing to `/sessions/<sandbox>/mnt/outputs/`
4. Clone fresh each session (into a writable path like `/sessions/<sandbox>/repo/`):
   ```bash
   mkdir -p /sessions/<sandbox>/repo
   cd /sessions/<sandbox>/repo
   git clone https://mchauth:TOKEN@github.com/mchauth/TaskQuest-HTML.git tq
   cd tq && git config user.email "mchauth@gmail.com" && git config user.name "Matt Hauth"
   ```

---

## Sprite Generation Technique

- **Source**: Manipulate existing sprite sheets frame-by-frame using Python/Pillow
- **Do NOT use PixelLab API** — quality issues at 80×64 (generates full characters, not just hair)
- **Hair isolation**: diff each hair frame against skin.png frame — any non-transparent pixel that differs from skin by >15 RGB units is a hair pixel
- **Palette mapping**: sample colors from hair_m1–5 and remap per color variant
- **Preview**: composite hair frame 0 over skin.png frame 0, scale 4×, grid of all styles/colors

### Man-Bun approach (hair_m26–30) — hand-painted
The man-bun was hand-painted pixel-by-pixel using Python/Pillow. Key pixel map (frame 0, all frames identical):

**Palette:**
- MAIN    = (89, 59, 31)   — base hair brown
- MID     = (64, 45, 32)   — mid shadow
- DARK    = (44, 34, 29)   — dark shadow / diagonal lines
- DARKEST = (19, 19, 28)   — outline / seam / left edge

**Head hair (flat strip on top):**
- y=21: x=37–43 DARK (hairline), x=35 DARKEST (left edge)
- y=22: x=37–43 MAIN, x=35 DARK
- y=23: x=37–43 MAIN
- x=44 col at y=22–25: DARKEST (seam separating head from bun)

**Diagonal lines (upper-right to lower-left, showing pull):**
- Line 1: (21,42)→(22,41)→(23,40) DARKEST/DARK
- Line 2: (21,40)→(22,39)→(23,38) DARKEST/DARK
- Line 3: (24,42)→(25,41)→(26,40) DARK (lower pull continuation)

**Additional hair mass at pull point:**
- y=24: x=42–43 MAIN; y=25: x=43 DARK

**Small round bun (right side, x=44–48):**
- y=23: x=44–47 (top, 4px)
- y=24: x=44–48 (5px)
- y=25: x=44–48 (5px)
- y=26: x=45–47 (bottom, 3px)
- Bun diagonal shade: (23,47)→(24,46)→(25,45) DARK
- Right edge dark: (24,48),(25,48) DARK

**Constraints (do not violate):**
- Tip of hair no higher than y=23
- Bun starts at x=44–47
- All hair to the right of x=35; nothing above y=21

### Slicked Back approach (hair_m21–25)
1. Start from short hair (hair_m1–5), process each of 70 frames independently
2. Isolate hair pixels (diff against skin.png — non-skin, non-transparent pixels)
3. Find bounding box (min_x, max_x, min_y, max_y) of hair pixels
4. Mirror horizontally within bounding box: place pixel at (x, y) → (min_x + max_x - x, y)
5. Apply 70% vertical compression: `y_new = min_y + int((y - min_y) * 0.70)`

---

## Known Issues / History

- **Bang removal approach** (previous): explicitly removing front pixels works but leaves an unnatural cutoff. The horizontal flip approach is more organic.
- **Bleedthrough fix** (zeroing pixels matching short hair base) makes crown look bald — avoid
- **PixelLab inpaint at 80×64** generates full characters, not just hair — don't use
- **Stamping frame 0 across all frames** breaks animation — always process per-frame
- **Old /tmp/tq clone** owned by `nobody` — always clone into `/sessions/<sandbox>/repo/` instead
