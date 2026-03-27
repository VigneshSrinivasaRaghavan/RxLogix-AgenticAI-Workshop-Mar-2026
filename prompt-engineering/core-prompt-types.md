# Prompt Engineering
## Module 4 — Core Prompt Techniques

---

# Agenda — Module 4

- From Prompt Types to Prompt Techniques — What's the Difference?
- Zero-Shot Prompting
- One-Shot Prompting
- Few-Shot Prompting
- Chain-of-Thought (CoT) Prompting
- Role / Persona Prompting
- System Prompting
- Prompt Chaining
- ReAct Prompting — Reasoning + Acting
- Summary & Key Takeaways

---

# From Prompt Types to Prompt Techniques

**What We Covered in Module 2 & 3:**
- Prompt *types* — the structure and purpose of how you ask
- Instructional, Contextual, Formatting, Open-Ended, Specific Example, Clarification, Comparative

**What We Cover Now:**
- Prompt *techniques* — industry-standard methods used by AI professionals, researchers, and engineers worldwide
- These techniques power everything from simple AI assistants to complex Agentic AI systems

**The Key Difference:**

| | Prompt Types | Prompt Techniques |
|---|---|---|
| **Focus** | How you structure a single prompt | How you engineer AI behaviour and reasoning |
| **Used By** | Anyone using AI | AI professionals, engineers, agent builders |
| **Scope** | One interaction | Entire workflows and agent systems |

> "Understanding these techniques will make you a more effective and confident AI practitioner — and prepare you for building Agentic AI systems."

---

# Zero-Shot Prompting

**What It Is:**
- Asking the AI to perform a task with **no examples or demonstrations**
- The AI relies entirely on its pre-trained knowledge to respond
- The most common form of prompting — most people use it without knowing it has a name

**Why It Works:**
- Modern AI models are trained on massive amounts of text data
- They already understand a wide range of tasks, concepts, and formats — without needing examples

**Example:**
> `Explain what regression testing is in simple terms.`

**Expected Output:** A clear, beginner-friendly explanation of regression testing — what it is, why it is done, and when it is used. No examples were needed to guide the AI.

**When to Use vs. When to Move On:**

| Situation | What to Do |
|---|---|
| Task is clear and straightforward | ✅ Zero-Shot is enough |
| Output is too generic or inaccurate | ➡️ Move to One-Shot or Few-Shot |
| Task involves complex multi-step reasoning | ➡️ Move to Chain-of-Thought |

> "Zero-shot is your starting point. If the output isn't good enough, that's your signal to move to a more guided technique."

---

# One-Shot Prompting

**What It Is:**
- Providing the AI with **exactly one example** before asking it to perform the same task on new input
- The single example acts as a template — showing the AI the format, tone, and structure you expect

**Why It Works:**
- One example is often enough to shift the AI from a generic response to one that matches your specific style or format
- Particularly useful when you have a consistent output pattern you want the AI to follow

**Example:**

> I will give you a bug description and you will convert it into a structured bug report.
>
> **Example:**
> Bug Description: The search bar doesn't return results when special characters are entered.
> Bug Report:
> - Title: Search bar fails to return results for special character inputs
> - Steps to Reproduce: 1. Navigate to the search bar. 2. Enter a special character such as "@" or "#". 3. Press Enter.
> - Expected Result: Relevant search results are displayed.
> - Actual Result: No results are returned and no error message is shown.
> - Severity: Medium
>
> Now convert this:
> Bug Description: The checkout button becomes unresponsive after applying a discount code on the payment page.

**Expected Output:** A structured bug report following the exact same format — Title, Steps to Reproduce, Expected Result, Actual Result, and Severity — applied to the checkout button issue.

> "One-shot prompting is powerful for standardising outputs. Show the AI one example of your team's format — it will follow it consistently."

---

# Few-Shot Prompting

**What It Is:**
- Providing the AI with **multiple examples** — typically 2 to 5 — before asking it to perform the task
- Each example reinforces the pattern, format, and style you expect
- Gives the AI a stronger signal to produce consistent and accurate outputs

**Why It Works:**
- Multiple examples reduce ambiguity — the AI identifies the pattern across all examples and applies it reliably to new inputs
- The more consistent your examples, the more consistent the output

**Example:**

> Classify the following test cases as Functional, Performance, or Security.
>
> Example 1: Verify that the login page accepts valid credentials and redirects to the dashboard. → **Functional**
> Example 2: Verify that the application handles 10,000 simultaneous users with response time under 3 seconds. → **Performance**
> Example 3: Verify that the API endpoint rejects requests without a valid authentication token. → **Security**
>
> Now classify:
> Verify that the password reset email is sent within 30 seconds of the request.

**Expected Output:** Performance — the AI follows the pattern from three examples and correctly identifies the timing-based test as performance-related.

**When to Use:**

| Use Few-Shot When... | Reason |
|---|---|
| Output must follow a strict format | Multiple examples reinforce the exact pattern |
| Zero-shot or one-shot gives inconsistent results | More examples reduce ambiguity |
| Classifying, categorising, or labelling data | Examples teach the AI your classification logic |

> "In Agentic AI, few-shot prompting is used to teach agents how to format outputs, make decisions, and follow workflows — all through examples rather than code."

---

# Chain-of-Thought (CoT) Prompting

**What It Is:**
- Instructing the AI to **think through a problem step by step** before arriving at a final answer
- Instead of jumping to a conclusion, the AI reasons out loud — breaking the problem into logical steps and working through each one sequentially

**Why It Works:**
- AI models perform significantly better on complex, multi-step problems when asked to reason through the steps first
- The reasoning process helps the AI catch errors and arrive at more accurate conclusions

**How to Trigger It — Add One of These Phrases:**
- *"Think step by step."*
- *"Walk me through your reasoning."*
- *"Explain your thought process before giving the final answer."*

**Side-by-Side Example:**

| Version | Prompt | Output Quality |
|---|---|---|
| ❌ Without CoT | `An automated test is passing locally but failing in the CI/CD pipeline. What is the cause?` | Generic list of possible causes — no structured reasoning |
| ✅ With CoT | `An automated test is passing locally but failing in the CI/CD pipeline. Think step by step through the possible causes, eliminate unlikely ones, and identify the most probable root cause with a recommended fix.` | Structured reasoning through environment differences, timing, dependencies — leading to a specific root cause and fix |

**Expected CoT Output Steps:**
- Step 1: Compare local vs. CI/CD environment — OS, browser version, dependencies
- Step 2: Check for hardcoded paths or local-only environment variables
- Step 3: Examine timing — CI/CD may run faster, causing timing-sensitive tests to fail
- Step 4: Check for missing test data or database state differences
- **Most Probable Cause:** Environment variable or dependency mismatch
- **Recommended Fix:** Add environment configuration checks and use relative paths

> "Chain-of-Thought is one of the most powerful techniques in Agentic AI. When an agent needs to plan, debug, or decide — CoT is what enables it to reason rather than just react."

---

# Role / Persona Prompting

**What It Is:**
- Assigning a specific **identity, expertise, or persona** to the AI before asking it to respond
- By telling the AI who it is, you shape the tone, depth, language, and perspective of its entire response

**Why It Works:**
- AI models are trained on content written by people with vastly different expertise levels and roles
- Assigning a role activates the knowledge, vocabulary, and communication style associated with that role

**Side-by-Side Example:**

| Version | Prompt |
|---|---|
| ❌ Without Role | `Review this test plan and identify any gaps. [paste test plan]` |
| ✅ With Role | `You are a senior QA architect with 15 years of experience in enterprise software testing. Your expertise includes test strategy, risk-based testing, and automation frameworks. Review the following test plan and identify gaps in coverage, unaddressed risks, and improvements to the overall testing strategy. [paste test plan]` |

**What Changes in the Output:**
- Without role: General review with surface-level observations
- With role: Expert-level review identifying specific coverage gaps, risk areas, and strategic recommendations — written in the authoritative tone of a senior QA professional

**When to Use:**

| Use Case | Role Prompt Example |
|---|---|
| Expert domain review | "You are a senior security engineer..." |
| Audience-appropriate communication | "You are a technical writer explaining to non-technical users..." |
| Building AI agents | "You are QA-Assist, a specialised QA support agent..." |

> "Every AI agent has a role prompt behind the scenes. It is what makes a support bot sound different from a coding assistant — even if they use the exact same underlying AI model."

---

# System Prompting

**What It Is:**
- A special set of instructions given to the AI **before any user interaction begins**
- Defines the AI's role, behaviour, boundaries, tone, and constraints for the entire session
- Set in advance by a developer or AI designer — not written during the conversation

**System Prompt vs. User Prompt:**

| | System Prompt | User Prompt |
|---|---|---|
| **Who Sets It** | Developer / AI Designer | End User |
| **When** | Before the conversation starts | During the live interaction |
| **Purpose** | Defines who the AI is and how it behaves | Defines what the user wants in that moment |
| **Scope** | Applies to the entire session | Applies to that specific exchange |

**Example — QA-Assist Agent:**

**System Prompt (set by developer):**
> "You are QA-Assist, an AI assistant specialised in software quality assurance. You help QA engineers write test cases, analyse bug reports, review test plans, and suggest testing strategies. You only answer questions related to software testing and quality assurance. If asked anything outside this scope, politely inform the user that you can only assist with QA-related topics. Always respond in a clear, professional, and concise manner."

**User Prompt:** `Can you help me write test cases for a forgot password feature?`
**Output:** Focused, professional test cases for the forgot password feature — entirely within the QA domain.

**Out-of-Scope Test:**
**User Prompt:** `What is the best restaurant in New York?`
**Output:** *"I'm QA-Assist, here to help with software testing and quality assurance. For restaurant recommendations, I'd suggest checking Google Maps or Yelp!"*

> "When we build AI agents in this course, writing an effective system prompt will be one of your most important tasks — it is how you define an agent's identity, expertise, and boundaries using plain English."

---

# Prompt Chaining

**What It Is:**
- Breaking a complex task into a **sequence of smaller, connected prompts**
- The output of one prompt becomes the input of the next
- Guides the AI through a structured workflow, one focused step at a time

**Why It Works:**
- A single prompt has limits — asking the AI to do too many things at once reduces quality at every step
- Chaining keeps each step focused, and the cumulative result is far more accurate and complete

**Example — QA Workflow Using Prompt Chaining:**

| Step | Prompt | Output |
|---|---|---|
| **Step 1** — Analyse Requirements | `Read the following user story and identify all functional requirements that need to be tested: "As a user, I want to reset my password by receiving a one-time link on my registered email that expires after 15 minutes."` | List of requirements — link delivery, expiry, single-use, registered email validation |
| **Step 2** — Generate Test Cases | `Based on the following requirements [paste Step 1 output], write detailed test cases covering both positive and negative scenarios.` | Comprehensive test cases built directly from the extracted requirements |
| **Step 3** — Identify Automation Candidates | `From the following test cases [paste Step 2 output], identify which are best suited for automation and which should remain manual. Explain your reasoning for each decision.` | Categorised list — repetitive and data-driven cases flagged for automation, exploratory cases flagged for manual |

> "Prompt chaining is the foundation of how Agentic AI works. An AI agent is essentially a system that automatically chains prompts together — passing outputs from one step to the next — to complete complex tasks without human intervention at each stage."

---

# ReAct Prompting — Reasoning + Acting

**What It Is:**
- An advanced technique that combines **Reasoning** and **Acting** in a continuous loop
- The AI alternates between thinking about what to do next, taking an action, observing the result, and reasoning again
- This loop continues until the task is complete

**The ReAct Loop:**

| Stage | What Happens |
|---|---|
| **Thought** | The AI reasons about what needs to be done next |
| **Action** | The AI takes an action — searches, calls a tool, writes code, queries data |
| **Observation** | The AI observes the result of the action |
| **Repeat** | The AI reasons again based on the observation and decides the next action |
| **Final Answer** | The loop ends when the task is complete |

**Conceptual Example — Regression Failure Analysis:**
- **Task:** Find all failing test cases from last night's regression run and suggest fixes
- **Thought:** I need to retrieve last night's test execution report first
- **Action:** Access the test execution report
- **Observation:** 12 failures — 8 in payment module, 4 in login module
- **Thought:** Analyse payment module failures first — they are the majority
- **Action:** Examine error logs for the 8 payment failures
- **Observation:** All 8 show a timeout error on the payment gateway API call
- **Thought:** This suggests an environment or configuration issue, not a code defect
- **Action:** Check if the payment gateway API endpoint changed in the latest deployment
- **Observation:** API endpoint URL was updated in the latest deployment but not reflected in the test environment
- **Final Answer:** Root cause — API endpoint mismatch between test environment and latest deployment. Fix — update test environment configuration and re-run the 8 failed tests

> "ReAct is what separates a basic AI chatbot from a true AI agent. A chatbot responds. An agent using ReAct thinks, acts, observes, and adapts — just like a human engineer working through a problem systematically."

---

# Summary — Core Prompt Techniques at a Glance

| Technique | What It Does | Best Used When |
|---|---|---|
| **Zero-Shot** | Ask AI with no examples | Task is simple and well-defined |
| **One-Shot** | Provide one example to guide output format | You have a specific format to follow |
| **Few-Shot** | Provide multiple examples for consistency | Output must follow a strict or repeatable pattern |
| **Chain-of-Thought** | Ask AI to reason step by step | Task is complex or involves multi-step logic |
| **Role / Persona** | Assign AI a specific identity or expertise | You need expert-level or role-specific responses |
| **System Prompting** | Define AI behaviour before conversation starts | Building AI agents or purpose-built assistants |
| **Prompt Chaining** | Break complex tasks into sequential prompts | Task has multiple dependent stages |
| **ReAct** | Combine reasoning and acting in a loop | Building or understanding AI agents |

---

# Key Takeaways — Core Prompt Techniques

**5 Rules to Remember:**

| Rule | What It Means |
|---|---|
| ✅ **Start simple, escalate when needed** | Always try zero-shot first — only add complexity when the output isn't good enough |
| ✅ **Show, don't just tell** | One-shot and few-shot prompting demonstrate what you want — examples beat descriptions |
| ✅ **Chain for complexity** | If one prompt isn't producing quality output, break the task into a focused chain |
| ✅ **Role and system prompts define agent identity** | These are how you program an AI agent's personality, expertise, and boundaries in plain English |
| ✅ **ReAct is the engine of Agentic AI** | Reasoning + Acting + Observing — this loop is how modern AI agents operate autonomously |

**The Bridge to What's Next:**
- Everything covered in this module — reasoning, acting, chaining, roles, system prompts — comes together when we build Agentic AI systems
- You will see each of these techniques working in practice in the hands-on sessions ahead

> "These are not academic concepts. Every technique in this module is actively used in real AI systems today. You are now equipped to use them — and to understand how they power the agents we will build together."