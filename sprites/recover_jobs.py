#!/usr/bin/env python3
"""
Check status of previously submitted PixelLab jobs and download any that completed.
These job IDs were submitted but timed out in our script — they may have finished
on PixelLab's side after we stopped waiting.
"""
import json, os, requests

API_KEY = "3bb7dcfa-b77f-4da7-bb9c-df390c610cf0"
BASE_URL = "https://api.pixellab.ai/v2"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
SPRITES_DIR = os.path.dirname(os.path.abspath(__file__))

# All job IDs from the previous run (sprite_name -> job_id)
JOBS = {
    "warrior_t4.png": "26af95b0-e163-4ae7-b786-184952ae9a14",
    "warrior_t5.png": "b45f9429-d8dd-4a49-be51-b937d48aecac",
    "mage_t1.png":    "d41236e7-0385-460f-8f6b-186a29cbaca3",
    "mage_t2.png":    "ba4785e3-56d9-40d2-b168-9878d3472659",
    "mage_t3.png":    "f17e10d1-28f2-4583-8cdb-4d7199cee4ed",
    "mage_t4.png":    "b5e064b2-4503-4cef-9107-96a13faeda93",
    "mage_t5.png":    "6f85d8d3-8686-4f2f-bd17-636c8400f84a",
    "ranger_t1.png":  "29769c2d-bf5a-4987-8b80-cbbb00ce354b",
    "ranger_t2.png":  "cf161fa5-eb26-430a-b3d3-462b6332d6e6",
    "ranger_t3.png":  "4c808665-c074-41f9-83d2-f7bfdcb354ff",
    "ranger_t4.png":  "a856213a-e97a-4417-91ac-7713abdc5e70",
    "ranger_t5.png":  "00c95d31-97b9-431f-b49b-22cf2fc663b4",
    "cleric_t1.png":  "c5c30bc2-9db9-4d31-a9ed-2ce3d8def67c",
    "cleric_t2.png":  "d0d90fbb-4cec-4916-9c30-a74ff9022abb",
    "cleric_t3.png":  "3138f83e-6eec-4fbb-bf36-bcce6e528a2b",
    "cleric_t4.png":  "4c019eba-c845-4b78-86e8-5c36c578234a",
    "cleric_t5.png":  "7ada3320-35d9-4273-a550-789b6222365c",
    "rogue_t1.png":   "d66392c6-b81f-4a0a-8dc7-2f99dd0583f2",
    "rogue_t2.png":   "0b23be20-c348-4dfe-be4e-ec2a99f06a09",
    "rogue_t3.png":   "0c63a26a-7eff-497d-8af9-ad106eff9594",
    "rogue_t4.png":   "bad36ab7-ba6e-4171-a9d7-b06e4a5031fc",
    "rogue_t5.png":   "098bc620-494b-4855-974d-debbc5308532",
    "bard_t1.png":    "3af48ae1-fc45-4aae-8f69-4e77fa9fdd49",
    "bard_t2.png":    "17be74db-98d4-404a-9fc7-941681471b2f",
    "bard_t3.png":    "fb70f4da-1a5d-43a0-b44f-10332bfa7cca",
}

def find_image_url(data):
    """Extract image URL from various response shapes."""
    result = data.get("result") or data.get("output") or data
    if isinstance(result, dict):
        images = result.get("images") or result.get("frames") or []
        if images:
            for img in images:
                direction = str(img.get("direction") or img.get("view") or "").lower()
                if direction in ("south", "front", "down"):
                    return img.get("url") or img.get("image_url")
            first = images[0]
            return first.get("url") or first.get("image_url")
        return result.get("url") or result.get("image_url")
    if isinstance(result, list) and result:
        first = result[0]
        if isinstance(first, dict):
            return first.get("url") or first.get("image_url")
        if isinstance(first, str):
            return first
    return None

recovered = 0
still_processing = []
failed = []
missing_ids = ["warrior_t1.png", "warrior_t2.png", "warrior_t3.png",
               "bard_t4.png", "bard_t5.png"]

print(f"Checking {len(JOBS)} job IDs...\n")
for sprite, job_id in JOBS.items():
    dest = os.path.join(SPRITES_DIR, sprite)
    if os.path.exists(dest):
        print(f"  SKIP  {sprite} (already exists)")
        recovered += 1
        continue

    try:
        r = requests.get(f"{BASE_URL}/background-jobs/{job_id}", headers=HEADERS, timeout=15)
        if r.status_code == 401:
            print(f"  AUTH ERROR — check API key")
            break
        if r.status_code == 404:
            print(f"  {sprite}: job not found (expired?)")
            failed.append(sprite)
            continue
        data = r.json()
        status = data.get("status", "unknown")
        print(f"  {sprite}: {status}", end="")

        if status == "succeeded":
            img_url = find_image_url(data)
            if img_url:
                ir = requests.get(img_url, timeout=30)
                ir.raise_for_status()
                with open(dest, "wb") as f:
                    f.write(ir.content)
                print(f"  → saved ({len(ir.content)} bytes) ✓")
                recovered += 1
            else:
                print(f"  → no URL in response: {json.dumps(data)[:200]}")
                failed.append(sprite)
        elif status == "processing":
            print(f"  → still running!")
            still_processing.append(sprite)
        else:
            print(f"  → {data.get('last_response', {}).get('error', 'unknown error')}")
            failed.append(sprite)
    except Exception as e:
        print(f"  {sprite}: ERROR {e}")
        failed.append(sprite)

print(f"\n{'='*50}")
print(f"Recovered: {recovered}")
print(f"Still processing: {still_processing}")
print(f"Failed/expired: {failed}")
print(f"No job ID (need re-submit): {missing_ids}")
