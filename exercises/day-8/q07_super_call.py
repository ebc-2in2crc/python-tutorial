# 親クラスのメソッドを super() を使って呼び出してください。

class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

class Dog(Animal):
    def greet(self):
        super().greet()
        print("Woof!")

if __name__ == '__main__':
    dog = Dog("Taro")
    dog.greet()
