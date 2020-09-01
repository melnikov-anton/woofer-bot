# Telegram Bot API: https://core.telegram.org/bots/api

# ACHTUNG! ACHTUNG!
# NOT ALL ARGUMENTS IN METHODS WILL BE PROCESSED:
# See setWebhook, sendMessage, sendPhoto, sendVideo !!!

import requests
import json

API_URL_BASE = 'https://api.telegram.org/bot'

class TelegramBotAPI(object):

    def __init__(self, token):
        self._botUrl = API_URL_BASE + '{}/'.format(token)


    def getMe(self):
        getMeUrl = self._botUrl + 'getMe'
        response = requests.get(getMeUrl)
        return response.json()


    def getUpdates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        updatesUrl = self._botUrl + 'getUpdates'
        params = ''
        if offset:
            if params == '':
                params += 'offset={}'.format(str(offset))
            else:
                params += '&offset={}'.format(str(offset))
        if limit:
            if params == '':
                params += 'limit={}'.format(str(limit))
            else:
                params += '&limit={}'.format(str(limit))
        if timeout:
            if params == '':
                params += 'timeout={}'.format(str(timeout))
            else:
                params += '&timeout={}'.format(str(timeout))
        if allowed_updates and type(allowed_updates) is list:
            if params == '':
                params += 'allowed_updates={}'.format(json.dumps(allowed_updates))
            else:
                params += '&allowed_updates={}'.format(json.dumps(allowed_updates))

        if params != '':
            updatesUrl = updatesUrl + '?' + params

        response = requests.get(updatesUrl)

        return response.json()


    def setWebhook(self, url, certificate=None, max_connections=None, allowed_updates=None):
        setWebhookUrl = self._botUrl + 'setWebhook'
        params = 'url={}'.format(str(url))
        if max_connections:
            params += '&max_connections={}'.format(str(max_connections))
        if allowed_updates and type(allowed_updates) is list:
            params += '&allowed_updates={}'.format(json.dumps(allowed_updates))
        if certificate:
            pass
            #Needs to be handled
        setWebhookUrl = setWebhookUrl + '?' + params

        response = requests.get(setWebhookUrl)

        return response.json()



    def deleteWebhook(self):
        deleteWebhookUrl = self._botUrl + 'deleteWebhook'
        response = requests.get(deleteWebhookUrl)
        return response.json()


    def getWebhookInfo(self):
        getWebhookInfoUrl = self._botUrl + 'getWebhookInfo'
        response = requests.get(getWebhookInfoUrl)
        return response.json()


    def sendMessage(self, chat_id, text, parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None):
        sendMessageUrl = self._botUrl + 'sendMessage'
        params = 'chat_id={}&text={}'.format(chat_id, text)
        if parse_mode:
            params += '&parse_mode={}'.format(str(parse_mode))
        if disable_web_page_preview != None and type(disable_web_page_preview) is bool:
            params += '&disable_web_page_preview={}'.format(str(disable_web_page_preview))
        if disable_notification != None and type(disable_notification) is bool:
            params += '&disable_notification={}'.format(str(disable_notification))
        if reply_to_message_id:
            params += '&reply_to_message_id={}'.format(str(reply_to_message_id))
        if reply_markup:
            pass
            #Needs to be handled
        sendMessageUrl = sendMessageUrl + '?' + params

        response = requests.get(sendMessageUrl)
        return response.json()


    def sendPhoto(self, chat_id, photo, parse_mode=None, caption=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None):
        sendPhotoUrl = self._botUrl + 'sendPhoto'
        params = 'chat_id={}&photo={}'.format(chat_id, photo) # photo per url
        if parse_mode:
            params += '&parse_mode={}'.format(str(parse_mode))
        if caption:
            params += '&caption={}'.format(str(caption))
        if disable_notification != None and type(disable_notification) is bool:
            params += '&disable_notification={}'.format(str(disable_notification))
        if reply_to_message_id:
            params += '&reply_to_message_id={}'.format(str(reply_to_message_id))
        if reply_markup:
            pass
            #Needs to be handled
        sendPhotoUrl = sendPhotoUrl + '?' + params

        response = requests.get(sendPhotoUrl)
        return response.json()


    def sendVideo(self, chat_id, video, duration=None, width=None, height=None,
                    thumb=None, parse_mode=None, caption=None, supports_streaming=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None):
        sendVideoUrl = self._botUrl + 'sendVideo'
        params = 'chat_id={}&video={}'.format(chat_id, video) # video per url
        if duration:
            params += '&duration={}'.format(str(duration))
        if width:
            params += '&width={}'.format(str(width))
        if height:
            params += '&height={}'.format(str(height))
        if thumb:
            params += '&thumb={}'.format(str(thumb))
        if parse_mode:
            params += '&parse_mode={}'.format(str(parse_mode))
        if caption:
            params += '&caption={}'.format(str(caption))
        if supports_streaming != None and type(supports_streaming) is bool:
            params += '&supports_streaming={}'.format(str(supports_streaming))
        if disable_notification != None and type(disable_notification) is bool:
            params += '&disable_notification={}'.format(str(disable_notification))
        if reply_to_message_id:
            params += '&reply_to_message_id={}'.format(str(reply_to_message_id))
        if reply_markup:
            pass
            #Needs to be handled
        sendVideoUrl = sendVideoUrl + '?' + params

        response = requests.get(sendVideoUrl)
        return response.json()
