# 問題：sample.txt に新たに「Python入門」と追記してください（追記モード）

if __name__ == '__main__':
    with open("sample.txt", "a") as f:
        f.write("\nPython入門")