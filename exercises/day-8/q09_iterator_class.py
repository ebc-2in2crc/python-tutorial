# 0 から n-1 までを順に返すイテレータクラスを作成してください。

class MyClass:
    def __init__(self, max_number):
        self.max = max_number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration

        result = self.current
        self.current += 1
        return result

if __name__ == '__main__':
    my = MyClass(5)
    for i in my:
        print(i)