"""AI/Data Science mini-project: clean and classify survey records."""

from pathlib import Path


def parse_line(raw_line):
    """Parse a messy survey record into a clean dictionary."""
    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)
    fields = {"survey": survey_part.strip().lower()}
    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = value.strip()
    fields["rating"] = int(fields["rating"])
    fields["age"] = int(fields["age"])
    return fields


def status_of(rating):
    """Return FLAGGED for low ratings and OK otherwise."""
    return "FLAGGED" if rating <= 2 else "OK"


records = []
records_path = Path(__file__).with_name("survey_records.txt")
with records_path.open(encoding="utf-8") as records_file:
    for raw_record in records_file:
        if raw_record.strip():
            records.append(parse_line(raw_record))

flagged_count = 0
for record in records:
    status = status_of(record["rating"])
    if status == "FLAGGED":
        flagged_count += 1
    print(record, status)

print(f"Summary: {len(records)} records, {flagged_count} flagged")
