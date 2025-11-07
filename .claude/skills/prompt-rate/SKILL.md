---
name: prompt-rate
description: Add or update ratings for music prompts after listening to generated tracks. Use when user provides feedback like "prompt 40 is excellent" or wants to rate/review prompts. Supports detailed notes and star ratings.
allowed-tools: Bash, Read
---

# Prompt Rating Skill

This skill adds or updates ratings for music prompts after the user has listened to generated tracks in Suno.

## What it does

- Adds ratings to prompts in the CSV
- Updates existing ratings
- Supports detailed feedback with notes
- Uses ⭐ emoji for excellent ratings
- Preserves all rating history in CSV

## When to use

- User says "prompt 40 is excellent"
- User provides feedback: "I like the sax texture in 41"
- User wants to rate a prompt
- User says something worked well or didn't work
- User gives qualitative feedback on generated music

## Usage examples

```bash
cd .claude/skills/prompt-rate/scripts
source ../../venv/bin/activate

# Simple excellent rating
python add_rating.py 40 "Excellent ⭐"

# Detailed feedback
python add_rating.py 41 "Excellent - sax texture perfect for midday refresh! ⭐"

# Negative/constructive feedback
python add_rating.py 42 "Too busy for deep focus - mellotron overwhelms"

# Multiple prompts (run separately)
python add_rating.py 40 "Excellent ⭐"
python add_rating.py 41 "Excellent - love the groove! ⭐"
```

## Rating guidelines

**Excellent ratings (⭐):**
- Use for prompts that achieve their goal perfectly
- Include specific details about what works
- Example: "Excellent - perfect BPM for deep focus, Rhodes adds warmth ⭐"

**Standard feedback:**
- Be specific about what works or doesn't
- Note particular instruments/elements
- Example: "Good energy but sax too prominent for background"

**Constructive criticism:**
- Identify what could be improved
- Note context (time block, use case)
- Example: "Too uptempo for morning warmup - try 90 BPM instead"

## Rating patterns from user feedback

The user has noted:
- **Prompt 40**: Deep house bossa nova - excellent for midday refresh
- **Prompt 41**: Chillwave with sax texture - excellent for midday refresh
- **Saxophone as texture** (not melodic lead) works well for programming music

## Files used

- `scripts/add_rating.py` - Rating script (embedded in this skill)
- `scripts/csv_utils.py` - CSV update utilities (embedded in this skill)
- `../../../../programming_music_prompts.csv` - Data source (project root)
- `../../../../docs/user-preferences.md` - Rating patterns and discoveries

## After rating

Run `prompt-stats` to see updated rating statistics, or use `prompt-find --excellent` to see all excellent-rated prompts.
