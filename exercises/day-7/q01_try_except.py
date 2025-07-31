# 問題: 文字列を整数に変換するプログラムを書き、無効な入力には "無効な入力です" と表示するようにしてください。

if __name__ == '__main__':
    while True:
        try:
            s = input("input digit: ")
            n = int(s)
            print(f"inputted digit: {n}")
        except ValueError:
            print("無効な入力です")