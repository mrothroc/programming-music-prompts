---
name: influence-manage
description: Manage the influences library database (influences_library.csv) for genetic algorithm mutations. Use when user wants to add influences, search for mutation ideas, track what's been used, or explore new sonic territory for prompt generation.
allowed-tools: Bash, Read, Write
---

# Influence Management Skill

This skill manages the influences library database containing 46 musical influences used for the genetic algorithm's mutation strategy (the 20% new DNA).

## What it does

- Lists all influences (with optional filtering by category, status)
- Searches influences by text (name, elements, adaptation notes)
- Shows detailed information for a specific influence
- Adds new influences to the library
- Updates influences (marks as used, changes status)
- Shows statistics (count by category, by status)
- Helps track the evolution from Unexplored → Tested → Proven/Avoid

## When to use

- User wants to add a new musical influence
- User asks "what mutation ideas do we have?"
- User wants to find influences by category (e.g., "show me acoustic instruments")
- User asks "what influences haven't we used yet?"
- User wants to mark an influence as used in a prompt
- User wants to track which influences are proven vs should be avoided
- User is generating new prompts and needs mutation inspiration

## Influence Lifecycle

Influences progress through these states:

1. **Unexplored** (initial state) - Not yet tried in any prompt
2. **Tested** - Used in at least one generated prompt, awaiting user feedback
3. **Proven** - User rated a prompt using this influence as excellent/very good
4. **Avoid** - User feedback suggests this influence doesn't work well

## Categories

The library organizes influences into these categories:

- **Acoustic Instruments** (14) - Dulcimer, harp, autoharp, celesta, steel pan, marimba, vibraphone, glockenspiel, mandolin, bouzouki, oud, sitar, lap steel, EBow guitar
- **Electronic Effects** (9) - Dub delay, tape echo, reverb plates, analog synth arpeggios, Mellotron, granular synthesis, ambient drones, vinyl crackle, tape saturation
- **Rhythmic Elements** (6) - Swing quantization, shuffle grooves, polyrhythmic layers, odd time signatures, clave patterns, gamelan rhythms
- **Textures** (7) - Field recordings (rain/forest/ocean), harmonic drones, sustained tones, melodic percussion, tuned drums
- **Genre Influences** (10) - Surf rock, krautrock, fourth world, Balearic beat, minimalism, space music, ambient dub, lo-fi hip hop, exotica, kosmische musik

## Usage examples

```bash
cd .claude/skills/influence-manage/scripts
source ../../venv/bin/activate

# List all influences
python manage_influences.py --list

# List by category
python manage_influences.py --list --category "Acoustic Instruments"

# List by status
python manage_influences.py --list --status "Unexplored"

# Search for specific influence ideas
python manage_influences.py --search "saxophone"
python manage_influences.py --search "delay"
python manage_influences.py --search "gamelan"

# Show detailed information for an influence
python manage_influences.py --show 1
python manage_influences.py --show 12  # Sitar

# Add new influence
python manage_influences.py --add \
  --category "Acoustic Instruments" \
  --name "Hang Drum" \
  --elements "Meditative metallic tones, melodic percussion, harmonic overtones" \
  --avoid "Busy melodic patterns, aggressive playing" \
  --notes "Perfect for theta states, use gentle patterns for ambient texture"

# Mark influence as used in a prompt
python manage_influences.py --mark-used 12 --prompt-ids "45,46"

# Update status
python manage_influences.py --update-status 12 --status "Proven"

# Show statistics
python manage_influences.py --stats
```

## Integration with Genetic Algorithm Workflow

When generating new prompts (using `prompt-generate` skill), this skill helps with the **20% Mutation** strategy:

### Finding Mutation Ideas

1. **Random exploration**: List unexplored influences by category
   ```bash
   python manage_influences.py --list --status "Unexplored" --category "Electronic Effects"
   ```

2. **Thematic search**: Search for influences matching the time block mood
   ```bash
   # For theta-inducing morning warmup
   python manage_influences.py --search "theta"
   python manage_influences.py --search "gentle"

   # For focus-enhancing deep work
   python manage_influences.py --search "focus"
   python manage_influences.py --search "harmonic"
   ```

3. **Proven winners**: Find influences that worked well before
   ```bash
   python manage_influences.py --list --status "Proven"
   ```

### After Generating & Testing Prompts

1. **Mark as used**: Track which influences were applied
   ```bash
   python manage_influences.py --mark-used 7 --prompt-ids "51,52,53"
   ```

2. **Update status based on ratings**:
   - If user rates prompt as excellent/very good → mark influence as "Proven"
   - If user rates prompt poorly → mark influence as "Avoid"
   - Otherwise → mark as "Tested"

   ```bash
   python manage_influences.py --update-status 7 --status "Proven"
   ```

## Key Principles

✅ **DO:**
- Use influences to inject diversity into prompt generation
- Track which influences work well vs should be avoided
- Mark influences as used to see what's fresh vs overused
- Search the library before adding duplicates
- Use adaptation notes to guide how to apply the influence

❌ **DON'T:**
- Add influences without clear "Elements_To_Use" and "Elements_To_Avoid"
- Forget to update status after testing prompts
- Use influences marked as "Avoid"
- Apply influences that don't fit the time block's purpose (e.g., aggressive sounds in theta-inducing morning warmup)

## Example: Using Influences for Midday Refresh

**Goal**: Generate 6 prompts for Midday Refresh time block (20% mutations = ~1-2 prompts)

**Step 1**: Find suitable mutation candidates
```bash
# Search for energizing but not aggressive influences
python manage_influences.py --search "refresh"
python manage_influences.py --search "alert"
python manage_influences.py --list --category "Rhythmic Elements"
```

**Step 2**: Review candidates (Influence #8 - Glockenspiel)
- Elements to use: "Bright metallic sparkle, gentle high tones, crystalline clarity"
- Elements to avoid: "Dominant melodies, march-like patterns"
- Adaptation notes: "Subtle high-frequency accents for alertness during afternoon slump"
- Status: Unexplored

**Step 3**: Generate prompt using this influence
- Add glockenspiel as subtle accent in an electronic/acoustic hybrid
- Keep it as texture, not melody
- Target gentle alertness, not harsh stimulation

**Step 4**: After testing in Suno
```bash
# Mark as used
python manage_influences.py --mark-used 8 --prompt-ids "41"

# Update status based on user feedback
python manage_influences.py --update-status 8 --status "Proven"  # If excellent rating
```

## Files used

- `scripts/manage_influences.py` - Main management script (embedded in this skill)
- `scripts/csv_utils.py` - CSV utilities for influences_library.csv (embedded in this skill)
- `../../../../influences_library.csv` - Influences database (project root)

## Related skills

- Use with `prompt-generate` to apply the 20% mutation strategy
- Use with `prompt-rate` to track which influences led to excellent prompts
- Use with `prompt-show` to see which influences were used in a prompt

## Current Library Status

As of 2025-11-07:
- **Total influences**: 46
- **Status**: All "Unexplored" (virgin territory!)
- **Categories**: Acoustic (14), Electronic (9), Rhythmic (6), Textures (7), Genre (10)

The library is a fresh canvas waiting to inject new sonic DNA into the prompt library.
