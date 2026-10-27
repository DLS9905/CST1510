# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

from pathlib import Path

sample_path = Path(__file__).resolve().parent.parent / "records_sample.txt"

with open(sample_path) as f:
    print(f.read())
