"""
The script contains small flask application with demo webhook.
"""

#imports
import logging
from flask import Flask, jsonify, request, Response


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/webhook', methods=['POST'])
def demo_webhook():
    """
    The function will handle the webhook request for '/webhook' endpoint.
    :param: None
    :return: Json response with appropriate message
    """
    if request.method == 'POST':
        # print("request method is post")
        status = 400
        response_key = "Error"
        try:
            data = request.json
            app.logger.info(f"Request data: {data}")
            status = 200
            response_key = "Success"
            response_msg = "Successfully received!"
        
        except Exception as e:
            response_msg = f"An error occured {e}!"
            app.logger.error(f"{response_msg}")
        
        finally:
            return jsonify({response_key:response_msg}), status


@app.route("/", methods=['GET'])
def index():
    """
    The function will handle request for '/' endpoint.
    """
    if request.method == 'GET':
        app.logger.info("welcome to flask webhook")
        return Response(response=b'health check success', status=200)
    
    return Response(status=405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)