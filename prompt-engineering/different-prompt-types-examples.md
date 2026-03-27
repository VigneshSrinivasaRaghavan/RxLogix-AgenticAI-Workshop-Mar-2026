# Prompt Engineering
## Module 3 — Practicing Different Prompt Types with Real Examples

---

# Agenda — Module 3

- How to Use This Session
- Instructional Prompts — Live Practice
- Contextual Prompts — Live Practice
- Formatting Prompts — Live Practice
- Open-Ended Prompts — Live Practice
- Specific Example Prompts — Live Practice
- Clarification Prompts — Live Conversation Demo
- Comparative Prompts — Live Practice
- Key Observations & Golden Rule

---

# How to Use This Session

**This is a Hands-On Module:**
- Every prompt in this session is designed to be run live — on ChatGPT, Gemini, Claude, or any AI tool you have access to
- You will see the difference between weak and strong prompts in real time

**What to Watch For in Every Demo:**
- How does the output change when you add more detail?
- How does the output change when you specify a format?
- How does a follow-up prompt improve the result without starting over?

**The Pattern for Each Prompt Type:**

| Step | What Happens |
|---|---|
| **Run the weak version first** | See what a vague prompt produces |
| **Run the strong version second** | See the immediate improvement |
| **Discuss the difference** | Understand exactly what changed and why |

> "The goal is not to memorise prompts. The goal is to develop the instinct to ask better questions."

---

# Instructional Prompts — Live Practice

**What to Focus On:**
- The AI follows a direct command with no background needed
- Output is clean, task-focused, and immediate
- One small instruction change can transform the entire output

**Demo 1 — Run Without Constraint First, Then With:**

| Version | Prompt |
|---|---|
| ❌ Without constraint | `List 5 best practices for writing effective automated test cases.` |
| ✅ With constraint | `List 5 best practices for writing effective automated test cases. Keep each point to one sentence.` |

**What Changes:** Without the constraint, the AI gives verbose multi-line explanations. With it, you get a tight, scannable list — ready to use immediately.

**Demo 2 — Bug Description Rewrite:**
> "Rewrite the following bug description in a clear and professional format suitable for a JIRA ticket: 'login button doesnt work sometimes when i click it fast multiple times not sure why maybe a timing issue'"

**Expected Output Structure:**
- Clear, descriptive bug title
- Steps to reproduce
- Expected vs. actual behaviour
- Possible root cause (timing / race condition)

---

# Contextual Prompts — Live Practice

**What to Focus On:**
- Run the same question with and without context
- Watch how dramatically the response changes when the AI understands your specific situation

**Demo — Without Context (Run First):**
> `What test cases should I write for a login feature?`

**Expected Output:** Generic list — valid/invalid credentials, empty fields, password case sensitivity. Broad, not specific to any application or risk area.

**Demo — With Context (Run Second):**
> "I am an automation engineer working on a mobile banking application. The login feature supports biometric authentication (fingerprint and face ID), a 4-digit PIN, and a standard username/password option. The app locks the account after 3 failed attempts and sends an OTP to the registered mobile number for account recovery. What test cases should I write to ensure this login feature works correctly and securely?"

**Expected Output Covers:**

| Area | Scenarios |
|---|---|
| Biometric Auth | Success, failure, unsupported device |
| PIN Entry | Valid, invalid, boundary values (3 failed attempts) |
| Account Lockout | Triggers correctly after 3 failures |
| OTP Recovery | Delivery, expiry, re-send, invalid OTP |
| Session Handling | Post-login behaviour, timeout |
| Auth Method Switching | Switching between biometric, PIN, and password |

---

# Formatting Prompts — Live Practice

**What to Focus On:**
- The content doesn't change — the structure does
- The same information presented differently has completely different usability

**Demo — Without Formatting (Run First):**
> `What are the different types of software testing?`

**Expected Output:** A paragraph or loosely structured response — types mixed together, hard to scan or reference quickly.

**Demo — With Formatting (Run Second):**
> "What are the different types of software testing? Present your answer as a table with three columns: Testing Type | Purpose (one sentence) | Example Scenario. Include at least 8 testing types."

**Expected Output:**

| Testing Type | Purpose | Example Scenario |
|---|---|---|
| Unit Testing | Validates individual components in isolation | Testing a single login validation function |
| Integration Testing | Verifies that modules work together correctly | Testing login module with the user database |
| End-to-End Testing | Validates complete user workflows | Full checkout flow from cart to payment confirmation |
| Regression Testing | Ensures new changes don't break existing features | Re-running full suite after a new feature release |
| Performance Testing | Measures system behaviour under load | Simulating 10,000 concurrent users on a payment page |
| Security Testing | Identifies vulnerabilities and access control gaps | Testing for SQL injection on a login form |
| UAT | Validates the system meets business requirements | Business users testing a new reporting feature |
| Exploratory Testing | Unscripted testing to discover unexpected issues | Manually exploring a new onboarding flow |

---

# Open-Ended Prompts — Live Practice

**What to Focus On:**
- There is no single correct answer — the goal is breadth and inspiration
- Use the AI as a brainstorming partner, not an answer machine

**Demo 1:**
> "What are some innovative ways AI could help automation engineers improve their test coverage without writing more test scripts?"

**Expected Output Areas:**
- AI-powered test generation from user stories or requirements
- Visual AI testing to catch UI anomalies automatically
- Self-healing test scripts that adapt to UI changes
- Intelligent test prioritisation based on code change impact
- Anomaly detection in test results to identify flaky tests

**Demo 2:**
> "What are the biggest challenges automation engineers face when maintaining large test suites, and what creative solutions could help address them?"

**Expected Output Areas:**

| Challenge | Creative Solution |
|---|---|
| Test flakiness and false positives | AI-based flakiness detection and auto-quarantine |
| High maintenance from frequent UI changes | Self-healing locators using AI element recognition |
| Slow regression suite execution | Intelligent test selection based on code diff analysis |
| Lack of clear test ownership | Automated ownership mapping from Git commit history |

> "You are not looking for one right answer. You are using the AI as a thinking partner — let it surprise you."

---

# Specific Example Prompts — Live Practice

**What to Focus On:**
- Grounding the prompt in a precise scenario forces the AI to produce output that is directly actionable — not generic
- The difference between a template and a solution

**Demo 1 — E-Commerce Checkout:**
> "A user adds 3 items to their shopping cart in an e-commerce application, applies a 20% discount coupon at checkout, and proceeds to payment. Write 5 detailed test cases for this specific scenario, including steps, expected results, and at least 2 negative test cases."

**Expected Test Cases Include:**
- ✅ Successful checkout with valid coupon — 20% discount correctly applied to total
- ✅ Coupon applied before and after adding items — discount recalculates correctly
- ❌ Checkout attempted with an expired coupon — appropriate error message shown
- ❌ Checkout attempted with a coupon exceeding usage limit — blocked with clear message
- ❌ Item removed from cart after coupon applied — total recalculates correctly

**Demo 2 — Automation Bug Report:**
> "An automation script is failing intermittently on the password reset flow. The script clicks the 'Forgot Password' link, enters the registered email, and waits for a confirmation message. The failure occurs randomly at the confirmation message step. Write a structured bug report for this issue."

**Expected Bug Report Structure:**
- **Title:** Intermittent failure on password reset confirmation step in automation script
- **Steps to Reproduce:** Defined clearly
- **Expected Behaviour:** Confirmation message appears consistently
- **Actual Behaviour:** Confirmation message intermittently not detected by script
- **Possible Root Cause:** Timing issue or dynamic element loading delay
- **Suggested Fix:** Add explicit wait for confirmation message element

---

# Clarification Prompts — Live Conversation Demo

**What to Focus On:**
- AI interaction is a conversation — not a one-shot query
- Each follow-up builds on the last — refine, don't restart

**Run This as a 3-Step Live Conversation:**

| Step | Prompt | Purpose |
|---|---|---|
| **Step 1** | `Explain what flaky tests are in automation testing.` | Get the initial technical response |
| **Step 2** | `That explanation was quite technical. Can you explain flaky tests using a simple real-world analogy that a non-technical stakeholder would understand?` | Simplify for a different audience |
| **Step 3** | `Good. Now give me 5 practical steps an automation engineer can take to reduce flaky tests in their test suite. Present it as a numbered action list.` | Get actionable output in a specific format |

**Expected Output — Step 3 Action List:**
- Add explicit waits instead of fixed sleep timers
- Isolate tests so they do not depend on execution order
- Use stable, unique test data for each run
- Configure the test runner to automatically retry failed tests to confirm flakiness
- Monitor, tag, and quarantine flaky tests separately for investigation

> "Notice what happened — one topic, three prompts, three completely different outputs. Same conversation. No starting over. That is how professionals use AI."

---

# Comparative Prompts — Live Practice

**What to Focus On:**
- The AI acts as an analyst — evaluating options side by side so you don't have to research each one separately
- Structured comparisons in seconds instead of hours

**Demo 1 — Testing Approaches:**
> "Compare end-to-end testing and unit testing. For each, explain what it tests, its key advantages, its limitations, and when you should use it. Present the comparison as a table."

**Expected Output:**

| Aspect | Unit Testing | End-to-End Testing |
|---|---|---|
| **What It Tests** | Individual functions or components in isolation | Complete user workflows across the full system |
| **Key Advantages** | Fast, precise, easy to debug | Validates real user journeys, catches integration issues |
| **Limitations** | Does not test component interactions | Slow, brittle, harder to maintain |
| **When to Use** | During development, for every function | Before releases, for critical user flows |

**Demo 2 — Framework Decision:**
> "I am deciding between a keyword-driven testing approach and a data-driven testing approach for our regression suite. Compare both covering: how they work, maintenance effort, scalability, and which type of project each is best suited for."

**Expected Output Highlights:**
- **Keyword-Driven:** Reusable keywords, accessible to non-technical testers, higher initial setup cost
- **Data-Driven:** Same script runs with multiple data sets, excellent for regression, easy to scale
- Clear guidance on which suits which project type

---

# Key Observations & The Golden Rule

**What We Observed Across All 7 Prompt Types:**

| Prompt Type | The Key Lesson |
|---|---|
| **Instructional** | Precision in your command = precision in the output |
| **Contextual** | More relevant context = more tailored, useful response |
| **Formatting** | Always specify structure — never let the AI decide the layout for you |
| **Open-Ended** | Use AI as a brainstorming partner — let it surface ideas you haven't considered |
| **Specific Example** | Ground your prompt in a real scenario for output that is immediately usable |
| **Clarification** | Refine, don't restart — every follow-up builds on the last |
| **Comparative** | Use AI as your analyst — structured comparisons in seconds, not hours |

**The Golden Rule:**

> "The quality of your prompt directly determines the quality of your output. Every prompt type is a tool — the more you practice, the faster you will know which tool to reach for."