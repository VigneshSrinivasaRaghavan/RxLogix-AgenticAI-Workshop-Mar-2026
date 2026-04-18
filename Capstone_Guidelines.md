# Capstone: Autonomous Self-Healing Agent
### Guidelines & Assignment Brief

---

## Overview

This capstone is the culmination of your learning journey. You will build an **Autonomous Self-Healing Agent** inside **Cursor IDE** that takes a JIRA user story and an existing UFT Keyword-Driven Excel as inputs, converts the flow into Playwright TypeScript test scripts, executes them, and automatically heals any locator failures — all without human intervention.

This is not just a coding exercise. This is a real-world automation migration scenario that mirrors what engineering teams face when moving from legacy UFT frameworks to modern Playwright-based automation.

---

## Session Schedule

| Time | Activity |
|---|---|
| First 20–30 mins | Capstone briefing (this document walkthrough) |
| Remaining ~4 hrs | Team working time — build the agent |
| Last 45 mins | Each team presents their demo |
| Final 15 mins | Skill file reveal + Feedback collection |

---

## What You Are Building

You will create a **Cursor Skill File** (a `.md` rule file placed inside `.cursor/rules/`) that instructs the Cursor Agent to autonomously perform the following pipeline:

```
INPUT (JIRA Story + UFT Excel)
        ↓
PHASE 0 — Parse Inputs
        ↓
PHASE 1 — Plan Test Cases
        ↓
PHASE 2 — Manual Browser Verification (Playwright MCP)
        ↓
PHASE 3 — Generate Playwright Scripts (Page Object Model)
        ↓
PHASE 4 — Execute Scripts + Self-Healing Loop
        ↓
REPORT — Migration summary + Healing log
```

Each phase is described in detail below.

---

## Input Files

You are free to choose **any web application** for this capstone:
- A public demo website
- Your own company's application
- Any web app your team has access to

You will need to prepare **two input files** for your chosen application:

### Input 1 — JIRA User Story (`.md` file)
Write a JIRA-style user story in Markdown format covering an end-to-end flow of your chosen application. It must include:
- User story statement (`As a... I want to... So that...`)
- Background / Context (app URL)
- Acceptance Criteria (AC-1 through AC-N) in Given/When/Then format
- Test Data table (with any hardcoded or random values)
- Notes for the automation agent

### Input 2 — UFT Keyword-Driven Excel (`.xlsx` file)
Create an Excel file with the following 4 sheets modelled after the UFT Keyword-Driven framework:

| Sheet Name | Purpose |
|---|---|
| `ObjectRepository` | All elements with page name, field name, field type, and Chrome XPath locator |
| `Actions` | List of logical action groups with `Run = Yes/No` flag |
| `TestSteps` | Every step with action, element reference, keyword, and value |
| `Framework_AUTFunctionality` | Master keyword dictionary |

> **Place both input files in:** `playwright-demo/inputs/`

---

## Phase-by-Phase Build Guide

### ⚙️ Phase 0 — Input Parsing

**What the agent must do:**
- Read the JIRA `.md` file — extract URL, Acceptance Criteria, and Test Data
- Read the UFT Excel — parse all 4 sheets
- Resolve element references from `TestSteps` → `ObjectRepository`
- Build an internal UFT Keyword → Playwright Action mapping table
- Produce a parsed summary before proceeding

**Hint:** Think about how the agent should handle `Value_Identifier = Reference` vs `Value_Identifier = Value`. What should it do differently for each?

---

### 📋 Phase 1 — Planning

**What the agent must do:**
- Group all `TestSteps` by their `Action` (in the order defined in the `Actions` sheet)
- Convert each group into a structured test case with:
  - Step number
  - Human-readable description
  - The Playwright action it maps to
  - Expected outcome
- Cross-reference every Acceptance Criteria from the JIRA story — confirm all are covered

**Hint:** The agent should produce a clear AC Coverage Table before moving on. If any AC is not covered by the steps, it should flag it.

---

### 🖥️ Phase 2 — Manual Browser Verification

**What the agent must do:**
- Use **Playwright MCP browser tools** to open a real browser
- Execute each planned step manually — navigate, click, fill, assert
- After each step, compare **actual browser state** against **expected outcome**
- Confirm every locator from the OR sheet resolves in the live DOM (exactly 1 match)
- Log ✅ PASS or ❌ FAIL per step with screenshots where required

**Hint:** The agent should NOT write any code in this phase. This phase is purely about verifying the flow works in a real browser before generating scripts.

---

### 🛠️ Phase 3 — Script Generation

**What the agent must do:**
- Generate Playwright TypeScript scripts using **Page Object Model (POM)**
- One Page Object class per page (locators + action methods)
- One single spec file for the entire E2E flow
- Use **only locators confirmed in Phase 2** — never assume
- Handle `RANDOM` value fields by generating random data at runtime

**Output structure:**
```
playwright-demo/
├── tests/
│   ├── pages/
│   │   ├── <PageName>Page.ts    ← one per page
│   └── e2e-flow.spec.ts         ← one spec for full E2E
```

**Hint:** Locators should use `data-test` attributes wherever available — they are the most stable selectors.

---

### ▶️ Phase 4 — Execution + Self-Healing

**What the agent must do:**
- Run the generated scripts:
  ```bash
  cd playwright-demo && npx playwright test --reporter=json 2>&1
  ```
- If **all pass** → proceed to Report Generation
- If **any fail** → trigger the Self-Healing loop:

#### Self-Healing Loop

| Step | What Happens |
|---|---|
| **Detect** | Parse JSON output — identify broken locator, file, line number |
| **Analyze** | Use Playwright MCP `browser_snapshot` — find what's actually in the DOM |
| **Guardrails** | Validate the candidate replacement (existence, uniqueness, element type, confidence ≥ 80%) |
| **Fix** | Replace only the broken selector string in the page object file |
| **Re-run** | Execute the test again — if pass, move on; if fail, repeat (max 3 iterations) |
| **Escalate** | After 3 failed iterations → write "Needs human review" in report → stop |

> **Rule:** Fix one locator at a time. Never batch multiple fixes. Never guess — always read the live DOM.

---

## Setup Instructions

### Step 1 — Project Setup
If Playwright is not installed on your machine, create a new folder and run:
```bash
npx init playwright@latest
```

### Step 2 — Place Your Skill File
```
playwright-demo/
└── .cursor/
    └── rules/
        └── SKILL.md        ← your skill file goes here
```

### Step 3 — Place Your Input Files
```
playwright-demo/
└── inputs/
    ├── your-jira-story.md
    └── your-uft-excel.xlsx
```

### Step 4 — Connect Playwright MCP in Cursor
Go to **Cursor → Settings → MCP → Add MCP Server** and add:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

### Step 5 — Run the Agent
- Open Cursor Chat (`Ctrl+L` / `Cmd+L`)
- Switch to **Agent mode**
- Type your trigger prompt, for example:
  ```
  Read the JIRA story and UFT Excel from the inputs folder and run the full migration agent.
  ```

---

## Deliverables

Each team must produce the following by end of session:

| # | Deliverable | Description |
|---|---|---|
| 1 | `SKILL.md` | The Cursor skill/rule file your team authored |
| 2 | `inputs/` | JIRA story `.md` + UFT Excel `.xlsx` |
| 3 | `tests/pages/*.ts` | Page Object files generated by the agent |
| 4 | `e2e-flow.spec.ts` | The full E2E spec file generated by the agent |
| 5 | `healing-report/*.md` | The timestamped healing + migration report |
| 6 | **Live Demo** | Walk the panel through the agent running end-to-end |

---

## Evaluation Criteria

Teams will be evaluated on the following:

| Criteria | Weight | What We Look For |
|---|---|---|
| **Input Quality** | 10% | JIRA story is well-structured; Excel covers all steps and elements correctly |
| **Skill File Design** | 25% | Phases are clearly defined; instructions are unambiguous; priority rules are stated |
| **Phase 0 & 1 Accuracy** | 15% | Agent correctly parses inputs and produces a structured test plan |
| **Phase 2 Verification** | 15% | Agent correctly verifies each step in the live browser before scripting |
| **Script Quality** | 15% | POM structure is clean; locators are accurate; random values handled correctly |
| **Self-Healing Logic** | 15% | Guardrails are well-defined; iteration limit is enforced; escalation is handled |
| **Report Completeness** | 5% | Migration map, AC coverage, and healing log are all present |
| **Demo Presentation** | Bonus | Clear explanation of how the agent works end-to-end |

---

## Rules & Constraints

1. **Do not share your skill file with other teams** during the session
2. **Excel always takes priority** over the JIRA story in case of any conflict
3. Self-healing must fix **one locator at a time** — no batch fixes
4. Maximum **3 iterations** per broken locator before escalating to human review
5. Every run must produce a **new timestamped report** — never overwrite an existing one

---

## Tips for Success

- ✅ **Start with Phase 0** — a clean input parsing phase makes every other phase easier
- ✅ **Be explicit in your skill file** — the more precise your instructions, the more reliably the agent follows them
- ✅ **Test your Excel manually first** — walk through the steps yourself before handing it to the agent
- ✅ **Keep the self-healing guardrails strict** — a low-confidence fix is worse than no fix
- ✅ **Document your design decisions** — the panel will ask why you made certain choices

---

## Need Help?

Your facilitator will be circulating throughout the session. Raise your hand or flag in the chat if your team is blocked. Focus on making progress phase by phase — a well-designed Phase 0 and Phase 1 is already a strong foundation.

**Good luck. Build something great. 🚀**

---

*Capstone Day — Autonomous Self-Healing Agent | UFT → Playwright Migration*
