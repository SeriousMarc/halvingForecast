import os
import pandas as pd

from datetime import datetime
from pathlib import Path

from bitcoin.halving import HalvingForecast


def get_cached_data():
    folder = Path.cwd() / 'bitcoin/csv'
    today = datetime.today()
    date = today.strftime("%m-%d-%Y")
    file_path = Path(folder) / f'{date}.csv'

    if file_path.exists():
        # file exists, read it with pandas
        halving_data = pd.read_csv(file_path, parse_dates=['date'])
    else:
        # file does not exist, do something else
        halving_data = HalvingForecast().get_halving_data()

        for f in os.listdir(folder):
            f_path = Path(folder) / f
            if f_path.is_file():
                os.remove(f_path)

        halving_data.to_csv(file_path, index=False)

    return halving_data
