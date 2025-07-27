# 問題:
# 2つの集合 {1, 2, 3} と {3, 4, 5} の和・積・差を求めて出力してください。


if __name__ == '__main__':
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    print(set1 | set2)
    print(set1 & set2)
    print(set1 - set2)