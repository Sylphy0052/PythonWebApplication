# PythonでWebサービスを作る - Python3+FLASKで作るWEBアプリケーション開発入門

## 1. Flaskの基本情報

Djangoと比べてFlaskは設定が少なく学習コストが低い．

|フレームワーク|スター数|
|:--|:--|
|Flask|35083|
|Django|33450|
|Tornado|15635|
|Bottle|5416|

### Flaskのメリット
- Pythonであること
  - バッチ処理，機械学習，統計処理や科学技術計算など応用が可能な言語
  - これらを活かしたWebアプリケーションを開発できる
  - `Batteries included`

なぜPythonのWebアプリケーションが普及してないのか
- 国内ではPython使う人が少ない
- 国内ではRubyが普及しており，Ruby on Railsが有用すぎる
- Pythonがあまり多くのリクエストをさばくことが不得意

## 2. Pythonについて
1980年代にオランド人のコンピュータ科学者のGuido van Rossum(グイド・ヴァン・ロッサム)氏によって開発が始められた言語．

グイドの所属していたCWIという研究機関内部でのみ使用されていた．

- 1991年にオープンソースの形式で一般に公開され，その利便性により急速に普及することになった
- 2000年: Python2と呼ばれるようになるUnicodeやガベージコレクタなどの機能を備えた新バージョンが登場

2010年にPython2の開発が中断した．

Python2とPython3は互換性がない

### venv
仮想環境を導入する

```shell
$ mkdir project
$ python -m venv project
$ cd project
$ source bin/activate

$ deactivate
```

## Flaskをはじめてみる
- 2010年に一般公開
- 製作者: Armin Ronacher氏
- シンプルさに主眼をおいたフレームワーク
- `Flask, web development one drop at a time`
- 依存しているのは`Jinja2`とWSGIフレームワークの`Werkzeug`
- Djangoと比べて
  - 高速に動作する
  - 2倍以上のリクエストをさばくことができる
  - RESTful構造

### URLの基本構造
スキーム(scheme)とホスト(host)とパス(path)

- scheme: プロトコルを指定する(httpかhttps)
- host: ドメインとサブドメインを組み合わせた部分
- path: 指定されたホストにあるWEBサーバからどの要素を取得するかを指定する部分

### Flaskのルーティングの注意点
パスの最後にスラッシュ(`/`)をつけるかつけないかで変化する．

例えば`@app.route('/foo/')`としても`localhost:5000/foo`や`localhost:5000/foo/`でアクセスできる.

しかし，`@app.route('/fuga')`とすると`localhost:5000/fuga`でアクセスできるが，`localhost:5000/fuga/`ではアクセスできない.

Apacheやnginxなどのサーバのパスと共通のルーティングのルールである．

### HTTPのメソッドを限定する
`GET`と`POST`
- `GET`: サーバ側からデータを**取得**するために用いられる
- `POST`: ユーザ側からデータを**送信**する際に使用される

### RESTfulとは
`RESTful`: Webアプリケーションの設計思想の1つで，クライアント側がサービスのAPIの構造を知らなくても直感的にアクセスができるようにすべきだとする発想．URLそのものがアプリケーションの構造を反映し，意味を持つべきだとする思想．

ロイ・フィールディングによって提唱された．(WWWの普及に大きく貢献した人物)

RESTfulでない例
```
# ユーザの情報を取得
http://www.sample.com/123
# 画像の情報を取得
http://www.sample.com/234
```
ユーザがわかりにくい

RESTfulの例
```
# ユーザの情報を取得
http://www.sample.com/user/23
# 画像の情報を取得
http://www.sample.com/image/234
```

こうすることで，ユーザはどの種類のデータにアクセスしようとしているのか，パスから直感的に理解できる．

## jinja2
Armin Ronacharが作成したPython用のテキストベースのテンプレートエンジン．

Pythonの記法でHTMlを作成できる．

- サンドボックス実行(危険なプログラムを実行しない)
- 強力なエスケープ処理によるXSS対策
- テンプレートの継承
- 高速なHTML出力
- デバッグが用意
- パイプ処理を追加可能

使用できる拡張子
- `.html`
- `.htm`
- `.xml`
- `.xhtml`

処理のフロー
1. HTMLの中に一部Pythonの構文を埋め込んだテンプレートファイルを作成
2. jinja2からこのテンプレートファイルを呼び出して適切な引数を与える
3. 引数に応じてその値の中身が埋め込まれたHTMlファイルが作成される
