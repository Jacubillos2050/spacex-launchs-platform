def parse_launch(data):
    return {
        'id': data.get('id'),
        'mission_name': data.get('name')
    }
