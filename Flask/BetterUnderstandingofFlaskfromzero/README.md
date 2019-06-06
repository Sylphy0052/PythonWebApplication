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
