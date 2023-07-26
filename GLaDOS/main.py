from os import environ
import logging

from logger import logger
from Check import CheckIn
from push import send_msg_ServerChan, send_msg_PushPlus, send_msg_Qmsg


def get_environment_variable(name):
    value = environ.get(name)
    if not value:
        logger.info(f'请先配置{name}！')
    return value


def send_push_message(title, msg, send_func):
    if send_func:
        try:
            response = send_func(title, msg)
            logger.info(response)
        except Exception as err:
            logger.error('推送消息出错！')
            logger.error(err)


def main():
    # 获取actions secrets配置的cookie SendKey
    ck = get_environment_variable("GLADOS_COOKIE")
    SendKey = get_environment_variable('SendKey')
    is_ServerChan_push = int(get_environment_variable('is_ServerChan_push'))
    token = get_environment_variable('token')
    is_PushPlus_push = int(get_environment_variable('is_PushPlus_push'))
    key = get_environment_variable('key')

    if not ck:
        return

    try:
        title, msg = CheckIn(ck)
        logger.info('GLaDOS 签到成功！')
    except Exception as err:
        logger.error('程序运行出错！')
        title = '程序运行出错！'
        msg = str(err)
    finally:
        tmp = msg.split('\n')
        for i in tmp:
            logger.info(i)

        send_push_message(title, msg, lambda t, m: send_msg_ServerChan(SendKey, t, m) if is_ServerChan_push else None)
        send_push_message(title, msg, lambda t, m: send_msg_PushPlus(token, t, m) if is_PushPlus_push else None)
        send_push_message(title, msg, lambda _, m: send_msg_Qmsg(key, m) if is_Qmsg_push else None)


if __name__ == '__main__':
    main()