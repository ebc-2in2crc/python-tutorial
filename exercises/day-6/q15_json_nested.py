# 問題：ネストした辞書を JSON として保存・読み込みして出力してください
import json

person = {
    "name": "花子",
    "scores": {"math": 90, "english": 85}
}

if __name__ == '__main__':
    with open("person.json", "w", encoding="utf-8") as f:
        json.dump(person, f)

    with open("person.json", "r", encoding="utf-8") as f:
        loaded_person = json.load(f)

    print(loaded_person)