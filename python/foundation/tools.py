from __future__ import annotations

import logging

from pysam import VariantFile

logger = logging.getLogger(__name__)


def calculate_pi(n: int) -> float:
    """
    Basic calculation of pi
    """
    result = 3.14159265

    return round(result, n)


def load_vcf(fpath: str) -> VariantFile:
    """
    Load and print a VCF file
    """
    vcf = VariantFile(fpath)

    for rec in vcf.fetch("chr1", 1_000_000, 1_200_000):
        assert rec
        break

    return vcf


if __name__ == "__main__":
    # calculate_pi(3)

    result = load_vcf("/home/mw9568/data/HG001_GRCh38_1_22_v4.2.1_benchmark.vcf.gz")
