from .telegrambotapi import TelegramBotAPI
import requests
import json
import random
import os

dogApiUrl = 'https://dog.ceo/api/breeds/image/random'
dogFactsFilePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static/facts/dog_facts.json'))

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
            telegramResponse = self.sendPhoto(chat_id, dogImageUrl, caption='Woof! Woof!')
            if not telegramResponse['ok']:
                print('Error: {}. {}'.format(telegramResponse['error_code'], telegramResponse['description']))

        return telegramResponse

    def commandFact(self, chat_id):
        dog_facts = []
        with open(dogFactsFilePath) as json_file:
            data = json.load(json_file)
            dog_facts = data['dog_facts']
        random_fact = dog_facts[random.randint(1, 60)]['fact']
        telegramResponse = self.sendMessage(chat_id, random_fact)
        if not telegramResponse['ok']:
            print('Error: {}. {}'.format(telegramResponse['error_code'], telegramResponse['description']))

        return telegramResponse
