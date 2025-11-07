# CSV Schema Reference

## File Location

`programming_music_prompts.csv` (70 prompts + 1 header row = 71 total lines)

---

## Column Definitions

### 1. Prompt_ID
**Type**: String
**Format**: Numeric (1-66) or "BONUS-N"
**Example**: `28`, `BONUS-1`

### 2. Time_Block
**Type**: String
**Values**:
- "Morning Warmup"
- "Deep Focus Block 1"
- "Midday Refresh"
- "Deep Focus Block 2"
- "Late Afternoon Push"
- "Evening Wind-Down"
- Special: "Complex Debugging", "Creative Algorithm Design", etc.

### 3. BPM
**Type**: Integer
**Range**: 75-122
**Example**: `106`

### 4. Brain_Wave_Target
**Type**: String
**Values**:
- "Theta-Gamma Coupling"
- "Alpha Boost"
- "Theta-Alpha Transition"
- "Beta Suppression + Alpha"
- "Alpha to Theta Descent"
- "Sustained Theta-Alpha"
- Special: "Gamma Bursts", "Alpha + Divergent Thinking", etc.

### 5. Duration_Type
**Type**: String
**Values**:
- "Gentle Entry"
- "Hypnotic Flow"
- "Novelty Refresh"
- "Extended Immersion"
- "Fatigue Combat"
- "Parasympathetic Shift"
- Special: "Problem Solving", "Creative Exploration", etc.

### 6. Primary_Genres
**Type**: Quoted string, comma-separated
**Example**: `"chillsynth, minimal techno"`
**Note**: CSV field is quoted to handle internal commas

### 7. Key_Instruments
**Type**: Quoted string, comma-separated
**Example**: `"TB-303 bass, electric piano, minimal percussion, analog pads"`
**Note**: CSV field is quoted to handle internal commas

### 8. Mood_Keywords
**Type**: String, space-separated
**Example**: `acid jazz hypnotic architectural precision`
**Note**: No commas in this field (uses spaces)

### 9. Suno_Short_Prompt
**Type**: Quoted string
**Format**: Condensed version for Suno Styles field
**Example**: `"chillsynth, minimal techno, TB-303 bass, electric piano, minimal percussion, analog pads, 106 BPM, instrumental"`
**Usage**: Copy/paste directly into Suno's Styles textarea

### 10. Full_Prompt
**Type**: Quoted string (long text)
**Format**: Detailed neurological description (2-3 sentences)
**Example**: `"Warm TB-303 bass synth pulses with hypnotic precision beneath electric piano chord stabs at 106 BPM, supported by minimal percussion and thick analog synthesizer pads in this chillsynth minimal techno fusion. The arrangement breathes with spacious restraint—acid jazz architecture for deep work, where repetitive cycles induce theta-gamma coupling through predictable sonic geometry."`
**Usage**: Documentation only (not used in Suno generation)

### 11. Notes
**Type**: String
**Format**: Genetic lineage or special notes
**Examples**:
- `"Based on Prompt #5 formula"`
- `"Hybrid: #13 + tape delay mutation"`
- `"Parent #13 clone (proven DNA)"`
- `"Mutation: mellotron + dub (Prompt #5 DNA)"`

### 12. Generated
**Type**: String
**Values**: `"Yes"` or empty
**Purpose**: Track which prompts have been created in Suno
**Current status**: All 70 prompts = "Yes"

### 13. Suno_Refined
**Type**: String (reserved for future use)
**Purpose**: Store Suno's auto-generated refinements
**Current status**: Empty (not used yet)

### 14. Rating
**Type**: String
**Format**: Free text with optional ⭐
**Examples**:
- `"Excellent ⭐"`
- `"Excellent for midday refresh ⭐"`
- `"Excellent - sax texture perfect for midday refresh! ⭐"`
- Empty (not yet rated)

---

## Working with the CSV

### Reading Examples

**Count total prompts:**
```bash
wc -l programming_music_prompts.csv
# Output: 71 (header + 70 prompts)
```

**Find specific prompt:**
```bash
grep "^40," programming_music_prompts.csv
```

**Count generated prompts:**
```bash
grep ",Yes," programming_music_prompts.csv | wc -l
# Output: 70
```

**Find excellent prompts:**
```bash
grep "⭐" programming_music_prompts.csv
```

**Extract all BPMs:**
```bash
awk -F',' 'NR>1 {print $3}' programming_music_prompts.csv | sort -n
```

**Find prompts by time block:**
```bash
grep "Midday Refresh" programming_music_prompts.csv
```

**Find prompts with specific instrument:**
```bash
grep -i "saxophone" programming_music_prompts.csv
```

---

## Updating the CSV

### ⚠️ Always Use Python csv Module

**Why**: The CSV contains quoted fields with internal commas. Simple text manipulation breaks the quoting.

**Wrong**:
```bash
# DON'T DO THIS - breaks quoting
sed -i 's/old/new/' programming_music_prompts.csv
awk -F',' '{...}' programming_music_prompts.csv
```

**Correct**:
```bash
source venv/bin/activate
python << 'EOF'
import csv

with open('programming_music_prompts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Make your changes to rows here
for row in rows:
    if row['Prompt_ID'] == '40':
        row['Rating'] = 'Excellent ⭐'

with open('programming_music_prompts.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
EOF
deactivate
```

---

## Common Field Combinations

### For Suno Generation
Use columns: `Suno_Short_Prompt` (Styles field) + `Prompt_ID` + `Time_Block` (Title field)

### For Analysis
Use columns: `BPM` + `Brain_Wave_Target` + `Primary_Genres` + `Rating`

### For Documentation
Use columns: `Full_Prompt` + `Notes` + `Mood_Keywords`

### For Genetic Tracking
Use columns: `Prompt_ID` + `Notes` + `Rating`

---

## Data Integrity Checks

```bash
# Should be 71 (header + 70 prompts)
wc -l programming_music_prompts.csv

# Should be 70 (all generated)
grep ",Yes," programming_music_prompts.csv | wc -l

# Should have no empty Prompt_ID fields
awk -F',' 'NR>1 && $1=="" {print "ERROR: Empty Prompt_ID on line " NR}' programming_music_prompts.csv

# Check for duplicate IDs
awk -F',' 'NR>1 {print $1}' programming_music_prompts.csv | sort | uniq -d
```

---

## Future Enhancements

### Potential New Columns

1. **Suno_URL**: Direct link to generated song
2. **Best_Version**: Which of 2 versions to keep (1 or 2)
3. **Generated_Date**: Timestamp of generation
4. **Credits_Used**: Track cost per prompt
5. **Play_Count**: User listening frequency
6. **Context_Tags**: "morning", "debugging", "creative", etc.

### Potential Analysis Columns

1. **Effective_Rating**: 1-5 numeric scale
2. **Energy_Level**: 1-5 (perceived energy)
3. **Focus_Score**: 1-5 (effectiveness for focus)
4. **Habituation_Rate**: How quickly it becomes boring
