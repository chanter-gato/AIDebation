import json
import time
import os
from google import genai
from google.genai.errors import ClientError

class Agent:
    def __init__(self, json_path, client=None, default_model='models/gemini-3.1-flash-lite'):
        with open(json_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        self.name = self.config.get("name", "名無しエージェント")

        # キーの優先順位: JSONのキー > 環境変数
        self.api_key = self.config.get("api_key") or os.getenv("GOOGLE_API_KEY")
        self.model = self.config.get("model") or default_model

        # クライアントの初期化（重複を整理）
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        elif client:
            self.client = client
        else:
            raise ValueError(f"エラー: '{self.name}' にAPIキーが設定されていません。")
        
        self.system_prompt = f"""
        あなたは {self.name} です。
        性格: {self.config.get('persona', '特になし')}
        専門分野: {', '.join(self.config.get('expertise', []))}
        行動動機: {self.config.get('motivation', '討論を楽しむこと')}
        制約事項: {self.config.get('constraints', '簡潔に話すこと')}

       【重要】
        回答は必ず日本語で、250文字以内でまとめてください。
        論点を明確にし、ダラダラと長く話さないこと。
        """

    def generate(self, prompt):
        full_prompt = f"{self.system_prompt}\n\n{prompt}"
        
        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=full_prompt
                )
                return response.text
            except ClientError as e:
                if e.code == 429:
                    print(f"\n[制限検知] 30秒休憩します... (試行 {attempt+1}/3)")
                    time.sleep(30)
                else:
                    raise e
        return "申し訳ありません、制限のため回答できませんでした。"