import os
import json
import requests
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

# Cache para evitar llamadas duplicadas
rocket_cache = {}
launchpad_cache = {}

def fetch_launches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_rocket_name(rocket_id):
    if rocket_id in rocket_cache:
        return rocket_cache[rocket_id]
    response = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
    response.raise_for_status()
    rocket_name = response.json()['name']
    rocket_cache[rocket_id] = rocket_name
    return rocket_name

def fetch_launchpad_name(launchpad_id):
    if launchpad_id in launchpad_cache:
        return launchpad_cache[launchpad_id]
    response = requests.get(f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}')
    response.raise_for_status()
    launchpad_name = response.json()['name']
    launchpad_cache[launchpad_id] = launchpad_name
    return launchpad_name

def upsert_launch(launch):
    item = {
        'id': launch['id'],
        'mission_name': launch['name'],
        'rocket_name': fetch_rocket_name(launch['rocket']),
        'launch_date': launch['date_utc'],
        'status': (
            'success' if launch['success'] else
            ('failed' if launch['success'] is False else 'upcoming')
        ),
        'launchpad': fetch_launchpad_name(launch['launchpad'])
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
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': f'Processed {count} launches.'
            })
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }

