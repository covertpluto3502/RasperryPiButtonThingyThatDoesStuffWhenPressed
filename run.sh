echo Starting server...
echo Server up at control.local:5000
sudo hostname control
export FLASK_APP=control_pi_4.py
sudo flask run --host=0.0.0.0
