"""
The script contain main code of flask application.
"""

#imports
import os
import logging
import json
from flask import Flask, jsonify, request, Response

from constant.common import APIConstant, HttpStatusCode, CommonConstant
from utils import trigger, validation

#creating flask app instance
app = Flask(__name__)

#configuring the logger
logging.basicConfig(filename='app.log', level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")


@app.route("/startAnalyzer", methods=APIConstant.ANALYZER_ALLOWED_METHODS)
def start_analyzer():
    """
    The function will handle the request for '/startAnalyzer' endpoint. And on successfull request will invoke run.py
    :param: None
    :return: Json Response with success/error message
    """
    if request.method == 'GET':
        app.logger.info("Inside the get request")
        return Response(response=b'hello get analyzer', status=HttpStatusCode.RESPONSE_OK)

    elif request.method == 'POST':

        app.logger.info("Received request to trigger run")
        # print("Got request")
        response_key = APIConstant.ERROR_RESPONSE_KEY
        status = HttpStatusCode.BAD_REQUEST

        try:
            data, msg = validation.validate_request(data=request.json)
            # print("got data ", data)
            
            #checking if any error message from validation
            if msg:
                app.logger.error(f"Validation Error occured : {msg}")
                response_msg = msg
                # print("validation error ", msg)
            else:
                # script_path = os.path.join(os.path.dirname(__file__), CommonConstant.SCRIPT_PATH)
                script_path = CommonConstant.SCRIPT_PATH
                parameters = [CommonConstant.TRIGGER_ARG_NAME, json.dumps(data)]
                # print("got script path and parameter ", script_path, parameters)
                #triggering run.py file
                trigger_flag = trigger.trigger_run(script_path, parameters)

                #checking if run.py triggered successfully
                if trigger_flag:
                    app.logger.info("Successfully triggered run.py")
                    # print("successfully triggered run")
                    response_msg = APIConstant.TRIGGER_SUCCESS_MSG
                    response_key = APIConstant.SUCCESS_RESPONSE_KEY
                    status = HttpStatusCode.ACCPETED
                else:
                    # print("failed to trigger")
                    app.logger.error("Failed to trigger run.py")
                    response_msg = APIConstant.TRIGGER_ERROR_MSG 
                    status = HttpStatusCode.BAD_REQUEST
        
        except Exception as e:
            response_msg = APIConstant.INTERNAL_ERROR_MSG.format(e=e)
            status = HttpStatusCode.BAD_REQUEST
            app.logger.error(response_msg)
            # print("main exception ", e)
        
        finally:
            app.logger.info(f"Return response: {response_key} : {response_msg}")
            # print(f"final message return {response_key} : {response_msg}")
            return jsonify({response_key:response_msg}), status
    
    return Response(status=HttpStatusCode.METHOD_NOT_ALLOWED)


@app.route("/nodeStatus", methods=APIConstant.HEALTH_CHECK_ALLOWED_METHODS)
def node_status():
    """
    The function will handle request for '/nodeStatus' endpoint.
    """
    if request.method == 'GET':
        app.logger.info("from logger in node status")
        # print("from print in node status")
        return Response(response=b'hello world', status=HttpStatusCode.RESPONSE_OK)
    
    return Response(status=HttpStatusCode.METHOD_NOT_ALLOWED)


@app.route("/", methods=APIConstant.HEALTH_CHECK_ALLOWED_METHODS)
def index():
    """
    The function will handle request for '/' endpoint.
    """
    if request.method == 'GET':
        print("welcome to app")
        app.logger.info('welcome to flask app')
        return Response(response=b'health check success', status=HttpStatusCode.RESPONSE_OK)
    
    return Response(status=HttpStatusCode.METHOD_NOT_ALLOWED)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)