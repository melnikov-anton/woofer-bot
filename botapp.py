from flask import Flask
from flask import request
from flask import render_template
import json
import requests
from telegram_bot.woofer_bot import WooferBot
from bottoken import token
from flask_sslify import SSLify

webhookUrl = '/bot/{}'.format(token)


app = Flask(__name__)
sslify = SSLify(app)

bot = WooferBot(token)

@app.route('/')
def index():
    return render_template('index.html')


@app.route(webhookUrl, methods=['POST'])
def web_hook_route():
    update = request.data.decode()
    updDict = json.loads(update)
    bot.processUpdate(updDict)
    return ''


if __name__ == '__main__':
    app.run()
