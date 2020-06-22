import time
import os
import requests

from dotenv import load_dotenv 
from twilio.rest import Client

load_dotenv()
vk_token = os.getenv('access_token')

def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': 5.92,
        'fields': 'online',
        'access_token': vk_token
    }
    user_status = requests.post(
        url='https://api.vk.com/method/users.get', 
        params=params
    )
    return user_status.json()['response'][0]['online']

caller = os.getenv('NUMBER_FROM')
receiver = os.getenv('NUMBER_TO')

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

def sms_sender(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_=caller,
        to=receiver
    )
    return message.sid

if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'Машуня {vk_id} сейчас онлайн! Машуня молодец!')
            break
        time.sleep(5)
