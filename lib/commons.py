from enum import Enum
from logging import getLogger, Logger
from logging.config import dictConfig

import json
from yaml import FullLoader, load


class LoggerName(Enum):
    """
    ロガー名定義
    """
    CONSOLE = "console"
    APPLICATION = "application"

def setup_logger(filename="config/logger_conf.yaml"):
    """ロガー設定(yaml)をロード"""
    with open(filename) as file:
        dictConfig(load(file.read(), FullLoader))

def setup_logger_2(filename="config/logger_conf.json"):
    """ロガー設定(yaml)をロード"""
    with open(filename, "rb") as file:
        _json = json.load(file)
        dictConfig(_json)


def get_logger(name: LoggerName = LoggerName.APPLICATION) -> Logger:
    return getLogger(name.value)

