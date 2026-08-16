#!/usr/bin/env python3
# Run: python3 generate_stone_house.py
import base64, json, urllib.request, os

API_KEY = "3bb7dcfa-b77f-4da7-bb9c-df390c610cf0"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview_assets/home")

# Reference: House Tiles.png = stone building, open front like a dollhouse stage set,
# triangular peaked roof with visible wooden rafters inside, stone brick walls on sides,
# arched wooden door, windows with blue glass, dark ground at bottom.
# We want the SAME open-front style for Ranger's Outpost.

variants = [
    (11,  "pixel art 2D RPG building, stone cottage open front stage set view, triangular peaked roof with wooden rafters visible inside, grey stone brick walls on left and right sides only, arched wooden door, two windows with blue glass, dark soil ground, no front wall, flat front facing"),
    (42,  "pixel art 2D game building sprite, medieval stone house dollhouse view, interior visible through open front, peaked red-brown roof exposed wooden beams inside, stone block walls flanking sides, rounded arched door bottom, small windows, flat 2D no perspective"),
    (77,  "2D pixel art platformer stone house, front open showing interior, triangular roof rafters exposed, stone walls left and right, wooden arched door ground floor, windows, dark foundation, flat game tile no perspective no depth"),
    (128, "pixel art RPG stone house open front, peaked roof with visible wooden rafters, grey stone walls on both sides, arched door and windows, interior open and visible, 2D side scroller building tile, flat front"),
    (256, "stone cottage pixel art open cutaway front, triangular tiled roof wooden structure visible inside, flanking stone walls, arched wooden door, blue window panes, dark ground, 2D flat RPG game building"),
]

for i, (seed, desc) in enumerate(variants, 1):
    payload = {
        "description": desc,
        "image_size": { "width": 128, "height": 128 },
        "text_guidance_scale": 7.0,
        "outline": "single color outline",
        "shading": "basic shading",
        "detail": "medium detail",
        "no_background": True,
        "seed": seed
    }
    req = urllib.request.Request(
        "https://api.pixellab.ai/v1/generate-image-pixflux",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        method="POST"
    )
    print(f"v{i} (seed {seed})...", flush=True)
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    out = os.path.join(OUT_DIR, f"home_t1_stone_house_v{i}.png")
    with open(out, "wb") as f:
        f.write(base64.b64decode(data["image"]["base64"]))
    print(f"  ✓  ${data['usage']['usd']:.4f}", flush=True)

print("\nDone — check v1–v5 in sprites/preview_assets/home/")
