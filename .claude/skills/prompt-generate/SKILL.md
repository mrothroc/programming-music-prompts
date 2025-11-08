---
name: prompt-generate
description: Generate new music prompts using genetic algorithm approach. Use when user wants to create more prompts for a time block, expand the library, or apply the genetic diversity strategy (50% parent DNA, 30% hybrids, 20% mutations).
allowed-tools: Bash, Read, Write
---

# Prompt Generation Skill

This skill generates new music prompts using the genetic algorithm approach to maintain diversity and quality.

## What it does

- Identifies excellent/very good prompts as "parent DNA"
- Generates new prompts using genetic diversity strategy
- Creates clones, hybrids, and mutations
- Helps expand the library for specific time blocks
- Documents the generation methodology

## When to use

- User wants to create more prompts for a time block
- User says "we need more midday refresh prompts"
- User wants to expand the library
- User asks to "generate new prompts"
- User wants to apply genetic algorithm approach

## Genetic Algorithm Strategy

### 50% Parent DNA (Proven Excellence)
Clone prompts that have been rated as excellent or very good:
- Preserve the exact formula that works
- Vary BPM slightly (±1-3 BPM)
- Adjust mood keywords for variety
- Keep core instruments and genres

### 30% Hybrids (Cross-breeding)
Combine elements from two different parent prompts:
- Mix instruments from both parents
- Blend genres creatively
- Combine rhythmic patterns
- Create acoustic-electronic fusions

### 20% Mutations (New DNA)
Introduce new instruments or effects:
- Explore uncharted sonic territory
- Add unique textures (mellotron, EBow, steel pan, etc.)
- Try new rhythmic elements (swing, dub delay)
- Test unconventional combinations

## Usage examples

```bash
cd .claude/skills/prompt-generate/scripts
source ../../venv/bin/activate

# Interactive mode (recommended)
python generate_prompts.py --interactive

# List available time blocks
python generate_prompts.py --list-blocks

# Show parent candidates for a time block
python generate_prompts.py --show-parents "Morning Warmup"

# Non-interactive (future)
python generate_prompts.py --time-block "Midday Refresh" --count 20
```

## Generation Process

1. **Identify Parents**: Find excellent/very good prompts in target time block
2. **Analyze Formula**: Extract key elements (BPM, instruments, genres, mood)
3. **Plan Distribution**:
   - How many parent clones? (50%)
   - How many hybrids? (30%)
   - How many mutations? (20%)
4. **Generate Prompts**: Create new prompts following the strategy
5. **Review & Refine**: Ensure quality and diversity
6. **Add to CSV**: Append to `programming_music_prompts.csv`
7. **Commit**: Version control the new prompts

## Example: Morning Warmup Generation

**Parents Identified:**
- Prompt #4: Acoustic jazz/Appalachian folk (fingerpicked guitar, upright bass, banjo, brush drums) @ 92 BPM - "Very good"
- Prompt #27: Ambient house/afro percussion (soft four-on-floor, kalimba, synth pads, congas) @ 101 BPM - "Excellent ⭐"

**Generated (20 prompts):**
- **6 Parent Clones**: 3 variations of each parent
- **6 Hybrids**: Combinations like fingerpicked guitar + kalimba, banjo + synth pads
- **8 Mutations**: New instruments like dulcimer, steel pan, harp, marimba, vibraphone, celesta, glockenspiel, autoharp

## Key Principles

✅ **DO:**
- Base on rated prompts (excellent/very good)
- Maintain time block characteristics (BPM range, brainwave target, mood)
- Inject diversity through mutations
- Document genetic lineage in Notes field
- Test generated prompts in Suno

❌ **DON'T:**
- Clone the same prompt 20 times (genetic incest)
- Ignore existing ratings when selecting parents
- Create prompts that don't fit the time block purpose
- Forget to capture what worked (rate the generated ones!)

## Mutation Ideas Library

**Acoustic Instruments:**
- Dulcimer, harp, autoharp, celesta
- Steel pan, marimba, vibraphone, glockenspiel
- Mandolin, bouzouki, oud, sitar
- Lap steel guitar, EBow guitar

**Electronic Effects:**
- Dub delay, tape echo, reverb plates
- Analog synth arpeggios, Mellotron
- Granular synthesis, ambient drones
- Vinyl crackle, tape saturation

**Rhythmic Elements:**
- Swing quantization, shuffle grooves
- Polyrhythmic layers, odd time signatures
- Clave patterns, gamelan rhythms

**Textures:**
- Field recordings (rain, forest, ocean)
- Harmonic drones, sustained tones
- Melodic percussion, tuned drums

## Files used

- `scripts/generate_prompts.py` - Generation script (embedded in this skill)
- `scripts/csv_utils.py` - CSV utilities (embedded in this skill)
- `../../../../programming_music_prompts.csv` - Data source (project root)

## Related skills

- Use `prompt-find` to identify parent candidates
- Use `prompt-show` to analyze parent prompts
- Use `prompt-rate` to rate generated prompts after testing
- Use `prompt-stats` to track library growth

## Current Status

⚠️ **Note**: The generation script currently provides:
- Interactive wizard to plan generation
- Parent candidate identification
- Time block listing
- Documentation of the process

Actual prompt creation is still done manually by following the genetic algorithm principles. Future enhancement: automate prompt generation using templates and combinatorial logic.
