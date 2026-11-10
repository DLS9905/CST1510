"""Check AI model metrics interactively using reusable functions."""


def status_of(percent):
    """Return a status label for a model metric percentage."""
    if percent >= 100:
        return "OVER TARGET"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check(value, target):
    """Return the difference from target and relative percentage."""
    difference = value - target
    percent = (value / target) * 100
    return difference, percent


def print_report(label, value, target, difference, percent, status):
    """Print a bordered report for one AI model metric."""
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


over_target_count = 0

while True:
    label = input("AI metric name (or 'quit' to finish): ").strip()
    if label.lower() == "quit":
        break

    value = float(input("Measured value: "))
    target = float(input("Target value: "))
    difference, percent = check(value, target)
    status = status_of(percent)
    print_report(label, value, target, difference, percent, status)
    if status == "OVER TARGET":
        over_target_count += 1

print(f"OVER TARGET metrics: {over_target_count}")
