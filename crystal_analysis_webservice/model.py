# -*- coding: utf-8 -*-
from . import __version__
from typing import Optional

from pydantic import BaseModel, validator


class CrystalanalysisModel(BaseModel):
    fileContent: str
    extension: Optional[str] = "cif"


class TopologyResponse(BaseModel):
    rcsrName: str
    apiVersion: Optional[str] = __version__
    rcsrLink: Optional[str]