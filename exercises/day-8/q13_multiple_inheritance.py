# 多重継承で、Flyable と Swimmable を継承する Duck クラスを作成し、それぞれのメソッドを呼び出してください。

class Flyable:
    def fly(self):
        print("I can fly!")

class Swimmable:
    def swim(self):
        print("I can swim!")

class Duck(Flyable, Swimmable):
    """"""

if __name__ == '__main__':
    duck = Duck()
    duck.fly()
    duck.swim()
