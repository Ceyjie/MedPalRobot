from flask import Flask, render_template, jsonify
import motor_control as motors
import atexit

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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

@app.route("/set_speed/<value>")
def set_speed(value):
    new_speed = motors.set_speed(float(value))
    return jsonify({"speed": new_speed})

@app.route("/get_speed")
def get_speed():
    return jsonify({"speed": motors.get_speed()})

def cleanup():
    motors.cleanup()

atexit.register(cleanup)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
