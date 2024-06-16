"""
The script contains utility functions for analyzer endpoint
"""

#imports
import threading
import subprocess


def trigger_run(script_path, parameters):
    """
    Function to trigger the run.py task
    :parma script_path: path for task file of string
    :param parameters: list of parameters to pass to invoke the file
    :return trigger_flag: boolean value representing the success status of process triggerd 
    """
    try:
        #creating subprocess to trigger run.py
        thread = threading.Thread(target=subprocess.run, args=(["python", script_path] + parameters,))
        thread.start()
        return True
    except Exception as e:
        print("Error in trigger", e)
        return False

