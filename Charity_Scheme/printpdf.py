from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
def printpdffn(data,fd,td):
# Define your table data including the headings and the total row
#     data = [
#         ['Date', 'User Name', 'Amount', 'Need'],
#         ['2024-04-01', 'John Doe', '100', 'Food'],
#         ['2024-04-02', 'Jane Smith', '200', 'Clothing'],
#         ['', 'Total', '300', ''],  # Total row
#
#     ]

    # Create a PDF document
    pdf_filename = r'C:\Users\THINKPAD\PycharmProjects\Charity_Scheme_and_Fund_Tracker_Using_Blockchain\media\report.pdf'
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []

    # Define styles for heading and date
    heading_style = ParagraphStyle(name='HeadingStyle', fontSize=18, alignment=1)
    date_style = ParagraphStyle(name='DateStyle', fontSize=12, alignment=1)

    # Add heading and date outside the table
    heading_text = '<u>Donation Report</u>'
    heading_paragraph = Paragraph(heading_text, heading_style)
    elements.append(heading_paragraph)

    from_date = fd
    to_date = td
    date_text = f'<p>From Date:{from_date} &nbsp;&nbsp;&nbsp; To Date:{to_date}</p>'
    date_paragraph = Paragraph(date_text, date_style)
    elements.append(Paragraph('<br/><br/>', date_style))
    elements.append(date_paragraph)

    # Add space between date and table
    elements.append(Paragraph('<br/><br/>', date_style))

    # Create a table from the data
    table = Table(data)

    # Apply styles to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),         # Center align all cells
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),        # Center align vertically
        ('GRID', (0, 0), (-1, -1), 1, colors.black),   # Add grid lines

    ])

    table.setStyle(style)
    elements.append(table)

    # Build the PDF document with the elements
    doc.build(elements)

    print(f'PDF report generated: {pdf_filename}')
