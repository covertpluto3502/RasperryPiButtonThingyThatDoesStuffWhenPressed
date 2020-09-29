# Code that runs in the Pi 4
# Make sure that the Pi 4 is on the same network as the other Pi
# Make sure that the network is connected to the internet
# Change the code in when_activated to do what you want it to do
import os
try:
    from flask import *

except ImportError:  # install packages if not already installed
    os.system("pip install flask")
    from flask import *

app = Flask(__name__)
os.system("hostname control")


def when_activated():
    # code here will be executed if the other button is pressed
    os.system("./take_photo.sh")
    return 0


@app.route("/")
def index():
    when_activated()
    return "Successfully executed"
