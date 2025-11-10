# Programming Music Prompts

**A Claude Code workflow for generating and refining neuroscience-informed music prompts for programming work.**

This isn't a static playlist. It's an **interactive system** using Claude Code skills to help you generate, test, rate, and evolve your own library of programming music prompts matched to your workflow and preferences.

## The Problem

Programming "in the zone" correlates with specific brainwave patterns—theta waves for memory access, alpha waves for relaxed focus, low beta for alertness without stress. Research shows music can help programmers reach these states.

In a field study, Lesiuk (2005) found programmers who listened to music while working wrote better code and completed tasks faster than those in silence. The music helped them enter flow state, improved mood, and maintained optimal arousal. Without music, code quality was poorest and tasks took longest.

Lab research supports this: background music helps maintain attention and reduces mind-wandering during focus-intensive tasks. The key is matching music to your current state—wrong music at the wrong time adds stress instead of helping.

Most "programming music" playlists ignore this. A chill lo-fi beat at 9am (theta-inducing) does nothing to wake you up. Energetic house music at 3pm when you're already fatigued just adds stress. And that harp? Sounds like a fairy tale. Hard pass.

The music needs to match where you are in your day:
- **Morning** - Gentle awakening (92-102 BPM)
- **Deep focus** - Flow state (95-112 BPM)
- **Midday fatigue** - Re-energize (108-122 BPM)
- **Evening** - Wind down (85-95 BPM)

I didn't measure brainwaves with EEG. I tested prompts across different times of day and tracked what helped me focus. The BPM ranges come from research on tempo and cognitive states, but the ratings are purely subjective—what works for me might not work for you.

## What This Is

**An intelligent workflow for creating personalized programming music**, not a static library.

### The Claude Code Skills Workflow

Six interactive skills automate the entire lifecycle:

1. **`prompt-stats`** - View your library statistics and progress
2. **`prompt-find`** - Search by instrument, genre, BPM, rating, or time block
3. **`prompt-show`** - Deep-dive into any prompt's details
4. **`prompt-generate`** - Use genetic algorithm (50% proven DNA + 30% hybrids + 20% mutations) to create new prompts
5. **`prompt-rate`** - Rate prompts after listening to capture what works for YOU
6. **`prompt-mark-generated`** - Track which prompts you've tested in Suno

**The workflow:**
```
Ask Claude → "Generate 20 new morning warmup prompts"
   ↓
Claude uses prompt-generate skill
   ↓
Identifies excellent parent prompts (your ratings)
   ↓
Generates clones, hybrids, and mutations
   ↓
You test in Suno AI
   ↓
Ask Claude → "Prompt 87 is excellent, prompt 89 is bad"
   ↓
Claude uses prompt-rate skill
   ↓
Your ratings feed back into future generation
   ↓
Library evolves to YOUR preferences
```

### What I'm Sharing

- **130 starter prompts** organized by time of day (40 tested, 90 ready to explore)
- **87 musical influences** curated for focus-enhancement (acoustic instruments, electronic effects, rhythmic elements)
- **Genetic algorithm methodology** for maintaining diversity while improving quality
- **Claude Code skills** that automate search, generation, rating, and tracking
- **Research-backed framework** connecting brainwave states to music characteristics

**This is not pre-made music.** You generate it yourself using Suno AI. The value is the **workflow** - you can adapt it, evolve it, and make it yours.

## What Worked (From Testing)

Out of 130 prompts, I tested 40:
- **4 Excellent** (3%) - Prompt #5 (chillsynth jazz fusion), #13 (deep house afro jazz), #27 (ambient house afro), #41 (chillwave boom bap)
- **14 Very Good** (11%) - Bluegrass/electronica hybrids, impressionist piano, West Coast jazz
- **15 Pretty Good** (12%) - Solid but not exceptional
- **4 Okay** (3%) - Too thumpy, wrong energy level
- **3 Bad** (2%) - Fairy-tale instruments, child's toy sounds

**Key findings:**
- Jazz-dominant hybrids work better than pure electronic
- Organic percussion (brushes, hand drums) beats electronic kicks for sustained focus
- Bluegrass/Appalachian influences work beyond just mornings
- Techno/motorik drums are too "thumpy" even at correct BPM
- Contextual energy matching matters: nocturnes at 3pm = disaster

70% remain untested. This is a work in progress.

## Quick Start

### Prerequisites

- **Claude Code** (Claude's official CLI) - [Installation guide](https://docs.claude.com/claude-code)
- **Suno AI account** - Free tier gives ~5-10 songs/day
- **Python 3.8+** (for the skills, auto-handled by Claude Code)

### Using the Workflow with Claude

**Step 1: Clone and open in Claude Code**
```bash
git clone https://github.com/mrothroc/programming-music-prompts.git
cd programming-music-prompts
claude  # Opens Claude Code CLI
```

**Step 2: Explore with natural language**
```
You: "Show me the library stats"
Claude: [uses prompt-stats skill]
        → 130 total prompts, 40 tested, 4 excellent...

You: "Find prompts with saxophone"
Claude: [uses prompt-find skill]
        → Prompt #41 (Excellent): chillwave boom bap with saxophone texture...

You: "Show me prompt 5 in detail"
Claude: [uses prompt-show skill]
        → Full details: genres, BPM, instruments, brainwave target...
```

**Step 3: Generate your first track in Suno**
```
You: "What's the best prompt to start with?"
Claude: "Try Prompt #5 - it's rated Excellent for deep focus..."

# Claude shows you the Suno-ready prompt:
chillsynth, jazz fusion, analog synth pads, electric piano, boom bap drums, 108 BPM, instrumental
```

1. Go to [Suno.ai](https://suno.ai)
2. Click Create → Instrumental mode
3. Paste the prompt → Create
4. Wait 2-3 minutes

**Step 4: Rate it and the library learns**
```
You: "Prompt 5 is excellent for me too"
Claude: [uses prompt-rate skill]
        → Rated! This will influence future generation...

You: "Prompt 89 was too playful, didn't help focus"
Claude: [uses prompt-rate skill]
        → Noted as 'Bad'. Won't use celesta in future prompts...
```

**Step 5: Generate your own prompts**
```
You: "Generate 20 new morning warmup prompts"
Claude: [uses prompt-generate skill]
        → Analyzing your ratings...
        → Found parents: Prompt #4 (Very Good), Prompt #27 (Excellent)
        → Generating: 10 clones, 6 hybrids, 4 mutations
        → Added prompts 131-150 to your library

You: "What mutations did you use?"
Claude: → Dulcimer, steel pan, vibraphone (unexplored influences)
```

### Or Use the Scripts Directly (Optional)

The skills call these Python scripts. You can run them directly if you prefer:

```bash
python scripts/stats.py                          # Library statistics
python scripts/find_prompts.py --rating "Excellent"  # Find rated prompts
python scripts/show_prompt.py 13                 # View specific prompt
python scripts/generate_prompts.py --interactive  # Generation wizard
```

But the **Claude Code workflow is the intended experience** - just talk naturally.

**Why this workflow matters:** The genetic algorithm (50% proven DNA + 30% hybrids + 20% mutations) prevents the library from converging on a single sound while continuously improving quality. Your ratings guide evolution. See [docs/genetic-algorithm.md](docs/genetic-algorithm.md) for methodology.

## Time Block Examples

### Morning Warmup (92-102 BPM)
- **Prompt #4** (Very Good) - Acoustic jazz, Appalachian folk, fingerpicked guitar
- **Prompt #27** (Excellent) - Ambient house, afro percussion, kalimba, soft kick

### Deep Focus Block 1 (95-112 BPM)
- **Prompt #5** (Excellent) - Chillsynth jazz fusion, electric piano, analog pads
- **Prompt #38** (Very Good) - Tech house jazz minimalism, filtered Rhodes

### Deep Focus Block 2 (96-108 BPM)
- **Prompt #13** (Excellent) - Deep house afro jazz, balafon, Rhodes
- **Prompt #92** (Very Good) - Impressionist piano, minimal house, Debussy-inspired

### Midday Refresh (108-122 BPM)
- **Prompt #41** (Excellent) - Chillwave boom bap, saxophone texture, lo-fi synths
- **Prompt #119** (Very Good) - Tropical house balearic, vibraphone, Mediterranean sounds

### Late Afternoon Push (95-122 BPM)
- **Prompt #128** (Very Good) - Bluegrass electronica, banjo, mandolin, synth pads
- **Prompt #130** (Pretty Good) - Nu-disco funk, Wurlitzer, funk guitar, live drums

## The Methodology

**Core principle:** Influences are ingredients. Prompts apply the neuroscience.

Each prompt targets specific mechanisms:
1. **Brainwave entrainment** - BPM matched to target states
2. **Cognitive load minimization** - Repetitive patterns, no lyrics, background texture
3. **Habituation prevention** - Polyrhythmic complexity, subtle variation
4. **Arousal modulation** - Steady energy appropriate to time of day
5. **Biophilic elements** - Field recordings (water, nature) where appropriate

The 87 influences provide diversity: acoustic instruments (dulcimer, sitar, mbira, tabla), electronic effects (dub delay, granular synthesis), rhythmic elements (swing, polyrhythms), textures (field recordings, drones), and genre influences (West Coast jazz, krautrock, balearic beat).

Add your own influences by analyzing your listening data. See the scripts for examples.

## What Doesn't Work

From testing:
- **Harp, celesta** (Prompts #85, #89) - Sound like children's toys
- **Steel pan + marimba** (Prompt #116) - Too playful, "toot toot" sounds
- **Techno/motorik kicks** (Prompts #122, #124, #125) - Too thumpy for focus
- **Emotional/reflective music in Block 2** (Prompts #95, #99, #100) - Wrong energy for fighting fatigue
- **Nocturnes at 3pm** - Night music when you need drive

Percussion matters as much as BPM. Texture should drive, not kick drums.

## What's in Here

- `programming_music_prompts.csv` - 130 prompts with 40 ratings
- `influences_library.csv` - 87 curated influences with use/avoid guidance
- `scripts/` - Python utilities for searching, rating, stats
- `.claude/skills/` - Claude Code automation (optional)
- `docs/` - [Methodology](docs/genetic-algorithm.md), [Schema](docs/csv-schema.md), [Suno workflow](docs/suno-generation-workflow.md)

## Practical Questions

**Do I need a Suno subscription?**
No. Free tier gives ~5-10 songs per day. Generate the excellent ones first.

**Can I use other platforms?**
Yes. Prompts work with any text-to-music AI (Udio, etc.)

**Should I automate generation?**
No. Manual copy/paste is faster. See [docs/suno-automation-summary.md](docs/suno-automation-summary.md).

## Installation

**Recommended:** Use with Claude Code for the full interactive experience

```bash
# Install Claude Code if you haven't already
# https://docs.claude.com/claude-code

# Clone this repository
git clone https://github.com/mrothroc/programming-music-prompts.git
cd programming-music-prompts

# Open in Claude Code
claude
```

The skills will automatically set up their Python environment on first use.

**Alternative:** Browse the CSV files directly

If you just want the data without the workflow, download `programming_music_prompts.csv` and `influences_library.csv`.

## Research References

This approach draws on research connecting music to programming performance and cognitive states:

**Music and programming performance:**
- Lesiuk (2005) - Programmers with music wrote better code faster than those in silence; music helped enter flow state and maintained optimal arousal

**Programmer brainwave studies:**
- Ishida & Uwano (2019) - Successful code comprehension significantly increased alpha (p=0.002) and beta (p<0.001) waves in programmers
- Medeiros et al. (2021) - 96.5% accuracy identifying code complexity from EEG; theta, alpha, and beta bands most discriminative
- Yeh et al. (2021) - Frontal alpha band strongly correlated with programming cognitive load (r = -0.76 to -0.94)

**Music type and cognitive states:**
- El Sayed et al. (2025) - Classical instrumental music maintains relaxed-alert EEG state; folk/pop music increases slow waves (reduced cognition)

**Flow states and brainwaves:**
- Nakamura & Csikszentmihalyi (2002) - Flow characteristics across work contexts
- Katahira et al. (2018) - EEG during flow: increased frontal theta, moderate alpha

**Brainwave entrainment:**
- Askarpour et al. (2024) - Beta-frequency beats for memory, alpha for relaxed alertness, but "significant inconsistencies remain across studies"
- Huang & Charyton (2008) - Comprehensive review of entrainment methods
- Jirakittayakorn & Wongsawat (2017) - 40 Hz binaural beats enhance working memory

**Music tempo and arousal:**
- Karageorghis & Priest (2012) - Tempo effects on arousal (sports context)

**Note:** Most brainwave entrainment research uses binaural beats (headphones required), not instrumental music at specific BPMs. The programmer EEG studies validate that alpha/beta states matter for coding, but using music tempo to target these states is theoretical. My subjective ratings reflect what worked for me, not validated science.

## License

MIT - Do what you want. Attribution appreciated.

---

**Start here:** Generate Prompt #5. If it helps you focus, explore the rest.
