#!/usr/bin/env python3
"""
Test PixelLab /create-character-pro endpoint.
"""
import json, requests, os

API_KEY = "3bb7dcfa-b77f-4da7b-bb9c-df390c610cf0"
BASE_URL = "https://api.pixellab.ai/v2"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def check(name, method, path, payload=None):
    print(f"\n{'='*50}")
    print(f"{method} {path}")
    try:
        if method == "GET":
            r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
        else:
            r = requests.post(f"{BASE_URL}{path}", json=payload or {}, headers=HEADERS, timeout=90)
        print(f"HTTP {r.status_code}")
        try:
            data = r.json()
            print(json.dumps(data, indent=2)[:1200])
            return r.status_code, data
        except:
            print(r.text[:400])
            return r.status_code, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# 1. Verify key works
check("balance", "GET", "/balance")

# 2. Try create-character-pro (synchronous?)
status, data = check("create-character-pro", "POST", "/create-character-pro", {
    "description": "pixel art chibi warrior in leather armor with sword, front facing",
    "image_size": {"width": 48, "height": 64},
    "outline": "black",
    "shading": "shading",
    "detail": "medium",
    "view": "front",
})

# 3. If it returned an image URL, download it
if data and isinstance(data, dict):
    img_url = None
    # Check various possible response shapes
    if data.get("image"):
        img_url = data["image"].get("url") if isinstance(data["image"], dict) else data["image"]
    elif data.get("url"):
        img_url = data["url"]
    elif data.get("images"):
        imgs = data["images"]
        img_url = imgs[0].get("url") if isinstance(imgs[0], dict) else imgs[0]
    elif data.get("background_job_id") or data.get("job_id") or data.get("id"):
        job_id = data.get("background_job_id") or data.get("job_id") or data.get("id")
        print(f"\nAsync job detected: {job_id} — polling for 60s...")
        import time
        for i in range(15):
            time.sleep(4)
            r2 = requests.get(f"{BASE_URL}/background-jobs/{job_id}", headers=HEADERS, timeout=15)
            print(f"  Poll {i+1}: HTTP {r2.status_code} → {r2.text[:200]}")
            try:
                d2 = r2.json()
                if d2.get("status") == "succeeded":
                    print("SUCCEEDED:", json.dumps(d2, indent=2)[:800])
                    break
                elif d2.get("status") in ("failed","cancelled"):
                    print("FAILED:", d2)
                    break
            except:
                pass

    if img_url:
        print(f"\nDownloading from: {img_url}")
        ir = requests.get(img_url, timeout=30)
        ir.raise_for_status()
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_warrior.png")
        with open(out, "wb") as f:
            f.write(ir.content)
        print(f"Saved {out} ({len(ir.content)} bytes) ✓")
