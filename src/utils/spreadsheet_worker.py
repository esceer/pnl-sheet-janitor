class SpreadsheetWorker:
    from config.config import Config

    def __init__(self, config: Config):
        self._spreadsheet_path = config.get_spreadsheet_path()
        self._active_spreadsheet_tab = config.get_active_spreadsheet_tab()

    def get_summary(self):
        spreadsheet = self._open_spreadsheet()
        return {
            'pnl': spreadsheet.read_summary_pnl_value(),
            'car-bike': spreadsheet.read_summary_car_bike_value(),
            'savings': spreadsheet.read_summary_savings_value(),
            'balance': spreadsheet.read_summary_balance_value()
        }

    def _open_spreadsheet(self):
        return Spreadsheet(self._spreadsheet_path, self._active_spreadsheet_tab)


class Spreadsheet:
    def __init__(self, file_path: str, active_tab: str):
        import pandas
        self._dataframe = pandas.read_excel(file_path, active_tab)

    def read_summary_pnl_value(self) -> int:
        return self._dataframe.iat[19, 1]

    def read_summary_car_bike_value(self) -> int:
        return self._dataframe.iat[20, 1]

    def read_summary_savings_value(self) -> int:
        return self._dataframe.iat[21, 1]

    def read_summary_balance_value(self) -> int:
        return self._dataframe.iat[22, 1]
