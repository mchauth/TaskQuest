#!/usr/bin/env python3
"""Quick PixelLab API diagnostic — submits 1 job and prints full responses."""
import requests, time

API_BASE = "https://api.pixellab.ai/v2"
API_KEY  = "3bb7dcfa-b77f-4da7-bb9c-df390c610cf0"
HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Submit one job
payload = {
    "description": "Warrior in simple leather armor, chibi RPG pixel art style",
    "image_size": {"width": 48, "height": 64},
    "outline": "black",
    "shading": "shading",
    "detail": "medium",
}
print("Submitting job...")
r = requests.post(f"{API_BASE}/create-character-with-4-directions", json=payload, headers=HEADERS, timeout=30)
print(f"HTTP {r.status_code}")
print("Response:", r.text)

if not r.ok:
    raise SystemExit("Submit failed")

data = r.json()
job_id = data.get("background_job_id") or data.get("id")
print(f"\nPolling job: {job_id}")

for i in range(20):
    time.sleep(5)
    r2 = requests.get(f"{API_BASE}/background-jobs/{job_id}", headers=HEADERS, timeout=15)
    print(f"\nPoll #{i+1} — HTTP {r2.status_code}")
    print("Response:", r2.text[:1000])
    status = r2.json().get("status", "")
    if status in ("succeeded", "failed", "error", "cancelled"):
        print(f"\nFinal status: {status}")
        break
