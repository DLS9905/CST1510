"""Report the size of an AI model against its expected size."""

label = input("Model name: ").strip()
actual_size = float(input("Actual model size (MB): "))
expected_size = float(input("Expected model size (MB): "))

difference = actual_size - expected_size
percent = (actual_size / expected_size) * 100

print()
print("=" * 42)
print(f"  AI MODEL SIZE CHECK - {label}")
print("=" * 42)
print(f"  Actual size   : {actual_size:>10.2f} MB")
print(f"  Expected size : {expected_size:>10.2f} MB")
print(f"  Difference    : {difference:>+10.2f} MB")
print(f"  Expected used : {percent:>10.2f} %")
print("=" * 42)
