# 問題:
# リストを使ってスタック（後入れ先出し）を実装してください。
# 3つの要素を push し、1つ pop した結果のスタックを表示してください

if __name__ == '__main__':
    stack = []

    # 要素を push
    stack.append('apple')
    stack.append('banana')
    stack.append('cherry')

    # 要素を pop
    stack.pop()

    # 結果を表示
    print(stack)  # ['apple', 'banana']
