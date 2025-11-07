import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


class TestNotebooks(unittest.TestCase):
    def test_placeholders_are_empty(self) -> None:
        for name in ["01_explore_labels.ipynb", "04_model_training.ipynb"]:
            path = NOTEBOOKS / name
            self.assertTrue(path.exists(), f"Missing {path}")
            self.assertEqual(path.stat().st_size, 0, f"{name} should be empty")

    def test_notebooks_are_valid_json(self) -> None:
        for name in ["02_pull_sentinel.ipynb", "02_pull_sentinel_time_series.ipynb", "03_anomaly_detection.ipynb"]:
            path = NOTEBOOKS / name
            self.assertTrue(path.exists(), f"Missing {path}")
            text = path.read_text()
            self.assertTrue(text.strip(), f"{name} is empty")
            obj = json.loads(text)
            self.assertIn("cells", obj)
            self.assertIsInstance(obj["cells"], list)
            self.assertGreater(len(obj["cells"]), 0)
