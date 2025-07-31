# 問題: 文字列を整数に変換して0で割る処理を行います。ValueError と ZeroDivisionError を個別に処理してください。

if __name__ == '__main__':
    try:
        n1 = int(input("割られる数を入力してください: "))
        n2 = int(input("割る数を入力してください: "))
        print(f"{n1} / {n2} = {n1 / n2}")
    except ValueError:
        print("ValueError が発生しました")
        raise
    except ZeroDivisionError:
        print("ZeroDivisionError が発生しました")
        raise
