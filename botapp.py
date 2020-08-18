from flask import Flask
from flask import request
from bottoken import token

apiUrl = 'https://api.telegram.org/bot' + token + '/'

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>Woofer Bot!</h1>'

@app.route('/bot/<token>', methods=['POST'])
def web_hook_route():
    return ''

if __name__ == '__main__':
    app.run()
