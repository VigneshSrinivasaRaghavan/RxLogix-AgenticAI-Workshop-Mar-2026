# Prompt Engineering
## Module 2 — Different Types of Prompts

---

# Agenda — Module 2

- What Are Prompt Types and Why Do They Matter?
- Instructional Prompts
- Contextual Prompts
- Formatting Prompts
- Open-Ended Prompts
- Specific Example Prompts
- Clarification Prompts
- Comparative Prompts
- When to Use Which Prompt Type
- Combining Prompt Types
- Summary & Key Takeaways

---

# What Are Prompt Types — and Why Do They Matter?

**The Core Idea:**
- Different tasks require different ways of asking
- Knowing which prompt type to use helps you get more accurate, relevant, and useful responses from AI — faster

**You Don't Need to Memorise the Names:**
- Focus on understanding **when** and **why** to use each type
- With practice, choosing the right type becomes instinct

**The 7 Prompt Types We'll Cover:**

| # | Prompt Type | One-Line Purpose |
|---|---|---|
| 1 | **Instructional** | Give the AI a direct task to execute |
| 2 | **Contextual** | Give the AI background to tailor its response |
| 3 | **Formatting** | Control how the AI structures its output |
| 4 | **Open-Ended** | Invite broad, exploratory responses |
| 5 | **Specific Example** | Ground the AI in a precise scenario |
| 6 | **Clarification** | Ask the AI to go deeper or reframe |
| 7 | **Comparative** | Ask the AI to compare or evaluate options |

---

# Instructional Prompts

**Definition:**
- The most direct type of prompt — you give the AI a clear, specific command and it executes it
- No ambiguity — you tell the AI exactly what to do, what to produce, and sometimes how to produce it
- Works best when you have a well-defined task in mind

**Example:**
> "Summarise the following paragraph in three bullet points: [paste paragraph]"

**Expected Output:**
- Three concise bullet points capturing the key ideas — no extra commentary, no filler

**When to Use:**
- Rewriting an email
- Generating a list
- Translating text
- Extracting key information from a document

> "Think of instructional prompts like briefing a new employee. The clearer and more specific your instruction, the better the result. Vague instructions lead to vague outputs."

---

# Contextual Prompts

**Definition:**
- Provides the AI with background information, a specific scenario, or relevant details before asking it to respond
- Without context → generic answer. With context → tailored, relevant answer
- The more relevant context you provide, the more accurate and useful the output

**Example:**
> "I am a product manager at a fintech startup. We are launching a mobile payment app for first-time smartphone users in rural areas with limited internet connectivity. What are the top UX considerations we should prioritise?"

**Expected Output:**
- UX recommendations specific to low-connectivity environments, first-time users, and mobile payment scenarios — not a generic UX checklist

**When to Use:**
- Drafting communication for a specific audience
- Analysing a scenario unique to your industry
- Solving a problem tied to your specific project constraints

> "Imagine asking a consultant for advice with no background vs. explaining your business, users, and constraints. Contextual prompts work the same way — more context, more useful output."

---

# Formatting Prompts

**Definition:**
- Instructs the AI on **how to structure or present** its response — not what to say, but how to say it
- You can ask for bullet points, numbered lists, tables, JSON, markdown, step-by-step guides, one-liners, or any structure that fits your needs

**Example:**
> "List the pros and cons of remote work. Present your response as a two-column table with 'Pros' on the left and 'Cons' on the right. Include at least five points in each column."

**Expected Output:**
- A clean two-column table with five or more well-articulated pros and cons — not a paragraph of text

**When to Use:**
- Generating JSON output to feed into an application
- Creating a table for a slide deck or report
- Structuring output for a specific tool or template

> "Without a formatting prompt, the AI decides how to present information — and it may not match what you need. Always specify the format when structure matters."

---

# Open-Ended Prompts

**Definition:**
- Gives the AI freedom to explore a topic broadly and generate a detailed, expansive response
- Unlike instructional prompts that narrow focus, open-ended prompts invite the AI to think widely
- Ideal for brainstorming, idea generation, and exploring possibilities without a predefined answer in mind

**Example:**
> "What are some innovative ways AI could transform how small businesses manage customer relationships over the next five years?"

**Expected Output:**
- A rich, multi-perspective response covering various possibilities — from AI-powered personalisation to predictive customer service — going beyond obvious answers

**When to Use:**
- Early stages of problem-solving
- Brainstorming new features or strategies
- Exploring creative ideas you haven't thought of yet

> "Open-ended prompts are like asking a smart colleague — 'What do you think we could do here?' — and letting them run with it. You want breadth, not just one answer."

---

# Specific Example Prompts

**Definition:**
- Grounds the AI's response in a concrete, well-defined scenario
- Instead of asking a general question, you provide a precise situation, constraint, or example
- Eliminates vagueness and forces the AI to produce output that is directly actionable and relevant

**Example:**
> "A user tries to log in to a mobile banking app with a correct username but an incorrect password three times in a row. Write three test cases covering this scenario — including the steps, expected behaviour, and what the app should do after the third failed attempt."

**Expected Output:**
- Three detailed, structured test cases with clear steps, expected results, and edge case handling — directly applicable to the described scenario

**When to Use:**
- Writing test cases for a known feature
- Drafting an email for a specific situation
- Generating code for a clearly defined problem

> "The more specific your scenario, the less the AI has to guess. Specific example prompts are the difference between getting a template and getting a solution."

---

# Clarification Prompts

**Definition:**
- Used **after** an initial AI response to ask the AI to go deeper, explain further, correct a misunderstanding, or approach the same topic from a different angle
- Part of an iterative conversation with the AI — refining and building on previous outputs rather than starting from scratch

**Example — In Sequence:**

| Turn | Prompt |
|---|---|
| **Initial Prompt** | `What is retrieval-augmented generation?` |
| **AI Response** | Gives a detailed technical explanation |
| **Clarification Prompt** | `That was too technical. Can you explain it again using a simple real-world analogy, as if explaining to someone who has never worked in tech?` |
| **New Output** | A simplified, analogy-driven explanation accessible to a non-technical audience |

**When to Use:**
- AI response is too complex, too vague, or off-topic
- You want a different perspective or format on the same content
- You need the AI to simplify, expand, or reframe its answer

> "Working with AI is a conversation, not a one-shot transaction. Clarification prompts let you steer without starting over."

---

# Comparative Prompts

**Definition:**
- Asks the AI to evaluate, contrast, or compare two or more options, approaches, tools, or concepts
- The AI analyses each option against the other and presents a structured comparison
- Helps you make informed decisions or understand key differences clearly

**Example:**
> "Compare REST APIs and GraphQL APIs. For each, explain how they work, their key strengths, their limitations, and which type of project each is best suited for. Present the comparison as a table."

**Expected Output:**

| Aspect | REST API | GraphQL API |
|---|---|---|
| **How It Works** | Fixed endpoints per resource | Single endpoint, client defines query |
| **Strengths** | Simple, widely supported | Flexible, reduces over-fetching |
| **Limitations** | Over/under-fetching of data | Steeper learning curve |
| **Best For** | Public APIs, simple CRUD apps | Complex apps with varied data needs |

**When to Use:**
- Evaluating technology or tool choices
- Comparing strategies or business options
- Helping stakeholders understand trade-offs

> "Comparative prompts turn the AI into an analyst — giving you a structured side-by-side view in seconds instead of hours of manual research."

---

# When to Use Which Prompt Type — Quick Decision Guide

**Ask Yourself These Questions:**

| Question | Use This Prompt Type |
|---|---|
| Do I need a **direct task** done? | ✅ Instructional Prompt |
| Does the AI need to understand **my specific situation**? | ✅ Contextual Prompt |
| Do I need the output in a **specific structure or layout**? | ✅ Formatting Prompt |
| Do I want to **explore ideas or brainstorm freely**? | ✅ Open-Ended Prompt |
| Do I need a response based on a **precise scenario**? | ✅ Specific Example Prompt |
| Do I want the AI to **go deeper or explain differently**? | ✅ Clarification Prompt |
| Do I need to **compare or evaluate options**? | ✅ Comparative Prompt |

> "In practice, you will rarely use just one prompt type. The real skill is knowing how to **combine** them — which is exactly what we'll look at next."

---

# Combining Prompt Types — Real-World Example

**Why Combine Prompt Types?**
- Real-world tasks are rarely simple
- Combining prompt types gives you more control over both the **content** and the **structure** of the AI's response

**Side-by-Side Comparison:**

| Approach | Prompt | Output Quality |
|---|---|---|
| ❌ **Single Type** (Instructional only) | `Write a project status update.` | Generic, one-size-fits-all — may not fit your project, audience, or format |
| ✅ **Combined** (Instructional + Contextual + Formatting) | `Write a project status update for our mobile app launch. The project is 80% complete, currently delayed by two weeks due to API integration issues. The audience is senior leadership with no technical background. Present the update in three short paragraphs: current status, key blockers, and next steps.` | Polished, leadership-ready — contextually accurate, non-technical, and structured exactly as requested |

> "Think of prompt types like ingredients in a recipe. Each one adds something specific. The right combination gives you a result that a single ingredient never could."

---

# Summary — Prompt Types at a Glance

| Prompt Type | Purpose | Example |
|---|---|---|
| **Instructional** | Direct task execution | `Summarise this article in five bullet points.` |
| **Contextual** | Tailor response to your situation | `I am a startup founder launching a B2B SaaS product. What pricing strategies should I consider?` |
| **Formatting** | Control output structure | `List the top five cloud providers and their key features in a comparison table.` |
| **Open-Ended** | Broad, exploratory, creative responses | `What are some unconventional ways AI could improve employee onboarding?` |
| **Specific Example** | Actionable output from a precise scenario | `Write three test cases for a checkout flow where a discount code is applied at payment.` |
| **Clarification** | Go deeper, simplify, or reframe | `Can you explain that using a simpler analogy?` |
| **Comparative** | Evaluate and contrast options | `Compare Agile and Waterfall for a government software project.` |

---

# Key Takeaways — Different Types of Prompts

**What We Covered:**
- There are 7 core prompt types — each suited to a different kind of task or need
- Choosing the right type improves output quality without changing the AI model itself

**3 Rules to Remember:**

| Rule | What It Means |
|---|---|
| ✅ **Match the type to the task** | Don't use an open-ended prompt when you need a precise output |
| ✅ **Iterate, don't restart** | Use clarification prompts to refine — not a brand new prompt every time |
| ✅ **Combine for best results** | Contextual + Formatting + Instructional together beats any single type alone |

**Coming Up Next:**
- These prompt types are your intuitive toolkit
- In the next module, we go deeper into **industry-standard prompting techniques** — Zero-Shot, Few-Shot, Chain-of-Thought, and more — which form the foundation of professional AI use and Agentic AI systems

> "Mastering prompt types is about developing a habit of thinking before you type — what do I need, and what is the best way to ask for it?"