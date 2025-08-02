# ジェネレータ式を使って、文字列リストの各単語の長さを出力してください。

if __name__ == '__main__':
    words = ["Taro", "Bob", "Maria"]
    for word_length in (len(word) for word in words):
        print(word_length)