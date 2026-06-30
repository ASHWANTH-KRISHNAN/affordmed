# AffordMed Vehicle Maintenance Scheduler Microservice

A lightweight Flask microservice for scheduling vehicle maintenance tasks used by the AffordMed platform.

## Features
- Exposes a simple HTTP API for scheduling maintenance jobs.
- Provides a test endpoint at `/schedule`.
- Includes authentication helpers and token utilities.
- Contains `scheduler` worker logic and service modules for vehicle/depot interactions.

## Quickstart (Windows)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and set environment variables as needed.

4. Run the app locally:

```powershell
python app.py
```

The service will respond at `http://127.0.0.1:5000/`. The root returns a short JSON with `test_endpoint: /schedule`.

## Files of interest
- `app.py` — Flask application entrypoint.
- `scheduler.py` — Scheduler process for background jobs.
- `routes/scheduler_routes.py` — HTTP routes for schedule operations.
- `auth.py`, `get_token.py`, `register.py` — authentication and token utilities.
- `services/vehicle_service.py`, `services/depot_service.py` — service-layer code.

## Environment
Populate `.env` with any required credentials and configuration. See `.env.example` for keys used by the app.

## Development
- Use the scheduler in background during development: `python scheduler.py` or run both app and scheduler in separate terminals.
- Add tests and CI as needed.

## Contributing
PRs are welcome. Open issues for bugs or feature requests.

## License
Specify your license here (e.g., MIT).