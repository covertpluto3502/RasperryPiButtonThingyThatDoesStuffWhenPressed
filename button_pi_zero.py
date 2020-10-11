# Code that runs in the Pi 0w
# Connect a button to GPIO 4 and ground
# Make sure that the Pi 0w is on the same network as the other Pi
# Make sure that the network is connected to the internet

import os
from signal import pause
try:
    from gpiozero import *

except ImportError:  # install packages if not already installed
    os.system("pip install gpiozero")
    from gpiozero import *

os.system("hostname button")  # sets the hostname of the button RPi
button_pin = 4  # set the pin of the button
button = Button(button_pin)


def send_request(hostname):
    os.system("wget " + hostname)


def send_signal():
    send_request("ip.of.your.pi") # rename this to pi address


button.when_released = send_signal
