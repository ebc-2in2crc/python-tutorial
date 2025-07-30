# 問題：上記の data.json を読み込み、内容を出力してください

import json

if __name__ == '__main__':
    with open("data.json", encoding="utf-8") as f:
        data = json.load(f)
        print(data)