# water-leakage

Kitchener, Ontario (Canada)

"Water Main Breaks" dataset = inventory of all water main breaks, updated hourly
https://open-kitchenergis.opendata.arcgis.com/datasets/KitchenerGIS%3A%3Awater-main-breaks/about?utm_source=chatgpt.com

Published work using the Kitchener GeoHub 
https://www.mdpi.com/2673-4591/69/1/13?utm_source=chatgpt.com

# static dataset viewers

Created a static viewer at outputs/kitchener_labels_viewer.html. It loads the cleaned GeoJSON, shows a searchable/paginated table, and can download a CSV.

To use it (needs a local server so fetch works):

python3 -m http.server 8000

Then open:

http://localhost:8000/outputs/kitchener_labels_viewer.html
