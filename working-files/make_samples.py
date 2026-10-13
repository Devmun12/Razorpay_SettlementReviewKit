"""Generates the synthetic sample PDFs in samples/ (reportlab). All data is fictional."""
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
W, H = A5
PAGES = [
    dict(no='1036', order='1036', name='Ishaan R.', date='2 Oct 2026', item='Cotton kurta set, mustard', amt='1,990'),
    dict(no='1038', order='1038', name='Anjali M.', date='3 Oct 2026', item='Bandhani dupatta + kurti', amt='2,150'),
    dict(no='M-0398', order=None, name='Neha K.', date='3 Oct 2026', item='Block-print kurta, indigo (handwritten bill, typed up)', amt='1,390'),
    dict(no='1044', order='1044', name='Pooja S.', date='4 Oct 2026', item='Leheriya saree', amt='1,250'),
    dict(gst=True),
    dict(no='1046', order='1046', name='Kavya R.', date='4 Oct 2026', item='Gota-patti lehenga skirt', amt='3,280'),
    dict(no='1047', order='1047', name='Simran D.', date='5 Oct 2026', item='Lehenga choli, rani pink', amt='1,180'),
    dict(no='1049', order='1049', name='Tanvi G.', date='5 Oct 2026', item='Two kurtas, festive set', amt='2,640'),
    dict(no='1052', order='1052', name=None, date='5 Oct 2026', item='Two kurtas, festive set', amt='2,640'),
]
def banner(c):
    c.setFont('Helvetica', 7); c.drawString(28, H - 20, 'SAMPLE - synthetic data for the Settlement Review Kit prototype. Not a real invoice.')
c = canvas.Canvas('samples/Ghoomar_invoices_SAMPLE.pdf', pagesize=A5)
c.setTitle('SAMPLE invoices - synthetic data')
for p in PAGES:
    banner(c)
    if p.get('gst'):
        c.setFont('Helvetica-Bold', 13); c.drawString(28, H - 60, 'Certificate of Registration (GST REG-06)')
        c.setFont('Helvetica', 10)
        for i, l in enumerate(['Legal name: Ghoomar Studio (sample)', 'GSTIN: 08ABCDE1234F1Z5 (sample)', 'Address: Jaipur, Rajasthan', 'Type of registration: Regular']):
            c.drawString(28, H - 90 - 16 * i, l)
        c.showPage(); continue
    c.setFont('Helvetica-Bold', 14); c.drawString(28, H - 56, 'Ghoomar Studio')
    c.setFont('Helvetica', 9); c.drawString(28, H - 70, 'Jaipur, Rajasthan  |  GSTIN 08ABCDE1234F1Z5 (sample)')
    c.setFont('Helvetica-Bold', 12); c.drawString(28, H - 100, 'TAX INVOICE')
    c.setFont('Helvetica', 10); y = H - 122
    for line in [f"Invoice No: {p['no'] if p['no'].startswith('M') else 'INV-' + p['no']}", f"Order No: {('#' + p['order']) if p['order'] else '-'}", f"Date: {p['date']}", f"Bill to: {p['name'] or ''}"]:
        c.drawString(28, y, line); y -= 15
    y -= 13
    c.setFont('Helvetica-Bold', 10); c.drawString(28, y, 'Item'); c.drawRightString(W - 28, y, 'Amount'); y -= 6; c.line(28, y, W - 28, y); y -= 16
    c.setFont('Helvetica', 10); c.drawString(28, y, p['item']); c.drawRightString(W - 28, y, 'Rs. ' + p['amt']); y -= 24
    c.line(28, y + 8, W - 28, y + 8)
    c.setFont('Helvetica-Bold', 11); c.drawRightString(W - 28, y - 8, 'Total: Rs. ' + p['amt'])
    c.showPage()
c.save()
c = canvas.Canvas('samples/Festive_catalogue_SAMPLE.pdf', pagesize=A5)
for i in range(3):
    banner(c)
    c.setFont('Helvetica-Bold', 16); c.drawString(28, H - 60, f'Festive collection 2026 - page {i + 1}')
    c.setFont('Helvetica', 10); c.drawString(28, H - 84, 'Lehengas, kurtas and dupattas. Prices from Rs. 990. (SAMPLE)'); c.showPage()
c.save()
print('samples written')
