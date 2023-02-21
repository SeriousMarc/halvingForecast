import pandas as pd

from datetime import datetime, timedelta

from bitcoin.api import Client


class HalvingForecast:
    def __init__(self):
        self.halving_period = 210_000
        self.last_block = Client.get_last_block()['data']['height']
        self.halving_blocks = list(range(0, self.last_block + 1, self.halving_period))
        self.next_halving_block = self.halving_blocks[-1] + self.halving_period
        self.next_forecast = datetime.now() + timedelta(minutes=(self.next_halving_block - self.last_block) * 10)

    def get_halving_data(self):
        halving_data = pd.DataFrame(
            Client.get_blocks_info(self.halving_blocks)['data'],
            columns=['timestamp', 'height'],
        ).rename(columns={'timestamp': 'date', 'height': 'block'})
        halving_data['date'] = pd.to_datetime(halving_data['date'], unit='s')
        halving_data = pd.concat(
            [
                halving_data,
                pd.DataFrame({'date': self.next_forecast, 'block': self.next_halving_block}, index=['block'])
            ],
            ignore_index=True,
        )

        return halving_data
