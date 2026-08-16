#!/usr/bin/env python3
"""
Submit ONE sprite job, handle "completed" status, and download the result.
"""
import json, os, time, requests

API_KEY = "3bb7dcfa-b77f-4da7-bb9c-df390c610cf0"
BASE_URL = "https://api.pixellab.ai/v2"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
SPRITES_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Submit ---
print("Submitting job...")
payload = {
    "description": "pixel art chibi warrior in leather armor with iron sword, front facing, white background",
    "image_size": {"width": 48, "height": 64},
    "outline": "black",
    "shading": "shading",
    "detail": "medium",
}
r = requests.post(f"{BASE_URL}/create-character-with-4-directions",
                  json=payload, headers=HEADERS, timeout=30)
print(f"HTTP {r.status_code}")
data = r.json()
print("Submit response:", json.dumps(data, indent=2))

if r.status_code != 200:
    exit(1)

job_id = data.get("background_job_id") or data.get("job_id") or data.get("id")
print(f"\nJob ID: {job_id}")
print("Polling every 10s...\n")

start = time.time()
poll_count = 0
while True:
    elapsed = time.time() - start
    if elapsed > 3600:
        print("Gave up after 60 minutes.")
        break

    time.sleep(10)
    poll_count += 1

    try:
        pr = requests.get(f"{BASE_URL}/background-jobs/{job_id}",
                         headers=HEADERS, timeout=15)
        pd = pr.json()
        status = pd.get("status", "?")
        mins, secs = int(elapsed // 60), int(elapsed % 60)
        print(f"  [{mins:02d}:{secs:02d}] Poll #{poll_count}: {status}")

        # Handle both "succeeded" and "completed"
        if status in ("succeeded", "completed"):
            print("\nFull response:")
            print(json.dumps(pd, indent=2)[:4000])

            # Extract image URL — try every known shape
            img_url = None
            result = pd.get("result") or pd.get("output") or pd.get("last_response") or pd

            if isinstance(result, dict):
                # Direct image fields
                img_url = result.get("url") or result.get("image_url")
                # Nested image object
                if not img_url and result.get("image"):
                    img = result["image"]
                    img_url = img.get("url") if isinstance(img, dict) else img
                # images list
                if not img_url:
                    images = result.get("images") or result.get("frames") or []
                    if images:
                        for img in images:
                            direction = str(img.get("direction") or img.get("view") or "").lower()
                            print(f"  Found image with direction: '{direction}'")
                            if direction in ("south", "front", "down", ""):
                                img_url = img.get("url") or img.get("image_url")
                                if img_url:
                                    break
                        if not img_url:
                            first = images[0]
                            img_url = first.get("url") or first.get("image_url")

            if isinstance(result, list) and result:
                first = result[0]
                img_url = first.get("url") if isinstance(first, dict) else first

            if img_url:
                print(f"\nDownloading: {img_url[:80]}...")
                ir = requests.get(img_url, timeout=60)
                ir.raise_for_status()
                out = os.path.join(SPRITES_DIR, "test_warrior_t1.png")
                with open(out, "wb") as f:
                    f.write(ir.content)
                print(f"Saved {out} ({len(ir.content)} bytes) ✓")
            else:
                print("\nNo image URL found — check full response above to see the structure.")
            break

        elif status in ("failed", "cancelled"):
            print(f"\nJob {status}:")
            print(json.dumps(pd, indent=2))
            break

    except KeyboardInterrupt:
        print("\nCancelled.")
        break
    except Exception as e:
        print(f"  Poll error: {e}")
