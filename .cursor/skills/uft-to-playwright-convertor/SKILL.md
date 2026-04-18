---
name: UFT to Playwright Self-Healing Migration Agent
description: >
  Reads a JIRA story (.md) and UFT Keyword-Driven Excel (.xlsx) as dual inputs,
  translates the UFT flow into Playwright test scripts using Page Object Model,
  executes them, and triggers a self-healing loop on failure.
  Covers: Input Parsing → Planning → Manual Browser Verification → Script Generation → Execution → Self-Healing → Reporting.
triggers:
  - migrate uft to playwright
  - uft keyword driven to playwright
  - self-heal playwright tests
  - fix failing playwright tests
  - broken locator
  - playwright locator not found
---

# UFT to Playwright Self-Healing Migration Agent

## Repo Context

- **App Under Test**: Read from `playwright-demo/inputs/SD-101_JiraStory.md` (AC-1 background URL) — default: `https://www.saucedemo.com/`
- **Input Files Folder**: `playwright-demo/inputs/`
  - JIRA Story: `*.md` file inside inputs folder
  - UFT Excel: `*.xlsx` file inside inputs folder
- **Tests Folder**: `playwright-demo/tests/` — scan for all `*.spec.ts` files
- **Page Objects Folder**: `playwright-demo/tests/pages/` — scan for all `*.ts` files
- **Test Data Folder**: `playwright-demo/tests/testData/`
- **Playwright Config**: `playwright-demo/playwright.config.ts`
- **Healing Report Output**: `playwright-demo/healing-report/healing-report-<YYYYMMDD-HHmmss>.md` (timestamped per run)

---

## Input Priority Rule

> ⚠️ **The UFT Excel always takes priority over the JIRA story.**
> The JIRA story may be outdated. Use it only for high-level context and acceptance criteria.
> All step-by-step flow, element references, and action sequences must be driven by the Excel.

---

## Phase 0 — Input Parsing

**Goal**: Read and fully understand both input files before doing anything else. Do not proceed to Phase 1 until this phase is complete.

### Step 1 — Read the JIRA Story

Open `playwright-demo/inputs/*.md`:
- Extract the **application URL** from the Background/Context section
- Extract the **Acceptance Criteria** (AC-1 through AC-N) as high-level expected outcomes
- Extract **Test Data** values (hardcoded values like username/password; note which fields are `Random`)
- Store AC list internally as the **verification checklist** for Phase 2

### Step 2 — Read the UFT Excel

Open `playwright-demo/inputs/*.xlsx`. Read all available sheets:

#### Sheet: `*_Actions`
- Read all rows where `Run = Yes`
- Extract the ordered list of **Action names** — these become the logical test groups
- Ignore rows where `Run = No`

#### Sheet: `*_TestSteps`
- Filter rows by each Action from the Actions sheet
- For each step, extract:
  - `Step_Number` — execution order
  - `Action` — which group this step belongs to
  - `AUT_Field` — element reference in `Page|FieldName` format (look up in OR sheet)
  - `Functionality` + `Sub_Functionality` — the keyword to execute (map using the table below)
  - `Value_Identifier` + `Value` — input data (`Value` = hardcoded string, `Reference` = runtime-generated)
  - `Take_Screenshot` — capture screenshot after this step if `Yes`
  - `Need_Reporting` — include in report if `Yes`

#### Sheet: `*_ObjectRepository`
- For each element referenced in TestSteps (`AUT_Field`), look it up in this sheet via `Page_And_AUT_Field` column
- Extract:
  - `GC_Locator` — always prefer Chrome locator (Playwright uses Chromium)
  - `Field_Type` — textbox / button / element / link
  - `Object_Type` — WebEdit / WebElement / TextboxSecure / Custom WebElement
  - `Page_Name` — which page this element belongs to

#### Sheet: `Framework_AUTFunctionality`
- Load the full keyword dictionary
- Use it to validate every `Functionality` + `Sub_Functionality` combination found in TestSteps

### Step 3 — UFT Keyword → Playwright Action Mapping

Translate every UFT keyword to its Playwright equivalent using this table:

| UFT Functionality | UFT Sub_Functionality | Playwright Action |
|---|---|---|
| GeneralUtilities | StandardOperation | `await locator.fill(value)` for textbox / `await locator.click()` for button/link |
| CheckPoint-FrontEnd | IsObjectExists | `await expect(locator).toBeVisible()` |
| CheckPoint-FrontEnd | IsObjectNotExists | `await expect(locator).toBeHidden()` |
| CheckPoint-FrontEnd | IsTextPresentOnPage | `await expect(page).toContainText(value)` |
| CheckPoint-FrontEnd | IsTextNotPresentOnPage | `await expect(page).not.toContainText(value)` |
| AdhocApplication | LaunchApplication | `await page.goto(url)` |
| AdhocApplication | MouseOver | `await locator.hover()` |
| AdhocApplication | FireClickEvent | `await locator.click()` |
| AdhocApplication | SetFocusOn | `await locator.focus()` |
| AdhocSynchronization | WaitForPageLoad | `await page.waitForLoadState('networkidle')` |
| AdhocSynchronization | WaitForTime | `await page.waitForTimeout(value * 1000)` |
| FramworkProperties | SetApplication | Set base URL context (no direct Playwright call) |
| FramworkProperties | SetObjectRepository | Load page object class for the referenced page |
| FramworkProperties | SetPageName | Set current page context (no direct Playwright call) |

### Step 4 — Value Resolution

For each step:
- `Value_Identifier = Value` → use the `Value` column string directly
- `Value_Identifier = Reference` + `Value = RANDOM|FirstName` → generate a random first name at runtime using `faker` or `Math.random()` string
- `Value_Identifier = Reference` + `Value = RANDOM|LastName` → generate a random last name at runtime
- `Value_Identifier = Reference` + `Value = RANDOM|ZipCode` → generate a random 5-digit zip code at runtime
- `Value_Identifier = --NA--` → no input value needed (click/hover/wait actions)

### Step 5 — Internal Parsed Summary

Produce this internal summary before moving to Phase 1:

```
PARSED INPUTS SUMMARY
=====================
App URL       : <url>
Actions (Run=Yes): [LoginToApplication, AddItemsToCart, ...]
Total Steps   : <N>
Total Elements: <N> (from OR sheet)
Test Data     :
  - username     : standard_user
  - password     : secret_sauce
  - firstName    : RANDOM
  - lastName     : RANDOM
  - zipCode      : RANDOM
Acceptance Criteria: AC-1 ... AC-N
```

---

## Phase 1 — Planning (Story → Structured Test Cases)

**Goal**: Convert the parsed inputs into a structured test plan. Do not guess — use only what Phase 0 extracted.

### Steps

1. Group all TestSteps by their `Action` (in the order defined in the Actions sheet)
2. For each Action, produce a structured test case:

```
TC-001: LoginToApplication
  Step 1 : Navigate to https://www.saucedemo.com/
           Playwright: await page.goto('https://www.saucedemo.com/')
           Expected  : Login page is displayed

  Step 2 : Enter username "standard_user" in Username field
           Playwright: await loginPage.username.fill('standard_user')
           Expected  : Username field accepts input

  Step 3 : Enter password "secret_sauce" in Password field
           Playwright: await loginPage.password.fill('secret_sauce')
           Expected  : Password field accepts input

  Step 4 : Click Login button
           Playwright: await loginPage.loginButton.click()
           Expected  : User is redirected to Products page

  [Screenshot: Yes]
```

3. Map each step to its Playwright action using the keyword mapping table from Phase 0
4. Cross-reference each AC from the JIRA story against the test cases — confirm every AC is covered
5. Produce a final **AC Coverage Table**:

```
AC Coverage Check
  AC-1 LOGIN              → Covered by TC-001 (LoginToApplication)
  AC-2 ADD ITEMS TO CART  → Covered by TC-002 (AddItemsToCart)
  AC-3 PROCEED TO CHECKOUT→ Covered by TC-003 (ProceedToCheckout)
  AC-4 FILL INFO          → Covered by TC-003 (ProceedToCheckout)
  AC-5 COMPLETE ORDER     → Covered by TC-004 (CompleteOrder)
```

---

## Phase 2 — Manual Browser Verification (Playwright MCP)

**Goal**: Execute each test case step manually in a real browser via Playwright MCP. Verify actual browser state against expected outcome from Phase 1. Do not write scripts yet.

### Steps

For each test case from Phase 1, in order:

1. Use Playwright MCP to navigate to the page:
   ```
   browser_navigate → <url>
   ```

2. Take a DOM snapshot after navigation:
   ```
   browser_snapshot
   ```

3. For each step in the test case:
   - Execute the action using the appropriate MCP browser tool
   - Take a screenshot if `Take_Screenshot = Yes`
   - After the action, take a new `browser_snapshot`
   - Compare **actual browser state** (from snapshot) vs **expected outcome** (from Phase 1)
   - Log ✅ PASS or ❌ FAIL per step

4. For each element used:
   - Confirm the `GC_Locator` from the OR sheet resolves in the live DOM
   - Count matches — must be exactly 1
   - If 0 matches → flag as broken locator (carry into Phase 3 script generation with a note)

5. Produce a step-by-step execution log:

```
Manual Execution Log — TC-001: LoginToApplication
  Step 1 : Navigate to https://www.saucedemo.com/    ✅ PASS
  Step 2 : Fill Username field                        ✅ PASS  [Screenshot saved]
  Step 3 : Fill Password field                        ✅ PASS  [Screenshot saved]
  Step 4 : Click Login button                         ✅ PASS  [Screenshot saved]
  Step 5 : Wait for page load                         ✅ PASS
  -----------------------------------------------
  TC-001 Result: PASS
```

---

## Phase 3 — Script Generation (Page Object Model)

**Goal**: Generate Playwright TypeScript test scripts using POM pattern. Use locators confirmed in Phase 2 (live DOM). One spec file for the entire E2E flow.

### Rules

- Use locators **exactly as confirmed in Phase 2** — never from memory or assumption
- If Phase 2 flagged a broken locator, use the best alternative found in the live DOM snapshot
- Follow POM strictly — locators in page files, test logic in spec file
- Generate random values for `RANDOM` fields using faker or inline random string helpers
- One Page Object class per page
- One spec file for the entire E2E flow: `e2e-order-flow.spec.ts`

### Output Structure

```
playwright-demo/
├── tests/
│   ├── pages/
│   │   ├── LoginPage.ts
│   │   ├── ProductsPage.ts
│   │   ├── YourCartPage.ts
│   │   ├── YourInformationPage.ts
│   │   ├── CheckoutOverviewPage.ts
│   │   └── CheckoutCompletePage.ts
│   └── e2e-order-flow.spec.ts
```

### Page Object Template

```typescript
// playwright-demo/tests/pages/LoginPage.ts
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly username: Locator;
  readonly password: Locator;
  readonly loginButton: Locator;

  constructor(page: Page) {
    this.page         = page;
    this.username     = page.locator("[data-test='username']");
    this.password     = page.locator("[data-test='password']");
    this.loginButton  = page.locator("[data-test='login-button']");
  }

  async navigate(url: string) {
    await this.page.goto(url);
  }

  async login(username: string, password: string) {
    await this.username.fill(username);
    await this.password.fill(password);
    await this.loginButton.click();
  }
}
```

### Spec File Template

```typescript
// playwright-demo/tests/e2e-order-flow.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/LoginPage';
// ... import all page objects

test.describe('E2E Order Flow — SD-101', () => {
  test('Complete order from login to confirmation', async ({ page }) => {

    // TC-001: Login
    const loginPage = new LoginPage(page);
    await loginPage.navigate('https://www.saucedemo.com/');
    await loginPage.login('standard_user', 'secret_sauce');
    await page.screenshot({ path: 'screenshots/login.png' });

    // TC-002: Add items to cart
    // ...

    // AC-5 Verification
    await expect(page.locator("[data-test='complete-header']"))
      .toContainText('Thank you for your order!');
    await page.screenshot({ path: 'screenshots/order-confirmation.png' });
  });
});
```

---

## Phase 4 — Script Execution + Self-Healing Loop

**Goal**: Run the generated scripts. If all pass, generate the report. If any fail, trigger the self-healing loop.

### Step 1 — Run the Tests

```bash
cd playwright-demo && npx playwright test --reporter=json 2>&1
```

### Step 2 — Evaluate Results

- **All pass** → skip to Report Generation
- **Any fail** → proceed to Self-Healing (below)

---

## Self-Healing — Failure Detection

**Goal**: Run the test suite, extract structured failure data. Do not guess — read what the tool output tells you.

### Steps

1. Parse the JSON output. For each failed test extract:
   - Test name
   - Error message (full timeout / not-found message)
   - File path where the failure originated
   - Line number
   - The broken selector string (appears in the error inside `page.locator(...)` calls)

2. Cross-reference: open the page object file at the reported line. Confirm the exact selector that caused the failure.

3. Produce an internal failure summary:

```
Test: "Complete order from login to confirmation"
Failures:
  1. File: tests/pages/<file>.ts | Line: <N> | Locator: <selector> | Error: <short error>
```

---

## Self-Healing — Deep Analysis (DOM Comparison)

**Goal**: For each broken locator, go to the live page, read the real DOM, find the correct replacement.

### Steps

For **each** broken locator:

1. Open the page object file. Read what URL or navigation brings up the page containing the broken locator. Use Playwright MCP to navigate there.

2. Take a DOM snapshot:
   ```
   browser_snapshot
   ```

3. Search the snapshot for:
   - The **original broken selector** — count matches (expect: 0)
   - The **element type** from the original selector
   - All elements of that type visible on the page
   - Any `data-test`, `aria-label`, `id`, placeholder text nearby

4. Propose a **candidate replacement locator** based on the live DOM.

5. Validate the candidate:
   - Does it return at least 1 match?
   - Does it return exactly 1 match?
   - Is the element type preserved?

6. Produce a side-by-side comparison:

```
Locator <N> — <page-object-file>.ts
  OLD:  <broken selector>   → 0 matches in current DOM
  DOM:  <element type> elements found: <list of visible text/attrs>
  NEW:  <proposed selector> → 1 match ✓ | ⚠ position-based
```

---

## Self-Healing — Fix Implementation

**Goal**: Apply the fix. Fix one locator at a time. Verify before moving on.

### Rules (do not deviate)

- Make the **minimum change** required: change only the selector string, nothing else
- Fix **one locator**, then re-run the test. Do not batch multiple fixes
- If the test passes after a fix → move to the next broken locator
- If the test still fails → repeat Failure Detection → Deep Analysis → Fix (max 3 iterations per locator)
- If 3 iterations exhausted without passing → write "Needs human review" in the healing report and **stop**
- If a structural change is needed beyond the selector, apply it but document every change in the report

### Steps

For **each** broken locator:

1. **Run Guardrails first** on the proposed new selector. Only proceed if guardrails PASS.

2. Edit the page object file — replace ONLY the broken selector string:
   - File: `playwright-demo/tests/pages/<file>.ts`
   - Change: the `page.locator('...')` argument on the specific line

3. Re-run the test:
   ```bash
   cd playwright-demo && npx playwright test --reporter=json 2>&1
   ```

4. If passes → record fix in healing report → move to next broken locator
5. If fails → increment iteration counter → repeat
6. After iteration 3 with no fix → log "Needs human review" → stop

---

## Self-Healing — Guardrails

**Goal**: Prevent AI hallucinations from writing broken selectors into production files. Run these checks **before every file edit**. All 5 checks must pass.

#### Check 1 — Existence
- Count matches for the new selector in the current DOM
- **PASS**: ≥ 1 match found
- **FAIL**: 0 matches → reject, return to Deep Analysis

#### Check 2 — Uniqueness
- **PASS**: Exactly 1 match
- **FAIL**: > 1 match → selector is ambiguous → reject, find more specific selector

#### Check 3 — Element Type
- Confirm the new selector resolves to the same HTML element type as the original
- **PASS**: Types match
- **FAIL**: Types differ → reject

#### Check 4 — Confidence Threshold
- Assess semantic similarity between old and new selector
- **PASS**: Confidence ≥ 80%
- **FAIL**: Confidence < 80% → do NOT apply fix → write "Needs human review — low confidence replacement" → stop

#### Check 5 — Position-based XPath Warning
- If the only working selector is `(//tag)[N]` (positional), it is fragile
- **PASS with WARNING**: Apply fix but flag as fragile in healing report, recommend `data-test` attribute

### When Guardrails Fail

- Log rejection reason internally
- Return to Deep Analysis, try the next best candidate selector
- If all candidates fail guardrails → write "Needs human review — all candidates failed guardrails" → do not edit the file

---

## Report Generation

Write a new timestamped file `playwright-demo/healing-report/healing-report-<YYYYMMDD-HHmmss>.md` after all phases are complete.
Generate the timestamp at the start of the run. Create the directory if it does not exist. Never overwrite an existing report.

Use this exact format:

```markdown
# Self-Healing Migration Report — <timestamp>

## Summary
- JIRA Story     : SD-101
- App Under Test : https://www.saucedemo.com/
- Tests Run      : <N>
- Failures Detected : <N>
- Locators Healed   : <N>
- Human Review Needed : <N>

---

## UFT → Playwright Migration Map

| Step | UFT Action | UFT Keyword (Functionality|Sub_Functionality) | AUT_Field | Playwright Equivalent |
|------|------------|------------------------------------------------|-----------|----------------------|
| Step#001 | LoginToApplication | FramworkProperties\|SetApplication | --NA-- | `await page.goto(url)` |
| Step#005 | LoginToApplication | GeneralUtilities\|StandardOperation | LoginPage\|Username | `await loginPage.username.fill('standard_user')` |
| ... | ... | ... | ... | ... |

---

## Manual Browser Verification Results

| Test Case | Steps Passed | Steps Failed | Result |
|-----------|-------------|-------------|--------|
| TC-001 LoginToApplication | <N> | <N> | ✅ PASS / ❌ FAIL |
| TC-002 AddItemsToCart     | <N> | <N> | ✅ PASS / ❌ FAIL |
| TC-003 ProceedToCheckout  | <N> | <N> | ✅ PASS / ❌ FAIL |
| TC-004 CompleteOrder      | <N> | <N> | ✅ PASS / ❌ FAIL |

---

## Acceptance Criteria Coverage

| AC | Description | Status |
|----|-------------|--------|
| AC-1 | User can login with valid credentials | ✅ Covered |
| AC-2 | Items added to cart successfully | ✅ Covered |
| AC-3 | User proceeds to checkout | ✅ Covered |
| AC-4 | Checkout information filled correctly | ✅ Covered |
| AC-5 | Order confirmation text is visible | ✅ Covered |

---

## Healed Locators

### Fix <N> — <filename>
- Old: `<old selector>`
- New: `<new selector>`
- Guardrail Result: PASS | PASS with WARNING | FAIL
- Guardrail Details: (<match count> match, type=<type>, confidence=<X>%)
- Verification: Test re-run passed ✓ | FAILED after 3 iterations ✗

---

## Items Needing Human Review

### <filename> — <locator>
- Reason: <why guardrails failed or iterations exhausted>
- Last Attempted Selector: `<selector>`
- Recommendation: <what a human should check>
```

---

## Execution Order

```
Phase 0 — Input Parsing (JIRA .md + UFT Excel)
        ↓
Phase 1 — Planning (Excel steps → structured test cases + AC coverage check)
        ↓
Phase 2 — Manual Browser Verification (Playwright MCP — actual vs expected)
        ↓
Phase 3 — Script Generation (POM TypeScript — locators from Phase 2)
        ↓
Phase 4 — Script Execution
        ↓ all pass?
        ✅ → Report Generation → DONE
        ❌ → Self-Healing Loop:
              Failure Detection → Deep Analysis → Guardrails → Fix → Re-run
              (max 3 iterations per locator)
              ↓ after 3 iterations
              "Needs human review" → STOP → Report Generation
```

After all locators processed → write healing report.
