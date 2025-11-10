# Contributing to Music to Code By

Thank you for your interest in contributing! This project welcomes contributions in two main areas.

---

## 1. Adding Musical Influences

The `influences_library.csv` contains curated musical influences that have been vetted for focus-enhancement properties. If you've discovered an instrument, effect, or genre that genuinely helps your programming focus, we'd love to add it.

### Criteria for Good Influences

**Must have:**
- Evidence from your personal testing that it aids concentration during programming
- Clear guidance on what aspects to use vs. avoid
- Applicability to programming context (not just "sounds nice")

**Examples:**
- ✅ Mbira (thumb piano) - Gentle metallic texture, repetitive patterns, supports theta-alpha states
- ✅ Dub delay - Spacious depth without distraction, adds interest while maintaining predictability
- ✅ Polyrhythms - Engaging complexity prevents habituation without demanding attention
- ❌ Vocals - Language interference with verbal working memory
- ❌ Dramatic crescendos - Attention capture takes focus away from code
- ❌ Emotional piano (Chopin nocturnes in high-energy blocks) - Wrong arousal level for task

### How to Add an Influence

1. **Fork the repository**

2. **Add your influence to `influences_library.csv`:**

```csv
Influence_ID,Category,Name,Elements_To_Use,Elements_To_Avoid,Adaptation_Notes,Used_In_Prompts,Status
88,Acoustic Instruments,Hammered Dulcimer,"Gentle metallic resonance, repetitive arpeggios, natural decay","Aggressive striking, dramatic builds","Use soft mallet techniques for morning warmup and theta-alpha transition blocks. Avoid loud hammered patterns that demand attention.",,Unexplored
```

**Fields:**
- **Influence_ID**: Next available number
- **Category**: One of: Acoustic Instruments, Electronic Effects, Rhythmic Elements, Textures, Genre Influences
- **Name**: Specific instrument, effect, or style
- **Elements_To_Use**: What aspects support focus (be specific)
- **Elements_To_Avoid**: What aspects destroy focus (critical for programming music)
- **Adaptation_Notes**: How to apply it to programming context, which time blocks it suits
- **Used_In_Prompts**: Leave blank (populated when used)
- **Status**: Set to "Unexplored"

3. **Submit a Pull Request with:**
   - Your influence addition
   - A clear explanation of:
     - Why this influence aids programming cognition
     - Personal testing experience (how long, what tasks, what you noticed)
     - Which time blocks it's best suited for
     - Any neuroscience rationale if applicable

4. **Review process:**
   - Maintainers will test the influence in their own workflows
   - May request clarification on Elements_To_Use/Avoid
   - Once merged, marked as "Unexplored" until tested by multiple users

---

## 2. Enhancing Claude Code Skills

The skills in `.claude/skills/` are the core of the workflow. Improvements are welcome!

### Skill Architecture

Each skill has:
- `SKILL.md` - Describes when/how to invoke the skill
- `scripts/` - Python implementation (called by Claude Code)
- Shared `venv/` at `.claude/skills/venv/`

### Areas for Improvement

#### Search & Discovery
- Fuzzy matching for instrument/genre searches
- Semantic search ("find calming morning music")
- Filter by multiple criteria simultaneously
- Search history and saved queries

#### Generation Algorithm
- More sophisticated parent selection (weighted by ratings)
- Automatic detection of overused influences
- A/B testing framework for comparing generation strategies
- Diversity metrics to prevent genetic convergence

#### Analytics & Insights
- Visualize library evolution over time
- Identify patterns in your ratings (what instruments correlate with "excellent"?)
- Time block statistics (which blocks need more variety?)
- Mutation success rate tracking

#### Integration
- Suno API integration when/if available
- Export to playlist formats (Spotify, Apple Music)
- Integration with EEG devices for validation
- Sync between multiple users (team programming music libraries)

### Contributing Code

**Before writing code:**
1. **Open an issue** describing the feature/enhancement
2. Discuss approach with maintainers
3. Ensure it fits the Claude Code conversational experience

**Development workflow:**
```bash
# Fork and clone
git clone https://github.com/yourusername/programming-music-prompts.git
cd programming-music-prompts

# Create feature branch
git checkout -b feature/semantic-search

# Make changes to skills
# Test in Claude Code:
cd .claude/skills/your-skill
source ../venv/bin/activate
python scripts/your_script.py --test

# Commit with conventional commits
git commit -m "feat(prompt-find): add semantic search capability"

# Push and create PR
git push origin feature/semantic-search
```

**Code guidelines:**
- Maintain the conversational Claude Code experience
- Keep skills focused and single-purpose
- Use the existing `csv_utils.py` for CSV operations
- Add docstrings and type hints
- Update `SKILL.md` with new functionality
- Test with various library sizes (10 prompts, 100 prompts, 1000 prompts)

**Testing:**
- Test all skills after changes to shared utilities
- Verify CSV integrity after write operations
- Test edge cases (empty ratings, missing columns, Unicode characters)

---

## Code of Conduct

- Be respectful and constructive
- Focus on programming cognition, not general music preferences
- Back claims with personal testing experience
- Credit research sources when applicable

---

## Questions?

Open an issue for discussion before contributing. We're happy to help!

## License

By contributing, you agree your contributions will be licensed under the MIT License.
