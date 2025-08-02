# インスタンスのメソッドオブジェクトを別の変数に代入し、その変数を通じてメソッドを呼び出してください。

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

if __name__ == '__main__':
    my = MyClass("Taro")
    my_greet = my.greet

    my_greet()

