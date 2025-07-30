# 7. 入力と出力

## 7.1. 出力を見やすくフォーマットする

- 標準出力を表すファイルは `sys.stdout` で参照できる
- 出力をフォーマットする方法
    - f-strings
    - `文字列の str.format()` メソッド
    - 文字列のスライス操作や結合操作を使い、全ての文字列を自分で処理する方法

```python
year = 2016
event = 'Referendum'

# f-strings
print(f'Results of the {year} {event}')           # Results of the 2016 Referendum

# str.format
print('Results of the {} {}'.format(year, event)) # Results of the 2016 Referendum
```

デバッグ目的で変数をすばやく表示したいときは `repr()`, `str()` 関数が使える。
`str()` 関数は値の人間に読める表現を返す。
`repr()` 関数はインタープリタに読める (あるいは同値となる構文がない場合は必ず SyntaxError になるような) 表現を返すためのもの。
数値やリスト、辞書を始めとするデータ構造など、多くの値がどちらの関数に対しても同じ表現を返す。
一方、文字列は、2つの異なる表現を持っている。

```python
hello = 'hello, world\n'

print(hello)       # hello, world (改行が続く)
print(str(hello))  # 'hello, world\n'
print(repr(hello)) # "'hello, world\\n'"
```

## 7.1.1. フォーマット済み文字列リテラル

- フォーマット済み文字リテラル。 短くして f-string とも呼ぶ
- 文字列の頭に `f` か `F` を付け、式を `{expression}` と書くことで、 Python の式の値を文字列の中に入れ込める
- オプションのフォーマット指定子を使って値のフォーマット方式を制御できる

```python
import math

print(f'The value of pi is approximately {math.pi:.3f}.') # The value of pi is approximately 3.142.
print(f'The value of pi is approximately {math.pi:.0f}.') # The value of pi is approximately 3.


# ':' の後ろに整数をつけると、そのフィールドの最小の文字幅を指定できる
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}') # Sjoerd     ==>       4127
                                        # Jack       ==>       4098
                                        # Dcab       ==>       7678

# = 指定子を使用すると式を展開して、`<式>=<式を評価した文字列表現>` の形式で表示される
greeting="good morning!"
print(f"{greeting=}") # greeting='good morning!'
```

## 7.1.2. 文字列の format() メソッド

```python
# 基本的な使い方
s = 'We are the {} who say "{}!"'.format('knights', 'Ni')
print(s) # We are the knights who say "Ni!"

# 括弧の中の数字で、str.format メソッドに渡されたオブジェクトの位置を指定できる
s = 'We are the {1} who say "{0}!"'.format('knights', 'Ni')
print(s) # We are the Ni who say "knights!

# str.format() メソッドにキーワード引数が渡された場合、キーワード引数の名前によって参照できる
# 順序引数とキーワード引数を組み合わせて使うこともできる
s = 'We are the {k} who say "{ni}!"'.format(k='knights', ni='Ni')
print(s) # We are the knights who say "Ni!"
```

## 7.1.3. 文字列の手作業でのフォーマット

- `str.rjust()` メソッド: 指定された幅のフィールド内に文字列が右寄せで入るように左側に空白を追加する
- 同様のメソッドとして、`str.ljust()`, `str.center()` がある
- `str.zfill()` 数値文字列の左側をゼロ詰めする。このメソッドは正と負の符号を正しく扱う

## 7.1.4. 古い文字列書式設定方法

```python
s = 'We are the %s who say "%s!"' % ('knights', 'Ni')
print(s) # We are the knights who say "Ni!"
```

## 7.2. ファイルを読み書きする

- `open()` は file object を返す
- 大抵は `open(filename, mode, encoding=None)` のように2つの位置引数と1つのキーワード引数を伴って呼び出される
- 1つめの引数: ファイル名の入った文字列
- 2つめの引数: ファイルをどのように使うかを示す1文字以上の文字列
  - `r`: ファイルが読み出し専用
  - `w`: 書き込み専用 (同名の既存のファイルがあれば消去される)
  - `a`: ファイルを追記用に開く
  - `b`: ファイルをバイナリモードで開く (指定しない場合はテキストモードで開く)
  - 省略された場合のデフォルト値は `r`
  - テキストモードの場合、読み込み / 書き込み時に、プラットフォーム固有の行末記号と `\n` の変換が行われる

ファイルオブジェクトを扱うときに `with` キーワードを使うのは良い習慣である。
処理中に例外が発生しても必ず最後にファイルがちゃんと閉じられる。
同じことは `try-finally` ブロックでも行えるが、`with` のほうがずっと簡潔に書ける。

```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# ファイルが自動でクローズされたことが確認できる
print(f.closed) # True
```

`f.write()` を `with` キーワードや `f.close()` を使わずに呼び出した場合、プログラムが正常に終了した場合でも、 `f.write()` の実引数がディスクに完全に書き込まれないことがある。

## 7.2.1. ファイルオブジェクトのメソッド

この節の以降の例は、 `f` というファイルオブジェクトが既に生成されているものと仮定する。

### read()

- ファイルの内容を読み出すには、 `f.read(size)` を呼び出す
- このメソッドは文字列 (テキストモードの場合) か bytes オブジェクト (バイナリーモードの場合) を返す
- `size` はオプションの数値引数で、size が省略されたり負の数であった場合、ファイルの内容全てを読み出す
- `size` が負でない数ならば、最大で (テキストモードの場合) `size` 文字、(バイナリモードの場合) `size` バイトを読み出して返す
- ファイルの終端にすでに達していた場合は `f.read()` は空の文字列 ('') を返します。

### readline()

- `f.readline()` はファイルから1行だけを読み取む
- 改行文字 (`\n`) は読み出された文字列の終端に残る
- 改行が省略されるのは、ファイルが改行で終わっていない場合の最終行のみ
- これは、戻り値があいまいでないようにするため
  - `f.readline()` が空の文字列を返したら、ファイルの終端に達したことが分かる
  - 一方、空行は `\n`、すなわち改行1文字だけからなる文字列で表現される

### ファイルオブジェクトをループ

ファイルから複数行を読み取るには、ファイルオブジェクトに対してループを書く方法がある。
この方法はメモリを効率的に使え、高速で、簡潔なコードになる。

```python
f = open("/path/to/file")
for line in f:
    print(line, end='')
```

### ファイルの行をリスト形式で読み込む()

- `list(f)`, `f.readlines()`

### write()

`f.write(string)` は、`string` の内容をファイルに書き込み、書き込まれた文字数を返す

```python
written_byte = f.write('This is a test\n')
print8(written_byte) # 15
```

オブジェクト型は、書き込む前に変換しなければならない。
テキストモードならば文字列に変換し、バイナリモードならば bytes オブジェクトに変換する

### tell(), seek()

- `f.tell()`: ファイルオブジェクトのファイル中における現在の位置を示す整数を返す
  - ファイル中の現在の位置は、バイナリモードではファイルの先頭からのバイト数、テキストモードでは不明瞭な値で表される
- `f.seek()`: ファイルオブジェクトの位置を変更する
  - ファイル位置は基準点 (reference point) にオフセット値 `offset` を足して計算される
  - 参照点は `whence` 引数で指定する
    - 0: ファイルの先頭から数える
    - 1: 現在のファイル位置
    - 2: ファイルの終端を参照点として使う。
    - `whence` は省略することができ、デフォルトの値は 0
  - テキストモードではいくつか制限がある
    - ファイルの先頭からの相対位置に対するシークだけが許可されている
    - (例外として、seek(0, 2) でファイルの末尾へのシークは可能)
    - `offset` は、`f.tell()` から返された値か、0 のいずれかのみ。それ以外の値は振る舞いは未定義

## 7.2.2. json による構造化されたデータの保存

- データをやり取りする場合には、JSON が便利
- `json.dumps(x)`: オブジェクト `x` の JSON 形式の文字列表現を返す
- `json.dump(x, f)`: オブジェクト `x` の JSON 形式の文字列表現をファイル `f` に書き込む
- `x = json.load(f)`: ファイル `f` から JSON 形式の文字列表現を読み込み、`x` にデシリアライズする
-  JSON ファイルは必ず UTF-8 でエンコードすること。つまり、読み書きとも `encoding="utf-8"` を指定する

```python
import json
x = [1, 'simple', 'list']
json.dumps(x) # '[1, "simple", "list"]'
```