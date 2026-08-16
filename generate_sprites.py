#!/usr/bin/env python3
"""
TaskQuest Sprite Generator
Keeps a rolling pool of 3 concurrent PixelLab jobs (API limit).
Saves south-facing images to ~/Projects/TaskQuest/sprites/
"""

import requests
import time
import sys
from pathlib import Path
from collections import deque

# ── Config ──────────────────────────────────────────────────────────────────
API_BASE       = "https://api.pixellab.ai/v2"
API_KEY        = "3bb7dcfa-b77f-4da7-bb9c-df390c610cf0"
SPRITES_DIR    = Path(__file__).parent / "sprites"
POLL_INTERVAL  = 15   # seconds between poll sweeps
MAX_CONCURRENT = 3    # PixelLab hard limit
MAX_JOB_WAIT   = 2400 # seconds before giving up (40 min — these jobs are slow)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# ── Sprite Definitions ───────────────────────────────────────────────────────
SPRITES = [
    ("warrior", 1, "Young recruit in simple leather armor and iron sword, brown hair, determined expression, chibi RPG fantasy pixel art style"),
    ("warrior", 2, "Soldier in chainmail with a steel sword and round shield, short dark hair, chibi RPG fantasy pixel art style"),
    ("warrior", 3, "Knight in plate armor with longsword and heater shield, closed helmet with visor, chibi RPG fantasy pixel art style"),
    ("warrior", 4, "Elite knight in ornate dark plate armor with glowing runes, great sword, plumed helmet, chibi RPG fantasy pixel art style"),
    ("warrior", 5, "Legendary paladin in radiant golden armor with holy sword, wings of light, glowing aura, chibi RPG fantasy pixel art style"),
    ("mage", 1, "Apprentice in simple blue robes holding a wooden staff, messy brown hair, chibi RPG fantasy pixel art style"),
    ("mage", 2, "Journeyman mage in purple robes with a crystal-tipped staff, pointy hat, chibi RPG fantasy pixel art style"),
    ("mage", 3, "Sorcerer in dark robes with arcane symbols, glowing blue staff, floating spell orb, chibi RPG fantasy pixel art style"),
    ("mage", 4, "Archmage in elaborate star-patterned robes, powerful staff with large gem, magical sparks, chibi RPG fantasy pixel art style"),
    ("mage", 5, "Grand Wizard in cosmic void-black robes with galaxy patterns, staff cracking with lightning, glowing eyes, chibi RPG fantasy pixel art style"),
    ("ranger", 1, "Scout in simple green tunic with short bow and quiver, blonde hair in ponytail, chibi RPG fantasy pixel art style"),
    ("ranger", 2, "Hunter in leather armor with a longbow, forest cloak, hood down, brown hair, chibi RPG fantasy pixel art style"),
    ("ranger", 3, "Ranger in studded leather armor with composite bow, hooded green cloak, steely gaze, chibi RPG fantasy pixel art style"),
    ("ranger", 4, "Warden in elven-carved armor with enchanted bow glowing green, silver arrows, leaf motifs, chibi RPG fantasy pixel art style"),
    ("ranger", 5, "Legendary archer in moonsilver armor with a divine bow trailing stardust, glowing green eyes, chibi RPG fantasy pixel art style"),
    ("cleric", 1, "Novice in simple white robes with a wooden holy symbol, gentle smile, red hair, chibi RPG fantasy pixel art style"),
    ("cleric", 2, "Acolyte in white and gold robes with an iron mace and small shield, short hair, chibi RPG fantasy pixel art style"),
    ("cleric", 3, "Priest in ornate white and gold vestments with a blessed mace, radiant holy symbol, chibi RPG fantasy pixel art style"),
    ("cleric", 4, "High priest in gleaming silver vestments with a divine mace, halo effect, glowing symbol, chibi RPG fantasy pixel art style"),
    ("cleric", 5, "Divine champion in angelic white and gold armor with a sacred war hammer, golden wings, brilliant aura, chibi RPG fantasy pixel art style"),
    ("rogue", 1, "Street thief in patched dark clothes with a small dagger, narrow eyes, dark hair, chibi RPG fantasy pixel art style"),
    ("rogue", 2, "Cutpurse in fitted dark leather with twin daggers, hood up, shadowy expression, chibi RPG fantasy pixel art style"),
    ("rogue", 3, "Shadow in sleek black leather armor with enchanted daggers, face scarf, hidden in shadow, chibi RPG fantasy pixel art style"),
    ("rogue", 4, "Assassin in masterwork shadow leather with poisoned blades, skull motif, barely visible, chibi RPG fantasy pixel art style"),
    ("rogue", 5, "Phantom in void-woven armor that seems to absorb light, ghostly daggers, ethereal smoke trails, chibi RPG fantasy pixel art style"),
    ("bard", 1, "Wanderer in colorful patchwork clothes strumming a small lute, curly hair, bright smile, chibi RPG fantasy pixel art style"),
    ("bard", 2, "Minstrel in jester-style outfit with a lute and small dagger, feathered hat, chibi RPG fantasy pixel art style"),
    ("bard", 3, "Performer in elegant colorful silks with an enchanted lute, theatrical expression, chibi RPG fantasy pixel art style"),
    ("bard", 4, "Virtuoso in noble's outfit with gold trim, magical lute with glowing strings, captivating aura, chibi RPG fantasy pixel art style"),
    ("bard", 5, "Legendary Bard in shimmering prismatic robes, divine instrument crackling with magical music, starlight effects, chibi RPG fantasy pixel art style"),
]

def log(msg):
    print(msg, flush=True)

def submit_job(description):
    payload = {
        "description": description,
        "image_size": {"width": 48, "height": 64},
        "outline": "black",
        "shading": "shading",
        "detail": "medium",
    }
    resp = requests.post(
        f"{API_BASE}/create-character-with-4-directions",
        json=payload, headers=HEADERS, timeout=30,
    )
    if not resp.ok:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    job_id = (data.get("background_job_id") or data.get("id")
              or data.get("job_id") or data.get("jobId"))
    if not job_id:
        raise ValueError(f"No job_id in: {data}")
    return job_id

def poll_job(job_id):
    """Returns result dict if succeeded, None if still running, raises on failure."""
    resp = requests.get(
        f"{API_BASE}/background-jobs/{job_id}",
        headers=HEADERS, timeout=15,
    )
    if not resp.ok:
        raise RuntimeError(f"Poll HTTP {resp.status_code}: {resp.text[:200]}")
    data = resp.json()
    status = data.get("status", "").lower()
    if status == "succeeded":
        return data
    elif status in ("failed", "error", "cancelled"):
        detail = (data.get("last_response") or {}).get("error", data)
        raise RuntimeError(f"Job failed: {detail}")
    return None

def extract_south_url(job_data):
    result = job_data.get("result") or job_data.get("output") or job_data
    if isinstance(result, dict):
        images = result.get("images") or result.get("frames") or {}
        if isinstance(images, dict):
            for key in ("south", "down", "front"):
                if key in images:
                    entry = images[key]
                    return entry.get("url") if isinstance(entry, dict) else entry
        if isinstance(images, list) and images:
            for item in images:
                dir_ = (item.get("direction") or item.get("name") or "").lower()
                if dir_ in ("south", "down", "front", "s"):
                    return item.get("url")
            # fallback: first image (south is usually index 0)
            first = images[0]
            return first.get("url") if isinstance(first, dict) else first
        url = result.get("url") or result.get("image_url")
        if url:
            return url
    raise ValueError(f"Cannot find south URL in: {job_data}")

def download_image(url, dest):
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    dest.write_bytes(resp.content)

def main():
    SPRITES_DIR.mkdir(parents=True, exist_ok=True)

    # Build queue of sprites that still need downloading
    todo = deque()
    for class_name, tier, desc in SPRITES:
        filename = f"{class_name}_t{tier}.png"
        if (SPRITES_DIR / filename).exists():
            log(f"  SKIP  {filename}  (already exists)")
        else:
            todo.append((filename, desc))

    if not todo:
        log("All sprites already exist — nothing to do.")
        return 0

    total   = len(todo)
    done    = 0
    failed  = []
    # in_flight: list of (filename, job_id, submitted_at)
    in_flight = []

    log(f"\n{'═'*60}")
    log(f"Generating {total} sprites (max {MAX_CONCURRENT} concurrent jobs)…")
    log("═" * 60)

    while todo or in_flight:
        # Fill up to MAX_CONCURRENT slots
        while todo and len(in_flight) < MAX_CONCURRENT:
            filename, desc = todo.popleft()
            try:
                job_id = submit_job(desc)
                in_flight.append((filename, job_id, time.time()))
                log(f"  → SUBMIT  {filename}  job={job_id}")
            except Exception as exc:
                log(f"  ✗ SUBMIT FAIL  {filename}: {exc}")
                failed.append(filename)

        if not in_flight:
            break

        time.sleep(POLL_INTERVAL)

        # Poll all in-flight jobs
        still_running = []
        for filename, job_id, submitted_at in in_flight:
            elapsed = time.time() - submitted_at
            try:
                result = poll_job(job_id)
                if result is not None:
                    url  = extract_south_url(result)
                    dest = SPRITES_DIR / filename
                    download_image(url, dest)
                    size = dest.stat().st_size
                    done += 1
                    log(f"  ✓ [{done}/{total}]  {filename}  ({size:,} bytes, {elapsed:.0f}s)")
                elif elapsed > MAX_JOB_WAIT:
                    log(f"  ✗ TIMEOUT  {filename}  after {elapsed:.0f}s")
                    failed.append(filename)
                else:
                    still_running.append((filename, job_id, submitted_at))
            except Exception as exc:
                log(f"  ✗ ERROR  {filename}: {exc}")
                failed.append(filename)

        in_flight = still_running
        if in_flight or todo:
            log(f"  … {len(in_flight)} running, {len(todo)} queued")

    log("")
    log("═" * 60)
    log(f"Done: {done}/{total} sprites saved to {SPRITES_DIR}")
    if failed:
        log(f"Failed ({len(failed)}): {', '.join(failed)}")
    log("═" * 60)
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
