# 動作確認

## 事前準備

### 1. 仮想環境の作成

```bash
# プロジェクトルートで実行
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### 2. パッケージのインストール

```bash
$ python -m pip install -U pip
$ python -m pip install -r requirements-llmapp.txt
```

### 3. 設定ファイルのコピー

```bash
$ cp .env.example .env
$ code .env
```

`.env` には以下を設定する。

```
API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

※ 本課題では Web検索機能を使用するため `TAVILY_API_KEY` が必要です。

## 実行方法

1. app.pyを実行する。
2. http://127.0.0.1:5000/ にアクセスする。