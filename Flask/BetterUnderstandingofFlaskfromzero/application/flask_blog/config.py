import os

# SQLAlchemyの初期設定
SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# デバッグモード
DEBUG = True
# セッション情報を暗号化する
# OS固有の乱数発生源から24Byteのランダムなバイト列
SECRET_KEY = os.urandom(24)
# ユーザ名とパスワード
USERNAME = 'test'
PASSWORD = 'test'
