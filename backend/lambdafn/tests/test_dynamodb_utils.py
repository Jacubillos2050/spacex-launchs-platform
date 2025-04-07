import boto3
import pytest
from moto import mock_dynamodb
from lambdafn.dynamodb_utils import upsert_launches

@pytest.fixture
def dynamodb_table():
    with mock_dynamodb():
        client = boto3.client("dynamodb", region_name="us-east-1")
        client.create_table(
            TableName="LaunchesTable",
            KeySchema=[{"AttributeName": "mission_name", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "mission_name", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST"
        )
        yield boto3.resource("dynamodb", region_name="us-east-1").Table("LaunchesTable")

def test_upsert_launches(dynamodb_table):
    data = [
        {
            "mission_name": "Test Mission",
            "launch_date": "2025-04-01T12:00:00.000Z",
            "rocket_id": "rocket_1",
            "rocket_name": "Falcon 9",
            "status": "success",
            "launchpad_id": "padA",
            "launchpad": "Pad 39A"
        }
    ]

    from lambdafn.dynamodb_utils import upsert_launches
    upsert_launches(data, "LaunchesTable")

    item = dynamodb_table.get_item(Key={"mission_name": "Test Mission"}).get("Item")

    assert item is not None
    assert item["rocket_name"] == "Falcon 9"
    assert item["launchpad"] == "Pad 39A"
