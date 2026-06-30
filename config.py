import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://4.224.186.213/evaluation-service")
EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
ROLL_NO = os.getenv("ROLL_NO")
ACCESS_CODE = os.getenv("ACCESS_CODE")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PORT = int(os.getenv("PORT", 5000))
MOBILE_NO = os.getenv("MOBILE_NO")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")