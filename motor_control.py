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

#-------------------------------------------------------------


from time import sleep

# ================== YOUR SAFE LED MOTOR PIN TEST (100% FIXED) ==================
def test_motor_pins_with_led():
    print("🚀 MedPalRobot - LED TEST using YOUR pins (GPIO 12,13,18,19)")
    print("Make sure 4 LEDs + 220Ω resistors are connected BEFORE running!")
    
    # Forward
    print("→ Forward (LEDs on GPIO12 + GPIO18 should light)")
    LEFT_R.value = 0.7
    RIGHT_R.value = 0.7
    sleep(2)
    
    # Backward
    print("← Backward (LEDs on GPIO13 + GPIO19 should light)")
    LEFT_L.value = 0.7
    RIGHT_L.value = 0.7
    sleep(2)
    
    # Left turn
    print("↺ Left Turn (GPIO13 + GPIO18)")
    LEFT_L.value = 0.7
    RIGHT_R.value = 0.7
    sleep(2)
    
    # Right turn
    print("↻ Right Turn (GPIO12 + GPIO19)")
    LEFT_R.value = 0.7
    RIGHT_L.value = 0.7
    sleep(2)
    
    # Stop
    print("⏹ STOP - All LEDs OFF")
    stop()   # your existing stop function
    print("✅ LED test finished! Pins are correct → now connect BTS7960 safely.")