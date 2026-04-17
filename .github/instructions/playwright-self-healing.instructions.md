---
name: Playwright Self-Healing
description: >
  Detects broken Playwright locators, analyzes live DOM via Playwright MCP,
  applies self-healing fixes with guardrails, and generates a healing report.
  Covers: Failure Detection → Deep Analysis → Self-Healing → Guardrails.
triggers:
  - fix failing playwright tests
  - self-heal locators
  - broken locator
  - playwright locator not found
  - heal playwright tests
---

# Playwright Self-Healing Skill

## Repo Context
 - **App Under Test**: `https://opensource-demo.orangehrmlive.com/`
 - **Tests Folder**: `playwright-demo/tests` - scan for all `*.spec.ts` files
 - **Page objects folder**: `playwright-demo/tests/pages/` — scan for all `*.ts` files; these contain `page.locator(...)` calls
- **Test data folder**: `playwright-demo/tests/testData/`
- **Playwright config**: `playwright-demo/playwright.config.ts`
- **Healing report output**: `playwright-demo/healing-report/healing-report-<YYYYMMDD-HHmmss>.md` (timestamped per run)

---

## Phase 1 - Failure Detection

**Goal**: Run the test suite, extract structured failure data. Do not guess - read what the tool output tells you.

### Steps

1. Run the tests with JSON reporter from `playwright-demo`:
```bash
cd playwright-demo &&  npx playwright test --reporter=json 2>&1
```

2. Parse the JSON output. For each failed test, extract:
   - Test name
   - Error message (the full timeout/not-found message)
   - File path where the failure originated
   - Line number
   - The broken selector string (it appears in the error message inside `page.locator(...)` calls)

3. Cross-reference: open the page object file at the reported line. Confirm the exact selector string that caused the failure.

4. Produce an internal failure summary before moving to Phase 2:
   ```
   Test: "<test name>"
   Failures:
     1. File: tests/pages/<file>.ts | Line: <N> | Locator: <selector> | Error: <short error>
     2. ...
   ```
---

## Phase 2 — Deep Analysis: Old vs New Locator Comparison

**Goal**: For each broken locator, go to the live page, read the real DOM, and find the correct replacement. This is RAG-style retrieval — the agent retrieves live context and compares it against the stale selector.

### Steps

For **each** broken locator from Phase 1:

1. Open the page object file reported in Phase 1 (inside `playwright-demo/tests/pages/`).
   Read the file to understand what URL or navigation action brings up the page that contains the broken locator.
   Use Playwright MCP to navigate to that page.

2. Take a DOM snapshot:
   ```
   browser_snapshot
   ```

3. Search the snapshot for:
   - The **original broken selector** — count how many matches it returns (expect: 0)
   - The **element type** from the original selector (span, input, button, etc.)
   - All elements of that type visible on the page
   - Any aria-labels, data-testid attributes, placeholder text, or unique text nearby

4. Propose a **candidate replacement locator** based on what is actually in the DOM.

5. Validate the candidate in the snapshot:
   - Does it return at least 1 match?
   - Does it return exactly 1 match?
   - Is the element type preserved?

6. Produce a side-by-side comparison:
   ```
   Locator <N> — <page-object-file>.ts
     OLD:  <broken selector>   → 0 matches in current DOM
     DOM:  <element type> elements found: <list of visible text/attrs>...
     NEW:  <proposed selector> → 1 match ✓ | ⚠ position-based
   ```

## Phase 3 — Self-Healing Implementation

**Goal**: Apply the fix from Phase 2. Fix one locator at a time. Verify before moving on.

### Rules (do not deviate)

- Make the **minimum change** required: change only the selector string, nothing else.
- Fix **one locator**, then re-run the test. Do not batch multiple fixes.
- If the test passes after a fix, move to the next broken locator.
- If the test still fails, run Phase 1 → Phase 2 → Phase 3 again for that locator (max 3 iterations total per locator).
- If 3 iterations are exhausted without a passing test, write "Needs human review" in the healing report and **stop**. Do not attempt further changes.
- If a structural change is needed beyond the selector (method rename, import update, new helper), apply it, but document every change in the healing report with a reason.

### Steps

For **each** broken locator (in Phase 1 order):

1. **Run Phase 4 guardrails first** on the proposed new selector. Only proceed if guardrails PASS.

2. Edit the page object file — replace ONLY the broken selector string:
   - File: `playwright-demo/tests/pages/<file>.ts`
   - Change: the `page.locator('...')` argument on the specific line

3. Re-run the test:
   ```bash
   cd playwright-demo && npx playwright test --reporter=json 2>&1
   ```

4. If the test passes → record the fix in the healing report → move to next broken locator.

5. If the test still fails → increment iteration counter → repeat Phase 1 → Phase 2 → Phase 3.

6. After iteration 3 with no fix → log "Needs human review" → stop.

---

## Phase 4 — Guardrails

**Goal**: Prevent AI hallucinations from writing broken selectors into production files. Run these checks **before every file edit in Phase 3**. This is structured output validation — same principle as Pydantic validation in LangGraph, but encoded as instructions.

### Guardrail Checklist

Run all 5 checks against the proposed new selector **before writing to any file**:

#### Check 1 — Existence
- Use `browser_snapshot` or `browser_evaluate` to count matches for the new selector in the current DOM.
- **PASS**: ≥ 1 match found.
- **FAIL**: 0 matches → reject this candidate, return to Phase 2 and find a different selector.

#### Check 2 — Uniqueness
- Count matches for the new selector.
- **PASS**: Exactly 1 match.
- **FAIL**: > 1 match → selector is ambiguous → reject, find a more specific selector (add aria-label, data-testid, or narrower context).

#### Check 3 — Element Type
- Identify the HTML element type the new selector resolves to.
- Compare to the original selector's intended type (if original targeted `input`, new must resolve to `input`; if `span`, new must be `span`; etc.).
- **PASS**: Types match.
- **FAIL**: Types differ → reject (agent found wrong element).

#### Check 4 — Confidence Threshold
- Assess semantic similarity between old and new selector: same element purpose, same page context, same functional role.
- **PASS**: Confidence ≥ 80% (the element clearly serves the same purpose as the original).
- **FAIL**: Confidence < 80% → do NOT apply the fix. Write to healing report: "Needs human review — low confidence replacement". Stop.

#### Check 5 — Position-based XPath Warning
- If the only working selector is `(//tag)[N]` (positional), it is fragile.
- **PASS with WARNING**: Apply the fix, but add a comment in the healing report flagging it as fragile and recommending a `data-testid` attribute.
- There is no hard failure for this check — it is a warning only.

### When Guardrails Fail

- Log the rejection reason internally.
- Return to Phase 2, try the next best candidate selector.
- If all candidates fail guardrails → escalate: write "Needs human review — all candidates failed guardrails" in the healing report. Do not edit the file.

---

## Report Generation

**Write** a new timestamped file `playwright-demo/healing-report/healing-report-<YYYYMMDD-HHmmss>.md` after all locators are processed.

Generate the timestamp at the start of the run using the current date and time in `YYYYMMDD-HHmmss` format (e.g. `healing-report-20260417-062244.md`).
Create the directory if it doesn't exist. Never overwrite an existing report — each run produces its own file.

Use this exact format:

```markdown
# Self-Healing Report — <timestamp>

## Summary
- Tests run: <N>
- Failures detected: <N>
- Locators healed: <N>
- Human review needed: <N>

## Healed Locators

### Fix <N> — <filename>
- Old: `<old selector>`
- New: `<new selector>`
- Guardrail result: PASS | PASS with WARNING | FAIL
- Guardrail details: (<match count> match, type=<type>, confidence=<X>%)
- Verification: Test re-run passed ✓ | FAILED after 3 iterations ✗

## Items Needing Human Review

### <filename> — <locator>
- Reason: <why guardrails failed or iterations exhausted>
- Last attempted selector: `<selector>`
- Recommendation: <what a human should check>
```

---

## Execution Order

```
Phase 1 → Phase 2 → Phase 4 (guardrails) → Phase 3 (fix + verify)
                                                    ↓ if still failing (max 3x)
                                            Phase 1 → Phase 2 → Phase 4 → Phase 3
                                                    ↓ after 3 iterations
                                            Write "Needs human review" → STOP
```

After all locators processed → write healing report.