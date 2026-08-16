#!/usr/bin/env node
// Run from sprites/ folder: node generate_stone_house.js
// Requires Node 18+ and: npm install sharp

const fs   = require('fs');
const path = require('path');

const API_KEY = '3bb7dcfa-b77f-4da7-bb9c-df390c610cf0';

async function generate() {
  // Resize style reference to exactly 128x128 using sharp (nearest-neighbour to keep pixel art crisp)
  let styleB64;
  try {
    const sharp = require('sharp');
    const resized = await sharp(path.join(__dirname, 'preview_assets/home/home_t0_tent.png'))
      .resize(128, 128, { kernel: 'nearest', fit: 'contain', background: { r:0,g:0,b:0,alpha:0 } })
      .png()
      .toBuffer();
    styleB64 = resized.toString('base64');
    console.log('Style image resized to 128x128');
  } catch(e) {
    // Fallback: read raw and hope it's already right size
    styleB64 = fs.readFileSync(path.join(__dirname, 'preview_assets/home/home_t0_tent.png')).toString('base64');
    console.warn('sharp not available, using raw file:', e.message);
  }

  const payload = {
    description: "small rustic stone house with wooden door, two small windows, mossy stone walls, simple pixel art, side view, fantasy RPG, transparent background",
    image_size: { width: 128, height: 128 },
    style_image: { type: "base64", base64: styleB64 },
    style_strength: 60.0,
    no_background: true
  };

  console.log('Calling PixelLab...');
  const resp = await fetch('https://api.pixellab.ai/v1/generate-image-bitforge', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!resp.ok) throw new Error(`API ${resp.status}: ${await resp.text()}`);

  const data = await resp.json();
  const outPath = path.join(__dirname, 'preview_assets/home/home_t1_stone_house.png');
  fs.writeFileSync(outPath, Buffer.from(data.image.base64, 'base64'));
  console.log('✅ Saved to:', outPath);
}

generate().catch(e => { console.error('Error:', e.message); process.exit(1); });
