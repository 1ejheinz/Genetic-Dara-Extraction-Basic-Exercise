"""
parse_vcf.py - Extracts SNP genotypes from .vcf.gz file and outputs TSV.

Author: Edward J Heinz
"""

import gzip
import pandas as pd

def parse_vcf(vcf_path, output_tsv):
    rsids = []
    genotypes = []
    chroms = []

    with gzip.open(vcf_path, 'rt') as f:
        for line in f:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            chrom, pos, rsid, ref, alt, qual, filter_, info, format_, sample = fields[:10]
            if not rsid.startswith('rs'):
                continue
            gt_info = sample.split(':')[0]
            if gt_info == '0/0':
                genotype = f"{ref}/{ref}"
            elif gt_info == '0/1' or gt_info == '1/0':
                genotype = f"{ref}/{alt}"
            elif gt_info == '1/1':
                genotype = f"{alt}/{alt}"
            else:
                genotype = 'NA'
            rsids.append(rsid)
            genotypes.append(genotype)
            chroms.append(chrom)

    df = pd.DataFrame({'Chromosome': chroms, 'ID': rsids, 'Genotype': genotypes})
    df.to_csv(output_tsv, sep='\t', index=False)
    print(f"Extracted {len(df)} SNPs to {output_tsv}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Extract SNP genotypes from VCF')
    parser.add_argument('--vcf', required=True, help='Input .vcf.gz file')
    parser.add_argument('--out', required=True, help='Output TSV path')
    args = parser.parse_args()
    parse_vcf(args.vcf, args.out)
