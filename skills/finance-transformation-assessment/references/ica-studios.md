# ICA Studios — Process Studio and Context Studio mechanics

**Process Studio designs the agents. Context Studio tells them what they know.** They run as a
closed loop: the engagement that discovers what to automate leaves behind the schema, knowledge
graph and blueprints that make the next engagement faster.

Absorbed from the former `ica-process-studio` and `ica-context-studio` skills. Where this file and
the official Process Studio User Guide disagree, the User Guide wins. Precedence against this
skill's own method is in `tool-method-integration.md` §1.

**Status.** Process Studio is generally available. Context Studio is early internal alpha, IBM
users only, suitable for testing and demos rather than client-facing production. Digital Twin and
BYOS are alpha and opt-in.

---

## 1. The four-stage loop

Two other framings are also official: **Ground → Assess → Re-imagine → Simulate** are the four
steps inside Process Studio; **AS IS context → Process Studio → TO BE context** is the
engagement-level shape and the most practical of the three.

| Stage | Studio | What happens |
|---|---|---|
| 1 Foundation | Context Studio | define a schema, ingest the client's materials, populate the knowledge graph, verify with the built-in assistant |
| 2 Discovery | Process Studio · **Procedure Eater** | feed it the client's existing SOPs; it surfaces triggers, actors, compliance considerations and AI use cases at scale |
| 3 Reimagination | Process Studio | cognitive decomposition splits agentic from non-agentic. Out comes the agent register, target operating model, business case and BPMN |
| 4 Implementation | Context Studio → **Bob** | expose the context as an MCP server, drop the Context ID into Bob, and the coding agent generates frontend, backend and data models |

**Do not skip stage 1.** A blueprint generated without a linked context produces generic agents —
the exact failure the two studios exist to prevent. The AS IS context must reach `Valid` status and
be exposed over MCP before Process Studio starts.

---

## 2. Context Studio — grounding

A central knowledge layer that ingests from GitHub, JIRA, SharePoint, Confluence and manual
uploads; extracts entities and metadata with [Docling](https://github.com/docling-project/docling);
builds a queryable knowledge graph; retrieves by graph query, vector search or hybrid, tailored to
an agent persona; and exposes itself as an **MCP server** any MCP-capable agent can pull from.

Deployment runs on IBM Cloud, multi-cloud or on-premises.

**Context Studio has no authoring API.** Schema, context, upload, ingest and expose are UI only, so
no part of this stage scripts end to end.

### Roles

- **Knowledge Engineer** — designs the graph schema, chooses sources, curates entity and
  relationship types.
- **Architect / Developer / PM** — consume the context and contribute domain knowledge.
- **Agent** — programmatic consumer over MCP.

### Workflow

1. **Define the project** — name, scope, expected agent personas.
2. **Connect sources** — wire up repositories, projects, spaces and sites. Each source registers
   its credentials inside Context Studio.
3. **Run ingestion** — Docling extracts text, tables, code and entities; the graph builds or
   updates.
4. **Curate the graph** — review extracted entities, merge duplicates, add ontology relationships.
5. **Test retrieval** — ask the query interface a real question and check the answer.
6. **Expose over MCP** — copy the endpoint into the agent's MCP config.
7. **Iterate** — refine ingestion frequency, retrieval prompts and ontology.

### Quality rules

- Choose narrow, durable sources first: architecture decision records, glossaries, key spaces.
  Adding everything produces graph noise.
- Define personas explicitly so retrieval prompts adapt the response.
- Re-run ingestion after major source changes, or the graph goes stale.
- Watch for hallucinated entities after ingestion. Docling is good and not infallible, so keep a
  curation pass in the workflow.
- **Recurring fixes go into the schema, then re-import.** Never patch the graph directly.

### When to choose it

| Need | Use |
|---|---|
| Single project, files only, fast turnaround | ICA 2.0 Document Collections |
| Single project, structured and unstructured, multi-source | **Context Studio** |
| Cross-project shared rules or coding standards | MCP Rules Server |
| Vector RAG only, no entity model needed | watsonx Discovery or a vector database |

Ingestion cap: 30 files / 100 MB per batch. Process Studio's limits are different — see
`tool-method-integration.md` §4.

---

## 3. Process Studio — ingest and analyse

### Create the project

Set scope, industry and organisational context, and **link a Context Studio workspace**.
Optionally import from SAP Signavio or Celonis so the blueprint is grounded in observed reality.

**Models are pluggable** — Anthropic (native Claude), AWS Bedrock, Azure OpenAI / AI Foundry,
GCP Vertex AI, LiteLLM gateway. Precedence runs per-run choice > project model > personal default
> admin system default, with per-role overrides inside a run.

Tick the artifact types you want generated. **Include JSON-LD Ontologies** if the TO BE context
will be built from this project; nothing downstream imports a schema that was never generated.

### Select a blueprint

Start from the **EAEF library** (EA Engineering Framework), backed by APQC PCF, APQC industry
frameworks (Banking, Consumer Products, Telco, Corporate Operations), BIAN, eTOM, SCOR, IBM
industry operations models and IBV — or start blank. **Check the repository before generating
anything;** reusing a library blueprint is the point of the library.

Observed folders: `APQC - Banking` · `APQC - Corporate Functions` · `APQC - Telco` ·
`SCOR - Supply Chain`. Corporate Functions → Finance carries a worked blueprint, *Accounts Payable
Expense Reimbursements* (APQC PCF 9.5), with target outcomes of 65–80% touchless invoice
processing, 40–55% FTE reduction and a 3-day cycle-time reduction.

Reference: `https://pages.github.ibm.com/Consulting-DTT-AI-Integration-Services/ea-engineering-framework/`

Built-in IP for grounding: **CBM** (Component Business Model) for capability decomposition, the
**IBM AI Use Case Library** to seed and benchmark opportunities, and **IBV benchmark data** for the
business case. The agent returns an explicit Sources footer.

### Ingest

Limits — Process Studio's own: 10 MB per file · 500 MB total · 2,000 files per staged upload ·
parallelism 1–32, with 4 a safe default.

Optional ingestion phases, each an independent toggle: full document text on the wiki · incremental
runs · Vision, which describes embedded PDF and PPTX images · Synthesizer · Contradictions.
Dry-run first, then run.

### Run the Procedure Eater

**It is not a separate tool.** It ships inside Process Studio as a set of skills. Analyze tab → run
an analysis → pick a Procedure Eater skill. Only skills built to run over a whole corpus appear
there; conversational skills belong in chat.

Batch analysis is what surfaces **shared capability clusters** — the basis for one consolidated
platform play instead of many one-off automations.

The lab prompt sequence, verbatim:

| Prompt | Produces | Time |
|---|---|---|
| `Analyze this procedure` | **Process Analysis Report** (.md + .html), after four analysis phases | minutes |
| `Generate a process blueprint based on this analysis, keep it simple` | **EAEF blueprint** | ~15 min |
| `Create a BPMN diagram for this process` | **.bpmn** with swim lanes | minutes |
| `Build a business case for this process transformation` | **.pptx** + interactive report + .xlsx | minutes |

**The Process Analysis Report is not the blueprint.** It is the diagnosis: it reads the procedure,
captures the policy and operational reality behind it, and surfaces the AI use cases worth
pursuing. Review it before generating the blueprint, because a wrong diagnosis propagates into
every downstream artifact.

Its output enters this method as candidates, not findings — `tool-method-integration.md` §3.

### Rank with the Portfolio Dashboard

Re-rank surfaced use cases against client-specific weights. The presets — Quick Wins, Max ROI,
Lowest Risk, High FTE Impact — are a starting point to argue from, not an answer. State which
preset produced any ranking shown on a page, and why.

---

## 4. Export and artifacts

**JSON is the source of truth.** Edit the JSON and re-render. **Hand-edited HTML is overwritten.**
Blueprints support inline editing and per-section feedback, and publish to a GitHub location under
your prefix.

Ten artifact types, not two:

| Artifact | Format |
|---|---|
| Blueprint document | .docx · interactive HTML · Markdown · **JSON** |
| Executive deck | .pptx |
| Process diagrams | BPMN 2.0 XML · Mermaid |
| Agent Evaluation Plan | Markdown |
| Evaluation suites | Markdown · CSV — functional, behavioural, adversarial |
| Risk Register | structured document |
| **Portfolio Dashboard** | interactive HTML — scores use cases go / conditional / no-go, clusters capabilities, recommends a path |
| **Target Operating Model** | interactive HTML / document |
| **Implementation spec** | `IMPLEMENTATION_SPEC.md` |
| Audit trace | JSON |

The **implementation spec** is the coding-agent handoff, written to be the first instruction to
Claude Code, Cursor, IBM Bob or Codex. It carries build objective, hard constraints, business
rules, scope boundaries, per-screen UX contracts, tech stack, agent and tool I/O contracts,
external systems and HITL touchpoints. It separates what the coding agent no longer has to invent —
with inferred numbers flagged and confidence noted — from what is deliberately deferred to it.

---

## 5. The EAEF blueprint — eight sections, not seven

The User Guide names seven. The product renders eight. Settled 2026-08-15 against the guided lab's
rendered navigation, which matches the Nestlé CA10 export section for section.

| # | Section | In the User Guide's seven? |
|---|---|---|
| 1.1 | Atomic Thinking Step Register — every step tagged `DET` or `AI`, with a reliability target | ✅ |
| 1.2 | **Business Ontology** | ❌ omitted |
| 1.3 | **Autonomy Zone Map** | ❌ omitted |
| 1.4 | Human-in-the-Loop Specification — per checkpoint: reviewer role, validation scope, decision authority, review SLA, override rules | ✅ |
| 1.5 | Data Products Definition — schemas, freshness, ownership | ✅ |
| 1.6 | Integration with Systems of Record | ✅ |
| 1.7 | MCP Tool Register — the integrations needed, classified, with auth | ✅ |
| 1.8 | Agent Definition Register — a table: Agent (ID) · Goal · Owned Steps · Orchestration Pattern · Tools Required · Autonomy Zone · HITL Touchpoints | ✅ |
| — | *Skills Library* — listed in the seven, but rendered in Phase 3 (§3.3) | borrowed |

Two independent exports agree on all eight and their order. Treat the User Guide's list as a
summary that drops two sections and borrows one. **Do not tell a client the blueprint has seven
sections.**

That is Phase 1 of six. Phases 2–6 — context and memory engineering, agentic app engineering,
hardening and verification, activation, operations — are in `eaef-phases-2-6.md`, with the six
checks to run on any generated export before quoting it.

`golden-threads.md` §5 carries a worked EAEF blueprint
(`general-accounting-reporting-FPA-APP.md`, APQC PCF 9.3). Read it before generating a first one.

---

## 6. Simulate — optional, alpha

Digital Twin compiles the blueprint into an executable spec, builds agents bound to **mock** tools,
and runs scenarios so KPIs can be observed before code is written. Opt-in, and not enabled in every
deployment. **BYOS** (Bring Your Own Skill) is likewise alpha.

Neither is client-facing.

---

## 7. Gates

1. **Review the Process Analysis Report before generating the blueprint.** It is the diagnosis;
   everything downstream inherits its errors.
2. **Check the blueprint repository before generating from blank.**
3. **No agent without a human approver.** Every AMBER step names the reviewer, the trigger and the
   SLA. An agent that posts to a ledger unattended is a finding, not a design.
4. **The generated business case is a draft.** Numbers the client did not supply are assumptions
   until confirmed.
5. **No generated figure is presented as a client actual.** Check the `Current Value` column of
   §6.2 first — that is where real exports have broken this.
6. **Confirm data residency before the first upload** — `tool-method-integration.md` §4.
