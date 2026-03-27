# Topic 1: Requirements & Risk Analysis
## Section 1.1 — Reading BRDs/FRS & Requirement Interpretation Techniques

---

# Agenda — Section 1.1

- What is a BRD vs. FRS?
- How to Read a BRD — 5 Steps
- How to Read an FRS — 4 Key Techniques
- Common Mistakes QAs Make
- Key Takeaways

---

# BRD vs. FRS — What's the Difference?

**BRD — Business Requirements Document**
- Written by: Business Analysts / Product Owners
- Answers: WHAT the business needs
- Language: Business terminology
- Audience: Stakeholders, Management, Dev, QA

**FRS — Functional Requirements Specification**
- Written by: Business Analysts / Solution Architects
- Answers: HOW the system should behave
- Language: Functional / Technical detail
- Audience: Development & QA

---

# BRD vs. FRS — Side by Side Example

**Simple Example (E-Commerce):**
- BRD: "Customers must be able to track their orders."
- FRS: "System shall display order status (Placed / Shipped / Delivered) on the Order Details page. Status shall refresh every 30 minutes via API call."

**RxLogix Example (Pharmacovigilance):**
- BRD: "PV users must be able to generate E2B(R3) reports."
- FRS: "System shall export case data in ICH E2B(R3) XML format per ICH M2 guidelines. If mandatory fields are missing → display validation error list before allowing export."

**As a QA — You Test Both Layers:**
- Does the feature work as described? ✅
- Does it behave exactly as the FRS specifies? ✅

---

# How to Read a BRD — 5 Steps

1. **Read the Objective Section First** → Understand WHY the feature exists
2. **Identify Actors and Their Roles** → Who uses it and with what permissions?
3. **Highlight Every "Shall" Statement** → Each "shall" = a testable requirement
4. **Map Requirements to Functional Areas** → Build your test coverage map
5. **Read Assumptions & Constraints** → Know what is OUT of scope

---

# Step 1 — Read the Objective First

**Simple Example:**
> BRD Objective: "Allow customers to return products within 30 days to improve satisfaction scores."
> QA insight: Returns are tied to a business KPI — any defect in the return flow directly impacts customer satisfaction metrics. Test thoroughly.

**RxLogix Example:**
> BRD Objective: "Enable PV teams to identify safety signals from aggregated ICSR data to meet EMA and FDA regulatory obligations."
> QA insight: This is a regulatory compliance feature — not just a search tool. A missed signal = a compliance failure. Test cases must be exhaustive.

**The Rule:** Understanding WHY prevents you from writing shallow test cases.

---

# Step 2 — Identify Actors & Their Roles

**Simple Example (Banking App):**
| Actor | Role |
|---|---|
| Customer | Views account balance, transfers funds |
| Bank Manager | Approves large transactions |
| System Admin | Manages user access |

**RxLogix Example (ICSR Workflow):**
| Actor | Role |
|---|---|
| PV Officer | Submits the safety case |
| Medical Reviewer | Reviews and approves the case |
| Regulatory Affairs Manager | Triggers E2B export to agency |

**The Rule:** Each actor = separate test scenarios. Never test with only one user type.

---

# Step 3 — "Shall" = Testable Requirement

**FRS Statement (Simple):**
> "The system **shall** allow password reset only via registered email."

**Test Cases Generated:**
- Reset via registered email → ✅ Should work
- Reset via unregistered email → ❌ Should be blocked
- Reset link expires after 24hrs → ✅ Should expire

**FRS Statement (RxLogix):**
> "The system **shall** allow case narrative editing only by a Medical Reviewer."

**Test Cases Generated:**
- PV Officer tries to edit → ❌ Blocked
- Medical Reviewer edits → ✅ Allowed
- Editing after case is locked → ❌ Blocked for everyone

**The Rule:** 1 "shall" statement = multiple test cases. Never just 1.

---

# Step 4 — Map Requirements to Functional Areas

**After highlighting all "shall" statements → Group them:**

| Functional Area | Simple Example | RxLogix Example |
|---|---|---|
| Data Entry | "User shall enter delivery address" | "PV Officer shall enter patient demographics" |
| Validation | "System shall reject expired credit cards" | "System shall block submission if AE date missing" |
| Workflow | "Manager shall approve refunds > $500" | "Medical Reviewer shall approve before export" |
| Reports | "System shall generate monthly sales PDF" | "System shall generate E2B(R3) XML on demand" |
| Notifications | "System shall email order confirmation" | "System shall email PV Officer on case rejection" |

**This grouping = your Test Coverage Map**
- Ensures no functional area is left untested
- Highlights areas with too few requirements → possible spec gap

---

# Step 5 — Read Assumptions & Constraints

**This section is most often skipped. Never skip it.**
- Tells you what the system is NOT responsible for
- Prevents you from raising invalid defects

**Simple Example:**
> Assumption: "The payment gateway handles fraud detection. The application is not responsible for flagging fraudulent transactions."
> QA Action: Do NOT raise a defect if the app passes a fraudulent card to the gateway. That is the gateway's responsibility.

**RxLogix Example:**
> Assumption: "The system assumes all incoming E2B(R2) files are well-formed XML. Malformed XML handling is out of scope."
> QA Action: Do NOT raise a defect for malformed XML crashes. Log it as a risk observation — not a defect.

---

# How to Read an FRS — 4 Key Techniques

1. **Boundary Value Extraction** — Find every field limit and test at the edges
2. **State Transition Reading** — Map every status/workflow flow
3. **Negative Path Reading** — For every "can do", ask "what if cannot?"
4. **Data Flow Reading** — Trace how data enters, transforms, and exits

---

# Technique 1 — Boundary Value Extraction

**Simple Example (Registration Form):**
> FRS: "Username shall be between 6 and 20 characters."

| Test | Input | Expected |
|---|---|---|
| Below minimum | 5 chars | ❌ Rejected |
| At minimum | 6 chars | ✅ Accepted |
| At maximum | 20 chars | ✅ Accepted |
| Above maximum | 21 chars | ❌ Rejected |

**RxLogix Example:**
> FRS: "Case narrative field shall accept maximum 20,000 characters."
- 19,999 chars → ✅ Accepted
- 20,000 chars → ✅ Accepted (boundary)
- 20,001 chars → ❌ Rejected

**The Rule:** Always test at, just below, and just above every boundary.

---

# Technique 2 — State Transition Reading

**Simple Example (E-Commerce Order):**
Placed → Confirmed → Shipped → Delivered → Return Requested → Refunded

> FRS: "A Shipped order cannot be cancelled. Only Placed or Confirmed orders can be cancelled."
- Cancel a Placed order → ✅ Allowed
- Cancel a Shipped order → ❌ Blocked. What error message shows?

**RxLogix Example (ICSR Case):**
Draft → Submitted → Under Review → Approved → Exported

> FRS: "Only a Medical Reviewer can send an Approved case back to Under Review."
- PV Officer tries to send back → ❌ Blocked
- Medical Reviewer sends back → ✅ Allowed

**The Rule:** Draw the state diagram. Test every arrow — including invalid transitions.

---

# Technique 3 — Negative Path Reading

**Simple Example (Login):**
> FRS: "User can login only with valid credentials."

| Test | Action | Expected |
|---|---|---|
| Positive | Correct username + password | ✅ Login success |
| Negative 1 | Wrong password | ❌ "Invalid credentials" error |
| Negative 2 | Blank username | ❌ "Username required" error |
| Negative 3 | Account locked after 5 attempts | ❌ "Account locked" error |

**RxLogix Example:**
> FRS: "PV Officer can submit a case only after all mandatory fields are filled."
- All fields filled → ✅ Submit success
- Patient Age blank → ❌ Error shown
- All fields filled but 0-byte attachment → ❌ Blocked with file error

**The Rule:** For every "can do" in the FRS → design a "cannot do" test.

---

# Technique 4 — Data Flow Reading

**Simple Example (Banking Transfer):**
User enters ₹5000 → App validates → Core Banking System processes → SMS sent → Balance updated

> QA must verify: Does the balance shown in the app match what Core Banking processed? Does the SMS show the correct amount?

**RxLogix Example (ICSR Data Flow):**
UI Entry (DD/MM/YYYY) → Database → E2B XML Export → EMA Gateway

> QA must verify: Date of Birth entered as 15/03/1990 in UI → Does E2B XML show 19900315? (YYYYMMDD is the mandatory E2B format)
> A format mismatch = regulatory non-compliance — not just a cosmetic bug.

**The Rule:** Don't just test the UI. Trace the data end-to-end at every stage.

---

# Common Mistakes QAs Make

| Mistake | Real Consequence |
|---|---|
| Only reading happy path sections | Edge case defects reach production |
| Skipping the Glossary | Misunderstanding domain terms → wrong test cases |
| Ignoring Change History | Testing against outdated requirements |
| Skipping integration/interface sections | Missing cross-system data validation |
| Treating all requirements equally | High-priority requirements get under-tested |

---

# Section 1.1 — Key Takeaways

- **BRD** = Business intent (WHAT) | **FRS** = Functional specification (HOW)
- Read BRDs in 5 steps: Objective → Actors → "Shall" → Coverage Map → Assumptions
- Use 4 FRS techniques: Boundary Extraction, State Transition, Negative Path, Data Flow
- Always ask: **"Is this requirement high-priority / compliance-driven?"**
  - If YES → Zero-defect tolerance. Exhaustive testing. No shortcuts.
- A QA who reads requirements well catches defects **before** writing a single test case.

---