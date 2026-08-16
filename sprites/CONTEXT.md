# TaskQuest - Sprites Module Context

## Project Overview

**TaskQuest** is a fantasy RPG web application with a focus on character progression and customization. The sprites module handles generation, management, and organization of all visual assets including character avatars, animations, backgrounds, and environment assets.

- **Platform**: Web-based RPG with mobile-responsive design
- **Core Features**: Character customization, avatar progression system, sprite-based animations
- **API Integration**: PixelLab AI for sprite generation, Supabase for database backend

## Tech Stack

### Backend/Generation
- **Python 3.x**: Primary scripting language for sprite generation
- **PixelLab API**: AI-powered sprite generation service
- **Supabase**: PostgreSQL database with real-time features
- **Sharp**: High-performance image processing (Node.js)

### Frontend
- **HTML5/CSS3**: Web interface with custom CSS variables
- **Vanilla JavaScript**: Client-side interactions
- **Supabase JS SDK**: Database connectivity
- **Google Fonts**: Cinzel (headers) and Crimson Pro (body text)

### Development Tools
- **Node.js**: Package management and build tools
- **Git**: Version control with staged asset management
- **Claude Code**: AI-assisted development and automation

## Database Schema

### Core Tables

#### `avatar_items`
```sql
- id: UUID (PRIMARY KEY, auto-generated)
- name: TEXT (display name, e.g. "Recruit", "Archmage")
- description: TEXT (flavor text)
- item_type: TEXT (currently "base" for all character types)
- is_default: BOOLEAN (true for tier 1 warriors only)
- sort_order: INTEGER (10-14 warriors, 20-24 mages, etc.)
- sprite_key: TEXT (file reference, e.g. "warrior_t1", "mage_t5")
```

#### `profiles`
```sql
- customization: JSONB (default: {"hair":"brown","skin":"medium"})
```

### Data Relationships
- **6 Character Classes**: warrior, mage, ranger, cleric, rogue, bard
- **5 Tiers per Class**: t1 (basic) through t5 (legendary)
- **30 Total Base Sprites**: Complete class-tier matrix
- **Sort Order System**: Classes separated by 10s (warriors: 10-14, mages: 20-24, etc.)

## Sprite Naming Conventions

### Character Sprites
- **Format**: `{class}_t{tier}` (e.g., `warrior_t1`, `mage_t5`)
- **Classes**: warrior, mage, ranger, cleric, rogue, bard
- **Tiers**: 1-5 (1=basic, 5=legendary)
- **File Type**: PNG with white background, south-facing orientation

### Character Layers
- **Base Layers**: `skin.png`, `hair.png`, `shirt.png`, `pants.png`, `boots.png`, `sword.png`
- **Hair Variants**:
  - Male: `hair_m1.png` through `hair_m21.png`+ 
  - Female: `hair_f1.png` through `hair_f5.png`+

### Animation Assets
- **Fire Animation**: `fire_f0.png` through `fire_f15.png` (16 frames)
- **Campfire**: `campfire.png`, `campfire_food.png`, `campfire_frame0.png`
- **Frame Naming**: Sequential numbering starting from 0

### Environment Assets
- **Backgrounds**: `layer1.png` through `layer5.png` (parallax layers)
- **Ground**: `ground.png` (base terrain)
- **Objects**: `chest.png`, `enemy_portal.png`

## Animation Frame Counts

| Asset Type | Frame Count | Format | Notes |
|------------|-------------|--------|-------|
| Fire Animation | 16 frames | `fire_f{0-15}.png` | Loop animation |
| Campfire | 2+ frames | `campfire_frame{n}.png` | Static + variants |
| Character Base | 1 frame | `{class}_t{tier}.png` | South-facing static |

## Character Layer System

### Rendering Order (bottom to top)
1. **Skin** (`skin.png`) - Base character body
2. **Hair** (`hair_m{n}.png` / `hair_f{n}.png`) - Gender-specific variants  
3. **Shirt** (`shirt.png`) - Upper body clothing
4. **Pants** (`pants.png`) - Lower body clothing
5. **Boots** (`boots.png`) - Footwear
6. **Weapons** (`sword.png`) - Equipment overlay

### Customization System
- **Hair Colors**: Defined in profile customization JSONB
- **Skin Tones**: Multiple variants supported via customization
- **Layer Compositing**: Client-side assembly of final avatar

## Asset Directory Structure

```
sprites/
├── generate_sprites.py          # Main sprite generation script
├── generate_stone_house.py      # Building asset generator (Python)
├── generate_stone_house.js      # Building asset generator (Node.js)
├── package.json                 # Node.js dependencies (Sharp)
├── node_modules/               # Node.js packages
│   └── sharp/                  # Image processing library
├── preview_assets/             # Generated and preview assets
│   ├── anim/                   # Animation frames
│   │   ├── fire_f0.png - fire_f15.png
│   │   ├── campfire*.png
│   │   └── tile_sample.png
│   ├── bg/                     # Background layers
│   │   └── layer1.png - layer5.png
│   ├── char/                   # Character assets and layers
│   │   ├── boots.png, hair.png, pants.png, shirt.png, skin.png, sword.png
│   │   ├── hair_m1.png - hair_m21.png+ (male variants)
│   │   └── hair_f1.png - hair_f5.png+ (female variants)
│   ├── clothing/               # Additional clothing items
│   ├── home/                   # Building/structure assets
│   ├── chest.png              # Interactive objects
│   ├── enemy_portal.png       # Portal/gateway assets
│   └── ground.png             # Base terrain texture
├── test_*.py                   # Testing and validation scripts
├── recover_jobs.py             # Job recovery utilities
└── scene_preview.html          # Asset preview interface
```

## Current Git Status Summary

### Staged Changes (Ready for Commit)
- **Modified**: `../index.html` (main application file)
- **Added**: 21 animation frames (`preview_assets/anim/`)
- **Added**: 5 background layers (`preview_assets/bg/`)
- **Added**: 6 character base layers (`preview_assets/char/`)
- **Added**: 1 ground texture (`preview_assets/`)

### Untracked Files
- **Hair Variants**: 27+ hair style variants (male/female)
- **Scripts**: `generate_sprites.py`, house generation scripts
- **Dependencies**: `node_modules/`, `package-lock.json`
- **Config**: `.DS_Store`, `.claude/` directory

### Recent Commits (Database Fixes)
- Fixed avatar_seed: delete stale rows before re-inserting
- Fixed avatar_items schema: use sprite_key column for sprite lookup  
- Removed non-existent class/tier/unlock_condition columns

### Active Development
- Large batch of sprite assets ready for commit
- Database schema recently stabilized
- Asset organization and naming conventions established

## Development Workflow

1. **Generation**: Use `generate_sprites.py` with PixelLab API
2. **Organization**: Assets sorted into preview_assets structure
3. **Database**: Seed data managed via `avatar_seed.sql`
4. **Version Control**: Assets staged via Git for deployment
5. **Testing**: Preview via `scene_preview.html` interface

---

*Generated: 2026-06-05 | Module: sprites | Context: Complete*