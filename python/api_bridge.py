from flask import Flask, request, jsonify
from flask_cors import CORS  # 追加
import requests

app = Flask(__name__)
CORS(app)  # 全てのドメインからのリクエストを許可（開発用）

@app.route('/generate', methods=['POST'])
def generate():
    # JavaScriptから送られてくるキーとプロンプトを受け取る
    data = request.json
    api_key = data.get('api_key')
    system_prompt = data.get('system_prompt')
    user_prompt = data.get('user_prompt')

    # Geminiへのリクエスト
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
    payload = {
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"parts": [{"text": user_prompt}]}]
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            return jsonify({"error": response.text}), response.status_code
            
        res_data = response.json()
        reply = res_data['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)