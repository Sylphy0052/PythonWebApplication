import os
import flask_blog
# テスト用のモジュールをインポート
import unittest
import tempfile
from flask_blog.scripts.db import InitDB

# テスト用のクラス(最初にTestとつけるのが慣例)
class TestFlaskBlog(unittest.TestCase):
    # 最初に実行される関数
    def setUp(self):
        # 一時的なデータベースを作成する
        self.db_fd, flask_blog.DATABASE = tempfile.mkstemp()
        self.app = flask_blog.app.test_client()
        InitDB().run()

    # テストの最後，終了直前に実行される
    def tearDown(self):
        # データベースを削除する
        os.close(self.db_fd)
        os.unlink(flask_blog.DATABASE)

    # フォームを使わないで実行できるようにした
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    # test_とついているメソッドが実行される
    def test_login_logout(self):
        # 正しい処理
        rv = self.login('test', 'test')
        assert 'ログインしました'.encode() in rv.data
        # 正しい処理
        rv = self.logout()
        assert 'ログアウトしました'.encode() in rv.data
        # 間違った処理
        rv = self.login('admin', 'admin')
        assert 'ユーザ名が異なります'.encode() in rv.data
        # 間違った処理
        rv = self.login('test', 'admin')
        assert 'パスワードが異なります'.encode() in rv.data

    if __name__ == '__main__':
        unittest.main()
