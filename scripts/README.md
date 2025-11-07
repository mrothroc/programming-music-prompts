# CSV Utility Scripts

Safe Python utilities for managing `programming_music_prompts.csv`.

**Why these exist**: The CSV has quoted fields with internal commas. Using sed/awk/grep for modifications breaks the quoting. These scripts use Python's csv module for safe operations.

---

## Setup

All scripts use the project's virtual environment:

```bash
source ../venv/bin/activate
```

---

## Available Scripts

### 1. `stats.py` - View Statistics

Show overall statistics about the prompt library.

```bash
python stats.py
```

**Output**:
```
📊 PROMPT LIBRARY STATISTICS
  Total prompts:       70
  Generated:           70 (100.0%)
  Rated:               4 (5.7%)
  Excellent (⭐):       4

📁 By Time Block:
  Morning Warmup                  7
  Deep Focus Block 1             14
  Midday Refresh                  6
  ...
```

---

### 2. `show_prompt.py` - View Prompt Details

Show details for a specific prompt.

```bash
# Basic info
python show_prompt.py 40

# Full details (includes Suno prompt and full description)
python show_prompt.py 40 --verbose
```

**Output**:
```
============================================================
Prompt 40: Midday Refresh
============================================================
BPM: 98 | Alpha Boost
Genres: "deep house, bossa nova"
Instruments: "four-on-floor, nylon guitar, Rhodes, swing quantization"

Notes: Mutation: swing quantization (Prompt #13 DNA)
Generated: Yes
Rating: Excellent for midday refresh ⭐
```

---

### 3. `mark_generated.py` - Mark as Generated

Mark prompts as generated in Suno.

```bash
# Single prompt
python mark_generated.py 40

# Multiple prompts
python mark_generated.py 40 41 42

# All prompts
python mark_generated.py --all
```

---

### 4. `add_rating.py` - Add Rating

Add or update rating for a prompt.

```bash
python add_rating.py 40 "Excellent ⭐"
python add_rating.py 41 "Excellent - sax texture perfect for midday refresh! ⭐"
```

---

### 5. `find_prompts.py` - Search & Filter

Find prompts by various criteria.

```bash
# By time block
python find_prompts.py --time-block "Midday Refresh"

# By BPM
python find_prompts.py --bpm 108

# Generated prompts
python find_prompts.py --generated yes

# Not generated yet
python find_prompts.py --generated no

# Rated prompts
python find_prompts.py --rated yes

# Not rated yet
python find_prompts.py --rated no

# Excellent prompts only
python find_prompts.py --excellent

# Search text in any field
python find_prompts.py --search "saxophone"
python find_prompts.py --search "mellotron"
python find_prompts.py --search "dub delay"
```

**Output**:
```
✅ Found 2 prompt(s):

      40 | Midday Refresh                 | BPM  98 | "deep house, bossa nova"
         └─ Excellent for midday refresh ⭐
      41 | Midday Refresh                 | BPM 105 | "chillwave, boom bap"
         └─ Excellent - sax texture perfect for midday refresh! ⭐
```

---

## Using csv_utils.py Directly

For custom operations, import the utility module:

```python
from csv_utils import (
    read_prompts,
    write_prompts,
    get_prompt,
    update_prompt,
    find_prompts,
    search_prompts,
    get_stats
)

# Example: Find all prompts with mellotron
prompts = search_prompts("mellotron", fields=["Key_Instruments"])
for p in prompts:
    print(f"Prompt {p['Prompt_ID']}: {p['Primary_Genres']}")

# Example: Bulk update
prompts = read_prompts()
for prompt in prompts:
    if prompt['Time_Block'] == 'Midday Refresh':
        prompt['Notes'] += ' [high-energy variant]'
write_prompts(prompts)
```

---

## Common Workflows

### After generating prompts in Suno

```bash
# Mark as generated
python mark_generated.py 40 41 42

# Add ratings for excellent ones
python add_rating.py 40 "Excellent for midday refresh ⭐"
python add_rating.py 41 "Excellent - sax texture perfect! ⭐"

# Check progress
python stats.py
```

### Find prompts to test

```bash
# Find prompts with new mutations not yet rated
python find_prompts.py --search "mellotron"
python find_prompts.py --search "EBow"
python find_prompts.py --search "dub delay"

# Find all generated but unrated prompts
python find_prompts.py --rated no
```

### Analysis

```bash
# Find all excellent prompts
python find_prompts.py --excellent

# Find prompts in specific BPM range
python find_prompts.py --bpm 108
python find_prompts.py --bpm 115

# Find all prompts in a time block
python find_prompts.py --time-block "Deep Focus Block 1"
```

---

## Safety Features

- ✅ All scripts use Python's csv module (handles quoted fields correctly)
- ✅ Atomic writes (reads full file, modifies in memory, writes back)
- ✅ Validation (checks prompt exists before updating)
- ✅ Clear error messages
- ❌ No sed/awk/grep for modifications (read-only grep is fine)

---

## Adding New Scripts

When creating new utilities:

1. Import from `csv_utils.py`
2. Use `read_prompts()` and `write_prompts()`
3. Never manually parse CSV with split/regex
4. Add docstring with usage examples
5. Update this README

---

## Troubleshooting

**ImportError: No module named 'csv_utils'**
- Make sure you're running from the `scripts/` directory
- Or add parent directory to path: `sys.path.insert(0, '..')`

**CSV file not found**
- Scripts expect to be run from `scripts/` directory
- Or set `CSV_PATH` environment variable

**Changes not saving**
- Check file permissions
- Make sure venv is activated
- Check for error messages in script output
