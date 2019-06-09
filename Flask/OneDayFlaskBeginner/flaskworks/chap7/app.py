import os
import sqlite3
import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # DBに接続する
    con = sqlite3.connect('test.db')
    # 切断する
    con.close()
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # 今日の日付を取得
        date_time = datetime.datetime.today()
        msg = request.form['msg']

        con = sqlite3.connect('test.db')
        c = con.cursor()
        # テーブルを作成する
        c.execute('''CREATE TABLE IF NOT EXISTS message(msg, date_time)''')
        # フォームから受け取ったmsgと今日の日付をデータベースへ登録
        c.execute('INSERT INTO message VALUES (?, ?)', (msg, date_time))
        con.commit()
        # データベースから全データを参照する
        c = con.execute('''select * from message''')
        # レコードをくるくる
        for row in c:
            result_0 = row[0]
            result_1 = row[1]

        # ここでDBをクローズするとテンプレートにレンダリングできない
    return render_template('index.html', result_0=result_0, result_1=result_1)

if __name__ == '__main__':
    app.debug = True
    app.run()
