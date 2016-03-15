import unittest
from feed import Feed


class TestFeed(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.feed = Feed()

    def test_fetch(self):
        html = self.feed.fetch()
        self.assertIsInstance(html, str)

    def test_parse(self):
        html = open('test/static/index.html', encoding='utf-8')
        payload = self.feed.parse(html)
        html.close()
        self.assertIsInstance(payload, list)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
