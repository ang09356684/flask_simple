# Flask 專案

這是一個使用 Flask 框架建立的專案模板，採用應用程式工廠模式和清晰的架構分離。

## 專案結構

```
flask-project/
│  app.py               # 程式啟動點；載入與註冊各 blueprint
│  config.py            # 配置設定（所有參數直接寫在 Config 類別中）
│  pyproject.toml       # uv 相依管理
│  README.md
│  .gitignore
│
├─app/
│  ├─__init__.py        # 應用程式工廠模式
│  ├─api/               # API 路由；每個檔案就是一個 blueprint
│  │  ├─__init__.py
│  │  └─api_v1.py       # Blueprint: /api/v1
│  │
│  ├─dao/               # 資料存取層（DB I/O）
│  │  └─__init__.py
│  │
│  └─model/             # ORM models / schema
│     └─__init__.py
```

## 安裝與執行

### 使用 uv 安裝依賴

```bash
# 安裝 uv (如果尚未安裝)
pip install uv

# 安裝專案依賴
uv sync

# 安裝開發依賴
uv sync --extra dev
```

### 啟動應用程式

#### 開發環境
```bash
uv run python app.py
```

#### 生產環境 (Windows)
```bash
uv run waitress-serve --host=0.0.0.0 --port=5000 app:app
```

#### 生產環境 (Linux)
```bash
uv run gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API 端點

- `GET /api/v1/health` - 健康檢查端點

## 配置

所有配置參數都在 `config.py` 中定義，支援多種環境：
- `development` - 開發環境
- `production` - 生產環境  
- `testing` - 測試環境

注意：此專案不包含資料庫功能，專注於 API 服務。

## 日誌

應用程式會自動記錄所有 HTTP 請求與回應，包含：
- 請求方法、路徑、參數
- 表單資料和 JSON 資料
- 回應狀態碼和資料

## 開發

### 程式碼格式化
```bash
uv run black .
```

### 程式碼檢查
```bash
uv run flake8 .
```

### 執行測試
```bash
uv run pytest
```
