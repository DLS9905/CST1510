"""Load AI model metrics, calculate statuses, and save the results."""

from pathlib import Path


def check_record(value, target):
    """Return the difference from target, percentage, and status."""
    difference = value - target
    percent = (value / target) * 100
    if percent >= 100:
        status = "OVER TARGET"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, target, difference, percent, status):
    """Print a bordered report for one AI metric."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Measured    : {value:>10.2f}")
    print(f"  Target      : {target:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Relative    : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Load label, value, and limit records from a text file."""
    records = []
    with open(path) as file:
        for line in file:
            if line.strip():
                label, value, target = line.strip().split(",")
                records.append(
                    {"label": label, "value": float(value), "target": float(target)}
                )
    return records


lab_folder = Path(__file__).resolve().parent
try:
    records = load_records(lab_folder / "records_sample.txt")
except FileNotFoundError:
    print("Record file not found; no records were loaded.")
    records = []

over_limit_count = 0
with open(lab_folder / "results.txt", "w") as results_file:
    for record in records:
        difference, percent, status = check_record(record["value"], record["target"])
        print_report(
            record["label"],
            record["value"],
            record["target"],
            difference,
            percent,
            status,
        )
        results_file.write(f"{record['label']},{status}\n")
        if status == "OVER TARGET":
            over_limit_count += 1

print(f"OVER TARGET metrics: {over_limit_count}")
