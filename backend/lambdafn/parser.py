

def parse_launch(launch, rocket_name, launchpad_name):
    return {
        "mission_name": launch.get("name", "Unknown"),
        "launch_date": launch.get("date_utc", ""),
        "rocket_id": launch.get("rocket", ""),
        "rocket_name": rocket_name,
        "status": (
            "success" if launch.get("success") else
            "failed" if launch.get("success") is False else
            "upcoming"
        ),
        "launchpad_id": launch.get("launchpad", ""),
        "launchpad": launchpad_name,
    }