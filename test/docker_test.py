# -*- coding: utf-8 -*-
"""Test if the API responds in the Docker image"""
import sys

import requests
import os
import json

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


r = requests.get("http://localhost:8091/version/")
keys = r.json().keys()
if "version" in keys:
    print("OK")
else:
    print("error")
    sys.exit(1)

with open(os.path.join(THIS_DIR, "HKUST-1.cif"), "r") as fh:
    content = fh.read()
r = requests.post(
    "http://localhost:8091/topology/", data=json.dumps({"fileContent": content})
)
response = r.json()

if response["rcsrName"] == "tbo":
    print("tbo found for HKUST")
    sys.exit(0)
else:
    print("error")
    sys.exit(1)
