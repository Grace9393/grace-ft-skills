---
name: finance-transformation-assessment
description: Conduct an end-to-end Finance Transformation assessment and carry it through to generated agentic artifacts — ground the client context, define the target operating model, benchmark against industry quartiles, diagnose pain points across the five lenses (people / policy / process / data / technology), quantify value at stake, build the phased roadmap and business case, then draft use-case blueprints and render the deck and Excel model in IBM Consulting house style. Absorbs the ICA Process Studio and Context Studio tool mechanics and the Blueprint Accelerator production line. Use when the user mentions finance transformation, current-state/as-is assessment, target operating model, capability or maturity assessment, benchmarking, pain point analysis, value at stake, transformation roadmap, business case, CFO agenda diagnostic, house style / banned marketing words in a finance deliverable, the golden threads (RTR / Record-to-Report, OTC / Order-to-Cash, S2P / Source-to-Pay) and their AI use case modals, Process Studio, the Procedure Eater, SOP analysis, EAEF or the EA Engineering Framework, atomic thinking step register, autonomy zones, agent register, BPMN generation from an SOP, an implementation spec for a coding agent, Context Studio, knowledge graphs or MCP-served context in ICA, Boblueprint, the blueprint accelerator, client schema/ontology, or use-case blueprints.
---

# Finance Transformation Assessment — conduct guide

You are conducting a consulting-grade finance transformation assessment and carrying it through to
generated artifacts. It runs in six phases and ends in three deliverables: **(1) Assessment Findings
& target operating model**, **(2) Transformation Roadmap & Business Case**, **(3) the deck + Excel
model** that carry them — plus the use-case blueprints the roadmap names.

This skill absorbs three formerly separate skills. The method is the spine; the tools serve it:

| Layer | What it is | Where it runs |
|---|---|---|
| **Method** | this assessment — phases, gates, evidence rules | all six phases |
| **Grounding** | Context Studio — schema, knowledge graph, MCP exposure | Phase 0 |
| **Production line** | the Blueprint Accelerator — research → schema → blueprint → deck | Phase 0 and Phase 5 |
| **Generation** | Process Studio — Procedure Eater, EAEF blueprints, BPMN, business case | Phases 3, 4, 5 |

Tool mechanics live in `references/ica-studios.md` and `references/accelerator.md`. The rules
governing what happens when a tool and the method both produce the same artifact are in
`references/tool-method-integration.md` — **read that before running any generation step.**

## Vocabulary — read first

**"Blueprint" means three different things across these tools.** Blurring them produces
deliverables that cite sections which do not exist.

| Term | What it is | Owner |
|---|---|---|
| **Use-case blueprint** | the house deliverable: narrative → 4 pain points → 3 agents → user benefits → 4 business benefits → checkpoint flags | Blueprint Accelerator |
| **EAEF blueprint** | the Process Studio artifact: 8 sections, Phase 1 of 6, starting at the Atomic Thinking Step Register | Process Studio |
| **Target operating model (TOM)** | the function-level architecture this skill's Phase 1 produces: seven layers at Level 2 | this skill |

Never call the TOM a blueprint. Never assume a use-case blueprint and an EAEF blueprint share a
section list — they share neither structure nor counts. The full contract, the closed enums, the
house voice rules and the two-taxonomy reconciliation are in
`references/house-style-and-blueprint-contract.md` — **read it before drafting any client-facing
content**, and defer to `H:\My Drive\AA\blueprint-accelerator` wherever the two disagree.

## Six hard rules, applied at every phase

1. **Every number traces to client data or a cited benchmark.** Never estimate a client
   metric. Missing data goes to the "Data requests / further analysis" list — visible in the
   deliverable, not silently interpolated.
2. **Separate observation from inference from recommendation.** A finding states what was
   observed and its evidence; the implication is labelled as inference; the recommendation is
   labelled as ours. Clients challenge blended claims and win.
3. **Benchmarks are context, not verdicts.** Always state the source, the population, the
   as-of date, and why the peer set is comparable — see `references/benchmark-library.md` §0
   for the citation discipline and the four ways benchmark comparisons go wrong.
4. **House style binds.** Active voice, present tense, third person, sentences averaging ~18
   words (hard cap 28). Lint before delivery: `python scripts/ft_house_style.py <path>`.
   No marketing words: <!-- house-style: allow -->
   *leverage, unlock, empower, seamless, robust, synergy, best-in-class, world-class,
   transformative*.
5. **Tool output is a draft; the method governs.** Process Studio generates a TOM, a business case
   and pain points. So does this assessment. Where they differ, the assessment's evidence rules
   decide, and the tool output is a draft until reconciled. `references/tool-method-integration.md`
   §1 carries the precedence table.
6. **No generated figure is presented as a client actual.** Generated detail grounds design well
   and must never appear as the client's numbers, names, vendors or KPIs. Treat every generated
   figure as illustrative until a client source is cited. Check the `Current Value` column of any
   generated business case first — that is where real exports have broken this.

## Phase 0 — Ground the context

**Do not skip this.** A blueprint generated without a linked context produces generic agents — the
exact failure the two studios exist to prevent. The AS IS context must reach `Valid` status and be
exposed over MCP before Process Studio starts.

Two entry points, depending on what exists:

- **Client research from scratch** — run the accelerator's Step 1: one-shot research into official
  org chart, financial statements and analyst reprints, then extend `assets/ft-base-ontology.jsonld`.
  Validate with `python scripts/validate_ontology.py <schema>.jsonld` and import only on CLEAN.
  Full procedure in `references/accelerator.md` §1.
- **Client corpus already supplied** — build the schema directly, ingest, and curate. Procedure in
  `references/ica-studios.md` §2.

Verify the graph with three grounding questions before proceeding: personas and pain points; system
access; evidence. Recurring fixes go into the schema and get re-imported — never patch the graph.

**Check data residency before the first upload.** A shared IBM instance takes synthetic or public
data only. A team boundary is an access boundary, not a residency class. The table is in
`references/tool-method-integration.md` §4.

**Gate 0:** the context reaches `Valid`, residency is confirmed in writing, and the ontology
validator returns CLEAN. Ingesting client-confidential material into the wrong instance is not
recoverable by deleting it afterwards.

## Phase 1 — Frame and define the target operating model

Establish scope before analysis: which processes, which entities/regions, which systems, and what
"good" means for this client.

**Set scope in golden thread identifiers.** The practice's process spine is three threads —
**RTR** (Record-to-Report, 12 sections / 73 steps), **S2P** (Source-to-Pay, 16 / 59) and **OTC**
(Order-to-Cash, 11 / 88), 220 steps in total, held in `assets/golden-thread-taxonomy.csv`:

```
python scripts/ft_golden_thread.py scope 1.7 1.8 1.9 3.7 3.9
```

That returns the step list, the mapping to the assessment taxonomy, the mapping to the closed
**process area enum**, and a checkpoint flag for any section with no enum member — scope that falls
outside is assessed normally but cannot be drafted as a blueprint later, which is a flag to raise
now rather than at Phase 5. `references/golden-threads.md` carries the framework, and browse with
`ft_golden_thread.py list --thread RTR --section 1.8`.

Then draft the **target operating model** — the seven layers (value proposition, service delivery
model, process architecture, data & technology, organization & talent, governance & policy,
performance management) at Level 2 detail. Work from `references/target-operating-model.md`, which
carries the process taxonomy, the delivery-model options with their trade-offs, and the maturity
model (5 levels × 5 lenses) you will score in Phase 3.

Process Studio also emits a TOM, on a different role taxonomy. Reconcile rather than run both —
`references/tool-method-integration.md` §2.

Fill the capability scope sheet from `assets/capability-assessment-template.csv`.

**Gate 1:** the client confirms scope, the peer set, and the target operating model's design
principles before any diagnostic work. Design principles chosen late invalidate the roadmap.

## Phase 2 — Benchmark the current state

Collect the client's actual metrics into `assets/client-metrics-template.csv`, then:

```
python scripts/ft_analyze.py gap assets/client-metrics-template.csv --industry cross-industry
```

This joins each metric to `references/benchmark-library.md`, computes the quartile position,
the gap to median and to top quartile, and the **value at stake** (gap × the driver volume you
supply). Read §0 of the library before quoting anything: every row carries a source, an as-of
date, and a confidence flag — `verified` rows may be quoted with the citation shown, `directional`
rows may only be used to frame a range, and you must never present a directional row as a number
on a client page.

Industry cuts available: cross-industry, distribution/transportation, consumer products,
retail/wholesale, financial services/banking, services, public sector, manufacturing, healthcare,
energy/utilities. Where an industry row is absent, say so and use cross-industry explicitly labelled.

Product throughput claims from the studios are `directional` and never go on a client page as a
benchmark — see `references/tool-method-integration.md` §5.

## Phase 3 — Diagnose pain points across the five lenses

Run the diagnostic in `references/pain-point-taxonomy.md`: interview guide, the observation →
root cause → lens classification chain, and the severity × frequency × effort scoring. Every pain
point is assigned a **primary lens** (people / policy / process / data / technology) and a **root
cause**, not just a symptom. The lens distribution is itself a finding — a pain point set that is
90% "technology" almost always means the interviews stopped at the first answer.

Record a **pain dimension** on every row as well (`cycle_time`, `control_risk`, `data_quality`,
`decision_quality`, `scalability`) and the **golden thread `step`** the finding sits on, so
findings, benchmarks and modals all reconcile against one spine. The lens is where the cause sits;
the dimension is what it costs the business, and the blueprint contract requires at least three
distinct dimensions across the four pain points of any use case. Use personas from
`blueprint-accelerator/personas/inventory.yaml` — a persona not in the inventory raises a
`persona_flag` and never enters a deliverable unreviewed.

**Where the client has a large SOP corpus, run the Procedure Eater first.** It surfaces triggers,
actors, compliance considerations and candidate use cases at scale, and batch analysis is what
reveals **shared capability clusters** — the basis for one consolidated platform play instead of
many one-off automations. Its output is a Process Analysis Report, which is a diagnosis and not a
blueprint; review it before generating anything downstream. Procedure in
`references/ica-studios.md` §3.

Machine-surfaced findings enter the register as candidates, not as findings. They need a lens, a
root cause and evidence before they count — `references/tool-method-integration.md` §3.

Score the capability maturity from your filled assessment sheet:

```
python scripts/ft_analyze.py score assets/capability-assessment-template.csv
```

Output is the maturity heatmap (capability × lens), the weighted score per capability, and the
gap to the target maturity you set in Phase 1.

**Gate 2:** walk the pain point register and the maturity heatmap through the process owners
before it reaches the CFO. Owners who first see their process rated in the steering deck become
opponents of the roadmap.

## Phase 4 — Build the roadmap and business case

Convert findings into initiatives in `assets/initiative-backlog-template.csv` (each traced to
the pain points it resolves), then sequence:

```
python scripts/ft_analyze.py roadmap assets/initiative-backlog-template.csv
```

This produces the impact/effort matrix, the dependency-respecting wave plan (Wave 1 quick wins
0–6 mo · Wave 2 core 6–18 mo · Wave 3 structural 18–36 mo), the benefit ramp, and the
cumulative net-benefit curve. `references/roadmap-and-business-case.md` carries the benefit
taxonomy (hard / soft / cost avoidance / working capital — never sum them into one headline),
the value driver tree, the ramp conventions, and the risk and change-impact treatment.

Process Studio generates its own business case with NPV, IRR, payback and Monte Carlo sensitivity.
Use it for the modelling and apply this skill's benefit rules to the output — FTE displacement is
a hard saving only if the headcount actually leaves. The ten inputs it needs, and the reconciliation
rule, are in `references/tool-method-integration.md` §2.

**Gate 3:** benefits must be owned. Any benefit line without a named accountable executive and
a baseline metric is presented as an *opportunity*, not a *benefit*.

### Name the blueprints

Every initiative that introduces agents becomes a **use-case blueprint**. Name them here — an
assessment that ends without saying which blueprints to draft has stopped one step short. Add a
`golden_thread_steps` column to the backlog (semicolon-separated step ids, e.g. `3.7.3;3.9.4`),
then build the queue:

```
python scripts/ft_golden_thread.py queue <backlog.csv> --register <register.csv>
```

It orders by wave, resolves the process area from the thread steps, and reports which initiatives
have the four evidenced pain points the contract requires and which are blocked. Per draftable
initiative, carry forward: the `process_area`, the four pain points (highest severity × frequency,
then swapped for dimensional coverage until three dimensions appear), the personas, and the SOW
excerpt and interview notes. Drafting procedure in `references/accelerator.md` §3.

Where the thread step already carries a prototype modal, you are **converting, not drafting** —
`references/golden-threads.md` §3 lists the two structural deltas (modals carry 3 pain points, the
contract needs 4; modals carry one user benefit per role, the contract needs 3). Close both from
the register. Never pad to hit a count, and never propose an agent without a named human approver
and a pause trigger.

## Phase 5 — Render the deliverables

Build the Excel model first — it is the evidence base the deck points to:

```
python scripts/ft_workbook.py --out FT_Assessment_Model.xlsx
```

Ten sheets: Executive Summary · Benchmark Gaps · Value at Stake · Maturity Heatmap · Pain Point
Register · Initiative Backlog · Roadmap (Gantt) · Business Case · Assumptions · Sources —
with native Excel charts (radar, bar-gap, waterfall-style benefit bridge, stacked wave plan) so
the client can re-cut the numbers without you.

Then the deck. Storyline patterns, the page-by-page skeleton, chart selection rules, and the
diagram conventions are in `references/deliverable-standards.md`. For rendering:
- **Deck:** use the `ibm-branded-pptx` skill for IBM-branded decks (or `pptx` for neutral). Pass
  it the storyline from `deliverable-standards.md` §2, not raw findings. For the accelerator's own
  10-slide pitch deck, the slot-by-slot spec already exists at
  `H:\My Drive\AA\blueprint-accelerator\slide-spec.md` — use it rather than rebuilding.
- **Process/swimlane diagrams:** use the `swimlane-diagram` skill for hand-off maps. Process Studio
  emits BPMN 2.0 XML and Mermaid directly where a generated diagram is acceptable.
- **Chart styling:** follow the `dataviz` skill before writing any chart code.
- **Excel beyond the model:** the `xlsx` skill.

Process Studio emits ten artifact types, including the Portfolio Dashboard and the implementation
spec that hands off to a coding agent. **JSON is the source of truth** — edit the JSON and
re-render, because hand-edited HTML is overwritten. The list and the export discipline are in
`references/ica-studios.md` §4.

**Gate 4:** before the deck ships, run the completeness check in `deliverable-standards.md` §5
— every page traced to evidence, every benchmark cited, every `[SENIOR REVIEW]` marker resolved —
and lint the house style:

```
python scripts/ft_house_style.py <deck-text-or-directory>
```

Insert `[SENIOR REVIEW]` where the analysis lacks content; never invent a finding to fill a page.
Nothing SOX-relevant reaches a client without senior consultant sign-off.

## The autonomy model

Every agent step carries a zone. This governs the design, not the presentation.

| Zone | Meaning | Treatment |
|---|---|---|
| **GREEN** | deterministic, rule-based, ~99.9% | runs unattended |
| **AMBER** | AI judgement, ~90–95% | named reviewer, validation scope, decision authority, review SLA, override rules |
| **RED** | stays human | not automated |

**All AI steps start AMBER.** Promotion to GREEN requires eval baselines to mature (97%+ over
several cycles) and is a governance decision. GREEN means *deterministic*, not *good*.

**RED is a live zone, not a formality.** Any step where an unattended action would create an
unauthorised financial commitment, bypass segregation of duties or cross an approval threshold is
RED. A zone map showing RED = 0 on a process that contains a threshold is wrong.

**Segregation of duties survives automation.** Where a maker-checker separation exists today,
automating both sides with one actor collapses the control. Document the assessment; do not assume
the tooling handles it.

## Readiness — what may face a client

| Surface | Status | Client-facing? |
|---|---|---|
| This assessment method | stable | yes |
| Process Studio | generally available | yes, within residency rules |
| Context Studio | early internal alpha, IBM users only | no — testing and demos |
| Digital Twin / Simulate, BYOS | alpha, opt-in | no |

Do not describe the whole chain as production-ready. Context Studio has no authoring API — schema,
context, upload, ingest and expose are UI only, so no step of Phase 0 can be scripted end to end.

## When only part of this is asked for

Each phase stands alone. "Benchmark us against the industry" is Phase 2 only; "build the
roadmap from these findings" is Phase 4 only; "help me drive Process Studio" is the tool mechanics
in `references/ica-studios.md` without the surrounding method. Run the phase asked for, and name
the upstream inputs you are assuming rather than silently inventing them.

For an RFP or proposal built on this assessment, use the `rfp-response` skill (09) — it consumes
the Phase 2 benchmarks and the Phase 4 roadmap directly. For AR/O2C-specific depth use
`ar-diagnostic` (06); for the contract and TA that follow, `contract-review` (07). For SOP input
assets, `storylinea` generates per-process SOPs and baselines. For what the studios are among the
wider ICA surfaces, `ica-overview`.

## References

**Method**
- `references/house-style-and-blueprint-contract.md` — **read first.** The three meanings of
  blueprint, the enforced contract and counts, closed enums, house voice rules, checkpoint flags.
- `references/target-operating-model.md` — the seven TOM layers, APQC-aligned taxonomy, delivery
  model options, the 5×5 maturity model, design principles.
- `references/benchmark-library.md` — cited benchmark tables with industry cuts, citation
  discipline, refresh procedure.
- `references/pain-point-taxonomy.md` — five-lens classification, interview guide, root-cause
  patterns, scoring.
- `references/roadmap-and-business-case.md` — wave planning, benefit taxonomy and ramps, value
  driver tree, risk/change treatment.
- `references/deliverable-standards.md` — deck storyline, chart and diagram selection, Excel
  model spec, quality checklist.
- `references/golden-threads.md` — the RTR / S2P / OTC spine (220 steps), the modal schema and its
  deltas from the contract, the three persona sets, the six-phase agentic app method.

**Tools and integration**
- `references/tool-method-integration.md` — **read before generating anything.** Artifact
  precedence, the duplicated TOM and business case, machine-surfaced findings, data residency,
  product claims.
- `references/ica-studios.md` — Process Studio and Context Studio mechanics: the four-stage loop,
  ingestion limits, the Procedure Eater, the EAEF library, export discipline.
- `references/accelerator.md` — the four-step Blueprint Accelerator, its gates and metric.
- `references/eaef-phases-2-6.md` — Phases 2–6 of the EAEF blueprint and the six export checks.
- `references/process-studio-lab.md` — hands-on walkthrough, verbatim prompts, business case inputs.
- `references/context-studio-loop.md` — schema building, ingestion limits, MCP exposure.
- `references/build-kit.md`, `references/step1-one-shot-prompts.md`, `references/proposal.md`,
  `references/video-script.md` — accelerator working material.

**Assets and scripts**
- `assets/golden-thread-taxonomy.csv` — every step with section, thread, process area and
  assessment mapping. Queried by `scripts/ft_golden_thread.py` (`list` / `scope` / `queue`).
- `assets/process-flows.md` — ready-to-render P2P / O2C / R2R hand-off maps, layer diagram,
  current→target shift table and roadmap Gantt.
- `assets/ft-base-ontology.jsonld`, `assets/client.example.json` — accelerator schema base and
  harvest config, used by `scripts/validate_ontology.py` and `scripts/harvest.py`.
- `assets/*.csv` — the five input templates (benchmarks, client metrics, capability assessment,
  pain point register, initiative backlog), pre-filled with a worked example so every script runs
  out of the box. Replace the example rows with client data; keep the column headers.
