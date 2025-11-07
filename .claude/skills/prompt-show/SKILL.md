---
name: prompt-show
description: Display detailed information about a specific music prompt including BPM, genres, instruments, brainwave target, notes, and ratings. Use when user asks about a specific prompt number or wants full details.
allowed-tools: Bash, Read
---

# Prompt Details Skill

This skill displays comprehensive information about a specific music prompt.

## What it does

- Shows all prompt details (BPM, genres, instruments, etc.)
- Displays brainwave target and mood keywords
- Shows generation status and ratings
- Includes prompt notes and genetic lineage
- Can display verbose output with full Suno prompt text

## When to use

- User asks "show me prompt 40"
- User wants details about a specific prompt
- User asks "what's in prompt 41?"
- User needs to see full Suno prompt text
- User wants to understand a prompt's composition

## Usage examples

```bash
cd .claude/skills/prompt-show/scripts
source ../../venv/bin/activate

# Basic info
python show_prompt.py 40

# Full details (includes Suno prompt and full description)
python show_prompt.py 40 --verbose
python show_prompt.py 40 -v
```

## Example output (basic)

```
============================================================
Prompt 40: Midday Refresh
============================================================
BPM: 98 | Alpha Boost
Genres: deep house, bossa nova
Instruments: four-on-floor, nylon guitar, Rhodes, swing quantization

Notes: Mutation: swing quantization (Prompt #13 DNA)
Generated: Yes
Rating: Excellent for midday refresh ⭐
```

## Example output (verbose)

Includes all the above plus:
- Full Suno prompt text (the actual prompt sent to Suno AI)
- Complete description field
- All CSV fields formatted for readability

## Prompt ID format

- Use just the number: `40` or `41`
- Leading zeros optional: `05` or `5` both work
- Must be valid prompt ID (1-70)

## Common use cases

1. **Before generating**: Review prompt details to understand composition
2. **After listening**: See what elements created the sound
3. **Comparing prompts**: View multiple prompts to find patterns
4. **Checking ratings**: See if prompt has been rated yet
5. **Understanding lineage**: See genetic algorithm notes (parent DNA, mutations, hybrids)

## Files used

- `scripts/show_prompt.py` - Display script (embedded in this skill)
- `scripts/csv_utils.py` - CSV reading and formatting utilities (embedded in this skill)
- `../../../../programming_music_prompts.csv` - Data source (project root)

## Related skills

- Use `prompt-find` to search for prompts first
- Use `prompt-rate` to add ratings after viewing
- Use `prompt-stats` for library overview
