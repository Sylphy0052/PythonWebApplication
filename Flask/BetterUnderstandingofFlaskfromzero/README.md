# ゼロからFlaskがよくわかる本

```shell
$ pip install pipenv
$ mkdir application
$ pipenv --three
# 仮想環境に入る
$ pipenv shell
$ pipenv install Flask
# 起動するメインファイル
$ touch server.py
$ mkdir flask_blog
# View
$ touch flask_blog/views.py
# 初期化ファイル
$ touch flask_blog/__init__.py
# 設定ファイル
$ touch flask_blog/config.py
```

```shell
(application) ~/G/P/F/B/application ❯❯❯ tree
.
├── Pipfile
├── Pipfile.lock
├── flask_blog
│   ├── __init__.py
│   ├── config.py
│   └── views.py
└── server.py
```

## Flaskのフレームワーク
FlaskはModel, Template, Viewの3つからなる，MTVフレームワークで構成されている

ユーザからリクエストがあったとき，Flaskでは以下のように処理される

1. ユーザがあるURLに対してアクセス(リクエスト)する
2. アクセスされたURLを読み取り，予め定義されたURLに紐付いた処理を実行する(View)
3. 処理の中で必要に応じてモデルと呼ばれるオブジェクトを通してデータベースにアクセスする(Model)
4. 処理の最後にユーザに表示するHTMLなどのテンプレートを返す(Template)
5. ユーザは返されたHTMLファイルを閲覧する

## Template
プログラムでhtmlファイルを返すようにする

```shell
$ mkdir -p templates/entries
$ touch templates/entries/index.html
```

## View
URLにリクエストが有った場合の処理を作成する．

ルーティング処理とそれに紐づく処理メソッドを記載する．

## sessionを扱う
ログインしていなかった場合にログイン画面に遷移させる

1. ログインに成功したらサーバからsession情報をブラウザ(クライアント)側に返す
2. クライアントはsession情報をcookieに保存する
3. 以後クライアントはそのsession情報を付与してリクエストし，サーバはそのsession情報が正しいか確認することでログインしているかどうかを判別する

secret keyを設定してsession情報を暗号化する

## Jinja2
htmlに`{% %}`で条件文を`{{ }}`でサーバの変数を表示できる．

## flashを使ってメッセージを表示する
`flash('<message>')`とすることで，表示したいメッセージをhtmlに送信する．

html側で`get_flashed_messages()`でサーバから渡されたすべてのメッセージを取得し，表示させる

## url_forで自動でリンクを作成する

`url_for(<method名>)`とすることで自動的に直接リンクに変換する

## データベースを扱う

### SQLAlchemyを使用する

```shell
$ pipenv install Flask-SQLAlchemy
```

configファイルにSQLAlchemyの初期設定を書く．

## Model
データベースのモデルを定義する．

ORM(Object Relation Mapping): モデル(Model)とデータベース(Relation)を結びつける(Mapping)．プログラムでは定義したモデルに対して簡単な指示をするだけで自動でデータベースを適切に操作してくれるので，簡単にデータベースを扱うことができる

### スクリプトでデータベースを作成する

```shell
$ pipenv install Flask-Script
# データベースの作成
$ python manage.py init_db
```

## CRUDについて
- Create: データの新規作成
- Read: データの読み込み
- Update: データの更新
- Delete: データの削除

## views.pyの分割

```shell
# テーブルの作成
$ pipenv run python manage.py init_db
```

## Blueprintでアプリケーションを分割する
blueprintという機能を使って大きくなったアプリケーションに対して機能を分割する．

1. divisionalな構造化: アプリケーションの中に複数の機能があるとき，その小さな機能を小さなアプリケーションとして独立させて構成できる．(view, template, static)をまとめて独立したアプリケーションにすること
2. functionalな構造化: templateやstaticファイルを共通で使っている場合にビューのみを分ける方法

## テストカバレッジの計測とレポートの作成
テストカバレッジ: アプリケーション全体のうちどれだけの範囲がテストコードが書かれているかという指標．100%に近づくほど，アプリケーションのコードがより網羅的にテストされているということを表す．

```shell
$ pipenv install coverage
```

```
# application/.coveragerc
[run]
source = ./flask_blog
```

```shell
# テストの実行
$ coverage run -m unittest
# テストカバレッジ
# coverage report -m
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
flask_blog/__init__.py             8      0   100%
flask_blog/config.py               7      0   100%
flask_blog/models/entries.py      14      4    71%   18-20, 24
flask_blog/scripts/db.py           5      0   100%
flask_blog/views/entries.py       45     22    51%   31, 38-45, 53-54, 61-62, 70-76, 84-88
flask_blog/views/view.py          26      2    92%   9, 40
------------------------------------------------------------
TOTAL                            105     28    73%
```

- Name: テスト対象のファイル
- Stmts: 対象ファイルにおけるテスト対象となるコード行数
- Miss: テストされていないコード行数
- Cover: テストカバレッジになる
- Missing: -mオプションで実行したときのみ表示される．実際にテストされていないコードが何行目に有るか示す

```shell
# レポートの作成
$ coverage html
```

## アプリケーションの構成
```
.
├── Pipfile
├── Pipfile.lock
├── flask_blog
│   ├── __init__.py
│   ├── config.py
│   ├── flask_blog.db
│   ├── models
│   │   └── entries.py
│   ├── scripts
│   │   └── db.py
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   ├── entries
│   │   │   ├── edit.html
│   │   │   ├── index.html
│   │   │   ├── new.html
│   │   │   └── show.html
│   │   ├── layout.html
│   │   └── login.html
│   └── views
│       ├── entries.py
│       └── view.py
├── htmlcov
│   ├── coverage_html.js
│   ├── flask_blog___init___py.html
│   ├── flask_blog_config_py.html
│   ├── flask_blog_models_entries_py.html
│   ├── flask_blog_scripts_db_py.html
│   ├── flask_blog_views_entries_py.html
│   ├── flask_blog_views_view_py.html
│   ├── index.html
│   ├── jquery.ba-throttle-debounce.min.js
│   ├── jquery.hotkeys.js
│   ├── jquery.isonscreen.js
│   ├── jquery.min.js
│   ├── jquery.tablesorter.min.js
│   ├── keybd_closed.png
│   ├── keybd_open.png
│   ├── status.json
│   └── style.css
├── manage.py
├── server.py
└── test_flask_blog.py
```

- Pipfile/Pipfile.lock
  - pythonライブラリの管理ファイル
- manage.py
  - スクリプトの管理ファイル
- server.py
  - 起動ファイル
- .coveragerc
  - テストカバレッジの定義ファイル
- htmlcov
  - テストカバレッジレポートの格納フォルダ
- flask_blog
  - アプリケーションの本体フォルダ
- \_\_init\_\_.py
  - アプリケーションの本体ファイル
- config.py
  - アプリケーションの設定ファイル
- flask_blog.db
  - データベースファイル
- models
  - モデルファイルが格納されるフォルダ
- scripts
  - スクリプト実行ファイルが格納されるフォルダ
- static
  - CSS,JSなどの静的ファイルが格納されるフォルダ
- templates
  - テンプレートファイルが格納されるフォルダ
- views
  - ビューファイルが格納されるフォルダ
