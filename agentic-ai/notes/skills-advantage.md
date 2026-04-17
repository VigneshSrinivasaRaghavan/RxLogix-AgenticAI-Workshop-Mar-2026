# Coding Way vs Skill Way — Why We Are Here


## 1. The Journey So Far — What You Built

Over the training so far, you built Agentic AI systems **from scratch, in Python**:

| Phase | Topics Covered | What You Built |
|-------|---------------|----------------|
| Foundations | AI vs Gen AI vs Agentic AI, Architecture of Agentic AI | Mental model of how agents work |
| Environment | Project repo, folder structure, env setup, core infra | Working Python project with LLM connectivity |
| Agent Building | Raw agent loop, LLM calls, system prompts | TestCase Generator Agent, Log Analyzer Agent (v1) |
| LangChain | LangChain installation, LLM helper, chains | Same 2 agents rebuilt with LangChain abstractions |
| LangGraph | LangGraph concepts, state machines, nodes, edges | Same 2 agents as stateful LangGraph graphs |
| RAG | RAG intro, vector store, retrieval integration | Agents that retrieve relevant context before answering |
| Memory | Memory types, implementation, conversation history | Agents that remember across interactions |

Two agents evolved through every phase: **TestCase Generator** and **Log Analyzer**.

Every step was deliberate. You wrote every node. You defined every edge. You controlled every LLM call.

That was intentional. You needed to understand the **mechanics** before you could work at a higher level.

Now we go up one level.

---

## 2. The Agentic AI Maturity Curve

There is a spectrum of how much autonomy you give an AI agent:

```
Low autonomy ──────────────────────────────────────────────────── High autonomy
      │                                                                  │
      ▼                                                                  ▼
 Raw API call → LangChain → LangGraph → RAG + Memory → Agent Delegation
 (you code        (chains)    (graph)    (knowledge +    (you describe goal,
  everything)                            persistence)     agent figures out
                                                          the steps)
```

- **Training so far:** You were on the left side. You coded the behavior step by step.
- **This topic:** We move to the right side. You describe the goal. The agent reasons about how to achieve it.

This is not a shortcut. This is the natural progression.

---

## 3. Coding Way vs Skill Way — The Real Difference

### Coding Way (Python + LangGraph)

You are the **architect**. You define:
- Every node (what happens at each step)
- Every edge (how steps connect)
- Every state (what gets passed between steps)
- Every prompt (what the LLM is told)

The LLM is a **component you call**. You orchestrate it.

```python
# Coding way — you define the graph explicitly
workflow = StateGraph(SelfHealState)
workflow.add_node("detect_failure", detect_failure)
workflow.add_node("analyze_locators", analyze_locators)
workflow.add_node("heal_locator", heal_locator)
workflow.add_node("validate_fix", validate_fix)
workflow.add_conditional_edges("validate_fix", should_retry)
```

### Skill / Agent Delegation Way

You are the **delegator**. You define:
- The goal ("fix the broken Playwright test")
- The constraints ("do not apply a fix unless the selector exists in the current DOM")
- The phases ("first detect, then analyze, then fix, then verify")

The agent reasons about **how** to execute. It picks its own tools. It loops until done.

```markdown
# In SKILL.md (what you write)
## Phase 1: Detect Failure
Run `npx playwright test` and parse the output.
Extract: test name, failed selector, error message.

## Phase 2: Analyze Locators
Read the current DOM of the failing page.
Compare the old selector against what exists in the DOM now.

## Phase 3: Heal
Propose a new selector that matches the same element semantically.
Before applying: validate the selector is unique and present in the DOM.

## Phase 4: Patch and Verify
Edit the .spec.ts file with the new selector.
Re-run the test. Repeat if still failing. Stop after 3 attempts.
```

The key difference:

| | Coding Way | Skill Way |
|--|-----------|-----------|
| Who defines the steps? | You (in code) | You (in natural language) |
| Who executes the steps? | Your Python graph | The AI agent |
| How does it adapt? | Only as you coded it | Reasons in real-time |
| Who calls external tools? | You wire up tool nodes | Agent uses built-in tools |
| Output | Deployable Python code | Autonomous agent execution |

---

## 4. Could These Topics Have Been Done the Coding Way?

**Yes. 100%.** Let's be honest about this.

Every sub-topic in this class CAN be implemented as a LangGraph graph:

- **Failure Detection** → A node that runs `subprocess.run(["npx", "playwright", "test"])` and parses stdout
- **Old vs New Locator Comparison** → A node that calls the LLM with old selector + current DOM snapshot
- **Self-Healing** → A node that generates a new selector and writes to the `.spec.ts` file
- **Guardrails** → A Pydantic validation node that checks the proposed fix before applying it
- **Loop** → A conditional edge that retries until the test passes or max attempts hit

You could absolutely build this in Python. It would work.

---

## 5. So What Is Actually Missing to Do It the Coding Way?

If you wanted to build this properly in LangGraph, you would need to learn **4 additional topics** that were not covered in the training so far:

### 1. Tool Calling / Function Calling
How to give a LangGraph agent the ability to call external CLI tools as "tools" — not just LLM chains, but actual system commands like running `npx playwright test` and reading back the output.

### 2. External System Integration
How to connect an agent to non-Python systems — browsers, test runners, file watchers. This includes how to read live DOM snapshots from a running browser page, not just static HTML.

### 3. Structured Output with Pydantic (for Guardrails)
How to force the LLM to return structured, validated output (e.g., `{ "new_selector": "...", "confidence": 0.9, "reason": "..." }`) and reject responses that fail validation — without letting hallucinated selectors silently corrupt your test files.

### 4. Loop Patterns with Exit Conditions
How to design LangGraph graphs that loop (retry), track iteration count in state, and gracefully exit when max retries are hit or when a success condition is met.

> **Note:** "Multi-agent" is NOT what's missing here. Multi-agent would mean separate agents talking to each other — a supervisor agent, a healer agent, a validator agent. That's a valid architecture, but it's overkill for this problem. A single well-designed looping graph handles this. The real gap is tool calling + external integration.

Each of those 4 topics is a 2–3 hour session on its own. That's 8–12 more hours of training.

---

## 6. Why the Skill Approach Is the Right Choice for This Topic

The IDE's AI agent already HAS everything you would spend 8–12 hours teaching:

| What You'd Need to Build | What the IDE Agent Already Has |
|--------------------------|-------------------------------|
| Tool calling setup | Built-in shell execution tool |
| File read/write integration | Built-in file read/write tools |
| External system integration | Built-in browser + DOM tools |
| Structured output validation | Reasoning baked into the model |
| Loop with exit conditions | Agent's own iteration behavior |

By writing a SKILL.md, you are **configuring an agent that already has the plumbing**. You skip building the infrastructure and jump straight to the concepts.

And this is not just a shortcut — it is **genuinely how senior engineers use AI agents** in the real world:
- You don't always write a new LangGraph graph for every problem
- Sometimes you configure an existing capable agent with domain-specific instructions
- The skill of writing a precise, structured system prompt for an agent IS a valuable engineering skill

---

## 7. The Student Experience Is Different — and That Matters

When you built the LangGraph graphs, you were **inside** the agent. You defined it. You understood every state.

With the skill approach, you are **watching** the agent reason and execute.

That shift is important. It shows you what it feels like to use an agentic system as a tool:
- You see the agent read the failure
- You watch it analyze the DOM
- You see it propose a fix, then validate it before applying
- You watch it re-run the test and adjust if it still fails

This is closer to how most QA engineers and developers will actually interact with AI agents in the next 2–3 years — **configuring and directing them**, not writing every node by hand.

---

## 8. When to Use Which Approach — Real World Decision

Use the **coding way (LangGraph)** when:
- You need production-grade reliability and auditability
- The behavior must be reproducible and version-controlled
- Other engineers will maintain the system
- The logic is deterministic (parse this format, extract these fields, route here)
- You need to deploy it as a microservice or pipeline

Use the **skill/delegation way** when:
- The problem is unpredictable (failures vary, DOM changes are different every time)
- The solution requires real-time contextual reasoning
- You need the agent to adapt mid-task without pre-coded branches
- Speed of delivery matters more than code ownership
- You're demonstrating or prototyping agentic behavior

**For the self-healing use case specifically:**
The Playwright DOM is dynamic. Failure messages vary. The "fix" requires understanding what the element WAS trying to target and finding its new location semantically. You literally cannot pre-code every failure scenario. This problem is in the "agent delegation" bucket by nature.

---

## 9. Key Takeaway — The Bridge Message

Everything covered so far taught you how to **build** agents by coding the behavior.

This topic teaches you how to **use** agents by describing the behavior.

Both are real skills. Both are used in industry. A complete Agentic AI engineer knows when to reach for each one.

The progression is:

```
You code every step               →    You describe the goal
(you understand the mechanics)         (you trust the agent)
      ↓                                       ↓
  Control + Auditability             Speed + Adaptability
  Production systems                 Intelligent automation
  Maintenance-friendly               Context-sensitive reasoning
```

The skill file you will write next is not a shortcut. It is the top of the ladder you have been climbing.

---