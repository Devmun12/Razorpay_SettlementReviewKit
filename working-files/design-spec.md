# Hold Release Kit: design spec (working file)

## Job
When Razorpay holds a merchant's settlement for a review that needs merchant evidence, let the merchant see exactly what is needed for which payments, send it from the phone in one complete pack, and track the review in one thread.

## Lead persona (emulated)
Riya, 29, runs Ghoomar Studio, an Instagram-led ethnic-wear label in Jaipur with her cousin. 14 months on Razorpay, Rs 6-8 lakh a month, average order ~Rs 1,400, ships via Shiprocket. A festive drop lifted volume ~8x in 4 days; Rs 3,18,400 of settlement is held. Invoices sit in her billing app as one PDF, delivery status in Shiprocket, customer confirmations in WhatsApp. Karigars and the Meta ad bill are due Friday.
Generalises to: Arjun, freelancer with an international client (one payment, contract + invoice + client confirmation).

## Hold types and routing (risk ops sets the type; merchant never sees the trigger)
| Hold type | Merchant sees | Evidence kit? |
| Evidence-eligible (delivery verification, volume spike, chargeback exposure) | Per-payment checklist, due date, estimated review window | Yes |
| Confidential review (incl. any suspected ML/STR case) | "Under review, nothing needed from you", update date, escalation ladder | Never (tipping-off) |
| Police / CFCFRMS lien | Held payment only, agency request, SOP timelines (15 days IO response, 90 days lift), grievance route | No; evidence goes to police/NCRP, not Razorpay risk |
| Re-KYC | Deadline, items, route to KYC update flow | No; KYC flow |

## Merchant flow (demo: 6 sampled payments x 2 items = 12)
1. Push -> case screen: amount held, due date, stepper, what's needed per payment, "you can still accept payments".
2. Fast-fill: invoices as one PDF (AI splits and matches pages to payments); delivery status from Shiprocket via AWB (verifiable source); WhatsApp/gallery for the rest.
3. AI pre-check (advisory): classify, extract amount/date/name/order, match to payment, flag mismatch, duplicate, unreadable, predicted follow-up. Merchant can fix or add a note.
4. Review pack: indexed cover sheet mapping each file to each request line (Razorpay's own blog format), declaration, submit.
5. Tracker: Requested -> Submitted -> In review -> Decision; estimated window; evidence locker; escalation ladder (10/20/30 business days).
6. Follow-up asks are delta-only ("1 new item; 11 accepted"). Decision: release / partial / more.

## Analyst side (two-sided value)
Console receives pre-indexed, pre-matched pack: independent verification (courier API), AI match confidence, merchant notes, soft flags; one-click delta request; release decision always human; reasons stay internal.

## AI jobs
- Document understanding: classify, extract, match (core).
- Predict likely follow-ups (soft flags).
- Plain Hindi/English explanation of the request.
- Not AI: release decisions, risk reasons, request content (templated by risk ops).
Evals: match precision >= 98% on labelled set; false-accept of wrong document < 1%; override rate tracked; latency < 5 s/file; fall back to manual upload + note.

## Key decisions
Show what, never why; kit only on eligible holds; complete packs only (no drip-feed both ways); verifiable evidence preferred over images; AI advisory, merchant can override with a note; estimate not SLA; delta-only re-requests; evidence locker; low-end Android (compression, retry); English/Hindi.

## Not built
Auto-release; showing reasons/scores; analyst chat; disputes (Dispute Responder); contesting police holds in-app; web version; partial-submission drip-feed.

## Metrics
North star: median time from hold notice to first complete submission.
Primary: first-submission completeness (no follow-up); hold-to-decision time by type.
Efficiency: support contacts per hold; analyst handle time.
Retention: 90-day volume retention of held merchants vs control.
Guardrails: loss on released funds; false-release rate; wrong AI accepts; escalations; zero kit launches on confidential cases.
