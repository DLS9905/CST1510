"""Check records interactively and report their usage percentages."""


def status_of(percent):
    """Return a status label for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the remaining amount and used percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


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


over_limit_count = 0

while True:
    label = input("Record name (or 'quit' to finish): ").strip()
    if label.lower() == "quit":
        break

    value = float(input("Value used: "))
    limit = float(input("Total limit: "))
    difference, percent = check(value, limit)
    status = status_of(percent)
    print_report(label, value, limit, difference, percent, status)
    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"OVER LIMIT records: {over_limit_count}")
