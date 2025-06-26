# 🧬 Genetic Health Report Generator

Generate a full personalized genetic health report from your VCF/TSV files.

### Author
Edward J Heinz — based on example imputed genome analysis, and trait curation.

### Features
- Parses and extracts genotypes from VCF or TSV files
- Annotates medically relevant SNPs (risk/protective/pharmacogenomic)
- Adds protease + rare variants (even if not imputed)
- Generates a PDF with:
  - Full SNP table
  - Trait summaries
  - Cancer and system-specific risks
  - Lifestyle and supplement protocol
  - Final narrative summary

### Setup
```bash
git clone https://github.com/YOUR_USERNAME/genetic-health-analysis.git
cd genetic-health-analysis
pip install -r requirements.txt
```

### Run (example pipeline)
```bash
python scripts/parse_vcf.py
python scripts/annotate_snps.py
python scripts/supplement_protocol.py
python scripts/protease_addendum.py
python scripts/pdf_report.py
python scripts/merge_reports.py
```

### License
MIT
