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

# 【修正】フロントエンド用にも簡易ローカルサーバー（ポート8000）を起動してCORSエラーを回避
python3 -m http.server 8000 &

# 少し待機してサーバーが準備できるのを待つ
sleep 2

# 【修正】file:// ではなく http://localhost:8000 でブラウザを開く
open http://localhost:8000/index.html
exit 0

:WINDOWS_SCRIPT
REM ==========================================
REM 🪟 Windows 用
REM ==========================================
cd /d "%~dp0"
@echo off

echo [システム] バックエンド（Pythonサーバー）を起動中...
start "AIDevation Backend" python api_bridge.py

echo [システム] フロントエンド（画面配信用サーバー）を起動中...
REM 【修正】フロントエンド用に簡易ローカルサーバー（ポート8000）を別窓で起動
start "AIDevation Frontend" python -m http.server 8000

echo [システム] ブラウザを立ち上げます...
timeout /t 3 > nul

REM 【修正】file:// ではなく http://localhost:8000 でブラウザを開く
start http://localhost:8000/index.html

echo.
echo ===================================================
echo 🚀 準備完了です！ブラウザが自動で開きます。
echo 終了する時は、Pythonの黒い画面を閉じてください。
echo ===================================================
pause