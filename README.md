# RUDRAKSHA ENTERPRISES DASHBOARD

A static dashboard (no server, no build step). It reads `data/DASHBOARD.csv` when the page opens.

## Publish it on GitHub Pages (one time)

1. On GitHub, create a new **public** repository, for example `logistics-dashboard`.
2. Click **Add file > Upload files** and drag in everything from this folder
   (`index.html`, `README.md`, `.nojekyll`, the `data` folder and the `tools` folder). Click **Commit changes**.
3. Open **Settings > Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**,
   choose branch **main** and folder **/ (root)**, then **Save**.
4. After about a minute the site is live at `https://YOUR-USERNAME.github.io/logistics-dashboard/`.
   Share that link with anyone.

## Update the data every day

1. Export the new Challan Unload CSV.
2. **Remove the PAN and Contact Number columns first** (the repository is public, so the CSV file itself is public).
   Either delete those columns in Excel, or run `python tools/clean_csv.py "new-export.csv"`, which writes a clean `data/DASHBOARD.csv`.
3. In GitHub open the `data` folder, choose **Add file > Upload files**, drop the new file
   **named exactly `DASHBOARD.csv`** and click **Commit changes**.
4. Wait about a minute and refresh the dashboard (Ctrl+F5 if you still see old numbers).
   The header shows when the data file was last updated.

### Keeping several months
To show more than one file together, upload each file into `data/` and list the names in `data/files.json`, for example
`["DASHBOARD.csv", "AUG-2026.csv"]`. Trips are matched by TP number, so a trip that appears twice is counted once (later file wins).

## Upload CSV button (preview)
The **Upload CSV** button, or dragging a file onto the page, loads a file into your own browser to check it.
It does not change what other people see, and it is forgotten on refresh. Public updates always go through `data/DASHBOARD.csv`.

## Notes
- Required columns: SlNo, Challan Date, Truck Number, Unloading Date, UL Net, Agent/Broker Name, Permit Number, Pass Number.
- Everything on the dashboard, including freight, HSD, advances and transporter names, is visible to anyone with the link.
- If you open `index.html` straight from your computer, the browser blocks reading `data/DASHBOARD.csv`, so it shows a built-in snapshot instead. On GitHub Pages it loads the live file.
