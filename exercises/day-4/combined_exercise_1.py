# 問題:
# 以下のステップでデータを処理してください：
#
# 空のキューに "apple", "banana", "cherry" を追加し、先頭から1つ削除。
#
# 残りの要素に対し、文字数が偶数のものだけをリスト内包表記で抽出。
#
# そのリストを集合に変換し、{"banana", "grape"} との積集合を出力。


if __name__ == '__main__':
    # 空のキューに "apple", "banana", "cherry" を追加し、先頭から1つ削除。
    queue = []
    queue.append("apple")
    queue.append("banana")
    queue.append("cherry")
    queue.pop(0)

    # 残りの要素に対し、文字数が偶数のものだけをリスト内包表記で抽出。
    filtered = [n for n in queue if len(n) % 2 == 0]

    # そのリストを集合に変換し、{"banana", "grape"} との積集合を出力。
    print(set(filtered) & {"banana", "grape"})
