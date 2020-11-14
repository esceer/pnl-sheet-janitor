import configparser


class Config:
    def __init__(self):
        self._config_file_path = '../resources/psj.ini'
        self._config = self._parse_config_file()

    def get_server_port(self) -> int:
        return int(self._config['Server']['port'])

    def get_spreadsheet_path(self) -> str:
        return self._config['Spreadsheet']['path']

    def get_active_spreadsheet_tab(self) -> str:
        return self._config['Spreadsheet']['active-tab']

    def _parse_config_file(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self._config_file_path)
        return config
