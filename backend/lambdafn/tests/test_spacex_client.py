import requests
from unittest.mock import patch
from lambdafn import spacex_client


@patch("lambdafn.spacex_client.requests.get")
def test_fetch_launches(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"name": "Demo"}]

    launches = spacex_client.fetch_launches()
    assert isinstance(launches, list)
    assert launches[0]["name"] == "Demo"


@patch("lambdafn.spacex_client.requests.get")
def test_fetch_rocket_name(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"name": "Falcon 9"}

    name = spacex_client.fetch_rocket_name("rocket_id")
    assert name == "Falcon 9"


@patch("lambdafn.spacex_client.requests.get")
def test_fetch_rocket_name_fallback(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}

    name = spacex_client.fetch_rocket_name("unknown_id")
    assert "Unknown Rocket" in name


@patch("lambdafn.spacex_client.requests.get")
def test_fetch_launchpad_name(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"name": "Pad 39A"}

    name = spacex_client.fetch_launchpad_name("launchpad_id")
    assert name == "Pad 39A"


@patch("lambdafn.spacex_client.requests.get")
def test_fetch_launchpad_name_fallback(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}

    name = spacex_client.fetch_launchpad_name("unknown_id")
    assert "Unknown Launchpad" in name
