import requests
from config import BASE_URL, ACCESS_TOKEN
from logging_middleware import log


def fetch_vehicles():
    try:
        response = requests.get(
            f"{BASE_URL}/vehicles",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
            timeout=10,
        )
        response.raise_for_status()
        log("backend", "info", "service", "Vehicles fetched successfully")
        return response.json().get("vehicles", [])
    except Exception as error:
        log("backend", "error", "service", f"Failed to fetch vehicles: {error}")
        raise
