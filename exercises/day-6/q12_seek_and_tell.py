# 問題：ファイル内の現在位置を表示し、読み込み位置を先頭に戻して再度出力してください

if __name__ == '__main__':
    with open("sample.txt") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
                
            print(f"line: {line}, pos: {f.tell()}")

        f.seek(0)
        print(f.read())