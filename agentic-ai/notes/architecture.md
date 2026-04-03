# Agentic AI Training — RxLogix
## Section 3 — Architecture of Agentic AI

---

# Agenda — Architecture of Agentic AI

- The Big Picture — How Agentic AI is Structured
- Core Component 1 — Reasoning Engine
- Core Component 2 — Memory System
- Core Component 3 — Tool Integration
- Core Component 4 — Action Executor
- How Components Talk to Each Other
- The Observe-Reason-Act Loop in Detail
- Architecture in a Real QA Scenario
- Key Takeaways

---

# The Big Picture — How Agentic AI is Structured

**Why Architecture Matters:**
- Understanding what is inside an Agentic AI system helps you build better agents
- Every agent you build in this course uses these same components
- Knowing the architecture helps you debug when agents behave unexpectedly

**The Four Core Components:**

| Component | Role | Analogy |
|---|---|---|
| Reasoning Engine | Thinks and plans | The brain |
| Memory System | Stores and recalls context | The notebook |
| Tool Integration | Connects to external systems | The hands |
| Action Executor | Carries out decisions | The legs |

**How They Fit Together:**
- The Reasoning Engine receives the goal and breaks it into steps
- The Memory System provides context from past interactions
- The Tool Integration layer connects to APIs, databases, and services
- The Action Executor carries out the decisions made by the Reasoning Engine
- All four work in a continuous loop until the goal is achieved

> "An Agentic AI system is only as strong as its weakest component. A powerful reasoning engine with no tools is just a chatbot. Great tools with no reasoning is just automation."

---

# Core Component 1 — Reasoning Engine

**What It Is:**
- The brain of the Agentic AI system
- Powered by a Large Language Model — GPT-4o, Claude, Gemini, or open-source alternatives
- Receives the high-level goal and breaks it down into actionable steps
- Makes decisions at every step of the workflow

**What It Does:**
- Understands the goal provided by the human
- Breaks complex objectives into smaller sub-tasks
- Decides which tool to use at each step
- Evaluates results and determines next action
- Handles unexpected situations by reasoning through them

**Reasoning Strategies:**

| Strategy | What It Means | When Used |
|---|---|---|
| Chain-of-Thought | Thinks step by step before acting | Complex multi-step problems |
| ReAct | Reasons then acts, then reasons again | Tool-use scenarios |
| Tree-of-Thought | Explores multiple paths before deciding | High-stakes decisions |
| Reflection | Reviews its own output and improves | Quality-sensitive tasks |

**In QA Context:**
- Receives goal: "Analyze last night's regression failures"
- Reasons: "I need to fetch the logs first, then classify each failure"
- Decides: "Use the log fetching tool, then the classification tool"
- Evaluates: "3 genuine bugs found — I need to create Jira tickets now"

---

# Core Component 2 — Memory System

**What It Is:**
- The system that stores and retrieves information across the agent's workflow
- Without memory, every agent interaction starts from zero
- Memory is what makes Agentic AI learn and improve over time

**The Four Types of Memory:**

| Memory Type | What It Stores | Duration | Example |
|---|---|---|---|
| Sensory | Raw inputs being processed right now | Seconds | Current log file being analyzed |
| Short-Term | Current task context and conversation | Session | Steps taken so far in this run |
| Long-Term | Historical data, patterns, past outcomes | Persistent | Known flaky tests, past bug patterns |
| Semantic | Knowledge about the domain and system | Persistent | What each API endpoint does |

**How Memory Works in Practice:**
- Short-term memory: Agent remembers it already checked the payment service logs
- Long-term memory: Agent knows Test\_Login has been flaky for 3 days on staging
- Semantic memory: Agent understands that a 500 error means server-side failure

**Memory Storage Options:**

| Storage Type | Technology | Best For |
|---|---|---|
| In-memory | Python dict, LangChain buffer | Short-term, current session |
| Vector database | Pinecone, ChromaDB, Weaviate | Long-term semantic search |
| Relational database | PostgreSQL, MySQL | Structured historical data |
| Document store | MongoDB, Redis | Flexible context storage |

> "Memory is what separates a one-time automation script from a system that genuinely gets better the more it runs."

---

# Core Component 3 — Tool Integration

**What It Is:**
- The layer that connects the Reasoning Engine to the outside world
- Without tools, an agent can only think — it cannot act on real systems
- Tools are functions the agent can call to interact with external services

**Categories of Tools:**

| Category | Examples | QA Use Case |
|---|---|---|
| Test Execution | Selenium, Playwright, Pytest | Run test suites autonomously |
| API Interaction | REST clients, GraphQL | Test and validate API endpoints |
| Ticketing Systems | Jira, Azure DevOps | Create and update bug tickets |
| Communication | Slack, Email, Teams | Send alerts and summaries |
| CI/CD Pipelines | Jenkins, GitHub Actions | Trigger builds and deployments |
| Databases | PostgreSQL, MongoDB | Query test data and results |
| File Systems | Read/write logs, reports | Analyze test output files |
| LLM APIs | OpenAI, Anthropic, Gemini | Call AI models for reasoning |

**How the Agent Uses Tools:**
- Reasoning Engine decides: "I need to fetch the test logs"
- It calls the log fetching tool with the correct parameters
- Tool returns the log content
- Reasoning Engine processes the result and decides the next tool to call

**Tool Design Principles:**
- Each tool should do one thing well — keep tools focused
- Tools must return clear, structured responses the agent can parse
- Always validate tool inputs before execution
- Log every tool call for debugging and audit purposes

---

# Core Component 4 — Action Executor

**What It Is:**
- The component that carries out the decisions made by the Reasoning Engine
- Translates reasoning outputs into real-world actions
- Manages the execution of tool calls in the correct sequence
- Handles errors, retries, and fallbacks when actions fail

**What It Does:**
- Receives the action plan from the Reasoning Engine
- Calls the appropriate tools in the correct order
- Passes outputs from one tool as inputs to the next
- Monitors execution and reports results back to the Reasoning Engine
- Retries failed actions with adjusted parameters

**Execution Patterns:**

| Pattern | What It Means | Example |
|---|---|---|
| Sequential | Actions run one after another | Fetch logs → Analyze → Create ticket |
| Parallel | Multiple actions run simultaneously | Test multiple API endpoints at once |
| Conditional | Next action depends on previous result | If bug found → create ticket, else → log pass |
| Loop | Repeat action until condition is met | Rerun flaky test until stable or limit reached |

**Error Handling:**
- If a tool call fails — retry with adjusted parameters
- If retry fails — log the error and inform the Reasoning Engine
- Reasoning Engine decides: skip, try alternative tool, or escalate to human
- All failures are logged with full context for debugging

---

# How Components Talk to Each Other

**The End-to-End Flow:**

| Step | Component | What Happens |
|---|---|---|
| 1 | Human | Provides high-level goal to the agent |
| 2 | Reasoning Engine | Receives goal, queries Memory for context |
| 3 | Memory System | Returns relevant past context and knowledge |
| 4 | Reasoning Engine | Plans first action, selects appropriate tool |
| 5 | Action Executor | Calls the selected tool with parameters |
| 6 | Tool Integration | Executes action, returns result |
| 7 | Action Executor | Passes result back to Reasoning Engine |
| 8 | Reasoning Engine | Evaluates result, updates Memory, plans next step |
| 9 | Memory System | Stores new context from this step |
| 10 | Repeat | Steps 4-9 repeat until goal is achieved |
| 11 | Reasoning Engine | Determines goal is complete, generates final output |
| 12 | Human | Receives result, summary, or report |

**A Real QA Example — Step by Step:**
- Goal received: "Analyze last night's regression and create tickets for real bugs"
- Memory queried: Known flaky tests retrieved from long-term memory
- Tool called: Log fetcher retrieves last night's failure report
- Reasoning: 5 failures found — cross-reference with known flaky list
- Result: 2 are known flaky, 3 are new genuine failures
- Tool called: Jira API creates 3 tickets with full context
- Tool called: Slack sends summary to QA channel
- Memory updated: New failures logged for future pattern recognition
- Goal complete: Final summary returned to human

---

# The Observe-Reason-Act Loop in Detail

**Why This Loop Matters:**
- This is the fundamental operating cycle of every Agentic AI system
- Understanding it helps you predict agent behavior and debug issues
- Every agent framework — LangChain, LangGraph, CrewAI — implements this loop

**The Loop — Expanded:**

| Phase | What Happens | Internal Question |
|---|---|---|
| Observe | Agent gathers current state — inputs, tool results, memory | "What do I know right now?" |
| Reason | Agent thinks through options using LLM reasoning | "What should I do next and why?" |
| Plan | Agent selects the next action and tool | "Which tool do I call and with what?" |
| Act | Action Executor calls the tool | "Execute the chosen action" |
| Evaluate | Agent reviews the result against the goal | "Did this move me closer to the goal?" |
| Update | Memory is updated with new information | "What do I need to remember?" |
| Repeat | Loop continues until goal is achieved or limit reached | "Is the goal complete?" |

**Loop Termination Conditions:**
- Goal achieved — agent determines objective is complete
- Max iterations reached — safety limit to prevent infinite loops
- Human intervention — Human-in-the-Loop approval required
- Unrecoverable error — agent cannot proceed and escalates

**Why Loops Can Go Wrong:**
- Poorly defined goal — agent loops without knowing when to stop
- Missing termination condition — always set a max iteration limit
- Tool returning ambiguous results — agent cannot evaluate progress
- Memory not updating — agent repeats the same action endlessly

---

# Architecture in a Real QA Scenario

**Scenario: Autonomous Nightly Regression Agent**

**Goal Given:** "Run nightly regression, triage failures, and report to the team"

**Architecture in Action:**

| Phase | Component Used | Action Taken |
|---|---|---|
| Start | Reasoning Engine | Receives goal, retrieves known flaky tests from Memory |
| Execute | Action Executor + Tool | Triggers Playwright test suite via CI/CD tool |
| Observe | Reasoning Engine | Receives test results — 8 failures detected |
| Reason | Reasoning Engine | Cross-references failures with known flaky list in Memory |
| Classify | Reasoning Engine | 3 flaky confirmed, 5 potential genuine bugs |
| Verify | Action Executor + Tool | Reruns 3 flaky tests — 2 pass, 1 still fails |
| Update | Memory System | Updates flaky test registry with new data |
| Act | Action Executor + Tool | Creates Jira tickets for 6 genuine bugs with full context |
| Communicate | Action Executor + Tool | Sends Slack summary to QA channel |
| Learn | Memory System | Stores failure patterns for future regression runs |
| Complete | Reasoning Engine | Goal achieved — final report generated |

**What a Human QA Engineer Did:**
- Set the goal once
- Reviewed the Slack summary in the morning
- Approved or adjusted Jira tickets if needed

> "This is not science fiction. Every step in this scenario can be built today using LangGraph, Playwright, Jira API, and Slack API. You will build a version of this in this course."

---

# Key Takeaways — Architecture of Agentic AI

**The Four Components — One Line Each:**

| Component | What It Does |
|---|---|
| Reasoning Engine | Thinks, plans, and decides — powered by an LLM |
| Memory System | Stores context so the agent learns and improves |
| Tool Integration | Connects the agent to real-world systems and APIs |
| Action Executor | Carries out decisions and manages tool execution |

**The Three Things to Remember:**
- No single component works alone — all four must work together
- The Observe-Reason-Act loop is the heartbeat of every agent
- Memory is what separates a one-time script from a learning system

**Architecture Checklist — Before You Build Any Agent:**

| Check | Question |
|---|---|
| ✅ Reasoning Engine | Which LLM will power the reasoning? |
| ✅ Memory | What context does this agent need to remember? |
| ✅ Tools | What external systems does this agent need to access? |
| ✅ Executor | What is the execution order and error handling strategy? |
| ✅ Loop | What is the termination condition for this agent? |
| ✅ Oversight | What level of human-in-the-loop is required? |

> "Architecture is not just a technical diagram. It is the blueprint for how your agent thinks, remembers, acts, and improves. Get the architecture right — and everything else follows."