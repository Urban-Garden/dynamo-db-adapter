'''
A simplifed interface for uploading data (sensor readings) to DynamoDB.
Each object instance reprisents a handle to ONE table. 

Additional Dependencies:
  * Expects AWS credentials and config file in ~/.aws
  * Expects json files describing the DynamoDB row format template
'''

import boto3
import json
from ez_logging import ez_logging
import logging
from botocore.exceptions import ClientError, ValidationError


class EZDynamoDBTable():

  def __init__(self, table_name, DB_template_path):
    '''Initialze EZDynamoDBTable handle object 

        table_name: name of table in DynamoDB. Each handle is tied to ONE table.
        DB_template_path: path to json template for upload to DynamoDB. This should match the DB row structure.
    '''
    # Create DynamoDB handle
    self.dynamodb = boto3.resource('dynamodb')
    # Create DB Table handle
    self.table = self.dynamodb.Table(table_name)
    # Load table data template
    self.load_template(DB_template_path)

  def load_template(self,DB_template_path):
    '''Loads json definition of table request for simplified upload requests'''
    self.template = None
    try:
      with open(DB_template_path, mode='r') as f:
        template_string = f.read()
    except  IOError as e: 
      logging.warning("Template not loaded. Could not open file for reading.")
      print(e)
      return False
    try:
      self.template = json.loads(template_string)
    except json.decoder.JSONDecodeError as e:
      logging.debug("Failed to load json with error: \n" + e)
      logging.warning("Template not loaded.")
      return False
    return True


  def form_request_body(self, data):
    '''Takes a dictionary of values and populate the json request
    
      data: dictionary of DB row entries to upload
    '''
    request = self.template.copy()
    for key, value in data.items():
      # ! Does not check for matching nested keys
      # ! Does not validate the validity of values (i.e. is a request['Timestamp'] actually a timstamp)
      if key in request.keys():
        request[key] = value
      else:
        logging.warning("Key not in template")
        return False, None  
    return True, request

  def upload(self, data, overwrite=False):
    '''Upload data to the DynamoDB'''
    # Get request body using data and template
    retval, item = self.form_request_body(data)
    if retval is False:
      logging.warning("Unable to form request body")
      return False, None

    # Upload data row
    try:
      response = self.table.put_item(Item=item)
    except ClientError as e:
      logging.debug(e)
      return False, None
    except ValidationError as e:
      logging.warning("Could not validate template: " + e)
      return False, None
    
    logging.info("PutItem succeeded.")
    logging.debug(json.dumps(response, indent=4))
    return True, response['ResponseMetadata']['HTTPStatusCode']
