"""
The script will print the JSON message received from UI and send 10 messages to webhook.
"""

#imports
import os
import sys
# import time
import json
import requests
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('run.log', 'w')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    """
    The function will receive the JSON message from command line and send some messages to webhook.
    :param: None
    :return: None
    """
    try:
        #checking the command line arguments
        if len(sys.argv) != 3:
            # print("Usage: python run.py --data <json_data>")
            logger.info("Usage: python run.py --data <json_data>")
            raise Exception("Error while passing the arguments")

        #checking if command line argument has --data parameter
        if sys.argv[1] == "--data":
 
            data_json = sys.argv[2]
            data = json.loads(data_json)  # Deserialize the JSON string
            # print("Received data:", data)
            logger.info(f"from logger printing data {data}")
            url = "https://webhook.coditas.org/webhook"
            # url = "http://127.0.0.1:5555/webhook"
            # print(url)
            logger.info(f"from logger printing url {url}")
            # Read the .json file
            with open('data.json', 'r') as json_file:
                loaded_data = json.load(json_file)


            for data in loaded_data:
                response = requests.post(url, headers={"Content-Type":"application/json"}, data=json.dumps(data))
                if response.ok == True:
                    logger.info("from logger printing respones ok")
                    # print("Response is okk")
                else:
                    logger.info(f"from logger printing respones not ok reason is {response.reason}")
                    # print("Not okay because ", response.reason)
    
    except Exception as e:
        # print(e)
        logger.error(f"got error {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()