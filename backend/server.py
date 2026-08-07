from flask import Flask, jsonify
from datetime import datetime

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
        "market": "closed",
        "signal": "waiting",
        "server": "online"
    })

@app.route("/time")
def current_time():
    return jsonify({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/market")
def market():
    return jsonify({
        "nifty": 25240.35,
        "banknifty": 57210.80,
        "market": "open"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
