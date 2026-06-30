import requests
from config import BASE_URL, ACCESS_TOKEN

ALLOWED_STACK = {"backend", "frontend"}
ALLOWED_LEVEL = {"debug", "info", "warn", "error", "fatal"}
ALLOWED_BACKEND_PACKAGES = {
    "cache", "controller", "cron_job", "db", "domain", "handler",
    "repository", "route", "service"
}
ALLOWED_COMMON_PACKAGES = {"auth", "config", "middleware", "utils"}


def log(stack: str, level: str, package: str, message: str):
    """Mandatory logging middleware: sends logs to AffordMed log API."""
    stack = stack.lower()
    level = level.lower()
    package = package.lower()

    if stack not in ALLOWED_STACK:
        return None
    if level not in ALLOWED_LEVEL:
        return None
    if package not in ALLOWED_BACKEND_PACKAGES and package not in ALLOWED_COMMON_PACKAGES:
        return None

    if not ACCESS_TOKEN:
        return None

    try:
        response = requests.post(
            f"{BASE_URL}/logs",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
            json={
                "stack": stack,
                "level": level,
                "package": package,
                "message": message[:250],
            },
            timeout=5,
        )
        return response.json()
    except Exception:
        return None
