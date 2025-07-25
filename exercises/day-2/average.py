# 問題: 可変長引数で平均を求める関数
#
# 問題文:
# 複数の数値を受け取り、それらの平均を返す関数 average(*args) を定義してください。受け取る数値の数は任意とします。
#
# 例:
# average(10, 20, 30) → 20.0
# average(5, 15) → 10.0

def average(*args):
    # 入力がない場合は None を返す
    if len(args) == 0:
        return None

    total = 0
    length = 0

    for i in args:
        total += i
        length += 1

    return total / length

if __name__ == '__main__':
    print(average(10, 20, 30))
    print(average(5, 15))