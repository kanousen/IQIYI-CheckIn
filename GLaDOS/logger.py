import logging
from pytz import timezone
from datetime import datetime

def fix_timezone(sec, what):
    tz = timezone('Asia/Shanghai')
    timenow = datetime.now(tz)
    return timenow.timetuple()

# 创建logger对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # log等级总开关

formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")

# 控制台handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# 添加到logger
logger.addHandler(stream_handler)

# 设置日志时间戳转换器
logging.Formatter.converter = fix_timezone