import time
import os
import requests

from dotenv import load_dotenv 
from twilio.rest import Client

load_dotenv()
VK_TOKEN = os.getenv('access_token')
URL_VK_API = 'https://api.vk.com/method/users.get'
VK_API_VERSION = 5.92

def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': VK_API_VERSION,
        'fields': 'online',
        'access_token': VK_TOKEN
    }
    try:
        user_status = requests.post(url=URL_VK_API, params=params)
    except:
        print('An exception occurred')
    return user_status.json()['response'][0]['online']

CALLER = os.getenv('NUMBER_FROM')
RECEIVER = os.getenv('NUMBER_TO')

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

def sms_sender(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_=CALLER,
        to=RECEIVER
    )
    return message.sid

def vk_user_name(user_id):
    params = {
                'user_ids': vk_id,
                'v': VK_API_VERSION,
                'fields': 'online',
                'access_token': VK_TOKEN
            }
    try:
        first_name = requests.post(url=URL_VK_API, params=params)
    except:
        print('An exception occurred')
    return first_name.json()['response'][0]['first_name']

if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            first_name = vk_user_name(vk_id)
            sms_sender(f'{first_name} {vk_id} сейчас онлайн! Машуня молодец!')
            break
        time.sleep(5)
