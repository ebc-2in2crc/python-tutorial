# クラス変数 species = "Human" を持ち、
# インスタンス変数 name を使って "<name> is a Human" と表示するクラスを作成してください。

class MyName:
    species = "Human"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"{self.name} is a {MyName.species}")

if __name__ == '__main__':
    my = MyName("Taro")
    my.greet()
