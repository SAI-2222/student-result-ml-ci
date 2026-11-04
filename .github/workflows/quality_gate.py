import json
import sys

with open("metrics.json", "r") as file:
    metrics = json.load(file)

accuracy = metrics.get("accuracy")

if accuracy is None:
    print("Quality gate failed: accuracy is missing.")
    sys.exit(1)

if accuracy < 0.90:
    print(f"Quality gate failed: accuracy {accuracy:.4f} is below 0.90.")
    sys.exit(1)

print(f"Quality gate passed: accuracy = {accuracy:.4f}")
