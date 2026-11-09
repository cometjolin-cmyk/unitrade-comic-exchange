# 全國大學生二手物品交換與買賣平台 (UniTrade Campus)
### ⚡ 經典美式波普美漫風 (American Comic Pop) 旗艦全功能實裝版

[![Test Pass Rate](https://img.shields.io/badge/Tests-100%2F100%20Pass%20(100%25)-brightgreen.svg)](#自動化測試與驗證結果)
[![Features](https://img.shields.io/badge/Features-24%2F24%20Completed-blue.svg)](#完整-24-項功能架構)
[![Design Style](https://img.shields.io/badge/Style-American%20Comic%20Pop-red.svg)](#視覺設計系統-american-comic-pop)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

本專案為針對台灣大專院校學生所設計之**二手物品交換與買賣市集平台**。以使用者選定的**「經典美式波普美漫風（American Comic Pop / Boom!）」**作為旗艦核心設計，全數貫徹實作課綱與作業規範所要求的 **10 項入門功能**、**10 項中階功能** 與 **4 大 AI 智慧功能**，並附帶具備 100 組合成資料覆蓋率的自動化隔離測試套件。

---

## 📖 目錄 (Table of Contents)

1. [線上即時體驗 (Live Demo)](#-線上即時體驗-live-demo)
2. [視覺設計系統 (American Comic Pop)](#-視覺設計系統-american-comic-pop)
3. [完整 24 項功能架構](#-完整-24-項功能架構)
4. [專案目錄結構](#-專案目錄結構)
5. [自動化測試與驗證結果](#-自動化測試與驗證結果)
6. [本地執行與操作指南](#-本地執行與操作指南)
7. [GitHub Pages 部署說明](#-github-pages-部署說明)

---

## 🚀 線上即時體驗 (Live Demo)

- **展示中樞入口 (Showcase Portal)**：[`index.html`](index.html) — 具備桌機 / 平板 / 手機三重視窗切換與多風格對比。
- **美漫旗艦獨立頁 (American Comic Flagship)**：[`style2-american-comic.html`](style2-american-comic.html) — 完整功能沉浸式體驗。

---

## 🎨 視覺設計系統 (American Comic Pop)

依據 [UIUX.md](UIUX.md) 規範，本專案採用經典美式英雄漫畫風格（Pop-Art / Boom!）：
- **色彩計畫 (Color Palette)**：
  - 💥 戰隊電光黃 (`#FACC15`)：主視覺行動焦點與價格標籤。
  - 🥊 美漫鮮紅 (`#DC2626`)：標題裝飾、重要徽章與醒目警示。
  - 🦸 英雄英雄藍 (`#2563EB`)：對話框背景與鏈接重點。
  - ✒️ 粗獷墨線 (`#000000`)：3.5px 實心黑邊框與硬投影 (`comic-shadow: 4px 4px 0px #000`)。
- **漫畫元素**：
  - Ben-Day 點陣 Halftone 網點背景質感。
  - 尖尾對話框氣泡（Speech Bubbles）與鋸齒狀狀聲詞貼紙（BOOM! POW! BANG!）。
  - 標題採復古美漫字體 *Bangers* 搭配粗黑立體陰影。

---

## ⚡ 完整 24 項功能架構

詳細規格請參閱 [PRD.md](PRD.md)。

### 1. 入門功能 (10 項)
- **F01 商品卡片列表**：展示實體照片、價格徽章、學校標籤、物況評級與刊登時間。
- **F02 商品詳細頁彈窗**：大圖輪播、物品詳細規格、賣家信箱與指定面交地點。
- **F03 商品分類導覽**：必修教科書、3C 電子神裝、宿舍家具、免費結緣標籤即時切換。
- **F04 關鍵字多欄位搜尋**：支援品名、敘述、校名即時檢索；無符合項目時出示美漫 OOPS 空白狀態。
- **F05 價格區間篩選**：手動最低/最高價篩選與預算快捷鍵（500元內/2000元內），內建「最高價不可小於最低價」防呆阻擋。
- **F06 學校與地區基地**：支援全台各大基地切換（臺大、交大、清大、成大、政大、全校基地）。
- **F07 價格與時效排序**：價格由低至高、價格由高至低、最新上架商品排序。
- **F08 多元交易型態標籤**：標示「現金收購」、「以物換物」、「0元免費結緣」。
- **F09 願望收藏清單**：愛心星號一鍵加入/移除，透過 `localStorage` 進行跨頁面持久化儲存。
- **F10 行動裝置專屬優化**：手機專用底部懸浮導覽列（市集、AI、刊登、收藏、我的基地）。

### 2. 中階功能 (10 項)
- **F11 會員認證機制**：強制限制 `.edu.tw` 學校信箱註冊，提供登入、註冊與忘記密碼模擬。
- **F12 特工個人檔案與賣場**：個人基地抽屜展示認證標章、所屬系所、信譽星級與上架統計。
- **F13 商品刊登與多圖上傳**：完整規格填寫，限制最多 5 張照片且單檔 `<5MB`。
- **F14 商品生命週期管理**：賣家可動態切換商品狀態為「上架中」、「已預訂」、「交易完成」、「已下架」。
- **F15 以物易物提案系統**：提供交換物品填寫與補貼差額輸入表單。
- **F16 公開問答與個資防護**：留言板內建 Regex 自動遮蔽手機號碼（如 `0912-***-***`）與 Email，避免隱私外洩。
- **F17 歷史交易檔案庫**：完整歸檔個人已完成之購買與結緣贈送紀錄。
- **F18 站內戰情通知中心**：即時匯聚買家提問、降價提醒與系統通知，支援「一鍵全部標記為已讀」。
- **F19 違規檢舉與管理員後台**：前台提供檢舉表單；後台管理員可即時審查案件並執行「下架處分」或「駁回」。
- **F20 校園身分藍勾驗證**：通過認證之特工標註官方藍勾徽章；首頁提供「僅顯示認證賣家」安全過濾。

### 3. AI 智慧功能 (4 大項)
- **AI01 AI 拍照速估辨識**：模擬神經網絡視覺辨識書名與 ISBN，一鍵自動代入刊登欄位。
- **AI02 AI 二手合理行情估算**：輸入原購定價與物況評分（1~10），動態計算建議折舊售價並標註估算聲明。
- **AI03 AI 個人化裝備推薦**：依使用者瀏覽歷史與關注系所，於頂部橫幅智慧推薦關聯教材。
- **AI04 AI 導購特派員**：自然語言對話機器人，支援預算條件匹配（如「3000元內二手平板」）與校區面交推薦。

---

## 📁 專案目錄結構

```text
├── index.html                   # 展示中樞門戶 (支援 Responsive Viewport 切換)
├── style2-american-comic.html   # 【旗艦選定】經典美式波普美漫版全功能主程式
├── style1-mlp-magic.html        # 彩虹小馬夢幻風格備選頁
├── style3-y2k-candytoon.html    # 美式千禧卡通風格備選頁
├── PRD.md                       # 產品需求規格書 (24 項功能驗收標準)
├── UIUX.md                      # 美漫風格設計規範與 Design Tokens
├── .gitignore                   # Git 忽略設定
├── README.md                    # 專案說明與部署指南
└── tests/                       # 自動化測試套件
    ├── functional_matrix.json   # 24 項功能定義對照表
    ├── synthetic_dataset_100.json # 100 組合成測試資料集
    ├── generate_dataset.py      # 資料集產生器
    ├── run_isolated_tests.py    # 隔離測試執行器 (Headless DOM + JSC)
    ├── cleanup_tests.py         # 測試環境清理工具
    ├── test_report.json         # 測試執行 JSON 記錄
    └── TEST_REPORT.md           # 完整自動化測試驗證報告
```

---

## 🧪 自動化測試與驗證結果

專案內建專用 Headless 測試引擎，針對 24 項功能產生了 **100 組涵蓋不同情境之合成資料**：

- **正常情境 (Normal, 50 組)**：涵蓋基礎瀏覽、各校基地切換、分類、關鍵字、詳細頁、收藏、上架、問答與 4 大 AI。
- **邊界情境 (Boundary, 20 組)**：0 元物資、極限預算、單字檢索、首尾空格自動 Trim、剛好 5 張照片、超長標題防破版等。
- **錯誤情境 (Error, 20 組)**：最高價小於最低價警告、非 .edu.tw 信箱阻擋、電話與 Email 個資自動 Regex 遮蔽、表單必填防呆等。
- **權限情境 (Permission, 10 組)**：藍勾認證特工篩選、訪客身分限制、已下架商品隱藏、管理員後台仲裁處置等。

### 測試執行報告摘要
- **總測試案例數**：100 組
- **通過數**：100 組 ✅
- **失敗數**：0 組
- **通過率**：**100.0%**
- **未涵蓋功能**：0 項 (全數覆蓋)

詳細測試歷程請見 [tests/TEST_REPORT.md](tests/TEST_REPORT.md)。

---

## 💻 本地執行與操作指南

### 1. 開啟網頁
本專案為純靜態前端架構，無須複雜後端設定：
- 直接以瀏覽器開啟 `index.html` 或 `style2-american-comic.html` 即可完整體驗所有功能。

### 2. 執行自動化測試
在專案根目錄下執行：
```bash
python3 tests/run_isolated_tests.py
```

### 3. 清理測試資料
```bash
python3 tests/cleanup_tests.py
```

---

## 🌐 GitHub Pages 部署說明

本專案可以直接發布至 **GitHub Pages** 提供全球線上訪問：

1. 在 GitHub 上建立儲存庫（Repository），例如 `unitrade-comic-exchange`。
2. 將本專案推送至 GitHub 儲存庫：
   ```bash
   git remote add origin https://github.com/<您的GitHub帳號>/<您的儲存庫名稱>.git
   git branch -M main
   git push -u origin main
   ```
3. 進入 GitHub 儲存庫頁面：
   - 點擊 **Settings** -> **Pages**。
   - 在 **Build and deployment** 下方的 **Branch** 選擇 `main`，資料夾選擇 `/ (root)`。
   - 點擊 **Save**。
4. 等待約 1 分鐘，即可獲得線上公開網址：  
   `https://<您的GitHub帳號>.github.io/<您的儲存庫名稱>/`
