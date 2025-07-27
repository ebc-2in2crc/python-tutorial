# 問題:
#
# 辞書 {"a": 1, "b": 2, "c": 3} を作成。
#
# del 文で "b" を削除。
#
# 残りのキーと値を enumerate() で番号付きで出力。
#
# タプル (10, 20) を x, y にアンパック。
#
# x と y の値が == と is で等しいかを比較。


if __name__ == '__main__':
    # 辞書 {"a": 1, "b": 2, "c": 3} を作成。
    my_dict = {"a": 1, "b": 2, "c": 3}

    # del 文で "b" を削除。
    del my_dict["b"]

    # 残りのキーと値を enumerate() で番号付きで出力。
    for i, (k, v) in enumerate(my_dict.items()):
        print(i, k, v)

    # タプル (10, 20) を x, y にアンパック。
    x, y = (10, 20)

    # x と y の値が == と is で等しいかを比較。
    print("x == y:", x == y)
    print("x is y:", x is y)