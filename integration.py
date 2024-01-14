import unittest
from app import app, items



class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            items.clear()

    def test_read_page(self):
        response=self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        response = self.app.post('/add', data={'item': 'Item1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Item1", response.data)

    def test_delete_item(self):
        self.app.post('/add', data={'item': 'Item2'}, follow_redirects=True)
        response = self.app.get('/delete/0',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Item2", response.data)     
        
    def test_update_item(self):
        self.app.post('/add', data={'item': 'Item3'}, follow_redirects=True)
        response = self.app.post('/update/0', data={'new_item': 'Item4'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Item4", response.data)
        self.assertNotIn(b"Item3", response.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
