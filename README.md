# Easy DynamoDB Data Upload for Urban Gardben Project

A simplifying interface to AWS DunamoDB for the specific needs of the Urban Garden project.

## Prerequisites

1. The DynamoDB Table(s) you want to upload to must already exist
2. You must create json templates in the ```templates``` directory to match the format of the DynamoDB table.
2. AWS ```config``` and ```credentials``` files in ```~/.aws``` must be correctly set. Use the AWS CLI to provision.

## Dependencies

~~~bash
pip3 install -r requirements.txt -t ./deps
~~~

## To Run

~~~bash
export PYTHONPATH="$(pwd)/ez_dynamo_db;$(pwd)/ez_logging;$(pwd)/deps;${PYTHONPATH}"
python3 example_usage.py
~~~