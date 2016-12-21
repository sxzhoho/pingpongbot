import RPi.GPIO as GPIO
import time

BIGBUTTON_PIN = 5
BLACKUPBUTTON_PIN = 3
BLACKDOWNBUTTON_PIN = 7
REDUPBUTTON_PIN = 8
REDDOWNBUTTON_PIN = 10

def pong_hardware_init():
    # set up board
    GPIO.setmode(GPIO.BOARD)
    # set up the pin directions
    GPIO.setup(BIGBUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BLACKUPBUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BLACKDOWNBUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(REDUPBUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(REDDOWNBUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_big_btn_press():
    if GPIO.input(BIGBUTTON_PIN) == 1:
        return False
    else:
        time.sleep(1)
        return True

def get_redup_btn_press():
    if GPIO.input(REDUPBUTTON_PIN) == 1:
        return False
    else:
        time.sleep(1)
        return True

def get_reddn_btn_press():
    if GPIO.input(REDDOWNBUTTON_PIN) == 1:
        return False
    else:
        time.sleep(1)
        return True

def get_blackup_btn_press():
    if GPIO.input(BLACKUPBUTTON_PIN) == 1:
        return False
    else:
        time.sleep(1)
        return True

def get_blackdn_btn_press():
    if GPIO.input(BLACKDOWNBUTTON_PIN) == 1:
        return False
    else:
        time.sleep(1)
        return True



