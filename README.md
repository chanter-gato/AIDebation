# AI Devation
My first project!

This is a prototype of a competitive system featuring AI agents and a judgment function.  
AIエージェントとジャッジ機能による対戦システムのプロトタイプです。  

<img width="1104" height="647" alt="image" src="https://github.com/user-attachments/assets/8951b21c-b173-4245-91a1-2720fd739492" />


## 🧬Concept／コンセプト・開発の背景
このプロジェクトは、「プロンプトエンジニアリングの技術向上を、より楽しく、より実践的にする」ことを目指して作られました。

既存のプリセットからAIを選ぶのではなく、ユーザー自身が設計した「AIのペルソナ（プロンプトや設定ファイル）」を持ち寄り、戦わせることができるのが最大のポイントです。  
自分で作ったプロンプトの強みや弱みを、バトルとジャッジのプロセスを通じて直感的に学ぶことができます。

This project was created with the aim of making the process of improving prompt engineering skills more enjoyable and practical.

The key feature is that, rather than simply selecting an AI from existing presets, **users can bring their own custom-designed "AI personas" (prompts and configuration files) and pit them against one another.**  
Through the process of battles and judging, you can intuitively learn the strengths and weaknesses of the prompts you have created.

<img width="1076" height="473" alt="image" src="https://github.com/user-attachments/assets/2ed6defd-c625-4026-94bf-9bafd8d8bcd8" />


## 🛠️ Prerequisites／前提条件  
このシステムをローカル環境で実行するには、以下の環境が必要です。  
To run this system in a local environment, the following environment is required:

- **Python 3.10+** (Pythonがインストールされている必要があります)
- **Gemini API Key** (Google AI Studio等から取得したAPIキーが必要です)  


## 🚀Future Plans／今後の構想
- **Implementation of 4-player battle mode／4人対戦モードの実装**:  
  Building an environment where up to four AI agents can compete against each other.  
  最大4人のAIエージェントがバトルできる環境の構築  

- **Creation of an intuitive UI／直感的なUIの作成**:  
  Setting up HTML screens in the `ui/` directory and enabling the replacement of persona configuration files via drag-and-drop.  
  `ui/` ディレクトリ配下にHTML画面を用意し、ペルソナ設定ファイルをドラッグ＆ドロップで差し替え可能にする  

- **Secure design／セキュアな設計**:  
  Loading configuration files (including API keys) into memory and excluding them from the repository.  
  APIキーを含む設定ファイルはメモリ読み込みとし、リポジトリには含めない  
