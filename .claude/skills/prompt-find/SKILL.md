---
name: prompt-find
description: Search and filter music prompts by time block, BPM, generation status, rating, or text search. Use when user wants to find specific prompts, search for instruments/genres, find unrated prompts, or filter by any criteria.
allowed-tools: Bash, Read
---

# Prompt Finder Skill

This skill searches and filters the music prompt library using various criteria.

## What it does

- Search by time block (Morning Warmup, Deep Focus, etc.)
- Filter by BPM
- Find generated/ungenerated prompts
- Find rated/unrated prompts
- Find excellent-rated prompts only
- Text search across all fields (genres, instruments, notes)

## When to use

- User asks to "find prompts with saxophone"
- User wants "unrated prompts"
- User asks for "midday refresh prompts"
- User searches for specific BPM
- User wants to see "excellent prompts"
- User asks "what prompts have mellotron?"

## Usage examples

```bash
cd .claude/skills/prompt-find/scripts
source ../../venv/bin/activate

# By time block
python find_prompts.py --time-block "Midday Refresh"

# By BPM
python find_prompts.py --bpm 108

# Generation status
python find_prompts.py --generated yes
python find_prompts.py --generated no

# Rating status
python find_prompts.py --rated yes
python find_prompts.py --rated no

# Excellent only
python find_prompts.py --excellent

# Text search
python find_prompts.py --search "saxophone"
python find_prompts.py --search "mellotron"
python find_prompts.py --search "dub delay"
```

## Example output

```
✅ Found 2 prompt(s):

     40 | Midday Refresh                 | BPM  98 | "deep house, bossa nova"
        └─ Excellent for midday refresh ⭐
     41 | Midday Refresh                 | BPM 105 | "chillwave, boom bap"
        └─ Excellent - sax texture perfect! ⭐
```

## Search capabilities

The text search is case-insensitive and searches across:
- Primary genres
- Key instruments
- Mood keywords
- Notes field
- Suno prompts

## Files used

- `scripts/find_prompts.py` - Search script (embedded in this skill)
- `scripts/csv_utils.py` - CSV utilities with find/search functions (embedded in this skill)
- `../../../../programming_music_prompts.csv` - Data source (project root)
