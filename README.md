
To set up start on boot:
Pi4: sudo nano /etc/rc.local
At the penultimate line add: bash /home/pi/run.sh

Pi0: sudo nano /etc/rc.local
At the penultimate line add: python3 /home/pi/button_pi_zero.py
