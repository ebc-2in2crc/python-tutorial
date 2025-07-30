# 問題：sample.txt の全行を1行ずつ読み込んで出力してください

if __name__ == '__main__':
    with open("sample.txt") as f:
        for line in f:
            print(line, end="")