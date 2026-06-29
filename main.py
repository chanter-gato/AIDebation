import json
import os
import webbrowser  # ブラウザ起動用from google import genai
from core.engine import DebateEngine
from core.judge import Judge
from core.agent import Agent

if __name__ == "__main__":
    # 1. 設定ファイルの読み込み
    config_path = os.path.join("config", "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    # 2. 環境変数をバックアップとして取得
    env_api_key = os.getenv("GOOGLE_API_KEY")

    # 3. エージェントの作成
    agents = []
    agent_dir = os.path.join("config", "agents")
    for filename in os.listdir(agent_dir):
        if filename.endswith(".json") and "player" in filename:
            path = os.path.join(agent_dir, filename)
            agents.append(Agent(path, client=None))

    # 4. キーチェック
    for agent in agents:
        if not agent.api_key and not env_api_key:
            print(f"エラー: エージェント '{agent.name}' に有効なAPIキーがありません。JSONまたは環境変数 GOOGLE_API_KEY を確認してください。")
            exit(1)

    # 5. 討論実行
    debate_topic = config.get("debate_topic", "自由討論")
    rounds = config.get("rounds", 1)
    
    engine = DebateEngine(agents)
    engine.run_debate(rounds=rounds, topic=debate_topic)
    
    # 6. 判定
    fallback_key = env_api_key or (agents[0].api_key if agents else None)
    judge = Judge(fallback_key=fallback_key) 
    result = judge.judge(engine.history, topic=debate_topic)
    
    print(f"\n--- Result ---\n{result}")

    # 7. ✨ HTMLレポートの生成とブラウザ表示処理（ここを追加！）
    html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>AIDevation 討論結果レポート</title>
    <style>
        body {{ font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', sans-serif; background-color: #f5f7f8; color: #333; margin: 0; padding: 30px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
        h1 {{ color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 15px; margin-top: 0; }}
        h2 {{ color: #2980b9; margin-top: 40px; border-left: 5px solid #2980b9; padding-left: 10px; }}
        .topic {{ background: #ebf5fb; padding: 20px; border-left: 5px solid #3498db; font-weight: bold; font-size: 1.2em; margin-bottom: 30px; border-radius: 4px; }}
        .chat-log {{ display: flex; flex-direction: column; gap: 20px; }}
        .message {{ padding: 18px; border-radius: 8px; max-width: 85%; line-height: 1.6; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }}
        .message.player {{ background-color: #f8f9fa; align-self: flex-start; border-top-left-radius: 0; border-left: 4px solid #bdc3c7; }}
        /* 経済学者と詩人で少し色分けを転換させたい場合のベース */
        .name {{ font-weight: bold; margin-bottom: 8px; color: #34495e; font-size: 0.95em; }}
        .message.judge {{ background-color: #fff9f2; align-self: center; border: 1px solid #f39c12; border-left: 5px solid #e67e22; max-width: 100%; width: 100%; box-sizing: border-box; }}
        .result-box {{ white-space: pre-wrap; font-size: 1.05em; color: #d35400; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>⚖️ AIDevation 討論結果レポート</h1>
        <div class="topic">討論テーマ: {debate_topic}</div>
        
        <h2>💬 討論ログ</h2>
        <div class="chat-log">
"""

    # 履歴から発言者と内容を分解してHTMLに埋め込む
    for log in engine.history:
        if ":" in log:
            name, text = log.split(":", 1)
            html_content += f"""
            <div class="message player">
                <div class="name">👤 {name.strip()}</div>
                <div>{text.strip()}</div>
            </div>"""

    html_content += f"""
        </div>
        
        <h2>⚖️ 審判のジャッジ</h2>
        <div class="message judge">
            <div class="name">👑 {judge.name} （判定員）</div>
            <div class="result-box">{result}</div>
        </div>
    </div>
</body>
</html>
"""

    from datetime import datetime
    from pathlib import Path

    # 保存用のフォルダを指定して、なければ自動生成する
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)

    # プロジェクトのルートディレクトリに「result.html」として保存
    # 現在日時を取得してファイル名に付加する（例: result_20260627_223500.html）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"result_{timestamp}.html"

    # フォルダの中に保存されるようにパスを結合
    output_filename = os.path.join(output_dir, f"result_{timestamp}.html")

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"\n[システム] 討論結果を {output_filename} に保存しました。")
    
    # 保存したHTMLファイルをブラウザで自動的に開く(日時がついた最新のHTMLファイルを開く)
    file_uri = Path(output_filename).resolve().as_uri()
    webbrowser.open(file_uri)