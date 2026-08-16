#!/usr/bin/env python3
"""
Generate 30 TaskQuest sprites via PixelLab API.
Saves south-facing PNGs to the same folder as this script.
"""
import json, os, time, requests

API_KEY = "3bb7dcfa-b77f-4da7-bb9c-df390c610cf0"
BASE_URL = "https://api.pixellab.ai/v2"
SPRITES_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

os.makedirs(SPRITES_DIR, exist_ok=True)

SPRITES = [
    ("warrior", 1, "pixel art chibi warrior in simple leather armor with iron sword, front facing, white background, fantasy RPG style"),
    ("warrior", 2, "pixel art chibi soldier in chainmail with steel sword and round shield, front facing, white background, fantasy RPG style"),
    ("warrior", 3, "pixel art chibi knight in plate armor with longsword and heater shield, closed helmet with visor, front facing, white background, fantasy RPG style"),
    ("warrior", 4, "pixel art chibi elite knight in ornate dark plate armor with glowing runes and great sword, plumed helmet, front facing, white background, fantasy RPG style"),
    ("warrior", 5, "pixel art chibi legendary paladin in radiant golden armor with holy sword and wings of light, glowing aura, front facing, white background, fantasy RPG style"),

    ("mage",    1, "pixel art chibi apprentice mage in simple blue robes holding a wooden staff, messy brown hair, front facing, white background, fantasy RPG style"),
    ("mage",    2, "pixel art chibi mage in purple robes with crystal-tipped staff and pointy hat, front facing, white background, fantasy RPG style"),
    ("mage",    3, "pixel art chibi sorcerer in dark robes with arcane symbols, glowing blue staff, floating spell orb, front facing, white background, fantasy RPG style"),
    ("mage",    4, "pixel art chibi archmage in star-patterned robes with powerful gem-tipped staff and magical sparks, front facing, white background, fantasy RPG style"),
    ("mage",    5, "pixel art chibi grand wizard in cosmic void-black robes with galaxy patterns, lightning staff, glowing eyes, front facing, white background, fantasy RPG style"),

    ("ranger",  1, "pixel art chibi scout in green tunic with short bow and quiver, blonde ponytail, front facing, white background, fantasy RPG style"),
    ("ranger",  2, "pixel art chibi hunter in leather armor with longbow and forest cloak, brown hair, front facing, white background, fantasy RPG style"),
    ("ranger",  3, "pixel art chibi ranger in studded leather with composite bow and hooded green cloak, front facing, white background, fantasy RPG style"),
    ("ranger",  4, "pixel art chibi warden in elven armor with enchanted glowing green bow and silver arrows, front facing, white background, fantasy RPG style"),
    ("ranger",  5, "pixel art chibi legendary archer in moonsilver armor with divine stardust bow and glowing green eyes, front facing, white background, fantasy RPG style"),

    ("cleric",  1, "pixel art chibi novice cleric in simple white robes with wooden holy symbol, red hair, gentle smile, front facing, white background, fantasy RPG style"),
    ("cleric",  2, "pixel art chibi acolyte in white and gold robes with iron mace and small shield, front facing, white background, fantasy RPG style"),
    ("cleric",  3, "pixel art chibi priest in ornate white and gold vestments with blessed mace and radiant holy symbol, front facing, white background, fantasy RPG style"),
    ("cleric",  4, "pixel art chibi high priest in silver vestments with divine mace and glowing halo, front facing, white background, fantasy RPG style"),
    ("cleric",  5, "pixel art chibi divine champion in angelic white and gold armor with sacred war hammer and golden wings, brilliant aura, front facing, white background, fantasy RPG style"),

    ("rogue",   1, "pixel art chibi street thief in patched dark clothes with small dagger, narrow eyes dark hair, front facing, white background, fantasy RPG style"),
    ("rogue",   2, "pixel art chibi cutpurse in fitted dark leather with twin daggers and hood up, front facing, white background, fantasy RPG style"),
    ("rogue",   3, "pixel art chibi shadow assassin in sleek black leather with enchanted daggers and face scarf, front facing, white background, fantasy RPG style"),
    ("rogue",   4, "pixel art chibi master assassin in shadow leather with poisoned blades and skull motif, front facing, white background, fantasy RPG style"),
    ("rogue",   5, "pixel art chibi phantom in void-woven armor with ghostly daggers and ethereal smoke trails, front facing, white background, fantasy RPG style"),

    ("bard",    1, "pixel art chibi wanderer bard in colorful patchwork clothes strumming small lute, curly hair bright smile, front facing, white background, fantasy RPG style"),
    ("bard",    2, "pixel art chibi minstrel in jester-style outfit with lute and feathered hat, front facing, white background, fantasy RPG style"),
    ("bard",    3, "pixel art chibi performer in elegant colorful silks with enchanted lute, theatrical expression, front facing, white background, fantasy RPG style"),
    ("bard",    4, "pixel art chibi virtuoso bard in noble outfit with gold trim and magical glowing lute strings, front facing, white background, fantasy RPG style"),
    ("bard",    5, "pixel art chibi legendary bard in shimmering prismatic robes with divine instrument and starlight effects, front facing, white background, fantasy RPG style"),
]


def find_image_url(data):
    """Extract best image URL from a completed job response."""
    # Print structure on first call to help debug
    if not hasattr(find_image_url, "_shown"):
        find_image_url._shown = True
        print(f"\n  [DEBUG] Full job response:\n  {json.dumps(data, indent=2)[:1500]}\n")

    def extract_url(obj):
        """Recursively try to pull a URL string out of whatever we get."""
        if isinstance(obj, str) and (obj.startswith("http://") or obj.startswith("https://")):
            return obj
        if isinstance(obj, dict):
            # Direct URL keys
            for key in ("url", "image_url", "src", "uri", "link"):
                val = obj.get(key)
                if isinstance(val, str) and val.startswith("http"):
                    return val
            # Nested image object
            for key in ("image", "images", "frames", "result", "output", "last_response"):
                val = obj.get(key)
                if val:
                    found = extract_url(val)
                    if found:
                        return found
        if isinstance(obj, list) and obj:
            # Try to find south/front facing first
            for item in obj:
                if isinstance(item, dict):
                    direction = str(item.get("direction") or item.get("view") or "").lower()
                    if direction in ("south", "front", "down"):
                        found = extract_url(item)
                        if found:
                            return found
            # Fallback: first item
            return extract_url(obj[0])
        return None

    return extract_url(data)


def submit_job(description):
    payload = {
        "description": description,
        "image_size": {"width": 48, "height": 64},
        "outline": "black",
        "shading": "shading",
        "detail": "medium",
    }
    r = requests.post(f"{BASE_URL}/create-character-with-4-directions",
                      json=payload, headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    job_id = data.get("background_job_id") or data.get("job_id") or data.get("id")
    return job_id, data


def poll_until_done(job_id, max_wait=600):
    """Poll until status is 'completed' or 'succeeded'. Returns job data."""
    start = time.time()
    while time.time() - start < max_wait:
        time.sleep(5)
        r = requests.get(f"{BASE_URL}/background-jobs/{job_id}",
                        headers=HEADERS, timeout=15)
        r.raise_for_status()
        data = r.json()
        status = data.get("status", "")
        if status in ("completed", "succeeded"):
            return data
        if status in ("failed", "cancelled"):
            err = (data.get("last_response") or {}).get("error", "unknown error")
            raise RuntimeError(f"Job {status}: {err}")
    raise TimeoutError(f"Job {job_id} not done after {max_wait}s")


def download(url, dest):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    with open(dest, "wb") as f:
        f.write(r.content)
    return len(r.content)


def main():
    total = len(SPRITES)
    success, skipped, errors = 0, 0, []

    for i, (cls, tier, desc) in enumerate(SPRITES, 1):
        filename = f"{cls}_t{tier}.png"
        dest = os.path.join(SPRITES_DIR, filename)

        if os.path.exists(dest):
            print(f"[{i:02d}/{total}] SKIP  {filename}")
            skipped += 1
            continue

        print(f"[{i:02d}/{total}] {filename}...", end=" ", flush=True)
        try:
            job_id, submit_data = submit_job(desc)
            print(f"job={job_id[:8]}...", end=" ", flush=True)

            job_data = poll_until_done(job_id, max_wait=600)
            img_url = find_image_url(job_data)

            if not img_url:
                raise ValueError(f"No image URL. Response: {json.dumps(job_data)[:300]}")

            size = download(img_url, dest)
            print(f"✓ ({size:,} bytes)")
            success += 1

        except Exception as e:
            print(f"✗ {e}")
            errors.append((filename, str(e)))

        # Small gap between submissions
        if i < total:
            time.sleep(1)

    print(f"\n{'='*50}")
    print(f"Done: {success} saved, {skipped} skipped, {len(errors)} errors")
    if errors:
        print("Errors:")
        for name, err in errors:
            print(f"  {name}: {err[:120]}")


if __name__ == "__main__":
    main()
