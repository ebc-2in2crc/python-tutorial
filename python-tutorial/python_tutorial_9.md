# 9. クラス

- クラスはデータと機能を組み合わせる方法を提供する
- 新しいオブジェクトの型を作成し、その型を持つ新しいインスタンスを作れる
- それぞれのインスタンスは自身の状態を保持する属性をもてる
- インスタンスは、その状態を変更するためのメソッドをもてる
- 継承メカニズム
  - 複数の基底クラスをもてる
  - 派生クラスで基底クラスのメソッドをオーバーライドできる
  - メソッドでは、基底クラスのメソッドを同じ名前で呼び出せる
- C++ の用語で言えば、
    - クラスメンバーはすべて public
    - メンバー関数はすべて仮想関数 (virtual)
    - メソッド宣言では、オブジェクト自体を表す第一引数を明示しなければならない
    - 第一引数のオブジェクトはメソッド呼び出しの際に暗黙の引数として渡される
    - クラスはそれ自体がオブジェクトで、import や名前変更といった操作が可能
    - 特別な構文を伴うほとんどの組み込み演算子はクラスインスタンスで使うために再定義できる

## 9.1. 名前とオブジェクトについて

- オブジェクトには個体性があり、同一のオブジェクトに (複数のスコープから) 複数の名前を割り当てることができる
- この機能は他の言語では別名づけ (alias) として知られている
- 変更不能な基本型 (数値、文字列、タプル)を扱うときには無視して差し支えない
- しかし、リストや辞書や他の多くの型など、変更可能 (mutable) な型を扱う Python コード上で驚くべき効果がある

## 9.2. Python のスコープと名前空間

- 名前空間 (namespace) とは、名前からオブジェクトへの対応付け (mapping) のこと
- 異なった名前空間にある名前の間には全く関係がない
    - 例えば、二つの別々のモジュールの両方で関数 maximize という関数を定義することができる
    - 定義自体は混同されることはない
    - モジュールのユーザは名前の前にモジュール名をつけなければならない
- 属性は読取り専用にも書込み可能にもできる
    - 書込み可能であれば属性に代入することができる
    - モジュール属性は書込み可能で `modname.the_answer = 42` のように書くことができる
    - 書込み可能な属性は、 del 文で削除することもできる。例: `del modname.the_answer`
- インタプリタのトップレベルで実行された文は `__main__` モジュールの一部とみなされる
    - スクリプトファイルから読み出されたものでも対話的に読み出されたものでもされたものでも
- スコープ (scope) とは、ある名前空間が直接アクセスできるような、 Python プログラムのテキスト上の領域
    - "直接アクセス可能" とは、修飾なしに (訳注: spam.egg ではなく単に egg のように) 名前を参照した際に、その名前空間から名前を見つけようと試みることを意味する
- スコープは静的に決定され、動的に使用される。実行中はいつでも、直接名前空間にアクセス可能な、3つまたは4つの入れ子になったスコープがル
    1. 最初に探される最も内側のスコープは、ローカルな名前を持っている 
    2. 外側の (enclosing) 関数のスコープは、近いほうから順に探され、ローカルでもグローバルでもない名前を持っている
    3. 次のスコープは、現在のモジュールのグローバルな名前を持っている
    4. 一番外側のスコープはビルトイン名を持っている (最後に検索される)
- 名前が `global` と宣言されている場合、その名前に対する参照や代入は全てモジュールのグローバルな名前の入った最後から2番目のスコープに対して直接行わる
    - 最内スコープの外側にある変数に再束縛するには、 `nonlocal` 文が使える
    - `nonlocal` と宣言されなかった変数は、全て読み出し専用となる
    - そのような変数に対する書き込みは、単に新しいローカル変数をもっとも内側のスコープで作成し、外部のスコープの値は変化しない
- ローカルスコープ
    - 通常、ローカルスコープは (プログラムテキスト上の) 現在の関数のローカルな名前を参照する
    - 関数の外側では、ローカルスコープはグローバルな名前空間と同じ名前空間、モジュールの名前空間を参照する
    - クラス定義では、ローカルスコープの中にもう一つ名前空間が置かれる
- `global`, `nonlocal`
    - `global` 文を使うと、特定の変数がグローバルスコープに存在し、そこで再束縛されることを指示できる
    - `nonlocal` 文は、特定の変数が外側のスコープに存在し、そこで再束縛されることを指示する

### 9.2.1. スコープと名前空間の例

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam
```

## 9.3. クラス初見

### 9.3.1. クラス定義の構文

最も単純なクラス定義の形式。

```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

- クラスの名前空間
    - クラス定義に入ると、新たな名前空間が作成され、ローカルな名前空間として使わる
    - 従って、ローカルな変数に対する全ての代入はこの新たな名前空間に入る
    - 特に、関数定義を行うと新たな関数の名前はこの名前空間に結び付けられる
- クラスオブジェクト
    - クラス定義の構文が終了すると、 クラスオブジェクト (class object) が生成される
    - クラスオブジェクトは、基本的にはクラス定義で作成された名前空間の内容をくるむラッパー
    - 生成されたクラスオブジェクトは復帰したローカルスコープに結びつけられる

### 9.3.2. クラスオブジェクト

- クラスオブジェクトでは２種類の演算、属性参照とインスタンス生成をサポートしている
- 属性参照: `obj.name`
-  クラスの インスタンス化 (instantiation) には関数記法を使う
    - クラスオブジェクトのことを、クラスの新しいインスタンスを返す、引数のない関数のように扱うとよい
- `__init__` メソッド
    - クラスが `__init__()` メソッドを定義している場合、クラスをインスタンス化時に自動的に `__init__()` が呼び出される
    - `__init__()` メソッドに複数の引数をもたせることができる
    - クラスのインスタンス化操作に渡された引数は `__init__()` に渡される
  
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x = Person("Taro", 20)
print(f"{x.name=}, {x.age=}") # x.name='Taro', x.age=20
```

### 9.3.3. インスタンスオブジェクト

クラスの関数オブジェクトは、インスタンスオブジェクトのメソッドオブジェクトになる。

### 9.3.4. メソッドオブジェクト

メソッドオブジェクトは別の変数に淹れておくことができる。
次の例では `x.f` はメソッドオブジェクトで、変数 `xf` に入れている。

```python
class MyClass:
    def f(self):
        return 'hello world'

x = MyClass()
xf = x.f
print(xf()) # hello world
```

### 9.3.5. クラスとインスタンス変数

- インスタンス変数は、それぞれのインスタンスについての固有データ
- クラス変数は、そのクラスのすべてのインスタンスによって共有されるデータ
    - `<クラス名>.<変数名>` でアクセスすることが推奨される
    - `obj.name` でのアクセスだと、インスタンス変数にシャドーイングされるため

```python
class Dog:

    kind = 'canine'         # 全インスタンスで共有されるクラス変数

    def __init__(self, name):
        self.name = name    # インスタンスごとに固有のインスタンス変数

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)     # 'canine' # すべての犬で共有
print(e.kind)     # 'canine' # すべての犬で共有

print(d.name)     #  'Fido'  # d 固有
print(e.name)     # 'Buddy'  # e 固有
```

### 9.4. いろいろな注意点

インスタンスとクラスの両方で同じ属性名が使用されている場合、属性検索はインスタンスが優先される。

```python
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region) # storage west

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region) # storage east
```

## 9.5. 継承

派生クラス (derived class) を定義する構文は次のようになる。

```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

- 派生クラスから基底クラスのメソッドを直接呼び出す方法: `BaseClassName.methodname(self, arguments)`
- 継承に関係する組み込み関数
    - `isinstance()`
        - インスタンスの型を調べられる
        - `isinstance(obj, int)` は `obj.__class__` が `int` や `int` の派生クラスの場合に限り `True` になる
    - `issubclass()`
        - クラスの継承関係を調べられる
        - `bool` は `int` のサブクラスなので `issubclass(bool, int)` は `True` になる
        - `float` は `int` のサブクラスではないので `issubclass(float, int)` は `False` になる

### 9.5.1. 多重継承

複数の基底クラスをもつクラス定義は次のようになる。

```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

- ほとんどのシンプルな多重継承において、
    - 親クラスから継承される属性の検索は、深さ優先で左から右に
    - 継承の階層の中で同じクラスが複数出てくる (ダイアモンド継承) 場合に２度探索をしない、と考えることができる
- ある属性が DerivedClassName で見つからない場合
    - まず Base1 から検索される
    - そして (再帰的に) Base1 の基底クラスから検索される
    - それでも見つからなかった場合は Base2 から検索される、といった具合になる
- 実際には、それよりもう少しだけ複雑。`super()` の呼び出しのためにメソッドの解決順序は動的に変更される
    - 動的順序付けが必要なのは、すべての多重継承で１つ以上のダイヤモンド継承 (少なくとも 1 つの祖先クラスに対して最下位クラスから到達する経路が複数ある状態) が見られるため

## 9.6. プライベート変数

- オブジェクトの中からしかアクセス出来ない "プライベート" インスタンス変数はない
- しかし、ほとんどの Python コードが従っている慣習がある
    - アンダースコアで始まる名前 (例: `_spam`) は、 (関数であれメソッドであれデータメンバであれ) 非 public な API として扱う
    - これらは (非 public なので) 予告なく変更されるかもしれない実装の詳細として扱われるべき
- 名前マングリング
- `__spam` (先頭に二個以上の下線文字) という形式の識別子は `_classname__spam` へとテキスト置換される

## 9.7. 残りのはしばし

言語の "構造体 (struct)" のような、名前つきのデータ要素を一まとめにするデータ型があると便利なことがある。
Python では慣用的な手法として `dataclasses` を使用する。

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)

print(john.dept)    # computer lab
print(john.salary)  # 1000
```

## 9.8. イテレータ (iterator)

`for` 文を使うとほとんどのコンテナオブジェクトにわたってループを行うことができる。

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

- 裏では `for` 文はコンテナオブジェクトに対して `iter()` 関数を呼んでいる
    - `iter()` 関数は、引数に指定されたオブジェクトの `__iter__()` メソッドを呼び出し、`__next__()` メソッドが定義されているイテレータオブジェクトを返す
    - `__next__()` メソッドはコンテナの要素を1つずつ返す
    - `__next__()` メソッドは、これ以上要素が無い場合は `StopIteration` 例外を送出する
    - その通知を受け `for` ループが終了する
- 自作のクラスにイテレータとしての振舞いを追加するのは簡単
    - `__next__()` メソッドを持つオブジェクトを返す `__iter__()` メソッドを定義
    - たとえば、クラスが `__next__()` メソッドを定義している場合、 `__iter__()` メソッドは単に `self` を返すだけ
 
```python
class Reverse:
    """シーケンスを後ろからまわるイテレータ."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char, end="") # maps
```

## 9.9. ジェネレータ (generator)

- ジェネレータは、イテレータを作成するための簡潔で強力なツール
- ジェネレータは通常の関数のように書くが、データを返すときには `yield` 文を使う
- ジェネレータに対して `next()` が呼び出されるたびに、ジェネレータは以前に中断した処理を再開する
- ジェネレータは、全てのデータ値と最後にどの文が実行されたかを記憶している

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char, end="") # flog
```

ジェネレータを使うと、通常の関数を書くのと同じ労力で簡単にイテレータを生成できる。

- ジェネレータでできることは、クラスを使ったイテレータでも実現できるが、ジェネレータのほうが労力が少ない
- ジェネレータの定義がコンパクトになるのは `__iter__()`, `__next__()` メソッドが自動で作成されるから
- ジェネレータは呼び出しごとにローカル変数と実行状態が自動的に保存される
    - `self.index` や `self.data` といったインスタンス変数を使ったアプローチよりも簡単に関数を書くことができる
- ジェネレータは終了時に自動的に `StopIteration` する

## 9.10. ジェネレータ式

- 単純なジェネレータなら式として簡潔に書ける
- 構文はリスト内包表記に似ており、角括弧ではなく丸括弧で囲う

```python
sum(i*i for i in range(10))                 # 平方和
# 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # ドット積
# 260
```