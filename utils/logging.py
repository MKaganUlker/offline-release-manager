"""
Centralized logging configuration.

Design goals:
- Single log location
- Append-only behavior
- Human-readable format
- Safe for offline environments

All modules should obtain loggers via get_logger().
"""

import logging
from pathlib import Path

# Base directory for all application data
BASE_DIR = Path.home() / ".offline_release_manager"

# Dedicated log directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "launcher.log"


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.

    Ensures:
    - No duplicate handlers
    - Consistent formatting
    - File-based persistence
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
