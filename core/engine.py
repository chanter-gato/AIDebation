import random
import time
import sys

class DebateEngine:
    def __init__(self, agents):
        self.agents = agents
        self.history = []

    # AIがその場でタイプしているような演出用
    def slow_print(self, text, delay=0.08):
        # 句点で分割して、一つずつ表示する
        sentences = text.split('。')
        for i, sentence in enumerate(sentences):
            if not sentence:
                continue
            
            # 各文を1文字ずつ表示
            for char in sentence:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            
            # 文末に「。」をつけて一呼吸
            if i < len(sentences) - 1:
                sys.stdout.write("。\n")
                sys.stdout.flush()
                # 句点でのウェイト（ここを長くするとよりゆっくりになります）
                time.sleep(1.2) 
        print() # 最後に改行

    def run_debate(self, rounds=3, topic=""):
        print(f"\n=== 討論テーマ: {topic} ===\n")
        print("--- AIDevation Debate Start ---")

        for r in range(rounds):
            print(f"\n--- 第{r+1}ラウンド ---")
            order = list(range(len(self.agents)))
            random.shuffle(order)
            
            for i in order:
                agent = self.agents[i]

                # プロンプトにお題を明示的に含める
                # エージェントに自分の役割を意識させるプロンプトに進化
                prompt = f"お題: {topic}\n\nあなたは{agent.name}です。以下の議論の流れを読んで、説得力のある発言をしてください。\n\nこれまでの議論:\n{' '.join(self.history)}\n\nあなたの発言:"
                
                # エラー対策（generateが使えない場合を考慮）
                try:
                    response = agent.generate(prompt)
                except AttributeError:
                    response = "（準備中...）"
                
                self.slow_print(f"[{agent.name}]: {response}")
                self.history.append(f"{agent.name}: {response}")
                time.sleep(1.0)

