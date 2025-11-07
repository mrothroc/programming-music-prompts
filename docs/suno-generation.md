# Suno Generation Guide

## Quick Start

See detailed workflow in: **`../CRITICAL-GENERATION-WORKFLOW.md`**

## Essential Requirements

### ✅ Use Custom Mode (NOT Simple Mode)

Simple mode has issues:
- Instrumental toggle clears the description field
- Less control over generation parameters
- Single field for both lyrics and style

### ✅ Fill BOTH Fields

1. **Styles Field** (Primary field)
   - Copy from CSV column: `Suno_Short_Prompt`
   - Format: `[genres], [instruments], [BPM] BPM, instrumental`
   - Example: `"chillsynth, minimal techno, TB-303 bass, electric piano, minimal percussion, analog pads, 106 BPM, instrumental"`

2. **Title Field** (Below "Advanced Options")
   - Format: `[Time Block]: Prompt [ID]`
   - Example: `"Deep Focus Block 1: Prompt 28"`
   - ⚠️ **CRITICAL**: Do NOT skip this field or song will be "Untitled"

### ✅ Wait for Validation

After filling fields, wait 500ms for React to process and enable Create button.

### ✅ Click Create

Button should now be enabled (not grayed out).

---

## Common Mistakes

### ❌ Mistake #1: Filling Only Styles Field
**Result**: Song created as "Untitled"
**Fix**: ALWAYS fill both Styles AND Title fields

### ❌ Mistake #2: Using Simple Mode
**Result**: Instrumental toggle clears your description
**Fix**: Use Custom mode exclusively

### ❌ Mistake #3: Not Waiting for Validation
**Result**: Create button stays disabled
**Fix**: Wait 500ms after filling fields, or take fresh snapshot

---

## Workflow Steps

1. Navigate to Create page → Custom tab
2. Leave Lyrics field blank (for instrumental)
3. Fill Styles field with CSV `Suno_Short_Prompt` value
4. Fill Title field with `[Time Block]: Prompt [ID]`
5. Wait 500ms for validation
6. Click Create button
7. Wait ~2-3 minutes for generation
8. Review 2 versions, keep best one
9. Mark CSV row as `Generated=Yes`
10. Add rating if excellent

---

## Quality Expectations

### Normal Variance

Suno generates **2 versions per prompt**. Quality varies:
- **Expected**: 1 excellent + 1 mediocre
- **Good luck**: 2 excellent versions
- **Bad luck**: 2 mediocre versions (rare)

**This is normal behavior** - keep the best, delete/ignore the rest.

### When to Re-generate

Re-generate if:
- Both versions are poor quality
- Neither captures the intended mood
- Technical issues (clipping, glitches)

Don't re-generate just because one version is weak - that's expected.

---

## Technical Details

### UI Automation (Optional)

If using Chrome DevTools MCP for automation:
- See: `../suno-automation-custom-mode.md`
- See: `../suno-automation-findings.md`

Key points:
- UIDs become stale after DOM modifications
- Always take fresh snapshot after filling form fields
- React validation takes ~500ms

### Credits Tracking

- Cost: ~10 credits per song
- Each prompt generates 2 songs = ~20 credits per prompt
- 70 prompts × 20 credits = ~1,400 credits total
- Check remaining credits in sidebar: `X,XXX Credits`

---

## Renaming Songs (If Title Was Forgotten)

If you created songs as "Untitled", see renaming workflow in:
**`../CRITICAL-GENERATION-WORKFLOW.md`** (Section: "Renaming Songs Workflow")

Key steps:
1. Use JavaScript `evaluate_script()` to click Edit button (MCP click times out)
2. Select existing text with `Control+A`
3. Fill new title
4. Click Save

---

## Post-Generation

### Update CSV
```bash
# Mark as generated (use Python csv module)
source venv/bin/activate
python << 'EOF'
import csv
with open('programming_music_prompts.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
for row in rows:
    if row['Prompt_ID'] == '40':
        row['Generated'] = 'Yes'
with open('programming_music_prompts.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
EOF
deactivate
```

### Add Rating (If Excellent)
```bash
# Add rating for excellent prompts
python << 'EOF'
import csv
with open('programming_music_prompts.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
for row in rows:
    if row['Prompt_ID'] == '40':
        row['Rating'] = 'Excellent for midday refresh ⭐'
with open('programming_music_prompts.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)
EOF
```

---

## Verification Checklist

Before clicking Create:
- [ ] In Custom mode (not Simple)
- [ ] Styles field filled
- [ ] Title field filled ⚠️ CRITICAL
- [ ] Advanced Options section visible (Title is below it)
- [ ] Create button is enabled (not disabled)
- [ ] Correct workspace selected (e.g., "Work Music")

---

For complete step-by-step instructions with screenshots and technical details, see:
- **`../CRITICAL-GENERATION-WORKFLOW.md`** (User workflow)
- **`../suno-automation-custom-mode.md`** (Technical automation)
- **`../suno-automation-findings.md`** (Testing lessons learned)
