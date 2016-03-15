from flask import Flask, json, jsonify
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
    data = feed.get()
    if title is None:
        return json.dumps(data)
    else:
        for item in data:
            if item['title'] == title:
                return json.dumps(item)
        return not_found()

if __name__ == '__main__':
    app.run(debug=True)
