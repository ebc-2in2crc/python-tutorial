# 問題: ラムダ式で数値リストを2倍にする
#
# 問題文:
# map() 関数とラムダ式を使って、整数リスト内のすべての要素を2倍にしたリストを返す関数 double_list(numbers) を作ってください。
# map() 関数は、リストの各要素に関数を適用するために使います。
# 使い方は次のようになります。
#
# たとえば、リスト内のすべての要素を2倍にする場合:
# list(map(lambda x: x * 2, [1, 2, 3])) → [2, 4, 6]
#
# 例:
# double_list([1, 2, 3]) → [2, 4, 6]

def double_list(numbers: list):
    return list(map(lambda x: x * 2, numbers))

if __name__ == '__main__':
    print(double_list([1, 2, 3]))