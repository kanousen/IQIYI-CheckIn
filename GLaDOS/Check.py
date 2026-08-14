import json
import requests
from fake_useragent import UserAgent

# URL = "https://glados.rocks/api/user/checkin"
# URL2 = "https://glados.rocks/api/user/status"
# REFERER = 'https://glados.rocks/console/checkin'
# ORIGIN = "https://glados.rocks"

# URL = "https://glados.cloud/api/user/checkin"
# URL2 = "https://glados.cloud/api/user/status"
# REFERER = 'https://glados.cloud/console/checkin'
# ORIGIN = "https://glados.cloud"

# URL = "https://railgun.info/api/user/checkin"
# URL2 = "https://railgun.info/api/user/status"
# URL3 = "https://railgun.info/api/user/points"
# REFERER = 'https://railgun.info/console/checkin'
# ORIGIN = "https://railgun.info"

URL = "https://glados.one/api/user/checkin"
URL2 = "https://glados.one/api/user/status"
URL3 = "https://glados.one/api/user/points"
REFERER = 'https://glados.one/console/checkin'
ORIGIN = "https://glados.one"

UA = UserAgent()

def CheckIn(cookie):
    useragent = get_random_user_agent()
    payload = {
        'token': 'glados.one'
    }
    headers = {
        'cookie': cookie,
        'referer': REFERER,
        'origin': ORIGIN,
        'user-agent': useragent,
        'content-type': 'application/json;charset=UTF-8'
    }

    checkin = requests.post(URL, headers=headers, json=payload)
    state = requests.get(URL2, headers=headers)
    point = requests.get(URL3, headers=headers)

    mess = checkin.json()['message']
    time = state.json()['data']['leftDays']
    days = time.split('.')[0]
    # days = time

    points = point.json()['points'].split('.')[0]

    msg = f'{mess}\n剩余天数：{days}天 累积：{points}\ncheckin: {checkin.status_code} | state: {state.status_code}'

    checkin.close()
    state.close()
    return f'剩余天数：{days}天 累积：{points}', msg

def get_random_user_agent():
    random_user_agent = UA.random
    return random_user_agent
