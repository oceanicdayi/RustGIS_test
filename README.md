# RustGIS_test｜臺灣地震 GIS 探究教材

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oceanicdayi/RustGIS_test/blob/main/notebooks/earthquake_gis.ipynb)

適合大學地球科學、地球物理、通識與教師研習。建議 120 分鐘。無須學 Rust。
- [完整實作 Notebook](notebooks/earthquake_gis.ipynb)
- [教師手冊與 WebGIS 操作](docs/teaching.md)
- [技術研究筆記](docs/research.md)
- [合成地震資料](data/synthetic_earthquakes.geojson)
- [Python 自動化腳本](examples/earthquake_map.py)

## 快速開始
開啟上方 Colab，確認 Python >=3.12，依序執行。或本機：
```sh
python -m pip install -r requirements.txt
python examples/earthquake_map.py
```
也可直接開啟 https://web.rustgis.app 並匯入 data 下的 GeoJSON。
輸出在 outputs/。合成資料僅教學，不是實際地震或防災指引。
API 依據 [官方 Python 文件](https://github.com/opengeos/RustGIS/blob/main/docs/python.md)；本次未執行 RustGIS runtime，需在 Colab 或本機驗證。
