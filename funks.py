import os
import logging
import datetime
from functools import wraps
from logging.handlers import RotatingFileHandler


def summary(*args):
    return sum(args)


def get_string(log_message):
    logger = logging.getLogger('main.log')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler('main.log', backupCount=10, maxBytes=1000000)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger.info(log_message)

def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        res = old_function(*args, **kwargs)
        string = f'\n{datetime.datetime.now()} | выполнение {old_function.__name__} | c аргументами {args}|{kwargs} | результат : {res}'
        get_string(string)
        return res
    return new_function

def logger2(path='main.log'):
    def logger_2(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            res = old_function(*args, **kwargs)
            logger = logging.getLogger(path)
            logger.setLevel(logging.DEBUG)
            handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            string = f'\n{datetime.datetime.now()} | выполнение {old_function.__name__} | c аргументами {args}|{kwargs} | результат : {res}'

            logger.info(string)
            return res
        return new_function
    return logger_2