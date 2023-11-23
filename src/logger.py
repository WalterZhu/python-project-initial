import logging
import sys
from config import config

def setup_logger() -> logging.Logger:
    '''
    初始化日志管理器和格式化
    '''
    logger = logging.getLogger('logger')
    log_level_name = config.LOG_LEVEL
    log_level = getattr(logging, log_level_name.upper(), None)
    formatter = logging.Formatter('[%(levelname)s %(asctime)s] %(filename)s: %(message)s')

    if config.DEBUG == True:
        print('DEBUG模式')
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(config.LOG_FILE, encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
