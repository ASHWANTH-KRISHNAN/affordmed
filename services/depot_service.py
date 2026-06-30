import requests
from config import BASE_URL, ACCESS_TOKEN
from logging_middleware import log


def fetch_depots():
    try:
        response = requests.get(
            f"{BASE_URL}/depots",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
            timeout=10,
        )
        response.raise_for_status()
        log("backend", "info", "service", "Depots fetched successfully")
        return response.json().get("depots", [])
    except Exception as error:
        log("backend", "error", "service", f"Failed to fetch depots: {error}")
        raise
