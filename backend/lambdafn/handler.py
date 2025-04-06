import os
import requests
import boto3
from datetime import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def fetch_launches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def upsert_launch(launch):
    item = {
        'id': launch['id'],
        'mission_name': launch['name'],
        'rocket_name': launch['rocket'],
        'launch_date': launch['date_utc'],
        'status': 'success' if launch['success'] else ('failed' if launch['success'] is False else 'upcoming'),
        'launchpad': launch['launchpad']
    }
    table.put_item(Item=item)

def main(event, context):
    try:
        launches = fetch_launches()
        count = 0
        for launch in launches:
            upsert_launch(launch)
            count += 1

        return {
            'statusCode': 200,
            'body': f'Processed {count} launches.'
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
