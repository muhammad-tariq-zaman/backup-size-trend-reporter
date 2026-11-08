"""Backup size trend per job: growing, shrinking or flat.

Usage: python3 main.py backups.csv
CSV columns: backup,date (ISO),size_gb.
Per job: first and last size, change in percent, and trend
GROWING / SHRINKING / FLAT (within 1%). Largest growth first.
"""
import argparse, csv, sys
from collections import defaultdict

def report(rows):
    by_job = defaultdict(list)
    for row in rows:
        by_job[row["backup"]].append((row["date"].strip(), float(row["size_gb"])))
    out = []
    for job, samples in by_job.items():
        samples.sort()
        first, last = samples[0][1], samples[-1][1]
        change = (last - first) / first if first else 0
        trend = "GROWING" if change > 0.01 else ("SHRINKING" if change < -0.01 else "FLAT")
        out.append((job, first, last, change, trend))
    return sorted(out, key=lambda r: -r[3])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for job, first, last, change, trend in report(list(csv.DictReader(f))):
            print(f"{job}: {trend} ({first:.1f} GB -> {last:.1f} GB, {change:+.0%})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
