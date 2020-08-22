from flask import Flask
from flask import request
from bottoken import token
import json
import requests

apiUrl = 'https://api.telegram.org/bot{}/'.format(token)
webhookUrl = '/bot/{}'.format(token)

dogApiUrl = 'https://dog.ceo/api/breeds/image/random'

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>Woofer Bot!</h1>'


@app.route(webhookUrl, methods=['POST'])
def web_hook_route():
    update = request.data.decode()
    updDict = json.loads(update)
    message_text = updDict['message']['text']
    chat_id = updDict['message']['chat']['id']
    print(updDict)
    if message_text == '/woof':
        res = requests.get(dogApiUrl)
        resDict = res.json()
        if resDict['status'] == 'success':
            dogImageUrl = resDict['message']
            telegramResponse = sendPhoto(chat_id, dogImageUrl)
            if not telegramResponse['ok']:
                print('Error: {}. {}'.format(telegramResponse['error_code'], telegramResponse['description']))

    return ''

def sendMessage(chat_id, message_text):
    sendMsgUrl = apiUrl + 'sendMessage?chat_id={}&text={}'.format(chat_id, message_text)
    res = requests.get(sendMsgUrl)
    return res.json()

def sendPhoto(chat_id, photo_url):
    sendPhotoUrl = apiUrl + 'sendPhoto?chat_id={}&photo={}'.format(chat_id, photo_url)
    res = requests.get(sendPhotoUrl)
    return res.json()

if __name__ == '__main__':
    app.run()
