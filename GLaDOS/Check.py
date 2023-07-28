import requests
from fake_useragent import UserAgent

URL = "https://glados.rocks/api/user/checkin"
URL2 = "https://glados.rocks/api/user/status"
REFERER = 'https://glados.rocks/console/checkin'
ORIGIN = "https://glados.rocks"

def check_in(cookie):
    ua = UserAgent()
    user_agent = ua.random

    payload = {'token': 'glados.network'}

    headers = {
        'cookie': cookie,
        'referer': REFERER,
        'origin': ORIGIN,
        'user-agent': user_agent,
        'content-type': 'application/json;charset=UTF-8'
    }

    checkin_response = requests.post(URL, headers=headers, json=payload)
    state_response = requests.get(URL2, headers=headers)

    checkin_data = checkin_response.json()
    state_data = state_response.json()

    message = checkin_data['message']
    left_days = state_data['data']['leftDays'].split('.')[0]

    msg = f'checkin: {checkin_response.status_code} | state: {state_response.status_code}\n{message}\n剩余天数：{left_days}天'

    return f'{message}，剩余{left_days}天', msg