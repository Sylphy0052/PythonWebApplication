from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# loginリンクをクリックするときはGETメソッドが
# ログインフォームのデータ送信にはPOSTメソッドが使われる
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # POSTならば
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else: # ログイン成功ならば
            # セッションにログインしたという情報を格納
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('entry.show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # セッションからログインしたという情報を破棄
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('login'))

@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('login'))
