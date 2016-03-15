import unittest
from feed import Feed


class TestFeed(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = 'http://www.metacritic.com/game/playstation-3'
        cls.feed = Feed(url=url)

    def test_fetch(self):
        html = self.feed.fetch()
        self.assertTrue(html)

    def test_parse(self):
        html = open('test/static/index.html', 'r')
        payload = self.feed.parse(html)
        html.close()
        self.assertIsInstance(payload, list)
        self.assertTrue(payload)

    def test_get(self):
        feed = self.feed.get()
        self.assertIsInstance(feed, str)
        self.assertTrue(feed)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
