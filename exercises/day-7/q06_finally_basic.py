# 問題: finally 節を使って、例外の有無に関係なく "終了処理中..." を表示してください。

if __name__ == '__main__':
    try:
        n = int(input("input digit: "))
        print(f"inputted digit: {n}")
    except ValueError:
        raise
    finally:
        print("終了処理中...")