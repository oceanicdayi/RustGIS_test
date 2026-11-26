"""Run from repository root; synthetic data only."""
from pathlib import Path
import rustgis

root = Path(__file__).resolve().parents[1]
out = root / "outputs"
out.mkdir(exist_ok=True)
s = rustgis.Session()
q = s.add_geojson(str(root / "data/synthetic_earthquakes.geojson"), name="Synthetic earthquakes")
assert q.count == 6
q.style("proportional", field="mag")
s.zoom_to(q)
s.to_png(str(out / "earthquakes.png"), width=1200, height=800)
print(s.describe("buffer"))
b = s.run_tool("buffer", input=q, distance=50, units="Kilometers")
b.set_transparency(65)
s.zoom_to(b)
s.to_png(str(out / "buffer.png"), width=1200, height=800)
s.save(str(out / "earthquakes.rgis"))
print(out)
