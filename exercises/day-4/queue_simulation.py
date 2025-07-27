# 問題:
# リストを使ってキュー（先入れ先出し）を実装してください。
# 3つの要素を enqueue し、1つ dequeue した結果のキューを表示してください

if __name__ == '__main__':
    queue = []

    # 要素を enqueue
    queue.append(1)
    queue.append(2)
    queue.append(3)

    # 要素を dequeue
    queue.pop(0)

    # 結果を表示
    print(queue)