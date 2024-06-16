"""
The script contains functions to validate the request.
"""

#imports
from cerberus import Validator

from constant.common import APIValidationSchema


def validate_request(data):
    """
    Function to validate the request data.
    :param data: dictionary containing request data
    :return data: validated dictionary with request data
    :return msg: err message if any
    """
    try:
        v = Validator()
        schema = APIValidationSchema.ANALYZER_START_REQUEST_SCHEMA
        if not v.validate(data, schema):
            msg = v.errors
            return None, msg
        return data, None
    except:
        raise
    