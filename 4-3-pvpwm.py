import RPi.GPIO as gp
gp.setmode(gp.BCM)
gp.setwarnings(False)

gp.setup([6, 12, 5, 0, 1, 7, 11, 8], gp.OUT)
dac = [6, 12, 5, 0, 1, 7, 11, 8]
gp.setup(21, gp.OUT)
p = gp.PWM(21, 60)

p.start(0)
try:
    while True:
        n = int(input())
        p.ChangeDutyCycle(n)
finally:
    p.stop()
    gp.cleanup()
