import sys
import logging
import os
import boto3
import re

# sys.path.insert(0, '/var/task/dep/')

logging.root.setLevel(os.getenv("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

def handler_echo(event, context): 
    logger.debug("Incoming debug event: %s", event)
    message = 'Hello {} {}!'.format(event['first_name'], 
                                        event['last_name'])
    return { 
            'message' : message
    }