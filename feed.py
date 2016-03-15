import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('feed_cache')


class Feed():

    url = 'http://www.metacritic.com/game/playstation-3'

    def fetch(self):
        '''Fetch the data'''
        try:
            res = requests.get(self.url, headers={'User-Agent': 'User Agent'})
        except requests.exceptions.ConnectionError as e:
            print('An error occurred retrieving the data feed: ', e.message)
        return res.text

    def parse(self, html):
        '''Parse the data'''
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('ol', class_='list_products')
        for it in items:
            titles = [x.get_text() for x in it.find_all('h3', 'product_title')]
            scores = [x.get_text() for x in it.find_all('span', 'metascore_w')]

        keys = ['title', 'score']
        payload = []
        for item in zip(titles, scores):
            payload.append((dict(zip(keys, item))))
        return payload

    def __iter__(self):
        pass
