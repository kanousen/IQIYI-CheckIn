from os import environ
from logger import logger
from Check import CheckIn
from push import send_msg_ServerChan, send_msg_PushPlus, send_msg_Qmsg


def main():
    # 获取actions secrets配置的cookie SendKey
    ck = environ["cookie"]
    SendKey = environ.get('SendKey')
    is_ServerChan_push = int(environ.get('is_ServerChan_push'))
    token = environ.get('token')
    is_PushPlus_push = int(environ.get('is_PushPlus_push'))
    key = environ.get('key')
    is_Qmsg_push = int(environ.get('is_Qmsg_push'))


    if not ck:
        logger.info('请先配置GLADOS_COOKIE！')
        return

    try:
        title, msg = CheckIn(ck)
        logger.info('GLaDOS 签到成功！')
    except Exception as err:
        logger.error('程序运行出错！')
        title = '程序运行出错！'
        msg = err
    finally:
        tmp = msg.split('\n')
        for i in tmp:
            logger.info(i)

        if is_ServerChan_push:         # server酱推送消息，无SendKey不推送
            rsp1 = send_msg_ServerChan(SendKey, title, msg)
            logger.info(rsp1)
        if is_PushPlus_push:            # pushplus推送消息，无token不推送
            rsp2 = send_msg_PushPlus(token, title, msg)
            logger.info(rsp2)
        if is_Qmsg_push:                # Qmsg推送消息，无key不推送
            rsp3 = send_msg_Qmsg(key, msg)
            logger.info(rsp3)


if __name__ == '__main__':
    main()