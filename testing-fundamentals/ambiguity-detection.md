# Section 1.2 — Ambiguity Detection & Stakeholder Validation

---

# Agenda — Section 1.2

- What is Ambiguity in Requirements?
- Types of Ambiguity with Examples
- How to Detect Ambiguity — 5 Techniques
- What to Do After Detecting Ambiguity
- Stakeholder Validation — What, Why, How
- Key Takeaways

---

# What is Ambiguity in Requirements?

**Definition:**
A requirement is ambiguous when it can be interpreted in more than one way
by different readers — leading to different implementations and different test cases.

**Why it matters:**
- Developer builds Feature A
- QA tests for Feature B
- Client expected Feature C
- → All three based on the same one-line requirement

**The Golden Rule:**
If a requirement leaves a question unanswered — it is ambiguous.
It is the QA's job to find it before development begins, not after.

---

# The Real Cost of Undetected Ambiguity

| Stage Defect Found | Relative Cost to Fix |
|---|---|
| Requirements phase | 1x |
| Design phase | 5x |
| Development phase | 10x |
| Testing phase | 15x |
| Production | 100x |

A single ambiguous requirement left unresolved can cost 100x more
to fix after go-live than catching it during requirement review.

---

# Types of Ambiguity — Overview

1. **Vague Language** — Words with no measurable definition
2. **Missing Conditions** — "What happens when...?" is never answered
3. **Conflicting Requirements** — Two statements contradict each other
4. **Assumed Knowledge** — The requirement assumes everyone knows something
5. **Incomplete Negative Scenarios** — Only happy path is described

---

# Type 1 — Vague Language

**What it looks like:**
Words like: *fast, user-friendly, soon, appropriate, reasonable, easy, secure*

**Simple Example:**
> "The system shall respond quickly to user actions."
- What is "quickly"? 1 second? 3 seconds? 10 seconds?
- QA cannot write a performance test without a number

**Corrected Version:**
> "The system shall respond to all user actions within 2 seconds under normal load."

**RxLogix Example:**
> Ambiguous: "The ICSR submission process shall be fast."
> Corrected: "The ICSR submission shall complete within 5 seconds after the user clicks Submit, under a concurrent load of 50 users."

**Detection Trigger:** Whenever you read a word you cannot measure → flag it.

---

# Type 2 — Missing Conditions

**What it looks like:**
The requirement describes the normal flow but never states
what happens in exception or edge cases.

**Simple Example:**
> "The system shall send an OTP to the registered mobile number."
- What if the mobile number is not registered?
- What if the OTP delivery fails?
- What if the user enters the OTP after it expires?
- None of these are addressed.

**RxLogix Example:**
> "The system shall send a case acknowledgement email to the PV Officer upon submission."
- What if the PV Officer's email is invalid?
- What if the mail server is down at time of submission?
- What if the case submission succeeds but email fails — is the submission still valid?

**Detection Trigger:** For every action described → ask "What if it fails? What if the data is missing?"

---

# Type 3 — Conflicting Requirements

**What it looks like:**
Two requirements in the same document that directly contradict each other.
This is more common than teams expect — especially in large documents.

**Simple Example:**
> Requirement 3.2: "Users shall be automatically logged out after 10 minutes of inactivity."
> Requirement 7.8: "The session shall remain active as long as the browser tab is open."
- Which one is correct? Both cannot be true simultaneously.

**RxLogix Example:**
> Requirement 4.1: "A case in Approved status cannot be edited by any user."
> Requirement 9.3: "A Medical Reviewer can update the case narrative at any stage of the workflow."
- Does "any stage" include Approved? Conflict.

**Detection Trigger:** While reading, maintain a list of all rules and constraints.
Cross-check each new rule against existing ones.

---

# Type 4 — Assumed Knowledge

**What it looks like:**
The requirement uses domain terms, acronyms, or concepts
without defining them — assuming all readers share the same understanding.

**Simple Example:**
> "The system shall process transactions using standard banking protocols."
- Which protocols? SWIFT? NEFT? IMPS? RTGS?
- "Standard" means different things to different people.

**RxLogix Example:**
> "The system shall generate reports compliant with ICH guidelines."
- Which ICH guideline? ICH E2B(R3)? ICH E2B(R2)? ICH E6?
- Each has a completely different format and field set.

**Detection Trigger:** Every acronym, standard name, or domain term
that is not defined in the Glossary section → flag for clarification.

---

# Type 5 — Incomplete Negative Scenarios

**What it looks like:**
The requirement only describes what happens when everything goes right.
What happens when it goes wrong is completely absent.

**Simple Example:**
> "The system shall allow users to upload a profile picture."
- What file formats are allowed? PDF? EXE?
- What is the maximum file size?
- What happens if the upload fails midway?

**RxLogix Example:**
> "The system shall allow users to import ICSR data via CSV file."
- What if the CSV has incorrect column headers?
- What if mandatory fields are blank in the CSV?
- What if the CSV contains 100,000 rows — is there a limit?
- What happens to partially imported records if the import fails at row 500?

**Detection Trigger:** For every "allow" or "shall support" statement →
ask "What are all the ways this can go wrong?"

---

# How to Detect Ambiguity — 5 Techniques

1. **The Measurement Test** — Can I put a number or pass/fail criteria to this?
2. **The "What If" Test** — What if the data is wrong / missing / extreme?
3. **The Multi-Reader Test** — Would two different people implement this the same way?
4. **The Negative Flip Test** — Flip the requirement → does the negative scenario have an answer?
5. **The Cross-Reference Check** — Does this requirement conflict with any other?

---

# Technique 1 — The Measurement Test

**Apply to:** Any requirement with subjective or qualitative language

**Ask yourself:** Can I write a pass/fail test case for this as written?

| Requirement | Measurable? | Action |
|---|---|---|
| "System shall respond quickly" | ❌ No | Flag — ask for response time in seconds |
| "System shall respond within 2 seconds" | ✅ Yes | Write performance test |
| "UI shall be user-friendly" | ❌ No | Flag — ask for specific UX criteria |
| "Error messages shall be displayed in red, font size 14" | ✅ Yes | Write UI validation test |

**Rule:** If you cannot write a clear pass/fail test case → the requirement is ambiguous.

---

# Technique 2 — The "What If" Test

**Apply to:** Every action, input, or process described in the FRS

**Question set to ask for every requirement:**
- What if the input data is missing?
- What if the input data is in the wrong format?
- What if the external system (API, email, gateway) is unavailable?
- What if the user has insufficient permissions?
- What if the volume of data exceeds normal expectations?

**Simple Example:**
> Requirement: "System shall calculate the total order amount."
- What if one product has no price set?
- What if a discount code is applied making total negative?
- What if currency conversion is involved?

**RxLogix Example:**
> Requirement: "System shall submit ICSR to the EMA gateway."
- What if the EMA gateway is down?
- What if the submission times out after 30 seconds?
- Is there a retry mechanism? How many retries?

---

# Technique 3 — The Multi-Reader Test

**Apply to:** Requirements that are written in natural language (not precise technical terms)

**How to apply it:**
Read the requirement. Then ask:
*"If I gave this to a developer and a tester independently — would they build and test the same thing?"*

**Simple Example:**
> "The system shall notify the user when their order is ready."
- Developer A: sends an in-app notification
- Developer B: sends an email
- Developer C: sends an SMS
- All three are valid interpretations of "notify"

**Corrected Version:**
> "The system shall send an email notification to the user's registered email address when order status changes to 'Ready for Pickup'."

**RxLogix Example:**
> Ambiguous: "The system shall alert the PV team when a case is overdue."
- Alert by email? In-app banner? Dashboard flag? All three?
- Who exactly is the "PV team"? All PV Officers? Only the case owner?

---

# Technique 4 — The Negative Flip Test

**Apply to:** Any requirement that only describes a positive/success scenario

**How to apply it:**
Take the requirement → flip it to negative → check if the document answers it

**Simple Example:**
> Positive: "Users with Admin role shall access the Settings panel."
> Negative flip: "What happens when a non-Admin user tries to access Settings?"
- Is there an error message? A redirect? A hidden menu?
- If the document is silent → ambiguity detected.

**RxLogix Example:**
> Positive: "A Medical Reviewer shall approve an ICSR case after review."
> Negative flip: "What happens if the Medical Reviewer rejects the case?"
- Does it go back to Draft? Back to PV Officer? With comments?
- If the document only describes approval and not rejection → ambiguity.

---

# Technique 5 — The Cross-Reference Check

**Apply to:** Requirements documents longer than 20 pages — always

**How to apply it:**
While reading, maintain a simple log of all rules and constraints.
When a new rule appears — compare it against your log.

**Simple Conflict Example:**
> Rule Log Entry: "Session timeout = 10 minutes (Req 3.2)"
> New requirement found: "Session stays active while tab is open (Req 7.8)"
> → Conflict detected. Raise for clarification.

**RxLogix Example:**
> Rule Log Entry: "Approved cases cannot be edited (Req 4.1)"
> New requirement found: "Medical Reviewer can update narrative at any stage (Req 9.3)"
> → Does "any stage" override the Approved lock? Raise for clarification.

**Tool tip:** Even a simple notepad list of rules works.
You don't need special software to do this.

---

# What to Do After Detecting Ambiguity

**Do NOT:**
- Assume an interpretation and proceed silently
- Ask the developer to decide
- Skip the requirement and test around it

**DO:**
1. Document the ambiguity clearly with the requirement reference number
2. Write your question in plain language — state what is unclear and why it matters for testing
3. Raise it through the correct channel (review meeting, JIRA, email — whatever your team uses)
4. Get written confirmation of the clarification — verbal is not enough
5. Ensure the requirement document is updated with the clarified version

**Template for raising an ambiguity:**
> "Requirement [X.X] states [quote the requirement].
> This is unclear because [specific reason].
> For testing purposes, I need to know: [specific question].
> Impact if unresolved: [what could go wrong in testing or production]."

---

# Stakeholder Validation — What & Why

**What is Stakeholder Validation?**
The process of formally confirming with the right people
that the requirements — as documented — match what was actually intended.

**Why QA must be involved:**
- Business writes what they want
- Developers build what they understood
- QA tests what the document says
- → These three can all be different things

**QA's role in validation:**
- Raise ambiguities before development starts
- Participate in requirement walkthroughs
- Confirm acceptance criteria are testable
- Ensure edge cases are covered in the spec — not discovered in production

---

# Who Are the Stakeholders?

| Stakeholder | Their Concern | What QA Needs From Them |
|---|---|---|
| Business Analyst | Is the requirement complete? | Clarification on ambiguous statements |
| Product Owner | Does this meet business goals? | Priority of requirements |
| Developer | Can this be built as written? | Feasibility of testable criteria |
| End User / Domain Expert | Does this match real workflow? | Validation of edge cases and exceptions |
| Regulatory / Compliance (RxLogix) | Does this meet regulatory standards? | Confirmation of compliance-critical requirements |

---

# How to Conduct Stakeholder Validation

**Step 1 — Prepare Your Ambiguity List Before the Meeting**
Never walk in empty-handed. Have all your flagged items documented with requirement reference numbers.

**Step 2 — Use the Requirement Walkthrough Format**
Go requirement by requirement for critical sections.
Don't just ask "any questions?" — actively walk through each "shall" statement.

**Step 3 — Confirm Acceptance Criteria**
For every requirement ask: *"How will we know this is done correctly?"*
The answer to that question is your acceptance criterion.

**Step 4 — Document Everything**
All decisions made in the meeting must be recorded.
Send a written summary after the meeting and get acknowledgement.

**Step 5 — Re-validate After Changes**
If any requirement is updated post-walkthrough — re-validate that section.
A change in one requirement can create a conflict in another.

---

# Real Scenario — Ambiguity Leading to Production Defect

**What happened (Simple E-Commerce):**
Requirement: "The system shall apply a discount for premium users."

- QA assumed: discount applies at checkout
- Developer implemented: discount applies only on orders above ₹1000
- Business expected: discount applies on all orders for premium users
- Result: Defect found in production. Customer complaints. Hotfix required.

**Root Cause:** The word "apply" had no defined condition.
Nobody validated: apply when? apply how much? apply on what?

**RxLogix Parallel:**
Requirement: "The system shall flag overdue cases."
- Flag at 7 days? 15 days? Per regulatory deadline?
- Flag for all users or only the case owner?
- Flag in the UI only or also trigger an email?
All of these needed stakeholder validation before development began.

---

# Section 1.2 — Key Takeaways

- Ambiguity in requirements is one of the top causes of production defects
- 5 types to watch for: Vague Language, Missing Conditions, Conflicting Requirements, Assumed Knowledge, Incomplete Negative Scenarios
- Use 5 detection techniques: Measurement Test, What If Test, Multi-Reader Test, Negative Flip Test, Cross-Reference Check
- After detecting ambiguity → document it, raise it, get it in writing, ensure the document is updated
- Stakeholder validation is not optional — it is a QA responsibility, not just a BA or PM responsibility
- The earlier ambiguity is resolved → the cheaper it is to fix