import unittest
from app import app

class TestApp(unittest.TestCase):

    def test_sum(self):
       with app.test_client() as client:
            response = client.get('/sum?a=1&b=2')
            self.assertEqual(response.data.decode('utf-8'), '3')

    def test_negative_sum(self):
        with app.test_client() as client:
            response = client.get('/sum?a=-5&b=2')
            self.assertEqual(response.data.decode('utf-8'), '-3')


if __name__ == '__main__':
    unittest.main()
