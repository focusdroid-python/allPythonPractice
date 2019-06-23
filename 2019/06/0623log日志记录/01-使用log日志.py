import logging

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:')


logging.info('这是 logging info message')
logging.debug('这是 logging debug message')
logging.warning('这是 logging warning message')
logging.error('这是 logging error message')
logging.critical('这是 logging critical message')