# 問題: ネストされた try 文の中で例外を送出し、外側で処理する構文を作成してください。

if __name__ == '__main__':
    try:
        try:
            raise ValueError("なにか値エラー")
        except ValueError as e:
            raise
    except ValueError as e:
        print(f"外側: ValueError: {e}")