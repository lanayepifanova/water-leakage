import datetime as _dt
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestGeoJSON(unittest.TestCase):
    def _load_json(self, rel_path: str) -> dict:
        path = ROOT / rel_path
        self.assertTrue(path.exists(), f"Missing file: {rel_path}")
        return json.loads(path.read_text())

    def test_labels_geojson(self) -> None:
        data = self._load_json("data/labels/kitchener_water_main_breaks.geojson")
        self.assertEqual(data.get("type"), "FeatureCollection")
        features = data.get("features", [])
        self.assertGreater(len(features), 0)

        ids = []
        for feat in features[:50]:
            self.assertEqual(feat.get("type"), "Feature")
            props = feat.get("properties", {})
            geom = feat.get("geometry", {})
            self.assertEqual(geom.get("type"), "Point")
            self.assertIn("id", props)
            self.assertIn("lat", props)
            self.assertIn("lon", props)
            self.assertIn("break_date", props)
            self.assertIsInstance(props["lat"], (int, float))
            self.assertIsInstance(props["lon"], (int, float))
            _dt.date.fromisoformat(props["break_date"])
            ids.append(props["id"])

        self.assertEqual(len(ids), len(set(ids)))

    def test_corridors_geojson(self) -> None:
        labels = self._load_json("data/labels/kitchener_water_main_breaks.geojson")
        label_ids = {feat["properties"]["id"] for feat in labels.get("features", [])}

        data = self._load_json("data/geometry/corridors.geojson")
        self.assertEqual(data.get("type"), "FeatureCollection")
        features = data.get("features", [])
        self.assertGreater(len(features), 0)

        for feat in features[:50]:
            self.assertEqual(feat.get("type"), "Feature")
            props = feat.get("properties", {})
            geom = feat.get("geometry", {})
            self.assertIn(geom.get("type"), {"Polygon", "MultiPolygon"})
            self.assertIn("break_id", props)
            self.assertIn("radius_m", props)
            self.assertIn("source", props)
            self.assertGreater(props["radius_m"], 0)
            self.assertIsInstance(props["source"], str)
            self.assertIn(props["break_id"], label_ids)

    def test_combined_dataset_geojson(self) -> None:
        data = self._load_json("kitchener_dataset.geojson")
        self.assertEqual(data.get("type"), "FeatureCollection")
        self.assertGreater(len(data.get("features", [])), 0)
