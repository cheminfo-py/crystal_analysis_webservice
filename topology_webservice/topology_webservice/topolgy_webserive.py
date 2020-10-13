"""
topology_webservice.py
Expose the topology analysis tool developed by C Coudert's group
"""
from . import __version__
from fastapi import FastAPI

app = FastAPI()


@app.get("/version")
def read_version():
    return {"version": __version__}
