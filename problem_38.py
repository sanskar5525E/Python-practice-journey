import requests
import csv

API_KEY = "579b464db66ec23bdd00000115dd67dbc3c14f8d40632054013b1b38"
RESOURCE_ID = "ecd49b12-3084-4521-8f7e-ca8bf72069ba"

STATE_NAME = "Maharashtra"
OUTPUT_FILE = "aadhaar_monthly_report.csv"

all_records = []
offset = 0
limit = 100

while True:
    url = f"https://api.data.gov.in/resource/{RESOURCE_ID}"

    params = {
        "api-key": "579b464db66ec23bdd00000115dd67dbc3c14f8d40632054013b1b38",
        "format": "json",
        "limit": limit,
        "offset": offset 
    }

    response = requests.get(url, params=params)
    data = response.json()
    records = data.get("records", [])

    if not records:
        break

    all_records.extend(records)
    offset += limit

print(f"Total records fetched: {len(all_records)}")

# FILTER STATE
filtered = [r for r in all_records if r.get("state") == STATE_NAME]

print(f"Records for {STATE_NAME}: {len(filtered)}")

# CALCULATE TOTAL
total = 0

for r in filtered:
    value = r.get("aadhaar_generated", "0")

    if value:
        value = value.replace(",", "").strip()
        try:
            total += int(value)
        except:
            pass

print("Total Aadhaar Generated:", total)
# SAVE CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["State", "Month", "Year", "Aadhaar Generated"])

    for r in filtered:
        writer.writerow([
            r.get("state"),
            r.get("month"),
            r.get("year"),
            r.get("aadhaar_generated")
        ])

print("Automation complete. Report saved.")
