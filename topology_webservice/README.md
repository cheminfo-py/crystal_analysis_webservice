# topology_webservice

![Docker Image Build and Test CI](https://github.com/cheminfo-py/topology_webservice/workflows/Docker%20Image%20Build%20CI/badge.svg)

This is a webservice built using [FastAPI](https://github.com/tiangolo/fastapi). It exposes the great [Julia topology analysis code developed by Lionel Zoubritzky](https://github.com/coudertlab/CrystalNets.jl).

## Usage

To be usable on Heroku or Dokku, which use `PORT`environmental variables, you need to either create this environmental variable or put it into an `.env` file. For local development, the `run_docker.sh` script uses `8091`.

```bash
./build_docker # builds the docker image
./run_docker # starts the service
```

For production, you may want to use Docker compose

```bash
docker-compose up
```

## Docs

You find docs on `http://127.0.0.1:$PORT/docs.`
