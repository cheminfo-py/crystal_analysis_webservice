#!/bin/bash

echo "connect to http://localhost:8091"
docker run -d -p 8091:8091 -e PORT=8091 --rm --name=crystal_analysis_webserviceinstance crystal_analysis_webservice
