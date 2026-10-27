"""Load records, calculate their statuses, and save the results."""

from pathlib import Path


def check_record(value, limit):
    """Return the free amount, percentage used, and status."""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Load label, value, and limit records from a text file."""
    records = []
    with open(path) as file:
        for line in file:
            if line.strip():
                label, value, limit = line.strip().split(",")
                records.append(
                    {"label": label, "value": float(value), "limit": float(limit)}
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
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status,
        )
        results_file.write(f"{record['label']},{status}\n")
        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"OVER LIMIT records: {over_limit_count}")
