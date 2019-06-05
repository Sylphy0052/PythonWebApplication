import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from werkzeug import secure_filename

# appという変数にFlaskオブジェクトを作成するおまじない
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

def allowed_file(filename):
    return '.' in filename and\
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# ~/にアクセスしたときに実行される関数
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST': # POSTのとき
        img_file = request.files['img_file']
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = '/uploads/' + filename
            return render_template('index.html', img_url=img_url)
        else:
            return '''<p>許可されていない拡張子です</p>'''

    else: # GETのとき
        # indexメソッドを実行する
        return redirect(url_for('index'))

# ファイルをブラウザで表示するメソッド
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# mainで実行されたなら
if __name__ == '__main__':
    # デバッグモードをオンにする
    app.debug = True
    # サーバ起動
    app.run()
