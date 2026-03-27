# Topic 2: Defect Prevention Mindset
## Section 2.1 — Defect Origin Points, Assumption Testing & User Personas

---

# Agenda — Section 2.1

- What is a Defect Prevention Mindset?
- Where Do Defects Actually Originate?
- Defect Origin Points — In Detail
- What is Assumption Testing?
- How to Surface and Test Assumptions
- User Personas — What & Why
- How to Build and Use Personas in Testing
- Key Takeaways

---

# What is a Defect Prevention Mindset?

**Definition:**
A proactive approach where QAs focus on eliminating the conditions
that cause defects — rather than only finding defects after they are created.

**Reactive QA:**
- Waits for the build
- Tests the feature
- Raises defects
- Cycle repeats

**Proactive QA — Defect Prevention Mindset:**
- Reviews requirements before development begins
- Identifies assumptions and ambiguities early
- Understands real user behaviour
- Eliminates defect-causing conditions upstream

**The shift in thinking:**
From *"How do I find bugs?"*
To *"How do I prevent bugs from being created in the first place?"*

---

# The Cost Argument — Why Prevention Beats Detection

| Activity | Cost to Fix |
|---|---|
| Defect prevented at requirements stage | 1x |
| Defect found during development | 10x |
| Defect found during QA testing | 15x |
| Defect found in production | 100x |

**The earlier a defect is prevented — the cheaper it is for everyone.**

Prevention is not just good practice.
In regulated industries like pharmacovigilance —
it is an expectation built into the quality framework.

---

# Where Do Defects Actually Originate?

**Industry research consistently shows:**

| Defect Origin | % of Total Defects |
|---|---|
| Requirements — ambiguity, gaps, conflicts | ~45% |
| Design — poor decisions, missing edge cases | ~20% |
| Code — implementation errors | ~20% |
| Test environment / configuration | ~10% |
| Other | ~5% |

**The key insight:**
Nearly half of all defects originate in requirements —
before a single line of code is written.

**What this means for QA:**
If you only test the code — you are addressing 20% of the problem.
If you also review requirements — you are addressing 65% of the problem.

---

# Defect Origin Point 1 — Requirements

**How defects originate here:**
- Ambiguous statements interpreted differently by dev and QA
- Missing edge cases and negative scenarios
- Conflicting requirements not caught during review
- Requirements that change without all stakeholders being informed

**Simple Example:**
> Requirement: "Users can upload documents."
> Dev assumed: PDF only
> QA assumed: any file type
> Business expected: PDF, Word, and Excel only
> Result: Wrong file validation built and tested → defect in production

**RxLogix Example:**
> Requirement: "System shall notify relevant users when a case is overdue."
> Who is "relevant"? Case owner only? All PV Officers? Team lead?
> Dev notified all PV Officers → Business expected only the case owner →
> Mass email notifications triggered → user complaints → hotfix required

---

# Defect Origin Point 2 — Design Decisions

**How defects originate here:**
- Edge cases not considered during solution design
- Poor data model decisions that cause downstream errors
- Workflow design that does not match real user behaviour
- Integration design that assumes external systems always respond correctly

**Simple Example:**
> Design decision: Store user age as a whole number integer.
> Edge case missed: User enters age as 0 or 999.
> No validation built → invalid data enters the system →
> Downstream reports show meaningless age data.

**RxLogix Example:**
> Design decision: ICSR case ID generated sequentially.
> Edge case missed: Two PV Officers submit cases simultaneously.
> Race condition → both cases assigned the same ID →
> Data integrity failure → one case overwrites the other →
> A regulatory submission is silently lost.

---

# Defect Origin Point 3 — Assumptions

**How defects originate here:**
- Developers assume the user will always follow the happy path
- BAs assume the business rule is universally understood
- QAs assume the requirement means what they think it means
- Everyone assumes the external system will always be available

**Simple Example:**
> Dev assumption: "Users will always fill forms top to bottom."
> Reality: Users tab through fields randomly, copy-paste content,
> use browser autofill, or leave and return to the form.
> Result: Validation logic breaks under real user behaviour.

**RxLogix Example:**
> Dev assumption: "PV Officers will always submit one case at a time."
> Reality: During a product safety review, a team submits
> 200 cases simultaneously over a 2-hour window.
> Result: System performance degrades → submission timeouts →
> Cases fail silently → regulatory deadline missed.

---

# Defect Origin Point 4 — Communication Gaps

**How defects originate here:**
- Verbal decisions made in meetings never documented
- Requirement updates sent by email — not reflected in the BRD
- Developer misunderstands a requirement but never raises the question
- QA tests based on an older version of the FRS

**Simple Example:**
> BA verbally told the developer in a meeting:
> "The password minimum length changed from 6 to 8 characters."
> BRD was never updated.
> QA tested against the BRD — validated 6 characters as correct.
> Live system enforced 8 characters → users unable to set passwords
> using the documented rule → support tickets raised.

**RxLogix Example:**
> Regulatory team verbally confirmed with the BA:
> "The E2B(R2) export format is being deprecated — switch to E2B(R3)."
> FRS was not updated.
> Dev built E2B(R2). QA tested E2B(R2). Both passed.
> EMA gateway rejected all submissions — only R3 accepted from that quarter.

---

# Defect Origin Point 5 — Environment & Configuration

**How defects originate here:**
- Feature works in test environment but fails in production
- Configuration differences between environments not documented
- Third-party services mocked in test but behave differently in production
- Data volume in production far exceeds what was tested

**Simple Example:**
> Feature tested successfully in a local environment
> with a database of 100 records.
> Production database has 2 million records.
> The same search query times out → feature unusable in production.

**RxLogix Example:**
> E2B XML export tested against a mock EMA gateway in test environment.
> Mock always returned a success response.
> Production EMA gateway has strict schema validation
> that the mock did not replicate.
> First live submission rejected → issue discovered post go-live.

---

# What is Assumption Testing?

**Definition:**
The process of explicitly identifying every assumption made
during requirements, design, or development —
and then testing whether those assumptions hold true in reality.

**Why it matters:**
Every untested assumption is a potential defect waiting to be triggered.

**Three layers of assumptions in every project:**

| Layer | Who Makes It | Example |
|---|---|---|
| Business | BA / Product Owner | "Users will always have a stable internet connection" |
| Technical | Developer | "The external API will respond within 2 seconds" |
| Behavioural | Everyone | "Users will read the instructions before submitting" |

---

# How to Surface Assumptions

**Step 1 — The Assumption Hunting Question Set**
For every feature or requirement — ask:

- What does this assume about the user's behaviour?
- What does this assume about the data being entered?
- What does this assume about external systems?
- What does this assume about the user's environment (device, browser, connectivity)?
- What does this assume about volume or load?
- What happens if any of these assumptions are false?

**Step 2 — Run an Assumption Log**
Document every assumption found:

| Assumption | Made By | Risk if False | Test Approach |
|---|---|---|---|
| Users submit one case at a time | Dev | Performance failure | Load test with concurrent submissions |
| EMA gateway always responds | Dev | Silent submission failure | Test with gateway unavailable / delayed |
| Users read error messages | BA | Task abandonment | UX test with real users or walkthroughs |

---

# How to Test Assumptions

**Assumption: "Users will follow the intended workflow sequence"**
- Test: Skip steps, go back mid-flow, refresh mid-submission
- Test: Use browser back button during a multi-step form
- Test: Open the same form in two browser tabs simultaneously

**Assumption: "Input data will always be in the correct format"**
- Test: Paste data from Excel with hidden characters
- Test: Enter data in a different language or character set
- Test: Copy-paste a date in a different format than expected

**Assumption: "The external system will always be available"**
- Test: Simulate the external system being down
- Test: Simulate a slow response (5 seconds, 30 seconds, timeout)
- Test: Simulate the external system returning an unexpected response

**RxLogix Example:**
> Assumption: "E2B XML will always be well-formed before export."
- Test: Trigger export with a case missing mandatory fields
- Test: Trigger export when a field contains special characters (< > & ")
- Test: Trigger export during a concurrent bulk submission of 50 cases

---

# User Personas — What & Why

**What is a User Persona?**
A detailed representation of a specific type of real user —
their role, goals, technical ability, behaviours, and pain points.

**Why personas matter in testing:**
- Different users interact with the same feature in completely different ways
- A test case written from one user's perspective misses all others
- Real defects hide in the gap between how QA imagines the user
  and how the user actually behaves

**Without personas:**
QA tests as themselves — a technically proficient person
who knows exactly what the system is supposed to do.

**With personas:**
QA tests as a range of real users — some inexperienced,
some rushed, some using the system in an unexpected way.

---

# How to Build a User Persona

**A persona has 5 components:**

**1. Role & Responsibility**
Who are they? What is their job? What are they trying to achieve?

**2. Technical Proficiency**
Are they a power user? A first-time user? Do they use keyboard shortcuts?
Or do they click everything slowly and carefully?

**3. Goals**
What does success look like for this user in this feature?

**4. Frustrations & Pain Points**
What slows them down? What confuses them? What do they avoid?

**5. Realistic Behaviours**
How do they actually use the system — not how they are supposed to?

---

# Persona Example — Simple (E-Commerce)

**Persona: Rahul — First-Time Online Shopper**

| Component | Detail |
|---|---|
| Role | Retail customer, buying online for the first time |
| Technical Proficiency | Low — uses mobile only, not comfortable with forms |
| Goal | Buy a birthday gift and get it delivered in 2 days |
| Frustrations | Confused by too many steps, worried about payment security |
| Real Behaviours | Goes back and forth between pages, misreads delivery date, calls support if unsure |

**Test cases this persona generates:**
- What happens when the user taps the back button mid-checkout?
- Is the delivery date displayed clearly enough for a non-technical user?
- What does the payment security indicator look like on a small mobile screen?
- Is the error message on failed payment clear enough for a first-time user?

---

# Persona Example — RxLogix

**Persona 1: Ananya — Junior PV Officer (6 months experience)**

| Component | Detail |
|---|---|
| Role | Enters and submits ICSRs for adverse event cases |
| Technical Proficiency | Medium — familiar with the system but still learning edge cases |
| Goal | Submit cases accurately and on time to meet regulatory deadlines |
| Frustrations | Confused when error messages are unclear, unsure which fields are truly mandatory |
| Real Behaviours | Saves drafts frequently, sometimes submits incomplete cases out of deadline pressure |

**Test cases this persona generates:**
- Are mandatory fields clearly marked before submission attempt?
- Does saving a draft preserve all entered data accurately?
- What happens when a case is submitted with optional fields empty?
- Is the deadline countdown visible and understandable on the case screen?

---

# Persona Example — RxLogix

**Persona 2: Dr. Mehta — Senior Medical Reviewer (10 years experience)**

| Component | Detail |
|---|---|
| Role | Reviews and approves ICSR cases before regulatory submission |
| Technical Proficiency | High — power user, uses keyboard shortcuts, reviews 30+ cases daily |
| Goal | Review cases quickly without sacrificing accuracy |
| Frustrations | Slow page loads, unnecessary confirmation dialogs, repetitive clicks |
| Real Behaviours | Opens multiple cases in separate tabs, uses keyboard to navigate, rarely reads tooltips |

**Test cases this persona generates:**
- Does the system support multiple cases open in separate tabs without session conflict?
- Do keyboard shortcuts work correctly across all review screens?
- Does the system perform acceptably when 30+ cases are loaded in a session?
- Are confirmation dialogs skippable or configurable for power users?

---

# Personas → Test Scenarios Mapping

| Persona | Feature | Test Scenario Generated |
|---|---|---|
| Junior PV Officer | ICSR Submission | Submit with deadline pressure — skips optional fields |
| Senior Medical Reviewer | Case Review | Opens 5 cases in tabs — reviews in non-linear order |
| Regulatory Affairs Manager | E2B Export | Triggers bulk export of 100 cases before quarter-end deadline |
| IT Administrator | User Management | Creates 50 new user accounts in a single session |
| First-Time User (any system) | Login / Onboarding | Misreads field labels, uses wrong date format, clicks submit twice |

**The rule:**
One feature + multiple personas = a complete test scenario set.
One feature + one persona = a partial test scenario set with gaps.

---

# Connecting It All — Origin Points + Assumptions + Personas

**The three concepts work together:**

**Defect Origin Points** tell you WHERE defects are most likely to come from
→ Focus your prevention efforts on requirements, design decisions, and communication gaps

**Assumption Testing** tells you WHAT hidden risks exist beneath the surface
→ Surface every assumption and verify it holds true under real conditions

**User Personas** tell you WHO will expose defects that structured testing misses
→ Test through the eyes of real users — not just through the eyes of a QA

**Together:**
They give you a complete defect prevention strategy —
covering the source, the hidden risks, and the human factor.

---

# Section 2.1 — Key Takeaways

- Defect prevention is more cost-effective than defect detection at every stage
- ~45% of defects originate in requirements — QA involvement at that stage is critical
- Five defect origin points: Requirements, Design, Assumptions, Communication, Environment
- Every untested assumption is a potential production defect
- Surface assumptions using structured question sets — then test each one deliberately
- User personas reveal test scenarios that purely technical testing will never generate
- One feature tested through multiple personas = significantly more complete coverage
- The defect prevention mindset shifts QA from a reactive role to a strategic one