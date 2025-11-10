---
name: prompt-generate
description: Generate new music prompts using genetic algorithm approach. Use when user wants to create more prompts for a time block, expand the library, or apply the genetic diversity strategy (50% parent DNA, 30% hybrids, 20% mutations).
allowed-tools: Bash, Read, Write
---

# Prompt Generation Skill

This skill generates new music prompts using the genetic algorithm approach to maintain diversity and quality.

**Research Foundation:** Lesiuk (2005) found programmers with music wrote better code faster than those in silence. This library applies that finding by creating music matched to different times of day—wrong music at the wrong time adds stress instead of helping.

## What it does

- Identifies excellent/very good prompts as "parent DNA"
- Generates new prompts using genetic diversity strategy
- Creates clones, hybrids, and mutations
- Helps expand the library for specific time blocks
- Documents the generation methodology

## When to use

- User wants to create more prompts for a time block
- User says "we need more midday refresh prompts"
- User wants to expand the library
- User asks to "generate new prompts"
- User wants to apply genetic algorithm approach

## Genetic Algorithm Strategy

### 50% Parent DNA (Proven Excellence)
Clone prompts that have been rated as excellent or very good:
- Preserve the exact formula that works
- Vary BPM slightly (±1-3 BPM)
- Adjust mood keywords for variety
- Keep core instruments and genres

### 30% Hybrids (Cross-breeding)
Combine elements from two different parent prompts:
- Mix instruments from both parents
- Blend genres creatively
- Combine rhythmic patterns
- Create acoustic-electronic fusions

### 20% Mutations (New DNA)
Introduce new instruments or effects:
- Explore uncharted sonic territory
- Add unique textures (mellotron, EBow, steel pan, etc.)
- Try new rhythmic elements (swing, dub delay)
- Test unconventional combinations

## Usage examples

```bash
cd .claude/skills/prompt-generate/scripts
source ../../venv/bin/activate

# Interactive mode (recommended) - includes mutation suggestions
python generate_prompts.py --interactive

# List available time blocks
python generate_prompts.py --list-blocks

# Show parent candidates for a time block
python generate_prompts.py --show-parents "Morning Warmup"

# Browse mutation influences
python generate_prompts.py --list-mutations                      # All influences by category
python generate_prompts.py --list-mutations "Acoustic Instruments"  # Filter by category

# Get random unexplored mutation suggestions
python generate_prompts.py --suggest-mutations     # 10 random suggestions
python generate_prompts.py --suggest-mutations 5   # 5 random suggestions

# Search mutations by keyword
python generate_prompts.py --search-mutations "gentle"    # For theta states
python generate_prompts.py --search-mutations "alert"     # For focus
python generate_prompts.py --search-mutations "harmonic"  # For deep work

# Non-interactive (future)
python generate_prompts.py --time-block "Midday Refresh" --count 20
```

## Generation Process

1. **Identify Parents**: Find excellent/very good prompts in target time block
2. **Analyze Formula**: Extract key elements (BPM, instruments, genres, mood)
3. **Plan Distribution**:
   - How many parent clones? (50%)
   - How many hybrids? (30%)
   - How many mutations? (20%)
4. **Generate Prompts**: Create new prompts following the strategy
5. **Review & Refine**: Ensure quality and diversity
6. **Add to CSV**: Append to `programming_music_prompts.csv`
7. **Commit**: Version control the new prompts

## Example: Morning Warmup Generation

**Parents Identified:**
- Prompt #4: Acoustic jazz/Appalachian folk (fingerpicked guitar, upright bass, banjo, brush drums) @ 92 BPM - "Very good"
- Prompt #27: Ambient house/afro percussion (soft four-on-floor, kalimba, synth pads, congas) @ 101 BPM - "Excellent ⭐"

**Generated (20 prompts):**
- **6 Parent Clones**: 3 variations of each parent
- **6 Hybrids**: Combinations like fingerpicked guitar + kalimba, banjo + synth pads
- **8 Mutations**: New instruments like dulcimer, steel pan, harp, marimba, vibraphone, celesta, glockenspiel, autoharp

## Key Principles

✅ **DO:**
- Base on rated prompts (excellent/very good)
- Maintain time block characteristics (BPM range, brainwave target, mood)
- Inject diversity through mutations
- Document genetic lineage in Notes field
- Test generated prompts in Suno
- **Match energy level to time block context** (see Contextual Energy Matching below)

❌ **DON'T:**
- Clone the same prompt 20 times (genetic incest)
- Ignore existing ratings when selecting parents
- Create prompts that don't fit the time block purpose
- Forget to capture what worked (rate the generated ones!)
- **Use relaxing influences in high-energy time blocks** (e.g., Chopin nocturnes in Deep Focus Block 2)

## Contextual Energy Matching

**Key Insight**: Energy level emerges from the *combination* of influences, BPM, and arrangement—not from individual influences alone.

**Example**:
- Chopin nocturne at 94 BPM with soft pads = Too relaxing for Deep Focus Block 2
- Chopin-inspired melody at 108 BPM with four-on-floor = Perfect for Deep Focus Block 1

### Energy Requirements by Time Block

**Morning Warmup** (Gentle awakening):
- **BPM**: 92-102
- **Energy approach**: Gentle, inviting, non-demanding
- **Good influences**: Vince Guaraldi jazz piano, acoustic folk, bossa nova, lo-fi
- **Tested influences**: Bluegrass/Appalachian (banjo, dulcimer) create pleasant morning energy alongside jazz and bossa nova variations
- **Avoid**: Aggressive rhythms, dramatic builds, very slow ambient (too sleepy)

**Deep Focus Block 1** (Building flow, fresh energy):
- **BPM**: 95-112
- **Energy approach**: Forward momentum, purposeful but not aggressive
- **Good influences**: West Coast jazz, Debussy impressionism, chamber music, Japanese koto, acoustic-electronic hybrids
- **Avoid**: Very slow nocturnes alone (unless energized with faster BPM/percussion), overly relaxing field recordings

**Deep Focus Block 2** (Fighting fatigue, sustained drive):
- **BPM**: 96-108 (sweet spot - not too slow, not too fast)
- **Energy approach**: Rhythmic drive, sustained energy, hypnotic but not sleepy
- **Good influences**: Afro-house, tropical house, mbira trance, tabla rhythms, Donald Fagen sophistication, polyrhythms
- **Avoid**: Chopin nocturnes (night music), pure ambient drones, very minimal textures, sleepy field recordings alone
- **⚠️ User feedback**: 112+ BPM feels too fast for sustained focus; creates jarring transitions when dropping back to ~96 BPM

**Midday Refresh** (Re-energize):
- **BPM**: 108-122
- **Energy approach**: Lift energy, refresh focus, inject vitality
- **Good influences**: Swing rhythms, tropical house, samba, saxophone textures, upbeat jazz
- **Avoid**: Sleepy ambient, nocturnes, very slow tempos

**Evening Wind Down** (Release, relax):
- **BPM**: 85-95
- **Energy approach**: Gentle release, theta dominance, prepare for rest
- **Good influences**: Chopin nocturnes (perfect here!), Ryuichi Sakamoto ambient, field recordings, ambient drones, nay flute
- **Avoid**: Four-on-floor kicks, polyrhythms, energizing percussion

### How to Apply

When generating prompts:

1. **Check time block context**: What energy level does the user need at this point in their day?
2. **Select base influences**: Choose influences appropriate for that energy level
3. **Adjust via BPM**: Slower = more relaxing, faster = more energizing (within brainwave target range)
4. **Add rhythmic drive**: Four-on-floor, percussion, polyrhythms increase energy
5. **Balance textures**: Soft pads + gentle rhythms = moderate energy; drones alone = very low energy

**Remember**: The same influence (like piano) can be energizing OR relaxing depending on context. Nocturnes are "night music"—reserve for low-energy blocks or energize them significantly for use elsewhere.

### 🧠 Critical: Influences vs. Prompts (Neuroscience Focus)

**KEY PRINCIPLE**: Influences are ingredients; prompts apply neuroscience.

**Influences** = Raw sonic possibilities, flavor palette, diverse textures
**Prompts** = Neuroscience application extracting what supports brain states

**The prompt does the heavy lifting**, not the influence. Keep influence diversity high (prevents monotony), but ensure every prompt applies research-backed mechanisms.

#### Neuroscience-Valid Prompt Requirements

Every prompt must specify:

1. **Brainwave Entrainment**
   - BPM matched to target: Theta (60-80), Alpha (80-120), Theta-Alpha (80-110)
   - Steady tempo (not variable)
   - Rhythmic foundation (entrains brainwaves)

2. **Cognitive Load Minimization**
   - Repetitive patterns (predictable, low processing demand)
   - Instrumental only (no language interference)
   - Background texture (not foreground melody/hooks)
   - Avoid earworms and attention capture

3. **Habituation Prevention**
   - Polyrhythmic complexity (engaging without demanding)
   - Subtle variation (not dramatic development)
   - Layered textures (complexity without chaos)

4. **Arousal Modulation**
   - Steady energy (avoid dramatic builds/drops)
   - Strip emotional content (use technique, not mood)
   - Moderate arousal (not euphoric, not sleepy)

5. **Research-Backed Elements**
   - Field recordings (biophilic design - proven)
   - Sub bass (physical grounding)
   - Modal scales (avoid emotional associations)
   - Jazz harmony (theta-gamma coupling - theoretical)
   - Swing quantization (habituation prevention)

#### Example: Extracting Neuroscience from Any Influence

**Influence**: "Euphoric Dance/Pop" (emotional, high-arousal)

❌ **Wrong** (emotion-driven):
```
"Euphoric piano house creates celebratory energy at 128 BPM with
uplifting chords and empowering builds for morning motivation."
```
Problems: Too fast (stress response), emotional engagement, builds demand attention

✅ **Right** (neuroscience-driven):
```
"Piano stabs provide harmonic texture at 96 BPM, extracted from house
tradition but stripped of euphoric elements. Repetitive four-on-floor
entrains theta-alpha brainwaves while chord voicings remain background
texture. Field recordings add biophilic grounding—using production
techniques for entrainment without emotional engagement."
```
Mechanisms: Tempo entrainment (96 BPM), emotional stripping, biophilic design, predictable patterns

**This approach**:
- ✅ Preserves influence diversity (prevents monotony)
- ✅ Ensures neuroscience validity (research-backed mechanisms)
- ✅ Separates "what sounds good" from "what supports brain states"

### ⚠️ Anti-Pattern: Emotional/Reflective Music in High-Energy Blocks

**User feedback** (Prompts 95, 99, 100): These were "musically good but wrong energy level for Deep Focus Block 2"

**Common attributes that make music too low-energy for Block 2**:

1. **Emotional/reflective quality**: Music designed for introspection or emotional resonance
   - Keywords: "wistful," "nostalgic," "romantic," "contemplative," "emotional restraint"
   - Examples: Chopin nocturnes, anime soundtracks, Ryuichi Sakamoto minimalism

2. **Emphasis on space/silence**: Generous space rather than rhythmic density
   - "Silence as element," "generous space," "restrained"
   - Field recordings dominant, minimal percussion
   - Chamber music intimacy vs. rhythmic drive

3. **Introspective intent**: Designed for passive reflection, not active sustained focus
   - "Study music" aesthetic = moderate energy, not high
   - "Meditative," "contemplative" = theta dominance, not theta-alpha balance
   - Night music (nocturnes) = preparation for sleep, not fighting fatigue

4. **Classical/acoustic heritage with emotional depth**:
   - Western classical (Chopin, chamber music, solo piano)
   - Japanese traditional (koto, Sakamoto)
   - Orchestral anime soundtracks
   - When these dominate without rhythmic foundation = too introspective for Block 2

**The fix**: These influences work beautifully in:
- **Morning Warmup** (gentle awakening with beauty)
- **Deep Focus Block 1** (fresh energy, can sustain with emotional depth)
- **Evening Wind Down** (perfect for release and reflection)

**For Block 2**, you need:
- **Rhythmic foundation**: Four-on-floor, tabla, polyrhythms, percussion
- **Hypnotic but energizing**: Mbira trance, afro-house, tropical house
- **Sophistication without introspection**: Donald Fagen production, West Coast jazz, jazz-rock
- **Minimal emotional content**: Textures and grooves over melodies and feelings

## Mutation Ideas: Influences Library

**The mutation ideas are now managed in a dedicated database**: `influences_library.csv`

This library contains 46 curated musical influences organized into 5 categories:
- **Acoustic Instruments** (14) - Dulcimer, harp, sitar, EBow guitar, etc.
- **Electronic Effects** (9) - Dub delay, Mellotron, granular synthesis, etc.
- **Rhythmic Elements** (6) - Swing, polyrhythms, odd time signatures, etc.
- **Textures** (7) - Field recordings, harmonic drones, melodic percussion, etc.
- **Genre Influences** (10) - Krautrock, space music, Balearic beat, etc.

Each influence includes:
- **Elements_To_Use**: What to incorporate for optimal brain stimulation
- **Elements_To_Avoid**: What destroys the focus-enhancement effect
- **Adaptation_Notes**: How to apply the influence to programming music
- **Status**: Unexplored → Tested → Proven/Avoid (tracks what works)

### Using the Influences Library

Use the **`influence-manage` skill** to browse and search mutations:

```bash
# Find mutation ideas by category
influence-manage --list --category "Acoustic Instruments"
influence-manage --list --category "Electronic Effects"

# Find unexplored mutations (fresh DNA)
influence-manage --list --status "Unexplored"

# Search for specific sonic qualities
influence-manage --search "gentle"     # For theta-inducing morning warmup
influence-manage --search "alert"      # For midday refresh
influence-manage --search "harmonic"   # For deep focus

# Find proven mutations that worked before
influence-manage --list --status "Proven"

# Show detailed guidance for a specific influence
influence-manage --show 12  # e.g., Sitar details
```

### Workflow: Generating Mutations

1. **Before generating prompts**: Browse influences library for mutation candidates
2. **Select appropriate influences**: Match the time block's purpose (e.g., theta-inducing, focus-enhancing)
3. **Apply following adaptation notes**: Use "Elements_To_Use", avoid "Elements_To_Avoid"
4. **After testing in Suno**: Mark influence as used and update status based on user ratings

See the `influence-manage` skill documentation for complete usage examples.

## Files used

- `scripts/generate_prompts.py` - Generation script (embedded in this skill)
- `scripts/csv_utils.py` - CSV utilities (embedded in this skill)
- `../../../../programming_music_prompts.csv` - Data source (project root)

## Related skills

- Use `prompt-find` to identify parent candidates
- Use `prompt-show` to analyze parent prompts
- Use `prompt-rate` to rate generated prompts after testing
- Use `prompt-stats` to track library growth

## Current Status

⚠️ **Note**: The generation script currently provides:
- Interactive wizard to plan generation
- Parent candidate identification
- Time block listing
- Documentation of the process

Actual prompt creation is still done manually by following the genetic algorithm principles. Future enhancement: automate prompt generation using templates and combinatorial logic.
