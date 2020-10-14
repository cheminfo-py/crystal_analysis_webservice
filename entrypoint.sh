#!/bin/bash
set -e

export JULIAPACKAGE=$(julia -e 'using CrystalNets; println(pathof(CrystalNets))')

exec "$@"