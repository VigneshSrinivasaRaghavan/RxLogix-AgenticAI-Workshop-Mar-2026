# Section 2.2 — Requirements Traceability Matrix (RTM) & Peer Reviews

---

# Agenda — Section 2.2

- What is an RTM?
- Why RTM is Critical for QA
- RTM Structure — Column by Column
- Building an RTM — Step by Step
- RTM Worked Example — Simple
- RTM Worked Example — RxLogix
- Reading and Using an RTM
- What is a Peer Review?
- Types of Peer Reviews
- How to Conduct an Effective Peer Review
- Peer Review in Practice — Examples
- Key Takeaways

---

# What is an RTM?

**RTM — Requirements Traceability Matrix**

A document that maps every requirement to its corresponding
design elements, test cases, and defects —
ensuring nothing is built without a requirement
and nothing is required without being tested.

**In simple terms:**
The RTM answers three critical questions:

- **Coverage:** Is every requirement covered by at least one test case?
- **Orphans:** Are there test cases that do not trace back to any requirement?
- **Gaps:** Are there requirements with no test cases written against them?

**The RTM is the single source of truth
for test coverage in a project.**

---

# Why RTM is Critical for QA

**Without an RTM:**
- Requirements can be forgotten during test planning
- New test cases get added with no clear purpose
- Coverage cannot be measured or reported objectively
- In audits — there is no evidence that all requirements were tested

**With an RTM:**
- Every requirement is accounted for
- Test coverage is measurable and reportable
- Gaps are visible before testing begins — not after
- Changes to requirements are immediately reflected as coverage gaps

**In RxLogix context:**
Regulatory validation frameworks (like GAMP 5)
explicitly require traceability from requirements to test cases.
An RTM is not optional in a regulated PV system —
it is a compliance document.

---

# RTM Structure — The Columns

| Column | Name | What it captures |
|---|---|---|
| 1 | **Requirement ID** | Unique identifier from the BRD/FRS (e.g. REQ-001) |
| 2 | **Requirement Description** | Brief description of what the requirement states |
| 3 | **Requirement Type** | Functional / Non-Functional / Regulatory |
| 4 | **Priority** | High / Medium / Low |
| 5 | **Test Case ID(s)** | All test cases written to cover this requirement |
| 6 | **Test Status** | Not Run / Pass / Fail / Blocked |
| 7 | **Defect ID(s)** | Any defects raised against this requirement |
| 8 | **Coverage Status** | Covered / Partially Covered / Not Covered |

**Minimum viable RTM:**
Columns 1, 2, 5, and 8 at a minimum.
The more columns — the more useful for reporting and audits.

---

# Building an RTM — Step by Step

**Step 1 — Extract All Requirements**
Go through the BRD and FRS.
List every requirement with its ID and description.
Do not filter or skip — every requirement must appear.

**Step 2 — Classify Each Requirement**
Mark each as Functional, Non-Functional, or Regulatory.
Assign a priority: High, Medium, or Low.

**Step 3 — Map Test Cases to Requirements**
For each requirement — list every test case that covers it.
One requirement can have multiple test cases.
One test case can cover multiple requirements.

**Step 4 — Identify Coverage Gaps**
Any requirement with no test case mapped = a coverage gap.
Flag it immediately — do not proceed to execution with gaps.

**Step 5 — Update Throughout the Lifecycle**
RTM is a living document.
Update test status after each test run.
Add defect IDs when defects are raised.
Re-check coverage whenever a requirement changes.

---

# RTM Worked Example — Simple (E-Commerce Checkout)

| Req ID | Requirement | Type | Priority | Test Case IDs | Status | Defect ID | Coverage |
|---|---|---|---|---|---|---|---|
| REQ-001 | User shall add items to cart | Functional | High | TC-001, TC-002 | Pass | — | Covered |
| REQ-002 | System shall apply valid discount codes | Functional | High | TC-003, TC-004, TC-005 | Fail | DEF-101 | Covered |
| REQ-003 | System shall send order confirmation email | Functional | Medium | TC-006 | Pass | — | Covered |
| REQ-004 | Checkout shall load within 3 seconds | Non-Functional | High | TC-007 | Not Run | — | Partially Covered |
| REQ-005 | System shall support payment via UPI | Functional | High | — | — | — | Not Covered |

**Reading this RTM:**
- REQ-002 has a failing test and an open defect → needs fix and retest
- REQ-004 is not yet run → testing is incomplete
- REQ-005 has no test cases → critical gap → must be addressed before release
- No release should be approved while REQ-005 shows "Not Covered"

---

# RTM Worked Example — RxLogix (ICSR Workflow)

| Req ID | Requirement | Type | Priority | Test Case IDs | Status | Defect ID | Coverage |
|---|---|---|---|---|---|---|---|
| REQ-101 | PV Officer shall submit ICSR with all mandatory fields | Functional | High | TC-101, TC-102, TC-103 | Pass | — | Covered |
| REQ-102 | System shall validate submission within 15-day window | Regulatory | High | TC-104, TC-105 | Fail | DEF-201 | Covered |
| REQ-103 | Medical Reviewer shall approve or reject cases | Functional | High | TC-106, TC-107, TC-108 | Pass | — | Covered |
| REQ-104 | System shall export cases in E2B(R3) XML format | Regulatory | High | TC-109, TC-110 | Not Run | — | Partially Covered |
| REQ-105 | System shall restrict case access by organisation | Functional | High | — | — | — | Not Covered |
| REQ-106 | System shall respond to all actions within 5 seconds | Non-Functional | Medium | TC-111 | Pass | — | Covered |

**Reading this RTM:**
- REQ-102 has a failing regulatory test → open defect → release blocker
- REQ-104 not yet run → E2B export untested → high risk before release
- REQ-105 has no test cases → access control gap → security and compliance risk
- In a regulated system → any Regulatory type requirement showing Fail or Not Covered
  = automatic release blocker

---

# RTM as a Reporting Tool

**Using the RTM to report test progress to stakeholders:**

| Metric | How RTM Provides It |
|---|---|
| Total requirements | Count of all rows |
| Requirements covered | Count of rows with Coverage = Covered |
| Requirements not covered | Count of rows with Coverage = Not Covered |
| Test pass rate | Pass count ÷ Total test cases run |
| Open defects by requirement | Count of rows with Defect ID filled |
| Release readiness | Zero "Not Covered" rows + Zero open P1 defects |

**Simple status report from RTM:**
> "As of today: 45 of 50 requirements are covered.
> 3 requirements have open defects.
> 2 requirements have no test cases — both are under review.
> Release readiness: Not yet achieved."

**This report takes 5 minutes to generate from a well-maintained RTM.**

---

# Common RTM Mistakes to Avoid

| Mistake | Consequence |
|---|---|
| Building RTM after test cases are written | Requirements may have been missed from the start |
| Not updating RTM after requirement changes | RTM becomes inaccurate — coverage reporting is wrong |
| Mapping one generic test case to all requirements | False coverage — requirements appear covered but are not |
| Ignoring non-functional requirements in RTM | Performance, security, accessibility go untested |
| Treating RTM as a one-time document | Stale RTM gives false confidence at release time |

**The golden rule:**
RTM is built from requirements — not from test cases.
Start with the requirement. Then write the test cases to cover it.
Never work backwards.

---

# What is a Peer Review?

**Definition:**
A structured process where one or more team members
examine a work product — requirements, test cases, test plans,
or designs — to identify errors, gaps, and improvements
before the work product is used or executed.

**What can be peer reviewed in QA:**
- Requirement documents (BRD / FRS)
- Test plans
- Test cases and test scripts
- RTM
- Defect reports
- Automated test code

**The core principle:**
The author of any document is the least qualified person
to find errors in it — because they will read what they intended,
not what they actually wrote.

---

# Why Peer Reviews Work

**The psychology:**
When you write something — your brain auto-corrects as you re-read it.
You see what you meant — not what you wrote.
A second reader sees what is actually there.

**The data:**
Industry studies show peer reviews catch
60–90% of defects before testing even begins.

**What peer reviews find that self-review misses:**
- Ambiguous test steps that only the author understands
- Test cases that test the same thing twice (redundancy)
- Missing negative scenarios and edge cases
- Incorrect expected results
- Test cases that do not map to any requirement (orphan tests)
- Requirements that have no test case coverage (gaps)

---

# Types of Peer Reviews

**1. Informal Review (Buddy Check)**
- One colleague reads through your work and gives verbal feedback
- No formal process or documentation
- Best for: Quick checks on small work products

**2. Walkthrough**
- Author presents the work product to the team
- Team asks questions and suggests improvements
- Author leads — team follows
- Best for: Complex test plans or new feature test strategies

**3. Technical Review**
- A structured review led by a moderator (not the author)
- Focus on correctness, completeness, and standards compliance
- Findings are documented and tracked
- Best for: RTMs, test plans for regulated features

**4. Formal Inspection**
- The most rigorous review type
- Defined roles: Moderator, Author, Reviewers, Scribe
- Entry and exit criteria must be met
- All findings logged and resolved before sign-off
- Best for: Regulatory validation documents in systems like RxLogix

---

# When to Use Each Review Type

| Situation | Recommended Review Type |
|---|---|
| Quick check on 5 new test cases | Informal / Buddy Check |
| New feature test plan for a complex workflow | Walkthrough |
| RTM for a major release | Technical Review |
| Test cases for a regulated ICSR submission feature | Formal Inspection |
| Automated test script written by a junior QA | Technical Review |
| Defect report with unclear reproduction steps | Informal / Buddy Check |

---

# How to Conduct an Effective Peer Review

**Step 1 — Define the Scope**
What exactly is being reviewed? Full test plan? Specific test cases?
Be specific — unfocused reviews produce unfocused feedback.

**Step 2 — Distribute in Advance**
Send the work product to reviewers at least 24 hours before the session.
Reviewers must read independently before the group session.
Never review cold — it wastes everyone's time.

**Step 3 — Use a Review Checklist**
Give reviewers a specific checklist to work from.
Without a checklist — reviewers focus on what interests them,
not what matters most.

**Step 4 — Document All Findings**
Every issue raised must be logged — not just discussed and forgotten.
Assign each finding: Major (blocks usage), Minor (needs improvement), Suggestion.

**Step 5 — Author Resolves — Reviewer Confirms**
The author addresses each finding.
The original reviewer confirms the resolution — not the author.
This prevents authors from self-approving their own fixes.

---

# Peer Review Checklist — Test Cases

**Completeness:**
- Does every test case have a clear objective?
- Are all mandatory fields covered — including boundary values?
- Are negative scenarios included alongside positive ones?
- Are all actors / user roles covered?

**Clarity:**
- Are test steps written clearly enough for someone unfamiliar with the feature?
- Is the expected result specific and measurable — not vague?
- Are any steps ambiguous or open to interpretation?

**Traceability:**
- Does every test case map to at least one requirement in the RTM?
- Are there any orphan test cases with no requirement mapping?

**Coverage:**
- Are there any requirements in the RTM with no test case coverage?
- Are edge cases, boundary values, and exception flows covered?

---

# Peer Review in Practice — Simple Example

**Work Product:** Test cases for an e-commerce discount feature

**Finding 1 — Major:**
> TC-004 tests a 10% discount code.
> No test case exists for an expired discount code.
> Missing negative scenario → gap in coverage.
> Action: Author to add TC-004b — expired code test.

**Finding 2 — Minor:**
> TC-003 expected result states: "Discount applied correctly."
> This is vague — does not state the expected discounted amount.
> Action: Update expected result to: "Order total reduced by 10% — from ₹1000 to ₹900."

**Finding 3 — Suggestion:**
> TC-005 and TC-006 test the same discount code on two different products.
> Consider combining into one parameterised test case to reduce redundancy.

---

# Peer Review in Practice — RxLogix Example

**Work Product:** Test cases for ICSR submission workflow

**Finding 1 — Major:**
> REQ-102 requires validation of the 15-day submission window.
> TC-104 tests submission on day 14 (pass) and day 16 (fail).
> No test case covers submission on exactly day 15 — the boundary.
> Action: Add TC-104c — submit on day 15 → verify system accepts.

**Finding 2 — Major:**
> REQ-105 (case access restricted by organisation) has no test cases in RTM.
> This is a security and compliance requirement.
> Action: Author to write test cases for REQ-105 before review sign-off.

**Finding 3 — Minor:**
> TC-108 — Medical Reviewer rejection flow.
> Test steps do not specify what happens to the case after rejection.
> Expected result only states "case rejected" — does not confirm
> whether case returns to Draft or to PV Officer queue.
> Action: Clarify expected result based on FRS section 4.3.

---

# RTM + Peer Review — Working Together

**How they complement each other:**

| RTM | Peer Review |
|---|---|
| Shows WHAT is covered | Shows HOW well it is covered |
| Identifies missing test cases (gaps) | Identifies weak or incorrect test cases |
| Tracks status across the lifecycle | Improves quality before execution begins |
| Provides audit evidence of coverage | Provides audit evidence of review rigour |

**The combined workflow:**
1. Build RTM from requirements
2. Write test cases mapped to RTM
3. Peer review the test cases
4. Update RTM based on review findings
5. Execute tests and update RTM with results
6. Use RTM to report release readiness

**This workflow gives you both breadth (RTM) and depth (peer review)
in your test coverage.**

---

# Section 2.2 — Key Takeaways

- RTM maps every requirement to test cases, execution status, and defects
- RTM is built from requirements first — never backwards from test cases
- Any requirement showing "Not Covered" = a gap that must be resolved before release
- In regulated systems — Regulatory type requirements showing Fail or Not Covered = release blocker
- Peer reviews catch 60–90% of defects before testing begins
- Four review types: Informal, Walkthrough, Technical Review, Formal Inspection
- Use a checklist in every review — unfocused reviews produce unfocused results
- RTM and peer reviews work together — RTM ensures breadth, peer reviews ensure depth
- A well-maintained RTM is your most powerful tool for communicating release readiness to stakeholders