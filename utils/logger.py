import logging


def configure_logger(name):
    """
    Configures and returns a logger instance.
    :param name: Name of the logger
    :return: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # File handler
    file_handler = logging.FileHandler("test_log.log")
    file_handler.setLevel(logging.DEBUG)
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
