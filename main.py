from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def create_invoice(invoice_data):
    file_name = "invoice.pdf"
    document_title = "Invoice"
    title = "Invoice"
    sub_title = "Order #{}".format(invoice_data['order_id'])
    customer_name = invoice_data['customer_name']
    address = invoice_data['address']
    items = invoice_data['items']
    total = sum(item['price'] * item['quantity'] for item in items)

    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.setTitle(document_title)

    # Title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(300, 750, title)

    # Subtitle
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(300, 730, sub_title)

    # Customer Details
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, "Customer Name: {}".format(customer_name))
    pdf.drawString(50, 680, "Address: {}".format(address))

    # Items
    pdf.setFillColor(colors.black)
    pdf.drawString(50, 650, "Item")
    pdf.drawString(200, 650, "Quantity")
    pdf.drawString(300, 650, "Price")
    pdf.drawString(400, 650, "Total")

    y = 630
    for item in items:
        pdf.drawString(50, y, item['description'])
        pdf.drawString(200, y, str(item['quantity']))
        pdf.drawString(300, y, "${:.2f}".format(item['price']))
        pdf.drawString(400, y, "${:.2f}".format(
            item['price'] * item['quantity']))
        y -= 20

    # Total
    pdf.drawString(50, y, "Total:")
    pdf.drawString(400, y, "${:.2f}".format(total))

    pdf.save()


invoice_data = {
    'order_id': '0072442',
    'customer_name': 'Mike the Mouse',
    'address': '123 Disney Street, Anytown, VIC 3001',
    'items': [
        {'description': 'Frozen Disney Head', 'quantity': 1, 'price':
         10099.00},
        {'description': 'Mouse Boots', 'quantity': 1000, 'price': 255.99},
        {'description': 'Goofy Socks', 'quantity': 399, 'price': 49.95}
    ]
}

create_invoice(invoice_data)
