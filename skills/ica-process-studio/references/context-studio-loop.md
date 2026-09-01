# The Context Studio half of the loop

Process Studio designs the agents; Context Studio tells them what they know. This covers stages 1
and 4 — enough to run the loop end to end. For Context Studio as a product surface in its own
right, use the `ica-context-studio` skill.

Sources: `process_studio_context_studio.html` and `India_Hands_On_Lab_ContextStudio.pptx` in
`C:\Users\GRACEPAN\Box\#Grace\[INTERNAL]\Studio`.

---

## 1. Schema — a JSON-LD ontology

A schema is `@context` plus `@graph`, with **schema.org as the base vocabulary**. Three ways to
build one:

- **Blank** — define every node by hand in the canvas.
- **Import** — drag-drop a JSON-LD file (the Context Studio Schema Builder assistant generates one
  from a prompt like `Create a schema for corporate finance process`; Process Studio can also emit
  one). Tag it with domain and industry on import.
- **Infer** — upload sample data and let the system derive the schema.

The canvas has four object types in the left sidebar:

| Object | What it is |
|---|---|
| **Nodes** | Entities — contracts, vendors, invoices, evaluators |
| **Edges** | Relationships — vendor-bids-on-contract, evaluator-scores-bid |
| **Actions** | Behaviours and workflows to automate against the graph |
| **Constraints** | Data-consistency rules, each enabled or disabled before publish |

Click a node to edit its description, properties and relationships. Then **Publish**.

The local generator for this shape is the `jsonld-ontology-generator` skill; the accelerator's
base ontology is `blueprint-accelerator/assets/ft-base-ontology.jsonld`, validated by
`validate_ontology.py`. Import to Context Studio only on a clean validation.

## 2. Context — a published schema populated with one client's data

`New Context` → name and client name → search for and select your published schema.

**Sources & Data** accepts `.docx .doc .md .xlsx .txt .json .csv .pdf .pptx .xml .html .yaml .yml`
— **up to 30 files / 100 MB per batch**. Assign the published schema, pick an ingestion (augment)
pattern, upload. The system extracts entities and maps them into the graph; each node carries its
properties, source file and the relationship paths anchoring it to the rest.

Scale reference: a demo RFP-evaluation context (client "BrightShelf") held **100+ nodes and 60+
relationship types** spanning bids, vendors, GFSI certificates, evaluation reports, evaluator
scores, contract compliance and gate assessments.

## 3. Verify before exposing — "talk to the context"

A built-in assistant queries the populated graph in natural language. Ask *"What is this context
about?"* and *"Which vendors are referenced in the GFSI certificates?"* to confirm the system
understood your source documents.

**Do this every time.** A context that ingested cleanly but mapped wrongly produces confidently
wrong agents downstream, and the error surfaces at demo time rather than at build time.

## 4. Expose as MCP

`Overview` → scroll → **Expose as MCP** → `Next` → copy the **server URL**, **bearer token** and
**Context ID** (`ctx_ab9924a2ef11` form). Drop-in configuration is generated for Bob, ICA Agent
Studio, Claude Desktop, VS Code, Cursor, Windsurf and Codex.

Generic MCP client configuration:

```json
{
  "mcp.servers": [
    {
      "name": "Context Studio – RFP-Evaluation-Context",
      "url": "https://servicesessentials.ibm.com/mcp-gateway/servers/{id}/mcp",
      "headers": {
        "Authorization": "Bearer eyJhbGciOiJI...",
        "Context-ID": "ctx_ab9924a2ef11"
      },
      "enabled": true
    }
  ]
}
```

**Verify with the MCP Inspector before wiring into a production agent:**

```bash
npx @modelcontextprotocol/inspector
```

Transport `Streamable HTTP`, connection `Direct`, auth via custom headers
(`Authorization: Bearer …`), URL from Context Studio. List the tools —
`context-broker-get-contexts` and others — and call them with your Context ID to confirm the
server returns the right graph data.

**Never paste a bearer token into a document, a deck or a chat that leaves your machine.** The lab
material contains live-looking URLs and a Context ID; treat every one as a credential.

## 5. Hand off to Bob

Drop the Context ID into IBM Bob. The coding agent generates a working frontend, backend and data
models against the context — the "hours instead of months" claim rests on this step, not on the
blueprint generation.

---

## The loop, in one line

**Schema → Context → verify → MCP → Bob builds the app; Process Studio's blueprint says what to
build.** Neither half is useful alone: a blueprint without a context yields generic agents, and a
context without a blueprint has nothing to serve.
