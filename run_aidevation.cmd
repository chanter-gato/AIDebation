:<<"::CMDLITERAL"
@echo off
goto :WINDOWS_SCRIPT
::CMDLITERAL

# ==========================================
# 🍎 Mac / Linux 用
# ==========================================
cd "$(dirname "$0")"
# Pythonサーバーをバックグラウンドで起動
python3 python/api_bridge.py &

# フロントエンド用にも簡易ローカルサーバー（ポート8000）を起動してCORSエラーを回避
python3 -m http.server 8000 &

# 少し待機してサーバーが準備できるのを待つ
sleep 2

# file:// ではなく http://localhost:8000 でブラウザを開く
# ブラウザを開くためのフォールバック処理
if command -v xdg-open > /dev/null; then
  xdg-open http://localhost:8000/src/index.html
elif command -v open > /dev/null; then
  open http://localhost:8000/src/index.html
else
  # open/xdg-openがない場合、ブラウザの実行ファイルを直接指定（例: firefoxなど）
  # 必要に応じてここに環境ごとのパスを追記してください
  echo "ブラウザを開くコマンドが見つかりません。http://localhost:8000/src/index.html を手動で開いてください。"
fi
exit 0

:WINDOWS_SCRIPT
REM ==========================================
REM 🪟 Windows 用
REM ==========================================
chcp 65001 > nul
cd /d "%~dp0"
@echo off

echo [システム] バックエンド（Pythonサーバー）を起動中...
start "AIDevation Backend" python python/api_bridge.py

echo [システム] フロントエンド（画面配信用サーバー）を起動中...
REM フロントエンド用に簡易ローカルサーバー（ポート8000）を別窓で起動
start "AIDevation Frontend" python -m http.server 8000

echo [システム] ブラウザを立ち上げます...
timeout /t 3 > nul

REM file:// ではなく http://localhost:8000 でブラウザを開く
start http://localhost:8000/src/index.html

echo.
echo ===================================================
echo 🚀 準備完了です！ブラウザが自動で開きます。
echo 終了する時は、Pythonの黒い画面を閉じてください。
echo ===================================================
pause