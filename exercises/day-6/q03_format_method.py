# 問題：format() メソッドを使って「x=10, y=20」という文字列を出力してください

if __name__ == '__main__':
    x = 10
    y = 20

    s = "x=10, y=20".format(x, y)
    print(s)