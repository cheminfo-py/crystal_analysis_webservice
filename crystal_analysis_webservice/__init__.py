"""
crystal_analysis_webservice
Expose the topology analysis tool developed by C Coudert's group
"""
import os
import logging
from fastapi.logger import logger


LOGLEVEL = os.getenv("LOGLEVEL")

if LOGLEVEL == "debug":
    logger.setLevel(logging.DEBUG)

from diskcache import Cache


__version__ = "0.2.0"


cache = Cache(size_limit=2 * 10 ** 7, disk_min_file_size=0)

# Add imports here
from .crystal_analysis_webservice import *
