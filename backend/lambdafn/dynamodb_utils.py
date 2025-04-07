import boto3
import os

def upsert_launches(launches, table_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

    table = dynamodb.Table(table_name)
    inserted = []

    for launch in launches:
        resp = table.get_item(Key={"mission_name": launch["mission_name"]})
        item_exists = "Item" in resp

        table.put_item(Item=launch)
        if not item_exists:
            inserted.append(launch["mission_name"])

    return {"inserted": inserted, "total": len(launches)}