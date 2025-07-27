# 問題:
# 1〜10 の整数の2乗をリスト内包表記で作成して出力してください。


if __name__ == '__main__':
    squares = [i ** 2 for i in range(1, 11)]
    print(squares)