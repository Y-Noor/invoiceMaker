from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_invoice(filename, invoice_data):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(2.5 * inch, height - 1 * inch, "ABDUR RAHIM YADALLEE")
    
    # Invoice details
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, f"Invoice Number: {invoice_data['invoice_number']}")
    c.drawString(1 * inch, height - 1.75 * inch, f"Date: {invoice_data['date']}")
    c.drawString(1 * inch, height - 2 * inch, f"Due Date: {invoice_data['due_date']}")
    
    # Billing Information
    c.drawString(1 * inch, height - 2.5 * inch, "Bill To:")
    c.drawString(1 * inch, height - 2.75 * inch, invoice_data['billing_info'])
    
    # Table header
    c.drawString(1 * inch, height - 3.25 * inch, "Description")
    c.drawString(5 * inch, height - 3.25 * inch, "Unit Price")
    c.drawString(6.5 * inch, height - 3.25 * inch, "Quantity")
    c.drawString(7.5 * inch, height - 3.25 * inch, "Total")
    
    # Table rows
    y_position = height - 3.5 * inch
    for item in invoice_data['items']:
        c.drawString(1 * inch, y_position, item['description'])
        c.drawString(5 * inch, y_position, f"${item['unit_price']:.2f}")
        c.drawString(6.5 * inch, y_position, str(item['quantity']))
        c.drawString(7.5 * inch, y_position, f"${item['total']:.2f}")
        y_position -= 0.25 * inch
    
    # Total Amount
    c.drawString(6.5 * inch, y_position - 0.5 * inch, "Total Amount:")
    c.drawString(7.5 * inch, y_position - 0.5 * inch, f"${invoice_data['total_amount']:.2f}")
    
    c.save()

# Example invoice data
invoice_data = {
    "invoice_number": "INV-001",
    "date": "2024-10-24",
    "due_date": "2024-11-24",
    "billing_info": "John Doe\n123 Main St\nCity, State ZIP",
    "items": [
        {"description": "Widget A", "unit_price": 10.00, "quantity": 2, "total": 20.00},
        {"description": "Widget B", "unit_price": 15.00, "quantity": 1, "total": 15.00},
    ],
    "total_amount": 35.00
}

# Create the invoice
create_invoice("invoice.pdf", invoice_data)

