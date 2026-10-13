# Settlement Review Kit

**Razorpay x ISB AI PM Build Challenge, Track 1: "Razorpay in Your Pocket"** · Devesh, ISB PGP 2026–27

When Razorpay holds a merchant's settlement for a review that needs evidence, the merchant sees exactly what's needed and for which payments. She prepares it on her phone, submits one versioned pack and gets a durable receipt. The review decision stays with Razorpay's analysts. They see each source, what was checked and what wasn't, and accept each requirement explicitly.

**AI does the paperwork. Razorpay makes the decision.**

| Submission item | Where |
| --- | --- |
| Prototype (live) | `index.html`, served by GitHub Pages: `https://<your-github-username>.github.io/<repo-name>/` |
| Demo video (90 s) | `video/Settlement_Review_Kit_Demo.mp4` |
| AI build log | [`AI_BUILD_LOG.md`](AI_BUILD_LOG.md) |
| Product note | [`docs/01_Product_Note.pdf`](docs/01_Product_Note.pdf) |

> Concept prototype, not a Razorpay product. All data is synthetic.
>
> **Real in the prototype:** reading a PDF you choose on your device (pdf.js), exact order-number and amount checks, merchant confirmation of ambiguous matches, the case state machine, saved progress, versioned receipts, and a review record for each requirement.
>
> **Simulated:** the hold service, the default demo files, the Shiprocket lookup, notifications and the analyst's decisions.

## Try it (about 2 minutes)

Open the live link on a phone, or in a desktop browser.

1. Tap the notification.
2. **Upload invoices** → Check invoices.
3. Fix #1044 by adding a note.
4. **Get delivery status** → Allow and fetch.
5. **Add from WhatsApp** → Simran's message.
6. **Review evidence pack** → tick the declaration → Submit. You get a receipt; refresh the page and it's still there.
7. On desktop, open the **Risk analyst's view** → View source → Accept → Ask for 1 item, or Release.

The left rail switches between hold types: no documents requested (confidential), police hold, and KYC update due. **Start over** clears the saved case.

**Try the real reading:**
1. In Upload invoices, choose **"Choose a PDF from this device"**.
2. Pick `samples/Ghoomar_invoices_SAMPLE.pdf`. It:
   - finds 5 invoices
   - flags ₹1,250 against ₹1,450 on #1044
   - ignores a GST certificate and two unrelated invoices
   - asks you to confirm a page that has no order number
3. Pick `samples/Festive_catalogue_SAMPLE.pdf` to see a wrong file rejected.

Everything is read in your browser; nothing is uploaded.

## Run it locally

Download the repo and open `index.html` in Chrome. It works offline, including PDF reading, as long as the `vendor/` folder stays next to it.

## Folders

- `docs/`: the product note.
- `video/`: the 90-second demo, a real screen recording of this prototype.
- `samples/`: synthetic PDFs for the real-reading path.
- `screenshots/`: desktop and phone views.
- `vendor/`: Mozilla's pdf.js 3.11.174 (Apache 2.0; licence included).
- `working-files/`: the design spec, the sample generator, and the script that records the demo video (`rec.py`, `stage.html`).
