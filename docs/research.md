# RustGIS 技術研究
查閱日期 2026-11-26。來源：[README](https://github.com/opengeos/RustGIS/blob/main/README.md)、[Python](https://github.com/opengeos/RustGIS/blob/main/docs/python.md)、[分析](https://github.com/opengeos/RustGIS/blob/main/docs/user-guide/analysis.md)、[MCP](https://github.com/opengeos/RustGIS/blob/main/docs/mcp.md)。
## 架構與選型
Rust workspace 分為 apps 與 crates；桌面、WebAssembly 與 Python 共用引擎能力，但 UI 與外部工具支援不同。命令 ID 是 UI、CLI、Python 與 AI 的共同介面。Python 3.12+，Session 為 headless；Map 為網路載入的 Jupyter widget，與 Session 雙向同步。小型可嵌入資料適合課堂；官方指出 Map 支援最多 2 MiB 的可嵌入檔案，較大資料可能只在 Python 渲染。
## 與現有工作比較
QGIS 適合成熟桌面生態與外掛；PyGMT 適合出版級地球科學圖件；RustGIS 值得試驗於瀏覽器教學與 agent 自動化。尚未做速度、精度或穩定性基準測試，不能宣稱較快或可替代現有營運系統。
## 驗證清單
以同一 GeoJSON 比較事件數、CRS、buffer 面積、輸出圖、跨平台可重現性；在北緯 24 度不能把度直接視為公里。使用合適投影或經驗證的測地距離。查 Session.describe 和 notices；固定經測試的套件版本後再正式授課。
AI：先用 commands/describe 確認命令，再執行。不要把 API keys 或非公開地震資料交給外部模型；web app 的 key 儲存方式需注意。MCP 可由官方 rustgis-cli mcp 接入，但本教材沒有部署 MCP。
上游 Apache-2.0；本教材為獨立撰寫，未複製上游程式檔。
