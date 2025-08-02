# グローバル変数 x と、クラス内のインスタンス変数 x を使って、それぞれの値を出力してください。

x = 1000

class MyClass:
    def __init__(self, x):
        self.x = x

if __name__ == '__main__':
    print("global:", x)
    my = MyClass(1)
    print("MyClass:", my.x)
