import logging
from runtime.paths import LOGS

def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    log.propagate = False

    if not log.handlers:
        h = logging.FileHandler(LOGS / "launcher.log")
        h.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        ))
        log.addHandler(h)

    return log
