---
name: prompt-stats
description: Show statistics about the music prompt library including total prompts, generation status, ratings, and breakdown by time block. Use when the user asks about library progress, completion status, or wants an overview of the prompt collection.
allowed-tools: Bash, Read
---

# Prompt Library Statistics Skill

This skill displays comprehensive statistics about the neuroscience-informed music prompt library.

## What it does

- Shows total number of prompts (target: 70)
- Displays generation completion percentage
- Shows rating statistics (rated vs unrated, excellent count)
- Breaks down prompts by time block (Morning Warmup, Deep Focus, etc.)

## When to use

- User asks "How many prompts are done?"
- User wants to see library progress
- User asks "What's the status?"
- User wants overview of prompt collection
- User asks about completion percentage

## How to use

```bash
cd .claude/skills/prompt-stats/scripts
source ../../venv/bin/activate
python stats.py
```

## Example output

```
📊 PROMPT LIBRARY STATISTICS
  Total prompts:       70
  Generated:           70 (100.0%)
  Rated:               3 (4.3%)
  Excellent (⭐):       2

📁 By Time Block:
  Morning Warmup                  7
  Deep Focus Block 1             16
  Midday Refresh                  6
  ...
```

## Files used

- `scripts/stats.py` - Statistics script (embedded in this skill)
- `scripts/csv_utils.py` - CSV reading utilities (embedded in this skill)
- `../../../../programming_music_prompts.csv` - Canonical data source (project root)
