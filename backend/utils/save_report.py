# backend/utils/save_report.py
import os, json
def save_report(obj, filename="reports/final_report.json"):
    os.makedirs("reports", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
    return filename
