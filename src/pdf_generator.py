import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Try different font paths
POSSIBLE_FONT_PATHS = [
    "C:/Windows/Fonts/ARIAL.TTF",
    "C:/Windows/Fonts/arial.ttf",
    "C:/Windows/Fonts/ARIALUNI.TTF",
    "C:/Windows/Fonts/TIMES.TTF",
    os.path.join(os.path.dirname(__file__), 'fonts', 'DejaVuSans.ttf')
]

def find_suitable_font():
    for font_path in POSSIBLE_FONT_PATHS:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('CustomFont', font_path))
                return True
            except:
                continue
    return False

def generate_pdf_from_csv(csv_file, pdf_file):
    # Register font
    if not find_suitable_font():
        raise RuntimeError("No suitable font found for PDF generation")
    
    # Read CSV
    df = pd.read_csv(csv_file, delimiter=';', encoding='utf-8')
    
    # Extract names
    donor_column = 'Öffentlich Spender-Name (als Nachweis auf den Spendenbannern)'
    names = [name for name in df[donor_column].dropna() if name.strip()]
    
    # Create table data
    table_data = []
    row = []
    for name in names:
        row.append(name)
        if len(row) == 3:
            table_data.append(row)
            row = []
    if row:
        while len(row) < 3:
            row.append('')
        table_data.append(row)
    
    # Generate PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    if table_data:
        table = Table(table_data, colWidths=[180] * 3)
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'CustomFont'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        doc.build([table])