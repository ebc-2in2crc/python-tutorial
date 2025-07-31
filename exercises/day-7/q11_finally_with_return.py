# 問題: finally 節が return を上書きしないことを確認してください。

def my_func(num: int):
    try:
        if num < 0:
            raise ValueError("num は 0 以上でなければならない")
        return num ** 2
    except RuntimeError:
        raise
    finally:
        print("my_func finished")

if __name__ == '__main__':
    n = int(input("input digit: "))
    print(my_func(n))
