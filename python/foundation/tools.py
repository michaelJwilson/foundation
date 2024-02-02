from __future__ import annotations

from pysam import VariantFile


def calculate_pi(n: int) -> float:
    """
    Basic calculation of pi
    """
    result = 0.0

    # Initialize denominator
    k = 1

    # Initialize sum
    for i in range(1_000_000):
        # even index elements are positive
        if i % 2 == 0:
            result += 4 / k
        else:
            # odd index elements are negative
            result -= 4 / k

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
