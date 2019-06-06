from flask_script import Command
from flask_blog import db

# スクリプト実行のためのクラス
class InitDB(Command):
    # クラス説明のためのコメント
    "create database"

    # スクリプトで実行される内容
    def run(self):
        # モデル定義の反映
        db.create_all()
