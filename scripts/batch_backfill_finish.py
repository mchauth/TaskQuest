#!/usr/bin/env python3
"""batch_backfill_finish.py — Retroactively apply finish_array() to all pre-update preview dirs.

Excluded (already generated with current rules):
  _plated_chest_preview
  _arcade*_preview  (incl. _arcadedome_helmet_preview)
  _zigzag*_preview  (incl. _zigzagdome_helmet_preview)
  _gadroon*_preview (incl. _gadroondome_helmet_preview)
  _backup_*

Also never touches sprites/preview_assets/char/ (the live game assets).

Idempotency: sprite_finish.py stamps finished files with TaskQuestFinish=VERSION.
Already-stamped files are skipped automatically — safe to re-run.

After finishing, runs sprite_qa.py per slot:
  helmets  --y-min 2
  shirts   (defaults)
  pants    --y-max 63
  boots    --y-max 63
"""

import os
import sys
import subprocess
import fnmatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")

# Dirs explicitly excluded per Matt's instructions (already current or off-limits)
EXCLUDE_PATTERNS = [
    "_plated_chest_preview",
    "_arcade*_preview",
    "_arcadedome*",
    "_zigzag*_preview",
    "_zigzagdome*",
    "_gadroon*_preview",
    "_gadroondome*",
    "_backup_*",
]


def is_excluded(dirname):
    for pat in EXCLUDE_PATTERNS:
        if fnmatch.fnmatch(dirname, pat):
            return True
    return False


def slot_of(filename):
    """Mirror sprite_finish.slot_of() — determines QA flags per file."""
    n = os.path.basename(filename).lower()
    if n.startswith("shirt") or "chest" in n:
        return "shirt"
    if n.startswith("helmet") or "helm" in n or "hat" in n:
        return "helmet"
    if n.startswith("pants") or "legging" in n or "skirt" in n:
        return "pants"
    if n.startswith("boots") or n.startswith("armor_boots"):
        return "boots"
    return "other"


# ── 1. Collect target directories ──────────────────────────────────────────

preview_dirs = []
for entry in sorted(os.listdir(ROOT)):
    full = os.path.join(ROOT, entry)
    if (
        entry.startswith("_")
        and "preview" in entry
        and os.path.isdir(full)
        and not is_excluded(entry)
    ):
        preview_dirs.append(full)

print(f"Found {len(preview_dirs)} directories to finish")
print("Excluded patterns:", EXCLUDE_PATTERNS)
print()


# ── 2. Finishing pass ───────────────────────────────────────────────────────

# --force is mandatory: the VERSION was not bumped when the rules were updated,
# so all pre-update files are already stamped but were finished with the OLD
# implementation (no chest plate shading, no asymmetric pauldrons, no slit
# variants). Without --force, sprite_finish.py skips every file.
print("=== Step 1: Finishing pass (--force) ===")
cmd = [sys.executable, os.path.join(SCRIPTS, "sprite_finish.py"), "--force"] + preview_dirs
result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout.strip())
if result.stderr.strip():
    print("STDERR:", result.stderr.strip())
print()


# ── 3. QA per slot ─────────────────────────────────────────────────────────

print("=== Step 2: QA per slot ===")

# QA flags per slot type
QA_FLAGS = {
    "helmet": ["--y-min", "2"],
    "shirt": [],
    "pants": ["--y-max", "63"],
    "boots": ["--y-max", "63"],
}

# Collect PNGs by slot
by_slot = {"helmet": [], "shirt": [], "pants": [], "boots": []}
for d in preview_dirs:
    try:
        entries = sorted(os.listdir(d))
    except OSError:
        continue
    for f in entries:
        if not f.endswith(".png"):
            continue
        slot = slot_of(f)
        if slot in by_slot:
            by_slot[slot].append(os.path.join(d, f))

overall_pass = True
for slot, files in by_slot.items():
    if not files:
        print(f"  {slot}: 0 files — skipped")
        continue

    flags = QA_FLAGS[slot]
    print(f"\n--- {slot} ({len(files)} files, flags: {flags or 'defaults'}) ---")

    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "sprite_qa.py")] + flags + files,
        capture_output=True,
        text=True,
    )

    # Print only FAIL lines and the final summary banner
    fail_lines = []
    summary = ""
    for line in result.stdout.splitlines():
        if line.startswith("FAIL"):
            fail_lines.append(line)
        elif "═" in line or "QA RESULT" in line:
            summary = line

    if fail_lines:
        overall_pass = False
        print(f"  {len(fail_lines)} FAIL(s):")
        for fl in fail_lines:
            print(f"    {fl}")
    else:
        pass_count = sum(1 for ln in result.stdout.splitlines() if ln.startswith("PASS"))
        print(f"  All {pass_count} PASS")

    if summary:
        print(f"  {summary}")

    if result.returncode not in (0, 1):  # 0=all pass, 1=failures, anything else = crash
        print(f"  WARNING: QA exited with code {result.returncode}")
        if result.stderr.strip():
            print("  STDERR:", result.stderr.strip()[:500])

print()
print("═" * 60)
print(
    "BATCH COMPLETE: ALL PASS ✓"
    if overall_pass
    else "BATCH COMPLETE: FAILURES FOUND ✗ — see above"
)
print("═" * 60)
sys.exit(0 if overall_pass else 1)
