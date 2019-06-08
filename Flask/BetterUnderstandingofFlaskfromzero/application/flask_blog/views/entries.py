from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required

# http://127.0.0.1:5000/にリクエストが有ったときにshow_entriesメソッドを呼び出す
@app.route('/')
@login_required
def show_entries():
    # 文字列を返し，ブラウザに表示する
    # return "Hello World!"
    # templatesフォルダ以下にあるentries/index.htmlを返してレンダリングする
    # ログインしたというセッション情報がなければログイン画面へ遷移する
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    # 全データをDBから取得する
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)

# ブログを投稿するメソッド
@app.route('/entries/new', methods=['GET'])
@login_required
def new_entry():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    return render_template('entries/new.html')

@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

# url_forで渡されるIDをint型に指定
@app.route('/entries/<int:id>', methods=['GET'])
@login_required
def show_entry(id):
    # if not session.get('logged_in'):
    #     return render_template(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)

@app.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)

# 更新処理
@app.route('/entries/<int:id>/update', methods=['POST'])
@login_required
def update_entry(id):
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

# 削除処理
@app.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))
