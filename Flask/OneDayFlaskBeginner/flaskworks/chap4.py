from flask import Flask, render_template, request, redirect, url_for

# appという変数にFlaskオブジェクトを作成するおまじない
app = Flask(__name__)

# ~/にアクセスしたときに実行される関数
@app.route('/')
def index():
    # 返り値の文字列をブラウザに表示する
    # return 'Hello World'
    # テンプレートを呼び出す
    # base.htmlの{{ message }}に'Hello'という文字列を渡している
    # return render_template('index.html', message='Hello')
    return render_template('index.html', message='indexページです')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST': # POSTのとき
        msg = request.form['msg'] # formのname="msg"の内容を取得
        return render_template('index.html', message=msg)
    else: # GETのとき
        # indexメソッドを実行する
        return redirect(url_for('index'))

# mainで実行されたなら
if __name__ == '__main__':
    # デバッグモードをオンにする
    app.debug = True
    # サーバ起動
    app.run()
