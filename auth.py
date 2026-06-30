import requests
from config import BASE_URL, EMAIL, NAME, ROLL_NO, ACCESS_CODE, CLIENT_ID, CLIENT_SECRET, MOBILE_NO, GITHUB_USERNAME


def register_user():
    payload = {
    "email": EMAIL,
    "name": NAME,
    "mobileNo": MOBILE_NO,
    "githubUsername": GITHUB_USERNAME,
    "rollNo": ROLL_NO,
    "accessCode": ACCESS_CODE,
}

    response = requests.post(f"{BASE_URL}/register", json=payload, timeout=10)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return {"error": response.text}

    return response.json()


def get_auth_token():
    payload = {
        "email": EMAIL,
        "name": NAME,
        "rollNo": ROLL_NO,
        "accessCode": ACCESS_CODE,
        "clientID": CLIENT_ID,
        "clientSecret": CLIENT_SECRET,
    }

    response = requests.post(f"{BASE_URL}/auth", json=payload, timeout=10)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return {"error": response.text}

    return response.json()