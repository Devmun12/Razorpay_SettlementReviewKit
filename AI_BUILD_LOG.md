# AI Build Log: Settlement Review Kit

**Razorpay x ISB AI PM Build Challenge · Track 1: "Razorpay in Your Pocket"** · Devesh, ISB PGP 2026–27

This log covers how AI was used to research, build, test and record the Settlement Review Kit. It contains no API keys, credentials, private data or proprietary Razorpay information; all merchant data in the prototype is synthetic.

---

## 1. AI tools and models used

| Tool | Model / version | Used for |
| --- | --- | --- |
| Claude (Anthropic), agent session with file, shell and document tools | Claude Opus | Research synthesis, product framing, prototype code, test scripts, document drafts, demo recording script |
| A second Claude agent, briefed as a senior Razorpay AI PM | Claude Opus | Independent evaluation of each revision, with no access to the builder's reasoning |
| Claude Docs | – | Drafting and editing the product note |
| Playwright + Chromium | 1.x | Automated regression tests (desktop, 390 px and 360 px phone widths) and the scripted screen recording of the demo video |
| pdf.js (Mozilla) | 3.11.174, bundled in `vendor/` | Real, on-device PDF text extraction in the prototype |
| reportlab, pypdf, pdftotext, ffmpeg | – | Generating the synthetic sample PDFs, checking document page counts and wording, encoding the video |

No AI video or image generator was used. The demo video is a real screen recording of the working prototype, driven by a script.

## 2. Key prompts, workflows and agent setup

**Agent setup.** Two agents with separate roles:

1. **Builder:** researches, designs, builds and tests.
2. **Evaluator:** a separate agent that sees only the finished submission. It is briefed to judge "as a Razorpay AI PM would", including regulatory and risk-ops angles, and returns scored must-fix items.

The builder never grades its own work.

**Workflow (repeated each round):** design → build → automated test → independent review → fix → re-test. Four rounds in total.

**Representative prompts:**

- *Framing:* "Find where a Razorpay merchant loses the most time or money on a phone today. Rank ideas by merchant pain, how often it happens, and whether a working prototype can show it."
- *Build:* "Build a single-file mobile prototype using Razorpay's Blade design tokens. The merchant's task must end at a receipt. Razorpay's analysts make every decision. Show which parts are real and which are simulated."
- *Evaluation:* "You are a senior AI PM at Razorpay judging this submission cold. Think about the regulator, risk ops and the merchant. Score it, list must-fix items, and try to break the prototype."
- *Verification:* "Write Playwright tests for every acceptance condition: release is blocked until each requirement is accepted, progress survives a refresh, stale jobs can't change a reset case, there is no overflow at 360 px, and there are zero JS errors."

## 3. One AI output I rejected, and why

**The AI's first analyst console let one "Release" click mark every requirement as accepted.**

It looked efficient, but I rejected it for three reasons:

- **It turned release into a bulk action.** It blurred who decided what. In a settlement hold, the audit trail has to show a reviewer's decision for each requirement.
- **It undercut the product's central principle:** AI does the paperwork; Razorpay makes the decision.
- **A pending delivery or an open clarification could be released by accident.**

**What I changed it to:**

- Each requirement now has its own status (in review, accepted, clarification, pending), set by the analyst.
- The console has a "View source" row for each payment. It shows the source page, the checks that ran and what was *not* checked.
- **Release** stays disabled until every requirement is explicitly accepted.

Automated tests cover this. Release is disabled before acceptance, with a clarification open and with a pending item. It becomes enabled only after late proof arrives and is accepted.

**Other corrections:**

- I replaced copy that overclaimed ("exactly what Razorpay's review team receives") with precise wording.
- I replaced a scripted "AI reads your invoices" step with real in-browser PDF reading.
- I regenerated a sample page that made the ambiguous-match test too easy.

## 4. What AI did versus what I decided or built

| AI did | I decided |
| --- | --- |
| Drafted research summaries from public Razorpay docs and merchant complaints | Chose Track 1 and the problem: settlement holds that need evidence |
| Wrote the prototype code, tests and sample-file generator | Decided the merchant's task ends at a receipt, and Razorpay decides release |
| Proposed screen layouts and copy | Decided risk policy sets the screen. A confidential review never shows a document request, and signals are never explained. |
| Ran the regression suite and fixed failures | Decided what is real in the prototype and what is labelled simulated |
| Played the independent Razorpay evaluator | Chose which review findings to act on, and the primary metric |
| Scripted and recorded the demo video | Approved the storyline, captions and closing line |

## 5. Known limitations, risks and verification steps

**Limitations (stated in the prototype as well):**

- All data is synthetic.
- The hold service, the Shiprocket lookup, notifications and the analyst's decisions are simulated.
- PDF reading works on text-based PDFs. Scanned images would need OCR, which isn't included.
- Document authenticity checks (file-reuse search, edit forensics, GSTIN match) are designed but not performed in the prototype.
- Progress is saved in the browser on one device.

**Risks and how the design handles them:**

- **Forged or reused documents.** Nothing is auto-accepted. The analyst sees each source and accepts each requirement, and screenshots are labelled merchant-supplied.
- **Over-trust in AI matching.** Matching requires an exact order number and amount. Ambiguous pages must be confirmed by the merchant, and mismatches are flagged rather than hidden.
- **Privacy.** Invoices are read in the browser, and nothing is uploaded in the prototype. Shiprocket access is consent-scoped to the held payments.
- **Tipping off.** Unclassified and confidential reviews show only "we're reviewing your settlement" and a next-update date. Police holds follow the separate legal process.

**Verification steps run:**

- A Playwright regression suite on every build. It covers the main path, persistence across a refresh, release gating, late proof as a new version, stale-job protection after a reset, the focus trap in dialogs, no horizontal overflow at 360 px, and zero JS errors.
- Real-PDF tests with the sample files:
  - The invoice PDF gives "5 of 6 invoices found · 1 to confirm · 1 needs a fix".
  - The catalogue PDF is rejected.
  - The prototype also works offline from a local file.
- Text scans of every submitted document for consistency (names, metrics, claims).
- An independent evaluator pass after each round.
