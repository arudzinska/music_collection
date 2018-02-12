import os
import unittest


from app import app, db

TEST_DB = 'test.db'
app.config['BASEDIR'] = os.path.abspath(os.path.dirname('views.py'))


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        # app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #                                         os.path.join(app.config['BASEDIR'], TEST_DB)
        # self.app = app.test_client()
        # db.drop_all()
        app.config.from_object('config.TestConfiguration')
        db.create_all()

    def tearDown(self):
        pass

    def test_root(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_show_albums(self):
        response = self.app.get('/show_albums', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()