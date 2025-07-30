# 問題：リストに入っている文字列を、1行ずつファイルに書き込んでください
lines = ["apple", "banana", "cherry"]

if __name__ == '__main__':
    with open("fruits.txt", "w") as f:
        for line in lines:
            f.write(f"{line}\n")