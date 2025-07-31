# 問題: 一つの except 節で複数の例外型を処理してください。

def my_func(num: int):
    if num == 0:
        raise ValueError("0 はだめ")
    if num == 1:
        raise RuntimeError("1 はだめ")
    return num ** 2

if __name__ == '__main__':
    for i in range(3):
        try:
            print(f"{i} => {my_func(i)}")
        except (ValueError, RuntimeError) as e:
            print(f"例外が発生した: {e}")
