from gpiozero import PWMOutputDevice
import config

# Left side driver
LEFT_R = PWMOutputDevice(config.LEFT_RPWM, frequency=config.PWM_FREQ)
LEFT_L = PWMOutputDevice(config.LEFT_LPWM, frequency=config.PWM_FREQ)

# Right side driver
RIGHT_R = PWMOutputDevice(config.RIGHT_RPWM, frequency=config.PWM_FREQ)
RIGHT_L = PWMOutputDevice(config.RIGHT_LPWM, frequency=config.PWM_FREQ)

speed = config.DEFAULT_SPEED


def set_speed(value):
    global speed
    speed = float(value)


def stop():
    LEFT_R.value = 0
    LEFT_L.value = 0
    RIGHT_R.value = 0
    RIGHT_L.value = 0


def forward():
    stop()
    LEFT_R.value = speed
    RIGHT_R.value = speed


def backward():
    stop()
    LEFT_L.value = speed
    RIGHT_L.value = speed


def left():
    stop()
    LEFT_L.value = speed
    RIGHT_R.value = speed


def right():
    stop()
    LEFT_R.value = speed
    RIGHT_L.value = speed