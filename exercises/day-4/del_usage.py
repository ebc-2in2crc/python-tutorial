# 問題:
# リスト [1, 2, 3, 4, 5] から2番目と3番目の要素を del を使って削除してください。


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    del numbers[1:3]
    print(numbers)
