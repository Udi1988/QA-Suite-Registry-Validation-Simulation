import json

def validate_record(record):
    errors = []

    # Validate holder_id starts with HLD
    if not record['holder_id'].startswith("HLD"):
        errors.append("Invalid holder_id prefix")

    # Validate balance is not negative
    if record['balance'] < 0:
        errors.append("Negative balance is not allowed")

    # Validate status
    if record['status'] not in ["Active", "Inactive", "Deceased"]:
        errors.append(f"Invalid status '{record['status']}'")

    # Validate name is not empty
    if not record['name']:
        errors.append("Name field is empty")

    return errors

# Load and validate registry records
with open('Sample_Registry_Data.json') as file:
    data = json.load(file)

print("=== RML Registry Record Validation ===")
for idx, record in enumerate(data, start=1):
    print(f"\nRecord #{idx}:")
    errors = validate_record(record)
    if errors:
        for error in errors:
            print(f"  ❌ {error}")
    else:
        print("  ✅ Record is valid")
