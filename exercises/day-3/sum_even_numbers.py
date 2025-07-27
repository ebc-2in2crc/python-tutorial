# 問題: 偶数の合計を求める関数
#
# 問題文:
# 整数のリストを受け取り、その中の偶数だけを足し合わせた合計を返す関数 sum_even_numbers(numbers) を定義してください。
#
# 使い方の例:
# sum_even_numbers([1, 2, 3, 4, 5, 6]) → 12  # 2 + 4 + 6

def sum_even_numbers(numbers: list):
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += i
    return result

if __name__ == '__main__':
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))