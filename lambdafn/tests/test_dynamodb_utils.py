from lambdafn import dynamodb_utils

def test_upsert():
    item = {'id': '1', 'mission_name': 'Test'}
    assert dynamodb_utils.upsert_to_dynamodb(item)
