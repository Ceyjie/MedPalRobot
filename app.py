from flask import Flask, render_template, request, jsonify
import motor_control as motors
import atexit

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/forward")
def forward():
    motors.forward()
    return jsonify({"status": "forward"})


@app.route("/backward")
def backward():
    motors.backward()
    return jsonify({"status": "backward"})


@app.route("/left")
def left():
    motors.left()
    return jsonify({"status": "left"})


@app.route("/right")
def right():
    motors.right()
    return jsonify({"status": "right"})


@app.route("/stop")
def stop():
    motors.stop()
    return jsonify({"status": "stop"})


@app.route("/speed", methods=["POST"])
def set_speed():
    value = float(request.json["speed"])
    motors.set_speed(value)
    return jsonify({"status": "speed set"})


# Safety: Stop motors when program exits
def cleanup():
    motors.stop()

atexit.register(cleanup)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)