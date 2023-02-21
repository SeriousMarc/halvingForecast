import requests


class URL:
    url = 'https://chain.api.btc.com/v3/block/'

    @property
    def last_block_url(self):
        return self.url + 'latest'


class Client:
    url = URL()

    @classmethod
    def get_last_block(cls):
        response = requests.get(cls.url.last_block_url)
        return response.json()

    @classmethod
    def get_blocks_info(cls, blocks):
        response = requests.get(URL.url + ','.join(str(x) for x in blocks))
        return response.json()
