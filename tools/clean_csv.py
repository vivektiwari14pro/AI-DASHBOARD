"""
Remove PAN and Contact Number columns from a Challan Unload export
before it is uploaded to a PUBLIC GitHub repository.

Usage:
    python tools/clean_csv.py "path/to/new-export.csv"

Result: data/DASHBOARD.csv (overwritten). Commit that file to GitHub.
"""
import csv, os, sys

SENSITIVE = {"PAN", "Contact Number"}

if len(sys.argv) != 2:
    sys.exit('Usage: python tools/clean_csv.py "path/to/new-export.csv"')

src = sys.argv[1]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "DASHBOARD.csv")

with open(src, newline="", encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))

header_at = next((i for i, r in enumerate(rows) if r and r[0].strip() == "SlNo"), None)
if header_at is None:
    sys.exit('Header row starting with "SlNo" not found. Is this the right export?')

drop = {i for i, h in enumerate(rows[header_at]) if h.strip() in SENSITIVE}
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow([c for i, c in enumerate(r) if i not in drop])

print(f"Wrote {os.path.normpath(out)} without {len(drop)} sensitive columns.")
