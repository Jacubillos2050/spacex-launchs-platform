from parser import parse_launch

def test_parse_launch():
    raw = {
        "name": "Test Mission",
        "date_utc": "2025-04-01T12:00:00.000Z",
        "rocket": "rocket123",
        "success": True,
        "launchpad": "padA"
    }
    parsed = parse_launch(raw)
    assert parsed["mission_name"] == "Test Mission"
    assert parsed["status"] == "success"
