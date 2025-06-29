import logging

def get_logger(name):
    """
    Create and configure a logger with the specified name.

    If the logger does not already have handlers, a StreamHandler with a
    specific format is added. The logger level is set to INFO.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        
        # Add a stream handler with a custom formatter if no handlers exist
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
