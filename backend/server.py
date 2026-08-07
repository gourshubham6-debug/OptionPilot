from datetime import datetime

@app.route("/time")
def current_time():
    return jsonify({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })from flask import Flask, jsonify

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
