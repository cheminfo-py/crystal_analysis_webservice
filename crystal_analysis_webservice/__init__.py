"""
crystal_analysis_webservice
Expose the topology analysis tool developed by C Coudert's group
"""

__version__ = "0.2.0"

from diskcache import Cache

cache = Cache()

# Add imports here
from .crystal_analysis_webservice import *
