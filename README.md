# Easy DynamoDB Data Upload for Urban Gardben Project

A simplifying interface to AWS DunamoDB for the specific needs of the Urban Garden project.

## To get dependencies

~~~bash
pip3 install -r requirements.txt -t ./deps
~~~

## To run

~~~bash
export PYTHONPATH="$(pwd)/ez_dynamo_db;$(pwd)/ez_logging;$(pwd)/deps;${PYTHONPATH}"
python3 example_usage.py
~~~