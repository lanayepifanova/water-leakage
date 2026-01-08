# water-leakage

Kitchener, Ontario (Canada)

"Water Main Breaks" dataset = inventory of all water main breaks, updated hourly
https://open-kitchenergis.opendata.arcgis.com/datasets/KitchenerGIS%3A%3Awater-main-breaks/about?utm_source=chatgpt.com

Published work using the Kitchener GeoHub 
https://www.mdpi.com/2673-4591/69/1/13?utm_source=chatgpt.com

# visual checks

static dataset viewers
- **outputs/kitchener_labels_viewer.html**
- It loads the cleaned GeoJSON, shows a searchable/paginated table, and can download a CSV.
- python3 -m http.server 8000
- http://localhost:8000/outputs/kitchener_labels_viewer.html

# stdlib-only test suite

covers the repo’s key artifacts (geojson integrity, viewer HTML hooks, notebook validity, and time‑series CSV expectations) and verifies it runs cleanly.

  - Added GeoJSON integrity checks (structure, required properties, geometry types, date
    parsing) in tests/test_geojson.py.
  - Added viewer smoke test for expected hooks and dataset reference in tests/test_viewer.py.
  - Added notebook validation plus placeholder checks for empty notebooks in tests/
    test_notebooks.py.
  - Added time‑series README and CSV column checks (skips cleanly if no CSVs yet) in tests/
    test_time_series.py.


