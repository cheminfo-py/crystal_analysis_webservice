"""
crystal_analysis_webservice.py
Expose the topology analysis tool developed by C Coudert's group
"""
from . import __version__, logger
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from .model import TopologyResponse, CrystalanalysisModel
from .core import run_topology_analysis

app = FastAPI(
    title="CrystalAnalysis webservice",
    description="his webservice provides Crystal analysis using the CrystalNets Julia package",
    version=__version__,
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/version")
def read_version():
    logger.debug("Got GET to /version")
    return {"version": __version__}


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>CrystalAnalysis webservice</title>
        </head>
        <h1> CrystalNet webservice </h1>
        <body>
            <p>This webservice provides CrystalNet analysis using the CrystalNets Julia package.</p>
            <p>Find the docs at <a href="./docs">/docs</a> and the openAPI specfication at <a href="./openapi.json">/openapi.json</a>.</p>
        </body>
    </html>
    """


@app.post("/topology", response_model=TopologyResponse)
def topology_analysis(parameters: CrystalanalysisModel):
    logger.debug("Got POST to /topology")
    try:
        return run_topology_analysis(parameters.fileContent, parameters.extension)
    except Exception as excep:
        logger.error("Crystal topology analysis failed {}".format(excep))
        raise HTTPException(
            status_code=400,
            detail="Crystal topology analysis failed due to {}".format(excep),
        )
