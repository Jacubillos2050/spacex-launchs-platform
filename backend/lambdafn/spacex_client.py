import requests

def fetch_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_rocket_name(rocket_id):
    url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("name", f"Unknown Rocket ({rocket_id})")

def fetch_launchpad_name(launchpad_id):
    url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("name", f"Unknown Launchpad ({launchpad_id})")
