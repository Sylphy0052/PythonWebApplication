import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from werkzeug import secure_filename

app = Flask(__name__)

# Config設定
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ランダムでシークレットキーを発行する
app.config['SECRET_KEY'] = os.urandom(24)

# 指定された拡張子以外受け付けない
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return '''<p>ログインしてください</p>'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    # POSTだったら
    if request.method == 'POST':
        username = request.form['username']
        if username == 'admin':
            # セッションにユーザ名を格納
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        # adminじゃなかったら
        else:
            return '''<p>ユーザ名が違います</p>'''
    # GETだったら
    return '''
        <form action="" method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    # セッションからusernameを削除しその値を返す
    # その項目がない場合，第二引数で渡されたものを返す
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/send', methods=['GET', 'POST'])
def send():
    # POSTだったら
    if request.method == 'POST':
        img_file = request.files['img_file']
        # ファイルが選択されているかつ指定された拡張子だったら
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html')
        # ファイルの拡張子が指定されたものじゃなかったら
        else:
            return '''<p>許可されていない拡張子です</p>'''
    # GETだったら
    else:
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.debug = True
    app.run()
