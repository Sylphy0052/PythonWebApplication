import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

# appという変数にFlaskオブジェクトを作成するおまじない
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and\
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

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
        img_file = request.files['img_file']
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html')
        else:
            return '''<p>許可されていない拡張子です</p>'''

    else: # GETのとき
        # indexメソッドを実行する
        return redirect(url_for('index'))

# To Do ここにファイルをブラウザで表示するメソッドを書く

# mainで実行されたなら
if __name__ == '__main__':
    # デバッグモードをオンにする
    app.debug = True
    # サーバ起動
    app.run()
