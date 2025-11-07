---
name: prompt-mark-generated
description: Mark music prompts as generated after creating them in Suno AI. Use when user says they've generated prompts, created songs, or completed Suno generation. Updates the Generated column in CSV to track progress.
allowed-tools: Bash, Read
---

# Mark Prompts as Generated Skill

This skill marks prompts as generated in the CSV after the user has created them in Suno AI.

## What it does

- Updates the "Generated" column to "Yes"
- Tracks which prompts have been created in Suno
- Supports single or multiple prompt IDs
- Can mark all prompts at once
- Provides confirmation of updates

## When to use

- User says "I generated prompts 40-45"
- User says "just finished creating these in Suno"
- User wants to mark progress after generation session
- User says "mark all as generated"
- User needs to track completion status

## Usage examples

```bash
cd scripts
source ../venv/bin/activate

# Single prompt
python mark_generated.py 40

# Multiple prompts
python mark_generated.py 40 41 42

# Range (must list individually)
python mark_generated.py 40 41 42 43 44 45

# All prompts
python mark_generated.py --all
```

## Example output

```
✅ Marked prompt 40 as generated
✅ Marked prompt 41 as generated
✅ Marked prompt 42 as generated
```

## When to mark prompts

**After Suno generation:**
1. User fills out Suno form with prompt details
2. User generates 2 versions in Suno
3. User listens and picks best version
4. Mark prompt as generated in CSV
5. Optionally add rating if prompt is excellent

**Workflow:**
```bash
# 1. Generate in Suno (manual)
# 2. Mark as generated
python mark_generated.py 40

# 3. Add rating if excellent
python add_rating.py 40 "Excellent ⭐"

# 4. Check progress
python stats.py
```

## Current status

All 70 prompts are currently marked as Generated=Yes. This skill will be useful for:
- Future prompt additions (71+)
- New time blocks
- Variant generations
- Testing new mutations

## Files used

- `scripts/mark_generated.py` - Marking script
- `scripts/csv_utils.py` - CSV update utilities
- `programming_music_prompts.csv` - Data source

## Related skills

- Use `prompt-stats` to see generation progress
- Use `prompt-find --generated no` to find ungenerated prompts
- Use `prompt-rate` after marking to add ratings
- Use `prompt-show` to verify prompt details before generating
