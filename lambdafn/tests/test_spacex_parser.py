from lambdafn import spacex_parser

def test_parse_launch():
    launch = {'id': 'abc123', 'name': 'Starlink'}
    parsed = spacex_parser.parse_launch(launch)
    assert parsed['mission_name'] == 'Starlink'
