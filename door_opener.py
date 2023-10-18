from gpiozero import MotionSensor
from playsound import playsound

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("Movement Detected")
    playsound('music/seinfeld.mp3')
    pir.wait_for_no_motion()