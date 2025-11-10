# Suno Automation: Chrome DevTools MCP Experiment

**Status:** ✅ Technically successful, ❌ **Not recommended for production use**

---

## Summary

We successfully developed a working browser automation workflow using Chrome DevTools MCP to generate music on Suno.ai. While the technical approach works, **manual copy/paste is faster and more practical** for this use case.

---

## Why We Don't Recommend Automation

### 1. **Too Slow**
- Each song generation takes 2-3 minutes
- Browser automation adds overhead (navigation, waits, validation)
- Processing 130 prompts = ~6-8 hours of automation runtime
- **Manual is faster:** Copy/paste 5 prompts in 2 minutes vs. 10-15 minutes automated

### 2. **Too Tedious**
- Requires monitoring for errors, session timeouts, rate limits
- UI changes break selectors (Suno updates frequently)
- Debugging automation issues takes longer than manual generation
- Not truly "hands-off" - needs supervision anyway

### 3. **Too Token-Heavy**
- Chrome DevTools MCP operations consume significant tokens
- Each screenshot, DOM inspection, script evaluation adds cost
- Running 130 prompts through automation = massive token burn
- **ROI negative:** Token cost exceeds value of time saved

### 4. **No Official API**
- Suno doesn't provide an official API
- Browser automation violates terms of service (gray area)
- Risk of account suspension
- UI-based automation is fragile

---

## What We Learned

### ✅ **Technical Success**
We **did** successfully automate the full workflow:

1. Navigate to suno.ai Create page
2. Enable Instrumental mode
3. Fill Song Description field (using React-compatible native setter)
4. Click Create button
5. Wait for generation

**Key technical insights:**
- React forms require native setter + input event dispatch
- Instrumental toggle must happen BEFORE filling description
- 500ms wait needed for React validation
- Element selectors found via `querySelectorAll` with text matching

See `suno-automation-detailed-workflow.md` for complete technical details.

### ❌ **Practical Reality**
Despite technical success, the automation approach has fatal flaws for this project:
- Time investment to build/maintain > time saved
- Token cost > value delivered
- Manual workflow (copy 5 prompts, paste in Suno) takes 90 seconds
- User generates music in batches of 5-10 anyway (fits free tier credits)

---

## Recommendation

**For open source users:**

If you're considering automation, evaluate these criteria first:

### ✅ **Automation makes sense if:**
- You have hundreds/thousands of prompts to generate
- You have a paid Suno account with unlimited credits
- You're comfortable with potential ToS violations
- You have technical skills to maintain selectors when UI changes
- Token cost is not a concern

### ❌ **Use manual workflow if:**
- You have <200 prompts (like this project: 130 prompts)
- You're on Suno free tier (limited daily credits anyway)
- You want to review quality before batch generating
- You value time over automation complexity
- You care about token efficiency

**Our verdict:** Manual workflow is the pragmatic choice for this project scale.

---

## Manual Workflow (Recommended)

### Simple 90-Second Process:

1. **Open CSV** in your tool of choice
2. **Copy 5 prompts** (Styles + Title fields)
3. **Open Suno.ai** → Create → Instrumental
4. **Paste each prompt** into Song Description
5. **Click Create** for each
6. **Wait 2-3 minutes** for generation
7. **Listen and rate** the results

**Advantages:**
- Quality control at every step
- Immediate feedback on what works
- No token cost
- No maintenance burden
- Fits free tier credit limits naturally

---

## If You Still Want to Try Automation

See the detailed workflow document for complete implementation:
- `suno-automation-detailed-workflow.md`

**You'll need:**
- Chrome DevTools MCP server installed
- Claude Code with MCP integration
- Patience for debugging UI changes
- Willingness to burn tokens on experimentation

**What's documented:**
- Complete working automation script
- React form handling techniques
- Element selectors (as of Nov 2025)
- Error handling strategies
- Rate limiting approach

---

## Project Decision

**For this project:** We're sticking with **manual copy/paste** for the 130 prompts.

**Reasoning:**
- 130 prompts ÷ 5 per batch = 26 sessions
- 90 seconds per session = ~40 minutes total manual time
- Automation would take 6-8 hours runtime + 4-6 hours development
- Manual allows real-time quality assessment
- Avoids token burn and ToS risk

**The automation work wasn't wasted** - we learned:
- How Suno's UI works
- React form automation techniques
- Chrome DevTools MCP capabilities
- When automation is/isn't worth it

---

## For Open Source Users

Include both documents in the repo:
1. **This summary** - helps users make informed decisions
2. **Detailed workflow** - for users who still want to experiment

Let users choose based on their scale and constraints. Be transparent about tradeoffs.

---

**Bottom line:** Automation is impressive technically, but impractical economically for this project scale. Sometimes the simple solution (copy/paste) is the right one.
