"""
The script contains the basic setup for the flask app.
"""

import pytest
from flask import Flask

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    return app

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()