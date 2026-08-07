from flask import Flask, jsonify
from datetime import datetime
from smartapi_client import login

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "app": "OptionPilot",
        "status": "running",
        "version": "0.1"
    })


@app.route("/status")
def status():
    return jsonify({
        "server": "online",
        "market": "closed",
        "signal": "waiting"
    })


@app.route("/time")
def current_time():
    return jsonify({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
