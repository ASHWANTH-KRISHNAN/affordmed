from flask import Flask, jsonify
from routes.scheduler_routes import scheduler_bp
from config import PORT
from logging_middleware import log

app = Flask(__name__)
app.register_blueprint(scheduler_bp)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AffordMed Vehicle Maintenance Scheduler Microservice",
        "test_endpoint": "/schedule"
    })


if __name__ == "__main__":
    log("backend", "info", "route", "Flask server started")
    app.run(host="0.0.0.0", port=PORT, debug=True)
