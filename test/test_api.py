from app import app
import unittest
import json


class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        res = self.app.get('/games')
        if isinstance(res.data, bytes):
            data = res.data.decode('utf-8')
        else:
            data = res.data
        items = json.loads(data)
        # Set the first item in the response for testing the second endpoint
        self.single_item = items.pop()

    def tearDown(self):
        pass

    def test_games_status_code(self):
        res = self.app.get('/games')
        self.assertEqual(res.status_code, 200)

    def test_games_data(self):
        res = self.app.get('/games')
        self.assertTrue(res.data)

    def test_game_status_code(self):
        res = self.app.get('/games/' + self.single_item['title'])
        self.assertEqual(res.status_code, 200)

    def test_game_data(self):
        res = self.app.get('/games/' + self.single_item['title'])
        self.assertTrue(res.data)
