from json import dumps
from requests import post, get
from fake_useragent import UserAgent

def CheckIn(cookie):
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = get_ua()
    payload = {
        'token': 'glados.network'
    }
    checkin = post(
        url,
        headers={
            'cookie': cookie,
            'referer': referer,
            'origin': origin,
            'user-agent': useragent,
            'content-type': 'application/json;charset=UTF-8'
        },
        data=dumps(payload)
    )
    state = get(
        url2,
        headers={
            'cookie': cookie,
            'referer': referer,
            'origin': origin,
            'user-agent': useragent
        }
    )

    mess = checkin.json()['message']
    time = state.json()['data']['leftDays']
    days = time.split('.')[0]
    msg = f'checkin: {checkin.status_code} | state: {state.status_code}\n{mess}\n剩余天数：{days}天'

    checkin.close()
    state.close()

    return f'{mess}，剩余{days}天', msg

def get_ua():

    # 创建UserAgent对象
    user_agent = UserAgent()
    # 获取随机的User-Agent字符串
    random_user_agent = user_agent.random
    # 随机的User-Agent
    return random_user_agent
