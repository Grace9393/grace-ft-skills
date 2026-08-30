---
name: ica-process-studio
description: Drive IBM Consulting Advantage Process Studio — turn a corpus of client SOPs into an implementation-ready agentic blueprint. Covers the Ground/Assess/Re-imagine/Simulate flow, the Procedure Eater analysis skills, the EAEF blueprint library (APQC/BIAN/eTOM/SCOR/IBV), the Portfolio Dashboard, and the generated artifacts (process analysis report, EAEF blueprint, BPMN diagram, business case, target operating model, implementation spec), plus the closed loop with Context Studio and the hand-off to Bob. Use when the user mentions Process Studio, the Procedure Eater or "procedure eater", SOP analysis, EAEF or the EA Engineering Framework, process blueprint generation, atomic thinking step register, autonomy zones, agent register, BPMN generation from an SOP, an implementation spec for a coding agent, or an agentic business case with NPV/IRR/payback.
---

# ICA Process Studio — conduct guide

**Process Studio designs the agents. Context Studio tells them what they know.** They run
as a closed loop: the engagement that discovers what to automate leaves behind the schema,
knowledge graph and blueprints that make the next engagement faster.

Use this skill to run Process Studio. For the Context Studio half use `ica-context-studio`;
for what the two are among the wider ICA surfaces, `ica-overview`.

**Status: generally available.** Process Studio has an official User Guide, an architecture
deck and an enablement playbook. Where this skill and the User Guide disagree, the User
Guide wins.

## Two framings, both official

| Framing | Shape |
|---|---|
| **Ground → Assess → Re-imagine → Simulate** | the four steps *inside* Process Studio (User Guide) |
| **AS IS context → Process Studio → TO BE context** | the engagement-level shape (playbook) — the most practical of the three |
| The four-stage two-studio loop | below — how the two products interlock |

| Stage | Studio | What happens |
|---|---|---|
| 1 Foundation | Context Studio | define a schema, ingest the client's materials, populate the knowledge graph, verify with the built-in assistant |
| 2 Discovery | Process Studio · **Procedure Eater** | feed it the client's existing SOPs; it surfaces triggers, actors, compliance considerations and AI use cases at scale |
| 3 Reimagination | Process Studio | cognitive decomposition splits agentic from non-agentic. Out comes the agent register, target operating model, business case and BPMN |
| 4 Implementation | Context Studio → **Bob** | expose the context as an MCP server, drop the Context ID into Bob, and the coding agent generates frontend, backend and data models |

**Do not skip stage 1.** A blueprint generated without a linked context produces generic
agents — the exact failure the two studios exist to prevent. The AS IS context must reach
`Valid` status and be exposed via MCP *before* Process Studio starts.

## The workflow

### Step 1 — Create the project

Scope, industry and organisational context. **Link a Context Studio workspace.** Optionally
import from SAP Signavio or Celonis so the blueprint is grounded in observed reality.

**Models are pluggable** — Anthropic (native Claude) · AWS Bedrock · Azure OpenAI/AI
Foundry · GCP Vertex AI · LiteLLM gateway. Precedence: per-run choice > project model >
personal default > admin system default, with per-role overrides available inside a run.

Tick the artifact types you want auto-generated. **Include JSON-LD Ontologies** if the
TO BE context will be built from this project — nothing downstream can import a schema
that was never generated.

### Step 2 — Select a blueprint

Start from the **EAEF library** (EA Engineering Framework), backed by APQC PCF, APQC
industry frameworks (Banking, Consumer Products, Telco, Corporate Operations), BIAN, eTOM,
SCOR, IBM industry operations models and IBV — or start blank. **Check the repository
before generating anything.**

Observed folders: `APQC - Banking` · `APQC - Corporate Functions` · `APQC - Telco` ·
`SCOR - Supply Chain`. Corporate Functions → Finance already carries a worked blueprint,
*Accounts Payable Expense Reimbursements* (APQC PCF 9.5), with target outcome 65–80%
touchless invoice processing, 40–55% FTE reduction and 3-day cycle-time reduction.

Reference: `https://pages.github.ibm.com/Consulting-DTT-AI-Integration-Services/ea-engineering-framework/`

Built-in IP available for grounding: **CBM** (Component Business Model) for capability
decomposition · the **IBM AI Use Case Library** to seed and benchmark opportunities ·
**IBV benchmark data** for the business case. The agent returns an explicit Sources footer.

### Step 3 — Ingest and analyse

**Limits — these are Process Studio's, not Context Studio's:** 10 MB per file · 500 MB
total · 2000 files per staged upload · parallelism 1–32 (4 is a safe default). Context
Studio's separate cap is 30 files / 100 MB per batch. Do not conflate them.

Optional ingestion phases, each an independent toggle: full document text on the wiki ·
incremental runs · Vision (describes embedded PDF/PPTX images) · Synthesizer ·
Contradictions. Dry-run first, then run.

**Procedure Eater is not a separate tool.** It ships inside Process Studio as a set of
skills. Analyze tab → run an analysis → pick a Procedure Eater skill. Only skills built to
run over a whole corpus appear there; conversational skills belong in chat. Batch analysis
is what surfaces **shared capability clusters** — the basis for one consolidated platform
play instead of many one-off automations.

Then drive it with prompts. The lab sequence, verbatim:

| Prompt | Produces | Time |
|---|---|---|
| `Analyze this procedure` | **Process Analysis Report** (.md + .html) after four analysis phases | minutes |
| `Generate a process blueprint based on this analysis, keep it simple` | **EAEF blueprint** | ~15 min |
| `Create a BPMN diagram for this process` | **.bpmn** with swim lanes | minutes |
| `Build a business case for this process transformation` | **.pptx** + interactive report + .xlsx | minutes |

**The Process Analysis Report is not the blueprint.** It is the diagnosis: it reads the
procedure, captures the policy and operational reality behind it, and surfaces the AI use
cases worth pursuing. Review it before generating the blueprint — a wrong diagnosis
propagates into every downstream artifact.

Use the **Portfolio Dashboard** to re-rank surfaced use cases against client-specific
weights. Presets — Quick Wins, Max ROI, Lowest Risk, High FTE Impact — are a starting point
to argue from, not an answer. State which preset you used and why on any page showing a
ranking.

### Step 4 — Export

**JSON is the source of truth.** Edit the JSON and re-render; **hand-edited HTML is
overwritten**. Blueprints support inline editing and per-section feedback, and can be
published to a GitHub location under your prefix.

### Step 5 — Simulate (optional, Alpha)

Digital Twin compiles the blueprint into an executable spec, builds agents bound to **mock**
tools, and runs scenarios so KPIs can be observed before code is written. Opt-in; may not
be enabled in a given deployment. **BYOS** (Bring Your Own Skill) is likewise Alpha.

## What the blueprint contains

The **seven sections the User Guide names** — see the correction immediately below, the
product renders eight:

| Section | Content |
|---|---|
| **Atomic Thinking Step Register** | every step tagged `DET` (deterministic) or `AI`, with a reliability target |
| **Human-in-the-Loop Specification** | per checkpoint: reviewer role, validation scope, decision authority, review SLA, override rules — all five |
| **Agent Definition Register** | **rendered as a table**: Agent (ID) · Goal · Owned Steps · Orchestration Pattern · Tools Required · Autonomy Zone · HITL Touchpoints |
| **Data Products** | schemas, freshness, ownership |
| **Integration with Systems of Record** | the system surfaces the agents touch |
| **MCP Tool Register** | the integrations needed, classified, with auth |
| **Skills Library** | reusable skills the agents draw on |

That is **Phase 1 of six**. Phases 2–6 — context & memory engineering, agentic app
engineering, hardening & verification, activation, operations — are in
`references/eaef-phases-2-6.md`, along with the six checks to run on any generated
blueprint before quoting it.

### The User Guide's seven is an incomplete summary — the product ships eight

Settled 2026-08-15 against the official guided lab's rendered blueprint navigation, which
matches the Nestlé CA10 export section for section. **Phase 1 as the product renders it:**

| # | Section | In the User Guide's seven? |
|---|---|---|
| 1.1 | Atomic Thinking Step Register | ✅ |
| 1.2 | **Business Ontology** | ❌ omitted |
| 1.3 | **Autonomy Zone Map** | ❌ omitted |
| 1.4 | Human-in-the-Loop Specification | ✅ |
| 1.5 | Data Products Definition | ✅ |
| 1.6 | Integration with Systems of Record | ✅ |
| 1.7 | MCP Tool Register | ✅ |
| 1.8 | Agent Definition Register | ✅ |
| — | *Skills Library* | listed, but the product renders it in **Phase 3** (§3.3) |

Two independent exports agree on all eight and their order. Treat the User Guide's list as a
summary that drops two sections and borrows one from another phase — and **do not tell a
client the blueprint has seven sections.**

## The autonomy model

| Zone | Meaning | Treatment |
|---|---|---|
| **GREEN** | deterministic, rule-based, ~99.9% | runs unattended |
| **AMBER** | AI judgement, ~90–95% | named reviewer, validation scope, decision authority, review SLA, override rules |
| **RED** | stays human | not automated |

**All AI steps start AMBER.** Promotion to GREEN requires eval baselines to mature (97%+
over several cycles) and is a governance decision. GREEN means *deterministic*, not *good*.

**RED is a live zone, not a formality.** The guided lab's worked blueprint is 12 steps split
**6 GREEN / 5 AMBER / 1 RED**, the RED being a security circuit breaker. Any step where an
unattended action would create an unauthorised financial commitment, bypass segregation of
duties or cross an approval threshold is RED. A zone map showing RED = 0 on a process that
contains a threshold is wrong.

`08-finance-transformation-assessment/references/golden-threads.md` §5 carries a worked
EAEF blueprint (`general-accounting-reporting-FPA-APP.md`, APQC PCF 9.3) — read it before
generating your first one.

## The artifacts — ten types, not two

| Artifact | Format |
|---|---|
| Blueprint document | .docx · interactive HTML · Markdown · **JSON** |
| Executive deck | .pptx |
| Process diagrams | BPMN 2.0 XML · Mermaid |
| Agent Evaluation Plan | Markdown |
| Evaluation suites | Markdown · CSV — functional, behavioural, adversarial |
| Risk Register | structured document |
| **Portfolio Dashboard** | interactive HTML — scores use cases go/conditional/no-go, clusters capabilities, recommends a path |
| **Target Operating Model** | interactive HTML / document |
| **Implementation spec** | `IMPLEMENTATION_SPEC.md` |
| Audit trace | JSON |

The **implementation spec** is the coding-agent handoff — written to be the first
instruction to Claude Code, Cursor, IBM Bob or Codex. It carries build objective, hard
constraints, business rules, scope boundaries, per-screen UX contracts, tech stack, agent
and tool I/O contracts, external systems and HITL touchpoints, and it separates what the
coding agent no longer has to invent (inferred numbers flagged, confidence noted) from what
is deliberately deferred to it.

**TOM role taxonomy** — human: Chief Accountability Officer · System Architect ·
Relationship Expert · Validator. AI: Reasoning Agent · Action Agent.

## The business case

Collect these ten inputs before running it; the lab's worked set is in brackets:

volume (3,200 requests/month) · average handling time (12 min) · FTEs involved (6: 4
operators + 2 reviewers) · exception/rework rate (18%) · time per affected request (8 min) ·
system upload volumes (1,900 + 1,300/month) · approval delay (1.5 business days) · loaded
labour rate (EUR 35/hr, ~EUR 58k/FTE/yr) · control incidents in the last 12 months (4) ·
annual revenue scope (EUR 2.5B).

It compares fully-loaded manual cost against projected post-automation cost, nets off
implementation and run costs, and outputs payback period, 3-year NPV, IRR, risk-adjusted
return, FTE displacement, Monte Carlo sensitivity and margin impact.

**The business case is a separate artifact from the blueprint.** ROI, NPV and payback live
there. A TOM citing "Blueprint §6.2 ROI" is citing a section that does not carry it.

**Ask for missing data rather than letting it be inferred.** The tool will research gaps; a
researched number and a client number are not the same evidence, and the difference must be
visible on the page. Apply the benefit rules in
`08-finance-transformation-assessment/references/roadmap-and-business-case.md` §2 — FTE
displacement is only a hard saving if the headcount actually leaves.

## Data residency — check before the first upload

| Deployment | Client-confidential data? |
|---|---|
| Shared IBM instance (global) | **Not allowed** — synthetic or public only |
| Regional IBM instance | Allowed **with explicit client approval** and all security requirements met |
| Enterprise Advantage deployment (client's own cloud) | Allowed |

A team boundary is an access boundary, not a residency class. "It is our team's instance"
does not answer this question.

## Gates

1. **Review the Process Analysis Report before generating the blueprint.** It is the
   diagnosis; everything downstream inherits its errors.
2. **Check the blueprint repository before generating from blank.** Reusing an EAEF
   blueprint is the point of the library.
3. **No agent without a human approver.** Every AMBER step names the reviewer, the trigger
   and the SLA. An agent that posts to a ledger unattended is a finding, not a design.
4. **The generated business case is a draft.** Numbers the client did not supply are
   assumptions until confirmed.
5. **No generated figure is presented as a client actual.** Illustrative detail is excellent
   for grounding design and must never appear as the client's numbers, names, vendors or
   KPIs. Treat every generated figure as illustrative until a client source is cited — and
   check the `Current Value` column of §6.2 first, because that is where real exports have
   broken this.

## Where this sits with the other skills

- `ica-context-studio` — stages 1 and 4: JSON-LD schema (nodes / edges / actions /
  constraints), ingestion, "talk to the context", Expose as MCP, and the Context ID that
  Bob consumes. **Context Studio has no authoring API** — schema, context, upload, ingest
  and expose are UI only.
- `boblueprint-accelerator` (03) — routes its Step 3 through Process Studio; use this skill
  for the tool mechanics and that one for the accelerator's gates and house structure.
- `storylinea` — generates Process Studio input assets (per-process SOPs and baselines).
- `finance-transformation-assessment` (08) — the golden threads name the processes worth
  feeding in; its pain point register supplies the evidence the use cases need.

## On the published numbers

The overview material quotes 3–5× faster delivery, 1,400+ SOPs analysed in under three
days, and 200+ active users in two weeks of Alpha. These are **product claims with no
stated population or baseline** — `directional` under the citation rules in
`08-finance-transformation-assessment/references/benchmark-library.md` §0. Use them to
frame the opportunity in conversation; never put them on a client page as a benchmark, and
never present the SOP-throughput figure as a delivery commitment.

## References
- `references/eaef-phases-2-6.md` — Phases 2–6 of the blueprint, and the six checks to run
  on any generated export.
- `references/process-studio-lab.md` — the hands-on lab walkthrough, verbatim prompts,
  environment and the business case input set.
- `references/context-studio-loop.md` — the Context Studio half: schema building, ingestion
  limits, MCP exposure and client configuration.
