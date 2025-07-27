# 問題:
# 3×3 の行列の転置を、ネストしたリスト内包表記で実装してください。


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    new_matrix = [[row[i] for row in matrix] for i in range(3)]
    print(new_matrix)
