import datetime
from  ez_dynamo.ez_dynamo_db import EZDynamoDBTable
from ez_logging import ez_logging

# Set logging options
ez_logging.set_logging()

# Upload Plant Data
tomato_data = '{"PlantName": "Tomato",  \
   "Metrics": {                         \
       "Humidity":{                     \
           "Ideal": 1,                  \
           "AlertLow": 0,               \
           "AlertHigh": 2               \
       },                               \
       "Temperature":{                  \
        "Ideal": 1,                     \
        "AlertLow": 0,                  \
        "AlertHigh": 2                  \
        },                              \
        "pH":{                          \
            "Ideal": 1,                 \
            "AlertLow": 0,              \
            "AlertHigh": 2              \
        }                               \
    }                                   \
}' 
plant_data_table = EZDynamoDBTable("Urban_Garden_Plant_Data", "templates/Urban_Garden_Plant_Data.json")
plant_data_table.upload(tomato_data)

# Upload Plant Info
tomato_plant_12_info = '{                           \
    "PlantID": "12",                                \
    "Timestamp": "Sun Apr 29 15:46:09 EDT 2018",    \
    "PlantType": "Tomato",                          \
    "PlanterIDs": ["abc123"]                        \
}'
plant_info_table = EZDynamoDBTable("Urban_Garden_Plant_Info", "templates/Urban_Garden_Plant_Info.json")
plant_info_table.upload(tomato_data)

# Upload Planter Info
planter_1002_info ='{                       \
    "PlanterID": "1002",                    \
    "PlantID": "12",                        \
    "IoTDeviceID":"dm1ioj210en",            \
    "Location": {                           \
        "Address":"The Moon, #1",           \
        "Row":"89"                          \
    }                                       \
}'
planter_info_table = EZDynamoDBTable("Urban_Garden_Planter_Info", "templates/Urban_Garden_Planter_Info.json")
planter_info_table.upload(planter_1002_info)


# Upload Plant Status
tomato_plant_status_sensor_reading = '{     \
   "PlantID": "12",
   "Timestamp": "Sun Apr 29 15:46:09 EDT 2018",
   "Planter":{
       "ID": "1002"
   },
   "IoT Device":{
        "ID":"dm1ioj210en",
        "Version":"123"
   },
   "SensorType":"Humidity",
   "SensorValue":1
}'
plant_status_table = EZDynamoDBTable("Urban_Garden_Plant_Status", "templates/Urban_Garden_Plant_Status.json")
planter_status_table.upload(tomato_plant_status_sensor_reading)