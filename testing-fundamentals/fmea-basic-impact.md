# Section 1.4 — FMEA Basics & Impact vs. Probability vs. Producibility Matrices

---

# Agenda — Section 1.4

- What is FMEA?
- Why QAs Use FMEA
- FMEA Structure — The 7 Columns
- FMEA Worked Example — Simple
- FMEA Worked Example — RxLogix
- Impact vs. Probability Matrix
- Producibility — The Third Dimension
- Three-Dimensional Risk Scoring
- Key Takeaways

---

# What is FMEA?

**FMEA — Failure Mode and Effects Analysis**

A structured technique used to:
- Identify all the ways a system, process, or feature can fail
- Analyse the effect of each failure
- Score each failure based on severity, likelihood, and detectability
- Prioritise which failures must be addressed before release

**Origin:**
Developed by the US Military in the 1940s.
Adopted by aerospace, automotive, healthcare, and now software industries.

**In simple terms:**
FMEA answers the question:
*"What can go wrong, how bad is it, how likely is it, and will we catch it before the user does?"*

---

# Why QAs Use FMEA

**Without FMEA:**
- Testing is based on intuition and past experience
- High-risk areas may be missed simply because no one thought of them
- No structured evidence for why certain tests were prioritised

**With FMEA:**
- Every potential failure is systematically identified and documented
- Test prioritisation is data-driven — not opinion-driven
- You can present risk decisions to management with evidence
- Regulatory auditors can see a structured risk-based testing approach

**In RxLogix context:**
Regulatory bodies like FDA and EMA expect pharmaceutical companies
to demonstrate risk-based validation approaches for their software systems.
FMEA provides exactly that documented evidence.

---

# FMEA Structure — The 7 Columns

| Column | Name | What it captures |
|---|---|---|
| 1 | **Feature / Function** | What part of the system are we analysing? |
| 2 | **Failure Mode** | In what way could this feature fail? |
| 3 | **Effect of Failure** | What is the consequence if this failure occurs? |
| 4 | **Severity (S)** | How serious is the effect? Scored 1–10 |
| 5 | **Probability (P)** | How likely is this failure to occur? Scored 1–10 |
| 6 | **Detectability (D)** | How likely are we to catch this before the user? Scored 1–10 |
| 7 | **RPN** | Risk Priority Number = S × P × D |

**RPN — Risk Priority Number:**
- Higher RPN = Higher priority to test and fix
- Maximum possible RPN = 10 × 10 × 10 = 1000
- Minimum possible RPN = 1 × 1 × 1 = 1

---

# FMEA Scoring Guide

**Severity (S) — How bad is the effect?**
| Score | Meaning |
|---|---|
| 1–2 | Negligible — minor cosmetic issue, no functional impact |
| 3–4 | Minor — small inconvenience, workaround exists |
| 5–6 | Moderate — feature partially fails, user can still proceed |
| 7–8 | High — feature fails, user cannot complete task |
| 9–10 | Critical — data loss, system crash, regulatory violation, safety risk |

**Probability (P) — How likely is the failure?**
| Score | Meaning |
|---|---|
| 1–2 | Very unlikely — rare edge case |
| 3–4 | Low — occurs occasionally under specific conditions |
| 5–6 | Moderate — occurs sometimes in normal use |
| 7–8 | High — occurs frequently |
| 9–10 | Almost certain — will occur in normal operation |

**Detectability (D) — Will we catch it before the user?**
| Score | Meaning |
|---|---|
| 1–2 | Almost certain to detect — caught by automated checks or obvious error |
| 3–4 | Likely to detect — visible during standard testing |
| 5–6 | Moderate — may be caught if specifically tested |
| 7–8 | Low — easy to miss, requires specific conditions to reproduce |
| 9–10 | Almost undetectable — silent failure, no error shown to user or tester |

---

# FMEA Worked Example — Simple (E-Commerce Checkout)

| Feature | Failure Mode | Effect | S | P | D | RPN |
|---|---|---|---|---|---|---|
| Payment Processing | Payment gateway timeout — no error shown to user | User retries → double charge | 9 | 5 | 8 | 360 |
| Discount Application | Wrong discount % applied | Customer overcharged or undercharged | 8 | 4 | 6 | 192 |
| Order Confirmation Email | Email not sent after successful order | User unaware order placed → contacts support | 5 | 6 | 7 | 210 |
| Cart Item Count | Cart shows wrong item count | Minor confusion — user can still checkout | 3 | 5 | 3 | 45 |

**Reading the results:**
- Payment gateway timeout → RPN 360 → Test this first, most extensively
- Cart item count → RPN 45 → Low priority, test when time permits
- Both failures involve the same checkout feature — but risk levels are completely different

---

# FMEA Worked Example — RxLogix (ICSR Submission Workflow)

| Feature | Failure Mode | Effect | S | P | D | RPN |
|---|---|---|---|---|---|---|
| E2B XML Export | Date format transformation error | EMA rejects submission → regulatory deadline missed | 10 | 5 | 8 | 400 |
| ICSR Submission Workflow | Case stuck in "Under Review" — no alert sent | Submission deadline missed silently | 9 | 6 | 9 | 486 |
| Case Narrative Field | Session timeout — narrative content lost | PV Officer re-enters data → duplicate risk | 7 | 7 | 6 | 294 |
| Signal Detection Report | Incorrect aggregation of ICSR data | Safety signal missed → patient safety risk | 10 | 3 | 8 | 240 |
| User Access Control | PV Officer can view other company's cases | Data privacy violation — GDPR / HIPAA breach | 10 | 2 | 7 | 140 |

**Reading the results:**
- Case stuck in workflow → RPN 486 → Highest priority
- E2B date format → RPN 400 → Second priority
- Access control breach → RPN 140 → Lower RPN but Severity = 10
- **Rule: Never ignore a Severity 9 or 10 item — regardless of RPN**

---

# The Golden Rule of FMEA

**RPN is a guide — not an absolute.**

**Always override RPN when Severity = 9 or 10:**
Even if Probability is 1 (very unlikely) and Detectability is 1 (easy to catch) →
S=10 × P=1 × D=1 = RPN of just 10

But a Severity 10 failure means:
- Patient safety risk
- Regulatory violation
- Data loss
- System crash

**These must be tested regardless of their RPN score.**

**Simple Rule:**
- RPN ≥ 200 → Must test. High priority.
- RPN 100–199 → Should test. Medium priority.
- RPN < 100 → Test when time permits. Low priority.
- Severity 9 or 10 → Always test. Non-negotiable.

---

# Impact vs. Probability Matrix

**The 2x2 Risk Matrix — A Visual Risk Prioritisation Tool**

|  | **LOW PROBABILITY** | **HIGH PROBABILITY** |
|---|---|---|
| **HIGH IMPACT** | 🟡 MITIGATE — Test thoroughly | 🔴 CRITICAL — Test first |
| **LOW IMPACT** | 🟢 ACCEPT — Low priority | 🟠 MONITOR — Test if time |

**Four Quadrants:**
- 🔴 **Critical** (High Impact + High Probability) → Test first, most rigorously
- 🟡 **Mitigate** (High Impact + Low Probability) → Test thoroughly — even if unlikely, consequence is severe
- 🟠 **Monitor** (Low Impact + High Probability) → Note it, test if time allows
- 🟢 **Accept** (Low Impact + Low Probability) → Lowest priority, document and move on

**Four Quadrants:**
- **Critical** (High Impact + High Probability) → Test first, most rigorously
- **Mitigate** (High Impact + Low Probability) → Test thoroughly — even unlikely, consequence is severe
- **Monitor** (Low Impact + High Probability) → Note it, test if time allows
- **Accept** (Low Impact + Low Probability) → Lowest priority, document and move on

---

# Impact vs. Probability — Mapping Examples

**Simple Examples:**
| Risk | Impact | Probability | Quadrant | Action |
|---|---|---|---|---|
| Payment double charge | High | Medium | Critical | Test first |
| Homepage logo misaligned | Low | High | Monitor | Test if time |
| Data loss on system crash | High | Low | Mitigate | Test thoroughly |
| Tooltip text has typo | Low | Low | Accept | Log and defer |

**RxLogix Examples:**
| Risk | Impact | Probability | Quadrant | Action |
|---|---|---|---|---|
| ICSR submission deadline missed | High | Medium | Critical | Test first |
| E2B XML field mapping error | High | Low | Mitigate | Test thoroughly |
| Report font size off by 1pt | Low | High | Monitor | Test if time |
| Unused admin menu item visible | Low | Low | Accept | Log and defer |

---

# Producibility — The Third Dimension

**What is Producibility?**
Also called **Detectability** in FMEA — but in broader risk matrices,
Producibility asks a slightly different question:

*"How difficult is it to reproduce this failure during testing?"*

**Why it matters:**
- A failure that is easy to reproduce → easy to confirm, fix, and verify
- A failure that is hard to reproduce → easy to miss in testing,
  likely to slip into production undetected

**Producibility Scale:**
| Score | Meaning |
|---|---|
| Low (1–3) | Easy to reproduce — happens consistently under standard conditions |
| Medium (4–6) | Reproducible under specific conditions — requires setup |
| High (7–10) | Difficult to reproduce — timing-dependent, load-dependent, or environment-specific |

---

# Producibility — Examples

**Easy to Reproduce (Low Producibility Risk):**
> Login with wrong password → error message always appears
> → Easy to test, easy to verify fix

**Medium Producibility:**
> Session timeout data loss → must wait for exact timeout duration
> → Requires specific test setup and timing

**Hard to Reproduce (High Producibility Risk):**
> Payment gateway timeout under high load
> → Only occurs when server is under stress + network is slow simultaneously
> → Very easy to miss in standard testing environments

**RxLogix Example (High Producibility Risk):**
> E2B submission failure when EMA gateway is under maintenance
> → Cannot be reproduced in a standard test environment
> → Requires a mock gateway or dedicated integration test environment
> → High producibility score → must be flagged as a testing risk

---

# Three-Dimensional Risk Scoring

**Combining all three dimensions for complete risk assessment:**

| Dimension | Question Asked | Scored As |
|---|---|---|
| **Impact** | How severe is the consequence? | 1–10 |
| **Probability** | How likely is this to occur? | 1–10 |
| **Producibility** | How hard is this to reproduce in testing? | 1–10 |

**Combined Risk Score = Impact × Probability × Producibility**

**Worked Example:**
> Risk: ICSR case stuck in workflow — no alert sent

| Dimension | Score | Reasoning |
|---|---|---|
| Impact | 9 | Regulatory submission deadline missed |
| Probability | 6 | Workflow transitions happen frequently |
| Producibility | 8 | Timing-dependent — hard to reproduce consistently |
| **Combined Score** | **432** | **Highest priority — test first** |

---

# FMEA in Practice — Step by Step

**Step 1 — List all features and functions under test**
Break the system into testable components.

**Step 2 — For each feature, brainstorm all failure modes**
Ask: "In what ways could this fail?" — no filtering at this stage.

**Step 3 — Describe the effect of each failure**
What does the user, the business, or the system experience?

**Step 4 — Score Severity, Probability, Detectability**
Use the scoring guide. Be honest — do not underestimate.

**Step 5 — Calculate RPN**
Multiply the three scores: S × P × D

**Step 6 — Prioritise**
Sort by RPN descending. Flag all Severity 9/10 items regardless of RPN.

**Step 7 — Map to test cases**
Highest RPN items → most test cases, most rigorous coverage.

---

# Section 1.4 — Key Takeaways

- FMEA = a structured technique to identify, score, and prioritise failures before they reach production
- Seven columns: Feature → Failure Mode → Effect → Severity → Probability → Detectability → RPN
- RPN = S × P × D → Higher RPN = Higher test priority
- Never ignore Severity 9 or 10 items — regardless of RPN score
- Impact vs. Probability Matrix = a visual tool to quickly categorise and act on risks
- Producibility = how hard a failure is to reproduce — high producibility = high testing risk
- Three-dimensional scoring (Impact × Probability × Producibility) gives the most complete risk picture
- FMEA is not a one-time exercise — revisit it when requirements change