# ⚡AI DEBATION⚡

A prototype of a prompt engineering battle system.  
プロンプトエンジニアリング・バトルシステムのプロトタイプ。  

<img width="495" height="507" alt="image" src="https://github.com/user-attachments/assets/74801b66-6660-4176-bf2e-e6a0d3e9ba28" />

## 🧬Concept／コンセプト・開発の背景🧬  
This project was created with the aim of making the process of improving prompt engineering skills more enjoyable and practical.  
このプロジェクトは、プロンプトエンジニアリングのスキルを向上させるプロセスを、より楽しく実践的なものにすることを目指して作成されました。

Its standout feature is the ability for users to bring their own AI personas—created using prompts or configuration files—and pit them against one another.  
Created personas can also be exported in JSON format and shared.  
最大の特徴は、ユーザー自身が設計した「AIのペルソナ（プロンプト・設定ファイル）」を持ち寄って戦わせることができる点です。  
作成したペルソナはJSON形式で出力して交換することもできます。  

<img width="1000" height="471" alt="image" src="https://github.com/user-attachments/assets/eb4bdd8c-dea4-4e30-84da-3f588b5a3fa6" />


  
## 🛠️ Prerequisites／前提条件  
このシステムをローカル環境で実行するには、以下の環境が必要です。  
To run this system in a local environment, the following environment is required:

- **Python 3.10+** (Pythonがインストールされている必要があります)
- **Gemini API Key** (Google AI Studio等から取得したAPIキーが必要です)

### Installation／インストール
必要なライブラリをインストールします：

```bash
pip install flask flask-cors google-generativeai
```


## 🚀Future Plans／今後の構想
- **Creation of an intuitive UI／直感的なUIの作成**:  
  Easily swap persona configuration files using intuitive drag-and-drop.  
  ペルソナ設定ファイルをドラッグ＆ドロップで差し替え可能にする  

- **Support for Multiple AI Models／AIモデルの切り替え対応** :
  Implementation of a feature that allows users to freely switch between multiple LLMs—such as Gemini, Claude, and Sakana AI—and pit them against each other in a "battle."  
  Geminiだけでなく、ClaudeやSakana AIなど、複数のLLMを自由に切り替えてバトルさせる機能の実装。

- Persona Sharing & Community／ペルソナの共有とコミュニティ化 :  
  Enhance the functionality to easily export and import personas in JSON format.
  Our goal is to build a "Prompt Battle Platform" where users can share their strongest personas and pit them against each other in the arena.  
  設計したペルソナをJSON形式で簡単にエクスポート・インポートできる機能を強化。  
  将来的には、ユーザー同士が作成した最強のペルソナを共有し、アリーナで戦わせる「プロンプト対戦プラットフォーム」の構築。  
