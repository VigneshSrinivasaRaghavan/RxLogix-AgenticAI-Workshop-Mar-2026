# Prompt Engineering
## Module 7 — Real-Time Tips & Tricks to Write Better Prompts

---

# Agenda — Module 7

- From Knowledge to Habit — What This Session Is About
- Tip 1 — Always Specify the Output Format
- Tip 2 — Use "Step by Step" for Complex Tasks
- Tip 3 — Assign a Role for Expert-Level Responses
- Tip 4 — Use "Explain Like I'm 5" for Simplified Explanations
- Tip 5 — Generate Multiple Variations for Better Selection
- Tip 6 — Use Section Labels to Organise Your Prompt
- Tip 7 — Tell the AI What NOT to Do
- Tip 8 — Set Output Length Limits
- Tip 9 — Use Delimiters to Separate Instructions from Content
- Tip 10 — Ask the AI to Identify What Is Missing
- Tip 11 — Use JSON or Structured Data for Technical Outputs
- Tip 12 — Iterative Prompt Refinement
- Tip 13 — The Prompt Clarity Checklist
- Key Takeaways

---

# From Knowledge to Habit

**What We Have Covered So Far:**
- Prompt types — the different ways to structure a single prompt
- Core techniques — Zero-Shot, Few-Shot, CoT, Role, System, Chaining, ReAct
- Common mistakes — and how to avoid every one of them

**What This Session Is About:**
- Practical, battle-tested tips that QA professionals and engineers can apply immediately
- Every tip includes a real, copy-pasteable example
- The goal is not just to know these tips — but to make them automatic habits

**The Difference Between Knowing and Doing:**

| Knowing | Doing |
|---|---|
| Understanding prompt types | Choosing the right type before you type |
| Knowing format matters | Always specifying format in every prompt |
| Understanding CoT | Adding "step by step" whenever the task is complex |
| Knowing AI can hallucinate | Reviewing every output before using it |

> "Knowing prompt engineering is one thing. Writing prompts that consistently deliver high-quality, usable results in real work is a different skill — and that is what this session builds."

---

# Tip 1 — Always Specify the Output Format

**Why This Matters:**
- When no format is specified, the AI decides how to present information — and it may not match what you need
- Specifying format ensures the output is directly usable without manual reformatting

**Real-Time Example:**
```
Write test cases for a login feature.

Format each test case as:
- Test Case ID
- Title
- Preconditions
- Steps
- Expected Result
```

**Why This Works:**
- The AI generates properly structured test cases that are immediately usable in a test plan, test management tool, or documentation — no reformatting needed

**Format Cheat Sheet:**

| Use Case | Format to Request |
|---|---|
| Test management tool | Numbered list with defined fields |
| Executive report or slide | Table with specific columns |
| Automation framework | JSON with defined schema |
| Stakeholder email | Short paragraphs with defined word count |
| JIRA ticket | Structured fields: Title, Steps, Expected, Actual |

> "Think of format instructions as a template you hand to the AI. The more precisely you define the structure, the less editing you do after."

---

# Tip 2 — Use "Step by Step" for Complex Tasks

**Why This Matters:**
- For complex reasoning, debugging, or multi-step analysis — asking the AI to think step by step forces it to break the problem down logically
- This dramatically improves accuracy and completeness compared to a direct-answer prompt

**Real-Time Example:**
> "Our automated regression suite has gone from completing in 40 minutes to taking over 3 hours. Walk me through a step-by-step analysis of what could be causing this, how to investigate each cause, and what the most likely root cause is."

**What Changes With "Step by Step":**

| Without | With |
|---|---|
| Generic list of possible causes | Structured investigation — one cause at a time |
| No prioritisation | Each cause evaluated for likelihood |
| No actionable next step | Specific recommendation on where to start |

**When to Use It:**
- Diagnosing a test failure or performance issue
- Planning a testing strategy for a new feature
- Analysing requirements for coverage gaps
- Root cause analysis of an automation failure

> " 'Step by step' is one of the simplest phrases you can add to a prompt — and one of the highest-impact ones. Use it any time the task involves diagnosis, planning, or multi-stage reasoning."

---

# Tip 3 — Assign a Role for Expert-Level Responses

**Why This Matters:**
- Assigning the AI a specific role activates domain-specific knowledge, vocabulary, and perspective
- The same question without a role gets a generic answer — with a role, it gets an expert-level response

**Two Framing Options — Both Work:**

| Framing | Best For |
|---|---|
| **"Act as..."** | Technical, practitioner-level responses |
| **"Think like..."** | Strategic, audience-specific responses |

**Real-Time Example 1 — Act As:**
```
Act as a Senior SDET with deep expertise in API automation
and CI/CD pipelines. Review the following test strategy and
identify weaknesses in our automation approach, coverage
gaps, and risks to our release quality.

Test Strategy Summary:
- We automate only UI tests using Selenium
- API layer is tested manually
- Tests run once a day in the CI/CD pipeline
- No performance or security testing is currently planned
```

**Real-Time Example 2 — Think Like:**
> "Think like a QA Manager presenting to a CTO. How would you build a business case for investing in test automation, focusing on ROI, risk reduction, and long-term cost savings?"

> "Every AI agent you will build in this course starts with a role definition in its system prompt. Practising role prompting now directly prepares you for agent design."

---

# Tip 4 — Use "Explain Like I'm 5" for Simplified Explanations

**Why This Matters:**
- AI naturally defaults to technical language when answering technical questions
- ELI5 (Explain Like I'm 5) forces the AI to strip away jargon and use simple language and analogies
- Ideal for explaining complex concepts to non-technical stakeholders, clients, or junior team members

**Real-Time Example:**
> "Explain what API rate limiting is and why it matters for testing — explain it like I'm 5, using a simple real-world analogy."

**The Difference It Makes:**

| Without ELI5 | With ELI5 |
|---|---|
| "Rate limiting is a technique used to control the number of requests a client can make to an API within a defined time window to prevent abuse and ensure service availability." | "Imagine a water tap. If too many people turn it on at once, the water pressure drops for everyone. API rate limiting is like a rule that says only a certain number of people can use the tap at once — so the water stays strong for everyone." |

**When to Use It:**
- Explaining a technical defect to a product manager or client
- Onboarding a new junior team member
- Preparing training material for a non-technical audience
- Simplifying a complex concept for a stakeholder presentation

> "As QA professionals, you often need to bridge the gap between technical findings and non-technical stakeholders. ELI5 prompting gives you that bridge instantly."

---

# Tip 5 — Generate Multiple Variations for Better Selection

**Why This Matters:**
- When you need options rather than a single answer — asking for multiple variations gives you a range to choose from or combine
- Particularly powerful for communication tasks where the same information needs to reach different audiences

**Real-Time Example:**
```
Generate 3 different versions of a bug report for the
following issue. Each version should vary in tone and
detail level:
- Version 1: Brief and executive-facing
- Version 2: Detailed and developer-facing
- Version 3: Structured for a test management tool

Issue: The payment confirmation screen does not appear
after a successful transaction. The user is redirected
back to the cart page instead.
```

**What You Get:**

| Version | Audience | Style |
|---|---|---|
| **Version 1** | CTO / Product Director | 3-4 sentence summary, business impact focused |
| **Version 2** | Developer | Full technical detail, error context, stack trace guidance |
| **Version 3** | JIRA / Zephyr | Structured fields — Title, Steps, Expected, Actual, Severity |

> "No rewriting needed — just pick the right version for the right person. The AI does the audience adaptation for you."

---

# Tip 6 — Use Section Labels to Organise Your Prompt

**Why This Matters:**
- When your prompt contains multiple parts — instructions, context, constraints, and data — writing them as one block of text makes it hard for the AI to process correctly
- Clear section labels organise your prompt so the AI handles each part independently and accurately

**Real-Time Example:**
```
Task:
Write test cases for a password reset feature.

Context:
This is for a mobile banking application. The password
reset flow uses OTP verification via registered mobile
number. The OTP expires after 5 minutes.

Requirements:
- Cover successful and failed password reset scenarios
- Include OTP expiry and resend scenarios
- Include account lockout after 3 failed OTP attempts

Output Format:
Present as a numbered list. Each test case must include:
Title, Precondition, Steps, and Expected Result.
```

**Why This Works:**
- The AI processes each labelled section independently — understanding the task, the context, the constraints, and the format as distinct inputs
- This produces a far more accurate and complete response than mixing everything into a single paragraph

**The Four Standard Sections:**

| Section | What Goes Here |
|---|---|
| **Task** | What you want the AI to do |
| **Context** | Background information and situation |
| **Requirements** | Constraints, rules, and must-haves |
| **Output Format** | Structure, length, and presentation |

---

# Tip 7 — Tell the AI What NOT to Do

**Why This Matters:**
- AI models tend to over-generate — adding introductions, summaries, disclaimers, and extra context you didn't ask for
- Explicitly telling the AI what to exclude keeps the output clean, focused, and directly usable

**Real-Time Example:**
```
Generate a test execution summary report based on the
following results.

Do NOT include:
- Any introduction or closing paragraph
- Passed test cases
- Recommendations or suggestions

Focus ONLY on:
- Failed test cases with their error details
- Total pass/fail count
- Overall pass rate percentage

Results:
Total Tests: 120 | Passed: 104 | Failed: 16
Failed Tests: [Payment timeout - checkout flow],
[Invalid OTP not rejected - login],
[Session not expiring after 30 mins - security],
[Profile update not saving - user settings]
```

**Why This Works:**
- The negative constraints act as a filter — the AI removes everything you don't need before generating, rather than you having to remove it afterwards

**Combine Include + Exclude for Maximum Control:**

| Use | Effect |
|---|---|
| "Focus only on..." | Narrows the AI's scope to what matters |
| "Do not include..." | Removes unwanted additions before they appear |
| Both together | Tightest possible control over output content |

> "Combining what to include with what to exclude gives you the tightest control over AI output — especially when the result goes directly into a report or stakeholder communication."

---

# Tip 8 — Set Output Length Limits

**Why This Matters:**
- Without length guidance, the AI calibrates response length on its own — sometimes too long, sometimes too brief
- Setting explicit length limits ensures the output fits your actual use case — a slide, a ticket, a report section

**Real-Time Example 1 — Short Output:**
> "Summarise the key benefits of test automation for a one-slide executive summary. Maximum 60 words."

**Real-Time Example 2 — Controlled Output:**
> "Write test cases for session timeout functionality. Include exactly 5 test cases — no more, no less. Each test case should be no longer than 5 lines."

**Length Control Options:**

| Constraint Type | Example Instruction |
|---|---|
| Word count | "Maximum 60 words" |
| Sentence count | "Summarise in exactly 3 sentences" |
| Item count | "List exactly 5 points — no more, no less" |
| Line count per item | "Each test case no longer than 5 lines" |
| Paragraph count | "Write in 2 short paragraphs" |

> "Length limits force the AI to prioritise the most important information rather than padding the response. The result is tighter, more impactful output that fits your actual context."

---

# Tip 9 — Use Delimiters to Separate Instructions from Content

**Why This Matters:**
- When your prompt contains both instructions AND content for the AI to process — such as a log file, user story, or bug description — mixing them in plain text can confuse the AI
- Delimiters clearly mark where your instruction ends and the data to be processed begins

**Real-Time Example:**
```
Review the test execution log below. Identify all
failures, provide a possible root cause for each,
and suggest a fix. Only analyse what is inside the
log — do not make assumptions about anything outside it.

---LOG START---
Test: Login with valid credentials | Status: PASS
Test: Login with invalid password | Status: FAIL | Error: NullPointerException at AuthService.java:142
Test: Password reset via email | Status: FAIL | Error: Timeout waiting for confirmation message element
Test: Session expiry after 30 mins inactivity | Status: PASS
Test: Concurrent login from two devices | Status: FAIL | Error: 500 Internal Server Error at SessionManager.java:87
---LOG END---
```

**Why This Works:**
- The delimiters `---LOG START---` and `---LOG END---` clearly signal where the instruction ends and the data begins
- The AI analyses only the content inside the delimiters — producing a cleaner, more accurate analysis

**Common Delimiter Patterns:**

| Delimiter Style | Use Case |
|---|---|
| `---LOG START--- / ---LOG END---` | Log files and execution reports |
| `---DOCUMENT START--- / ---DOCUMENT END---` | Requirements, test plans, user stories |
| `---DATA START--- / ---DATA END---` | Test data, API responses, database records |

> "Delimiters become especially important in Agentic AI — used in system prompts to separate instructions, context, and data cleanly."

---

# Tip 10 — Ask the AI to Identify What Is Missing

**Why This Matters:**
- Most people use AI to generate content — very few use it to critically review what they have already created
- Asking the AI to identify gaps turns it into a peer reviewer — surfacing blind spots and missing scenarios you may have overlooked

**Real-Time Example:**
```
Below are the test cases I have written for a payment
gateway integration. Review them critically and tell me
what important scenarios, edge cases, security risks,
or coverage gaps I have missed.

Do NOT rewrite or improve the existing test cases —
only list what is missing and briefly explain why each
missing scenario matters.

My Current Test Cases:
1. Verify successful payment with a valid credit card
2. Verify payment fails with an expired credit card
3. Verify payment fails with insufficient funds
4. Verify order confirmation email is sent after payment
5. Verify user is redirected to order summary after payment
```

**What the AI Will Likely Surface as Missing:**
- Network timeout during payment processing
- Duplicate transaction prevention
- 3D Secure authentication scenarios
- Payment with a blocked or stolen card
- Currency conversion edge cases
- Session expiry mid-payment
- Partial payment handling

> "This is one of the most underused techniques in professional AI usage. Apply your QA instinct — use AI to find what is wrong with your own work before it reaches production."

---

# Tip 11 — Use JSON Format for Technical Outputs

**Why This Matters:**
- When working with APIs, automation frameworks, or data-driven testing — you often need machine-readable output
- Asking the AI to respond in JSON produces output ready to use directly in automation scripts or tools — no manual conversion needed

**Real-Time Example:**
```
Generate test data for a user registration API in JSON
format. Include 5 test users covering:
- Valid user with all fields complete
- User with missing mandatory email field
- User with an already registered email address
- User with a password not meeting complexity requirements
- User with special characters in the username field

Use this JSON structure for each user:
{
  "testCaseId": "",
  "scenario": "",
  "username": "",
  "email": "",
  "password": "",
  "expectedStatusCode": "",
  "expectedMessage": ""
}
```

**Why This Works:**
- The AI respects the defined JSON schema and populates each field correctly for all 5 scenarios
- Output is directly importable into a data-driven automation framework — no manual conversion

**When to Use Structured Output:**

| Output Type | Use Case |
|---|---|
| **JSON** | API test data, automation scripts, data-driven frameworks |
| **CSV** | Bulk test data import into test management tools |
| **XML** | Legacy system integrations, config file generation |
| **Markdown Table** | Documentation, reports, Notion or Confluence pages |

---

# Tip 12 — Iterative Prompt Refinement

**Why This Matters:**
- The first AI response is rarely the best response
- Iterative refinement is the practice of deliberately improving your prompt based on what the previous response lacked — treating AI as a conversation partner, not a one-shot machine

**The Refinement Process:**

| Step | Action |
|---|---|
| **Run** | Submit your initial prompt and read the output honestly |
| **Evaluate** | Is it too generic? Wrong format? Missing something critical? |
| **Adjust** | Add specificity, context, constraints, or format instructions |
| **Rerun** | Submit the refined prompt and compare outputs |
| **Repeat** | Continue until the output meets your professional standard |

**Real-Time Example:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Initial | `Write test cases for an API endpoint.` | Too generic — basic happy path only, no structure, no technical detail |
| ✅ Refined | `Write test cases for a REST API POST endpoint that creates a new user account. Include positive, negative, and boundary test cases. For each provide: Test Case Title, HTTP Method, Request Body, Expected Response Code, and Expected Response Body. Include at least 8 test cases.` | Structured, specific, technically accurate, directly usable |

> "Professional AI users rarely settle for the first response. Build the habit of evaluating every AI output critically and refining once before using it in your actual work."

---

# Tip 13 — The Prompt Clarity Checklist

**Why This Matters:**
- Before sending any important prompt, a 30-second mental checklist prevents the most common mistakes
- This checklist combines everything covered in this session into a pre-send review habit

**The Checklist — Run This Before Every Important Prompt:**

| # | Check | Question to Ask Yourself |
|---|---|---|
| 1 | ✅ **Task** | Have I clearly stated what I want the AI to do? |
| 2 | ✅ **Context** | Have I provided enough background for the AI to understand my specific situation? |
| 3 | ✅ **Format** | Have I specified the output format I need? |
| 4 | ✅ **Constraints** | Have I set limits on length, scope, or content? |
| 5 | ✅ **Focus** | Is this prompt focused on one task — or am I asking for too many things at once? |
| 6 | ✅ **Clarity** | Have I used clear, unambiguous language with no room for misinterpretation? |
| 7 | ✅ **Exclusions** | Have I told the AI what NOT to include? |
| 8 | ✅ **Examples** | Have I provided a template or example if a specific format is required? |

> "This checklist takes 30 seconds and can save you 10 minutes of refinement. Over time, running through it becomes second nature — and your first prompts will be significantly stronger."

---

# Key Takeaways — Real-Time Tips & Tricks

**6 Habits to Build From Today:**

| Habit | What It Means in Practice |
|---|---|
| ✅ **Format is not optional** | Always specify structure — never leave it to the AI to decide |
| ✅ **Structure your prompt like a briefing** | Use section labels, delimiters, and clear separation between instructions and data |
| ✅ **Constraints are your best friend** | Define what to include, what to exclude, how long, and what format |
| ✅ **Use AI as a reviewer too** | Ask the AI to find what is missing — not just to generate |
| ✅ **Refine, don't restart** | One or two rounds of refinement consistently produces significantly better output |
| ✅ **Run the checklist** | Before every important prompt — 30 seconds, every time |

**The Complete Prompt Engineering Toolkit:**

| Module | What You Learned |
|---|---|
| Module 1 | What prompt engineering is and why it matters |
| Module 2 | The 7 prompt types and when to use each |
| Module 3 | Practicing prompt types with real examples |
| Module 4 | 8 core techniques — from Zero-Shot to ReAct |
| Module 5 | Practicing core techniques with real examples |
| Module 6 | 11 common mistakes and how to avoid them |
| Module 7 | 13 real-time tips and tricks for consistent quality |

> "Every tip in this session is a habit, not a one-time technique. The more consistently you apply them, the faster and more effective your AI interactions become — whether you are writing test cases, analysing failures, building automation scripts, or designing AI agents."