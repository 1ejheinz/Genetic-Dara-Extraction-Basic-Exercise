"""
protease_addendum.py - Outputs placeholder table for rare/unimputed SNPs

Author: Edward J Heinz
"""

import pandas as pd

def generate_addendum(output_tsv):
    protease_snps = [
        ('rs903107', 'ALT regulation', 'Liver'),
        ('rs10812428', 'Drug-induced liver injury', 'Liver'),
        ('rs540431307', 'WASH7P regulatory site', 'Unknown'),
        ('rs555500075', 'WASH7P variant', 'Unknown'),
    ]
    df = pd.DataFrame(protease_snps, columns=['ID', 'Trait', 'System'])
    df['Genotype'] = 'Not Imputed'
    df.to_csv(output_tsv, sep='\t', index=False)
    print(f"Addendum saved to {output_tsv}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='Output TSV for protease addendum')
    args = parser.parse_args()
    generate_addendum(args.output)
