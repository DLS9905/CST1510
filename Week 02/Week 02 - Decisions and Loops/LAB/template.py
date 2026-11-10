"""Classify AI model confidence scores against a target threshold."""

over_target_count = 0

while True:
    model_name = input("Model name (or 'quit' to finish): ").strip()
    if model_name.lower() == "quit":
        break

    confidence = float(input("Confidence score (%): "))
    target = float(input("Target score (%): "))
    difference = confidence - target
    percent = (confidence / target) * 100

    if percent >= 100:
        status = "OVER TARGET"
        over_target_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "BELOW TARGET"

    print()
    print("=" * 42)
    print(f"  AI CONFIDENCE CHECK - {model_name}")
    print("=" * 42)
    print(f"  Confidence : {confidence:>10.2f} %")
    print(f"  Target     : {target:>10.2f} %")
    print(f"  Difference : {difference:>+10.2f} points")
    print(f"  Relative   : {percent:>10.2f} %")
    print(f"  Status     : {status}")
    print("=" * 42)

print(f"Models over target: {over_target_count}")
