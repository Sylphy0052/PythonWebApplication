# データベースモジュールのインポート
from flask_blog import db
# 日付を扱うモジュールをインポート
from datetime import datetime

class Entry(db.Model):
    # テーブルの名前
    __tablename__ = 'entries'
    # 主キー
    id = db.Column(db.Integer, primary_key=True)
    # ユニークキー
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    # コンストラクタ
    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow() # UTC時間

    # コンソールの出力形式
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
