# 問題：テキストファイルを読み込み、行数と文字数を表示してください

if __name__ == '__main__':
    with open("sample.txt") as f:
        line_count = 0
        for line in f:
            line_count += 1

        f.seek(0)

        content = f.read()
        char_count = len(content)

        print(f"行数: {line_count}, 文字数: {char_count}")