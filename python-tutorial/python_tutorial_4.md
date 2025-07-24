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
