import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
log_handler = logging.StreamHandler()
log_handler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s', datefmt='%m.%d.%Y %I:%M:%S %p'))
root_logger.addHandler(log_handler)