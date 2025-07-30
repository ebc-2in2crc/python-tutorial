# 問題：上の sample.txt を読み込んで内容を出力してください

if __name__ == '__main__':
    with open("sample.txt", "r") as f:
        content = f.read()
    print(content)