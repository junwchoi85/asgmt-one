import logging
from logging.handlers import TimedRotatingFileHandler
import os

# logs 폴더가 존재하지 않으면 생성
if not os.path.exists('logs'):
    os.makedirs('logs')


def get_db_logger(name='db_logger', level=logging.DEBUG, log_file='logs/db.log'):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 콘솔 핸들러 설정
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # 파일 핸들러 설정 (날짜별로 로그 파일을 회전)
    file_handler = TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=7)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # 핸들러 추가
    # logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_app_logger(name='app_logger', level=logging.DEBUG, log_file='logs/app.log'):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 콘솔 핸들러 설정
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # 파일 핸들러 설정 (날짜별로 로그 파일을 회전)
    file_handler = TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=7)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # 핸들러 추가
    # logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_test_logger(name='test_logger', level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 콘솔 핸들러 설정
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # 핸들러 추가
    logger.addHandler(console_handler)

    return logger
