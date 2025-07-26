# 問題:
# 辞書 {'apple': 100, 'banana': 80} をループで key と value を出力してください。


if __name__ == '__main__':
    fruits = {'apple': 100, 'banana': 80}

    for k, v in fruits.items():
        print(f"{k}: {v}")