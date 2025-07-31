# 問題: Exception を継承したユーザー定義例外 MyError を作成し、特定条件で送出してください。

class MyError(Exception):
    pass

if __name__ == '__main__':
    raise MyError("何かエラーが起きた")