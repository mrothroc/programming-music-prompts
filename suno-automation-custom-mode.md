# Suno Custom Mode Automation Guide

**Date:** 2025-11-06
**Status:** ✅ Custom mode identified - preferred workflow
**Browser:** Chrome with DevTools MCP

---

## Overview

**Custom mode** provides more control than Simple mode and is the recommended approach for generating instrumental music with detailed style specifications.

### Custom Mode vs Simple Mode

| Feature | Simple Mode | Custom Mode |
|---------|-------------|-------------|
| Song Description | Single field | N/A |
| Lyrics | N/A | Separate expandable section |
| Styles | N/A | Separate expandable section with tags |
| Instrumental Toggle | Yes (clears description!) | Leave Lyrics blank |
| Title | N/A | Optional field |
| Advanced Options | N/A | Yes |
| Best for | Quick generation | Detailed control |

---

## Custom Mode UI Elements

### Identified via Chrome DevTools MCP (uid references)

```
Custom Tab Structure:
├── Audio button (uid: 3_44) - "Add audio - upload or record"
├── Persona button (uid: 3_45) - "Add Persona"
├── Inspo button (uid: 3_46) - "Add inspiration from a playlist"
├── Lyrics section (uid: 3_47) - Expandable, expanded by default
│   ├── Lyrics textarea (uid: 3_52) - "Write some lyrics or a prompt — or leave blank for instrumental"
│   └── Enhance lyrics input (uid: 3_54) - "Enhance lyrics (e.g. 'make it sound happier')"
├── Styles section (uid: 3_55) - Expandable, expanded by default
│   ├── Styles textarea (uid: 3_60) - "indie, electronic, synths, 120bpm, distorted"
│   ├── Exclude styles input (uid: 3_62+) - Various style tag buttons
│   └── Style suggestion buttons - "techno", "smooth piano", "afrobeat", etc.
├── Advanced Options (uid: 3_87) - Expandable
├── Song Title field (uid: 3_88) - "Song Title (Optional)"
├── Save to workspace (uid: 3_90) - Dropdown
└── Create button (uid: 3_92) - "Create song" (disabled until valid input)
```

---

## Automation Workflow for Custom Mode

### Step 1: Navigate to Create Page
```javascript
// Click Create in left sidebar
const createLink = Array.from(document.querySelectorAll('a')).find(el =>
  el.textContent.trim() === 'Create'
);
createLink.click();
await new Promise(resolve => setTimeout(resolve, 2000));
```

### Step 2: Switch to Custom Tab
```javascript
// Click Custom tab (Simple is default)
const customTab = Array.from(document.querySelectorAll('button')).find(btn =>
  btn.textContent.trim() === 'Custom'
);
customTab.click();
await new Promise(resolve => setTimeout(resolve, 1000));
```

### Step 3: Leave Lyrics Blank (for instrumental)
```javascript
// For instrumental music, simply leave the Lyrics field empty
// The placeholder text says: "Write some lyrics or a prompt — or leave blank for instrumental"
const lyricsTextarea = Array.from(document.querySelectorAll('textarea')).find(el =>
  el.placeholder.includes('Write some lyrics')
);

// Ensure it's empty
lyricsTextarea.value = '';
```

### Step 4: Fill Styles Field
```javascript
// This is the primary field for instrumental music prompts
const stylesTextarea = Array.from(document.querySelectorAll('textarea')).find(el =>
  el.placeholder.includes('indie, electronic, synths')
);

stylesTextarea.focus();
stylesTextarea.click();

// Use native setter for React
const nativeSetter = Object.getOwnPropertyDescriptor(
  window.HTMLTextAreaElement.prototype, 'value'
).set;

const stylePrompt = "chillsynth jazz fusion, 108 BPM, analog synth pads, electric piano, boom bap drums, instrumental";
nativeSetter.call(stylesTextarea, stylePrompt);

// Trigger React's onChange
stylesTextarea.dispatchEvent(new Event('input', { bubbles: true }));
stylesTextarea.dispatchEvent(new Event('change', { bubbles: true }));
```

### Step 5: Optional - Add Title
```javascript
const titleInput = Array.from(document.querySelectorAll('input')).find(el =>
  el.placeholder && el.placeholder.includes('Song Title')
);

if (titleInput) {
  const nativeSetter = Object.getOwnPropertyDescriptor(
    window.HTMLInputElement.prototype, 'value'
  ).set;
  nativeSetter.call(titleInput, "Deep Focus Track 5");
  titleInput.dispatchEvent(new Event('input', { bubbles: true }));
}
```

### Step 6: Wait for Validation
```javascript
// Wait for React to validate the form
await new Promise(resolve => setTimeout(resolve, 500));
```

### Step 7: Click Create
```javascript
const createButton = Array.from(document.querySelectorAll('button')).find(btn =>
  btn.getAttribute('aria-label') === 'Create song' ||
  (btn.textContent.trim() === 'Create' && !btn.disabled)
);

if (createButton && !createButton.disabled) {
  createButton.click();
  console.log('✅ Song generation started!');
} else {
  console.error('❌ Create button not enabled');
}
```

---

## Complete Custom Mode Script

```javascript
async function generateSunoSongCustomMode(stylePrompt, title = null) {
  try {
    // 1. Navigate to Create
    console.log('Step 1: Navigating to Create...');
    const createLink = Array.from(document.querySelectorAll('a')).find(el =>
      el.textContent.trim() === 'Create'
    );
    if (!createLink) throw new Error('Create link not found');
    createLink.click();
    await new Promise(resolve => setTimeout(resolve, 2000));

    // 2. Switch to Custom tab
    console.log('Step 2: Switching to Custom mode...');
    const customTab = Array.from(document.querySelectorAll('button')).find(btn =>
      btn.textContent.trim() === 'Custom'
    );
    if (!customTab) throw new Error('Custom tab not found');
    customTab.click();
    await new Promise(resolve => setTimeout(resolve, 1000));

    // 3. Ensure Lyrics is empty (instrumental)
    console.log('Step 3: Clearing lyrics (instrumental mode)...');
    const lyricsTextarea = Array.from(document.querySelectorAll('textarea')).find(el =>
      el.placeholder.includes('Write some lyrics')
    );
    if (lyricsTextarea) {
      lyricsTextarea.value = '';
    }

    // 4. Fill Styles
    console.log('Step 4: Filling styles...');
    const stylesTextarea = Array.from(document.querySelectorAll('textarea')).find(el =>
      el.placeholder.includes('indie, electronic, synths')
    );
    if (!stylesTextarea) throw new Error('Styles textarea not found');

    stylesTextarea.focus();
    stylesTextarea.click();

    const textareaSetter = Object.getOwnPropertyDescriptor(
      window.HTMLTextAreaElement.prototype, 'value'
    ).set;
    textareaSetter.call(stylesTextarea, stylePrompt);
    stylesTextarea.dispatchEvent(new Event('input', { bubbles: true }));
    stylesTextarea.dispatchEvent(new Event('change', { bubbles: true }));

    // 5. Optional: Add title
    if (title) {
      console.log('Step 5: Adding title...');
      const titleInput = document.querySelector('input[placeholder*="Song Title"]');
      if (titleInput) {
        const inputSetter = Object.getOwnPropertyDescriptor(
          window.HTMLInputElement.prototype, 'value'
        ).set;
        inputSetter.call(titleInput, title);
        titleInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
    }

    // 6. Wait for validation
    console.log('Step 6: Waiting for form validation...');
    await new Promise(resolve => setTimeout(resolve, 500));

    // 7. Click Create
    console.log('Step 7: Clicking Create...');
    const createButton = Array.from(document.querySelectorAll('button')).find(btn =>
      btn.getAttribute('aria-label') === 'Create song'
    );

    if (!createButton) throw new Error('Create button not found');
    if (createButton.disabled) throw new Error('Create button is disabled');

    createButton.click();

    console.log('✅ Song generation submitted successfully!');
    console.log(`   Style: ${stylePrompt.substring(0, 60)}...`);
    if (title) console.log(`   Title: ${title}`);

    // Wait for generation to start
    await new Promise(resolve => setTimeout(resolve, 3000));

    return {
      success: true,
      style: stylePrompt,
      title: title,
      timestamp: new Date().toISOString()
    };

  } catch (error) {
    console.error('❌ Generation failed:', error.message);
    return {
      success: false,
      error: error.message
    };
  }
}

// Example usage:
// await generateSunoSongCustomMode(
//   "chillsynth jazz fusion, 108 BPM, analog synth pads, electric piano, boom bap drums",
//   "Deep Focus 5"
// );
```

---

## Prompt Format for Custom Mode Styles Field

### Recommended Structure
```
[genres], [BPM], [key instruments], [mood/texture], instrumental
```

### Examples from Your Prompts

**Prompt #5 (Excellent):**
```
chillsynth jazz fusion, 108 BPM, analog synth pads, electric piano, boom bap drums, hypnotic, instrumental
```

**Prompt #13 (Excellent):**
```
deep house afro jazz fusion, 115 BPM, balafon, four-on-floor kick, sub bass, wordless vocals, Rhodes, ritual precision, instrumental
```

**General Template:**
```
[primary genre] [fusion genre], [BPM] BPM, [instrument1], [instrument2], [instrument3], [mood adjective], instrumental
```

### Style Field Character Limits
- **Recommended:** 80-120 characters
- **Maximum observed:** ~200 characters (may truncate)
- **Optimal:** Focus on key identifiers rather than full neurological descriptions

---

## Key Differences from Simple Mode

### Simple Mode Issues (AVOID)
1. ❌ **Instrumental toggle clears description field**
2. ❌ Single field tries to be both lyrics and style
3. ❌ Less control over generation parameters

### Custom Mode Advantages (RECOMMENDED)
1. ✅ **Separate Lyrics and Styles fields** - clearer intent
2. ✅ **Leaving Lyrics blank = instrumental** - no toggle confusion
3. ✅ **Styles field** optimized for genre/instrument tags
4. ✅ **Optional title field** for organization
5. ✅ **Advanced Options** for more control
6. ✅ **Style suggestion buttons** for exploration

---

## Batch Processing Strategy

### For Your 48 Prompts

```javascript
async function batchGenerateFromCSV(csvPrompts) {
  const results = [];

  for (let i = 0; i < csvPrompts.length; i++) {
    const prompt = csvPrompts[i];

    console.log(`\n🎵 Generating ${i + 1}/${csvPrompts.length}: ${prompt.Prompt_ID}`);

    // Extract condensed style from full prompt
    const stylePrompt = `${prompt.Primary_Genres}, ${prompt.BPM} BPM, ${prompt.Key_Instruments}, instrumental`;
    const title = `Track ${prompt.Prompt_ID}`;

    const result = await generateSunoSongCustomMode(stylePrompt, title);

    if (result.success) {
      results.push({
        promptId: prompt.Prompt_ID,
        status: 'generated',
        timestamp: result.timestamp
      });

      // Wait between generations (rate limiting)
      console.log('⏳ Waiting 15 seconds before next generation...');
      await new Promise(resolve => setTimeout(resolve, 15000));
    } else {
      results.push({
        promptId: prompt.Prompt_ID,
        status: 'failed',
        error: result.error
      });

      // Continue despite failure
    }
  }

  return results;
}
```

---

## Monitoring Generation Progress

### After Clicking Create

The page will show generation progress. To monitor:

```javascript
// Wait for generation to complete (2-3 minutes typical)
async function waitForGeneration() {
  let attempts = 0;
  const maxAttempts = 36; // 3 minutes at 5 second intervals

  while (attempts < maxAttempts) {
    await new Promise(resolve => setTimeout(resolve, 5000));

    // Check if new song appeared in library
    const newSong = document.querySelector('[role="row"]'); // First song in list
    if (newSong) {
      console.log('✅ Generation complete!');

      // Extract audio URL
      const audioElement = newSong.querySelector('audio source');
      if (audioElement) {
        return audioElement.src;
      }
    }

    attempts++;
    console.log(`⏳ Checking progress... (${attempts}/${maxAttempts})`);
  }

  throw new Error('Generation timed out');
}
```

---

## Error Handling

### Common Issues

1. **Create button stays disabled**
   - Verify Styles field has content
   - Check for validation errors
   - Ensure React events fired correctly

2. **Generation fails**
   - Check credit balance (2,230 shown)
   - Verify style tags are valid
   - Check for rate limiting

3. **UI doesn't respond**
   - Page may have refreshed
   - Re-navigate to Create page
   - Switch back to Custom tab

---

## Next Steps

1. ✅ Test single generation with Prompt #5 style
2. ✅ Extract audio URL after completion
3. ✅ Update CSV with results
4. ✅ Test batch of 5 prompts
5. ✅ Scale to full 48 prompt library

---

**Status:** Ready for testing with Custom mode!
