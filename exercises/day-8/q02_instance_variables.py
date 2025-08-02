# インスタンス変数 name を持ち、"Hello, <name>!" を表示するクラスを作成してください。

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

if __name__ == '__main__':
    my = MyClass("Taro")
    my.greet()