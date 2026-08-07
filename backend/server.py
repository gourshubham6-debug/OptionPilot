from flask import Flask, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo
from smartapi_client import login

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "OptionPilot",
        "version": "0.1",
        "status": "running"
    })


@app.route("/status")
def status():
    return jsonify({
        "server": "online",
        "market": "OPEN",
        "signal": "WAIT"
    })


@app.route("/time")
def current_time():
    india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    return jsonify({
        "time": india_time.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "Asia/Kolkata"
    })

@app.route("/market")
def market():
    try:
        obj, session = login()

        return jsonify({
            "status": "connected",
            "broker": "Angel One",
            "market": "OPEN",
            "signal": "WAIT",
            "message": "Angel One login successful"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


@app.route("/quote")
def quote():
    try:
        obj, session = login()

        # Live market data will be added here in V2
        return jsonify({
            "status": "ready",
            "message": "Login successful. Quote API will be added next."
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
