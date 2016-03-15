import json
import logging
import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('feed_cache', backend='sqlite', expire_after=300)


class Feed:

    def __init__(self, url=''):
        self._url = url
        self._feed = None
        self._prepare()

    def fetch(self):
        '''Fetch the data from the metacritic page'''
        try:
            res = requests.get(self._url, headers={'User-Agent': 'User Agent'})
        except requests.exceptions.ConnectionError as e:
            logging.error('An error occurred retrieving the data feed: ',
                          e.message)
            raise
        return res.text

    def parse(self, html):
        '''Parse the data from the metacritic page'''
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('ol', class_='list_products')
        payload = []

        if items is not None:
            titles = []
            scores = []
            for item in items:
                titles = [x.get_text() for x
                          in item.find_all('h3', 'product_title')]
                scores = [x.get_text() for x
                          in item.find_all('span', 'metascore_w')]

            keys = ['title', 'score']
            for item in zip(titles, scores):
                payload.append(dict(zip(keys, item)))
        return payload

    def _prepare(self):
        '''Fetch and parse the data'''
        html = self.fetch()
        self._feed = self.parse(html)

    def get(self):
        '''Get the feed as JSON'''
        return json.dumps(self._feed)
