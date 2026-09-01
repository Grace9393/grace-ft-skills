# Changes — 2026-08-15

Brought `10-ica-process-studio` up to the official documentation. The skill was distilled
from Box lab decks before IBM published anything; four official sources have since arrived.

Executed from `H:\My Drive\AA\ICA-Studios-Consolidated\PROMPT-F-backfill-skill.md`.

## Sources, by authority rank

| Rank | Source |
|---|---|
| 1 | `ICA-Studios-Consolidated\official-sources\EAActivationHubKnowledgeCapture.md` §10 — **Process Studio User Guide v1.5** |
| 1 | `…\official-sources\Process-Studio-ARCHITECTURE.pptx` |
| 2 | `…\official-sources\Client-Context-…-Master-Playbook.docx` v3.0 |
| 2 | `…\official-sources\Process Studio guided lab.zip` — 26 slides |
| 3 | [CLIENT] CA10 EAEF export (Box) — evidence of what the product does, including its defects |

## Corrections

| # | Was | Now | Source rank |
|---|---|---|---|
| 1 | "Procedurator" discovery engine | **Procedure Eater**, and not a separate tool — skills inside Process Studio, run from the Analyze tab; only corpus-wide skills appear there | 1 |
| 2 | four-stage loop only | added **Ground → Assess → Re-imagine → Simulate** (User Guide) and **AS IS → PS → TO BE** (playbook), alongside the existing loop | 1, 2 |
| 3 | "Choose the model — Azure GPT-5 or Opus from GCP" | model-agnostic: Anthropic · Bedrock · Azure · Vertex · LiteLLM, with the precedence chain | 1 |
| 4 | ingestion cap stated once, conflated | **two separate limits**, labelled by product: PS 10 MB/file · 500 MB · 2000 files · parallelism 1–32; CS 30 files / 100 MB | 1 |
| 5 | seven sections, one of them the Autonomy Zone Map | the User Guide's seven, **with the Autonomy Zone Map disagreement recorded, not resolved** | 1 vs 2 |
| 6 | — | **JSON is the source of truth**; hand-edited HTML is overwritten on re-render | 1 |
| 7 | artifacts implied as blueprint + BPMN + business case | **ten artifact types**, including the Portfolio Dashboard and `IMPLEMENTATION_SPEC.md` | 1 |
| 8 | status implied Alpha | **generally available**; Simulate and BYOS are the Alpha parts | 1 |
| 9 | — | **data residency, three tiers**, plus the note that a team boundary is not a residency class | 1 |

## Additions

| Where | What |
|---|---|
| `references/eaef-phases-2-6.md` **(new, 130 lines)** | Phases 2–6 with their ~16 subsections, taken from the real export's structure and cross-read against the User Guide; plus **the six checks** to run on any generated blueprint |
| `SKILL.md` § autonomy model | **RED is a live zone** — the lab's worked blueprint is 6 GREEN / 5 AMBER / 1 RED; a zone map showing RED = 0 on a process with an approval threshold is wrong |
| `SKILL.md` § blueprint | the Agent Definition Register is a **table**, with its seven columns named |
| `SKILL.md` § step 2 | the EAEF repository is populated — four observed folders, and the Finance blueprint that already exists (APQC PCF 9.5) |
| `SKILL.md` § step 3 | Procedure Eater mechanics; ingestion phase toggles; batch analysis surfaces **shared capability clusters** |
| `SKILL.md` § business case | the business case is a **separate artifact**; a TOM citing "Blueprint §6.2 ROI" cites a section that does not carry it |
| `SKILL.md` § gates | **Gate 5 — no generated figure is presented as a client actual** (the Golden Rule), cross-referenced to the export that broke it |
| `SKILL.md` frontmatter | trigger terms added: Procedure Eater, Ground/Assess/Re-imagine/Simulate, Portfolio Dashboard, implementation spec, target operating model. **No existing trigger removed** |

## Unchanged, deliberately

The four existing gates · the autonomy model's substance (it was right; the real export
confirms it) · the four verbatim prompts (confirmed against both the playbook and the lab) ·
the ten business-case inputs · the `directional`-only treatment of the Alpha claims ·
frontmatter `name`.

## Disagreements recorded rather than resolved

**The seven canonical sections.** The User Guide's seven exclude the Autonomy Zone Map; the
guided lab lists it as a key output; the real export carries it as §1.3. Both positions are
written with their sources. A skill that silently resolves a contradiction between two IBM
sources is worse than one that surfaces it.

## Distribution — there are FOUR copies, not three

Written to the source of record, then copied with **merge semantics only** — no destination
directory was cleared, per `CLAUDE.md` §1 on Google Drive path poisoning.

| Copy | Path | Loaded when |
|---|---|---|
| source | `H:\My Drive\AA\bob-skills\10-ica-process-studio\` | — |
| Bob, workspace | `H:\My Drive\AA\.bob\skills\ica-process-studio\` | Bob opens a folder inside `H:\My Drive\AA` |
| **Bob, user-level** | `C:\Users\GRACEPAN\.bob\skills\ica-process-studio\` | **Bob opens any other folder — this is the one that matters for the CA10 benchmark** |
| Claude, user-level | `C:\Users\GRACEPAN\.claude\skills\ica-process-studio\` | any Claude session |

> ⚠️ **The user-level Bob path was missed on the first sync and was still stale.** It has no
> `eaef-phases-2-6.md` and an older `SKILL.md`. Because the CA10 benchmark opens a folder
> under `C:\Users\GRACEPAN\Box\…`, **that stale copy is the one Bob would have loaded** —
> which would have silently defeated the point of updating the skill at all.
>
> Caught and synced 2026-08-15 before the first benchmark run. Verified four-way
> byte-identical across all four files. **Sync all four every time.**

---

# Pass 2 — lab reconciliation, same day

`references/process-studio-lab.md` rewritten against the official guided lab
(`official-sources\Process Studio guided lab.zip`, 26 slides, IBM Consulting FutureNow),
which supersedes the earlier Box deck. Differences marked **[changed]** / **[new]** in the
file itself.

## The one that changes SKILL.md

**The seven-section disagreement is now settled, and neither earlier reading was right.**

The lab's rendered blueprint navigation pane lists **eight** Phase 1 sections, and it
matches the [CLIENT] CA10 export section for section. The User Guide's list of seven **omits
Business Ontology and the Autonomy Zone Map**, and includes *Skills Library*, which the
product renders in **Phase 3** (§3.3).

Two independent exports agree. `SKILL.md` § "The User Guide's seven is an incomplete
summary" now carries the eight-row table with a column marking what the User Guide drops.
The previous "record, do not resolve" framing has been replaced — this is resolvable, and
the evidence resolves it.

## Other changes to the lab file

| | |
|---|---|
| **Access** | team captains sign in at a **standalone AWS-hosted URL** (`https://ic-<id>.ecs.us-east-1.on.aws/`), not `servicesessentials` and not a regional `*.ica.ibm.com`. Relevant to establishing residency class |
| **Steps** | the official deck numbers `00 · 01 · 02 · 03 · 04 · 06` — **05 is skipped**. Six steps, not seven |
| **Project form** | contexts are **multi-select**; system default model shown as `aws · claude-opus-4-6-v1`; the four blueprint domain folders; the seven auto-generate artifact toggles; collaborator Read/Write |
| **Context detail** | `[CLIENT]-Finance` holds four named files, all `ready` |
| **A real blueprint's tiles** | 12 atomic steps · 50% DET / 50% AI · 10 agents · 10 data products · 14 MCP tools · **6 Green / 5 Amber / 1 Red** — counts sum, RED populated |
| **Agent register semantics** | the product's own explanation of each column, plus what RED is for: a Payment Security Sentinel Agent that stops processing on credential exposure, token misuse, unauthorized requests or vendor banking data leakage |
| **Business case has two gates** | a mandatory **KPI review gate** and a **baseline data collection mode** choice — and option 4, *"Use EAEF defaults for everything"*, is the mechanism by which an unsourced figure enters a business case. Flagged in place |
| **Business case output** | **three** files, not two; the dashboard's eleven tabs; the lab run's real figures (NPV €1.9M, payback 31 mo, IRR 73.3%, 4.4 FTE, €209K/yr, €798K year-0, 99.4% P(NPV>0), 10,000 Monte Carlo runs) |
| **Demo failure points** | now four — the two business-case gates added, because the workflow pauses and waits at exactly the moment an audience expects a number |

## Still open

- The skill does not carry the **Process Studio REST surface**. That lives in
  `ICA-Studios-Consolidated\Studio-Automation\` and is an internal contract, not something a
  conduct guide should teach as stable.
- `references/context-studio-loop.md` has not been re-read against the newer Context Studio
  guided lab, which was captured but not opened in this pass.
