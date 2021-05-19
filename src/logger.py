import logging


dict_log_formats = {
    "DEBUG": "%(asctime)s | %(module)s | %(funcName)s | %(lineno)d | %(levelname)s - %(message)s",
    "INFO": "%(message)s",
}


def get_logger(module, log_level="DEBUG"):
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, log_level.upper()))
    return logger


# set up the default streamhandler for the logger
def init_default_handler(logger, log_level="DEBUG"):
    log_level = log_level.upper()
    _handler = logging.StreamHandler()
    _handler.setLevel(getattr(logging, log_level))
    _handler.setFormatter(logging.Formatter(dict_log_formats.get(log_level)))
    logger.addHandler(_handler)
