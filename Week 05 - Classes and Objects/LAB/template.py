"""AI model monitoring report using classes and objects."""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    """Store an AI model metric and report whether it exceeds its limit."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Create a metric with a label, measured value and safe limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return the measured value as a percentage of its limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK for this model metric."""
        percent = self.percent()
        return (
            "OVER LIMIT"
            if percent >= 100
            else "WARNING"
            if percent >= 90
            else "OK"
        )


def load_records(path):
    """Load comma-separated AI metrics from a file."""
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

records = load_records("ai_metrics.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Measured: {record.value}")
    print(f"  Limit   : {record.limit}")
    print(f"  Usage   : {record.percent():.1f}%")
    print(f"  Status: {record.status()}")

    print("=" * 34)

over_limit_count = sum(record.status() == "OVER LIMIT" for record in records)
print(f"AI metrics over limit: {over_limit_count} of {len(records)}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
