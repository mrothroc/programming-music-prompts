# Music Prompt Library Skills

This project includes 5 custom Claude Code skills for managing the neuroscience-informed music prompt library.

## Available Skills

### 1. `prompt-stats`
**Purpose**: View library statistics and progress

**When Claude uses it**:
- User asks "how many prompts are done?"
- User wants to see completion status
- User asks for library overview

**What it shows**:
- Total prompts
- Generation completion %
- Rating statistics
- Breakdown by time block

---

### 2. `prompt-find`
**Purpose**: Search and filter prompts

**When Claude uses it**:
- User asks to find prompts with specific instruments
- User searches for genres, BPM, or text
- User wants unrated prompts
- User asks for excellent-rated prompts only

**Search options**:
- By time block
- By BPM
- By generation status
- By rating status
- Text search across all fields

---

### 3. `prompt-show`
**Purpose**: Display detailed prompt information

**When Claude uses it**:
- User asks "show me prompt 40"
- User wants full details about a specific prompt
- User needs to see Suno prompt text

**What it shows**:
- BPM and brainwave target
- Genres and instruments
- Generation status and ratings
- Genetic lineage notes
- Full Suno prompt (with --verbose)

---

### 4. `prompt-rate`
**Purpose**: Add ratings to prompts after listening

**When Claude uses it**:
- User says "prompt 40 is excellent"
- User provides feedback on generated music
- User wants to rate a prompt

**Rating guidelines**:
- Use ⭐ for excellent prompts
- Include specific details about what works
- Note particular instruments/elements

---

### 5. `prompt-mark-generated`
**Purpose**: Mark prompts as generated in Suno

**When Claude uses it**:
- User says "I generated prompts 40-45"
- User wants to track generation progress
- User needs to mark completion

**Options**:
- Single prompt: `40`
- Multiple: `40 41 42`
- All: `--all`

---

## How Skills Work

Claude Code skills are **model-invoked** - Claude automatically decides when to use them based on:
1. Your request
2. The skill's description
3. Available context

You don't need to explicitly call skills - just ask naturally:
- "How many prompts are rated?" → triggers `prompt-stats`
- "Find prompts with saxophone" → triggers `prompt-find`
- "Show me prompt 40" → triggers `prompt-show`
- "Prompt 41 is excellent" → triggers `prompt-rate`

---

## Under the Hood

All skills use the Python utility scripts in `scripts/`:
- `stats.py` - Statistics
- `find_prompts.py` - Search/filter
- `show_prompt.py` - Display details
- `add_rating.py` - Add ratings
- `mark_generated.py` - Mark generation status

Skills automatically:
- Navigate to `scripts/` directory
- Activate Python virtual environment
- Run appropriate script
- Handle CSV operations safely

---

## Benefits

**For you:**
- Natural language interaction with library
- No need to remember script commands
- Automatic context awareness

**For future Claude sessions:**
- Don't need to figure out CSV operations from scratch
- Consistent, safe CSV handling
- Clear documentation of available operations

---

## Files

Skills are located in `.claude/skills/`:
```
.claude/skills/
├── prompt-stats/SKILL.md
├── prompt-find/SKILL.md
├── prompt-show/SKILL.md
├── prompt-rate/SKILL.md
└── prompt-mark-generated/SKILL.md
```

Each skill is a standalone directory with a `SKILL.md` file containing:
- YAML frontmatter (name, description, allowed-tools)
- Detailed documentation
- Usage examples
- Related skills

---

## Testing Skills

Skills should be automatically detected by Claude Code. To verify:

1. Ask Claude a question that should trigger a skill:
   - "Show me the library stats"
   - "Find prompts with saxophone"
   - "What's in prompt 40?"

2. Claude should automatically invoke the appropriate skill

3. If skills aren't working, check:
   - Files are in `.claude/skills/[skill-name]/SKILL.md`
   - YAML frontmatter is valid (proper `---` delimiters)
   - You're in the project root directory
   - Try restarting the Claude Code session

---

## Adding New Skills

To create additional skills:

1. Create directory: `.claude/skills/skill-name/`
2. Create `SKILL.md` with YAML frontmatter
3. Write clear description with trigger terms
4. Document usage and examples
5. Test with natural language queries

See existing skills as templates.
