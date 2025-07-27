# 内容：以下の操作を1つのスクリプトで行ってください。
#
# モジュールを作成し関数を定義
#
# import の別名使用
#
# if __name__ == "__main__" 判定
#
# dir() 関数で属性確認
#
# モジュール検索パス確認

import sys

# import の別名利用
import composite_exercise_1 as my_mod_1


def greet(name: str):
    print(f"Hello, {name}")

if __name__ == '__main__':
    # __main__ 判定
    print("main?: ", __name__ == '__main__')

    # import の別名利用
    my_mod_1.greet("alias import")

    # dir() 関数で属性確認
    print(dir(my_mod_1))

    # モジュール検索パス確認
    print(sys.path)
