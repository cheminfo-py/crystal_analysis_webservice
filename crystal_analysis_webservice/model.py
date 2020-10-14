# -*- coding: utf-8 -*-
from . import __version__
from typing import Optional

from pydantic import BaseModel, validator


class CrystalanalysisModel(BaseModel):
    filecontent: str
    extension: Optional[str] = "cif"


class TopologyResponse(BaseModel):
    rcsr_name: str
    api_version: Optional[str] = __version__
