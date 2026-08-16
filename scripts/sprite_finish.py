#!/usr/bin/env python3
"""sprite_finish.py — THE canonical finishing pass for every armor sheet.

Everything Matt approved on 8/1 (no-smooth shading, sculptural chest plates,
helmet visors, class-hat folds) lives behind ONE call so that:

  * every design already generated can be backfilled in bulk, and
  * every future generator gets the same treatment by adding one line,
    instead of each gen_*.py re-implementing its own shading.

FOR FUTURE GENERATORS — replace the per-script `shade(...)` call with:

    from sprite_finish import finish_array
    arr = finish_array(arr, dst)        # dst = the filename you're about to save
    Image.fromarray(arr).save(dst)

`dst` is passed because the variant (chest separation, helmet visor) is chosen
from a hash of the filename, so a sheet always regenerates identically.

Chain, by slot (slot is read from the filename):

  all slots   sprite_shade.shade_sheet(smooth=False)
                --no-smooth ALWAYS: the diffusion pre-pass blurs authored
                pattern geometry, which is the whole point of the axis sheets.
  shirt       add_chest_plates.plate_sheet(variant)   pauldrons, sheen,
                gorget, sternum/band separation
  helmet      black eye/mouth pixels (one of the five VISOR_VARIANTS) plus
                local brow/cheek shading. NO full-silhouette rim — that is
                what mangled coloured/patterned domes.
              coverage < HELM_MIN_PX -> not a helm at all but open headgear
                (hat/hood/circlet); shade_class_hats applies brim/crease folds
                instead. A coverage test rather than a filename list, so new
                hats need no maintenance — and a THRESHOLD rather than "== 0",
                because the low-brimmed female wizard hat clips the eye row by
                a couple of dozen pixels and would otherwise get a visor cut
                into its brim.
  pants/boots shading only

Idempotency: finished files are stamped with a PNG text chunk
(TaskQuestFinish=VERSION). `finish_file` skips an already-stamped sheet unless
--force, so a bulk backfill can be re-run safely and cannot double-apply
shading. Bump VERSION when the chain changes to make the next run re-finish.
"""
import os
import sys
import argparse
import numpy as np
from PIL import Image, PngImagePlugin

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS)

import sprite_shade                      # noqa: E402
import add_chest_plates                  # noqa: E402
import carve_face_openings               # noqa: E402
import shade_class_hats                  # noqa: E402

VERSION = "2026-08-01.6"
STAMP_KEY = "TaskQuestFinish"
HELM_MIN_PX = 120        # below this a helmet sheet counts as open headgear

# SCOPE (Matt 8/1, final): this pass runs ONLY on sheets produced by the sprite
# creation task — the staged _*_preview/ dirs. Nothing already deployed in the
# app (sprites/preview_assets/char/) is ever written to.
#
# A "visor" is just the BLACK eye/mouth pixels plus their local brow/cheek
# shading, and that stamps cleanly onto any blank-dome helmet regardless of its
# colour or pattern. The full-silhouette dark RIM is a separate thing and is
# now off — darkening the whole boundary is what swamped the coloured and
# patterned domes. No allowlist is needed once the rim is gone.


def slot_of(name):
    n = os.path.basename(name).lower()
    if n.startswith('shirt') or 'chest' in n:
        return 'shirt'
    if n.startswith('helmet') or 'helm' in n or 'hat' in n:
        return 'helmet'
    if n.startswith('pants') or 'legging' in n or 'skirt' in n:
        return 'pants'
    if n.startswith('boots') or n.startswith('armor_boots'):
        return 'boots'
    return 'other'


def finish_array(arr, name, profile=None):
    """Apply the full finishing chain in memory. Returns (arr, info dict)."""
    slot = slot_of(name)
    gender = 'f' if os.path.basename(name)[:-4].endswith('_f') else 'm'
    info = {'slot': slot, 'variant': None}

    # protect=False: this only ever runs on standalone ARMOR sheets, which
    # contain no real skin or hair — see sprite_shade.classify()
    arr, _ = sprite_shade.shade_sheet(arr, smooth=False, protect=False)

    if slot == 'shirt':
        prof = profile or add_chest_plates.PROFILES['medium']
        vname, sep = add_chest_plates.variant_for(name)
        n = add_chest_plates.plate_sheet(arr, prof, sep)
        info['variant'] = vname if n >= 0 else 'skipped-wide-geometry'

    elif slot == 'helmet':
        # Every generated dome gets a visor: black eye/mouth pixels plus their
        # local brow/cheek shading. rim=False — the full-silhouette darkening
        # is what mangled coloured and patterned domes, and it is not part of
        # what a visor is.
        vname, var = carve_face_openings.variant_for(name)
        carved, n = carve_face_openings.carve(arr, gender, var=var,
                                              relief=True, rim=False)
        if n >= HELM_MIN_PX:
            arr = carved
            info['variant'] = vname
        else:
            # Open headgear (hat / hood / circlet) — fold-shade instead.
            # The test is a THRESHOLD, not n == 0: the low-brimmed female
            # wizard hat clips the eye row by a couple of dozen pixels total
            # and would otherwise get a visor slit cut into its brim. A real
            # closed helm carves 200-400 px.
            shade_class_hats.shade_sheet(arr)
            info['variant'] = 'hat-folds'

    return arr, info


def is_finished(path):
    try:
        return Image.open(path).info.get(STAMP_KEY) == VERSION
    except Exception:
        return False


def save_finished(arr, path):
    """Write a sheet that has ALREADY been through finish_array(), carrying the version stamp.

    Generators that call finish_array() in-line must save through this rather than a bare
    Image.fromarray(arr).save(path). Without the stamp the sheet looks unfinished to
    is_finished(), so a later bulk `python3 scripts/sprite_finish.py <dir>` backfill would run
    the whole chain over it a SECOND time — double shading, double plates. The stamp is the only
    thing that makes the finishing pass idempotent, and it lives on the file, not in the array."""
    meta = PngImagePlugin.PngInfo()
    meta.add_text(STAMP_KEY, VERSION)
    Image.fromarray(arr).save(path, pnginfo=meta)


def finish_file(path, force=False):
    if not force and is_finished(path):
        return None
    img = Image.open(path).convert('RGBA')
    if img.size != (800, 448):
        return None
    arr, info = finish_array(np.array(img), path)
    save_finished(arr, path)
    return info


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('paths', nargs='+', help='PNG sheets or directories')
    ap.add_argument('--force', action='store_true',
                    help='re-finish sheets already stamped with this version')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            for root, _, names in os.walk(p):
                files += [os.path.join(root, n) for n in names
                          if n.endswith('.png')]
        else:
            files.append(p)

    counts = {}
    done = skipped = 0
    for f in sorted(files):
        if slot_of(f) == 'other':
            continue
        if args.dry_run:
            print(f"would finish {f}")
            continue
        info = finish_file(f, force=args.force)
        if info is None:
            skipped += 1
            continue
        done += 1
        k = f"{info['slot']}:{info['variant']}"
        counts[k] = counts.get(k, 0) + 1
    print(f"finished {done}, skipped {skipped} (already stamped / wrong size)")
    for k in sorted(counts):
        print(f"   {k}: {counts[k]}")


if __name__ == '__main__':
    main()
