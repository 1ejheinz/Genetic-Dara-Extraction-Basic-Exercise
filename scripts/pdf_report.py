"""
pdf_report.py - Generate PDF from annotated SNP data

Author: Edward J Heinz
"""

import pandas as pd
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Genetic Health Report', ln=True, align='C')
        self.ln(5)

def generate_pdf(input_tsv, output_pdf):
    df = pd.read_csv(input_tsv, sep='\t')
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    pdf.cell(25, 8, 'rsID', 1)
    pdf.cell(25, 8, 'Genotype', 1)
    pdf.cell(30, 8, 'Gene', 1)
    pdf.cell(65, 8, 'Trait', 1)
    pdf.cell(40, 8, 'System', 1)
    pdf.cell(20, 8, 'Effect', 1, ln=True)

    for _, row in df.iterrows():
        pdf.cell(25, 8, str(row['ID']), 1)
        pdf.cell(25, 8, str(row['Genotype']), 1)
        pdf.cell(30, 8, str(row['Gene']), 1)
        pdf.cell(65, 8, str(row['Trait'])[:40], 1)
        pdf.cell(40, 8, str(row['System']), 1)
        pdf.cell(20, 8, str(row['Effect']), 1, ln=True)

    pdf.output(output_pdf)
    print(f"PDF report saved to {output_pdf}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input annotated TSV file')
    parser.add_argument('--output', required=True, help='Output PDF file')
    args = parser.parse_args()
    generate_pdf(args.input, args.output)
