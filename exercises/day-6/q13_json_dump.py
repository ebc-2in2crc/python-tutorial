# 問題：辞書データを JSON 形式で保存してください

import json

data = {"name": "太郎", "age": 30, "score": 95}

if __name__ == '__main__':
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f)