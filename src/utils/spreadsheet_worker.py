import pandas

from config.config import Config


class SpreadsheetWorker:
    def __init__(self, config: Config):
        self._dataframe = pandas.read_excel(config.get_spreadsheet_path(), config.get_active_spreadsheet_tab())
        print(self._dataframe)

    def read_summary(self):
        return {
            'pnl': self._read_summary_pnl_value(),
            'car-bike': self._read_summary_car_bike_value(),
            'savings': self._read_summary_savings_value(),
            'balance': self._read_summary_balance_value()
        }

    def _read_summary_pnl_value(self) -> int:
        return self._dataframe.iat[19, 1]

    def _read_summary_car_bike_value(self) -> int:
        return self._dataframe.iat[20, 1]

    def _read_summary_savings_value(self) -> int:
        return self._dataframe.iat[21, 1]

    def _read_summary_balance_value(self) -> int:
        return self._dataframe.iat[22, 1]
