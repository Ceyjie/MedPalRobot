from gpiozero import PWMOutputDevice, DigitalOutputDevice
import config
import atexit

# =========================
# GLOBAL STATE
# =========================
current_speed = config.DEFAULT_SPEED

# =========================
# Motor Setup
# =========================

# Initialize PWM Pins (Speed)
left_rpwm = PWMOutputDevice(config.LEFT_RPWM, frequency=config.PWM_FREQ)
left_lpwm = PWMOutputDevice(config.LEFT_LPWM, frequency=config.PWM_FREQ)
right_rpwm = PWMOutputDevice(config.RIGHT_RPWM, frequency=config.PWM_FREQ)
right_lpwm = PWMOutputDevice(config.RIGHT_LPWM, frequency=config.PWM_FREQ)

# Initialize Digital Pins (Direction/Enable)
# We define these ONLY ONCE here to prevent GPIOPinInUse error
left_ren = DigitalOutputDevice(config.LEFT_REN)
left_len = DigitalOutputDevice(config.LEFT_LEN)
right_ren = DigitalOutputDevice(config.RIGHT_REN)
right_len = DigitalOutputDevice(config.RIGHT_LEN)

# =========================
# Enable/Disable Logic
# =========================

def enable_motors():
    left_ren.on()
    left_len.on()
    right_ren.on()
    right_len.on()
    print("✅ Hardware Pins Enabled")

def disable_motors():
    left_ren.off()
    left_len.off()
    right_ren.off()
    right_len.off()
    print("🛑 Hardware Pins Disabled")

# Run enable at startup
enable_motors()

# =========================
# Speed Control
# =========================

def set_speed(speed):
    global current_speed
    try:
        speed = float(speed)
        if speed < 0: speed = 0
        if speed > 1: speed = 1
        current_speed = speed
        print(f"⚡ Speed set to {current_speed}")
        return current_speed
    except:
        return current_speed

def get_speed():
    return current_speed

# =========================
# Movement Functions
# =========================

def stop():
    left_rpwm.value = 0
    left_lpwm.value = 0
    right_rpwm.value = 0
    right_lpwm.value = 0

def forward():
    stop()
    left_rpwm.value = current_speed
    right_rpwm.value = current_speed

def backward():
    stop()
    left_lpwm.value = current_speed
    right_lpwm.value = current_speed

def left():
    stop()
    left_lpwm.value = current_speed
    right_rpwm.value = current_speed

def right():
    stop()
    left_rpwm.value = current_speed
    right_lpwm.value = current_speed

def cleanup():
    stop()
    disable_motors()

atexit.register(cleanup)
