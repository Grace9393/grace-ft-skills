# The EAEF Layer 2 blueprint — Phases 2 to 6

`SKILL.md` describes the seven canonical sections. Those are **Phase 1**. A real export
runs to six phases and ~24 numbered subsections.

Structure below is taken from a real Process Studio export — Nestlé Canada CA10 Returns
and Refusals, 14 atomic steps, 9 agents, 12 MCP tools — cross-read against the Process
Studio User Guide v1.5. Where the two differ, the User Guide wins and the difference is
noted.

Source rank: 1 = User Guide / architecture deck · 2 = playbook / guided lab · 3 = the real
export.

---

## Phase 1 — Cognitive Deconstruction

The seven canonical sections, plus two the export carries that the User Guide's list does
not name:

| § | Section | Note |
|---|---|---|
| 1.1 | Atomic Thinking Step Register | canonical |
| 1.2 | Business Ontology | **not in the User Guide's seven** — core entities and their relationships |
| 1.3 | Autonomy Zone Map | **not in the User Guide's seven**; the guided lab lists it as a key output. See `SKILL.md` § "A disagreement to carry" |
| 1.4 | Human-in-the-Loop Specification | canonical |
| 1.5 | Data Products Definition | canonical |
| 1.6 | Integration with Systems of Record | canonical |
| 1.7 | MCP Tool Register | canonical |
| 1.8 | Agent Definition Register | canonical |

---

## Phase 2 — Context & Memory Engineering

What the agents are given, what they remember, and what is provable afterwards.

| § | Subsection | Contains |
|---|---|---|
| 2.1 | Context Payload Specifications | what each agent receives per invocation — fields, sources, size envelope |
| 2.2 | Memory Architecture Configuration | semantic memory (the client's reference data, hierarchies, canonical lists), episodic state across turns, what persists between runs |
| 2.3 | Audit Trace Architecture Specification | what is recorded per decision so a control can be evidenced later — retention, granularity, who can read it |

**Why it exists:** an agent that reasons correctly but cannot show its working fails an
audit. 2.3 is where a SOX-relevant process earns the right to be automated at all.

---

## Phase 3 — Agentic App Engineering

The build specification. The largest phase.

| § | Subsection | Contains |
|---|---|---|
| 3.1 | Agent Roster | one row per agent — the register from 1.8, resolved to deployables |
| 3.2 | Model Selection | model per agent or per role, version-pinned. Pinning matters: an unpinned model is an unannounced change to a control |
| 3.3 | Skills Library | the reusable skills the agents draw on |
| 3.4 | MCP Tool Engineering Plan | build plan per tool from 1.7 — auth, schema, error surface, owner |
| 3.5 | Orchestration Topology | single-agent · supervisor · sequential; who delegates to whom |
| 3.6 | Guardrail Configuration | hard limits — thresholds that must not be crossed, zones that must not be promoted, injection defences |
| 3.7 | Error Handling & Fallback Design | runbooks per failure mode (system-of-record outage, model provider outage, upstream schema change) |
| 3.8 | Observability Requirements | what is emitted, where it lands, what alerts |

**The load-bearing one is 3.6.** A threshold enforced only in a prompt is not enforced.
The real export puts the ≥50K CAD approval gate behind a hard-coded circuit breaker
*and* an adversarial eval — belt and braces, because the prompt alone is the failure mode.

---

## Phase 4 — Hardening & Verification

Evals. Nothing is promoted out of AMBER without this phase producing numbers.

| § | Subsection | Contains |
|---|---|---|
| 4.1 | Functional Evals | does it produce the right output on known cases |
| 4.2 | Behavioural Evals | does it behave correctly at the edges — refusals, escalations, zone boundaries |
| 4.3 | Adversarial Evals | prompt injection, threshold bypass, forged inputs. **Each guardrail in 3.6 needs a matching adversarial case** |
| 4.4 | Domain Evals | client-specific rules a generic suite would never test |
| 4.5 | Human-in-the-Loop Validation | is the reviewer interface usable, and do reviewers actually catch injected errors |
| 4.6 | Observability Validation | do the traces from 2.3 and 3.8 actually reconstruct a decision |

**4.5 is the one teams skip and regret.** Once agent accuracy exceeds ~95%, reviewers
drift into rubber-stamping. The counter is canary cases: known-wrong outputs injected into
the review queue, with remedial training for reviewers who approve them.

---

## Phase 5 — Agentic Activation

Going live. Organisational, not technical.

| § | Subsection | Contains |
|---|---|---|
| 5.1 | Change Management & User Enablement | role transitions, certification, the reskilling path from processor to reviewer |
| 5.2 | Cognitive Telemetry Activation | turning on the measurement before turning on the autonomy |
| 5.3 | Operational Handover | runbook acknowledgements signed by named L1/L2/L3 responders; escalation chain live |

Typical wave structure from the real export: **shadow mode** (humans decide, agents run in
parallel, measure ≥90% agreement) → **Green-zone autonomous** while AMBER stays reviewed →
**full activation**. Each wave has an exit gate with a named decision-maker.

---

## Phase 6 — Agentic Operations & Evolution

| § | Subsection | Contains |
|---|---|---|
| 6.1 | Continuous Agent Evaluation | the eval suites from Phase 4, run on a cadence; drift detection against a locked baseline |
| 6.2 | Outcome Measurement | the KPI table — cognitive health and business impact, baseline vs current vs target, with a reporting cadence per row |

### 6.2 and the trap in it

The KPI table has a **Pre-Transformation Baseline**, a **Current Value** and a **Target**
column.

> ⚠️ **`Current Value` must be empty until something has actually run.** The real export
> ships this column fully populated — decision stability 96.0%, STP 94%, cost CAD $8.60 —
> for a pilot that had not started, with every reviewer in the accompanying TOM still
> marked `Pending`. It reads as measured and is not.

This breaks the Golden Rule (see `SKILL.md` Gate 5). When reviewing any generated
blueprint, check this column first: a number there is a claim that something was measured.

**Cognitive health KPIs:** decision stability · hallucination rate · escalation accuracy ·
autonomy compliance · trace coverage · eval coverage · agent regression · model drift.

**Business impact KPIs:** cycle time · straight-through processing rate · quality (error
and duplicate rates) · compliance (threshold breaches, missing evidence) · financial (FTE
displacement, cost per transaction, LLM cost per transaction) · value (asset reusability,
deploy speed) · experience (requestor and reviewer satisfaction).

---

## Reading a generated blueprint — the six checks

Run these on any export before anyone quotes it:

1. **Zone arithmetic.** Counts sum to the step count; percentages sum to 100%. A threshold
   split is two rows, not an averaged one.
2. **No AI step in GREEN.** GREEN means deterministic.
3. **RED is not zero** on any process containing an approval threshold or a
   stop-processing condition.
4. **Header counts equal register counts** — agents, steps, tools.
5. **`Current Value` is empty** unless something ran, and the something is named.
6. **Every figure quoted in the TOM exists in the blueprint** at the cited section. ROI and
   payback live in the **business case**, a separate artifact — a TOM citing "§6.2 ROI" is
   citing a section that does not carry it.

All six failed at least once in the real export used as the source for this file. They are
not hypothetical.
