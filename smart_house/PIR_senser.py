from gpiozero import MotionSensor

pir = MotionSensor(18)

while True:
    if pir.motion_detected:
        print('Motion detected')

