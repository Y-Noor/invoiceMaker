from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Paragraph, paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
def my_first_page(canvas, doc):

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=styles['Title'],  # Inherit from the default Title style
        fontName='Helvetica-Bold',  # Specify the font name
        fontSize=24,  # Set the font size
        leading=28,  # Adjust line spacing
        alignment=1  # Center the title
    )


    centered_style = ParagraphStyle(
        name='CenteredStyle',
        parent=styles['Normal'],  # Inherit from the default Normal style
        alignment=1,  # Align the text to the center
        fontSize=14,
        leading=16
    )


    customer_style = ParagraphStyle(
        name='CenteredStyle',
        parent=styles['Normal'],  # Inherit from the default Normal style
        alignment=1,  # Align the text to the center
        fontSize=16,
        leading=20
    )



    left_align = ParagraphStyle(
        name='reightAlignedStyle',
        parent=styles['Normal'],  # Inherit from the default Normal style
        alignment=0,  # Align the text to the right
        fontSize=14,
        leading=0
    )

    right_align = ParagraphStyle(
        name='reightAlignedStyle',
        parent=styles['Normal'],  # Inherit from the default Normal style
        alignment=2,  # Align the text to the right
        fontSize=14,
        leading=16
    )


    sig_style = ParagraphStyle(
        name='signature',
        parent=styles['Normal'],  # Inherit from the default Normal style
        alignment=0,  # Align the text to the right
        fontSize=11,
        leading=0
    )


    styles = getSampleStyleSheet()
    blank_line = Paragraph("", title_style)
    title = Paragraph("Abdur Rahim Yadallee", title_style)
    story.append(title)
   

    line_of_text = Paragraph("Cnr. Victoria & Ollier Avenues, Quatre Bornes, Mauritius <br /> BRN No.: I10004640 <br /> 428 3848", centered_style)
    story.append(line_of_text)
    story.append(blank_line)


    date_invoice = "Date: 22/12/00"
    jajaja = 12345
    invoice_num = f"Invoice: {jajaja}"
    l1 = Paragraph(date_invoice, left_align)
    l2 = Paragraph(invoice_num, right_align)
    story.append(l1)
    story.append(l2)


    customer = "customeeeeeeeeeeeeeeeeeeeeeeeeeer"
    l3 = Paragraph(customer, customer_style)
    story.append(l3)


    
    invoice_data = fetch_data()

    while len(invoice_data) < 21:
        invoice_data.append([])
    # ... other items
    
    invoice_data.append([Paragraph("Total", right_align), "", "", "Rs 12484.00"])

    styles = getSampleStyleSheet()
    table = Table(invoice_data, colWidths=[1.25 * cm, 12.25 * cm, 2.5 *cm, 3 * cm])


    n = len(invoice_data)-1
# Apply table styles (customize as needed)
    table.setStyle(TableStyle([
        ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'grey'),
        ('SPAN', (0, n), (2, n)),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, 'black'),
        ('BOX', (0, 0), (-1, -1), 0.25, 'black'),
    ]))


    story.append(table)

    for i in range(6):
        story.append(blank_line)
    sig = Paragraph("_"*24, left_align)
    story.append(sig)
    story.append(blank_line) 
    story.append(blank_line) 
    story.append(blank_line) 
    story.append(Paragraph('Signature of customer/receiving officer', sig_style))
        
    story.append(blank_line) 
    story.append(blank_line) 
    story.append(blank_line) 
    story.append(blank_line) 
    story.append(blank_line) 

    story.append(sig)
    story.append(blank_line)
    story.append(blank_line) 
    story.append(blank_line)
    story.append(Spacer(5 * cm, 0)) 
    story.append(Paragraph('Name of customer/receiving officer', sig_style))
        


def fetch_data():
    pass


doc = SimpleDocTemplate("invoice.pdf", pagesize=letter)
story = [Spacer(1, 0)]  # Assuming 'taaable' is your table object

doc.build(story, onFirstPage=my_first_page, onLaterPages=my_first_page)
