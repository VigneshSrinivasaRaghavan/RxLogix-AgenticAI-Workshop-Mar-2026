# Section 1.3 — Risk Identification: Technical, Business & User Experience Risks

---

# Agenda — Section 1.3

- What is Risk in Software Testing?
- Why QAs Must Think in Risks
- Three Categories of Risk
- Technical Risks — Detection & Examples
- Business Risks — Detection & Examples
- User Experience Risks — Detection & Examples
- Risk Identification Techniques
- Key Takeaways

---

# What is Risk in Software Testing?

**Definition:**
A risk is any condition, uncertainty, or gap that has the potential
to cause a negative outcome — in the system, the business, or the user's experience.

**Risk ≠ Defect**
- A defect is something already broken
- A risk is something that could break — or cause harm — if not addressed

**Two dimensions of every risk:**
- **Likelihood** — How probable is this risk occurring?
- **Impact** — How severe is the consequence if it does occur?

**The QA's job:**
Identify risks early → Prioritise testing around them →
Ensure the highest-risk areas receive the most rigorous testing.

---

# Why QAs Must Think in Risks

**Scenario:**
You have 500 test cases and 3 days to test before release.
You cannot run all 500. Which ones do you run?

**Without risk thinking:** You run whatever comes first.
**With risk thinking:** You run the highest-risk areas first.

**The consequence of ignoring risk:**
- Low-risk features get tested thoroughly
- High-risk features go to production undertested
- The defect that reaches the client is always in the area nobody prioritised

**In regulated systems like RxLogix:**
Risk thinking is not optional — regulatory frameworks
explicitly require risk-based testing approaches.

---

# Three Categories of Risk

| Category | What it Covers | Who is Affected |
|---|---|---|
| **Technical Risk** | System stability, integrations, data, performance, security | Development & QA Teams |
| **Business Risk** | Compliance, financials, legal obligations, reputation | Organisation & Stakeholders |
| **User Experience Risk** | Usability, accessibility, workflow disruption | End Users |

**Important:**
These three categories are not isolated.
One technical risk can trigger a business risk and a UX risk simultaneously.

---

# Category 1 — Technical Risks

**Definition:**
Risks arising from how the system is built, integrated,
or how it handles data, load, and security.

**Common Technical Risk Areas:**
- Integration failures between systems
- Data loss or data corruption
- Performance degradation under load
- Security vulnerabilities
- Incorrect calculations or data transformations
- Third-party dependency failures

---

# Technical Risk — Simple Examples

**Integration Risk:**
> E-Commerce: Payment gateway API changes its response format.
> The order system still expects the old format.
> Result: All payments silently fail — no error shown to the user.

**Data Corruption Risk:**
> Banking: A batch job that calculates monthly interest
> runs twice due to a server restart.
> Result: Interest is double-credited to all accounts.

**Performance Risk:**
> Retail App: Works perfectly with 10 concurrent users during testing.
> On sale day with 10,000 concurrent users — the system crashes.

**Security Risk:**
> A user manipulates the URL parameter to access
> another user's account data — no authorisation check in place.

---

# Technical Risk — RxLogix Examples

**Integration Risk:**
> RxLogix integrates with the EMA E2B gateway for ICSR submissions.
> If the gateway changes its XML schema version and RxLogix
> is not updated → all regulatory submissions fail silently.
> Regulatory deadline missed → compliance violation.

**Data Transformation Risk:**
> ICSR date fields entered as DD/MM/YYYY in the UI
> must be exported as YYYYMMDD in E2B XML.
> If the transformation logic has a bug →
> dates are exported incorrectly → submission rejected by EMA.

**Performance Risk:**
> End of quarter reporting: 500 PV Officers simultaneously
> generate aggregate safety reports.
> System slows to a halt → reports cannot be submitted
> before the regulatory deadline.

---

# How to Identify Technical Risks

**Ask these questions while reading the FRS:**

- Where does this system connect to an external system or API?
- Where is data being transformed, calculated, or converted?
- What happens to data if the system crashes mid-process?
- Are there any batch jobs or scheduled tasks — what if they run twice?
- What is the maximum expected user load — has it been specified?
- Are there any security-sensitive operations (login, payments, data export)?
- Are there any third-party dependencies — what if they are unavailable?

**Flag every "yes" answer as a technical risk area requiring focused testing.**

---

# Category 2 — Business Risks

**Definition:**
Risks that directly impact the organisation's financial position,
legal standing, regulatory compliance, or market reputation.

**Common Business Risk Areas:**
- Regulatory non-compliance
- Financial calculation errors
- Data privacy violations
- Contractual obligation failures
- Reputational damage from public-facing defects
- Missed deadlines with legal consequences

---

# Business Risk — Simple Examples

**Financial Calculation Risk:**
> E-Commerce: A discount logic bug applies a 90% discount
> instead of 9% during a flash sale.
> Result: Company loses significant revenue before the bug is caught.

**Data Privacy Risk:**
> A user can view another user's personal order history
> due to a missing access control check.
> Result: GDPR violation → regulatory fine → reputational damage.

**Contractual Risk:**
> An SLA states the system must have 99.9% uptime.
> A defect causes 4 hours of downtime.
> Result: SLA breach → financial penalty to the client.

---

# Business Risk — RxLogix Examples

**Regulatory Compliance Risk:**
> FDA requires ICSRs to be submitted within 15 calendar days
> of initial receipt for serious adverse events.
> A workflow defect delays case progression → submission missed →
> FDA issues a warning letter to the pharmaceutical company.
> This is not just a bug — it is a regulatory violation with legal consequences.

**Data Privacy Risk:**
> Patient safety data in RxLogix contains highly sensitive PII
> (name, age, medical history).
> A misconfigured access control allows unauthorised users
> to view or export patient records.
> Result: HIPAA / GDPR violation → significant regulatory fine.

**Reputational Risk:**
> A PV system that misses safety signals or fails to flag
> a drug interaction pattern damages the credibility of the
> pharmaceutical company's entire safety monitoring programme.

---

# How to Identify Business Risks

**Ask these questions while reading requirements:**

- Is there a regulatory deadline or legal obligation tied to this feature?
- Does this feature involve financial calculations, pricing, or billing?
- Does this feature handle personally identifiable information (PII)?
- What is the business consequence if this feature fails in production?
- Is there a contractual SLA tied to the availability of this feature?
- Would a failure here make news or damage the company's reputation?
- Who is the regulatory authority overseeing this product?

**In RxLogix context — always ask:**
Is this feature tied to an FDA, EMA, or ICH requirement?
If yes → it is automatically a high business risk item.

---

# Category 3 — User Experience Risks

**Definition:**
Risks that affect how easily, efficiently, and confidently
a real user can complete their tasks using the system.

**Common UX Risk Areas:**
- Confusing or misleading error messages
- Illogical workflow sequences
- Missing confirmation or undo mechanisms
- Accessibility barriers
- Poor performance perceived by the user
- Data loss due to accidental user actions

---

# UX Risk — Simple Examples

**Confusing Error Message Risk:**
> User submits a form with an error.
> System shows: "Error code 500. Contact administrator."
> User has no idea what went wrong or how to fix it.
> Result: User abandons the form. Task not completed.

**No Undo Mechanism Risk:**
> Admin accidentally deletes 200 records.
> System has no confirmation dialog and no undo.
> Result: Data permanently lost. Manual recovery required.

**Accessibility Risk:**
> A form is built without keyboard navigation support.
> A user with a motor disability cannot complete the form using a mouse.
> Result: System is unusable for that user segment.

---

# UX Risk — RxLogix Examples

**Workflow Confusion Risk:**
> A PV Officer submits a case and receives no on-screen confirmation.
> They are unsure if the submission went through.
> They submit again → duplicate case created in the system →
> Duplicate ICSR submitted to the regulatory authority →
> Compliance issue due to duplicate reporting.

**Data Loss Risk:**
> A Medical Reviewer spends 45 minutes writing a detailed case narrative.
> The browser session times out silently.
> On refresh, all narrative content is lost with no auto-save.
> Result: User frustration, productivity loss, risk of incomplete case entry.

**Error Message Risk:**
> During E2B export, a mandatory field is missing.
> System shows: "Export failed. Please try again."
> No information on which field is missing or how to fix it.
> Result: PV Officer cannot resolve the issue without developer help.

---

# How to Identify UX Risks

**Ask these questions for every user-facing feature:**

- What does the user see when something goes wrong — is the error message clear and actionable?
- Is there a confirmation step before any irreversible action (delete, submit, export)?
- What happens if the user loses connectivity mid-task — is their work saved?
- Does the workflow match how the user actually works, or does it force an unnatural sequence?
- Are all interactive elements accessible via keyboard — not just mouse?
- What happens on a slow connection or low-end device?
- Is there any step where the user might accidentally do something they cannot undo?

---

# Risk Identification Techniques

**Technique 1 — Risk Brainstorming**
Gather QA + Dev + BA in a session.
Go feature by feature. For each — ask: "What could go wrong?"
Document every answer — no filtering at this stage.

**Technique 2 — Historical Defect Analysis**
Look at past defect logs for the project or similar projects.
Recurring defect areas = high-risk areas in the current release.

**Technique 3 — Complexity Mapping**
The more complex a feature (more conditions, more integrations, more actors) →
the higher the risk. Map complexity → prioritise testing accordingly.

**Technique 4 — Regulatory/Compliance Review**
In regulated industries — cross-reference features against
the applicable regulatory standard.
Any feature tied to a regulatory obligation = automatic high risk.

**Technique 5 — New or Changed Code Analysis**
New features and recently changed code carry higher risk than stable, unchanged code.
Focus heavier testing on what changed — not just what exists.

---

# Risk Classification Matrix

| Risk | Likelihood | Impact | Priority |
|---|---|---|---|
| EMA gateway integration failure | Medium | Very High | P1 — Test Extensively |
| Session timeout with no auto-save | High | High | P1 — Test Extensively |
| Discount calculation error | Low | Very High | P2 — Test Thoroughly |
| UI label alignment issue | High | Low | P3 — Test When Time Permits |
| Report font size slightly off | Low | Low | P4 — Log & Defer |

**Rule:** Likelihood × Impact = Priority.
High impact risks always get priority — even if likelihood is low.

---

# The Risk Mindset in Daily QA Work

**Every time you read a requirement — ask three questions:**

1. **Technical:** How could this break technically?
2. **Business:** What is the consequence if this fails in production?
3. **UX:** How could this confuse or block a real user?

**You are not looking to find every possible defect.**
**You are looking to find the defects that matter most — before they reach the user.**

---

# Section 1.3 — Key Takeaways

- Risk = a condition that could cause negative outcomes — not the same as a defect
- Three categories: Technical (system), Business (organisation), UX (user)
- One technical risk can simultaneously trigger business and UX risks
- Risk identification starts at requirement review — not at test execution
- Prioritise testing based on: Likelihood × Impact
- In regulated systems — any feature tied to a regulatory obligation = automatic P1 risk
- The QA who thinks in risks is the QA who prevents the most critical production defects