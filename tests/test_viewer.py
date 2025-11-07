import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestViewer(unittest.TestCase):
    def test_viewer_html_has_expected_hooks(self) -> None:
        path = ROOT / "outputs/kitchener_labels_viewer.html"
        self.assertTrue(path.exists(), "Missing outputs/kitchener_labels_viewer.html")

        text = path.read_text()
        self.assertIn("kitchener_water_main_breaks.geojson", text)
        self.assertIn("Download CSV", text)
        self.assertIn("tableBody", text)
