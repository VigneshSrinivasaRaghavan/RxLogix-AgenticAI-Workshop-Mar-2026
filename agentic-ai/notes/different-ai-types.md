# Agentic AI Training — RxLogix
## Section 2 — AI vs Gen AI vs Agentic AI vs AI Agents

---

# Agenda — AI vs Gen AI vs Agentic AI vs AI Agents

- The Spectrum: Narrow AI to Agentic AI
- Understanding AI — Artificial Intelligence
- Understanding Gen AI — Generative AI
- Understanding AI Agents
- Understanding Agentic AI
- AI Agents vs Agentic AI — The Most Confused Pair
- Side-by-Side Comparison — All Four
- Simple Real-World Comparison
- Key Takeaways

---

# The Spectrum: Narrow AI → Gen AI → Agentic AI

**Why Start Here:**
- These four terms are used interchangeably in the industry — they are not the same
- Each represents a different level of capability, autonomy, and intelligence
- Understanding the spectrum gives you the mental model for everything that follows

**The Progression:**

| Stage | What It Can Do | Example |
|---|---|---|
| Narrow AI | One specific task, rule-based | Spam filter, image classifier |
| Generative AI | Create new content from learned patterns | GPT-4o, Claude, Gemini |
| AI Agent | Execute defined tasks using tools and rules | Scheduled test runner, RPA bot |
| Agentic AI | Set goals, plan, act, and learn autonomously | LangGraph agent, CrewAI crew |

**The Key Insight:**

| Type | Core Behavior |
|---|---|
| Narrow AI | Reacts to inputs |
| Generative AI | Responds to prompts |
| AI Agent | Executes defined tasks |
| Agentic AI | Pursues goals autonomously |

> "Every Agentic AI system is built on top of Generative AI — which is itself a leap beyond Narrow AI. You cannot fully understand agents without understanding what came before them."

---

# Understanding AI — Artificial Intelligence

**Definition:**
- Broad field of creating machines that perform tasks requiring human intelligence
- Encompasses everything from simple rule-based systems to complex reasoning models
- Has existed as a field since the 1950s — long before LLMs and agents

**What Traditional AI Can Do:**
- Recognize images and classify objects
- Translate text between languages
- Recommend products based on purchase history
- Detect fraud based on transaction patterns
- Filter spam emails based on learned rules

**Key Characteristics:**

| Characteristic | Detail |
|---|---|
| Task Scope | Narrow — designed for one specific task |
| Learning | Trained on labeled data for that task only |
| Flexibility | Cannot adapt to tasks outside its training |
| Interaction | Reactive — responds to inputs, does not initiate |
| Output | Classification, prediction, or decision |

**In QA Context:**
- Defect prediction models — predicts which modules are likely to have bugs
- Test prioritization — ranks test cases by risk score
- Visual regression tools — detects pixel-level UI differences
- These are powerful but limited to the task they were built for

---

# Understanding Gen AI — Generative AI

**Definition:**
- AI that generates new content — text, code, images, audio — from learned patterns
- Powered by Large Language Models trained on massive datasets
- Does not just classify or predict — it creates
- Foundation technology that makes Agentic AI possible

**What Gen AI Can Do:**
- Generate human-like text, code, and documentation
- Summarize long documents, logs, and reports
- Answer questions based on context provided
- Write and debug code in multiple languages
- Translate between languages and formats
- Reason through multi-step problems when prompted

**Key Characteristics:**

| Characteristic | Detail |
|---|---|
| Task Scope | Broad — can handle many different types of tasks |
| Learning | Pre-trained on trillions of words and code |
| Flexibility | Adapts to different tasks via prompting |
| Interaction | Responds to prompts — waits for next input |
| Output | Generated text, code, images, or structured data |

**Important Limitation:**
- Gen AI responds and waits — it does not act on its own
- Every output requires a human to read, decide, and take action
- It is a powerful assistant — not an autonomous worker

> "Gen AI is the brain. It can think, reason, and generate. But without an agent framework around it, it just sits and waits for the next prompt."

---

# Understanding AI Agents

**Definition:**
- Software that perceives its environment and takes actions to achieve specific goals
- Operates based on predefined rules, scripts, or configurations
- Uses tools and APIs to interact with external systems
- Requires human setup and configuration to define what it does

**What AI Agents Can Do:**
- Run a test suite every night at 2 AM automatically
- Monitor an API endpoint and alert when it goes down
- Scrape data from a website on a schedule
- Execute a fixed workflow when triggered by an event
- Send notifications based on predefined conditions

**Key Characteristics:**

| Characteristic | Detail |
|---|---|
| Task Scope | Narrow — defined by its configuration |
| Decision Making | Rule-based — follows predefined logic |
| Autonomy | Limited — cannot deviate from its script |
| Goal Setting | Human defines the goal and the steps |
| Adaptability | Cannot handle situations outside its rules |

**In QA Context:**
- Selenium Grid running tests on a schedule — AI Agent
- Jenkins pipeline triggering test suite on code push — AI Agent
- Slack bot sending test result notifications — AI Agent
- These are valuable but rigid — they do exactly what they are told, nothing more

---

# Understanding Agentic AI

**Definition:**
- AI system that autonomously sets sub-goals and pursues a high-level objective
- Combines the reasoning power of Gen AI with the action capability of AI Agents
- Plans its own steps, uses tools, learns from outcomes, and adapts
- Does not need step-by-step instructions — just a goal

**What Agentic AI Can Do:**
- Receive one high-level goal and break it into steps autonomously
- Decide which tools to use and in what order
- Handle unexpected situations by reasoning through them
- Learn from past outcomes and improve future performance
- Coordinate multiple agents working together toward a shared goal

**Key Characteristics:**

| Characteristic | Detail |
|---|---|
| Task Scope | Broad — handles complex, multi-step objectives |
| Decision Making | Reasoning-based — thinks before acting |
| Autonomy | High — initiates and adapts without human prompts |
| Goal Setting | Human sets the high-level goal only |
| Adaptability | Adjusts approach based on feedback and results |

**The Workflow Loop:**

| Step | What Happens |
|---|---|
| Observe | Analyze current state and available information |
| Reason | Think through options and plan next steps |
| Decide | Choose the best course of action |
| Act | Execute using available tools |
| Learn | Update knowledge based on outcomes |

---

# AI Agents vs Agentic AI — The Most Confused Pair

**Why Students Confuse Them:**
- Both use the word "agent"
- Both interact with tools and external systems
- Both can operate without a human present
- The difference is in reasoning, adaptability, and goal ownership

**The Core Difference:**

| | AI Agent | Agentic AI |
|---|---|---|
| Who defines the steps? | Human | AI itself |
| Can it handle the unexpected? | No — fails or stops | Yes — reasons through it |
| Does it learn from outcomes? | No | Yes |
| Can it set its own sub-goals? | No | Yes |
| What happens when rules run out? | Stops or errors | Adapts and continues |
| Powered by LLM reasoning? | Not necessarily | Always |

**Simple Analogy:**

| | AI Agent | Agentic AI |
|---|---|---|
| **Like a...** | Junior employee with a checklist | Senior professional with a goal |
| **You give them...** | Step-by-step instructions | The outcome you want |
| **They handle surprises by...** | Stopping and asking you | Figuring it out themselves |
| **They improve over time?** | No | Yes |

**Real QA Example:**

| Scenario | AI Agent | Agentic AI |
|---|---|---|
| Nightly regression | Runs tests at 2 AM, sends report | Runs tests, classifies failures, reruns flaky tests, creates Jira tickets, sends summary |
| A test fails unexpectedly | Marks as failed, stops | Analyzes why, checks logs, determines if environment or code issue, acts accordingly |
| New requirement added | Cannot adapt — needs reconfiguration | Reads requirement, generates new test cases, adds to suite |

> "An AI Agent does what you told it to do. Agentic AI does what needs to be done to achieve your goal — even if you did not anticipate every step."

---

# Side-by-Side Comparison — All Four

| | Narrow AI | Gen AI | AI Agent | Agentic AI |
|---|---|---|---|---|
| **Core Function** | Classify or predict | Generate content | Execute defined tasks | Pursue goals autonomously |
| **Powered By** | ML models | LLMs | Rules or scripts | LLMs + reasoning loop |
| **Flexibility** | Very low | High | Low | Very high |
| **Autonomy** | None | None | Partial | Full |
| **Learns Over Time** | Only via retraining | No | No | Yes |
| **Handles Unexpected** | No | With prompting | No | Yes |
| **Human Input Needed** | Input data | Every prompt | Initial setup | Goal only |
| **QA Example** | Defect predictor | Test case generator | Scheduled test runner | Autonomous QA agent |

---

# Simple Real-World Comparison

**The Same Problem — Four Different Responses:**
> Problem: "5 tests failed in last night's regression run"

**Narrow AI:**
- Flags the failures based on pass/fail classification
- Labels them as high/medium/low risk based on historical data
- Stops — a human must investigate and decide next steps

**Gen AI (ChatGPT / Claude):**
- You paste the logs and ask: "Why did these tests fail?"
- It analyzes and responds: "Likely a timeout issue in the payment service"
- Stops and waits for your next prompt — takes no action

**AI Agent:**
- Configured to: Send a Slack alert when more than 3 tests fail
- It detects 5 failures and sends the alert automatically
- Stops — it has completed its defined task

**Agentic AI:**
- Receives goal: "Ensure nightly regression is stable"
- Detects 5 failures autonomously
- Analyzes logs and classifies: 2 flaky, 3 genuine bugs
- Reruns flaky tests to confirm classification
- Creates Jira tickets for real bugs with full context
- Sends team summary with root cause and recommendations
- Logs patterns for future regression improvement
- Continues monitoring — never stops until goal is met

---

# Key Takeaways — AI vs Gen AI vs Agentic AI vs AI Agents

**The Four in One Line Each:**

| Type | One Line Summary |
|---|---|
| Narrow AI | Does one thing well — nothing more |
| Gen AI | Creates content when you ask — then waits |
| AI Agent | Executes what you configured — nothing unexpected |
| Agentic AI | Receives a goal and figures out everything else |

**The Two Most Important Distinctions:**
- Gen AI vs Agentic AI: Gen AI responds, Agentic AI acts
- AI Agent vs Agentic AI: Agents follow rules, Agentic AI reasons and adapts

**What This Means for Your QA Career:**
- Narrow AI tools are already in your workflow — defect prediction, visual testing
- Gen AI is your daily assistant — test case generation, log summarization
- AI Agents are your automation scripts evolved — smarter triggers and actions
- Agentic AI is where QA is heading — autonomous, reasoning, self-improving systems

> "The question is no longer whether Agentic AI will change QA. It already is. The question is whether you will be the one building it — or the one waiting to be told about it."