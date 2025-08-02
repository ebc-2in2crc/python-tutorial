# Animal クラスを継承する Dog クラスを作り、"Woof!" と鳴くメソッドを追加してください。

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name}: Woof!")


if __name__ == '__main__':
    dog = Dog("Taro")
    dog.bark()