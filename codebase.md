**This is a small, notebook-driven prototype to detect water-main break signals 
around Kitchener, Ontario using Sentinel imagery + break labels**
  - README.md explains the dataset source and how to use the static viewer.
  - kitchener_dataset.geojson appears to be a bundled dataset artifact.
  - anna_notes.txt and lana_notes.txt are research notes outlining the concept and steps.

**Key Terminology:**
  - Labels: the event data you want to predict or detect. Here that’s the water‑main break
    points in data/labels/kitchener_water_main_breaks.geojson.
  - Geometry: the spatial mask/area you analyze. Here that’s the pipe corridor polygons in
    data/geometry/corridors.geojson.

**Labels and geometry live as GeoJSON: **
- data/labels/kitchener_water_main_breaks.geojson (break points) 
    - A static label viewer exists at outputs/kitchener_labels_viewer.html (served locally)
- data/geometry/corridors.geojson (pipeline corridor mask)

Google Earth Engine pulls Sentinel‑2 imagery, produces time series around each break
- **notebooks/02_pull_sentinel.ipynb**: uses Earth Engine to build monthly Sentinel‑2 composites over the corridor mask and exports images to Google Drive
- those CSVs are stored in **data/imagery/sentinel2_time_series/**

**Anomaly features are computed from those CSVs**
- written to data/features/anomaly_features.parquet.

**Notebooks**
  - notebooks/02_pull_sentinel.ipynb: uses Earth Engine to build monthly Sentinel‑2
    composites over the corridor mask and exports images to Google Drive.
  - notebooks/02_pull_sentinel_time_series.ipynb: builds per‑break time series (NDVI/NDWI/
    NDRE/RENDVI) with a baseline window and exports a CSV to Drive.
  - notebooks/03_anomaly_detection.ipynb: loads exported CSVs, builds same‑month baselines,
    computes z‑score anomalies, aggregates per break, and saves a parquet.
  - notebooks/01_explore_labels.ipynb and notebooks/04_model_training.ipynb are empty
    placeholders.

 
