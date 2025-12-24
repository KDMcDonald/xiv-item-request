# Standard Libraries
import logging
import datetime

def setup_logger(name : str | None = None, log_destination : str = '.') -> logging.Logger:
    # Get datetime in proper format
    now = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')

    # Setup logger
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)

    # Setup file handler
    file_handler = logging.FileHandler(f'{log_destination}/{now}_log.txt')
    file_handler.setLevel(logging.DEBUG)

    # Setup log formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

