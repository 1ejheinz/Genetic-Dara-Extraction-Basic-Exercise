"""
annotate_snps.py - Annotates SNPs with gene, trait, system, and effect.

Author: Edward J Heinz
"""

import pandas as pd

# Example mapping dictionary
known_snp_annotations = {
    'rs738409': ('PNPLA3', 'Fatty liver risk', 'Liver', 'Risk'),
    'rs1801133': ('MTHFR', '↓ Methylation', 'Systemic', 'Risk'),
    'rs53576': ('OXTR', 'Empathy/stress response', 'Brain', 'Trait'),
    'rs6323': ('MAOA', 'Mood & impulse control', 'Brain', 'Risk'),
    'rs4244285': ('CYP2C19', '↓ SSRI metabolism', 'Pharmacogenomics', 'Risk'),
}

def annotate(tsv_path, output_path):
    df = pd.read_csv(tsv_path, sep='\t')
    annots = []
    for rsid in df['ID']:
        gene, trait, system, effect = known_snp_annotations.get(rsid, ('Unknown', '', '', ''))
        annots.append((gene, trait, system, effect))
    gene, trait, system, effect = zip(*annots)
    df['Gene'] = gene
    df['Trait'] = trait
    df['System'] = system
    df['Effect'] = effect
    df.to_csv(output_path, sep='\t', index=False)
    print(f"Annotated {len(df)} SNPs → {output_path}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input TSV with rsIDs')
    parser.add_argument('--output', required=True, help='Output annotated TSV')
    args = parser.parse_args()
    annotate(args.input, args.output)
