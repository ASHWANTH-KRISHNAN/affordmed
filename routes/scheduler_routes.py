from flask import Blueprint, jsonify
from services.depot_service import fetch_depots
from services.vehicle_service import fetch_vehicles
from scheduler import optimize_vehicle_tasks
from logging_middleware import log

scheduler_bp = Blueprint("scheduler", __name__)


@scheduler_bp.route("/schedule", methods=["GET"])
def schedule_maintenance():
    try:
        depots = fetch_depots()
        vehicles = fetch_vehicles()

        result = []
        for depot in depots:
            depot_id = depot.get("ID")
            mechanic_hours = int(depot.get("MechanicHours", 0))
            optimized = optimize_vehicle_tasks(vehicles, mechanic_hours)

            result.append({
                "depotID": depot_id,
                "availableMechanicHours": mechanic_hours,
                **optimized,
            })

        log("backend", "info", "controller", "Maintenance schedule generated")
        return jsonify({"schedules": result}), 200

    except Exception as error:
        log("backend", "fatal", "controller", f"Schedule generation failed: {error}")
        return jsonify({"error": "Unable to generate schedule"}), 500
