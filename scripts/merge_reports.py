"""
merge_reports.py - Combines the main report with an addendum.

Author: Edward J Heinz
"""

from PyPDF2 import PdfMerger

def merge_pdfs(pdf1, pdf2, output_path):
    merger = PdfMerger()
    merger.append(pdf1)
    merger.append(pdf2)
    merger.write(output_path)
    merger.close()
    print(f"Merged into {output_path}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--main', required=True, help='Main PDF file')
    parser.add_argument('--addendum', required=True, help='Addendum PDF file')
    parser.add_argument('--output', required=True, help='Final merged PDF path')
    args = parser.parse_args()
    merge_pdfs(args.main, args.addendum, args.output)
