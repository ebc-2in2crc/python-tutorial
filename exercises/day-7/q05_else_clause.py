# 問題: try 節の後に else 節を使って、例外が発生しなかった場合に "成功しました" と表示してください。

if __name__ == '__main__':
    try:
        n = int(input("input digit: "))
    except ValueError:
        raise
    else:
        print("成功しました")
