# AI Agent GIS 教學（90 分鐘）
1. 10 分鐘：提出自然語言問題，預測結果。
2. 15 分鐘：replay 模式觀察結構化計畫，核對 UTC、規模與深度門檻。
3. 20 分鐘：核准後執行 USGS 查詢、RustGIS Select、Buffer、Render。
4. 20 分鐘：比較事件 ID 集合及環域近似半徑驗證；未通過不得聲稱正確。
5. 15 分鐘：live 模式改變問題（需 OpenAI API Key 與模型權限），比較兩次結果。
6. 10 分鐘：CER 報告與成果 ZIP。評量：問題與規劃 25%、資料正確 25%、驗證 30%、推理 20%。

## 原生 MCP 進階路線
安裝官方 CLI 後，以 Codex 為例：
```sh
codex mcp add rustgis -- rustgis-cli mcp --sample
```
提示：請先列出 Cities 欄位，選出人口大於一千萬的城市，建立 50 km buffer 並核對事件數。
本機資料可用官方 `rustgis-cli mcp --data /absolute/path/data.geojson` 初始化；不要預設開啟 --yes 或 Full access。MCP 客戶端提供模型，RustGIS 不需額外模型金鑰。官方文件：https://github.com/opengeos/RustGIS/blob/main/docs/mcp.md
本教材未安裝或測試 MCP，也未執行 Colab。Notebook 使用受限的 LLM 規劃器與固定工具，不是原生 MCP。
