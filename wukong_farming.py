import vgamepad
import time

# Constants
resetCameraLoopCount = 1
gamepad = vgamepad.VX360Gamepad()

# Button mappings
UP = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
DOWN = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
LEFT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
RIGHT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

START = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START
BACK = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK
GUIDE = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE

LEFT_THUMB = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
RIGHT_THUMB = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
LEFT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
RIGHT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER

A = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
B = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B
X = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
Y = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y

# Functions to trigger actions
def left_trigger(value):
    gamepad.left_trigger_float(value)
    gamepad.update()

def right_trigger(value):
    gamepad.right_trigger_float(value)
    gamepad.update()

def left_joystick(x_value, y_value):
    gamepad.left_joystick_float(x_value, y_value)
    gamepad.update()

def right_joystick(x_value, y_value):
    gamepad.right_joystick_float(x_value, y_value)
    gamepad.update()

def press_button(button, duration):
    gamepad.press_button(button=button)
    gamepad.update()
    time.sleep(duration)
    gamepad.release_button(button=button)
    gamepad.update()

# Game-related actions
def return_shrine():
    print("Returning back to shrine")
    right_trigger(100)
    for _ in range(4):
        press_button(DOWN, 0.5)
    right_trigger(0)
    left_joystick(0, 0)

def call_rat_form():
    print("Becoming rat form")
    right_trigger(100)
    for _ in range(3):
        press_button(B, 0.3)
    right_trigger(0)

def call_rat_explosion():
    print("Calling Rat Explosion")
    right_trigger(100)
    for _ in range(3):
        press_button(B, 0.2)
    right_trigger(0)

def to_the_venue():
    print("Heading to the venue")
    left_joystick(-12000, -32700)
    time.sleep(2)
    press_button(A, 0.5)
    left_joystick(-12000, -32700)
    time.sleep(2)
    press_button(A, 0.5)
    left_joystick(31000, -32700)
    time.sleep(1.5)
    press_button(A, 0.5)
    left_joystick(31700, -32700)
    time.sleep(1.5)
    press_button(A, 0.5)
    left_joystick(31700, -12700)
    time.sleep(3.9)
    press_button(A, 0.5)
    left_joystick(0, 0)

def reset_camera():
    print("Resetting camera")
    right_trigger(100)
    time.sleep(1)
    right_trigger(0)
    time.sleep(1)
    right_trigger(100)
    time.sleep(1)
    right_trigger(0)
    time.sleep(5)
    press_button(B, 0.2)
    time.sleep(3)
    right_joystick(-31700, 0)
    time.sleep(0.514)
    right_joystick(0, 0)

def finish_one_run_farming():
    to_the_venue()
    time.sleep(1)
    call_rat_form()
    time.sleep(1)
    call_rat_explosion()
    time.sleep(1)
    call_rat_explosion()
    time.sleep(1)
    call_rat_explosion()
    time.sleep(1)
    return_shrine()
    time.sleep(1)
    return_shrine()
    time.sleep(1)
    return_shrine()
    time.sleep(1)

# Main function
def main():
    print("Wukong Farming Start!")
    time.sleep(3)
    press_button(A, 1)

    runtimes = 0
    while True:
        runtimes += 1 
        reset_camera()  # Every resetCameraLoopCount times, reset the camera
        for _ in range(resetCameraLoopCount):
            finish_one_run_farming()
            time.sleep(10)
        gamepad.reset()
        gamepad.update()
        print(f"Loop iteration {runtimes}")

if __name__ == "__main__":
    main()
