# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
import os
import sys
from crystal_analysis_webservice import __version__, app

client = TestClient(app)

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


def test_read_main():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": __version__}


def test_topology_analysis():
    with open(os.path.join(THIS_DIR, "HKUST-1.cif"), "r") as fh:
        content = fh.read()
    response = client.post("/topology", json={"fileContent": content})
    assert response.status_code == 200
    body = response.json()
    assert "rcsrName" in body.keys()
    assert "apiVersion" in body.keys()
    assert body["rcsrName"] == "tbo"

    with open(os.path.join(THIS_DIR, "diamond.cif"), "r") as fh:
        content = fh.read()
    response = client.post("/topology", json={"fileContent": content})
    assert response.status_code == 200
    body = response.json()

    assert "rcsrName" in body.keys()
    assert "apiVersion" in body.keys()
    assert body["rcsrName"] == "dia"
