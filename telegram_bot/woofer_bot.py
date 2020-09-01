from .telegrambotapi import TelegramBotAPI
import requests

dogApiUrl = 'https://dog.ceo/api/breeds/image/random'

class WooferBot(TelegramBotAPI):

    def __init__(self, token):
        super().__init__(token)


    def processUpdate(self, update):
        message_text = update['message']['text']
        chat_id = update['message']['chat']['id']
        if message_text == '/woof':
            return self.commandWoof(chat_id)
        if message_text == '/fact':
            return self.commandFact(chat_id)


    def commandWoof(self, chat_id):
        res = requests.get(dogApiUrl)
        resDict = res.json()
        if resDict['status'] == 'success':
            dogImageUrl = resDict['message']
            telegramResponse = self.sendPhoto(chat_id, dogImageUrl)
            if not telegramResponse['ok']:
                print('Error: {}. {}'.format(telegramResponse['error_code'], telegramResponse['description']))

        return telegramResponse

    def commandFact(self, chat_id):
        pass
