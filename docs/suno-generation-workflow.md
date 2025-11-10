# CRITICAL: Complete Song Generation Workflow

**Last Updated:** 2025-11-06
**Status:** ✅ VERIFIED - This is the CORRECT workflow

---

## ⚠️ CRITICAL MISTAKE TO AVOID

**DO NOT** generate songs without filling the Title field!

### What I Did Wrong (BONUS-1)
- Only filled the Styles field
- Forgot to fill the Title field
- Result: 2 songs created as "Untitled"

### What I Must Do (BONUS-2, 3, 4 and ALL future generations)
- Fill BOTH the Styles field AND the Title field
- Title field is located BELOW the "Advanced Options" section
- Wait for validation BEFORE clicking Create

---

## Complete Generation Workflow (Custom Mode)

### Step 1: Ensure You're in Custom Mode
```javascript
// Should already be on Create page in Custom mode
// Verify by looking for Styles textarea with placeholder "indie, electronic, synths"
```

### Step 2: Fill Styles Field (PRIMARY FIELD)
**Element**: Textarea with placeholder containing "indie, electronic, synths"

**Format**: `[genres], [instruments], [BPM] BPM, instrumental`

**Example**:
```javascript
fill(styles_uid, "psychedelic jazz, samba fusion, phased percussion, wah guitar, analog synth, samba drums, 100 BPM, instrumental");
```

### Step 3: Fill Title Field ⚠️ CRITICAL - DO NOT SKIP
**Element**: Input field with placeholder "Song Title (Optional)"
**Location**: BELOW the "Advanced Options" expandable section

**Format**: `BONUS: [Descriptive Title]`

**Example**:
```javascript
fill(title_uid, "BONUS: Creative Algorithm Design");
```

### Step 4: Wait for Validation
```javascript
// Wait 500ms for React to process and enable Create button
await new Promise(resolve => setTimeout(resolve, 500));
```

### Step 5: Click Create Button
```javascript
click(create_button_uid); // aria-label="Create song"
```

### Step 6: Wait for Submission
```javascript
// Wait 3 seconds for generation to start
await new Promise(resolve => setTimeout(resolve, 3000));
```

---

## Complete MCP Operation Sequence

```javascript
// 1. Take snapshot to get current UIDs
take_snapshot();

// 2. Fill Styles field
fill(uid=[STYLES_UID], "[genres], [instruments], [BPM] BPM, instrumental");

// 3. Fill Title field ⚠️ CRITICAL
fill(uid=[TITLE_UID], "BONUS: [Title]");

// 4. Wait for validation
// (MCP doesn't have async wait, but button should enable quickly)

// 5. Take fresh snapshot to get updated Create button state
take_snapshot();

// 6. Click Create button
click(uid=[CREATE_BUTTON_UID]);

// 7. Take snapshot to verify submission
take_snapshot();
```

---

## Renaming Songs Workflow (When Title Was Forgotten)

### Problem
- MCP `click()` on Edit title button times out
- Solution: Use JavaScript `evaluate_script` instead

### Step 1: Find and Click Edit Button (JavaScript)
```javascript
evaluate_script({
  function: `() => {
    const rows = document.querySelectorAll('[role="row"]');
    const targetRow = Array.from(rows).find(row =>
      row.textContent.includes('Untitled') &&
      row.textContent.includes('[unique text from song description]')
    );

    if (targetRow) {
      const editButton = Array.from(targetRow.querySelectorAll('button')).find(btn =>
        btn.textContent.trim() === 'Edit title'
      );

      if (editButton) {
        editButton.click();
        return { success: true, message: 'Edit mode activated' };
      }
    }

    return { success: false, message: 'Could not find Edit button' };
  }`
});
```

### Step 2: Select Existing Text
```javascript
press_key("Control+A");
```

### Step 3: Take Snapshot to Find Title Input UID
```javascript
take_snapshot();
// Look for textbox in edit mode
```

### Step 4: Fill New Title
```javascript
fill(uid=[TITLE_INPUT_UID], "BONUS: [Correct Title]");
```

### Step 5: Click Save Title Button
```javascript
click(uid=[SAVE_BUTTON_UID]); // Button with text "Save title"
```

---

## BONUS Prompt Specifications

### BONUS-1: Complex Debugging ✅ GENERATED (1 renamed, 1 needs renaming)
- **Styles**: `math rock, afro jazz fusion, kora, electric guitar, talking drums, 115 BPM, instrumental`
- **Title**: `BONUS: Complex Debugging`
- **Status**: Generated without title, 1/2 renamed

### BONUS-2: Creative Algorithm Design ✅ GENERATION SUBMITTED
- **Styles**: `psychedelic jazz, samba fusion, phased percussion, wah guitar, analog synth, samba drums, 100 BPM, instrumental`
- **Title**: `BONUS: Creative Algorithm Design`
- **Status**: Generated WITH title (correct workflow)

### BONUS-3: Refactoring/Cleanup (PENDING)
- **Styles**: `minimalist acoustic folk, meditation, solo fingerstyle guitar, room ambience, 75 BPM, instrumental`
- **Title**: `BONUS: Refactoring/Cleanup`
- **Status**: Not yet generated

### BONUS-4: Late Night Crunch (PENDING)
- **Styles**: `dark chillsynth, boom bap, minor-key synth bass, lo-fi drums, moody Rhodes, tape hiss, 88 BPM, instrumental`
- **Title**: `BONUS: Late Night Crunch`
- **Status**: Not yet generated

---

## Verification Checklist

Before clicking Create, verify:
- [ ] Styles field is filled
- [ ] Title field is filled ⚠️ CRITICAL
- [ ] Advanced Options section is visible (Title field is below it)
- [ ] Create button is enabled (not disabled)
- [ ] Correct workspace selected (Work Music)

---

## Key UI Elements (Custom Mode)

| Element | Typical UID Pattern | Description |
|---------|---------------------|-------------|
| Styles textarea | `*_60` | Primary field for genre/instruments/BPM |
| Title input | `*_88` | Below Advanced Options - MUST FILL |
| Create button | `*_92` | aria-label="Create song" |
| Edit title button | `*_103` (varies) | In song row, MCP click times out |
| Save title button | Varies | Appears when in edit mode |

---

## Credits Tracking

- Starting credits: 2,230
- After BONUS-1 (2 songs): 2,190
- Cost per generation: ~20 credits/song (40 for 2 versions)
- Remaining generations: 2 (BONUS-3, BONUS-4)
- Expected cost: 80 credits
- Expected remaining: 2,110 credits

---

**REMEMBER**: Always fill BOTH Styles AND Title fields. No exceptions!
