import os
from lambdafn.spacex_client import (
    fetch_launches,
    fetch_rocket_name,
    fetch_launchpad_name
)
from lambdafn.parser import parse_launch
from lambdafn.dynamodb_utils import upsert_launches

def main(event, context):
    table_name = os.environ["TABLE_NAME"]

    try:
        launches = fetch_launches()
        enriched_launches = []

        for launch in launches:
            rocket_name = fetch_rocket_name(launch["rocket"])
            launchpad_name = fetch_launchpad_name(launch["launchpad"])
            parsed = parse_launch(launch, rocket_name, launchpad_name)
            enriched_launches.append(parsed)

        upsert_launches(enriched_launches, table_name)

        return {
            "statusCode": 200,
            "body": f"Processed {len(enriched_launches)} launches"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
    