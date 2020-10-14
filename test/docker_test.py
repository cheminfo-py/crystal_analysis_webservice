# -*- coding: utf-8 -*-
"""Test if the API responds in the Docker image"""
import sys
import os
import requests

JULIAPACKAGE = os.getenv("JULIAPACKAGE")


r = requests.get("http://localhost:8091/version/")
keys = r.json().keys()
if "version" in keys:
    print("OK")
else:
    print("error")
    sys.exit(1)

if JULIAPACKAGE:
    print(JULIAPACKAGE)
    sys.exit(0)
else:
    print("error")
    sys.exit(1)
