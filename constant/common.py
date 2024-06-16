"""
The script contains some constants values.
"""

class CommonConstant:

    SCRIPT_PATH = "run.py"
    TRIGGER_ARG_NAME = "--data"


class APIConstant:

    SUCCESS_RESPONSE_KEY = "Success"
    ERROR_RESPONSE_KEY = "Error"
    TRIGGER_SUCCESS_MSG = "Successfully triggered run!"
    TRIGGER_ERROR_MSG = "Error while triggering run!"
    VALIDATION_ERROR_MSG = "Error while validating the requst {e}!"
    INTERNAL_ERROR_MSG = "An error occured {e}!"
    ANALYZER_ALLOWED_METHODS = ['GET','POST']
    HEALTH_CHECK_ALLOWED_METHODS = ['GET']
    

class HttpStatusCode:

    RESPONSE_OK = 200
    ACCPETED = 202
    BAD_REQUEST = 400
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500


class APIValidationSchema:

    ANALYZER_START_REQUEST_SCHEMA = {
        "video": {
            "type": "dict",
            "required": True,
            "schema": {
                "url": {"type": "string", "required": True},
                "gameDate": {
                    "type": "string", 
                    "required": True, 
                    "regex": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z$"
                },
                "videoInfo": {
                    "type": "dict",
                    "required": True,
                    "schema": {
                        "duration": {"type": "integer"},
                        "start_time": {"type": "integer"},
                        "bit_rate": {"type": "integer"},
                        "codec": {"type": "string"},
                        "size": {"type": "integer"},
                        "width": {"type": "integer"},
                        "height": {"type": "integer"},
                    },
                },
            },
        },
        "user": {
            "type": "dict",
            "required": True,
            "schema": {
                "userID": {"type": "string", "required": True},
                "videoID": {
                    "type": "string",
                    "required": True,
                    "regex": r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                },
                "projectID": {
                    "type": "string",
                    "required": True,
                    "regex": r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
                },
            },
        },
        "task": {
            "type": "dict",
            "schema": {
                "param1": {"type": "integer"},
                "param2": {"type": "string"},
            },
        },
    }
