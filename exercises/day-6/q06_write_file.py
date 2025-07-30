# 問題：sample.txt というファイルに「Hello, world!」と書き込んでください

if __name__ == '__main__':
    with open("sample.txt", "w") as f:
         f.write("Hello, world!")