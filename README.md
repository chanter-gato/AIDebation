# AI Devation
My first project!  
This is a prototype of a competitive system featuring AI agents and a judgment function.  
> AIエージェントとジャッジ機能による対戦システムのプロトタイプです。  

<img width="1104" height="647" alt="image" src="https://github.com/user-attachments/assets/8951b21c-b173-4245-91a1-2720fd739492" />
<img width="1407" height="889" alt="image" src="https://github.com/user-attachments/assets/67c1029b-1606-4024-a82f-95fc354f309e" />



## 🧬Concept／コンセプト・開発の背景  
This project was created with the aim of making the process of improving prompt engineering skills more enjoyable and practical.  

The key feature is that, rather than simply selecting an AI from existing presets, **users can bring their own custom-designed "AI personas" (prompts and configuration files) and pit them against one another.**  
Through the process of battles and judging, you can intuitively learn the strengths and weaknesses of the prompts you have created.  

Rather than defining AI behavior solely in abstract terms, we conceptualize it by distinguishing between "victory conditions" (motivations) and "rules" (constraints) within the game.   
This approach enables precise control over prompt-driven behavior while prioritizing the design of unpredictable and engaging interactive experiences.  

>このプロジェクトは、「プロンプトエンジニアリングの技術向上を、より楽しく、より実践的にする」ことを目指して作られました。
>
>既存のプリセットからAIを選ぶのではなく、ユーザー自身が設計した「AIのペルソナ（プロンプトや設定ファイル）」を持ち寄り、戦わせることができるのが最大のポイントです。  
>自分で作ったプロンプトの強みや弱みを、バトルとジャッジのプロセスを通じて直感的に学ぶことができます。
> 
>AIの行動をただ抽象的に定義するのではなく、ゲームの「勝利条件（Motivation）」と「ルール（Constraints）」として分離することで、プロンプトの挙動を厳密にコントロールし、予測不可能な面白いラリー（議論）を生み出す設計にしています。
  
<img width="730" height="763" alt="image" src="https://github.com/user-attachments/assets/77133f9c-dd93-4cc2-bc50-c1bf4d4225df" />
<img width="1076" height="473" alt="image" src="https://github.com/user-attachments/assets/2ed6defd-c625-4026-94bf-9bafd8d8bcd8" />
  
How it works?  
  1. Setup: Leverage Gemini to rapidly generate personas with distinct personalities (in formats like JSON or YAML).
  2. Battle: AIs engage in a turn-based debate while adhering to set constraints (e.g., a 150-character limit).
  3. Judge: An independent judge AI objectively evaluates the logical structure and constraint compliance of both sides to determine the winner.
> 仕組みは?  
>  1. Setup: Geminiを活用し、尖った個性を持つペルソナ（JSON/YAML等）を爆速で生成。
>  2. Battle: 設定された制約（150文字以内など）を守りながら、AI同士が交互にターン制で議論。
>  3. Judge: 独立したジャッジAIが、両者の論理構成や制約違反の有無を客観的に評価して勝敗を判定。
  
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
