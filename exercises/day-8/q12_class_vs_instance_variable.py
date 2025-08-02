# クラス変数とインスタンス変数が衝突しないように使い分ける例を示してください。

class MyClass:
    value = "class"

    def __init__(self, value):
        self.value = value

    def print(self):
        print(f"class value: {MyClass.value}")
        print(f"instance value: {self.value}")

if __name__ == '__main__':
    my = MyClass("instance")
    my.print()