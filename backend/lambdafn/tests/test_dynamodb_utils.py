from moto import mock_dynamodb
import boto3
import os
import time
from lambdafn import dynamodb_utils

@mock_dynamodb
def test_upsert_launches():
    os.environ["TABLE_NAME"] = "LaunchesTable"
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

    table = dynamodb.create_table(
        TableName="LaunchesTable",
        KeySchema=[{"AttributeName": "mission_name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "mission_name", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

    # Esperar a que la tabla esté lista
    table.meta.client.get_waiter('table_exists').wait(TableName="LaunchesTable")
    time.sleep(1)

    launches = [{
        "mission_name": "MissionX",
        "launch_date": "2025",
        "rocket_id": "rx",
        "status": "success",
        "launchpad_id": "pad"
    }]

    result = upsert_launches(launches, dynamodb=dynamodb)

    assert result["inserted"] == ["MissionX"]
    assert result["total"] == 1
