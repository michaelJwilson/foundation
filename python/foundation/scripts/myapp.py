from __future__ import annotations

import logging
import logging.config

from foundation.tools import calculate_pi

logging.config.fileConfig("logging.conf")


logger = logging.getLogger("FOUNDATION")

pi = calculate_pi(6)

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")

logger.info("Found pi to be {pi}", extra={"pi": pi})
