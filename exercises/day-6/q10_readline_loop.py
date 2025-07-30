# 問題：readline() を使ってファイルを1行ずつ読み込み、ループで出力してください

if __name__ == '__main__':
    with open("sample.txt") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            print(line, end="")