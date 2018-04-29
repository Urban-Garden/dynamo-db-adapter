import datetime
from  ez_dynamo.ez_dynamo_db import EZDynamoDBTable
from ez_logging import ez_logging

# Set logging options
ez_logging.set_logging()

# Instantiate a simplified handler for DynamoDB, one handler per table.
plant_status_handle = EZDynamoDBTable("Urban_Garden_Plant_Status", "schemas/Urban_Garden_Plant_Status.json")

# Create data entry and format in a dictionary. Limited validation; keys should match the DB and values should be valid.
data = {'PlantID': 'ABC123', 'Timestamp': datetime.datetime.today().isoformat(), 'Sensors': {'Humidity': 50}}

# Upload to the DB
plant_status_handle.upload(data)