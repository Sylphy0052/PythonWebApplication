# Flaskクラスをインポートする
from flask import Flask
# テンプレートを使用するための関数をインポートする
from flask import render_template

# 実際はこう
# from flask import Flask, render_template

# appという変数にFlaskオブジェクトを作成するおまじない
app = Flask(__name__)

# ~/にアクセスしたときに実行される関数
@app.route('/')
def hello_world():
    # 返り値の文字列をブラウザに表示する
    # return 'Hello World'
    # テンプレートを呼び出す
    # base.htmlの{{ message }}に'Hello'という文字列を渡している
    # return render_template('index.html', message='Hello')
    return render_template('index.html', message='indexページです')

# ~/helloにアクセスしたときに実行される関数
@app.route('/hello/')
def hello():
    return render_template('hello.html', message = 'Hello World!')

# mainで実行されたなら
if __name__ == '__main__':
    # デバッグモードをオンにする
    app.debug = True
    # サーバ起動
    app.run()
