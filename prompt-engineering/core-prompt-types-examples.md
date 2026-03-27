# Prompt Engineering
## Module 5 — Practicing Core Prompt Techniques with Real Examples

---

# Agenda — Module 5

- How to Use This Session
- Zero-Shot Prompting — Live Practice
- One-Shot Prompting — Live Practice
- Few-Shot Prompting — Live Practice
- Chain-of-Thought Prompting — Live Practice
- Role / Persona Prompting — Live Practice
- System Prompting — Live Practice
- Prompt Chaining — Live Practice
- ReAct Prompting — Simulated Live Demo
- Key Observations & Golden Rule

---

# How to Use This Session

**This is a Hands-On Module:**
- Every prompt in this session is complete, accurate, and ready to copy and paste directly into any AI tool
- Run each prompt live — on ChatGPT, Claude, Gemini, or any AI tool you have access to

**The Demo Pattern for Each Technique:**

| Step | What Happens |
|---|---|
| **Run the weak version first** | See what happens without the technique applied |
| **Run the strong version second** | See the immediate, measurable improvement |
| **Discuss the difference** | Understand exactly what changed and why |

**What to Watch For:**
- How does the output change when you apply the technique?
- How does reasoning, structure, and depth improve?
- Which technique would you reach for in your own daily work?

> "The goal is not to memorise prompts. The goal is to develop the instinct to choose the right technique for the right task."

---

# Zero-Shot Prompting — Live Practice

**What to Focus On:**
- The AI performs the task with zero guidance or examples
- No demonstrations, no format instructions — just a clear task description
- Notice the quality ceiling — and where it starts to break down

**Demo 1:**
> `What is the difference between smoke testing and sanity testing in software QA? Explain clearly in simple terms.`

**Expected Output:**
- Smoke Testing: Broad, shallow test run on a new build to verify it is stable enough for further testing — done first, covers critical paths only
- Sanity Testing: Narrow, focused test run after a specific bug fix or change to verify that the fix works and has not broken related functionality
- Key Difference: Smoke is done on a new build before any deep testing begins; Sanity is done after a targeted change to verify a specific area

**Demo 2:**
> `List the key information that should be included in a well-written bug report.`

**Expected Output — A structured list covering:**
- Bug title
- Environment details (OS, browser, version)
- Steps to reproduce
- Expected result
- Actual result
- Severity and priority
- Screenshots or logs
- Reported by / assigned to

**Discussion After Both Demos:**
> "The AI answered correctly with zero guidance. Now think — what kind of tasks would zero-shot NOT work well for? What would you need to add?"

---

# One-Shot Prompting — Live Practice

**What to Focus On:**
- One single example completely shapes the format and structure of the output
- The AI reads the example, identifies the pattern, and applies it to the new input consistently

**Demo 1 — Bug Report Conversion:**

> I will give you a plain text bug description. Convert it into a structured bug report following the exact format shown in the example.
>
> **Example:**
> Plain Text: The profile picture upload fails when the file size exceeds 2MB.
> Structured Bug Report:
> - Title: Profile picture upload fails for files exceeding 2MB
> - Steps to Reproduce: 1. Log in. 2. Go to Profile Settings. 3. Click Upload Profile Picture. 4. Select a file larger than 2MB. 5. Click Upload.
> - Expected Result: Application displays a clear error message informing the user of the file size limit.
> - Actual Result: Upload fails silently with no error message shown.
> - Severity: Medium | Priority: High
>
> Now convert this:
> Plain Text: The search results page crashes when the user enters more than 100 characters in the search bar.

**Expected Output:**
- Title: Search results page crashes when search input exceeds 100 characters
- Steps to Reproduce: Navigate to search, enter 100+ characters, submit search
- Expected Result: Application handles long input gracefully with a validation message
- Actual Result: Search results page crashes
- Severity and Priority filled in appropriately

**Demo 2 — Test Case Summary from User Story:**

> I will give you a user story. Write a test case summary following the exact format shown in the example.
>
> **Example:**
> User Story: As a user, I want to log out so that my session is securely ended.
> Test Case Summary:
> - Test Case ID: TC-001
> - Title: Verify successful logout terminates user session
> - Precondition: User is logged in
> - Steps: 1. Click profile icon. 2. Select Logout.
> - Expected Result: User is logged out, session terminated, login page displayed
> - Test Type: Functional
>
> Now write a test case summary for:
> User Story: As a user, I want to receive an email notification when my password is successfully changed so that I am aware of any account security changes.

**Expected Output:**
- Test Case ID: TC-002
- Title: Verify email notification is sent upon successful password change
- Precondition: User is logged in with a registered email address
- Steps: Navigate to security settings, change password, submit
- Expected Result: User receives an email confirming the password change
- Test Type: Functional

---

# Few-Shot Prompting — Live Practice

**What to Focus On:**
- Multiple examples reinforce the pattern more strongly than one
- The AI becomes more consistent and accurate as the number of well-chosen examples increases

**Demo 1 — Test Case Classification:**

> Classify the following test cases into one of these categories: Functional, Performance, Security, or Usability. Follow the pattern shown in the examples.
>
> Example 1: Verify a registered user can log in with valid credentials → **Functional**
> Example 2: Verify the application maintains response time under 2 seconds with 5,000 concurrent users → **Performance**
> Example 3: Verify the application blocks SQL injection attempts on the login form → **Security**
> Example 4: Verify error messages are clearly displayed and easy to understand for incorrect password entry → **Usability**
>
> Now classify:
> 1. Verify the payment gateway processes a transaction within 3 seconds under normal load
> 2. Verify sensitive user data such as passwords and card numbers are encrypted in the database
> 3. Verify a user can successfully add an item to the cart and proceed to checkout
> 4. Verify the navigation menu is intuitive and accessible for first-time mobile users

**Expected Output:**

| Test Case | Classification |
|---|---|
| Payment gateway processes within 3 seconds | ✅ Performance |
| Sensitive data encrypted in database | ✅ Security |
| Add to cart and proceed to checkout | ✅ Functional |
| Navigation menu intuitive for mobile users | ✅ Usability |

**Demo 2 — Test Case Title Generation:**

> Generate a one-line test case title for each scenario, following the naming convention shown in the examples.
>
> Example 1: Check what happens when a user logs in with an incorrect password → *Verify login fails when incorrect password is entered*
> Example 2: Check if the system sends a confirmation email after registration → *Verify confirmation email is sent upon successful user registration*
> Example 3: Check if the form blocks submission when mandatory fields are empty → *Verify form submission is blocked when mandatory fields are left empty*
>
> Now generate titles for:
> 1. Check what happens when a user uploads an unsupported file format
> 2. Check if the session expires after 30 minutes of inactivity
> 3. Check if the discount code is correctly applied at checkout

**Expected Output:**
- Verify file upload fails when an unsupported file format is selected
- Verify user session expires after 30 minutes of inactivity
- Verify discount code is correctly applied to the total amount at checkout

---

# Chain-of-Thought Prompting — Live Practice

**What to Focus On:**
- Run WITHOUT CoT first — show the generic output
- Run WITH CoT second — show the structured, reasoned, actionable output
- The difference in depth and accuracy will be immediately obvious

**Demo 1 — Side by Side:**

| Version | Prompt |
|---|---|
| ❌ Without CoT | `An automated regression suite that used to complete in 45 minutes is now taking over 3 hours to run. What is the cause?` |
| ✅ With CoT | `An automated regression suite that used to complete in 45 minutes is now taking over 3 hours to run. Think step by step through the possible causes. For each, explain how you would investigate it and how likely it is to be the root cause. Then give a final recommendation on where to start the investigation.` |

**Expected CoT Output — Step by Step:**
- Step 1: Check if new test cases were added recently — more tests = longer run time
- Step 2: Check for hard-coded sleep timers or fixed waits recently introduced in test scripts
- Step 3: Investigate if the test environment is running on degraded infrastructure
- Step 4: Check if previously parallel tests are now running sequentially due to a configuration change
- Step 5: Look for tests making repeated slow external API calls or database queries
- **Most Likely Cause:** Hard-coded waits or loss of parallel execution from a configuration change
- **Recommendation:** Compare current test configuration against the last known good configuration — check parallelisation settings first

**Demo 2 — Production vs Staging Failure:**
> `A critical end-to-end test for the checkout flow is failing in production but passing in staging. Walk me through a step-by-step analysis of why this could be happening, what evidence to look for at each step, and what the most likely root cause is.`

**Expected CoT Output — Step by Step:**
- Step 1: Compare environment configurations — databases, API endpoints, environment variables
- Step 2: Check if production uses live payment gateways while staging uses mocks or stubs
- Step 3: Investigate whether the failure is consistent or intermittent — consistent = configuration; intermittent = timing or data
- Step 4: Review recent production deployments — any code or config changes just before the failure?
- Step 5: Verify all third-party dependencies behave identically across both environments
- **Most Likely Root Cause:** Test relies on a third-party payment gateway that is live in production but mocked in staging
- **Recommended Next Step:** Review all external dependencies in the checkout flow and verify each one is consistent across both environments

---

# Role / Persona Prompting — Live Practice

**What to Focus On:**
- Run the same prompt with and without the role assignment
- Watch how depth, tone, credibility, and quality change dramatically with a well-defined role

**Demo 1 — Test Plan Review:**

| Version | Prompt |
|---|---|
| ❌ Without Role | `Review this test plan and identify any gaps: [paste test plan below]` |
| ✅ With Role | `You are a senior QA architect with 15 years of experience in enterprise software testing, specialising in e-commerce platforms. You are known for identifying critical gaps that others miss. Review the following test plan and provide a detailed critique covering: missing test types, risks with the current approach, test data concerns, automation strategy gaps, and whether the timeline and exit criteria are realistic. [paste test plan below]` |

**Test Plan to Review (use in both versions):**
- Application: E-commerce web application
- Scope: Login, Product Search, Add to Cart, Checkout, Payment
- Test Types: Functional Testing only
- Environment: Staging | Test Data: Copied from production
- Automation: None planned | Timeline: 5 days
- Exit Criteria: All functional test cases pass

**Expected Output With Role — Key Gaps Identified:**

| Gap Area | Finding |
|---|---|
| **Missing Test Types** | No performance, security, cross-browser, mobile, or negative testing |
| **Test Data Risk** | Using copied production data in staging is a serious data privacy and compliance violation — PII must never be used in non-production environments |
| **Automation Gap** | No automation for a regression-heavy e-commerce platform creates long-term speed and coverage risks |
| **Timeline** | 5 days for a payment-critical e-commerce platform is extremely aggressive — high risk of insufficient coverage |
| **Exit Criteria** | "All functional tests pass" is too narrow — no performance benchmarks, security sign-off, or accessibility standards |

**Demo 2 — Automation Roadmap:**
> `You are an experienced automation engineer who specialises in helping teams transition from manual to automated testing. A QA team has 500 manual regression test cases, a 3-month timeline, and 4 testers with basic automation knowledge. Give them a realistic, practical roadmap for building their automation framework from scratch.`

**Expected Output — 3-Month Roadmap:**

| Month | Focus | Target |
|---|---|---|
| **Month 1** | Framework setup, tool selection, team training | Automate top 50 high-priority smoke tests |
| **Month 2** | Expand to critical regression paths, CI/CD integration, reporting | 100-120 automated tests stable in pipeline |
| **Month 3** | Scale coverage, stabilise flaky tests, document framework | 150-200 automated tests, maintainable and documented |

- Key Advice: Do not try to automate all 500 — focus on high-value, high-frequency tests first
- Team Guidance: Pair experienced automators with beginners for knowledge transfer throughout

---

# System Prompting — Live Practice

**What to Focus On:**
- A system prompt transforms a general-purpose AI into a focused, purpose-built assistant
- Demonstrate in-scope responses AND out-of-scope boundary handling

**How to Set a System Prompt:**

| Tool | How to Set It |
|---|---|
| **ChatGPT** | Settings → Personalisation → Custom Instructions |
| **API Playground** | Use the `system` role in the messages array |
| **This Demo** | Paste the system prompt first, clearly labelled, then run user prompts separately |

**System Prompt — Set This First:**
> "You are QA-Assist, a specialised AI assistant for software quality assurance professionals. Your expertise covers test case design, bug reporting, test strategy, automation planning, and QA best practices. You only respond to questions related to software testing, quality assurance, and automation. If asked anything outside this scope, politely let the user know and suggest they use a general-purpose AI assistant. Always respond in a clear, structured, and professional tone."

**In-Scope Prompt 1:**
> `Can you help me write test cases for a two-factor authentication feature?`

**Expected Output Covers:**
- Successful 2FA with valid OTP
- Expired OTP handling
- Invalid OTP entry and retry limits
- OTP resend functionality
- Account lockout after multiple failed OTP attempts
- 2FA bypass attempt handling

**In-Scope Prompt 2:**
> `What is the best way to handle test data management in an automated regression suite?`

**Expected Output Covers:**
- Use dedicated test databases — never production data
- Generate synthetic test data programmatically
- Reset test data before each test run
- Avoid hardcoded data in scripts
- Use data-driven testing frameworks for scalability

**Out-of-Scope Prompt — Run This to Show Boundaries:**
> `Can you recommend a good project management tool for our team?`

**Expected Output:**
> *"I'm QA-Assist, here to help specifically with software testing and quality assurance. For project management tool recommendations, I'd suggest consulting a general-purpose AI assistant. Is there anything QA-related I can help you with?"*

---

# Prompt Chaining — Live Practice

**The Scenario:**
- A new **Guest Checkout** feature has been added to an e-commerce application
- Users can now complete a purchase without creating an account
- We will build a complete QA workflow across 4 chained prompts

**Run Each Step Sequentially — Copy Output Into the Next Prompt**

| Step | Prompt Goal | Input | Output |
|---|---|---|---|
| **Step 1** | Extract all testable requirements from the user story | User story text | Functional + non-functional requirements list |
| **Step 2** | Generate detailed test cases from requirements | Step 1 output | 8-12 test cases with ID, title, steps, expected result |
| **Step 3** | Identify automation vs. manual candidates | Step 2 output | Categorised table with reasoning for each decision |
| **Step 4** | Generate automation script outline | Step 3 automation candidates | Tool-agnostic script outline per test case |

**Step 1 Prompt:**
> `Read the following user story and extract all functional and non-functional requirements a QA engineer would need to test: "As a guest user, I want to complete a purchase without creating an account so I can check out quickly. The guest checkout should collect my shipping address, contact email, and payment details. After the order is placed, I should receive an order confirmation email. I should also have the option to create an account after checkout using the details I already provided."`

**Step 2 Prompt:**
> `Based on the following requirements [paste Step 1 output], write detailed test cases covering both positive and negative scenarios. For each include: Test Case ID, Title, Precondition, Steps, and Expected Result.`

**Step 3 Prompt:**
> `From the following test cases [paste Step 2 output], identify which are strong automation candidates and which should remain manual. Present as a table: Test Case Title | Automation Candidate (Yes/No) | Reason.`

**Step 4 Prompt:**
> `For the automation candidates below [paste Step 3 output], write a high-level tool-agnostic automation script outline. For each include: test method name, setup required, key actions to automate, and assertions to verify.`

**Expected Final Output Quality:**

| Automation Candidates | Manual Candidates |
|---|---|
| Successful guest checkout flow | Mobile UX experience and visual review |
| Order confirmation email trigger | Post-checkout account creation usability |
| Field validation and error handling | Accessibility review of the checkout flow |
| Payment failure scenarios | Edge case exploratory testing |

---

# ReAct Prompting — Simulated Live Demo

**What to Focus On:**
- Simulate the ReAct reasoning loop in ChatGPT so students can visualise how an AI agent thinks and acts
- This is conceptual now — students will see it fully automated when building agents

**Demo Prompt:**
> `I want you to act as a QA investigation agent using the ReAct framework. Work through the problem by alternating between Thought (your reasoning), Action (what you would do next), and Observation (what you find) — until you reach a Final Answer.`
>
> `Problem: Our nightly automated regression suite ran last night and 23 test cases failed. Normally we see 0-2 failures. The failures are spread across the Login, Payment, and User Profile modules. Investigate this systematically and identify the most likely root cause.`
>
> `Begin your ReAct investigation now.`

**Expected ReAct Output:**

| Stage | Content |
|---|---|
| **Thought 1** | 23 failures across multiple modules suggests a systemic issue — not individual defects. Check for environment or deployment changes first. |
| **Action 1** | Check the deployment log for any releases or configuration changes before last night's run. |
| **Observation 1** | A new build was deployed at 11:45 PM — 15 minutes before the regression suite started at midnight. |
| **Thought 2** | The timing strongly suggests the deployment triggered the failures. Review the changelog for this build. |
| **Action 2** | Review the deployment changelog for the build released at 11:45 PM. |
| **Observation 2** | A database schema update was included — two column names in the Users table were renamed. |
| **Thought 3** | Renamed columns would break any test querying or updating those columns. Login, Payment, and User Profile all interact with the Users table — this explains the spread. |
| **Action 3** | Cross-reference the renamed columns with the 23 failed test cases to confirm the connection. |
| **Observation 3** | All 23 failed test cases reference the renamed columns in test data setup or API response mapping. |
| **Final Answer** | Root cause: database schema update renamed two Users table columns. Fix: update test data setup scripts and API response mappings, re-run failed tests to confirm resolution, and establish a process to notify QA of schema changes before deployment. |

> "When we build AI agents, the agent does exactly this — automatically, without you writing each Thought and Action manually. What you just saw is the reasoning brain of an AI agent."

---

# Key Observations & The Golden Rule

**What We Observed Across All 8 Techniques:**

| Technique | The Key Lesson from Practice |
|---|---|
| **Zero-Shot** | Works great for clear tasks — know when to escalate |
| **One-Shot** | One example locks in format — use it whenever structure matters |
| **Few-Shot** | More examples = higher consistency — essential for classification tasks |
| **Chain-of-Thought** | Always use for complex problems — reasoning dramatically improves accuracy |
| **Role / Persona** | The right role transforms depth, credibility, and quality of output |
| **System Prompting** | The foundation of every AI agent — defines identity, scope, and boundaries |
| **Prompt Chaining** | Each step builds on the last — compounding quality improvement |
| **ReAct** | The engine of Agentic AI — reason, act, observe, repeat |

**The Golden Rule:**

> "Choosing the right technique is as important as writing the right prompt. As you build AI-powered workflows and agents, these techniques become your core engineering toolkit — not optional extras."