# 8. エラーと例外

エラーには、構文エラー (syntax error / parsing error) と例外 (exception) がある。

## 8.1. 構文エラー

## 8.2. 例外

実行中に検出されたエラーは例外 (exception) と呼ばれる。
例外には致命的なものあり、そうでないものもある。

- 例外は様々な型 (type) で起こり、その型がエラーメッセージの一部として出力される
- 例外型として出力される文字列は、発生した例外の組み込み名になる
- これは全ての組み込み例外について成り立ちますが、ユーザ定義の例外では必ずしも成り立たない。
    - 成り立つようにするのは有意義な慣習ではある
- 標準例外の名前は組み込みの識別子 (予約語ではナイ)

## 8.3. 例外を処理する

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

- `try`, `except`
    - 一つの `try` 文には複数の except 節 が付けられ、別々の例外に対するハンドラを指定できる
- ハンドラ
    - ハンドラは最初に該当した1つしか実行されない
    - ハンドラは対応する `try` 節内で発生した例外だけを処理し、同じ `try` 節内の別の例外ハンドラで起きた例外は処理しない
- `except` 節 では丸括弧で囲ったタプルという形で複数の例外を指定できる
    - `except (RuntimeError, TypeError, NameError):`
- `except` 節内のクラスは、そのクラスや派生クラスのインスタンスである例外とマッチする
- 例外が発生するとき、例外は関連付けられた値を持つことができる
    - この値は例外の 引数 (arguments) とも呼ばれる
    - 引数の有無および引数の型は、例外の型に依存する
- `except` 節は例外名の後に変数を指定できる
  - その変数は例外インスタンスに紐付けられる
  - 一般的には引数を保持する `args` 属性を持つ

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # <class 'Exception'> # the exception type
    print(inst.args)     # ('spam', 'eggs')    # arguments stored in .args
    print(inst)          # ('spam', 'eggs')    # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)      # x = spam
    print('y =', y)      # y = eggs
```

- `BaseException` はすべての例外に共通する基底クラス
- `Exception` は `BaseException` のサブクラスの1つで、致命的でない例外すべての基底クラス
- `Exception` のサブクラスではない例外は、一般的にプログラムが終了することを示すために使われているため処理されない
    - 例: `sys.exit()` によって送出される `SystemExit`
    - 例: ユーザーがプログラムを中断させたいときに送出される `KeyboardInterrupt`
- `Exception` はほぼすべての例外を捕捉するワイルドカードとして使える
- 良い例外処理の手法とは、処理対象の例外の型をできる限り詳細に書き、予期しない例外はそのまま伝わるようにすること
- `Exception` の最も一般的な例外処理のパターンでは、例外を表示あるいはログ出力してから再度送出する (呼び出し側でも例外を処理できるようにする):

```python

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise                                     # 例外を表示した後、再度送出する
```

- `try ... except` 文には、オプションで `else` 節を設けることができる
- `else` 節を設ける場合、全ての `except` 節よりも後ろに置かなければなりない
- `else` 節は `try` 節 で全く例外が送出されなかったときに実行されるコードを書くのに役立つ
- 追加のコードを付け加えるのは `try` 節よりも `else` 節の方がよい
    - `try ... except` 文で保護されたコードから送出されたもの以外の例外を過って捕捉してしまうことを避けられる

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

## 8.4. 例外を送出する

- `raise` 文を使って、特定の例外を発生させることができる。
- `raise` には送出される例外を指定する。例外インスタンスか例外クラスのいずれか
- 例外クラスが渡された場合は、引数無しのコンストラクタが呼び出され、暗黙的にインスタンス化される
    - `raise ValueError` は `raise ValueError()` の短縮表記

```
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
```

## 8.5. 例外の連鎖

`except` 節の中で未処理の例外が発生した場合、その未処理の例外は処理された例外のエラーメッセージに含まれる。

```
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error
```

ある例外が他の例外から直接影響されていることを示すために、`raise` 文にオプションの `from` 句を指定できる。
これは例外を変換するときに便利。

```
>>> def func():
...     raise ConnectionError
... 
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
```

自動的な例外の連鎖を無効にするには `from None` を指定する。

## 8.6. ユーザー定義例外

- プログラム上で新しい例外クラスを作成することで、独自の例外を指定することができる
- 例外は、典型的には `Exception` クラスから直接または間接的に派生したもの
- 例外クラスでは、普通のクラスができることなら何でも定義することができる
    - 通常は単純なものにしておく
    - 大抵はいくつかの属性だけを提供し、例外が発生したときにハンドラがエラーに関する情報を取り出せるようにする程度にとどめる
- ほとんどの例外は、標準の例外の名前付けと同様に、"Error" で終わる名前で定義される
- 多くの標準モジュールでは、モジュールで定義されている関数内で発生する可能性のあるエラーを報告させるために、独自の例外を定義している

## 8.7. クリーンアップ動作を定義する

- `try` 文のオプションの `finally` 句は、例外が発生してもしなくても必ず実行される
- `finally` 節は、ファイルやネットワーク接続などの外部リソースを、利用が成功したかどうかにかかわらず解放するために便利

## 8.8. 定義済みクリーンアップ処理

- オブジェクトのなかには、利用の成否にかかわらず、不要になった際に実行される標準的なクリーンアップ処理が定義されているものがある
- ファイルなどの定義済みクリーンアップ処理を持つオブジェクトについては、それぞれのドキュメントで示される
- 下記コードは、実行時に行の処理中に問題があったとしても、ファイル `f` は必ず `close` される

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

## 8.9. 複数の関連しない例外の送出と処理

- 組み込みの `ExceptionGroup` は例外インスタンスのリストをまとめ、同時に送出できる
- `ExceptionGroup` も例外であり、他の例外と同じように捕捉できる
- `except` の代わりに `except*` を使用すると、グループの中にある特定の型に一致した例外だけを選択して処理できる
- 例外グループの中に含める例外は、型ではなくインスタンスでなければならない
    - プログラムで送出された複数の例外を捕捉することが多いため

## 8.10. ノートによって例外を充実させる

- 例外は生成されたときに初期化されるが、例外を受け取ったあとに情報を追加することもできる
- この目的のために、例外は `add_note(note)` メソッドを持つ
    - このメソッドは文字列を受け取り、例外のノートのリストに追加する
    - 標準のトレースバックでは例外の後に、全てのノートが追加した順番に出力される

