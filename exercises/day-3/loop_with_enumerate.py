# 問題:
# リスト ['a', 'b', 'c'] の各要素を、インデックス付きで出力してください（enumerate を使うこと）。


if __name__ == '__main__':
    l = ['a', 'b', 'c']

    for i, v in enumerate(l):
        print(f"[{i}]: {v}")
