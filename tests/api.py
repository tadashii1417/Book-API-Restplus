import os
import unittest

from main import app

TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        # db.drop_all()
        # db.create_all()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_all_books(self):
        response = self.app.get('/api/books/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_a_book(self):
        response = self.app.get('/api/books/2132')
        self.assertEqual(response.status_code, 404)

    def test_get_a_book(self):
        response = self.app.get('/api/books/2132')

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
