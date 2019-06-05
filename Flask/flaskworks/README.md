# Python flamework Flask(Japanese Edition)

## 初期設定
```shell
$ python -m venv flaskworks
$ source flaskworks/bin/activate
$ pip install flask
```

## エラー
- Address already in use
  - ``
```shell
$ ps aux | grep python
501  5785  4589   0 12:48AM ??         5:44.16 /Users/pyente/.pyenv/versions/anaconda3-5.3.1/bin/python login.py
$ kill 5785
```
