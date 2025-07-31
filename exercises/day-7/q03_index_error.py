# 問題: リストの要素にインデックス指定でアクセスします。範囲外アクセスに対してエラーをキャッチしてください。

if __name__ == '__main__':
    my_list = [1, 2, 3]
    try:
        v = my_list[len(my_list)] # 例外が発生するはず
    except IndexError:
        print("範囲外アクセスが発生しました")
        raise