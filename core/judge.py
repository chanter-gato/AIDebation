import json
import os
import time
from google import genai

class Judge:
    def __init__(self, json_path=None, fallback_key=None):
        # デフォルトのパスを設定
        if json_path is None:
            json_path = os.path.join("config", "judge", "judge.json")
            
        # JSONファイルの読み込み（存在しない場合はデフォルト値）
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "name": "ポワポワ審判",
                "persona": "公平にジャッジする審判。",
                "model": "models/gemini-3.1-flash-lite"
            }
        
        self.name = self.config.get("name")
        self.model = self.config.get("model", "models/gemini-3.1-flash-lite")
        
        # キーの優先順位: 1. JSONのキー -> 2. 環境変数 -> 3. mainから渡された予備キー
        self.api_key = self.config.get("api_key") or os.getenv("GOOGLE_API_KEY") or fallback_key

    def judge(self, history, topic="自由討論"):
        if not self.api_key:
            raise ValueError("エラー: 審判用のAPIキーが設定されていません。")

        client = genai.Client(api_key=self.api_key)
        debate_text = "\n".join(history)
        
        # JSONから読み込んだキャラクター付け（persona）をプロンプトに組み込む
        prompt = f"""討論テーマ: {topic}

あなたは「{self.name}」です。
キャラクター設定: {self.config.get('persona')}

上記の討論を客観的に判定し、どちらの論が勝っていたか、その勝者と理由を簡潔（200文字以内）に述べてください:

{debate_text}"""
        
        time.sleep(1)
        
        response = client.models.generate_content(
            model=self.model, 
            contents=prompt
        )
        return response.text