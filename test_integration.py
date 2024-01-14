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

        response = self.app.post('/add', data={'item': 'TestItem'}, follow_redirects=True)
        self.assertIn(b"TestItem", response.data)

        response = self.app.post('/update/0', data={'new_item': 'NewItem'}, follow_redirects=True)
        self.assertIn(b"NewItem", response.data)
        self.assertNotIn(b"TestItem", response.data)

        response = self.app.get('/delete/0',follow_redirects=True)
        self.assertNotIn(b"NewItem", response.data)     
        
if __name__ == '__main__':
    unittest.main()
