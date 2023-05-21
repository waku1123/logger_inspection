from logging import Logger, getLogger
from lib.commons import LoggerName, get_logger, setup_logger, setup_logger_2
from lib.sub import sum


# yamlからlogger設定をロード
setup_logger()
# jsonからlogger設定をロード
# setup_logger_2()

logger: Logger = getLogger(__file__)

if __name__ == "__main__":
    logger.debug("DEBUG in main")
    logger.info("INFO in main")
    logger.warning("WARNING in main")
    logger.error("ERROR in main")
    logger.critical("CRITICAL in main")

    sum()

