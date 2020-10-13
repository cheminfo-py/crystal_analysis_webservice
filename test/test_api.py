# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from topology_webservice import __version__, app

client = TestClient(app)