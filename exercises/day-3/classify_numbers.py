# 問題: 整数を分類して出力する関数
#
# 問題文:
# 整数のリストを引数に取り、各整数が正の数・負の数・ゼロのいずれかに分類されるかを表示する関数 classify_numbers(numbers) を作成してください。
# for 文と if 文 を使ってください。
#
# 例:
# classify_numbers([3, -1, 0, 7])
#
# 出力:
# 3 は正の数です
# -1 は負の数です
# 0 はゼロです
# 7 は正の数です

def classify_numbers(numbers: list):
    for i in numbers:
        if i > 0:
            print(f"{i} は正の数です")
        elif i == 0:
            print(f"{i} はゼロです")
        else:
            print(f"{i} は負の数です")

if __name__ == '__main__':
    classify_numbers([3, -1, 0, 7])