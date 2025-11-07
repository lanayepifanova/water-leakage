import csv
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIME_SERIES_DIR = ROOT / "data/imagery/sentinel2_time_series"


class TestTimeSeries(unittest.TestCase):
    def test_time_series_readme_exists(self) -> None:
        readme = TIME_SERIES_DIR / "README.txt"
        self.assertTrue(readme.exists(), "Missing data/imagery/sentinel2_time_series/README.txt")
        text = readme.read_text()
        self.assertIn("Sentinel-2 time series", text)

    def test_time_series_csv_columns(self) -> None:
        csv_paths = sorted(TIME_SERIES_DIR.glob("*.csv"))
        if not csv_paths:
            self.skipTest("No time series CSVs present; export them to run this test.")

        required = {"break_id", "break_date", "NDVI", "NDWI", "NDRE", "RENDVI"}
        for path in csv_paths:
            with path.open(newline="") as handle:
                reader = csv.reader(handle)
                header = next(reader, [])
            missing = required.difference(header)
            self.assertFalse(missing, f"{path.name} missing columns: {sorted(missing)}")
