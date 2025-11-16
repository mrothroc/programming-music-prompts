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

## 🎯 Core Principle: Avoid "AI Slop" Convergence

Like generic UI design (Inter fonts, purple gradients), music prompts naturally converge toward "on-distribution" outputs—the same safe combinations that dominate training data. Without active intervention, you'll generate generic ambient/lo-fi with piano, guitar, and synth pads.

**Fight distributional convergence. Make creative, distinctive prompts that surprise and delight.**

### Focus on Distinctiveness

**Instrumentation**: Choose beautiful, unique, and interesting instruments. Avoid overused defaults (generic synth pads, simple piano, basic guitar). Opt instead for distinctive choices that elevate the music's character:
- ✅ Balafon, mbira, bansuri flute, autoharp, Debussy-style piano techniques
- ✅ Wordless vocals as texture, chorus-drenched guitar pads, talking drums
- ✅ Jazz clarinet (Benny Goodman-style), vibraphone, Indian tabla
- ❌ "Synth pads," "ambient piano," "soft guitar" (too generic)

**Genre & Theme**: Commit to a cohesive, specific aesthetic. Dominant characteristics with sharp contrasts outperform timid, evenly-distributed descriptions. Reference specific artists/movements for clarity:
- ✅ "Steely Dan-inspired Fender Rhodes voicings with studio perfection"
- ✅ "The Cure-style chorus-drenched guitar pads"
- ✅ "Debussy-inspired impressionist piano with whole-tone scales"
- ❌ "Ambient electronic music" (lacks distinctive character)

**Temporal Character**: Use vivid descriptions of HOW rhythm works. One well-orchestrated rhythmic concept creates more interest than scattered generic descriptions:
- ✅ "Ritual precision," "cascading arpeggios," "polyrhythmic layers," "tremolo shimmer"
- ✅ "Four-on-floor pulse with talking drum polyrhythms"
- ✅ "Hypnotic repetitive patterns in trance-inducing cycles"
- ❌ "Steady beat," "rhythmic pattern" (lacks specificity)

**Textural Depth**: Create atmosphere through layered, specific techniques rather than defaulting to vague descriptors:
- ✅ "Chorus effect creating spatial depth," "whole-tone scales creating aquatic textures"
- ✅ "Metallic shimmer from mbira polyrhythmic layers"
- ✅ "Woody resonance with subtle vibrato, gentle swing phrasing"
- ❌ "Atmospheric," "ambient," "textural" (too generic)

### Avoid Generic "Focus Music" Aesthetics

- **Overused instruments**: Generic synth pads, simple piano, basic acoustic guitar without specific technique
- **Clichéd combinations**: Piano + rain sounds, lo-fi beats, generic ambient drones
- **Predictable patterns**: "Soft melody over gentle rhythm" without distinctive character
- **Cookie-cutter descriptions**: Lacking artist references, specific techniques, or contextual detail

### Critical: You Still Converge on Common Choices

Even with the genetic algorithm, you tend to reuse Rhodes, vibraphone, and tabla across generations. The 50/30/20 split provides structure, but **YOU must push for genuine distinctiveness within each type**:

- **Clones (50%)**: Don't just copy—change ONE distinctive element (different technique, reference artist, or textural approach)
- **Hybrids (30%)**: Create genuinely NEW combinations, not just "parent A's instruments + parent B's instruments in sequence"
- **Mutations (20%)**: CENTER the new influence as PRIMARY element, not just accent

**Interpret creatively.** Make unexpected choices that feel genuinely designed for the neuroscience goal, not just "programming music." Vary instruments, aesthetics, and techniques dramatically across generations.

## Genetic Algorithm Strategy

### 50% Parent DNA (Proven Excellence)
Clone prompts that have been rated as excellent or very good:
- Preserve the exact formula that works
- Vary BPM slightly (±1-3 BPM)
- **Change ONE distinctive element** (technique, artist reference, or textural detail)
- Keep core instruments and genres

### 30% Hybrids (Cross-breeding)
Combine elements from two different parent prompts:
- Mix instruments from both parents
- Blend genres creatively
- Combine rhythmic patterns
- Create acoustic-electronic fusions
- **Write COMPLETELY NEW descriptions** that genuinely blend both parents

### 20% Mutations (New DNA)
Introduce new instruments or effects weighted by cross-block success:
- **70% weighted**: Prioritize influences that appear in highly-rated prompts from other time blocks
- **30% random**: Explore completely uncharted sonic territory for diversity
- Add unique textures (mellotron, EBow, steel pan, etc.)
- Try new rhythmic elements (swing, dub delay)
- Test unconventional combinations
- **CENTER mutation as PRIMARY element**, not accent

**Cross-block learning**: If vibraphone gets "excellent" in Midday Refresh, it's prioritized for mutations in other blocks that need similar energy.

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

## 🚨 CRITICAL: Synthesis Discipline (Prevent Lazy Copy-Paste)

**Problem**: It's tempting to copy a parent prompt, add a few words about the new influence, and call it done. This creates a library of nearly identical prompts that defeats the genetic diversity goal.

**The Script-LLM Hybrid Workflow**:

1. **Script outputs JSON plan** with:
   - Parent prompts (for reference)
   - Target BPM, genres, instruments
   - For mutations: `Elements_To_Use`, `Elements_To_Avoid` from influences library

2. **LLM (you) synthesizes the actual Full_Prompt** based on prompt type:

### For Parent Clones (50%)

**Goal**: Preserve proven formula with minor variation

✅ **Correct approach**:
```
1. Copy parent's Full_Prompt text
2. Adjust BPM (±1-3 BPM)
3. Optionally vary ONE small element (e.g., "brushed hi-hats" → "soft tambourine")
4. Keep everything else identical
```

❌ **Wrong approach**: Creating significant variations (that's what hybrids are for)

### For Hybrids (30%)

**Goal**: Genuinely blend two parent prompts' sonic characteristics

✅ **Correct approach**:
```
1. Read BOTH parent prompts completely
2. Write a COMPLETELY NEW prompt from scratch that:
   - Takes rhythmic foundation from Parent A
   - Takes harmonic texture from Parent B
   - Blends instrumentation (e.g., Parent A's guitar + Parent B's synth pads)
   - Creates a cohesive sonic identity (not a list of disparate elements)
3. DO NOT copy/paste text from either parent
```

❌ **Wrong approach**:
```
1. Copy Parent A's prompt
2. Add "with influences from Parent B" or similar lazy addition
3. Result: Parent A with a tacked-on mention of Parent B
```

**Real example of WRONG hybrid synthesis** (from Midday Refresh generation):
- Parent A: "Sophisticated West Coast jazz instrumentation meets tropical house production..."
- Parent B: "Sophisticated Latin jazz-meets-house creates uplifting midday energy..."
- Lazy hybrid: "Sophisticated West Coast jazz instrumentation meets tropical house production..." (nearly identical to Parent A)

**What the hybrid SHOULD have been**:
```
Blend West Coast jazz trumpet phrasing (Parent A) with Latin percussion
patterns (Parent B). Four-on-floor anchors the groove while congas and
timbales add syncopation. Fender Rhodes provides harmonic bed, referencing
both jazz tradition and house music warmth. The result is energizing but
sophisticated—uptempo Latin rhythm with cool West Coast restraint.
```

### For Mutations (20%)

**Goal**: Center the new influence while using parent as foundation

✅ **Correct approach**:
```
1. Read parent prompt to understand time block context
2. Read mutation's Elements_To_Use and Elements_To_Avoid
3. Write a COMPLETELY NEW prompt from scratch that:
   - Centers the mutation influence as the PRIMARY sonic element
   - Uses parent's BPM range, brainwave target, and energy level as context
   - Applies adaptation notes from influences library
   - Creates a distinct sonic identity around the mutation
4. DO NOT copy/paste text from parent
```

❌ **Wrong approach**:
```
1. Copy parent prompt
2. Add "featuring [mutation influence]" at the beginning or end
3. Result: Parent prompt with mutation mentioned but not centered
```

**Real example of WRONG mutation synthesis** (from Midday Refresh generation):
- Parent: "Sophisticated West Coast jazz instrumentation meets tropical house production..."
- Mutation: Surf rock (reverb texture, Dick Dale influence)
- Lazy mutation: "Sophisticated West Coast jazz instrumentation meets tropical house production with surf rock reverb textures..."

**What the mutation SHOULD have been**:
```
Dick Dale-inspired reverb drenches sustained organ chords, creating
shimmering texture without aggressive surf melody. Four-on-floor kick
grounds the reverb wash while crisp hi-hats add brightness. Spring reverb
and tremolo reference surf tradition, but slow harmonic pace (108 BPM)
prevents frenetic energy—textural depth for midday refresh without
distraction.
```

## 🚨 CRITICAL: Suno 1000 Character Limit

**Suno enforces a strict 1000 character maximum for the Full_Prompt field.**

This is a HARD LIMIT - prompts that exceed 1000 characters will be truncated or rejected.

### Writing Within the Limit

**Strategy**: Be concise and specific, not verbose and generic.

✅ **Good (specific, concise)**:
```
"Moog modular pads unfold in Klaus Schulze-inspired cathedral swells at 103 BPM,
their cosmic waves providing vast space beneath Wurlitzer loops with metronomic
precision. Roland TR-808 boom bap provides minimal pulse while Minimoog bass
drones create tectonic foundation—Berlin school ambition meeting hip-hop restraint
for theta-gamma coupling through spatial immensity."
```
Character count: ~385

❌ **Bad (verbose, exceeds limit)**:
```
Long-winded explanations of every technical detail, neuroscience mechanisms
spelled out repeatedly, redundant descriptions...
```

### Conciseness Techniques

1. **Cut neuroscience explanations** - Don't explain "tempo entrainment (103 BPM = theta-gamma coupling)" in every prompt
2. **Remove redundant phrases** - "creating textures that support flow states for deep work" can be "supporting flow states"
3. **Use em-dashes** - Connect ideas efficiently: "Rhodes filtered to sine purity—extreme low-pass removes attack"
4. **Artist/gear references over descriptions** - "Klaus Schulze-inspired" vs "cosmic ambient electronic textures"
5. **Prioritize sonic detail** - Cut philosophy, keep technique

**Target**: 600-900 characters for safety margin and editorial flexibility.

## Verification Checklist

After generating prompts, verify:

- [ ] **Character limit**: Each Full_Prompt is under 1000 characters (target: 600-900)
- [ ] **Clones**: Only BPM and one small element changed?
- [ ] **Hybrids**: Did I write a NEW prompt? Can I identify characteristics from BOTH parents?
- [ ] **Mutations**: Is the mutation the PRIMARY sonic element, not just mentioned?
- [ ] **Distinctness**: Do all prompts sound different when read aloud?
- [ ] **Time block fit**: Does each prompt match the energy level and brainwave target?
- [ ] **Diversity check**: Are more than 3 out of 5 prompts using the same parent or genre?
- [ ] **Positive language**: Describe what you WANT, not what you DON'T want (see below)

If any hybrids or mutations could be mistaken for simple clones, rewrite them following the correct approach above.

## 🚨 CRITICAL: Use Positive Language Only ("Pink Elephant" Problem)

**Problem**: Like image generators, Suno LLMs struggle with negative instructions. Saying "not bluegrass picking" primes the model to think about bluegrass picking.

**Wrong approach**:
```
"Mandolin creates tremolo at 96 BPM—not bluegrass picking, but sustained texture..."
```
Result: Suno focuses on "bluegrass picking" and generates bluegrass anyway.

**Right approach**:
```
"Mandolin creates gentle tremolo shimmer at 96 BPM through sustained single-note
technique that produces organic shimmer texture."
```
Result: Describes the desired technique without mentioning unwanted genres.

### How to Avoid Genre Associations:

When adapting instruments with strong genre associations:

**Don't mention the unwanted genre at all** - instead describe:
1. **Technique**: "tremolo on held notes," "slow glissandos," "sparse plucks"
2. **Texture**: "shimmering sustain," "smooth vocal-like slides," "metallic sparkle"
3. **Aesthetic**: "vintage folk-rock," "tropical warmth," "Hawaiian smoothness"
4. **Context**: "British folk-rock aesthetic" (shifts away from American bluegrass)

**Examples**:

❌ **Wrong** (mentions unwanted genre):
- "Mandolin tremolo, not fast bluegrass picking"
- "Steel drums without Caribbean clichés"
- "Banjo texture avoiding country twang"

✅ **Right** (describes desired outcome):
- "Mandolin sustained tremolo on held notes creates shimmering texture"
- "Steel drums provide gentle melodic shimmer through soft mallet technique"
- "Banjo fingerpicked arpeggios float through ambient space with sparse touches"

### Note on Suno_Refined Field:

The user only uses the **Full_Prompt** field for generation, not Suno_Refined. Therefore:
- Don't populate Suno_Refined with negative prompts
- Keep all instructions positive in Full_Prompt
- Suno_Refined should remain empty unless specifically requested

## 🚨 CRITICAL: Preventing Genetic Incest

**Problem**: Over-reliance on a single parent creates a library that lacks diversity.

**Warning signs**:
- Script shows "⚠️ WARNING: Only 1 parent found"
- More than 3 out of 5 prompts use the same genre/parent
- All mutations are variations of the same base (e.g., all bluegrass mutations)

**When you see this**:

1. **Check the parent pool**: How many rated prompts exist for this time block?
   - If only 1 parent: Expand by including "Pretty good" rated prompts
   - The script now includes "Pretty good" in parent search automatically

2. **Diversify your selections**:
   - **Clones**: If only 1 parent exists, clone it at most ONCE (20% not 50%)
   - **Hybrids**: Cross-breed with parents from OTHER time blocks that match the energy level
   - **Mutations**: Use mutations heavily (60-80% instead of 20%) to inject diversity

3. **Cross-time-block hybrids**:
   - Morning Warmup + Midday Refresh = Gentle energy boost
   - Deep Focus Block 1 + Deep Focus Block 2 = Extended flow variations
   - Late Afternoon Push can borrow from Midday Refresh (both energizing)

**Example fix for single-parent situation**:
```
Time block has only 1 "Very good" parent (#128 - bluegrass)

Instead of:
- 3 clones of #128 (genetic incest!)
- 1 hybrid #128 + something
- 1 mutation from #128

Do this:
- 1 clone of #128 (20%)
- 1 hybrid #128 + Midday Refresh parent (cross-block) (20%)
- 3 mutations with diverse influences (60%)
  - Lap steel (NOT bluegrass)
  - Nu-disco/funk texture
  - Electronic/synth-based
```

**Ask the user**: If the script warns about limited parents, ask whether to:
1. Proceed with mutation-heavy approach (60-80% mutations)
2. Cross-breed with other time blocks that match energy
3. Wait and rate more prompts first

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
