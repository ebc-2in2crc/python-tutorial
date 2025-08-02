# ジェネレータ関数を使って、0 から n-1 までを順に返してください。

def gen(max_number):
    for i in range(max_number):
        yield i

if __name__ == '__main__':
    for num in gen(5):
        print(num)