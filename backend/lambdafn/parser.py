def parse_launch(launch):
    return {
        "mission_name": launch.get("name", "Unknown"),
        "launch_date": launch.get("date_utc", ""),
        "rocket_id": launch.get("rocket", ""),
        "status": (
            "success" if launch.get("success") else
            "failed" if launch.get("success") is False else
            "upcoming"
        ),
        "launchpad_id": launch.get("launchpad", "")
    }