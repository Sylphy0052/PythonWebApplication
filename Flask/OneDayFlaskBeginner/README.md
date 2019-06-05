# Python flamework Flask(Japanese Edition)

## 仮想環境構築とFlaskのインストール，そしてHello World

FlaskはDjangoよりも簡易的なマイクロフレームワーク．bottleのような簡単な構成でWebアプリケーションが開発できる．

### インストール

```shell
$ python3 -m venv flaskworks
$ source flaskworks/bin/activate

# (flaskworks)と出ていればOk
$ pip install flask
$ cd flaskworks
$ touch index.py
# プログラムを書く
# 実行する
$ python index.py
# http://127.0.0.1:5000/(Local Hostにアクセスする)
```

## テンプレートの利用

### 静的ファイルの取扱について

```shell
$ mkdir templates
$ mkdir static
$ touch templates/base.html
# templates/base.htmlを記述
$ touch templates/index.html
# index.htmlを記述
# index.pyを編集
# 実行
$ python index.py
```

- `templates/base`: 使い回せる箇所を記述するテンプレートファイル

```python
{% block head %}{% endblock %}
{% block footer %}{% endblock %}
```

## ルーティングの基本

### 基本的なルーティングについて

```shell
# templates/index.htmlをtemplates/hello.htmlにコピー
$ cp templates/index.html templates/hello.html
# templates/base.htmlを編集
# index.pyを編集
# 実行
$ python index.py
```

## HTTPメソッド

### フォームを受け取ってみよう

```shell
# index.pyを編集
```

## ファイルアップロード

### 画像ファイルなどファイルのアップロード

```shell
$ mkdir uploads
```
