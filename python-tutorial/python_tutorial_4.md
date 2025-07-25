# 4. その他の制御フローツール

## 4.1 if 文

- 0個以上の `elif` を使うことができる
- `else` を使うこともできる

```python
a = 0
while a < 10:
    if a == 0:
        print("zero")
    elif a == 1:
        print("one")
    elif 2 <= a <= 5:
        print(" >= 2 and a <= 5")
    else:
        print(a)
    a = a + 1
```

## 4.2 for 文

- 任意のシーケンス型を反復する
- コレクションオブジェクトの値を反復処理をしているときに、そのコレクションオブジェクトを変更するのは止めた方がよい
- コレクションオブジェクトのコピーに対して反復処理をするか、新しいコレクションオブジェクトを作成する方がよい

```python
# 文字列の長さを計測:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

## 4.3 range 関数

- 算術型の数列を生成する
- 開始値を指定したり、増加値を指定することもできる。負数も指定できる

```python
for i in range(5):
    print(i, end=",")       # 0,1,2,3,4,

list(range(5, 10))          # [5, 6, 7, 8, 9]
list(range(0, 10, 3))       # [0, 3, 6, 9]
list(range(-10, -100, -30)) # [-10, -40, -70]
```

- `range()` が返すオブジェクトはリストではないが、リストっぽく振る舞う
- しかし実際にリストを作るわけではないので、スペースの節約になる
- `sum(range(4))` は `6` を返す

## 4.4. break 文と continue 文

- `break` 文は、その `break` 文を内包している最も内側にある `for` 文または `while` 文から抜け出す

```python
for i in range(3):
    for j in range(3):
        if i == j:
            print(f"{i} == {j}, break")
            break
        print(f"i: {i}, j: {j}")

# 0 == 0, break
# i: 1, j: 0
# 1 == 1, break
# i: 2, j: 0
# i: 2, j: 1
# 2 == 2, break
```

- `continue` 文はループの次のイテレーションを実行する

```python
for i in range(10):
    if i % 3 != 0:
        # 3の倍数ではない場合は何もしない
        continue
    print(i)
    
# 0
# 3
# 6
# 9
```

## 4.5. ループの else 節

- `break` を実行せずにループが終了すると `else` 節が実行される
    - `for` 文の場合、 `else` 節はループ処理の最後のイテレーションが実行されたあとに実行される 
    - `while` 文の場合は、ループ条件が偽となったあとに実行される

```python
def print_number_and_break(n: int, target: int):
  for i in range(n):
      if i == target:
          break
      print(i, end=" ")
  else:
      print(f"not found: {target}")

print_number_and_break(3, 2) # 0 1
print_number_and_break(3, 3) # 0 1 2 not found: 3
```

## 4.6. pass 文

- `pass` 文は何もしない
- 構文上、文を書くことが要求されているが、何も動作させる必要がないときに使う

```python
# キーボード割り込み(Ctrl+C)のためのビジーウェイト
while True:
    pass
```
 
```python
# 最小のクラスを作るときによく使われる方法
class MyEmptyClass:
    pass
```

```python
# 関数や条件文の仮置き
def initlog(*args):
    pass # ここを忘れずに実装すること!
```

## 4.7. match 文

- Rust や Haskell のパターンマッチングに近い
- 最初にマッチしたパターンのみが実行され、値からコンポーネント (シーケンス要素やオブジェクト属性) を変数に抽出することもできる
- `case _:` はすべてのパターンにマッチしなかったときに実行される。`_` はワイルドカードパターンで、任意の値にマッチする

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

複数のリテラルを `|` ("or") を使用して組み合わせて1つのパターンにできる。

```python
case 401 | 403 | 404:
    return "Not allowed"
```

パターンはアンパック代入ができ、変数に結びつけられる。

```python
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y={y}"
        case (x, 0):
            return f"X={x}"
        case (x, y):
            return f"X={x}, Y={y}"
        case _:
            raise ValueError("Not a point")

test_points = [
    (0, 0),      # "Origin"
    (0, 5),      # "Y=5"
    (3, 0),      # "X=3"
    (2, 4),      # "X=2, Y=4"
]

for p in test_points:
    s = describe_point(p)
    print(s)
```

パターンに `if` 節を追加でき、"ガード" と呼ばれる。
パターンがマッチしてもガードが `false` の場合、match は次の `case` ブロックの処理に移動する。
(ガードを評価する前に値が取り出されることに注意！)

```python
def describe_point(point):
  match point:
    case (x, y) if x == y:
      print(f"Y=X at {x}")
    case (x, y):
      print(f"対角線上ではない")
```

## 4.8. 関数を定義する

- `def` は関数を定義するキーワード
- 関数の本体の記述する文の最初の行は文字列リテラルにすることもでき、この文字列は関数の docstring と呼ばれる
- 自分が書くコードにドキュメンテーション文字列を入れるのはよい習慣である
- 実引数は 値渡し (call by value) で関数に渡される。 
  - ここでの 値 (value) とはオブジェクトへの 参照 (reference) をいい、オブジェクトの値そのものではない
  - 正確には、オブジェクトへの参照渡し (call by object reference)
- 関数を変数に入れることができる。

## 4.9. 関数定義についてもう少し

- 引数の定義方法は3つある
  - デフォルトの引数値
  - キーワード引数
  - 特殊なパラメータ

### 4.9.1. デフォルトの引数値

- 一つ以上の引数に対してデフォルトの値を指定する形式で、とても便利
- この形式を使うと、定義されている引数より少ない個数の引数で関数を呼び出せる
- デフォルト値は1度だけ評価される

```python
def greet(name="Unknown"):
  print(f"Hello, {name}!")

if __name__ == '__main__':
  greet("Taro") # "Hello, Taro!"
  greet()       # "Hello, Unknown!"
```

デフォルト値は、関数が定義された時点で、関数を 定義している 側のスコープ (scope) で評価される。
したがって、次のコードは `5` を出力する。

```python
i = 5

def f(arg=i):
  print(arg)

i = 6
f()
```

### 4.9.2. キーワード引数

- 関数を `kwarg=value` という形式の キーワード引数 を使って呼び出すことができる
- 関数の呼び出しにおいて、キーワード引数は位置引数の後でなければならない

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 適切な呼び出し
parrot(1000)                                          # 1つの位置引数
parrot(voltage=1000)                                  # 1つのキーワード引数
parrot(voltage=1000000, action='VOOOOOM')             # 2つのキーワード引数
parrot(action='VOOOOOM', voltage=1000000)             # 2つのキーワード引数
parrot('a million', 'bereft of life', 'jump')         # 3つの位置引数
parrot('a thousand', state='pushing up the daisies')  # 1との位置引数と1つのキーワード引数

# 不正な呼び出し
parrot()                     # 必須の引数がない
parrot(voltage=5.0, 'dead')  # キーワード引数の後ろにキーワードのない引数
parrot(110, voltage=220)     # 同じ引数に対して2つの値を指定
parrot(actor='John Cleese')  # 未知のキーワード引数
```

仮引数の最後に `**name` の形式のものがあると、それまでの仮引数に対応したものを除くすべてのキーワード引数が入った辞書を受け取る。
複数のキーワード引数を与えた場合に、それらが取り出される順序は、関数呼び出しで与えられた順序と同じになる。

```python
def print_attr(name, **keywords):
  print(f"Name: {name}.")
  for key in keywords:
    print(f"{key}: {keywords[key]}.")

if __name__ == '__main__':
  print_attr("Taro") # "Name: Taro"
  print_attr("Jiro", Age=20, Sex="man") # "Name: Taro\nAge: 20.\nSex: man."
```

### 4.9.3. 特殊なパラメータ

- デフォルトでは、引数は位置またはキーワードによる明示で Python 関数に渡される
- 可読性とパフォーマンスのために、その引数が位置、位置またはキーワード、キーワードのどれで渡されるかを開発者が判定するのに関数定義だけを見ればよいように、引数の渡され方を制限することには意味がある
- `/` と `*` はオプション。これらの記号は、引数が関数に渡される方法を示す。
  - 位置専用
  - 位置またはキーワード
  - キーワード専用

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        位置またはキーワード    |
        |                                - キーワード専用
         -- 位置専用
```

- 位置またはキーワード引数: 関数定義に `/` も `*` もない場合
- 位置専用引数
  - `/` がある場合、`/` の前にある引数は位置専用引数になる
  - 位置専用引数の場合、キーワードでは引数を渡せない
  - `/` の後の引数は、位置またはキーワード、もしくはキーワード専用
- キーワード専用引数
  - `*` がある場合、`*` の後ろにある引数はキーワード専用引数になる

```python
# 位置専用引数
def print_attr(name, /):
  print(f"Name: {name}.")

if __name__ == '__main__':
  print_attr("Taro")      # "Name: Taro"
  print_attr(name="Jiro") # TypeError: print_attr() got some positional-only arguments passed as keyword arguments: 'name'
```

### 4.9.3.5. 要約

- 引数の名前をユーザーに知らせる必要がないなら、位置専用引数を使用する。
- 引数の名前に意味がある、またはユーザーが引数の順番に縛られることを避けたほうがいいと考えるのなら、キーワード専用引数を使用する
- API の場合、将来引数の名前が変更された場合に API の変更ができなくなることを防ぐために、位置専用引数を使用する

## 4.9.4. 任意引数リスト

- 関数が任意の個数の引数で呼び出せるよう指定する方法
- これらの引数はタプルに格納される
- 最も使うことの少ない

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

## 4.9.5. 引数リストのアンパック

`*` 演算子を使うとリストやタプルから引数をアンパックできる。

```python
list(range(3, 6))            # 個別に引数を指定する通常の関数呼び出し

args = [3, 6]
list(range(*args))            # 引数リストをアンパックして関数呼び出し
```

## 4.9.6. ラムダ式

- キーワード `lambda` を使うと名前のない小さな関数を生成する
- 例えば `lambda a, b: a+b` は、二つの引数の和を返す関数になる
- ラムダ式の関数は、関数オブジェクトが要求されている場所にならどこでも使うことができる
- ラムダ式は構文上単一の式に制限される
- 意味付け的にはラムダ形式は単なる糖衣構文にすぎない
- 入れ子構造になった関数定義と同様、ラムダ式もそれを取り囲むスコープから変数を参照できる

```python
def make_power(n):
  return lambda x: x ** n

if __name__ == '__main__':
  print(make_power(2)(2)) # 4
  print(make_power(3)(2)) # 8
```

## 4.9.7. ドキュメンテーション文字列 (docstring)

- 最初の行は、対象物の目的を短く簡潔にまとめたものでなくてはならない
- 最初の行は大文字で始まり、ピリオドで終わっていなければならない
- 2行目以降がある場合
  - 2行目は空行にし、まとめの行と残りの記述部分を視覚的に分離する
  - 3行目以降は1つまたはそれ以上の段落で、対象物の呼び出し規約や副作用について記述する

https://docs.python.org/ja/3/tutorial/controlflow.html#documentation-strings

## 4.9.8. 関数のアノテーション

関数アノテーション はユーザ定義関数で使用される型についての完全にオプションなメタデータ情報。

https://docs.python.org/ja/3/tutorial/controlflow.html#function-annotations

## 4.10. 間奏曲: コーディングスタイル

ほとんどのプロジェクトが守っているスタイルガイドとして [PEP 8](https://peps.python.org/pep-0008/) がある。
全ての Python 開発者はある時点でそれを読むべきで、最も重要な点を抜き出しておく。

- インデントには空白4つを使い、タブは使わない 
  - 空白4つは (深くネストできる) 小さいインデントと (読み易い) 大きいインデントのちょうど中間に当たる
  - タブは混乱させるので使わずにおくのが良い
-  ソースコードの幅が 79 文字を越えないように行を折り返すこと
  - こうすることで小さいディスプレイを使っているユーザも読み易くなる
  - 大きなディスプレイではソースコードファイルを並べることもできるようになる
- 関数やクラスや関数内の大きめのコードブロックの区切りに空行を使うこと
- 可能なら、コメントは行に独立で書くこと
-  docstring を使うこと
-  演算子の前後とコンマの後には空白を入れ、括弧類のすぐ内側には空白を入れないこと: `a = f(1, 2) + g(3, 4)`
- クラスや関数に一貫性のある名前を付けること。以下に慣習を示す
  - クラス名には UpperCamelCase 使う
  - 関数名やメソッド名には lowercase_with_underscores を使う
  - メソッドの第1引数の名前は常に `self` を使う
- 風変りな文字エンコーディングは使わないこと
  - あなたのコードを世界中で使ってもらうつもりならば
  - どんな場合でも、Python のデフォルト UTF-8 またはプレーン ASCII が最も上手くいく
- 非 ASCII 文字を識別子に使うべきではない
  - ほんの少しでも他の言語を話す人がコードを読んだりメンテナンスする可能性があるのならば
