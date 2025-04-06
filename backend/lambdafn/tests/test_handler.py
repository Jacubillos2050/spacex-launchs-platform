import pytest
import boto3
from moto import mock_dynamodb
from lambdafn import handler
from unittest.mock import patch

# Setup de DynamoDB simulado
@pytest.fixture
def setup_dynamodb():
    with mock_dynamodb():
        client = boto3.client('dynamodb', region_name='us-east-1')
        client.create_table(
            TableName='SpaceXLaunches',
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        yield

# Mock de la API de SpaceX
mock_launches = [
    {
        "id": "launch1",
        "name": "FalconSat",
        "rocket": "rocket_id",
        "date_utc": "2006-03-24T22:30:00.000Z",
        "success": False,
        "launchpad": "launchpad_id"
    },
    {
        "id": "launch2",
        "name": "CRS-20",
        "rocket": "rocket_id",
        "date_utc": "2020-03-07T04:50:31.000Z",
        "success": True,
        "launchpad": "launchpad_id"
    }
]

@patch("lambda.handler.fetch_launches", return_value=mock_launches)
def test_main_success(mock_fetch, setup_dynamodb, monkeypatch):
    monkeypatch.setenv("TABLE_NAME", "SpaceXLaunches")
    response = handler.main({}, {})
    assert response["statusCode"] == 200
    assert "Processed 2 launches" in response["body"]
