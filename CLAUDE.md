# Suno Music Generation Project

**Last Updated**: 2025-11-07
**Status**: ✅ All 70 prompts generated and catalogued

---

## Quick Summary

This project generates a **neuroscience-informed library of 70 instrumental music prompts** for programming work using Suno AI. Music is designed to induce specific brainwave states (Theta-Gamma coupling, Alpha boost, etc.) throughout a programmer's workday.

**Key Innovation**: Using a genetic algorithm approach - 50% proven parent DNA + 30% hybrids + 20% mutations to avoid convergence while maintaining quality.

---

## File Structure

### Primary Files

- **`programming_music_prompts.csv`** - CANONICAL SOURCE (70 prompts, all generated)
- **`venv/`** - Python virtual environment for CSV processing
- **`scripts/`** - Python utilities for safe CSV operations
- **`backup/`** - Historical CSVs (not actively used)

### Documentation

- **`docs/project-overview.md`** - Detailed project background and methodology
- **`docs/music-library.md`** - Complete prompt catalog organized by time blocks
- **`docs/genetic-algorithm.md`** - Parent DNA, mutations, and diversity strategy
- **`docs/csv-schema.md`** - Column definitions and usage examples
- **`docs/suno-generation.md`** - How to generate prompts in Suno (links to existing workflow docs)
- **`docs/user-preferences.md`** - Ratings and feedback on generated music

### Scripts & Skills

- **`scripts/README.md`** - Python utility scripts for CSV management
- **`.claude/SKILLS_README.md`** - Claude Code skills documentation

### Legacy Workflow Docs (Keep as-is)

- **`CRITICAL-GENERATION-WORKFLOW.md`** - Step-by-step Suno generation workflow
- **`suno-automation-custom-mode.md`** - Technical UI automation details
- **`suno-automation-findings.md`** - Testing results and lessons learned

---

## Common Tasks

**Note**: Claude Code skills automate these tasks - just ask naturally!

### View library statistics
- **Ask Claude**: "Show me the library stats"
- **Manual**: `cd scripts && source ../venv/bin/activate && python stats.py`

### Find prompts
- **Ask Claude**: "Find prompts with saxophone" or "Show unrated prompts"
- **Manual**: `cd scripts && python find_prompts.py --search "saxophone"`

### View prompt details
- **Ask Claude**: "Show me prompt 40"
- **Manual**: `cd scripts && python show_prompt.py 40`

### Add ratings
- **Ask Claude**: "Prompt 40 is excellent"
- **Manual**: `cd scripts && python add_rating.py 40 "Excellent ⭐"`

### Mark as generated
- **Ask Claude**: "I generated prompts 40-45"
- **Manual**: `cd scripts && python mark_generated.py 40 41 42 43 44 45`

See `scripts/README.md` for detailed script usage and `.claude/SKILLS_README.md` for skills documentation.

---

## Key Insights

1. **Saxophone as texture** (not melody) works excellently for midday refresh (Prompt 41 ⭐)
2. **Quality variance is normal** - Suno generates 2 versions per prompt, keep the best
3. **Both Styles AND Title fields must be filled** - Common mistake causes "Untitled" songs
4. **Genetic diversity prevents incest** - Don't clone the same 2 prompts 38 times

---

## For More Details

- **What we're building**: See `docs/project-overview.md`
- **Prompt catalog**: See `docs/music-library.md`
- **Why genetic algorithm**: See `docs/genetic-algorithm.md`
- **CSV structure**: See `docs/csv-schema.md`
- **How to generate**: See `docs/suno-generation.md`
- **User ratings**: See `docs/user-preferences.md`

---

*Keep this file concise. Add details to docs/ files.*
