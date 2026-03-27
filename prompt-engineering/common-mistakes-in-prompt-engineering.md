# Prompt Engineering
## Module 6 — Common Mistakes in Prompt Engineering

---

# Agenda — Module 6

- Why Mistakes Matter More Than You Think
- Mistake 1 — Being Too Vague or General
- Mistake 2 — Overly Complex Prompts
- Mistake 3 — Lack of Context
- Mistake 4 — Ambiguous Language
- Mistake 5 — Asking for Multiple Tasks in One Prompt
- Mistake 6 — Ignoring Prompt Refinement
- Mistake 7 — Expecting AI to Fill Knowledge Gaps
- Mistake 8 — Not Specifying Output Format
- Mistake 9 — Blindly Trusting AI Output
- Mistake 10 — Using AI for the Wrong Task
- Mistake 11 — Ignoring Conversation History Impact
- Summary & Key Takeaways

---

# Why Mistakes Matter More Than You Think

**The Problem With Bad Prompts:**
- A poorly written prompt doesn't just produce a bad answer — it produces a *confidently presented* bad answer
- AI models do not flag uncertainty the way a human colleague would — they generate fluent, structured output regardless of quality
- In a QA or engineering context, acting on flawed AI output can introduce defects, coverage gaps, or compliance risks

**The Good News:**
- Every mistake in this module is avoidable
- Most come down to one root cause — not giving the AI enough of the right information

**What We Cover:**

| # | Mistake | Core Problem |
|---|---|---|
| 1 | Too Vague | AI has no direction |
| 2 | Overly Complex | AI loses focus |
| 3 | No Context | AI gives generic output |
| 4 | Ambiguous Language | AI interprets incorrectly |
| 5 | Multiple Tasks at Once | AI gives shallow coverage |
| 6 | No Prompt Refinement | First draft accepted as final |
| 7 | Expecting AI to Guess | Unstated requirements missed |
| 8 | No Output Format Specified | Structure is unusable |
| 9 | Blind Trust in Output | Errors go undetected |
| 10 | Wrong Task for AI | Fundamental capability mismatch |
| 11 | Ignoring Conversation History | Earlier context corrupts later output |

---

# Mistake 1 — Being Too Vague or General

**Description:**
- Writing prompts that lack specific details is the most common mistake
- Vague prompts give the AI no direction — so it defaults to the most generic possible response

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Vague | `Write a test case.` | No feature, no context, no scope — output is broad and unhelpful |
| ✅ Specific | `Write a test case for a login screen, covering both successful and failed login attempts, including expected results for each scenario.` | Clear feature, clear scope, clear output expectation |

**How to Avoid It:**
- Before submitting a prompt, ask: *"If I gave this instruction to a new team member, would they know exactly what to produce?"*
- If the answer is no — add more detail before sending

> "Vague instructions produce vague outputs — every time. The more specific your prompt, the more useful the response."

---

# Mistake 2 — Overly Complex Prompts

**Description:**
- Long prompts with multiple instructions, contradictory constraints, or confusing language overwhelm the AI
- When the AI cannot determine which instruction to prioritise, it either ignores parts of the prompt or produces a shallow response to each part

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Overloaded | `Generate a login test case with different scenarios for valid and invalid inputs, covering various edge cases, including expected results, without making it too technical but also not too simple.` | Contradictory constraints — "not too technical but not too simple" gives the AI no clear target |
| ✅ Simplified | `Generate test cases for a login screen. Include valid and invalid input scenarios. For each, list the steps and expected result in simple, non-technical language.` | One clear task, one clear format, one clear tone instruction |

**How to Avoid It:**
- One prompt = one primary task
- If you have multiple requirements, use prompt chaining — one focused prompt per step
- Remove contradictory constraints — decide what you actually want before prompting

> "If your prompt is hard to read, it is hard for the AI to follow. Simplify first, then send."

---

# Mistake 3 — Lack of Context

**Description:**
- Leaving out important background information forces the AI to make assumptions
- Without context, the AI gives a generic response that could apply to any situation — which often applies to none of them

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ No Context | `Generate test data.` | No feature, no fields, no format — output is random and unusable |
| ✅ With Context | `Generate test data for a user registration form. Include 5 sets covering: valid usernames, valid and invalid email formats, passwords with and without special characters, and a blank field scenario.` | Clear feature, clear fields, clear coverage requirement |

**How to Avoid It:**
- Answer these four questions before writing your prompt:
- *What is the feature or system?*
- *Who is the user or audience?*
- *What are the constraints or requirements?*
- *What will this output be used for?*

> "Context helps the AI produce results that align with your actual situation. Without it, you get an answer to a question nobody asked."

---

# Mistake 4 — Ambiguous Language

**Description:**
- Words like "short," "detailed," "simple," "a few," or "brief" mean different things to different people — and to the AI
- Ambiguous language forces the AI to guess, and its interpretation may not match yours

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Ambiguous | `Write a short description.` | "Short" is subjective — output could be 1 sentence or 10 |
| ✅ Precise | `Write a 50-word description of the benefits of automated testing, written for a non-technical business stakeholder.` | Word count defined, topic defined, audience defined |

**Common Ambiguous Words to Replace:**

| Ambiguous Word | Replace With |
|---|---|
| Short / Brief | Exact word or character count |
| Detailed / Thorough | Specify what areas to cover |
| Simple | "Suitable for a non-technical audience" |
| A few | Exact number — "3" or "5" |
| Soon / Quickly | Specific timeframe or step count |

> "Specific instructions eliminate guesswork. If a word can be interpreted in more than one way — define it."

---

# Mistake 5 — Asking for Multiple Tasks in One Prompt

**Description:**
- Trying to get the AI to complete several unrelated tasks in a single prompt leads to incomplete or shallow responses
- The AI may focus on one part, skip another, or give surface-level coverage across all of them

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Multi-Task | `Generate test cases for login, write a summary of automation benefits, and explain regression testing.` | Three unrelated tasks — AI gives shallow output for each |
| ✅ Separated | Run three separate prompts — one per task | Each prompt gets full focus and produces a complete, detailed response |

**The Rule:**
- One prompt = one task
- If tasks are related and sequential → use **prompt chaining**
- If tasks are unrelated → use **separate conversations**

**How to Spot This Mistake:**
- Count the number of distinct deliverables in your prompt
- If the count is more than one — split it

> "Breaking tasks into separate prompts gives you more comprehensive answers. The AI does one thing very well — not three things adequately."

---

# Mistake 6 — Ignoring Prompt Refinement

**Description:**
- Many users accept the first AI response as the final output without testing or adjusting the prompt
- Prompt engineering is an iterative process — the first response is a starting point, not a finished product

**Side by Side:**

| Version | Prompt | Output Quality |
|---|---|---|
| ❌ Not Refined | `List benefits of automation.` | Too broad — generic list with no focus or depth |
| ✅ Refined | `List five specific benefits of test automation in a regression-heavy enterprise QA environment. Focus on speed, accuracy, and long-term cost reduction. Use one sentence per benefit.` | Focused, specific, immediately usable |

**The Refinement Process:**

| Step | Action |
|---|---|
| **Run** | Submit your initial prompt and review the output |
| **Evaluate** | Is it too generic? Too long? Wrong format? Missing something? |
| **Adjust** | Add specificity, context, constraints, or format instructions |
| **Rerun** | Submit the refined prompt and compare |
| **Repeat** | Continue until the output meets your standard |

> "Prompt refinement is not a sign that your first prompt failed — it is the normal process of getting to a high-quality output. Expect to iterate."

---

# Mistake 7 — Expecting AI to Fill Knowledge Gaps

**Description:**
- Users sometimes expect the AI to understand unstated requirements, implied context, or domain-specific details it was never given
- The AI does not have access to your project, your system, or your team's conventions — unless you tell it

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Assumptive | `Create a test case.` | AI doesn't know the feature, type, scope, or format required |
| ✅ Explicit | `Create a functional test case for the search feature in an e-commerce application. Cover both successful searches returning results and failed searches returning no results. Include steps and expected results.` | All necessary information provided — nothing left for the AI to guess |

**What the AI Does Not Know Unless You Tell It:**
- Your application's name, architecture, or business rules
- Your team's test case format or naming conventions
- Which regulatory standards apply to your domain
- What "done" looks like for your specific task

> "Explicit instructions produce targeted responses. Never assume the AI knows what you know — state everything that matters."

---

# Mistake 8 — Not Specifying Output Format

**Description:**
- Telling the AI *what* to produce but not *how* to present it is one of the most common and costly mistakes
- When no format is specified, the AI chooses its own structure — which often requires significant manual reformatting before it is usable

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ No Format | `List the test cases for a forgot password feature.` | AI may return a paragraph, a loose list, or an inconsistent structure — not directly usable |
| ✅ With Format | `List the test cases for a forgot password feature. Present each as a numbered item with these fields: Test Case Title, Precondition, Steps, and Expected Result.` | Structured, consistent, immediately usable in a test management tool or report |

**When Format Specification is Critical:**

| Output Will Be Used In | Format to Specify |
|---|---|
| Test management tool (JIRA, Zephyr) | Numbered list with defined fields |
| Slide deck or report | Table with specific columns |
| Application or pipeline | JSON or structured data format |
| Email or stakeholder communication | Paragraph with defined length and tone |

> "In engineering, the format of AI output determines whether it is directly usable or needs rework. Specifying format upfront saves significant time."

---

# Mistake 9 — Blindly Trusting AI Output

**Description:**
- Accepting AI-generated output as correct without reviewing or validating it is one of the most dangerous mistakes — especially in QA
- AI models can produce responses that sound confident and well-structured but are factually wrong, logically flawed, or missing critical scenarios
- This is known as an **AI hallucination** — the model generates plausible-sounding but incorrect content

**Real-World Example:**
- An automation engineer asks ChatGPT to generate test cases for an OAuth 2.0 authentication flow and copies them directly into the test suite without review
- The AI produces well-formatted test cases — but misses critical security scenarios such as token expiry handling, refresh token rotation, and scope validation
- The test suite appears complete but has significant coverage gaps in a security-critical feature

**How to Avoid It:**

| Rule | Action |
|---|---|
| **Treat output as a first draft** | Review every response with your domain expertise before using it |
| **Ask for gaps explicitly** | Follow up with: *"What scenarios might I be missing?"* or *"What edge cases have you not covered?"* |
| **Apply extra scrutiny to critical areas** | Security, performance, data integrity, and compliance outputs require the most careful review |
| **Never skip validation for regulated domains** | In pharmacovigilance, finance, or healthcare — AI output must always be verified by a qualified professional |

> "As QA professionals, your job is to find what is wrong. Apply the same critical mindset to AI output as you would to any deliverable you are asked to review."

---

# Mistake 10 — Using AI for the Wrong Task

**Description:**
- AI language models are powerful — but they have clear, fundamental limitations
- A common mistake is using AI for tasks it is structurally incapable of performing, such as accessing live systems, executing actual tests, or making decisions that require human accountability

**Side by Side:**

| Version | Prompt | Problem |
|---|---|---|
| ❌ Wrong Use | `Check our live application and tell me if the payment flow is working correctly.` | A language model cannot access your application, run tests, or verify real system behaviour |
| ✅ Right Use | `Based on the following payment flow description, generate a comprehensive set of test cases including edge cases and negative scenarios.` | AI generates the plan — humans or automation frameworks execute and verify |

**What AI Can and Cannot Do:**

| ✅ AI Can | ❌ AI Cannot |
|---|---|
| Generate test cases, scripts, and reports | Execute tests against a live system |
| Analyse requirements and identify gaps | Access your application, database, or network |
| Suggest strategies and approaches | Make accountable decisions on your behalf |
| Explain concepts and compare options | Guarantee factual accuracy without verification |

> "Use AI to plan, write, analyse, and suggest. Use your tools and expertise to execute, verify, and decide."

---

# Mistake 11 — Ignoring Conversation History Impact

**Description:**
- In a multi-turn conversation, earlier messages influence all later responses
- A poorly framed early message can bias or corrupt every subsequent response in the same conversation — even if later prompts are perfectly written

**Real-World Example:**
- An engineer starts a conversation by saying *"Assume our application has no security vulnerabilities"* while asking for general test planning help
- Later in the same conversation, they ask for security test cases
- The AI produces shallow security test cases because the earlier instruction anchored its thinking toward a "no vulnerabilities" assumption

**How to Avoid It:**

| Situation | What to Do |
|---|---|
| Switching to a significantly different task | Start a fresh conversation |
| Earlier context is no longer relevant | Explicitly reset: *"Ignore any previous assumptions. Treat the application as untested with all risk areas unverified."* |
| You notice responses drifting or becoming inconsistent | Start fresh and re-establish context cleanly |

**Why This Matters for Agentic AI:**
- In AI agents, conversation history and context management is a critical design consideration
- Understanding how earlier prompts influence later responses is foundational knowledge for building reliable, predictable agents

> "Be mindful of what you establish early in a conversation. The AI remembers — and it builds on everything you have said, whether you intended it to or not."

---

# Summary — 11 Common Mistakes at a Glance

| # | Mistake | How to Avoid It |
|---|---|---|
| 1 | **Too Vague** | Be specific — include feature, scope, and expected output |
| 2 | **Overly Complex** | One prompt, one task — chain for multi-step workflows |
| 3 | **No Context** | Answer: what, who, why, and what it will be used for |
| 4 | **Ambiguous Language** | Replace vague words with exact counts, definitions, and audience descriptions |
| 5 | **Multiple Tasks at Once** | Separate unrelated tasks into individual prompts |
| 6 | **No Prompt Refinement** | Treat the first response as a draft — iterate until it meets your standard |
| 7 | **Expecting AI to Guess** | State everything explicitly — the AI only knows what you tell it |
| 8 | **No Output Format** | Define structure upfront — table, list, JSON, or template |
| 9 | **Blind Trust in Output** | Review every response — treat AI output as a first draft, not a final deliverable |
| 10 | **Wrong Task for AI** | Use AI to generate and analyse — use tools and humans to execute and verify |
| 11 | **Ignoring Conversation History** | Start fresh for new tasks — explicitly reset context when needed |

---

# Key Takeaways — Avoiding Prompt Engineering Mistakes

**5 Rules to Carry Forward:**

| Rule | What It Means |
|---|---|
| ✅ **Be specific and clear** | The more precise your prompt, the more useful the response |
| ✅ **Always provide context** | The AI only knows what you tell it — never assume shared knowledge |
| ✅ **Always specify output format** | Never leave structure to chance when the output will be used directly in your work |
| ✅ **AI output is a first draft** | Review every response with your professional expertise — you are the quality gate |
| ✅ **Know AI's boundaries** | AI generates, suggests, and analyses — it does not execute, access live systems, or replace human judgement |

**Final Thought:**

> "Mastering these basics will help you avoid the most common pitfalls and maximise the value of Generative AI — whether you are generating test cases, building automation scripts, designing agents, or solving complex QA challenges. The AI is a powerful collaborator. You are the expert."