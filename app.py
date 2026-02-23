from flask import Flask, render_template, request, jsonify
import motor_control as motors
import atexit
from motor_control import test_motor_pins_with_led

app = Flask(__name__)


# ======================
# Main Page
# ======================
@app.route("/")
def index():
    return render_template("index.html")


# ======================
# Movement Routes
# ======================
@app.route("/forward")
def forward():
    motors.forward()
    return jsonify({"action": "MOVING FORWARD"})


@app.route("/backward")
def backward():
    motors.backward()
    return jsonify({"action": "MOVING BACKWARD"})


@app.route("/left")
def left():
    motors.left()
    return jsonify({"action": "TURNING LEFT"})


@app.route("/right")
def right():
    motors.right()
    return jsonify({"action": "TURNING RIGHT"})


@app.route("/stop")
def stop():
    motors.stop()
    return jsonify({"action": "STOPPED"})


# ======================
# Speed Control (You forgot this route)
# ======================
@app.route("/speed", methods=["POST"])
def set_speed():
    data = request.get_json()
    speed = float(data.get("speed", 0.6))
    motors.set_speed(speed)
    return jsonify({"status": "Speed Updated"})

#Test LED
@app.route('/test_led')
def test_led():
    test_motor_pins_with_led()   # calls the function you just added
    return "✅ LED motor pin test completed! Check terminal for results."



# ======================
# Safety Shutdown
# ======================
def cleanup():
    motors.stop()

atexit.register(cleanup)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)