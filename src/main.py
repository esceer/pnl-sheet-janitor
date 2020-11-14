import bottle

from api import api
from config.config import Config
from utils.spreadsheet_worker import SpreadsheetWorker

app = application = bottle.default_app()

if __name__ == '__main__':
    config = Config()
    spreadsheet_worker = SpreadsheetWorker(config)
    bottle.run(api.make_wsgi_app(spreadsheet_worker), host='127.0.0.1', port=config.get_server_port())
