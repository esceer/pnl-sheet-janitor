import json

from bottle import response, Bottle

from utils.spreadsheet_worker import SpreadsheetWorker


def make_wsgi_app(spreadsheet_worker: SpreadsheetWorker):
    app = Bottle()

    @app.get('/pnl-janitor/')
    def get_summary():
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        summary = spreadsheet_worker.get_summary()
        return json.dumps(summary)

    return app
