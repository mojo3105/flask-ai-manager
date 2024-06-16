"""
The script contains the unit test for startAnalyzer endpoint.
"""

#imports
import pytest
# from constant.common import HttpStatusCode
from flask import Flask
import json



@pytest.fixture
def correct_analyzer_request_payload():
    data = {
            "video":{
                "url":"<url>",
                "gameDate":"2020-07-29T18:16:41.506Z",
                "videoInfo":{
                    "duration":0,
                    "start_time":0,
                    "bit_rate":0,
                    "codec":"unknown",
                    "size":0,
                    "width":0,
                    "height":0
                }
            },
            "user":{
                "userID":"john.doe@mail.com",
                "videoID": "550e8400-e29b-41d4-a716-446655440000",
                "projectID": "5ae6d5f7-8d38-4e4e-8d31-35cfc80c1a18"
            },
            "task":{
                "param1":1,
                "param2":"hi"
            }
        }
    return data

@pytest.fixture
def create_client():
    app = Flask(__name__)
    return app.test_client


def test_analyzer_by_get(create_client):
    response = create_client().get('/startAnalyzer')
    assert response.status_code == 200


def test_analyzer_by_post(create_client, correct_analyzer_request_payload):
    response = create_client().post('/startAnalyzer', headers={'Content-Type':'application-json'}, 
                                    data=json.dumps(correct_analyzer_request_payload))
    assert response.status_code == 202


def test_node_status(create_client):
    response = create_client().get('/nodeStatus')
    assert response.status_coee == 200