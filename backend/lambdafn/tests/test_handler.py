import boto3
import pytest
from moto import mock_dynamodb
from unittest.mock import patch
from lambdafn import handler

mock_launches = [
    {
        "name": "FalconSat",
        "date_utc": "2006-03-24T22:30:00.000Z",
        "rocket": "rocket_id_1",
        "success": False,
        "launchpad": "launchpad_id_1"
    },
    {
        "name": "CRS-20",
        "date_utc": "2020-03-07T04:50:31.000Z",
        "rocket": "rocket_id_2",
        "success": True,
        "launchpad": "launchpad_id_2"
    }
]


@pytest.fixture
def setup_dynamodb():
    with mock_dynamodb():
        client = boto3.client('dynamodb', region_name='us-east-1')
        client.create_table(
            TableName='LaunchesTable',
            KeySchema=[{'AttributeName': 'mission_name', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'mission_name', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        yield


@patch("lambdafn.handler.fetch_launchpad_name", side_effect=lambda x: f"Launchpad-{x}")
@patch("lambdafn.handler.fetch_rocket_name", side_effect=lambda x: f"Rocket-{x}")
@patch("lambdafn.handler.fetch_launches", return_value=mock_launches)
def test_main_success(mock_fetch_launches, mock_fetch_rocket, mock_fetch_launchpad, setup_dynamodb, monkeypatch):
    
    monkeypatch.setenv("TABLE_NAME", "LaunchesTable")

    response = handler.main({}, {})
    assert response["statusCode"] == 200

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table("LaunchesTable")

    item1 = table.get_item(Key={"mission_name": "FalconSat"})["Item"]
    item2 = table.get_item(Key={"mission_name": "CRS-20"})["Item"]

    assert item1["rocket_name"] == "Rocket-rocket_id_1"
    assert item2["launchpad"] == "Launchpad-launchpad_id_2"

@patch("lambdafn.handler.fetch_launches", side_effect=Exception("Test Error"))
def test_main_error(mock_fetch_launches, monkeypatch):
    monkeypatch.setenv("TABLE_NAME", "LaunchesTable")

    response = handler.main({}, {})
    assert response["statusCode"] == 500
    assert "Error: Test Error" in response["body"]

@patch("lambdafn.handler.fetch_launches", side_effect=Exception("Simulated error"))
def test_main_failure(mock_fetch_launches, monkeypatch):
    monkeypatch.setenv("TABLE_NAME", "LaunchesTable")
    response = handler.main({}, {})
    assert response["statusCode"] == 500
    assert "Simulated error" in response["body"]
