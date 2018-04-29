#!/bin/bash

pip3 install --upgrade -r requirements.txt -t "$(pwd)/deps"
export PYTHONPATH="$(pwd)/ez_dynamo_db;$(pwd)/ez_logging;$(pwd)/deps;${PYTHONPATH}"