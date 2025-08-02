# 名前マングリングを利用してプライベート変数 __secret を隠し、メソッドからのみアクセスできるようにしてください。

class MyClass:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        return self.__secret

if __name__ == '__main__':
    my = MyClass("秘密")
    print(my.get_secret())