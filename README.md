# Grace FT Skills — IBM Process Studio BYOS Pack

18 Finance Transformation and IBM Consulting skills for IBM Process Studio (ICA).

## Skills included

| Skill | Description |
|-------|-------------|
| exception-resolution-agent | Finance Exception Resolution workflow |
| fpna-advisor-hank | FP&A digital advisor — P&L cuts, variance analysis, what-if |
| boblueprint-accelerator | Finance Transformation Blueprint Accelerator |
| fte-visibility | FTE Effort & Cost-Center Visibility workflow |
| ask-finance-grounded | Grounded finance Q&A from client data |
| ar-diagnostic | Accounts Receivable diagnostic — DSO/CEI/aging |
| contract-review | Contract/TA review — 8-check sweep + CUAD risk checklist |
| finance-transformation-assessment | End-to-end Finance Transformation assessment |
| rfp-response | Build a winning RFP/RFI/tender response |
| ica-process-studio | IBM Consulting Advantage Process Studio — SOP to agentic blueprint |
| opportunity-radar | Competition, hackathon and partner-community radar |
| browser-recon | Explore a live web app and document what is actually there |
| corpus-prep-for-ingestion | Make a document corpus ingestible under file-size caps |
| deep-extract | Recursively extract every scrap of content from a document |
| extract | One entry point for getting content out of documents |
| sop-rules-register | Extract business rules register from SOP corpus |
| ibm-carbon-report | IBM Carbon house-style interactive HTML deliverable |
| exec-diagnostic-onepager | Convert long analysis into a one-page executive diagnostic |

## How to connect in Process Studio

1. Go to **Settings ? Skills ? Bring Your Own Skill (BYOS)**
2. Repository URL: `https://github.com/Grace9393/grace-ft-skills`
3. Branch: `main`
4. Folder: `/` (root — each subfolder is a skill)
5. Enter your GitHub PAT and click **Connect**

## Author-side tooling

`tooling/<skill>/` holds QA scripts that need a browser (playwright) or an HTML
parser (bs4). They sit outside `skills/` on purpose: Process Studio scans every
file in a connected skill and disables the skill if any file imports a package
its runtime lacks. These are run locally by the author, never by the platform.
