"""
Central logging configuration for the PayFlow Intelligence Platform.

Provides a single logger instance that writes to both the console
and a log file.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

import logging
from logging.handlers import RotatingFileHandler

from src.utils.paths import LOGS_DIR
from src.utils.config import config


def get_logger(name: str = "payflow") -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(config.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File output
    file_handler = RotatingFileHandler(
        LOGS_DIR / "pipeline.log",
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=3,
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger