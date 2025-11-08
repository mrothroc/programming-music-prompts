# Suno Music Generation Project

**Last Updated**: 2025-11-08
**Status**: ✅ 90 prompts generated (70 original + 20 Morning Warmup expansion)

---

## Quick Summary

This project generates a **neuroscience-informed library of 90 instrumental music prompts** for programming work using Suno AI. Music is designed to induce specific brainwave states (Theta-Gamma coupling, Alpha boost, etc.) throughout a programmer's workday.

**Key Innovation**: Using a genetic algorithm approach - 50% proven parent DNA + 30% hybrids + 20% mutations to avoid convergence while maintaining quality. Mutations are tracked in a separate influences library with status tracking (Unexplored → Tested → Proven/Avoid).

---

## File Structure

### Primary Files

- **`programming_music_prompts.csv`** - CANONICAL SOURCE (90 prompts, all generated)
- **`influences_library.csv`** - Musical influences database (46 influences, 5 categories)
- **`.claude/skills/venv/`** - Python virtual environment (shared by all skills)
- **`scripts/`** - Legacy Python utilities (superseded by skills)
- **`backup/`** - Historical CSVs (not actively used)

### Documentation

- **`docs/project-overview.md`** - Detailed project background and methodology
- **`docs/music-library.md`** - Complete prompt catalog organized by time blocks
- **`docs/genetic-algorithm.md`** - Parent DNA, mutations, and diversity strategy
- **`docs/csv-schema.md`** - Column definitions and usage examples
- **`docs/suno-generation.md`** - How to generate prompts in Suno (links to existing workflow docs)
- **`docs/user-preferences.md`** - Ratings and feedback on generated music

### Claude Code Skills

- **`.claude/SKILLS_README.md`** - Overview of all skills
- **`prompt-stats`** - View library statistics
- **`prompt-find`** - Search and filter prompts
- **`prompt-show`** - Display prompt details
- **`prompt-rate`** - Add ratings after listening
- **`prompt-mark-generated`** - Track generation progress
- **`prompt-generate`** - Generate new prompts using genetic algorithm
- **`influence-manage`** - Manage the influences library (mutations)

### Legacy Workflow Docs (Keep as-is)

- **`CRITICAL-GENERATION-WORKFLOW.md`** - Step-by-step Suno generation workflow
- **`suno-automation-custom-mode.md`** - Technical UI automation details
- **`suno-automation-findings.md`** - Testing results and lessons learned

---

## Common Tasks

**Note**: Claude Code skills automate these tasks - just ask naturally!

### Working with Prompts

- "Show me the library stats" → `prompt-stats`
- "Find prompts with saxophone" → `prompt-find`
- "Show unrated prompts" → `prompt-find`
- "Show me prompt 40" → `prompt-show`
- "Prompt 40 is excellent" → `prompt-rate`
- "I generated prompts 40-45" → `prompt-mark-generated`

### Generating New Prompts

- "Generate 20 new Morning Warmup prompts" → `prompt-generate`
- "Show parent candidates for Midday Refresh" → `prompt-generate --show-parents`
- "Suggest mutation ideas" → `prompt-generate --suggest-mutations`

### Managing Influences

- "Search for influences with reverb" → `influence-manage`
- "Show me influence 37" → `influence-manage`
- "Mark surf rock as used in prompt 91" → `influence-manage`
- "Mark celesta as avoid" → `influence-manage`

See `.claude/SKILLS_README.md` for complete skills documentation.

---

## Key Insights

### What Works ✓
1. **Saxophone as texture** (not melody) - Excellent for midday refresh (Prompt 41 ⭐)
2. **Autoharp** - Pretty good for Morning Warmup (Prompt 87, tested)
3. **Genetic diversity** - Using the 50/30/20 split prevents convergence

### What Doesn't Work ✗
1. **Celesta** - Too childlike, music box associations too playful (Prompt 89, marked "Avoid")
2. **Suno generates 2 versions** - Quality variance is normal, keep the best version
3. **Both Styles AND Title fields must be filled** - Missing either causes "Untitled" songs

### Workflow Patterns
1. **Rate based on best version** - If one version is excellent, rate the prompt excellent
2. **Track influences** - Mark influences as Used/Tested/Proven/Avoid after generating
3. **Use the influences library** - Don't repeat failed mutations (celesta), focus on proven ones

---

## Project Stats (Current)

- **Total prompts**: 90 (100% generated)
- **Time blocks**: 10 (Morning Warmup expanded to 27 prompts)
- **Influences**: 46 (1 Avoid, 1 Tested, 44 Unexplored)
- **Ratings**: 10 prompts rated (3 excellent ⭐)

## For More Details

- **What we're building**: See `docs/project-overview.md`
- **Prompt catalog**: See `docs/music-library.md`
- **Why genetic algorithm**: See `docs/genetic-algorithm.md`
- **CSV structure**: See `docs/csv-schema.md`
- **How to generate**: See `docs/suno-generation.md`
- **User ratings**: See `docs/user-preferences.md`
- **Skills documentation**: See `.claude/SKILLS_README.md`

---

*Keep this file concise. Add details to docs/ files.*
