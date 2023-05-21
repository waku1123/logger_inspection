from lib.commons import LoggerName, get_logger
from logging import Logger, getLogger


#logger: Logger = get_logger(LoggerName.APPLICATION)

# NOTE: logger_conf.yamlに定義されていない名前では
logger: Logger = getLogger(__file__)


def sum():
    logger.info("roop start")
    total: int = 0
    for i in range(10):
        total += 1
    logger.info("roop end")


