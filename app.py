import json
from flask import Flask, jsonify
from feed import Feed

app = Flask(__name__)
url = 'http://www.metacritic.com/game/playstation-3'


@app.errorhandler(404)
def not_found(error=None):
    '''404 error handler'''
    message = {
        'status': 404,
        'message': 'Page Not Found',
    }
    res = jsonify(message)
    res.status_code = 404
    return res


@app.route('/games')
@app.route('/games/<title>')
def games(title=None):
    '''
    Usage:

    Get all games at /games
    Get one game at /games/title

    returns json or 404 if not found
    '''
    feed = Feed(url=url)

    if title is None:
        return app.response_class(feed.get(), content_type='application/json')
    else:
        data = json.loads(feed.get())
        for item in data:
            if item['title'] == title:
                return app.response_class(json.dumps(item),
                                          content_type='application/json')
        return not_found()

if __name__ == '__main__':
    app.run(debug=True)
