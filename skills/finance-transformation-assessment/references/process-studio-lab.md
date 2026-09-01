# Process Studio hands-on lab — walkthrough

Reconciled 2026-08-15 against the **official guided lab**
(`ICA-Studios-Consolidated\official-sources\Process Studio guided lab.zip`, 26 slides, IBM
Consulting FutureNow), which supersedes the earlier Box deck
(`ProcessStudio_Lab_final_v2.pptx`, also 26 slides — a different deck of the same length).

Where the two differ, the official lab wins and the difference is marked **[changed]**.

Use this to run the lab, to onboard someone, or as the script for a live demo.

## The scenario — unchanged

Marco, Global Process Owner for Source-to-Pay at a strategic client. His AP team runs an
Indonesia payments operation: validating manual payment requests from markets, building
payment files, uploading them, routing approvals. He wants agentic transformation but knows
the usual path — analysts read the SOP page by page, interview SMEs, map every task,
decision, control and hand-off, and only then start designing agents. Months.

The lab does it in one session.

## Steps

| # | Step | What you do |
|---|---|---|
| 00 | Blueprint Repository | `Explore Process Blueprints` in the left sidebar. Four domain folders: **APQC - Banking · APQC - Corporate Functions · APQC - Telco · SCOR - Supply Chain**. Open Corporate Functions → Finance → *Accounts Payable Expense Reimbursements* (APQC PCF 9.5) and read the Atomic Thinking Step Register and HITL Specification side by side |
| 01 | Project Creation | `+ New Project`. Name `AP_PAYMENTS_<YourName>`, description "AP Payments transformation" |
| 02 | Upload & analyse | Paperclip → attach the SOP (Bank Processing of ID Payments). Send **`Analyze this procedure`**. Wait for all four analysis phases; `view` the .md and .html in the File Canvas |
| 03 | Generate blueprint | Send **`Generate a process blueprint based on this analysis, keep it simple`**, then confirm `Go ahead, keep it simple`. **~15 minutes** |
| 04 | BPMN | Send **`Create a BPMN diagram for this process`** |
| 06 | Business case | Send **`Build a business case for this process transformation`** |

**[changed]** The official deck numbers its steps `00 · 01 · 02 · 03 · 04 · 06` — **05 is
skipped**. A deck numbering slip, not a missing step. Six steps, not seven.

**[changed] Access.** Team captains navigate to a **standalone AWS-hosted Process Studio
URL** (`https://ic-<id>.ecs.us-east-1.on.aws/`) and click **Sign In with IBM W3ID**. A
request is sent; approval takes a few minutes. Note the host — it is neither
`servicesessentials.ibm.com` nor a regional `*.ica.ibm.com`, which matters when establishing
the instance's residency class.

## Step 01 in detail — the project form

**[changed]** The form is richer than the earlier deck showed.

| Field | Detail |
|---|---|
| **Client Context** | *"Link Context Studio workspaces to enrich blueprints with client-specific knowledge. **You can select multiple contexts.**"* Search and tick. The lab uses **`[CLIENT]-Finance`** — IBV material on the process and domain, including benchmark data |
| **Model** | System default shown as **`aws · claude-opus-4-6-v1`**. Provider and Model are separate dropdowns; the lab picks `azure` / `5-1`, and the slide text offers "azure GPT 5 model or Opus 4.6 from GCP" |
| **Blueprints** | Multi-select of the four domain folders to include in the project |
| **Auto-Generate Artifacts** | Agent Evaluation Plan (.md + .csv) · PowerPoint · BPMN 2.0 XML · HTML Report · Mermaid Diagram · **JSON-LD Ontologies** · Risk Register (.md + .html) |
| **Collaborators** | by email, permission **Read** (view and download) or **Write** (also participate in the conversation) |

**Tick JSON-LD Ontologies** if a TO BE context will be built from this project. Without it
there is no schema to import into Context Studio, and the loop does not close.

The `[CLIENT]-Finance` context holds four files, all `ready`:
`[CLIENT]-technical-context-v2.md` · `Finance_Procurement_CHF_additional quartiles.xlsx` ·
`2025 Finance organization benchmark report – Research findings.pptx` ·
`2025 Finance organization benchmark report – KPIs by industry.pptx`.

## What a real blueprint looks like

**[new]** The official lab shows the rendered blueprint from an actual run — worth knowing
before you generate your first one.

**Executive summary tiles:**

| 12 | 50% | 50% | 10 | 10 | 14 |
|---|---|---|---|---|---|
| atomic steps | deterministic | AI-powered | agents | data products | MCP tools |

**Autonomy bar: 6 Green · 5 Amber · 1 Red.** Counts sum to 12; RED is populated. That is
the shape a correctly formed zone map has.

### The sections, as the product actually renders them

The blueprint's own navigation pane, Phase 1:

1. Atomic Thinking Step Register
2. **Business Ontology**
3. **Autonomy Zone Map**
4. Human-in-the-Loop Specification
5. Data Products Definition
6. Integration with Systems of Record
7. MCP Tool Register
8. Agent Definition Register

Then **Phase 2: Context & Memory Engineering** — Context Payload Specifications · Memory
Architecture Configuration · Audit Trace Architecture Specification.

> **[changed] This settles the seven-section question, mostly.** The Process Studio User
> Guide lists seven canonical sections and **omits Business Ontology and the Autonomy Zone
> Map**, while including *Skills Library* — which the product renders in **Phase 3**, not
> Phase 1. The product ships **eight** Phase 1 sections, and two independent exports (this
> lab and the [CLIENT] CA10 blueprint) agree on all eight and their order.
>
> Treat the User Guide's seven as an incomplete summary, not a contract. Do not tell a
> client the blueprint has seven sections.

Full Phase 2–6 structure: `eaef-phases-2-6.md`.

### Agent Definition Register — the row semantics

From the assistant's own explanation in the lab, when asked *"Can you explain the Agent
Definition section?"*:

**Agent** (name) · **Goal** · **Steps** it supports · **Pattern** (event-driven intake, AI
classification, deterministic reconciliation, guided human-in-browser execution) · **Tools**
(the MCP tools it uses) · **Zone** (GREEN / AMBER / RED) · **HITL** (the required control,
if any).

And the design principle it states: *"the process is not one single AI agent… agents in
AMBER require human confirmation, and the RED agent — the Payment Security Sentinel Agent —
can stop processing immediately if it detects credential exposure, token misuse,
unauthorized requests, or vendor banking data leakage. This preserves segregation of duties
and prevents AI from independently approving or releasing payments."*

That is what RED is for. A blueprint with no RED on a payments or approvals process has not
found its stop condition.

## Step 06 in detail — the business case has two gates

**[new]** The earlier deck showed the business case as a single prompt. It is not.

### Gate 1 — KPI Review Required

> *"The business case workflow is currently paused at the mandatory KPI review gate."*

Options: **Accept as-is** · Remove some KPIs · Modify existing KPIs · Add custom KPIs.

### Gate 2 — baseline data collection mode

> *"Please select the baseline data collection mode so I can continue."*

1. I'll provide the numbers myself
2. Research my organization externally
3. **Mix: I'll fill what I know, research the rest**
4. Use EAEF defaults for everything

> ⚠️ **Option 4 is how an unsourced number enters a business case.** It is legitimate for a
> demo and indefensible on a client page. Whichever option is chosen, record it, and mark
> every researched or defaulted figure as such. A researched number and a client number are
> not the same evidence.

### Scope selection

Before generating, it asks which process domains to include: the named domain · All domains ·
Do not proceed / adjust scope.

### The ten inputs

The lab supplies these. On a real engagement, collect them from the client.

| # | Input | Lab value |
|---|---|---|
| 1 | Monthly manual payment request volume | 3,200 requests/month |
| 2 | Average handling time per request | 12 minutes |
| 3 | AP Payments analysts involved | 6 FTE (4 operators + 2 reviewers) |
| 4 | Exception / rework rate | 18% of requests |
| 5 | Average time on attachment / amount reconciliation | 8 minutes per affected request |
| 6 | CitiDirect uploads | 1,900/month |
| 7 | QLola BRI uploads | 1,300/month |
| 8 | Average approval delay / aging after upload | 1.5 business days |
| 9 | Loaded labour rate | EUR 35/hour (~EUR 58,000/FTE/year) |
| 10 | Control incidents, last 12 months | 4 — 2 duplicate payments, 1 incorrect amount, 1 audit finding on attachment traceability |
| — | Annual revenue scope | EUR 2.5B |

### What comes out

**[new]** Three files, not two:
`*-business-case-deck.pptx` · `*-business-case-dashboard.html` · `*-business-case-financials.xlsx`

The dashboard has eleven tabs — Executive Summary · Scope · Baseline · Domains · Cash Flow ·
Scenarios · Investment · Sensitivity · Risks · Roadmap · Recommendation — and on the lab's
run reported:

| NPV | Payback | IRR | FTEs displaced | Annual saving | Year-0 investment | P(NPV > 0) |
|---|---|---|---|---|---|---|
| €1.9M (P10 €594K · P90 €2.3M) | 31 months | 73.3% | 4.4 | €209K | €798K | 99.4% (VaR 5% €400K) |

Basis: 1 domain · 5-year projection · EUR · **10,000 Monte Carlo simulations**.

You can iterate on it afterwards: discount rate, horizon, platform cost, implementation
rate and LLM assumptions · domain baselines (FTE count, cost/FTE, monthly volume, cycle
time, error rate, SLA) · KPIs · scenario assumptions (adoption bounds, benefits ramp, Monte
Carlo sensitivity ranges) · blueprint overrides (FTE impact range, cycle-time target,
deterministic/AI ratio).

**The business case is a separate artifact from the blueprint.** ROI, NPV and payback live
here. A TOM citing "Blueprint §6.2 ROI" is citing a section that does not carry it.

## Running it as a demo

Four live failure points.

1. **Access.** W3ID approval is per-person and takes minutes. Confirm the whole team is in
   before you start, not at the start. **[changed]** Team captains use the standalone AWS
   URL above.
2. **The 15-minute blueprint generation.** The lab itself suggests filling the gap with the
   EAEF documentation page. Or pre-generate one and show a finished blueprint while the live
   run proceeds.
3. **The context.** Attaching a real context is what separates a specific blueprint from a
   generic one. Attach it in step 01 or the demo undersells the product.
4. **[new] The two business-case gates.** The workflow pauses twice and waits. If you have
   not rehearsed the answers, the demo stalls at exactly the moment the audience is waiting
   for a number.

## One thing the lab exposes that is worth noticing

The lab's own screenshots show the project sidebar of a shared instance, carrying other
engagements' project names, and a blueprint containing a real client internal mailbox
address. Whatever instance you run on, assume anything you create is visible to others on
that instance — and check the residency rules in `SKILL.md` § *Data residency* before
uploading anything client-confidential.
