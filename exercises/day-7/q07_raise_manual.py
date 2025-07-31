# 問題: 入力値が負の数なら ValueError を送出する関数を定義してください。

if __name__ == '__main__':
    try:
        n = int(input("input digit: "))
        if n < 0:
            raise ValueError("input digit: must be positive")
        print(f"inputted digit: {n}")
    except ValueError:
        raise
