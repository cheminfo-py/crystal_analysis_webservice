"""
crystal_analysis_webservice
Expose the topology analysis tool developed by C Coudert's group
"""



# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

# Add imports here
from .crystal_analysis_webservice import *